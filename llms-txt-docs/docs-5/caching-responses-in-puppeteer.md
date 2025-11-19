# Source: https://docs.apify.com/academy/node-js/caching-responses-in-puppeteer.md

# How to optimize Puppeteer by caching responses

**Learn why it is important for performance to cache responses in memory when intercepting requests in Puppeteer and how to implement it in your code.**

***

> In the latest version of Puppeteer, the request-interception function inconveniently disables the native cache and significantly slows down the crawler. Therefore, it's not recommended to follow the examples shown in this article unless you have a very specific use-case where the default browser cache is not enough (e.g. cashing over multiple scraper runs)

When running crawlers that go through a single website, each open page has to load all resources again. The problem is that each resource needs to be downloaded through the network, which can be slow and/or unstable (especially when proxies are used).

For this reason, in this article, we will take a look at how to use memory to cache responses in Puppeteer (only those that contain header **cache-control** with **max-age** above **0**).

In this example, we will use a scraper which goes through top stories on the CNN website and takes a screenshot of each opened page. The scraper is very slow right now because it waits till all network requests are finished and because the posts contain videos. If the scraper runs with disabled caching, these statistics will show at the end of the run:

![Bad run stats](/assets/images/bad-scraper-stats-b38622928fa3b188cae38d285750451e.png)

As you can see, we used 177MB of traffic for 10 posts (that is how many posts are in the top-stories column) and 1 main page.

From the screenshot above, it's clear that most of the traffic is coming from script files (124MB) and documents (22.8MB). For this kind of situation, it's always good to check if the content of the page is cache-able. You can do that using Chromes Developer tools.

## Understanding and reproducing the issue

If we go to the CNN website, open up the tools and go to the **Network** tab, we will find an option to disable caching.

![Disabling cache in the Network tab](/assets/images/cnn-network-tab-0ca18e39872e758ab7f60f2cd601e0f1.png)

Once caching is disabled, we can take a look at how much data is transferred when we open the page. This is visible at the bottom of the developer tools.

![5.3MB of data transferred](/assets/images/slow-no-cache-0681379c53774a230ff67f2ec4704f7c.png)

If we uncheck the disable-cache checkbox and refresh the page, we will see how much data we can save by caching responses.

![642KB of data transferred](/assets/images/fast-with-cache-1a683d4e3a74468186b8d004c5fba276.png)

By comparison, the data transfer appears to be reduced by 88%!

## Solving the problem by creating an in-memory cache

We can now emulate this and cache responses in Puppeteer. All we have to do is to check, when the response is received, whether it contains the **cache-control** header, and whether it's set with a **max-age** higher than **0**. If so, then we'll save the headers, URL, and body of the response to memory, and on the next request check if the requested URL is already stored in the cache.

The code will look like this:


```
// On top of your code
const cache = {};

// The code below should go between newPage function and goto function

await page.setRequestInterception(true);

page.on('request', async (request) => {
    const url = request.url();
    if (cache[url] && cache[url].expires > Date.now()) {
        await request.respond(cache[url]);
        return;
    }
    request.continue();
});

page.on('response', async (response) => {
    const url = response.url();
    const headers = response.headers();
    const cacheControl = headers['cache-control'] || '';
    const maxAgeMatch = cacheControl.match(/max-age=(\d+)/);
    const maxAge = maxAgeMatch && maxAgeMatch.length > 1 ? parseInt(maxAgeMatch[1], 10) : 0;
    if (maxAge) {
        if (cache[url] && cache[url].expires > Date.now()) return;

        let buffer;
        try {
            buffer = await response.buffer();
        } catch (error) {
            // some responses do not contain buffer and do not need to be catched
            return;
        }

        cache[url] = {
            status: response.status(),
            headers: response.headers(),
            body: buffer,
            expires: Date.now() + (maxAge * 1000),
        };
    }
});
```


> If the code above looks completely foreign to you, we recommending going through our free https://docs.apify.com/academy/puppeteer-playwright.md.

After implementing this code, we can run the scraper again.

