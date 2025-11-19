# Source: https://docs.apify.com/sdk/js/docs/examples/capture-screenshot.md

# Capture a screenshot using Puppeteer

Copy for LLM

tip

To run this example on the Apify Platform, select the `apify/actor-node-puppeteer-chrome` image for your Dockerfile.

This example captures a screenshot of a web page using `Puppeteer`. It would look almost exactly the same with `Playwright`.

* Page Screenshot
* Crawler Utils Screenshot

Using `page.screenshot()`:

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IGxhdW5jaFB1cHBldGVlciB9IGZyb20gJ2NyYXdsZWUnO1xcblxcbmF3YWl0IEFjdG9yLmluaXQoKTtcXG5cXG5jb25zdCB1cmwgPSAnaHR0cDovL3d3dy5leGFtcGxlLmNvbS8nO1xcbi8vIFN0YXJ0IGEgYnJvd3NlclxcbmNvbnN0IGJyb3dzZXIgPSBhd2FpdCBsYXVuY2hQdXBwZXRlZXIoKTtcXG5cXG4vLyBPcGVuIG5ldyB0YWIgaW4gdGhlIGJyb3dzZXJcXG5jb25zdCBwYWdlID0gYXdhaXQgYnJvd3Nlci5uZXdQYWdlKCk7XFxuXFxuLy8gTmF2aWdhdGUgdG8gdGhlIFVSTFxcbmF3YWl0IHBhZ2UuZ290byh1cmwpO1xcblxcbi8vIENhcHR1cmUgdGhlIHNjcmVlbnNob3RcXG5jb25zdCBzY3JlZW5zaG90ID0gYXdhaXQgcGFnZS5zY3JlZW5zaG90KCk7XFxuXFxuLy8gU2F2ZSB0aGUgc2NyZWVuc2hvdCB0byB0aGUgZGVmYXVsdCBrZXktdmFsdWUgc3RvcmVcXG5hd2FpdCBBY3Rvci5zZXRWYWx1ZSgnbXkta2V5Jywgc2NyZWVuc2hvdCwgeyBjb250ZW50VHlwZTogJ2ltYWdlL3BuZycgfSk7XFxuXFxuLy8gQ2xvc2UgUHVwcGV0ZWVyXFxuYXdhaXQgYnJvd3Nlci5jbG9zZSgpO1xcblxcbmF3YWl0IEFjdG9yLmV4aXQoKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.xy-Qn13nROyNEPEB6pUG8xQ1VfIjq56rsat4wKqhq9o\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { launchPuppeteer } from 'crawlee';

await Actor.init();

const url = 'http://www.example.com/';
// Start a browser
const browser = await launchPuppeteer();

// Open new tab in the browser
const page = await browser.newPage();

// Navigate to the URL
await page.goto(url);

// Capture the screenshot
const screenshot = await page.screenshot();

// Save the screenshot to the default key-value store
await Actor.setValue('my-key', screenshot, { contentType: 'image/png' });

// Close Puppeteer
await browser.close();

await Actor.exit();
```

Using `puppeteerUtils.saveSnapshot()`:

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IGxhdW5jaFB1cHBldGVlciwgdXRpbHMgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5hd2FpdCBBY3Rvci5pbml0KCk7XFxuXFxuY29uc3QgdXJsID0gJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vJztcXG4vLyBTdGFydCBhIGJyb3dzZXJcXG5jb25zdCBicm93c2VyID0gYXdhaXQgbGF1bmNoUHVwcGV0ZWVyKCk7XFxuXFxuLy8gT3BlbiBuZXcgdGFiIGluIHRoZSBicm93c2VyXFxuY29uc3QgcGFnZSA9IGF3YWl0IGJyb3dzZXIubmV3UGFnZSgpO1xcblxcbi8vIE5hdmlnYXRlIHRvIHRoZSBVUkxcXG5hd2FpdCBwYWdlLmdvdG8odXJsKTtcXG5cXG4vLyBDYXB0dXJlIHRoZSBzY3JlZW5zaG90XFxuYXdhaXQgdXRpbHMucHVwcGV0ZWVyLnNhdmVTbmFwc2hvdChwYWdlLCB7IGtleTogJ215LWtleScsIHNhdmVIdG1sOiBmYWxzZSB9KTtcXG5cXG4vLyBDbG9zZSBQdXBwZXRlZXJcXG5hd2FpdCBicm93c2VyLmNsb3NlKCk7XFxuXFxuYXdhaXQgQWN0b3IuZXhpdCgpO1xcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjQwOTYsInRpbWVvdXQiOjE4MH19.QSyAaQjtq2wJi2-pHooiFMBrLOELGoFYIBj8kQcDYtA\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { launchPuppeteer, utils } from 'crawlee';

await Actor.init();

const url = 'http://www.example.com/';
// Start a browser
const browser = await launchPuppeteer();

// Open new tab in the browser
const page = await browser.newPage();

// Navigate to the URL
await page.goto(url);

// Capture the screenshot
await utils.puppeteer.saveSnapshot(page, { key: 'my-key', saveHtml: false });

// Close Puppeteer
await browser.close();

await Actor.exit();
```

This example captures a screenshot of multiple web pages when using `PuppeteerCrawler`:

* Page Screenshot
* Crawler Utils Screenshot

