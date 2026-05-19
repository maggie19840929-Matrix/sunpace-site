import { readFileSync } from 'node:fs';

const SUNPACE_DATA_URL = new URL('../../data/pte-knowledge.sunpace.json', import.meta.url);
const DATA_URL = new URL('../../data/pte-knowledge.json', import.meta.url);
const GENERATED_DATA_URL = new URL('../../data/pte-knowledge.generated.json', import.meta.url);

const OUT_OF_SCOPE_ANSWER = [
  '这个问题先被 Sunny 学姐拦一下哈。',
  '我现在主要负责 SunPace 的 PTE 备考、题型训练、模考诊断、课程安排和留学备考相关问题。',
  '天气、八卦、闲聊和生活百科我就不展开啦，怕把你的备考节奏带跑偏。',
  '你可以直接问我：RA 怎么练、WFD 怎么提分、50 到 58 怎么规划，或者发分数单做诊断。'
].join('');

const GREETING_ANSWER = [
  '来啦，我是 Sunny，小昇学姐在线。',
  '我主要帮你看 PTE 备考、题型提分、模考诊断和 SunPace 课程安排。',
  '你可以直接把当前分数、目标分数和考试时间丢给我，我帮你先拆训练优先级。'
].join('');

const SCOPE_KEYWORDS = [
  'pte', 'pearson', 'academic', 'core', 'sunpace', '昇培', '小昇', 'sunny',
  'ra', 'rs', 'di', 'rl', 'asq', 'wfd', 'sst', 'fib', 'ro', 'we', 'swt', 'rts', 'sgd',
  'read aloud', 'repeat sentence', 'describe image', 'retell lecture', 'write from dictation',
  'summarize spoken text', 'summarize written text', 'write essay', 'response to situation',
  'summarize group discussion', 'group discussion',
  '口语', '听力', '阅读', '写作', '朗读', '复述', '听写', '小作文', '大作文', '小组讨论',
  '题型', '模考', '备考', '提分', '目标分', '当前分', '分数', '评分', '机经', '高频',
  '成绩单', '分数单', '小分', '供分', '权重', '题型权重', 'skills profile', 'score report',
  'speaking', 'listening', 'reading', 'writing', 'short speaking', 'extended speaking',
  'short writing', 'extended writing', 'open response', 'reproducing', 'comprehension',
  '50到58', '50 到 58', '50-58', '58到65', '58 到 65', '58-65', '目标58', '目标65', '目标79',
  '模板', '词汇', '语法', '发音', '流利度', '卡顿', '回读', '错题', '复盘',
  '考试', '考位', '报名', '换题', '课程', '集训', '顾问', '企业微信',
  '留学', '澳洲', '签证', '语言班', '英语考试'
];

const GREETING_PATTERNS = [
  /^(hi|hello|hey|你好|您好|哈喽|hello sunny|hi sunny|在吗|在不在|你是谁|你能做什么|你会什么)[\s!！。?？]*$/i
];

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

function isGreeting(question) {
  const q = String(question || '').trim();
  return GREETING_PATTERNS.some(pattern => pattern.test(q));
}

function isInSunnyScope(question) {
  const q = normalize(question);
  const tokens = q.match(/[a-z0-9]+/g) || [];
  return SCOPE_KEYWORDS.some(keyword => {
    if (/^[a-z0-9]{1,2}$/.test(keyword)) {
      return tokens.includes(keyword);
    }
    return q.includes(keyword);
  });
}

const BROAD_SCORE_SOURCE_IDS = [
  'sunpace-official-question-weighting-priorities',
  'sunpace-plan-diagnostic',
  'sunpace-study-five-step'
];

const FIRST_EXAM_SOURCE_IDS = [
  'sunpace-exam-registration',
  'sunpace-exam-booking-checklist',
  'sunpace-pte-test-types'
];

const WFD_SCORE_SOURCE_IDS = [
  'sunpace-listening-wfd-high-value',
  'sunpace-listening-wfd',
  'sunpace-listening-wfd-one-question-three-drills'
];

const SECTION_SCORE_SOURCE_IDS = {
  listening: [
    'sunpace-listening-wfd-high-value',
    'sunpace-listening-wfd',
    'sunpace-listening-sst',
    'sunpace-listening-fib-hiw-priority',
    'sunpace-extensive-listening'
  ],
  speaking: [
    'sunpace-speaking-overview-priority',
    'sunpace-speaking-ra',
    'sunpace-speaking-rs',
    'sunpace-speaking-di',
    'sunpace-speaking-rl'
  ],
  reading: [
    'sunpace-reading-time-priority',
    'sunpace-reading-fib',
    'sunpace-reading-ro'
  ],
  writing: [
    'sunpace-writing-score-priority-wfd',
    'sunpace-writing-swt',
    'sunpace-writing-we'
  ]
};

