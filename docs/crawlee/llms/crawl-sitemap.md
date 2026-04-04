# Source: https://crawlee.dev/js/docs/examples/crawl-sitemap.md

# Crawl a sitemap

Copy for LLM

We will crawl sitemap which tells search engines which pages and file are important in the website, it also provides valuable information about these files. This example builds a sitemap crawler which downloads and crawls the URLs from a sitemap, by using the [`Sitemap`](https://crawlee.dev/js/api/utils/class/Sitemap.md) utility class provided by the [`@crawlee/utils`](https://crawlee.dev/js/api/utils.md) module.

* Cheerio Crawler
* Puppeteer Crawler
* Playwright Crawler

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IENoZWVyaW9DcmF3bGVyLCBTaXRlbWFwIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBDaGVlcmlvQ3Jhd2xlcih7XFxuICAgIC8vIEZ1bmN0aW9uIGNhbGxlZCBmb3IgZWFjaCBVUkxcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCBsb2cgfSkge1xcbiAgICAgICAgbG9nLmluZm8ocmVxdWVzdC51cmwpO1xcbiAgICB9LFxcbiAgICBtYXhSZXF1ZXN0c1BlckNyYXdsOiAxMCwgLy8gTGltaXRhdGlvbiBmb3Igb25seSAxMCByZXF1ZXN0cyAoZG8gbm90IHVzZSBpZiB5b3Ugd2FudCB0byBjcmF3bCBhIHNpdGVtYXApXFxufSk7XFxuXFxuY29uc3QgeyB1cmxzIH0gPSBhd2FpdCBTaXRlbWFwLmxvYWQoJ2h0dHBzOi8vY3Jhd2xlZS5kZXYvc2l0ZW1hcC54bWwnKTtcXG5cXG5hd2FpdCBjcmF3bGVyLmFkZFJlcXVlc3RzKHVybHMpO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlclxcbmF3YWl0IGNyYXdsZXIucnVuKCk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.tV8iOCFCHW8ymY2fNGesiSri1fq3k4YmUem3HRJ4EzA\&asrc=run_on_apify)

```
import { CheerioCrawler, Sitemap } from 'crawlee';

const crawler = new CheerioCrawler({
    // Function called for each URL
    async requestHandler({ request, log }) {
        log.info(request.url);
    },
    maxRequestsPerCrawl: 10, // Limitation for only 10 requests (do not use if you want to crawl a sitemap)
});

const { urls } = await Sitemap.load('https://crawlee.dev/sitemap.xml');

await crawler.addRequests(urls);

// Run the crawler
await crawler.run();
```

tip

To run this example on the Apify Platform, select the `apify/actor-node-puppeteer-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIsIFNpdGVtYXAgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCBjcmF3bGVyID0gbmV3IFB1cHBldGVlckNyYXdsZXIoe1xcbiAgICAvLyBGdW5jdGlvbiBjYWxsZWQgZm9yIGVhY2ggVVJMXFxuICAgIGFzeW5jIHJlcXVlc3RIYW5kbGVyKHsgcmVxdWVzdCwgbG9nIH0pIHtcXG4gICAgICAgIGxvZy5pbmZvKHJlcXVlc3QudXJsKTtcXG4gICAgfSxcXG4gICAgbWF4UmVxdWVzdHNQZXJDcmF3bDogMTAsIC8vIExpbWl0YXRpb24gZm9yIG9ubHkgMTAgcmVxdWVzdHMgKGRvIG5vdCB1c2UgaWYgeW91IHdhbnQgdG8gY3Jhd2wgYSBzaXRlbWFwKVxcbn0pO1xcblxcbmNvbnN0IHsgdXJscyB9ID0gYXdhaXQgU2l0ZW1hcC5sb2FkKCdodHRwczovL2NyYXdsZWUuZGV2L3NpdGVtYXAueG1sJyk7XFxuXFxuYXdhaXQgY3Jhd2xlci5hZGRSZXF1ZXN0cyh1cmxzKTtcXG5cXG4vLyBSdW4gdGhlIGNyYXdsZXJcXG5hd2FpdCBjcmF3bGVyLnJ1bigpO1xcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjQwOTYsInRpbWVvdXQiOjE4MH19.xqNohmh8_of2Vvb4ZItu__LG2i404uvrtO2NqNMAkls\&asrc=run_on_apify)

```
import { PuppeteerCrawler, Sitemap } from 'crawlee';

const crawler = new PuppeteerCrawler({
    // Function called for each URL
    async requestHandler({ request, log }) {
        log.info(request.url);
    },
    maxRequestsPerCrawl: 10, // Limitation for only 10 requests (do not use if you want to crawl a sitemap)
});

const { urls } = await Sitemap.load('https://crawlee.dev/sitemap.xml');

await crawler.addRequests(urls);

// Run the crawler
await crawler.run();
```

tip

To run this example on the Apify Platform, select the `apify/actor-node-playwright-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/6i5QsHBMtm3hKph70?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFBsYXl3cmlnaHRDcmF3bGVyLCBTaXRlbWFwIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBQbGF5d3JpZ2h0Q3Jhd2xlcih7XFxuICAgIC8vIEZ1bmN0aW9uIGNhbGxlZCBmb3IgZWFjaCBVUkxcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCBsb2cgfSkge1xcbiAgICAgICAgbG9nLmluZm8ocmVxdWVzdC51cmwpO1xcbiAgICB9LFxcbiAgICBtYXhSZXF1ZXN0c1BlckNyYXdsOiAxMCwgLy8gTGltaXRhdGlvbiBmb3Igb25seSAxMCByZXF1ZXN0cyAoZG8gbm90IHVzZSBpZiB5b3Ugd2FudCB0byBjcmF3bCBhIHNpdGVtYXApXFxufSk7XFxuXFxuY29uc3QgeyB1cmxzIH0gPSBhd2FpdCBTaXRlbWFwLmxvYWQoJ2h0dHBzOi8vY3Jhd2xlZS5kZXYvc2l0ZW1hcC54bWwnKTtcXG5cXG5hd2FpdCBjcmF3bGVyLmFkZFJlcXVlc3RzKHVybHMpO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlclxcbmF3YWl0IGNyYXdsZXIucnVuKCk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6NDA5NiwidGltZW91dCI6MTgwfX0.gYC10LbyMQ7K8r7Pc_WYu2KpbHLP6jmqOtfJvMxeIWM\&asrc=run_on_apify)

```
import { PlaywrightCrawler, Sitemap } from 'crawlee';

const crawler = new PlaywrightCrawler({
    // Function called for each URL
    async requestHandler({ request, log }) {
        log.info(request.url);
    },
    maxRequestsPerCrawl: 10, // Limitation for only 10 requests (do not use if you want to crawl a sitemap)
});

const { urls } = await Sitemap.load('https://crawlee.dev/sitemap.xml');

await crawler.addRequests(urls);

// Run the crawler
await crawler.run();
```
