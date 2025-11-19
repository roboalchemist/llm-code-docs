# Source: https://docs.apify.com/sdk/js/docs/examples/crawl-relative-links.md

# Crawl a website with relative links

Copy for LLM

When crawling a website, you may encounter different types of links present that you may want to crawl. To facilitate the easy crawling of such links, we provide the `enqueueLinks()` method on the crawler context, which will automatically find links and add them to the crawler's [`RequestQueue`](https://docs.apify.com/sdk/js/sdk/js/reference/class/RequestQueue.md).

We provide 3 different strategies for crawling relative links:

* [All](https://crawlee.dev/api/core/enum/EnqueueStrategy#All)
  <!-- -->
  which will enqueue all links found, regardless of the domain they point to.
* [SameHostname](https://crawlee.dev/api/core/enum/EnqueueStrategy#SameHostname)
  <!-- -->
  which will enqueue all links found for the same hostname (regardless of any subdomains present).
* [SameSubdomain](https://crawlee.dev/api/core/enum/EnqueueStrategy#SameSubdomain)
  <!-- -->
  which will enqueue all links found that have the same subdomain and hostname. This is the default strategy.

note

For these examples, we are using the [`CheerioCrawler`](https://crawlee.dev/api/cheerio-crawler/class/CheerioCrawler), however the same method is available for both the [`PuppeteerCrawler`](https://crawlee.dev/api/puppeteer-crawler/class/PuppeteerCrawler) and [`PlaywrightCrawler`](https://crawlee.dev/api/playwright-crawler/class/PlaywrightCrawler), and you use it the exact same way.

* All Links
* Same Hostname
* Same Subdomain

Example domains

Any urls found will be matched by this strategy, even if they go off of the site you are currently crawling.

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IENoZWVyaW9DcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuYXdhaXQgQWN0b3IuaW5pdCgpO1xcblxcbmNvbnN0IGNyYXdsZXIgPSBuZXcgQ2hlZXJpb0NyYXdsZXIoe1xcbiAgICBtYXhSZXF1ZXN0c1BlckNyYXdsOiAxMCwgLy8gTGltaXRhdGlvbiBmb3Igb25seSAxMCByZXF1ZXN0cyAoZG8gbm90IHVzZSBpZiB5b3Ugd2FudCB0byBjcmF3bCBhbGwgbGlua3MpXFxuICAgIGFzeW5jIHJlcXVlc3RIYW5kbGVyKHsgcmVxdWVzdCwgZW5xdWV1ZUxpbmtzIH0pIHtcXG4gICAgICAgIGNvbnNvbGUubG9nKHJlcXVlc3QudXJsKTtcXG4gICAgICAgIGF3YWl0IGVucXVldWVMaW5rcyh7XFxuICAgICAgICAgICAgLy8gU2V0dGluZyB0aGUgc3RyYXRlZ3kgdG8gJ2FsbCcgd2lsbCBlbnF1ZXVlIGFsbCBsaW5rcyBmb3VuZFxcbiAgICAgICAgICAgIC8vIGhpZ2hsaWdodC1uZXh0LWxpbmVcXG4gICAgICAgICAgICBzdHJhdGVneTogJ2FsbCcsXFxuICAgICAgICB9KTtcXG4gICAgfSxcXG59KTtcXG5cXG4vLyBSdW4gdGhlIGNyYXdsZXJcXG5hd2FpdCBjcmF3bGVyLnJ1bihbJ2h0dHBzOi8vYXBpZnkuY29tLyddKTtcXG5cXG5hd2FpdCBBY3Rvci5leGl0KCk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.a1IFpzCtFyz6kXkEkdwjYb-WWnJaRH4hJxbbzFMcYfg\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { CheerioCrawler } from 'crawlee';

await Actor.init();

const crawler = new CheerioCrawler({
    maxRequestsPerCrawl: 10, // Limitation for only 10 requests (do not use if you want to crawl all links)
    async requestHandler({ request, enqueueLinks }) {
        console.log(request.url);
        await enqueueLinks({
            // Setting the strategy to 'all' will enqueue all links found
            strategy: 'all',
        });
    },
});

// Run the crawler
await crawler.run(['https://apify.com/']);

await Actor.exit();
```

Example domains

For a url of `https://example.com`, `enqueueLinks()` will match relative urls, urls that point to the same full domain or urls that point to any subdomain of the provided domain.

For instance, hyperlinks like `https://subdomain.example.com/some/path`, `https://example.com/some/path`, `/absolute/example` or `./relative/example` will all be matched by this strategy.

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IENoZWVyaW9DcmF3bGVyLCBFbnF1ZXVlU3RyYXRlZ3kgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5hd2FpdCBBY3Rvci5pbml0KCk7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBDaGVlcmlvQ3Jhd2xlcih7XFxuICAgIG1heFJlcXVlc3RzUGVyQ3Jhd2w6IDEwLCAvLyBMaW1pdGF0aW9uIGZvciBvbmx5IDEwIHJlcXVlc3RzIChkbyBub3QgdXNlIGlmIHlvdSB3YW50IHRvIGNyYXdsIGFsbCBsaW5rcylcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCBlbnF1ZXVlTGlua3MgfSkge1xcbiAgICAgICAgY29uc29sZS5sb2cocmVxdWVzdC51cmwpO1xcbiAgICAgICAgYXdhaXQgZW5xdWV1ZUxpbmtzKHtcXG4gICAgICAgICAgICAvLyBTZXR0aW5nIHRoZSBzdHJhdGVneSB0byAnc2FtZS1zdWJkb21haW4nIHdpbGwgZW5xdWV1ZSBhbGwgbGlua3MgZm91bmQgdGhhdCBhcmUgb24gdGhlIHNhbWUgaG9zdG5hbWVcXG4gICAgICAgICAgICAvLyBhcyByZXF1ZXN0LmxvYWRlZFVybCBvciByZXF1ZXN0LnVybFxcbiAgICAgICAgICAgIC8vIGhpZ2hsaWdodC1uZXh0LWxpbmVcXG4gICAgICAgICAgICBzdHJhdGVneTogRW5xdWV1ZVN0cmF0ZWd5LlNhbWVIb3N0bmFtZSxcXG4gICAgICAgICAgICAvLyBBbHRlcm5hdGl2ZWx5LCB5b3UgY2FuIHBhc3MgaW4gdGhlIHN0cmluZyAnc2FtZS1ob3N0bmFtZSdcXG4gICAgICAgICAgICAvLyBzdHJhdGVneTogJ3NhbWUtaG9zdG5hbWUnLFxcbiAgICAgICAgfSk7XFxuICAgIH0sXFxufSk7XFxuXFxuLy8gUnVuIHRoZSBjcmF3bGVyXFxuYXdhaXQgY3Jhd2xlci5ydW4oWydodHRwczovL2FwaWZ5LmNvbS8nXSk7XFxuXFxuYXdhaXQgQWN0b3IuZXhpdCgpO1xcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjEwMjQsInRpbWVvdXQiOjE4MH19.yF2AJFRXorzWRuCXhRGjM8nWXBFT585D7nwOkBPAPf0\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { CheerioCrawler, EnqueueStrategy } from 'crawlee';

await Actor.init();

const crawler = new CheerioCrawler({
    maxRequestsPerCrawl: 10, // Limitation for only 10 requests (do not use if you want to crawl all links)
    async requestHandler({ request, enqueueLinks }) {
        console.log(request.url);
        await enqueueLinks({
            // Setting the strategy to 'same-subdomain' will enqueue all links found that are on the same hostname
            // as request.loadedUrl or request.url
            strategy: EnqueueStrategy.SameHostname,
            // Alternatively, you can pass in the string 'same-hostname'
            // strategy: 'same-hostname',
        });
    },
});

// Run the crawler
await crawler.run(['https://apify.com/']);

await Actor.exit();
```

tip

This is the default strategy when calling `enqueueLinks()`, so you don't have to specify it.

Example domains

For a url of `https://subdomain.example.com`, `enqueueLinks()` will only match relative urls or urls that point to the same full domain.

For instance, hyperlinks like `https://subdomain.example.com/some/path`, `/absolute/example` or `./relative/example` will all be matched by this strategy, while `https://other-subdomain.example.com` or `https://otherexample.com` will not.

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IENoZWVyaW9DcmF3bGVyLCBFbnF1ZXVlU3RyYXRlZ3kgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5hd2FpdCBBY3Rvci5pbml0KCk7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBDaGVlcmlvQ3Jhd2xlcih7XFxuICAgIG1heFJlcXVlc3RzUGVyQ3Jhd2w6IDEwLCAvLyBMaW1pdGF0aW9uIGZvciBvbmx5IDEwIHJlcXVlc3RzIChkbyBub3QgdXNlIGlmIHlvdSB3YW50IHRvIGNyYXdsIGFsbCBsaW5rcylcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCBlbnF1ZXVlTGlua3MgfSkge1xcbiAgICAgICAgY29uc29sZS5sb2cocmVxdWVzdC51cmwpO1xcbiAgICAgICAgYXdhaXQgZW5xdWV1ZUxpbmtzKHtcXG4gICAgICAgICAgICAvLyBTZXR0aW5nIHRoZSBzdHJhdGVneSB0byAnc2FtZS1zdWJkb21haW4nIHdpbGwgZW5xdWV1ZSBhbGwgbGlua3MgZm91bmQgdGhhdCBhcmUgb24gdGhlIHNhbWUgc3ViZG9tYWluIGFuZCBob3N0bmFtZVxcbiAgICAgICAgICAgIC8vIGFzIHJlcXVlc3QubG9hZGVkVXJsIG9yIHJlcXVlc3QudXJsXFxuICAgICAgICAgICAgLy8gaGlnaGxpZ2h0LW5leHQtbGluZVxcbiAgICAgICAgICAgIHN0cmF0ZWd5OiBFbnF1ZXVlU3RyYXRlZ3kuU2FtZUhvc3RuYW1lLFxcbiAgICAgICAgICAgIC8vIEFsdGVybmF0aXZlbHksIHlvdSBjYW4gcGFzcyBpbiB0aGUgc3RyaW5nICdzYW1lLXN1YmRvbWFpbidcXG4gICAgICAgICAgICAvLyBzdHJhdGVneTogJ3NhbWUtc3ViZG9tYWluJyxcXG4gICAgICAgIH0pO1xcbiAgICB9LFxcbn0pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlclxcbmF3YWl0IGNyYXdsZXIucnVuKFsnaHR0cHM6Ly9hcGlmeS5jb20vJ10pO1xcblxcbmF3YWl0IEFjdG9yLmV4aXQoKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.dyU8vmMEV9LyeUOm-72BRE7THBxt7nDR7zN35H27ulw\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { CheerioCrawler, EnqueueStrategy } from 'crawlee';

await Actor.init();

const crawler = new CheerioCrawler({
    maxRequestsPerCrawl: 10, // Limitation for only 10 requests (do not use if you want to crawl all links)
    async requestHandler({ request, enqueueLinks }) {
        console.log(request.url);
        await enqueueLinks({
            // Setting the strategy to 'same-subdomain' will enqueue all links found that are on the same subdomain and hostname
            // as request.loadedUrl or request.url
            strategy: EnqueueStrategy.SameHostname,
            // Alternatively, you can pass in the string 'same-subdomain'
            // strategy: 'same-subdomain',
        });
    },
});

// Run the crawler
await crawler.run(['https://apify.com/']);

await Actor.exit();
```
