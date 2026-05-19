import handler from '../netlify/functions/sunny-chat.mjs';

const cases = [
  ['first_exam', '第一次考 PTE 应该注意什么？', 'sunpace-exam-registration'],
  ['broad_score', 'PTE 如何提分？', 'sunpace-official-question-weighting-priorities'],
  ['listening_score', 'PTE 听力怎么提分？', 'sunpace-listening-wfd-high-value'],
  ['wfd_score', 'WFD 如何提分？', 'sunpace-listening-wfd-high-value'],
  ['reading_fib_word_form', '阅读 FIB 总是错词性怎么办？', 'sunpace-reading-fib-word-form'],
  ['swt_score', 'SWT 怎么提分？', 'sunpace-writing-swt'],
  ['speaking_score', 'PTE 口语怎么提分？', 'sunpace-speaking-overview-priority'],
  ['reading_score', 'PTE 阅读怎么提分？', 'sunpace-reading-time-priority'],
  ['writing_score', 'PTE 写作怎么提分？', 'sunpace-writing-score-priority-wfd']
];

async function ask(question) {
  const request = new Request('https://sunpace.cn/api/sunny-chat', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ question })
  });
  const response = await handler(request);
  return response.json();
}

let failures = 0;

for (const [name, question, expectedFirstSource] of cases) {
  const data = await ask(question);
  const sourceIds = Array.isArray(data.sources)
    ? data.sources.map(source => String(source.id || ''))
    : [];
  const actual = sourceIds[0] || '';
  const ok = actual === expectedFirstSource;
  if (!ok) failures += 1;
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}: ${actual || '-'} expected=${expectedFirstSource}`);
}

if (failures) {
  console.error(`sunny_chat_regression_failed failures=${failures} total=${cases.length}`);
  process.exit(1);
}

console.log(`sunny_chat_regression_ok total=${cases.length}`);
