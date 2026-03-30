# Source: https://crawlee.dev/js/docs/examples/capture-screenshot.md

# Capture a screenshot using Puppeteer

Copy for LLM

## Using Puppeteer directly[​](#using-puppeteer-directly "Direct link to Using Puppeteer directly")

tip

To run this example on the Apify Platform, select the `apify/actor-node-puppeteer-chrome` image for your Dockerfile.

This example captures a screenshot of a web page using `Puppeteer`. It would look almost exactly the same with `Playwright`.

* Page Screenshot
* Crawler Utils Screenshot

Using `page.screenshot()`:

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEtleVZhbHVlU3RvcmUsIGxhdW5jaFB1cHBldGVlciB9IGZyb20gJ2NyYXdsZWUnO1xcblxcbmNvbnN0IGtleVZhbHVlU3RvcmUgPSBhd2FpdCBLZXlWYWx1ZVN0b3JlLm9wZW4oKTtcXG5cXG5jb25zdCB1cmwgPSAnaHR0cHM6Ly9jcmF3bGVlLmRldic7XFxuLy8gU3RhcnQgYSBicm93c2VyXFxuY29uc3QgYnJvd3NlciA9IGF3YWl0IGxhdW5jaFB1cHBldGVlcigpO1xcblxcbi8vIE9wZW4gbmV3IHRhYiBpbiB0aGUgYnJvd3NlclxcbmNvbnN0IHBhZ2UgPSBhd2FpdCBicm93c2VyLm5ld1BhZ2UoKTtcXG5cXG4vLyBOYXZpZ2F0ZSB0byB0aGUgVVJMXFxuYXdhaXQgcGFnZS5nb3RvKHVybCk7XFxuXFxuLy8gQ2FwdHVyZSB0aGUgc2NyZWVuc2hvdFxcbmNvbnN0IHNjcmVlbnNob3QgPSBhd2FpdCBwYWdlLnNjcmVlbnNob3QoKTtcXG5cXG4vLyBTYXZlIHRoZSBzY3JlZW5zaG90IHRvIHRoZSBkZWZhdWx0IGtleS12YWx1ZSBzdG9yZVxcbmF3YWl0IGtleVZhbHVlU3RvcmUuc2V0VmFsdWUoJ215LWtleScsIHNjcmVlbnNob3QsIHsgY29udGVudFR5cGU6ICdpbWFnZS9wbmcnIH0pO1xcblxcbi8vIENsb3NlIFB1cHBldGVlclxcbmF3YWl0IGJyb3dzZXIuY2xvc2UoKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.hnB2LA3UbM_7PMJC08VHU7l3FPloqtx7pSzIDU4nO0I\&asrc=run_on_apify)

```
import { KeyValueStore, launchPuppeteer } from 'crawlee';

const keyValueStore = await KeyValueStore.open();

const url = 'https://crawlee.dev';
// Start a browser
const browser = await launchPuppeteer();

// Open new tab in the browser
const page = await browser.newPage();

// Navigate to the URL
await page.goto(url);

// Capture the screenshot
const screenshot = await page.screenshot();

// Save the screenshot to the default key-value store
await keyValueStore.setValue('my-key', screenshot, { contentType: 'image/png' });

// Close Puppeteer
await browser.close();
```

Using `utils.puppeteer.saveSnapshot()`:

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IGxhdW5jaFB1cHBldGVlciwgdXRpbHMgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCB1cmwgPSAnaHR0cDovL3d3dy5leGFtcGxlLmNvbS8nO1xcbi8vIFN0YXJ0IGEgYnJvd3NlclxcbmNvbnN0IGJyb3dzZXIgPSBhd2FpdCBsYXVuY2hQdXBwZXRlZXIoKTtcXG5cXG4vLyBPcGVuIG5ldyB0YWIgaW4gdGhlIGJyb3dzZXJcXG5jb25zdCBwYWdlID0gYXdhaXQgYnJvd3Nlci5uZXdQYWdlKCk7XFxuXFxuLy8gTmF2aWdhdGUgdG8gdGhlIFVSTFxcbmF3YWl0IHBhZ2UuZ290byh1cmwpO1xcblxcbi8vIENhcHR1cmUgdGhlIHNjcmVlbnNob3RcXG5hd2FpdCB1dGlscy5wdXBwZXRlZXIuc2F2ZVNuYXBzaG90KHBhZ2UsIHsga2V5OiAnbXkta2V5Jywgc2F2ZUh0bWw6IGZhbHNlIH0pO1xcblxcbi8vIENsb3NlIFB1cHBldGVlclxcbmF3YWl0IGJyb3dzZXIuY2xvc2UoKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.43Fi6LdMsWMLqVj33VMqbSZKfZFbgbNBSo11DKsWzto\&asrc=run_on_apify)

```
import { launchPuppeteer, utils } from 'crawlee';

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
```

## Using `PuppeteerCrawler`[​](#using-puppeteercrawler "Direct link to using-puppeteercrawler")

This example captures a screenshot of multiple web pages when using `PuppeteerCrawler`:

* Page Screenshot
* Crawler Utils Screenshot