const TASK_SCORE_SOURCE_IDS = {
  listening_fib: [
    'sunpace-listening-fibl-vocab',
    'sunpace-listening-fib-hiw-priority'
  ],
  hiw: [
    'sunpace-listening-fib-hiw-priority',
    'sunpace-listening-priority-ladder'
  ],
  sst: [
    'sunpace-listening-sst',
    'sunpace-listening-sst-practice-order',
    'sunpace-listening-sst-content-words'
  ],
  swt: [
    'sunpace-writing-swt',
    'sunpace-writing-swt-skill',
    'sunpace-writing-swt-main-structure'
  ],
  we: [
    'sunpace-writing-we',
    'sunpace-writing-we-time-allocation',
    'sunpace-writing-we-template-needs-logic'
  ],
  fib: [
    'sunpace-reading-fib',
    'sunpace-reading-fib-word-form',
    'sunpace-reading-fib-collocations'
  ],
  ro: [
    'sunpace-reading-ro',
    'sunpace-reading-ro-step-by-step',
    'sunpace-reading-ro-target-accuracy'
  ],
  speaking_priority: [
    'sunpace-speaking-priority-ra-rs-di-rl',
    'sunpace-speaking-overview-priority',
    'sunpace-speaking-ra',
    'sunpace-speaking-rs',
    'sunpace-speaking-di',
    'sunpace-speaking-rl'
  ],
  di: [
    'sunpace-speaking-di',
    'sunpace-speaking-di-25-second-plan',
    'sunpace-speaking-di-finish-thirty-seconds'
  ],
  rl: [
    'sunpace-speaking-rl',
    'sunpace-speaking-rl-content-logic-reform',
    'sunpace-speaking-rl-answer-length'
  ],
  ra: [
    'sunpace-speaking-ra',
    'sunpace-speaking-ra-breakdown',
    'sunpace-speaking-ra-scoring-dimensions'
  ],
  rs: [
    'sunpace-speaking-rs',
    'sunpace-speaking-rs-chunking-method',
    'sunpace-speaking-rs-chunking-fluency'
  ]
};

const TASK_ROUTE_DEFINITIONS = [
  ['listening_fib', ['FIB', 'LFIB', 'FIBL'], ['听力 FIB', '听力填空', 'listening fib', 'fib listening']],
  ['hiw', ['HIW'], ['高亮错词', '错词高亮', 'highlight incorrect words']],
  ['sst', ['SST'], ['听力总结', 'summarize spoken text']],
  ['swt', ['SWT'], ['小作文', 'summarize written text']],
  ['we', ['WE'], ['大作文', 'write essay']],
  ['fib', ['FIB', 'FIBR', 'FIBRW'], ['阅读 FIB', '阅读填空', '完形填空', 'fill in the blanks']],
  ['ro', ['RO'], ['排序', 'reorder paragraphs']],
  ['di', ['DI'], ['describe image', '描述图片', '描述图', '图表题']],
  ['rl', ['RL'], ['retell lecture', '复述讲座', '重述讲座', '讲座复述']],
  ['ra', ['RA'], ['read aloud', '朗读']],
  ['rs', ['RS'], ['repeat sentence', '复述句子', '复述']]
];

const SPECIFIC_ROUTE_MARKERS = [
  'fib', 'fibr', 'swt', 'we', 'ra', 'rs', 'wfd', 'sst', 'ro', 'hiw', 'di', 'rl',
  '小作文', '大作文', '阅读', '听力', '口语', '写作', '词性', '填空', '复述', '朗读', '听写', '作文',
  '50', '58', '65', '79'
];

function hasScoreOrTrainingIntent(question) {
  return [
    '怎么提分', '如何提分', '如何提', '怎么提', '提分', '提升', '提高',
    '怎么练', '如何练', '训练', '练习', '备考', '怎么安排', '如何安排', '安排',
    '优先级', '顺序', '怎么拿分', '如何拿分', '拿分', '怎么得分', '如何得分',
    '得分', '怎么计分', '如何计分', '计分', '怎么记分', '如何记分', '记分',
    '怎么给分', '如何给分', '给分'
  ].some(term => question.includes(term));
}

function hasScoreImprovementIntent(question) {
  return [
    '怎么提分', '如何提分', '如何提', '怎么提', '提分', '提升分数', '提高分数'
  ].some(term => question.includes(term));
}

