# Source: https://crawlee.dev/js/docs/examples/playwright-crawler-firefox.md

# Using Firefox browser with Playwright crawler

Copy for LLM

This example demonstrates how to use [`PlaywrightCrawler`](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md) with headless Firefox browser.

tip

To run this example on the Apify Platform, select the `apify/actor-node-playwright-firefox` image for your Dockerfile.

[Run on](https://console.apify.com/actors/6i5QsHBMtm3hKph70?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFBsYXl3cmlnaHRDcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuaW1wb3J0IHsgZmlyZWZveCB9IGZyb20gJ3BsYXl3cmlnaHQnO1xcblxcbi8vIENyZWF0ZSBhbiBpbnN0YW5jZSBvZiB0aGUgUGxheXdyaWdodENyYXdsZXIgY2xhc3MuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBQbGF5d3JpZ2h0Q3Jhd2xlcih7XFxuICAgIGxhdW5jaENvbnRleHQ6IHtcXG4gICAgICAgIC8vIFNldCB0aGUgRmlyZWZveCBicm93c2VyIHRvIGJlIHVzZWQgYnkgdGhlIGNyYXdsZXIuXFxuICAgICAgICAvLyBJZiBsYXVuY2hlciBvcHRpb24gaXMgbm90IHNwZWNpZmllZCBoZXJlLFxcbiAgICAgICAgLy8gZGVmYXVsdCBDaHJvbWl1bSBicm93c2VyIHdpbGwgYmUgdXNlZC5cXG4gICAgICAgIGxhdW5jaGVyOiBmaXJlZm94LFxcbiAgICB9LFxcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcih7IHJlcXVlc3QsIHBhZ2UsIGxvZyB9KSB7XFxuICAgICAgICBjb25zdCBwYWdlVGl0bGUgPSBhd2FpdCBwYWdlLnRpdGxlKCk7XFxuXFxuICAgICAgICBsb2cuaW5mbyhgVVJMOiAke3JlcXVlc3QubG9hZGVkVXJsfSB8IFBhZ2UgdGl0bGU6ICR7cGFnZVRpdGxlfWApO1xcbiAgICB9LFxcbn0pO1xcblxcbmF3YWl0IGNyYXdsZXIuYWRkUmVxdWVzdHMoWydodHRwczovL2V4YW1wbGUuY29tJ10pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlciBhbmQgd2FpdCBmb3IgaXQgdG8gZmluaXNoLlxcbmF3YWl0IGNyYXdsZXIucnVuKCk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6NDA5NiwidGltZW91dCI6MTgwfX0.vWp2zchK13fPXAQRaau5xNiHOhbCxKML5odaC7BwEDU\&asrc=run_on_apify)

```
import { PlaywrightCrawler } from 'crawlee';
import { firefox } from 'playwright';

// Create an instance of the PlaywrightCrawler class.
const crawler = new PlaywrightCrawler({
    launchContext: {
        // Set the Firefox browser to be used by the crawler.
        // If launcher option is not specified here,
        // default Chromium browser will be used.
        launcher: firefox,
    },
    async requestHandler({ request, page, log }) {
        const pageTitle = await page.title();

        log.info(`URL: ${request.loadedUrl} | Page title: ${pageTitle}`);
    },
});

await crawler.addRequests(['https://example.com']);

// Run the crawler and wait for it to finish.
await crawler.run();
```

To see a real-world example of how to use [`PlaywrightCrawler`](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md) in combination with [`RequestQueue`](https://crawlee.dev/js/api/core/class/RequestQueue.md) to recursively scrape the [Hacker News website](https://news.ycombinator.com) check out the [`Playwright crawler example`](https://crawlee.dev/js/docs/examples/playwright-crawler.md).
