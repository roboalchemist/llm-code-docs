# Source: https://crawlee.dev/js/docs/examples/crawl-all-links.md

# Crawl all links on a website

Copy for LLM

This example uses the `enqueueLinks()` method to add new links to the `RequestQueue` as the crawler navigates from page to page. This example can also be used to find all URLs on a domain by removing the `maxRequestsPerCrawl` option.

tip

If no options are given, by default the method will only add links that are under the same subdomain. This behavior can be controlled with the [`strategy`](https://crawlee.dev/js/api/core/interface/EnqueueLinksOptions.md#strategy) option. You can find more info about this option in the [`Crawl relative links`](https://crawlee.dev/js/docs/examples/crawl-relative-links.md) examples.

* Cheerio Crawler
* Puppeteer Crawler
* Playwright Crawler

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IENoZWVyaW9DcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBDaGVlcmlvQ3Jhd2xlcih7XFxuICAgIGFzeW5jIHJlcXVlc3RIYW5kbGVyKHsgcmVxdWVzdCwgZW5xdWV1ZUxpbmtzLCBsb2cgfSkge1xcbiAgICAgICAgbG9nLmluZm8ocmVxdWVzdC51cmwpO1xcbiAgICAgICAgLy8gQWRkIGFsbCBsaW5rcyBmcm9tIHBhZ2UgdG8gUmVxdWVzdFF1ZXVlXFxuICAgICAgICBhd2FpdCBlbnF1ZXVlTGlua3MoKTtcXG4gICAgfSxcXG4gICAgbWF4UmVxdWVzdHNQZXJDcmF3bDogMTAsIC8vIExpbWl0YXRpb24gZm9yIG9ubHkgMTAgcmVxdWVzdHMgKGRvIG5vdCB1c2UgaWYgeW91IHdhbnQgdG8gY3Jhd2wgYWxsIGxpbmtzKVxcbn0pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlciB3aXRoIGluaXRpYWwgcmVxdWVzdFxcbmF3YWl0IGNyYXdsZXIucnVuKFsnaHR0cHM6Ly9jcmF3bGVlLmRldiddKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.LBIV5tC8xatPLd7liUmYWtCnUL8bFQBt6Eq8fnylMkg\&asrc=run_on_apify)

```
import { CheerioCrawler } from 'crawlee';

const crawler = new CheerioCrawler({
    async requestHandler({ request, enqueueLinks, log }) {
        log.info(request.url);
        // Add all links from page to RequestQueue
        await enqueueLinks();
    },
    maxRequestsPerCrawl: 10, // Limitation for only 10 requests (do not use if you want to crawl all links)
});

// Run the crawler with initial request
await crawler.run(['https://crawlee.dev']);
```

tip

To run this example on the Apify Platform, select the `apify/actor-node-puppeteer-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCBjcmF3bGVyID0gbmV3IFB1cHBldGVlckNyYXdsZXIoe1xcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcih7IHJlcXVlc3QsIGVucXVldWVMaW5rcywgbG9nIH0pIHtcXG4gICAgICAgIGxvZy5pbmZvKHJlcXVlc3QudXJsKTtcXG4gICAgICAgIC8vIEFkZCBhbGwgbGlua3MgZnJvbSBwYWdlIHRvIFJlcXVlc3RRdWV1ZVxcbiAgICAgICAgYXdhaXQgZW5xdWV1ZUxpbmtzKCk7XFxuICAgIH0sXFxuICAgIG1heFJlcXVlc3RzUGVyQ3Jhd2w6IDEwLCAvLyBMaW1pdGF0aW9uIGZvciBvbmx5IDEwIHJlcXVlc3RzIChkbyBub3QgdXNlIGlmIHlvdSB3YW50IHRvIGNyYXdsIGFsbCBsaW5rcylcXG59KTtcXG5cXG4vLyBSdW4gdGhlIGNyYXdsZXIgd2l0aCBpbml0aWFsIHJlcXVlc3RcXG5hd2FpdCBjcmF3bGVyLnJ1bihbJ2h0dHBzOi8vY3Jhd2xlZS5kZXYnXSk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6NDA5NiwidGltZW91dCI6MTgwfX0.G2vsd_Fgpa50zBrg6m9S-dTzY4pzWTkAxqe6CzZtX5k\&asrc=run_on_apify)

```
import { PuppeteerCrawler } from 'crawlee';

const crawler = new PuppeteerCrawler({
    async requestHandler({ request, enqueueLinks, log }) {
        log.info(request.url);
        // Add all links from page to RequestQueue
        await enqueueLinks();
    },
    maxRequestsPerCrawl: 10, // Limitation for only 10 requests (do not use if you want to crawl all links)
});

// Run the crawler with initial request
await crawler.run(['https://crawlee.dev']);
```

tip

To run this example on the Apify Platform, select the `apify/actor-node-playwright-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/6i5QsHBMtm3hKph70?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFBsYXl3cmlnaHRDcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBQbGF5d3JpZ2h0Q3Jhd2xlcih7XFxuICAgIGFzeW5jIHJlcXVlc3RIYW5kbGVyKHsgcmVxdWVzdCwgZW5xdWV1ZUxpbmtzLCBsb2cgfSkge1xcbiAgICAgICAgbG9nLmluZm8ocmVxdWVzdC51cmwpO1xcbiAgICAgICAgLy8gQWRkIGFsbCBsaW5rcyBmcm9tIHBhZ2UgdG8gUmVxdWVzdFF1ZXVlXFxuICAgICAgICBhd2FpdCBlbnF1ZXVlTGlua3MoKTtcXG4gICAgfSxcXG4gICAgbWF4UmVxdWVzdHNQZXJDcmF3bDogMTAsIC8vIExpbWl0YXRpb24gZm9yIG9ubHkgMTAgcmVxdWVzdHMgKGRvIG5vdCB1c2UgaWYgeW91IHdhbnQgdG8gY3Jhd2wgYWxsIGxpbmtzKVxcbn0pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlciB3aXRoIGluaXRpYWwgcmVxdWVzdFxcbmF3YWl0IGNyYXdsZXIucnVuKFsnaHR0cHM6Ly9jcmF3bGVlLmRldiddKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.NdlPlyegNit9Kua8PQcBs0l9SELlDds4jvMbM0_tnhc\&asrc=run_on_apify)

```
import { PlaywrightCrawler } from 'crawlee';

const crawler = new PlaywrightCrawler({
    async requestHandler({ request, enqueueLinks, log }) {
        log.info(request.url);
        // Add all links from page to RequestQueue
        await enqueueLinks();
    },
    maxRequestsPerCrawl: 10, // Limitation for only 10 requests (do not use if you want to crawl all links)
});

// Run the crawler with initial request
await crawler.run(['https://crawlee.dev']);
```
