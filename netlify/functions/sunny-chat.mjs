import { readFileSync } from 'node:fs';

const DATA_URL = new URL('../../data/pte-knowledge.json', import.meta.url);

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

function loadKnowledge() {
  try {
    return JSON.parse(readFileSync(DATA_URL, 'utf8'));
  } catch (error) {
    return [];
  }
}

function normalize(text) {
  return String(text || '').toLowerCase();
}

function scoreEntry(question, entry) {
  const q = normalize(question);
  const title = normalize(entry.title);
  let score = title && q.includes(title) ? 4 : 0;

  for (const keyword of entry.keywords || []) {
    const key = normalize(keyword);
    if (key && q.includes(key)) score += key.length > 2 ? 3 : 2;
  }

  return score;
}

function findMatches(question, knowledge) {
  return knowledge
    .map(entry => ({ entry, score: scoreEntry(question, entry) }))
    .filter(item => item.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, 2)
    .map(item => item.entry);
}

function buildAnswer(matches) {
  if (!matches.length) {
    return [
      '这个问题我在当前课程库里还没有找到完全匹配的条目。',
      '你可以先做一次 PTE 模考定位，再把问题拆到具体题型，比如 RA、RS、DI、WE 或 WFD。也可以添加企业微信，让顾问根据你的目标分数和考试时间给出学习节奏。'
    ].join('');
  }

  const answer = matches.map(item => item.answer).join(' ');
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

    const aiAnswer = await askOpenAIKnowledgeBase(question);
    if (aiAnswer) {
      return json({ answer: aiAnswer, sources: [{ id: 'openai-vector-store', title: 'SunPace PTE 课程知识库' }] });
    }

    const knowledge = loadKnowledge();
    const matches = findMatches(question, knowledge);
    return json({
      answer: buildAnswer(matches),
      sources: matches.map(item => ({ id: item.id, title: item.title }))
    });
  } catch (error) {
    return json({ error: 'Sunny is temporarily unavailable' }, 500);
  }
}
