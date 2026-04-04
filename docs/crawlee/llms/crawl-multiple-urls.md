# Source: https://crawlee.dev/js/docs/examples/crawl-multiple-urls.md

# Crawl multiple URLs

Copy for LLM

This example crawls the specified list of URLs.

* Cheerio Crawler
* Puppeteer Crawler
* Playwright Crawler

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IENoZWVyaW9DcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBDaGVlcmlvQ3Jhd2xlcih7XFxuICAgIC8vIEZ1bmN0aW9uIGNhbGxlZCBmb3IgZWFjaCBVUkxcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCAkLCBsb2cgfSkge1xcbiAgICAgICAgY29uc3QgdGl0bGUgPSAkKCd0aXRsZScpLnRleHQoKTtcXG4gICAgICAgIGxvZy5pbmZvKGBVUkw6ICR7cmVxdWVzdC51cmx9XFxcXG5USVRMRTogJHt0aXRsZX1gKTtcXG4gICAgfSxcXG59KTtcXG5cXG4vLyBSdW4gdGhlIGNyYXdsZXIgd2l0aCBpbml0aWFsIHJlcXVlc3RcXG5hd2FpdCBjcmF3bGVyLnJ1bihbJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0xJywgJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0yJywgJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0zJ10pO1xcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjEwMjQsInRpbWVvdXQiOjE4MH19.EkXGuY4BB9beeDa547KhHku8moogGGz0it_b02peucA\&asrc=run_on_apify)

```
import { CheerioCrawler } from 'crawlee';

const crawler = new CheerioCrawler({
    // Function called for each URL
    async requestHandler({ request, $, log }) {
        const title = $('title').text();
        log.info(`URL: ${request.url}\nTITLE: ${title}`);
    },
});

// Run the crawler with initial request
await crawler.run(['http://www.example.com/page-1', 'http://www.example.com/page-2', 'http://www.example.com/page-3']);
```

tip

To run this example on the Apify Platform, select the `apify/actor-node-puppeteer-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCBjcmF3bGVyID0gbmV3IFB1cHBldGVlckNyYXdsZXIoe1xcbiAgICAvLyBGdW5jdGlvbiBjYWxsZWQgZm9yIGVhY2ggVVJMXFxuICAgIGFzeW5jIHJlcXVlc3RIYW5kbGVyKHsgcmVxdWVzdCwgcGFnZSwgbG9nIH0pIHtcXG4gICAgICAgIGNvbnN0IHRpdGxlID0gYXdhaXQgcGFnZS50aXRsZSgpO1xcbiAgICAgICAgbG9nLmluZm8oYFVSTDogJHtyZXF1ZXN0LnVybH1cXFxcblRJVExFOiAke3RpdGxlfWApO1xcbiAgICB9LFxcbn0pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlciB3aXRoIGluaXRpYWwgcmVxdWVzdFxcbmF3YWl0IGNyYXdsZXIucnVuKFsnaHR0cDovL3d3dy5leGFtcGxlLmNvbS9wYWdlLTEnLCAnaHR0cDovL3d3dy5leGFtcGxlLmNvbS9wYWdlLTInLCAnaHR0cDovL3d3dy5leGFtcGxlLmNvbS9wYWdlLTMnXSk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6NDA5NiwidGltZW91dCI6MTgwfX0.giI3tJSfWG6oPGR2aMc4P1hv9q3DjQouI10GxYdUr5c\&asrc=run_on_apify)

```
import { PuppeteerCrawler } from 'crawlee';

const crawler = new PuppeteerCrawler({
    // Function called for each URL
    async requestHandler({ request, page, log }) {
        const title = await page.title();
        log.info(`URL: ${request.url}\nTITLE: ${title}`);
    },
});

// Run the crawler with initial request
await crawler.run(['http://www.example.com/page-1', 'http://www.example.com/page-2', 'http://www.example.com/page-3']);
```

tip

To run this example on the Apify Platform, select the `apify/actor-node-playwright-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/6i5QsHBMtm3hKph70?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFBsYXl3cmlnaHRDcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBQbGF5d3JpZ2h0Q3Jhd2xlcih7XFxuICAgIC8vIEZ1bmN0aW9uIGNhbGxlZCBmb3IgZWFjaCBVUkxcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCBwYWdlLCBsb2cgfSkge1xcbiAgICAgICAgY29uc3QgdGl0bGUgPSBhd2FpdCBwYWdlLnRpdGxlKCk7XFxuICAgICAgICBsb2cuaW5mbyhgVVJMOiAke3JlcXVlc3QudXJsfVxcXFxuVElUTEU6ICR7dGl0bGV9YCk7XFxuICAgIH0sXFxufSk7XFxuXFxuLy8gUnVuIHRoZSBjcmF3bGVyIHdpdGggaW5pdGlhbCByZXF1ZXN0XFxuYXdhaXQgY3Jhd2xlci5ydW4oWydodHRwOi8vd3d3LmV4YW1wbGUuY29tL3BhZ2UtMScsICdodHRwOi8vd3d3LmV4YW1wbGUuY29tL3BhZ2UtMicsICdodHRwOi8vd3d3LmV4YW1wbGUuY29tL3BhZ2UtMyddKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.usJ_mWQQRhnzUWTSjqEaplezGdxO-uK49YEErKaMke0\&asrc=run_on_apify)

```
import { PlaywrightCrawler } from 'crawlee';

const crawler = new PlaywrightCrawler({
    // Function called for each URL
    async requestHandler({ request, page, log }) {
        const title = await page.title();
        log.info(`URL: ${request.url}\nTITLE: ${title}`);
    },
});

// Run the crawler with initial request
await crawler.run(['http://www.example.com/page-1', 'http://www.example.com/page-2', 'http://www.example.com/page-3']);
```
