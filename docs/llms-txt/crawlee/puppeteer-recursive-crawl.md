# Source: https://crawlee.dev/js/docs/examples/puppeteer-recursive-crawl.md

# Puppeteer recursive crawl

Copy for LLM

Run the following example to perform a recursive crawl of a website using [`PuppeteerCrawler`](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md).

tip

To run this example on the Apify Platform, select the `apify/actor-node-puppeteer-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCBjcmF3bGVyID0gbmV3IFB1cHBldGVlckNyYXdsZXIoe1xcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcih7IHJlcXVlc3QsIHBhZ2UsIGVucXVldWVMaW5rcywgbG9nIH0pIHtcXG4gICAgICAgIGNvbnN0IHRpdGxlID0gYXdhaXQgcGFnZS50aXRsZSgpO1xcbiAgICAgICAgbG9nLmluZm8oYFRpdGxlIG9mICR7cmVxdWVzdC51cmx9OiAke3RpdGxlfWApO1xcblxcbiAgICAgICAgYXdhaXQgZW5xdWV1ZUxpbmtzKHtcXG4gICAgICAgICAgICBnbG9iczogWydodHRwPyhzKTovL3d3dy5pYW5hLm9yZy8qKiddLFxcbiAgICAgICAgfSk7XFxuICAgIH0sXFxuICAgIG1heFJlcXVlc3RzUGVyQ3Jhd2w6IDEwLFxcbn0pO1xcblxcbmF3YWl0IGNyYXdsZXIuYWRkUmVxdWVzdHMoWydodHRwczovL3d3dy5pYW5hLm9yZy8nXSk7XFxuXFxuYXdhaXQgY3Jhd2xlci5ydW4oKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.WX9qygDqmffD0uvnNe4zaDatAVvSiCm1XcrSGPwvh6g\&asrc=run_on_apify)

```
import { PuppeteerCrawler } from 'crawlee';

const crawler = new PuppeteerCrawler({
    async requestHandler({ request, page, enqueueLinks, log }) {
        const title = await page.title();
        log.info(`Title of ${request.url}: ${title}`);

        await enqueueLinks({
            globs: ['http?(s)://www.iana.org/**'],
        });
    },
    maxRequestsPerCrawl: 10,
});

await crawler.addRequests(['https://www.iana.org/']);

await crawler.run();
```