function hasAcronym(question, acronym) {
  const letters = acronym.split('').map(char => char.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('\\s*');
  return new RegExp(`(^|[^A-Za-z])${letters}($|[^A-Za-z])`, 'i').test(question);
}

function preferredEntries(knowledge, ids) {
  const byId = new Map(knowledge.map(entry => [String(entry.id || ''), entry]));
  return ids.map(id => byId.get(id)).filter(Boolean);
}

function isSpecificTaskQuestion(question) {
  const q = normalize(question);
  return SPECIFIC_ROUTE_MARKERS.some(marker => q.includes(marker));
}

function isFirstExamQuestion(question) {
  const q = normalize(question);
  if (!['第一次', '首次', '第一回', '刚开始', '剛開始'].some(term => q.includes(term))) {
    return false;
  }
  return ['pte', '考', '考试', '注意', '应该', '應該', '准备', '流程', '报名', '报考'].some(term => q.includes(term));
}

function isGeneralExamAttentionQuestion(question) {
  const q = normalize(question);
  if (isSpecificTaskQuestion(question)) return false;
  return [
    '注意什么', '注意点什么', '注意事項', '注意事项', '应该注意', '應該注意',
    '有什么要注意', '有什麼要注意'
  ].some(term => q.includes(term)) || (q.includes('考试') && q.includes('注意'));
}

function detectTaskScoreRoute(question) {
  const q = normalize(question);
  if (!hasScoreOrTrainingIntent(q)) return null;

  const speakingTaskCount = ['RA', 'RS', 'DI', 'RL'].filter(acronym => hasAcronym(question, acronym)).length;
  if (speakingTaskCount >= 2) return 'speaking_priority';

  for (const [taskKey, acronyms, aliases] of TASK_ROUTE_DEFINITIONS) {
    if (taskKey === 'listening_fib' && !['听力', 'listening', 'lfib', 'fibl'].some(term => q.includes(term))) {
      continue;
    }
    if (acronyms.some(acronym => hasAcronym(question, acronym))) return taskKey;
    if (aliases.some(alias => q.includes(normalize(alias)))) return taskKey;
  }
  return null;
}

function detectSectionScoreRoute(question) {
  const q = normalize(question);
  if (!hasScoreOrTrainingIntent(q)) return null;
  if (q.includes('听力') || q.includes('listening')) return 'listening';
  if (q.includes('口语') || q.includes('speaking')) return 'speaking';
  if (q.includes('阅读') || q.includes('reading')) return 'reading';
  if (q.includes('写作') || q.includes('writing')) return 'writing';
  return null;
}

function isBroadScoreImprovementQuestion(question) {
  const q = normalize(question);
  if (!q.includes('pte')) return false;
  if (!hasScoreImprovementIntent(q)) return false;
  return !SPECIFIC_ROUTE_MARKERS.some(marker => q.includes(marker));
}

function findRoutedMatches(question, knowledge) {
  if (isFirstExamQuestion(question) || isGeneralExamAttentionQuestion(question)) {
    return preferredEntries(knowledge, FIRST_EXAM_SOURCE_IDS);
  }

  const q = normalize(question);
  if ((q.includes('wfd') || q.includes('听写')) && hasScoreOrTrainingIntent(q)) {
    return preferredEntries(knowledge, WFD_SCORE_SOURCE_IDS);
  }

  const taskKey = detectTaskScoreRoute(question);
  if (taskKey) {
    const sourceIds = taskKey === 'fib' && q.includes('词性')
      ? ['sunpace-reading-fib-word-form', 'sunpace-reading-fib', 'sunpace-reading-fib-collocations']
      : TASK_SCORE_SOURCE_IDS[taskKey];
    return preferredEntries(knowledge, sourceIds || []);
  }

  const sectionKey = detectSectionScoreRoute(question);
  if (sectionKey) {
    return preferredEntries(knowledge, SECTION_SCORE_SOURCE_IDS[sectionKey] || []);
  }

  if (isBroadScoreImprovementQuestion(question)) {
    return preferredEntries(knowledge, BROAD_SCORE_SOURCE_IDS);
  }

  return [];
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

    if (q.includes(key)) {
      score += key.length > 2 ? Math.min(8, 2 + Math.floor(key.length / 3)) : 2;
    }
  }

  if (score > 0 && entry.sourceType === 'sunpace') score += 8;
  if (score > 0 && entry.sourceType === 'curated') score += 4;
  return score;
}

function findMatches(question, knowledge) {
  const routed = findRoutedMatches(question, knowledge);
  if (routed.length) return routed.slice(0, 3);

  const scored = knowledge
    .map(entry => ({ entry, score: scoreEntry(question, entry) }))
    .filter(item => item.score > 0)
    .sort((a, b) => b.score - a.score);

  const topScore = scored[0]?.score || 0;
  const relevant = topScore >= 8
    ? scored.filter(item => item.score >= Math.max(6, topScore * 0.75))
    : scored;

  const sunpace = relevant.filter(item => item.entry.sourceType === 'sunpace');
  if (sunpace.length) {
    return sunpace.slice(0, 2).map(item => item.entry);
  }

  const curated = relevant.filter(item => item.entry.sourceType === 'curated');
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

    if (isGreeting(question)) {
      return json({ answer: GREETING_ANSWER, sources: [{ id: 'sunny-greeting', title: 'Sunny 小昇' }] });
    }

    if (!isInSunnyScope(question)) {
      return json({ answer: OUT_OF_SCOPE_ANSWER, sources: [{ id: 'sunny-scope-gate', title: 'Sunny 只回答 PTE 相关问题' }] });
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
