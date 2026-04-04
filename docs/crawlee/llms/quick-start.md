# Source: https://crawlee.dev/js/docs/quick-start.md

# Quick Start

Copy for LLM

With this short tutorial you can start scraping with Crawlee in a minute or two. To learn in-depth how Crawlee works, read the [Introduction](https://crawlee.dev/js/docs/introduction.md), which is a comprehensive step-by-step guide for creating your first scraper.

## Choose your crawler[​](#choose-your-crawler "Direct link to Choose your crawler")

Crawlee comes with three main crawler classes: [`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md), [`PuppeteerCrawler`](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md) and [`PlaywrightCrawler`](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md). All classes share the same interface for maximum flexibility when switching between them.

### CheerioCrawler[​](#cheeriocrawler "Direct link to CheerioCrawler")

This is a plain HTTP crawler. It parses HTML using the [Cheerio](https://github.com/cheeriojs/cheerio) library and crawls the web using the specialized [got-scraping](https://github.com/apify/got-scraping) HTTP client which masks as a browser. It's very fast and efficient, but can't handle JavaScript rendering.

### PuppeteerCrawler[​](#puppeteercrawler "Direct link to PuppeteerCrawler")

This crawler uses a headless browser to crawl, controlled by the [Puppeteer](https://github.com/puppeteer/puppeteer) library. It can control Chromium or Chrome. Puppeteer is the de-facto standard in headless browser automation.

### PlaywrightCrawler[​](#playwrightcrawler "Direct link to PlaywrightCrawler")

[Playwright](https://github.com/microsoft/playwright) is a more powerful and full-featured successor to Puppeteer. It can control Chromium, Chrome, Firefox, Webkit and many other browsers. If you're not familiar with Puppeteer already, and you need a headless browser, go with Playwright.

before you start

Crawlee requires [Node.js 16 or later](https://nodejs.org/en/).

## Installation with Crawlee CLI[​](#installation-with-crawlee-cli "Direct link to Installation with Crawlee CLI")

The fastest way to try Crawlee out is to use the **Crawlee CLI** and choose the **Getting started example**. The CLI will install all the necessary dependencies and add boilerplate code for you to play with.

```
npx crawlee create my-crawler
```

After the installation is complete you can start the crawler like this:

```
cd my-crawler && npm start
```

## Manual installation[​](#manual-installation "Direct link to Manual installation")

You can add Crawlee to any Node.js project by running:

* CheerioCrawler
* PlaywrightCrawler
* PuppeteerCrawler

```
npm install crawlee
```

caution

`playwright` is not bundled with Crawlee to reduce install size and allow greater flexibility. You need to explicitly install it with NPM. 👇

```
npm install crawlee playwright
```

caution

`puppeteer` is not bundled with Crawlee to reduce install size and allow greater flexibility. You need to explicitly install it with NPM. 👇

```
npm install crawlee puppeteer
```

## Crawling[​](#crawling "Direct link to Crawling")

Run the following example to perform a recursive crawl of the Crawlee website using the selected crawler.

Don't forget about module imports

To run the example, add a `"type": "module"` clause into your `package.json` or copy it into a file with an `.mjs` suffix. This enables `import` statements in Node.js. See [Node.js docs](https://nodejs.org/dist/latest-v16.x/docs/api/esm.html#enabling) for more information.

* CheerioCrawler
* PlaywrightCrawler
* PuppeteerCrawler

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IENoZWVyaW9DcmF3bGVyLCBEYXRhc2V0IH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuLy8gQ2hlZXJpb0NyYXdsZXIgY3Jhd2xzIHRoZSB3ZWIgdXNpbmcgSFRUUCByZXF1ZXN0c1xcbi8vIGFuZCBwYXJzZXMgSFRNTCB1c2luZyB0aGUgQ2hlZXJpbyBsaWJyYXJ5LlxcbmNvbnN0IGNyYXdsZXIgPSBuZXcgQ2hlZXJpb0NyYXdsZXIoe1xcbiAgICAvLyBVc2UgdGhlIHJlcXVlc3RIYW5kbGVyIHRvIHByb2Nlc3MgZWFjaCBvZiB0aGUgY3Jhd2xlZCBwYWdlcy5cXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCAkLCBlbnF1ZXVlTGlua3MsIGxvZyB9KSB7XFxuICAgICAgICBjb25zdCB0aXRsZSA9ICQoJ3RpdGxlJykudGV4dCgpO1xcbiAgICAgICAgbG9nLmluZm8oYFRpdGxlIG9mICR7cmVxdWVzdC5sb2FkZWRVcmx9IGlzICcke3RpdGxlfSdgKTtcXG5cXG4gICAgICAgIC8vIFNhdmUgcmVzdWx0cyBhcyBKU09OIHRvIC4vc3RvcmFnZS9kYXRhc2V0cy9kZWZhdWx0XFxuICAgICAgICBhd2FpdCBEYXRhc2V0LnB1c2hEYXRhKHsgdGl0bGUsIHVybDogcmVxdWVzdC5sb2FkZWRVcmwgfSk7XFxuXFxuICAgICAgICAvLyBFeHRyYWN0IGxpbmtzIGZyb20gdGhlIGN1cnJlbnQgcGFnZVxcbiAgICAgICAgLy8gYW5kIGFkZCB0aGVtIHRvIHRoZSBjcmF3bGluZyBxdWV1ZS5cXG4gICAgICAgIGF3YWl0IGVucXVldWVMaW5rcygpO1xcbiAgICB9LFxcblxcbiAgICAvLyBMZXQncyBsaW1pdCBvdXIgY3Jhd2xzIHRvIG1ha2Ugb3VyIHRlc3RzIHNob3J0ZXIgYW5kIHNhZmVyLlxcbiAgICBtYXhSZXF1ZXN0c1BlckNyYXdsOiA1MCxcXG59KTtcXG5cXG4vLyBBZGQgZmlyc3QgVVJMIHRvIHRoZSBxdWV1ZSBhbmQgc3RhcnQgdGhlIGNyYXdsLlxcbmF3YWl0IGNyYXdsZXIucnVuKFsnaHR0cHM6Ly9jcmF3bGVlLmRldiddKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.Ja0vzMfKZoDTDX1L9bEJsVFrKUcp0sJyWJ46kbitQOs\&asrc=run_on_apify)

```
import { CheerioCrawler, Dataset } from 'crawlee';

// CheerioCrawler crawls the web using HTTP requests
// and parses HTML using the Cheerio library.
const crawler = new CheerioCrawler({
    // Use the requestHandler to process each of the crawled pages.
    async requestHandler({ request, $, enqueueLinks, log }) {
        const title = $('title').text();
        log.info(`Title of ${request.loadedUrl} is '${title}'`);

        // Save results as JSON to ./storage/datasets/default
        await Dataset.pushData({ title, url: request.loadedUrl });

        // Extract links from the current page
        // and add them to the crawling queue.
        await enqueueLinks();
    },

    // Let's limit our crawls to make our tests shorter and safer.
    maxRequestsPerCrawl: 50,
});

// Add first URL to the queue and start the crawl.
await crawler.run(['https://crawlee.dev']);
```

[Run on](https://console.apify.com/actors/6i5QsHBMtm3hKph70?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFBsYXl3cmlnaHRDcmF3bGVyLCBEYXRhc2V0IH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuLy8gUGxheXdyaWdodENyYXdsZXIgY3Jhd2xzIHRoZSB3ZWIgdXNpbmcgYSBoZWFkbGVzc1xcbi8vIGJyb3dzZXIgY29udHJvbGxlZCBieSB0aGUgUGxheXdyaWdodCBsaWJyYXJ5LlxcbmNvbnN0IGNyYXdsZXIgPSBuZXcgUGxheXdyaWdodENyYXdsZXIoe1xcbiAgICAvLyBVc2UgdGhlIHJlcXVlc3RIYW5kbGVyIHRvIHByb2Nlc3MgZWFjaCBvZiB0aGUgY3Jhd2xlZCBwYWdlcy5cXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCBwYWdlLCBlbnF1ZXVlTGlua3MsIGxvZyB9KSB7XFxuICAgICAgICBjb25zdCB0aXRsZSA9IGF3YWl0IHBhZ2UudGl0bGUoKTtcXG4gICAgICAgIGxvZy5pbmZvKGBUaXRsZSBvZiAke3JlcXVlc3QubG9hZGVkVXJsfSBpcyAnJHt0aXRsZX0nYCk7XFxuXFxuICAgICAgICAvLyBTYXZlIHJlc3VsdHMgYXMgSlNPTiB0byAuL3N0b3JhZ2UvZGF0YXNldHMvZGVmYXVsdFxcbiAgICAgICAgYXdhaXQgRGF0YXNldC5wdXNoRGF0YSh7IHRpdGxlLCB1cmw6IHJlcXVlc3QubG9hZGVkVXJsIH0pO1xcblxcbiAgICAgICAgLy8gRXh0cmFjdCBsaW5rcyBmcm9tIHRoZSBjdXJyZW50IHBhZ2VcXG4gICAgICAgIC8vIGFuZCBhZGQgdGhlbSB0byB0aGUgY3Jhd2xpbmcgcXVldWUuXFxuICAgICAgICBhd2FpdCBlbnF1ZXVlTGlua3MoKTtcXG4gICAgfSxcXG4gICAgLy8gVW5jb21tZW50IHRoaXMgb3B0aW9uIHRvIHNlZSB0aGUgYnJvd3NlciB3aW5kb3cuXFxuICAgIC8vIGhlYWRsZXNzOiBmYWxzZSxcXG5cXG4gICAgLy8gTGV0J3MgbGltaXQgb3VyIGNyYXdscyB0byBtYWtlIG91ciB0ZXN0cyBzaG9ydGVyIGFuZCBzYWZlci5cXG4gICAgbWF4UmVxdWVzdHNQZXJDcmF3bDogNTAsXFxufSk7XFxuXFxuLy8gQWRkIGZpcnN0IFVSTCB0byB0aGUgcXVldWUgYW5kIHN0YXJ0IHRoZSBjcmF3bC5cXG5hd2FpdCBjcmF3bGVyLnJ1bihbJ2h0dHBzOi8vY3Jhd2xlZS5kZXYnXSk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6NDA5NiwidGltZW91dCI6MTgwfX0.t_TCm8kwdGMajR-HxGyGZQ-N9vOJbcHUo8cgMhCec0E\&asrc=run_on_apify)

```
import { PlaywrightCrawler, Dataset } from 'crawlee';

// PlaywrightCrawler crawls the web using a headless
// browser controlled by the Playwright library.
const crawler = new PlaywrightCrawler({
    // Use the requestHandler to process each of the crawled pages.
    async requestHandler({ request, page, enqueueLinks, log }) {
        const title = await page.title();
        log.info(`Title of ${request.loadedUrl} is '${title}'`);

        // Save results as JSON to ./storage/datasets/default
        await Dataset.pushData({ title, url: request.loadedUrl });

        // Extract links from the current page
        // and add them to the crawling queue.
        await enqueueLinks();
    },
    // Uncomment this option to see the browser window.
    // headless: false,

    // Let's limit our crawls to make our tests shorter and safer.
    maxRequestsPerCrawl: 50,
});

// Add first URL to the queue and start the crawl.
await crawler.run(['https://crawlee.dev']);
```

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIsIERhdGFzZXQgfSBmcm9tICdjcmF3bGVlJztcXG5cXG4vLyBQdXBwZXRlZXJDcmF3bGVyIGNyYXdscyB0aGUgd2ViIHVzaW5nIGEgaGVhZGxlc3NcXG4vLyBicm93c2VyIGNvbnRyb2xsZWQgYnkgdGhlIFB1cHBldGVlciBsaWJyYXJ5LlxcbmNvbnN0IGNyYXdsZXIgPSBuZXcgUHVwcGV0ZWVyQ3Jhd2xlcih7XFxuICAgIC8vIFVzZSB0aGUgcmVxdWVzdEhhbmRsZXIgdG8gcHJvY2VzcyBlYWNoIG9mIHRoZSBjcmF3bGVkIHBhZ2VzLlxcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcih7IHJlcXVlc3QsIHBhZ2UsIGVucXVldWVMaW5rcywgbG9nIH0pIHtcXG4gICAgICAgIGNvbnN0IHRpdGxlID0gYXdhaXQgcGFnZS50aXRsZSgpO1xcbiAgICAgICAgbG9nLmluZm8oYFRpdGxlIG9mICR7cmVxdWVzdC5sb2FkZWRVcmx9IGlzICcke3RpdGxlfSdgKTtcXG5cXG4gICAgICAgIC8vIFNhdmUgcmVzdWx0cyBhcyBKU09OIHRvIC4vc3RvcmFnZS9kYXRhc2V0cy9kZWZhdWx0XFxuICAgICAgICBhd2FpdCBEYXRhc2V0LnB1c2hEYXRhKHsgdGl0bGUsIHVybDogcmVxdWVzdC5sb2FkZWRVcmwgfSk7XFxuXFxuICAgICAgICAvLyBFeHRyYWN0IGxpbmtzIGZyb20gdGhlIGN1cnJlbnQgcGFnZVxcbiAgICAgICAgLy8gYW5kIGFkZCB0aGVtIHRvIHRoZSBjcmF3bGluZyBxdWV1ZS5cXG4gICAgICAgIGF3YWl0IGVucXVldWVMaW5rcygpO1xcbiAgICB9LFxcbiAgICAvLyBVbmNvbW1lbnQgdGhpcyBvcHRpb24gdG8gc2VlIHRoZSBicm93c2VyIHdpbmRvdy5cXG4gICAgLy8gaGVhZGxlc3M6IGZhbHNlLFxcblxcbiAgICAvLyBMZXQncyBsaW1pdCBvdXIgY3Jhd2xzIHRvIG1ha2Ugb3VyIHRlc3RzIHNob3J0ZXIgYW5kIHNhZmVyLlxcbiAgICBtYXhSZXF1ZXN0c1BlckNyYXdsOiA1MCxcXG59KTtcXG5cXG4vLyBBZGQgZmlyc3QgVVJMIHRvIHRoZSBxdWV1ZSBhbmQgc3RhcnQgdGhlIGNyYXdsLlxcbmF3YWl0IGNyYXdsZXIucnVuKFsnaHR0cHM6Ly9jcmF3bGVlLmRldiddKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.r3-Jgz2GRxUEVxzBr5czC9lcH0ty_8aKkcd9XHHZryg\&asrc=run_on_apify)

```
import { PuppeteerCrawler, Dataset } from 'crawlee';

// PuppeteerCrawler crawls the web using a headless
// browser controlled by the Puppeteer library.
const crawler = new PuppeteerCrawler({
    // Use the requestHandler to process each of the crawled pages.
    async requestHandler({ request, page, enqueueLinks, log }) {
        const title = await page.title();
        log.info(`Title of ${request.loadedUrl} is '${title}'`);

        // Save results as JSON to ./storage/datasets/default
        await Dataset.pushData({ title, url: request.loadedUrl });

        // Extract links from the current page
        // and add them to the crawling queue.
        await enqueueLinks();
    },
    // Uncomment this option to see the browser window.
    // headless: false,

    // Let's limit our crawls to make our tests shorter and safer.
    maxRequestsPerCrawl: 50,
});

// Add first URL to the queue and start the crawl.
await crawler.run(['https://crawlee.dev']);
```

When you run the example, you will see Crawlee automating the data extraction process in your terminal.

```
INFO  CheerioCrawler: Starting the crawl
INFO  CheerioCrawler: Title of https://crawlee.dev/ is 'Crawlee · Build reliable crawlers. Fast. | Crawlee'
INFO  CheerioCrawler: Title of https://crawlee.dev/js/docs/examples is 'Examples | Crawlee'
INFO  CheerioCrawler: Title of https://crawlee.dev/js/docs/quick-start is 'Quick Start | Crawlee'
INFO  CheerioCrawler: Title of https://crawlee.dev/js/docs/guides is 'Guides | Crawlee'
```

### Running headful browsers[​](#running-headful-browsers "Direct link to Running headful browsers")

Browsers controlled by Puppeteer and Playwright run headless (without a visible window). You can switch to headful by adding the `headless: false` option to the crawlers' constructor. This is useful in the development phase when you want to see what's going on in the browser.

* PlaywrightCrawler
* PuppeteerCrawler

[Run on](https://console.apify.com/actors/6i5QsHBMtm3hKph70?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFBsYXl3cmlnaHRDcmF3bGVyLCBEYXRhc2V0IH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBQbGF5d3JpZ2h0Q3Jhd2xlcih7XFxuICAgIGFzeW5jIHJlcXVlc3RIYW5kbGVyKHsgcmVxdWVzdCwgcGFnZSwgZW5xdWV1ZUxpbmtzLCBsb2cgfSkge1xcbiAgICAgICAgY29uc3QgdGl0bGUgPSBhd2FpdCBwYWdlLnRpdGxlKCk7XFxuICAgICAgICBsb2cuaW5mbyhgVGl0bGUgb2YgJHtyZXF1ZXN0LmxvYWRlZFVybH0gaXMgJyR7dGl0bGV9J2ApO1xcbiAgICAgICAgYXdhaXQgRGF0YXNldC5wdXNoRGF0YSh7IHRpdGxlLCB1cmw6IHJlcXVlc3QubG9hZGVkVXJsIH0pO1xcbiAgICAgICAgYXdhaXQgZW5xdWV1ZUxpbmtzKCk7XFxuICAgIH0sXFxuICAgIC8vIFdoZW4geW91IHR1cm4gb2ZmIGhlYWRsZXNzIG1vZGUsIHRoZSBjcmF3bGVyXFxuICAgIC8vIHdpbGwgcnVuIHdpdGggYSB2aXNpYmxlIGJyb3dzZXIgd2luZG93LlxcbiAgICBoZWFkbGVzczogZmFsc2UsXFxuXFxuICAgIC8vIExldCdzIGxpbWl0IG91ciBjcmF3bHMgdG8gbWFrZSBvdXIgdGVzdHMgc2hvcnRlciBhbmQgc2FmZXIuXFxuICAgIG1heFJlcXVlc3RzUGVyQ3Jhd2w6IDUwLFxcbn0pO1xcblxcbi8vIEFkZCBmaXJzdCBVUkwgdG8gdGhlIHF1ZXVlIGFuZCBzdGFydCB0aGUgY3Jhd2wuXFxuYXdhaXQgY3Jhd2xlci5ydW4oWydodHRwczovL2NyYXdsZWUuZGV2J10pO1xcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjQwOTYsInRpbWVvdXQiOjE4MH19.hy0W1IDTCxm-B-7JSs_YOrqWnYAemKGg8vJVLIaigIg\&asrc=run_on_apify)

```
import { PlaywrightCrawler, Dataset } from 'crawlee';

const crawler = new PlaywrightCrawler({
    async requestHandler({ request, page, enqueueLinks, log }) {
        const title = await page.title();
        log.info(`Title of ${request.loadedUrl} is '${title}'`);
        await Dataset.pushData({ title, url: request.loadedUrl });
        await enqueueLinks();
    },
    // When you turn off headless mode, the crawler
    // will run with a visible browser window.
    headless: false,

    // Let's limit our crawls to make our tests shorter and safer.
    maxRequestsPerCrawl: 50,
});

// Add first URL to the queue and start the crawl.
await crawler.run(['https://crawlee.dev']);
```

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIsIERhdGFzZXQgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCBjcmF3bGVyID0gbmV3IFB1cHBldGVlckNyYXdsZXIoe1xcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcih7IHJlcXVlc3QsIHBhZ2UsIGVucXVldWVMaW5rcywgbG9nIH0pIHtcXG4gICAgICAgIGNvbnN0IHRpdGxlID0gYXdhaXQgcGFnZS50aXRsZSgpO1xcbiAgICAgICAgbG9nLmluZm8oYFRpdGxlIG9mICR7cmVxdWVzdC5sb2FkZWRVcmx9IGlzICcke3RpdGxlfSdgKTtcXG4gICAgICAgIGF3YWl0IERhdGFzZXQucHVzaERhdGEoeyB0aXRsZSwgdXJsOiByZXF1ZXN0LmxvYWRlZFVybCB9KTtcXG4gICAgICAgIGF3YWl0IGVucXVldWVMaW5rcygpO1xcbiAgICB9LFxcbiAgICAvLyBXaGVuIHlvdSB0dXJuIG9mZiBoZWFkbGVzcyBtb2RlLCB0aGUgY3Jhd2xlclxcbiAgICAvLyB3aWxsIHJ1biB3aXRoIGEgdmlzaWJsZSBicm93c2VyIHdpbmRvdy5cXG4gICAgaGVhZGxlc3M6IGZhbHNlLFxcblxcbiAgICAvLyBMZXQncyBsaW1pdCBvdXIgY3Jhd2xzIHRvIG1ha2Ugb3VyIHRlc3RzIHNob3J0ZXIgYW5kIHNhZmVyLlxcbiAgICBtYXhSZXF1ZXN0c1BlckNyYXdsOiA1MCxcXG59KTtcXG5cXG4vLyBBZGQgZmlyc3QgVVJMIHRvIHRoZSBxdWV1ZSBhbmQgc3RhcnQgdGhlIGNyYXdsLlxcbmF3YWl0IGNyYXdsZXIucnVuKFsnaHR0cHM6Ly9jcmF3bGVlLmRldiddKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.SeMW82sV8hdxSVLInwu1lVZjrCxNzASe8GlszF0s-W8\&asrc=run_on_apify)

```
import { PuppeteerCrawler, Dataset } from 'crawlee';

const crawler = new PuppeteerCrawler({
    async requestHandler({ request, page, enqueueLinks, log }) {
        const title = await page.title();
        log.info(`Title of ${request.loadedUrl} is '${title}'`);
        await Dataset.pushData({ title, url: request.loadedUrl });
        await enqueueLinks();
    },
    // When you turn off headless mode, the crawler
    // will run with a visible browser window.
    headless: false,

    // Let's limit our crawls to make our tests shorter and safer.
    maxRequestsPerCrawl: 50,
});

// Add first URL to the queue and start the crawl.
await crawler.run(['https://crawlee.dev']);
```

When you run the example code, you'll see an automated browser blaze through the Crawlee website.

note

For the sake of this show off, we've slowed down the crawler, but rest assured, it's blazing fast in real world usage.

![An image showing off Crawlee scraping the Crawlee website using Puppeteer/Playwright and Chromium](/img/chrome-scrape-light.gif)![An image showing off Crawlee scraping the Crawlee website using Puppeteer/Playwright and Chromium](/img/chrome-scrape-dark.gif)

## Results[​](#results "Direct link to Results")

Crawlee stores data to the `./storage` directory in your current working directory. The results of your crawl will be available under `./storage/datasets/default/*.json` as JSON files.

./storage/datasets/default/000000001.json

```
{
    "url": "https://crawlee.dev/",
    "title": "Crawlee · The scalable web crawling, scraping and automation library for JavaScript/Node.js | Crawlee"
}
```

tip

You can override the storage directory by setting the `CRAWLEE_STORAGE_DIR` environment variable.

## Examples and further reading[​](#examples-and-further-reading "Direct link to Examples and further reading")

You can find more examples showcasing various features of Crawlee in the [Examples](https://crawlee.dev/js/docs/examples.md) section of the documentation. To better understand Crawlee and its components you should read the [Introduction](https://crawlee.dev/js/docs/introduction.md) step-by-step guide.

**Related links**

* [Configuration](https://crawlee.dev/js/docs/guides/configuration.md)
* [Request storage](https://crawlee.dev/js/docs/guides/request-storage.md)
* [Result storage](https://crawlee.dev/js/docs/guides/result-storage.md)
