# Source: https://docs.apify.com/sdk/js/docs/examples/crawl-multiple-urls.md

# Crawl multiple URLs

Copy for LLM

This example crawls the specified list of URLs.

* Cheerio Crawler
* Puppeteer Crawler
* Playwright Crawler

Using `CheerioCrawler`:

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IENoZWVyaW9DcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuYXdhaXQgQWN0b3IuaW5pdCgpO1xcblxcbmNvbnN0IGNyYXdsZXIgPSBuZXcgQ2hlZXJpb0NyYXdsZXIoe1xcbiAgICAvLyBGdW5jdGlvbiBjYWxsZWQgZm9yIGVhY2ggVVJMXFxuICAgIGFzeW5jIHJlcXVlc3RIYW5kbGVyKHsgcmVxdWVzdCwgJCB9KSB7XFxuICAgICAgICBjb25zdCB0aXRsZSA9ICQoJ3RpdGxlJykudGV4dCgpO1xcbiAgICAgICAgY29uc29sZS5sb2coYFVSTDogJHtyZXF1ZXN0LnVybH1cXFxcblRJVExFOiAke3RpdGxlfWApO1xcbiAgICB9LFxcbn0pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlclxcbmF3YWl0IGNyYXdsZXIucnVuKFtcXG4gICAgJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0xJyxcXG4gICAgJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0yJyxcXG4gICAgJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20vcGFnZS0zJyxcXG5dKTtcXG5cXG5hd2FpdCBBY3Rvci5leGl0KCk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.CeiVEdnjPDfQ0i8PLiJLQhDJFF2dN9OtHDx7MiAmQD8\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { CheerioCrawler } from 'crawlee';

await Actor.init();

const crawler = new CheerioCrawler({
    // Function called for each URL
    async requestHandler({ request, $ }) {
        const title = $('title').text();
        console.log(`URL: ${request.url}\nTITLE: ${title}`);
    },
});

// Run the crawler
await crawler.run([
    'http://www.example.com/page-1',
    'http://www.example.com/page-2',
    'http://www.example.com/page-3',
]);

await Actor.exit();
```

Using `PuppeteerCrawler`:

tip

To run this example on the Apify Platform, select the `apify/actor-node-puppeteer-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5hd2FpdCBBY3Rvci5pbml0KCk7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBQdXBwZXRlZXJDcmF3bGVyKHtcXG4gICAgLy8gRnVuY3Rpb24gY2FsbGVkIGZvciBlYWNoIFVSTFxcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcih7IHJlcXVlc3QsIHBhZ2UgfSkge1xcbiAgICAgICAgY29uc3QgdGl0bGUgPSBhd2FpdCBwYWdlLnRpdGxlKCk7XFxuICAgICAgICBjb25zb2xlLmxvZyhgVVJMOiAke3JlcXVlc3QudXJsfVxcXFxuVElUTEU6ICR7dGl0bGV9YCk7XFxuICAgIH0sXFxufSk7XFxuXFxuLy8gUnVuIHRoZSBjcmF3bGVyXFxuYXdhaXQgY3Jhd2xlci5ydW4oW1xcbiAgICAnaHR0cDovL3d3dy5leGFtcGxlLmNvbS9wYWdlLTEnLFxcbiAgICAnaHR0cDovL3d3dy5leGFtcGxlLmNvbS9wYWdlLTInLFxcbiAgICAnaHR0cDovL3d3dy5leGFtcGxlLmNvbS9wYWdlLTMnLFxcbl0pO1xcblxcbmF3YWl0IEFjdG9yLmV4aXQoKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.N3_G0e276h-8f8FDQW4iLmyjhKEPItvUgrKXe3Rpxy8\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { PuppeteerCrawler } from 'crawlee';

await Actor.init();

const crawler = new PuppeteerCrawler({
    // Function called for each URL
    async requestHandler({ request, page }) {
        const title = await page.title();
        console.log(`URL: ${request.url}\nTITLE: ${title}`);
    },
});

// Run the crawler
await crawler.run([
    'http://www.example.com/page-1',
    'http://www.example.com/page-2',
    'http://www.example.com/page-3',
]);

await Actor.exit();
```

Using `PlaywrightCrawler`:

tip

To run this example on the Apify Platform, select the `apify/actor-node-playwright-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/6i5QsHBMtm3hKph70?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IFBsYXl3cmlnaHRDcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuYXdhaXQgQWN0b3IuaW5pdCgpO1xcblxcbmNvbnN0IGNyYXdsZXIgPSBuZXcgUGxheXdyaWdodENyYXdsZXIoe1xcbiAgICAvLyBGdW5jdGlvbiBjYWxsZWQgZm9yIGVhY2ggVVJMXFxuICAgIGFzeW5jIHJlcXVlc3RIYW5kbGVyKHsgcmVxdWVzdCwgcGFnZSB9KSB7XFxuICAgICAgICBjb25zdCB0aXRsZSA9IGF3YWl0IHBhZ2UudGl0bGUoKTtcXG4gICAgICAgIGNvbnNvbGUubG9nKGBVUkw6ICR7cmVxdWVzdC51cmx9XFxcXG5USVRMRTogJHt0aXRsZX1gKTtcXG4gICAgfSxcXG59KTtcXG5cXG4vLyBSdW4gdGhlIGNyYXdsZXJcXG5hd2FpdCBjcmF3bGVyLnJ1bihbXFxuICAgICdodHRwOi8vd3d3LmV4YW1wbGUuY29tL3BhZ2UtMScsXFxuICAgICdodHRwOi8vd3d3LmV4YW1wbGUuY29tL3BhZ2UtMicsXFxuICAgICdodHRwOi8vd3d3LmV4YW1wbGUuY29tL3BhZ2UtMycsXFxuXSk7XFxuXFxuYXdhaXQgQWN0b3IuZXhpdCgpO1xcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjQwOTYsInRpbWVvdXQiOjE4MH19.tFxeTZWttzvkWqmTccMmErP36zwOU4YG608H07ALpD0\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { PlaywrightCrawler } from 'crawlee';

await Actor.init();

const crawler = new PlaywrightCrawler({
    // Function called for each URL
    async requestHandler({ request, page }) {
        const title = await page.title();
        console.log(`URL: ${request.url}\nTITLE: ${title}`);
    },
});

// Run the crawler
await crawler.run([
    'http://www.example.com/page-1',
    'http://www.example.com/page-2',
    'http://www.example.com/page-3',
]);

await Actor.exit();
```
