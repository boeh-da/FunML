const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // Navigate to your Reveal.js presentation with ?print-pdf appended
await page.goto('file:///Users/dboehnke/Workspaces/20240311_FunML/FunML/Vorlesung/12_Ausblick NN.slides.html?print-pdf', {waitUntil: 'networkidle2'});
  await page.waitForTimeout(10000);
  // Print the page as PDF
await page.pdf({ path: '12_Ausblick NN.pdf', format: 'A4', printBackground: true });

  await browser.close();
})();
