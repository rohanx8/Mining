// Headless run of the in-app checks. Usage: node tools/run-checks.js [viewportWidth]
// Requires Playwright with Chromium available (require('playwright')).
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const width = Number(process.argv[2] || 375);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width, height: 900 } });
  const errors = [];
  page.on('pageerror', (e) => errors.push(e.message));
  await page.goto('file://' + path.resolve(__dirname, '..', 'index.html'));
  const results = await page.evaluate(() => runChecks());
  for (const r of results) console.log(`${r.ok ? 'PASS' : 'FAIL'}  ${r.name}  ->  ${r.detail}`);
  if (errors.length) console.log('Page errors:\n' + errors.join('\n'));
  await browser.close();
  const failed = results.filter((r) => !r.ok).length + errors.length;
  console.log(`\n${results.length - results.filter((r) => !r.ok).length}/${results.length} checks pass at ${width}px`);
  process.exit(failed ? 1 : 0);
})();