![Good run results](/assets/images/good-run-results-38dc359a0a3b4cdf6b7611255218d234.png)

Looking at the statistics, caching responses in Puppeteer brought the traffic down from 177MB to 13.4MB, which is a reduction of data transfer by 92%. The related screenshots can be found https://my.apify.com/storage/key-value/iWQ3mQE2XsLA2eErL.

It did not speed up the crawler, but that is only because the crawler is set to wait until the network is nearly idle, and CNN has a lot of tracking and analytics scripts that keep the network busy.

## Implementation in Crawlee

Since most of you are likely using https://crawlee.dev, here is what response caching would look like using `PuppeteerCrawler`:

https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IERhdGFzZXQsIFB1cHBldGVlckNyYXdsZXIgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCBjYWNoZSA9IHt9O1xcblxcbmNvbnN0IGNyYXdsZXIgPSBuZXcgUHVwcGV0ZWVyQ3Jhd2xlcih7XFxuICAgIHByZU5hdmlnYXRpb25Ib29rczogW2FzeW5jICh7IHBhZ2UgfSkgPT4ge1xcbiAgICAgICAgYXdhaXQgcGFnZS5zZXRSZXF1ZXN0SW50ZXJjZXB0aW9uKHRydWUpO1xcblxcbiAgICAgICAgcGFnZS5vbigncmVxdWVzdCcsIGFzeW5jIChyZXF1ZXN0KSA9PiB7XFxuICAgICAgICAgICAgY29uc3QgdXJsID0gcmVxdWVzdC51cmwoKTtcXG4gICAgICAgICAgICBpZiAoY2FjaGVbdXJsXSAmJiBjYWNoZVt1cmxdLmV4cGlyZXMgPiBEYXRlLm5vdygpKSB7XFxuICAgICAgICAgICAgICAgIGF3YWl0IHJlcXVlc3QucmVzcG9uZChjYWNoZVt1cmxdKTtcXG4gICAgICAgICAgICAgICAgcmV0dXJuO1xcbiAgICAgICAgICAgIH1cXG4gICAgICAgICAgICByZXF1ZXN0LmNvbnRpbnVlKCk7XFxuICAgICAgICB9KTtcXG5cXG4gICAgICAgIHBhZ2Uub24oJ3Jlc3BvbnNlJywgYXN5bmMgKHJlc3BvbnNlKSA9PiB7XFxuICAgICAgICAgICAgY29uc3QgdXJsID0gcmVzcG9uc2UudXJsKCk7XFxuICAgICAgICAgICAgY29uc3QgaGVhZGVycyA9IHJlc3BvbnNlLmhlYWRlcnMoKTtcXG4gICAgICAgICAgICBjb25zdCBjYWNoZUNvbnRyb2wgPSBoZWFkZXJzWydjYWNoZS1jb250cm9sJ10gfHwgJyc7XFxuICAgICAgICAgICAgY29uc3QgbWF4QWdlTWF0Y2ggPSBjYWNoZUNvbnRyb2wubWF0Y2goL21heC1hZ2U9KFxcXFxkKykvKTtcXG4gICAgICAgICAgICBjb25zdCBtYXhBZ2UgPSBtYXhBZ2VNYXRjaCAmJiBtYXhBZ2VNYXRjaC5sZW5ndGggPiAxID8gcGFyc2VJbnQobWF4QWdlTWF0Y2hbMV0sIDEwKSA6IDA7XFxuXFxuICAgICAgICAgICAgaWYgKG1heEFnZSkge1xcbiAgICAgICAgICAgICAgICBpZiAoIWNhY2hlW3VybF0gfHwgY2FjaGVbdXJsXS5leHBpcmVzID4gRGF0ZS5ub3coKSkgcmV0dXJuO1xcblxcbiAgICAgICAgICAgICAgICBsZXQgYnVmZmVyO1xcbiAgICAgICAgICAgICAgICB0cnkge1xcbiAgICAgICAgICAgICAgICAgICAgYnVmZmVyID0gYXdhaXQgcmVzcG9uc2UuYnVmZmVyKCk7XFxuICAgICAgICAgICAgICAgIH0gY2F0Y2gge1xcbiAgICAgICAgICAgICAgICAgICAgLy8gc29tZSByZXNwb25zZXMgZG8gbm90IGNvbnRhaW4gYnVmZmVyIGFuZCBkbyBub3QgbmVlZCB0byBiZSBjYWNoZWRcXG4gICAgICAgICAgICAgICAgICAgIHJldHVybjtcXG4gICAgICAgICAgICAgICAgfVxcblxcbiAgICAgICAgICAgICAgICBjYWNoZVt1cmxdID0ge1xcbiAgICAgICAgICAgICAgICAgICAgc3RhdHVzOiByZXNwb25zZS5zdGF0dXMoKSxcXG4gICAgICAgICAgICAgICAgICAgIGhlYWRlcnM6IHJlc3BvbnNlLmhlYWRlcnMoKSxcXG4gICAgICAgICAgICAgICAgICAgIGJvZHk6IGJ1ZmZlcixcXG4gICAgICAgICAgICAgICAgICAgIGV4cGlyZXM6IERhdGUubm93KCkgKyBtYXhBZ2UgKiAxMDAwLFxcbiAgICAgICAgICAgICAgICB9O1xcbiAgICAgICAgICAgIH1cXG4gICAgICAgIH0pO1xcbiAgICB9XSxcXG4gICAgcmVxdWVzdEhhbmRsZXI6IGFzeW5jICh7IHBhZ2UsIHJlcXVlc3QgfSkgPT4ge1xcbiAgICAgICAgYXdhaXQgRGF0YXNldC5wdXNoRGF0YSh7XFxuICAgICAgICAgICAgdGl0bGU6IGF3YWl0IHBhZ2UudGl0bGUoKSxcXG4gICAgICAgICAgICB1cmw6IHJlcXVlc3QudXJsLFxcbiAgICAgICAgICAgIHN1Y2NlZWRlZDogdHJ1ZSxcXG4gICAgICAgIH0pO1xcbiAgICB9LFxcbn0pO1xcblxcbmF3YWl0IGNyYXdsZXIucnVuKFsnaHR0cHM6Ly9hcGlmeS5jb20vc3RvcmUnLCAnaHR0cHM6Ly9hcGlmeS5jb20nXSk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6NDA5NiwidGltZW91dCI6MTgwfX0.JN2lYfrYhuU1Kj6T5Ya9YEuVQboRB4s5BbGj-WHjpVw&asrc=run_on_apify