Using `page.screenshot()`:

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5hd2FpdCBBY3Rvci5pbml0KCk7XFxuXFxuLy8gQ3JlYXRlIGEgUHVwcGV0ZWVyQ3Jhd2xlclxcbmNvbnN0IGNyYXdsZXIgPSBuZXcgUHVwcGV0ZWVyQ3Jhd2xlcih7XFxuICAgIGFzeW5jIHJlcXVlc3RIYW5kbGVyKHsgcmVxdWVzdCwgcGFnZSB9KSB7XFxuICAgICAgICAvLyBDYXB0dXJlIHRoZSBzY3JlZW5zaG90IHdpdGggUHVwcGV0ZWVyXFxuICAgICAgICBjb25zdCBzY3JlZW5zaG90ID0gYXdhaXQgcGFnZS5zY3JlZW5zaG90KCk7XFxuICAgICAgICAvLyBDb252ZXJ0IHRoZSBVUkwgaW50byBhIHZhbGlkIGtleVxcbiAgICAgICAgY29uc3Qga2V5ID0gcmVxdWVzdC51cmwucmVwbGFjZSgvWzovXS9nLCAnXycpO1xcbiAgICAgICAgLy8gU2F2ZSB0aGUgc2NyZWVuc2hvdCB0byB0aGUgZGVmYXVsdCBrZXktdmFsdWUgc3RvcmVcXG4gICAgICAgIGF3YWl0IEFjdG9yLnNldFZhbHVlKGtleSwgc2NyZWVuc2hvdCwgeyBjb250ZW50VHlwZTogJ2ltYWdlL3BuZycgfSk7XFxuICAgIH0sXFxufSk7XFxuXFxuLy8gUnVuIHRoZSBjcmF3bGVyXFxuYXdhaXQgY3Jhd2xlci5ydW4oW1xcbiAgICB7IHVybDogJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0xJyB9LFxcbiAgICB7IHVybDogJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0yJyB9LFxcbiAgICB7IHVybDogJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0zJyB9LFxcbl0pO1xcblxcbmF3YWl0IEFjdG9yLmV4aXQoKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.V_BcbfCWH__rcmGznaMSLm6R1wTtqF583QKH4Z3n5Uc\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { PuppeteerCrawler } from 'crawlee';

await Actor.init();

// Create a PuppeteerCrawler
const crawler = new PuppeteerCrawler({
    async requestHandler({ request, page }) {
        // Capture the screenshot with Puppeteer
        const screenshot = await page.screenshot();
        // Convert the URL into a valid key
        const key = request.url.replace(/[:/]/g, '_');
        // Save the screenshot to the default key-value store
        await Actor.setValue(key, screenshot, { contentType: 'image/png' });
    },
});

// Run the crawler
await crawler.run([
    { url: 'http://www.example.com/page-1' },
    { url: 'http://www.example.com/page-2' },
    { url: 'http://www.example.com/page-3' },
]);

await Actor.exit();
```

Using `puppeteerUtils.saveSnapshot()`:

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIsIHB1cHBldGVlclV0aWxzIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuYXdhaXQgQWN0b3IuaW5pdCgpO1xcblxcbi8vIENyZWF0ZSBhIFB1cHBldGVlckNyYXdsZXJcXG5jb25zdCBjcmF3bGVyID0gbmV3IFB1cHBldGVlckNyYXdsZXIoe1xcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcih7IHJlcXVlc3QsIHBhZ2UgfSkge1xcbiAgICAgICAgLy8gQ29udmVydCB0aGUgVVJMIGludG8gYSB2YWxpZCBrZXlcXG4gICAgICAgIGNvbnN0IGtleSA9IHJlcXVlc3QudXJsLnJlcGxhY2UoL1s6L10vZywgJ18nKTtcXG4gICAgICAgIC8vIENhcHR1cmUgdGhlIHNjcmVlbnNob3RcXG4gICAgICAgIGF3YWl0IHB1cHBldGVlclV0aWxzLnNhdmVTbmFwc2hvdChwYWdlLCB7IGtleSwgc2F2ZUh0bWw6IGZhbHNlIH0pO1xcbiAgICB9LFxcbn0pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlclxcbmF3YWl0IGNyYXdsZXIucnVuKFtcXG4gICAgeyB1cmw6ICdodHRwOi8vd3d3LmV4YW1wbGUuY29tL3BhZ2UtMScgfSxcXG4gICAgeyB1cmw6ICdodHRwOi8vd3d3LmV4YW1wbGUuY29tL3BhZ2UtMicgfSxcXG4gICAgeyB1cmw6ICdodHRwOi8vd3d3LmV4YW1wbGUuY29tL3BhZ2UtMycgfSxcXG5dKTtcXG5cXG5hd2FpdCBBY3Rvci5leGl0KCk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6NDA5NiwidGltZW91dCI6MTgwfX0.udR8araTvFL0crHf63ENyHe6LCZ4yd1J7FwSdJauc5M\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { PuppeteerCrawler, puppeteerUtils } from 'crawlee';

await Actor.init();

// Create a PuppeteerCrawler
const crawler = new PuppeteerCrawler({
    async requestHandler({ request, page }) {
        // Convert the URL into a valid key
        const key = request.url.replace(/[:/]/g, '_');
        // Capture the screenshot
        await puppeteerUtils.saveSnapshot(page, { key, saveHtml: false });
    },
});

// Run the crawler
await crawler.run([
    { url: 'http://www.example.com/page-1' },
    { url: 'http://www.example.com/page-2' },
    { url: 'http://www.example.com/page-3' },
]);

await Actor.exit();
```

In both examples using `page.screenshot()`, a `key` variable is created based on the URL of the web page. This variable is used as the key when saving each screenshot into a key-value store.
