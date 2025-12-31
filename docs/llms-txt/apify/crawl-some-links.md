# Source: https://docs.apify.com/sdk/js/docs/examples/crawl-some-links.md

# Crawl some links on a website

Copy for LLM

This [`CheerioCrawler`](https://crawlee.dev/api/cheerio-crawler/class/CheerioCrawler) example uses the [`pseudoUrls`](https://crawlee.dev/api/core/class/PseudoUrl) property in the [`enqueueLinks()`](https://crawlee.dev/api/cheerio-crawler/interface/CheerioRequestHandlerInputs#enqueueLinks) method to only add links to the [`RequestQueue`](https://docs.apify.com/sdk/js/sdk/js/reference/class/RequestQueue.md) queue if they match the specified regular expression.

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IENoZWVyaW9DcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuYXdhaXQgQWN0b3IuaW5pdCgpO1xcblxcbi8vIENyZWF0ZSBhIENoZWVyaW9DcmF3bGVyXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBDaGVlcmlvQ3Jhd2xlcih7XFxuICAgIC8vIExpbWl0cyB0aGUgY3Jhd2xlciB0byBvbmx5IDEwIHJlcXVlc3RzIChkbyBub3QgdXNlIGlmIHlvdSB3YW50IHRvIGNyYXdsIGFsbCBsaW5rcylcXG4gICAgbWF4UmVxdWVzdHNQZXJDcmF3bDogMTAsXFxuICAgIC8vIEZ1bmN0aW9uIGNhbGxlZCBmb3IgZWFjaCBVUkxcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCBlbnF1ZXVlTGlua3MgfSkge1xcbiAgICAgICAgY29uc29sZS5sb2cocmVxdWVzdC51cmwpO1xcbiAgICAgICAgLy8gQWRkIHNvbWUgbGlua3MgZnJvbSBwYWdlIHRvIHRoZSBjcmF3bGVyJ3MgUmVxdWVzdFF1ZXVlXFxuICAgICAgICBhd2FpdCBlbnF1ZXVlTGlua3Moe1xcbiAgICAgICAgICAgIHBzZXVkb1VybHM6IFsnaHR0cFtzP106Ly9hcGlmeS5jb20vWy4rXS9bLitdJ10sXFxuICAgICAgICB9KTtcXG4gICAgfSxcXG59KTtcXG5cXG4vLyBEZWZpbmUgdGhlIHN0YXJ0aW5nIFVSTCBhbmQgcnVuIHRoZSBjcmF3bGVyXFxuYXdhaXQgY3Jhd2xlci5ydW4oWydodHRwczovL2FwaWZ5LmNvbS9zdG9yZSddKTtcXG5cXG5hd2FpdCBBY3Rvci5leGl0KCk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.wHLH-CdKCylWDVcIRISOGWdcfzTZHeVAVlfiQhkzdko\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { CheerioCrawler } from 'crawlee';

await Actor.init();

// Create a CheerioCrawler
const crawler = new CheerioCrawler({
    // Limits the crawler to only 10 requests (do not use if you want to crawl all links)
    maxRequestsPerCrawl: 10,
    // Function called for each URL
    async requestHandler({ request, enqueueLinks }) {
        console.log(request.url);
        // Add some links from page to the crawler's RequestQueue
        await enqueueLinks({
            pseudoUrls: ['http[s?]://apify.com/[.+]/[.+]'],
        });
    },
});

// Define the starting URL and run the crawler
await crawler.run(['https://apify.com/store']);

await Actor.exit();
```