Using `page.screenshot()`:

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIsIEtleVZhbHVlU3RvcmUgfSBmcm9tICdjcmF3bGVlJztcXG5cXG4vLyBDcmVhdGUgYSBQdXBwZXRlZXJDcmF3bGVyXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBQdXBwZXRlZXJDcmF3bGVyKHtcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCBwYWdlIH0pIHtcXG4gICAgICAgIC8vIENhcHR1cmUgdGhlIHNjcmVlbnNob3Qgd2l0aCBQdXBwZXRlZXJcXG4gICAgICAgIGNvbnN0IHNjcmVlbnNob3QgPSBhd2FpdCBwYWdlLnNjcmVlbnNob3QoKTtcXG4gICAgICAgIC8vIENvbnZlcnQgdGhlIFVSTCBpbnRvIGEgdmFsaWQga2V5XFxuICAgICAgICBjb25zdCBrZXkgPSByZXF1ZXN0LnVybC5yZXBsYWNlKC9bOi9dL2csICdfJyk7XFxuICAgICAgICAvLyBTYXZlIHRoZSBzY3JlZW5zaG90IHRvIHRoZSBkZWZhdWx0IGtleS12YWx1ZSBzdG9yZVxcbiAgICAgICAgYXdhaXQgS2V5VmFsdWVTdG9yZS5zZXRWYWx1ZShrZXksIHNjcmVlbnNob3QsIHsgY29udGVudFR5cGU6ICdpbWFnZS9wbmcnIH0pO1xcbiAgICB9LFxcbn0pO1xcblxcbmF3YWl0IGNyYXdsZXIuYWRkUmVxdWVzdHMoW1xcbiAgICB7IHVybDogJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0xJyB9LFxcbiAgICB7IHVybDogJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0yJyB9LFxcbiAgICB7IHVybDogJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0zJyB9LFxcbl0pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlclxcbmF3YWl0IGNyYXdsZXIucnVuKCk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6NDA5NiwidGltZW91dCI6MTgwfX0.dW6w_in8q5kLx6sM1tplVR0-n9GFpTMRCTjpsTyNhzQ\&asrc=run_on_apify)

```
import { PuppeteerCrawler, KeyValueStore } from 'crawlee';

// Create a PuppeteerCrawler
const crawler = new PuppeteerCrawler({
    async requestHandler({ request, page }) {
        // Capture the screenshot with Puppeteer
        const screenshot = await page.screenshot();
        // Convert the URL into a valid key
        const key = request.url.replace(/[:/]/g, '_');
        // Save the screenshot to the default key-value store
        await KeyValueStore.setValue(key, screenshot, { contentType: 'image/png' });
    },
});

await crawler.addRequests([
    { url: 'http://www.example.com/page-1' },
    { url: 'http://www.example.com/page-2' },
    { url: 'http://www.example.com/page-3' },
]);

// Run the crawler
await crawler.run();
```

Using the context-aware [`saveSnapshot()`](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#saveSnapshot) utility:

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIgfSBmcm9tICdjcmF3bGVlJztcXG5cXG4vLyBDcmVhdGUgYSBQdXBwZXRlZXJDcmF3bGVyXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBQdXBwZXRlZXJDcmF3bGVyKHtcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCBzYXZlU25hcHNob3QgfSkge1xcbiAgICAgICAgLy8gQ29udmVydCB0aGUgVVJMIGludG8gYSB2YWxpZCBrZXlcXG4gICAgICAgIGNvbnN0IGtleSA9IHJlcXVlc3QudXJsLnJlcGxhY2UoL1s6L10vZywgJ18nKTtcXG4gICAgICAgIC8vIENhcHR1cmUgdGhlIHNjcmVlbnNob3RcXG4gICAgICAgIGF3YWl0IHNhdmVTbmFwc2hvdCh7IGtleSwgc2F2ZUh0bWw6IGZhbHNlIH0pO1xcbiAgICB9LFxcbn0pO1xcblxcbmF3YWl0IGNyYXdsZXIuYWRkUmVxdWVzdHMoW1xcbiAgICB7IHVybDogJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0xJyB9LFxcbiAgICB7IHVybDogJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0yJyB9LFxcbiAgICB7IHVybDogJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0zJyB9LFxcbl0pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlclxcbmF3YWl0IGNyYXdsZXIucnVuKCk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6NDA5NiwidGltZW91dCI6MTgwfX0.0vtFUxFqfNHq5Y7EZ95YMfXOq2WqBpN0zprfavDk7mU\&asrc=run_on_apify)

```
import { PuppeteerCrawler } from 'crawlee';

// Create a PuppeteerCrawler
const crawler = new PuppeteerCrawler({
    async requestHandler({ request, saveSnapshot }) {
        // Convert the URL into a valid key
        const key = request.url.replace(/[:/]/g, '_');
        // Capture the screenshot
        await saveSnapshot({ key, saveHtml: false });
    },
});

await crawler.addRequests([
    { url: 'http://www.example.com/page-1' },
    { url: 'http://www.example.com/page-2' },
    { url: 'http://www.example.com/page-3' },
]);

// Run the crawler
await crawler.run();
```

To take full page screenshot using puppeteer we need to pass parameter `fullPage` as `true`in the `screenshot()`: `page.screenshot(fullPage: true)`

In both examples using `page.screenshot()`, a `key` variable is created based on the URL of the web page. This variable is used as the key when saving each screenshot into a key-value store.
