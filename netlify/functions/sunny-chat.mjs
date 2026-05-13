import { readFileSync } from 'node:fs';

const SUNPACE_DATA_URL = new URL('../../data/pte-knowledge.sunpace.json', import.meta.url);
const DATA_URL = new URL('../../data/pte-knowledge.json', import.meta.url);
const GENERATED_DATA_URL = new URL('../../data/pte-knowledge.generated.json', import.meta.url);

export const config = {
  path: '/api/sunny-chat',
  rateLimit: {
    windowLimit: 6,
    windowSize: 60,
    aggregateBy: ['ip', 'domain']
  }
};

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8' }
  });
}

function readJson(url) {
  try {
    return JSON.parse(readFileSync(url, 'utf8'));
  } catch (error) {
    return [];
  }
}

function loadKnowledge() {
  const sunpace = readJson(SUNPACE_DATA_URL).map(entry => ({ ...entry, sourceType: 'sunpace' }));
  const curated = readJson(DATA_URL).map(entry => ({ ...entry, sourceType: 'curated' }));
  const generated = readJson(GENERATED_DATA_URL).map(entry => ({ ...entry, sourceType: 'generated' }));
  return [...sunpace, ...curated, ...generated];
}

function normalize(text) {
  return String(text || '').toLowerCase();
}

function scoreEntry(question, entry) {
  const q = normalize(question);
  const title = normalize(entry.title);
  const genericKeywords = new Set(['内容']);
  let score = 0;
  if (title && q.includes(title)) score += 4;

  for (const keyword of entry.keywords || []) {
    const key = normalize(keyword);
    if (!key) continue;
    if (genericKeywords.has(key)) continue;

    if (/^[a-z0-9]{1,2}$/.test(key)) {
      const tokens = q.match(/[a-z0-9]+/g) || [];
      if (tokens.includes(key)) score += 2;
      continue;
    }

    if (q.includes(key)) score += key.length > 2 ? 3 : 2;
  }

  if (score > 0 && entry.sourceType === 'sunpace') score += 8;
  if (score > 0 && entry.sourceType === 'curated') score += 4;
  return score;
}

function findMatches(question, knowledge) {
  const scored = knowledge
    .map(entry => ({ entry, score: scoreEntry(question, entry) }))
    .filter(item => item.score > 0)
    .sort((a, b) => b.score - a.score);

  const sunpace = scored.filter(item => item.entry.sourceType === 'sunpace');
  if (sunpace.length) {
    return sunpace.slice(0, 2).map(item => item.entry);
  }

  const curated = scored.filter(item => item.entry.sourceType === 'curated');
  if (curated.length) {
    return curated.slice(0, 2).map(item => item.entry);
  }

  const seen = new Set();
  const generated = [];
  for (const item of scored) {
    const key = item.entry.title || item.entry.id;
    if (seen.has(key)) continue;
    seen.add(key);
    generated.push(item.entry);
    if (generated.length >= 2) break;
  }
  return generated;
}

function hasHumanAnswer(matches) {
  return matches.some(item => item.sourceType === 'sunpace' || item.sourceType === 'curated');
}

function buildAnswer(matches) {
  if (!matches.length) {
    return [
      '这个问题我在当前课程库里还没有找到完全匹配的条目。',
      '你可以先做一次 PTE 模考定位，再把问题拆到具体题型，比如 RA、RS、DI、WE 或 WFD。也可以添加企业微信，让顾问根据你的目标分数和考试时间给出学习节奏。'
    ].join('');
  }

  const answer = matches.map(item => {
    if (item.sourceType === 'generated') {
      return [
        `我在 SunPace PTE 资料库里找到了与「${item.title}」相关的内容。`,
        '这部分资料已进入 Sunny 的自动索引，适合进一步咨询对应题型、模板、学习计划或备考方法。',
        '如果你告诉我当前分数、目标分数和考试时间，我可以先按资料主题帮你拆一个训练方向。'
      ].join('');
    }
    return item.answer;
  }).join(' ');
  return `${answer} 如果你愿意，可以继续告诉我你的当前分数、目标分数和考试日期，我会按时间帮你拆训练优先级。`;
}

function getOutputText(response) {
  if (response.output_text) return response.output_text;

  return (response.output || [])
    .flatMap(item => item.content || [])
    .map(part => part.text || '')
    .filter(Boolean)
    .join('\n')
    .trim();
}

async function askOpenAIKnowledgeBase(question) {
  const apiKey = Netlify.env.get('OPENAI_API_KEY');
  const vectorStoreId = Netlify.env.get('OPENAI_VECTOR_STORE_ID');
  const model = Netlify.env.get('OPENAI_MODEL') || 'gpt-5-mini';

  if (!apiKey || !vectorStoreId) return null;

  const response = await fetch('https://api.openai.com/v1/responses', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model,
      instructions: [
        '你是 SunPace 昇培教育的 PTE 助教 Sunny。',
        '只回答 PTE 备考、课程安排、模考诊断、线下活动和留学备考相关问题。',
        '优先依据文件检索结果回答；如果课程库没有相关信息，要明确说明，并建议添加企业微信咨询。',
        '回答要简洁、具体、适合官网访客，不要输出大段课程原文。'
      ].join('\n'),
      input: question,
      tools: [{
        type: 'file_search',
        vector_store_ids: [vectorStoreId]
      }],
      max_output_tokens: 500
    })
  });

  if (!response.ok) {
    throw new Error(`OpenAI request failed: ${response.status}`);
  }

  const data = await response.json();
  return getOutputText(data);
}

export default async function handler(request) {
  if (request.method !== 'POST') {
    return json({ error: 'Method not allowed' }, 405);
  }

  try {
    const body = await request.json();
    const question = String(body.question || '').trim().slice(0, 180);

    if (!question) {
      return json({ error: 'Question is required' }, 400);
    }

    const knowledge = loadKnowledge();
    const matches = findMatches(question, knowledge);
    if (hasHumanAnswer(matches)) {
      return json({
        answer: buildAnswer(matches),
        sources: matches.map(item => ({ id: item.id, title: item.title }))
      });
    }

    const aiAnswer = await askOpenAIKnowledgeBase(question);
    if (aiAnswer) {
      return json({ answer: aiAnswer, sources: [{ id: 'openai-vector-store', title: 'SunPace PTE 课程知识库' }] });
    }

    return json({
      answer: buildAnswer(matches),
      sources: matches.map(item => ({ id: item.id, title: item.title }))
    });
  } catch (error) {
    return json({ error: 'Sunny is temporarily unavailable' }, 500);
  }
}
