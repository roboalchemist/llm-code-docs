# Source: https://crawlee.dev/js/docs/examples/crawl-relative-links.md

# Crawl a website with relative links

Copy for LLM

When crawling a website, you may encounter different types of links present that you may want to crawl. To facilitate the easy crawling of such links, we provide the `enqueueLinks()` method on the crawler context, which will automatically find links and add them to the crawler's [`RequestQueue`](https://crawlee.dev/js/api/core/class/RequestQueue.md).

We provide 3 different strategies for crawling relative links:

* [All (or the string "all")](https://crawlee.dev/js/api/core/enum/EnqueueStrategy.md#All) which will enqueue all links found, regardless of the domain they point to.
* [SameHostname (or the string "same-hostname")](https://crawlee.dev/js/api/core/enum/EnqueueStrategy.md#SameHostname) which will enqueue all links found for the same hostname. This is the default strategy.
* [SameDomain (or the string "same-domain")](https://crawlee.dev/js/api/core/enum/EnqueueStrategy.md#SameDomain) which will enqueue all links found that have the same domain name, including links from any possible subdomain.

note

For these examples, we are using the [`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md), however the same method is available for both the [`PuppeteerCrawler`](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md) and [`PlaywrightCrawler`](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md), and you use it the exact same way.

* All Links
* Same Hostname
* Same Subdomain

Example domains

Any urls found will be matched by this strategy, even if they go off of the site you are currently crawling.

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IENoZWVyaW9DcmF3bGVyLCBFbnF1ZXVlU3RyYXRlZ3kgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCBjcmF3bGVyID0gbmV3IENoZWVyaW9DcmF3bGVyKHtcXG4gICAgbWF4UmVxdWVzdHNQZXJDcmF3bDogMTAsIC8vIExpbWl0YXRpb24gZm9yIG9ubHkgMTAgcmVxdWVzdHMgKGRvIG5vdCB1c2UgaWYgeW91IHdhbnQgdG8gY3Jhd2wgYWxsIGxpbmtzKVxcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcih7IHJlcXVlc3QsIGVucXVldWVMaW5rcywgbG9nIH0pIHtcXG4gICAgICAgIGxvZy5pbmZvKHJlcXVlc3QudXJsKTtcXG4gICAgICAgIGF3YWl0IGVucXVldWVMaW5rcyh7XFxuICAgICAgICAgICAgLy8gU2V0dGluZyB0aGUgc3RyYXRlZ3kgdG8gJ2FsbCcgd2lsbCBlbnF1ZXVlIGFsbCBsaW5rcyBmb3VuZFxcbiAgICAgICAgICAgIC8vIGhpZ2hsaWdodC1uZXh0LWxpbmVcXG4gICAgICAgICAgICBzdHJhdGVneTogRW5xdWV1ZVN0cmF0ZWd5LkFsbCxcXG4gICAgICAgICAgICAvLyBBbHRlcm5hdGl2ZWx5LCB5b3UgY2FuIHBhc3MgaW4gdGhlIHN0cmluZyAnYWxsJ1xcbiAgICAgICAgICAgIC8vIHN0cmF0ZWd5OiAnYWxsJyxcXG4gICAgICAgIH0pO1xcbiAgICB9LFxcbn0pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlciB3aXRoIGluaXRpYWwgcmVxdWVzdFxcbmF3YWl0IGNyYXdsZXIucnVuKFsnaHR0cHM6Ly9jcmF3bGVlLmRldiddKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.zrKphqRNzrvQObV0GryliVYKQmeIFEkOtV_qBMeXvis\&asrc=run_on_apify)

```
import { CheerioCrawler, EnqueueStrategy } from 'crawlee';

const crawler = new CheerioCrawler({
    maxRequestsPerCrawl: 10, // Limitation for only 10 requests (do not use if you want to crawl all links)
    async requestHandler({ request, enqueueLinks, log }) {
        log.info(request.url);
        await enqueueLinks({
            // Setting the strategy to 'all' will enqueue all links found
            strategy: EnqueueStrategy.All,
            // Alternatively, you can pass in the string 'all'
            // strategy: 'all',
        });
    },
});

// Run the crawler with initial request
await crawler.run(['https://crawlee.dev']);
```

Example domains

For a url of `https://example.com`, `enqueueLinks()` will match relative urls and urls that point to the same hostname.

> This is the default strategy when calling `enqueueLinks()`, so you don't have to specify it.

For instance, hyperlinks like `https://example.com/some/path`, `/absolute/example` or `./relative/example` will all be matched by this strategy. But links to any subdomain like `https://subdomain.example.com/some/path` won't.

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IENoZWVyaW9DcmF3bGVyLCBFbnF1ZXVlU3RyYXRlZ3kgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCBjcmF3bGVyID0gbmV3IENoZWVyaW9DcmF3bGVyKHtcXG4gICAgbWF4UmVxdWVzdHNQZXJDcmF3bDogMTAsIC8vIExpbWl0YXRpb24gZm9yIG9ubHkgMTAgcmVxdWVzdHMgKGRvIG5vdCB1c2UgaWYgeW91IHdhbnQgdG8gY3Jhd2wgYWxsIGxpbmtzKVxcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcih7IHJlcXVlc3QsIGVucXVldWVMaW5rcywgbG9nIH0pIHtcXG4gICAgICAgIGxvZy5pbmZvKHJlcXVlc3QudXJsKTtcXG4gICAgICAgIGF3YWl0IGVucXVldWVMaW5rcyh7XFxuICAgICAgICAgICAgLy8gU2V0dGluZyB0aGUgc3RyYXRlZ3kgdG8gJ3NhbWUtaG9zdG5hbWUnIHdpbGwgZW5xdWV1ZSBhbGwgbGlua3MgZm91bmQgdGhhdCBhcmUgb24gdGhlXFxuICAgICAgICAgICAgLy8gc2FtZSBob3N0bmFtZSAoaW5jbHVkaW5nIHN1YmRvbWFpbikgYXMgcmVxdWVzdC5sb2FkZWRVcmwgb3IgcmVxdWVzdC51cmxcXG4gICAgICAgICAgICAvLyBoaWdobGlnaHQtbmV4dC1saW5lXFxuICAgICAgICAgICAgc3RyYXRlZ3k6IEVucXVldWVTdHJhdGVneS5TYW1lSG9zdG5hbWUsXFxuICAgICAgICAgICAgLy8gQWx0ZXJuYXRpdmVseSwgeW91IGNhbiBwYXNzIGluIHRoZSBzdHJpbmcgJ3NhbWUtaG9zdG5hbWUnXFxuICAgICAgICAgICAgLy8gc3RyYXRlZ3k6ICdzYW1lLWhvc3RuYW1lJyxcXG4gICAgICAgIH0pO1xcbiAgICB9LFxcbn0pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlciB3aXRoIGluaXRpYWwgcmVxdWVzdFxcbmF3YWl0IGNyYXdsZXIucnVuKFsnaHR0cHM6Ly9jcmF3bGVlLmRldiddKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.iCcYmWUvfNLGhjIu0mJ9cQwXfpdl2TIbAnyCU5XVdrw\&asrc=run_on_apify)

```
import { CheerioCrawler, EnqueueStrategy } from 'crawlee';

const crawler = new CheerioCrawler({
    maxRequestsPerCrawl: 10, // Limitation for only 10 requests (do not use if you want to crawl all links)
    async requestHandler({ request, enqueueLinks, log }) {
        log.info(request.url);
        await enqueueLinks({
            // Setting the strategy to 'same-hostname' will enqueue all links found that are on the
            // same hostname (including subdomain) as request.loadedUrl or request.url
            strategy: EnqueueStrategy.SameHostname,
            // Alternatively, you can pass in the string 'same-hostname'
            // strategy: 'same-hostname',
        });
    },
});

// Run the crawler with initial request
await crawler.run(['https://crawlee.dev']);
```

Example domains

For a url of `https://subdomain.example.com`, `enqueueLinks()` will match relative urls or urls that point to the same domain name, regardless of their subdomain.

For instance, hyperlinks like `https://subdomain.example.com/some/path`, `/absolute/example` or `./relative/example` will all be matched by this strategy, as well as links to other subdomains or to the naked domain, like `https://other-subdomain.example.com` or `https://example.com` will work too.

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IENoZWVyaW9DcmF3bGVyLCBFbnF1ZXVlU3RyYXRlZ3kgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCBjcmF3bGVyID0gbmV3IENoZWVyaW9DcmF3bGVyKHtcXG4gICAgbWF4UmVxdWVzdHNQZXJDcmF3bDogMTAsIC8vIExpbWl0YXRpb24gZm9yIG9ubHkgMTAgcmVxdWVzdHMgKGRvIG5vdCB1c2UgaWYgeW91IHdhbnQgdG8gY3Jhd2wgYWxsIGxpbmtzKVxcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcih7IHJlcXVlc3QsIGVucXVldWVMaW5rcywgbG9nIH0pIHtcXG4gICAgICAgIGxvZy5pbmZvKHJlcXVlc3QudXJsKTtcXG4gICAgICAgIGF3YWl0IGVucXVldWVMaW5rcyh7XFxuICAgICAgICAgICAgLy8gU2V0dGluZyB0aGUgc3RyYXRlZ3kgdG8gJ3NhbWUtZG9tYWluJyB3aWxsIGVucXVldWUgYWxsIGxpbmtzIGZvdW5kIHRoYXQgYXJlIG9uIHRoZVxcbiAgICAgICAgICAgIC8vIHNhbWUgaG9zdG5hbWUgYXMgcmVxdWVzdC5sb2FkZWRVcmwgb3IgcmVxdWVzdC51cmxcXG4gICAgICAgICAgICAvLyBoaWdobGlnaHQtbmV4dC1saW5lXFxuICAgICAgICAgICAgc3RyYXRlZ3k6IEVucXVldWVTdHJhdGVneS5TYW1lRG9tYWluLFxcbiAgICAgICAgICAgIC8vIEFsdGVybmF0aXZlbHksIHlvdSBjYW4gcGFzcyBpbiB0aGUgc3RyaW5nICdzYW1lLWRvbWFpbidcXG4gICAgICAgICAgICAvLyBzdHJhdGVneTogJ3NhbWUtZG9tYWluJyxcXG4gICAgICAgIH0pO1xcbiAgICB9LFxcbn0pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlciB3aXRoIGluaXRpYWwgcmVxdWVzdFxcbmF3YWl0IGNyYXdsZXIucnVuKFsnaHR0cHM6Ly9jcmF3bGVlLmRldiddKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.eW4ZGM7CltwTaGI0ye7ioJvou8nYvf6dW6LLwLtFWWA\&asrc=run_on_apify)

```
import { CheerioCrawler, EnqueueStrategy } from 'crawlee';

const crawler = new CheerioCrawler({
    maxRequestsPerCrawl: 10, // Limitation for only 10 requests (do not use if you want to crawl all links)
    async requestHandler({ request, enqueueLinks, log }) {
        log.info(request.url);
        await enqueueLinks({
            // Setting the strategy to 'same-domain' will enqueue all links found that are on the
            // same hostname as request.loadedUrl or request.url
            strategy: EnqueueStrategy.SameDomain,
            // Alternatively, you can pass in the string 'same-domain'
            // strategy: 'same-domain',
        });
    },
});

// Run the crawler with initial request
await crawler.run(['https://crawlee.dev']);
```