```
import { Dataset, PuppeteerCrawler } from 'crawlee';

const cache = {};

const crawler = new PuppeteerCrawler({
    preNavigationHooks: [async ({ page }) => {
        await page.setRequestInterception(true);

        page.on('request', async (request) => {
            const url = request.url();
            if (cache[url] && cache[url].expires > Date.now()) {
                await request.respond(cache[url]);
                return;
            }
            request.continue();
        });

        page.on('response', async (response) => {
            const url = response.url();
            const headers = response.headers();
            const cacheControl = headers['cache-control'] || '';
            const maxAgeMatch = cacheControl.match(/max-age=(\d+)/);
            const maxAge = maxAgeMatch && maxAgeMatch.length > 1 ? parseInt(maxAgeMatch[1], 10) : 0;

            if (maxAge) {
                if (!cache[url] || cache[url].expires > Date.now()) return;

                let buffer;
                try {
                    buffer = await response.buffer();
                } catch {
                    // some responses do not contain buffer and do not need to be cached
                    return;
                }

                cache[url] = {
                    status: response.status(),
                    headers: response.headers(),
                    body: buffer,
                    expires: Date.now() + maxAge * 1000,
                };
            }
        });
    }],
    requestHandler: async ({ page, request }) => {
        await Dataset.pushData({
            title: await page.title(),
            url: request.url,
            succeeded: true,
        });
    },
});

await crawler.run(['https://apify.com/store', 'https://apify.com']);
```
