# Source: https://crawlee.dev/js/docs/examples/crawler-plugins.md

# Using Puppeteer Stealth Plugin (puppeteer-extra) and playwright-extra

Copy for LLM

[`puppeteer-extra`](https://www.npmjs.com/package/puppeteer-extra) and [`playwright-extra`](https://www.npmjs.com/package/playwright-extra) are community-built libraries that bring in a plugin system to enhance the usage of [`puppeteer`](https://www.npmjs.com/package/puppeteer) and [`playwright`](https://www.npmjs.com/package/playwright) respectively (bringing in extra functionality, like improving stealth for example by using the Puppeteer Stealth plugin [(`puppeteer-extra-plugin-stealth`)](https://www.npmjs.com/package/puppeteer-extra-plugin-stealth)).

Available plugins

You can see a list of available plugins on the [`puppeteer-extra`s plugin list](https://www.npmjs.com/package/puppeteer-extra#plugins).

For [`playwright`](https://www.npmjs.com/package/playwright), please see [`playwright-extra`s plugin list](https://www.npmjs.com/package/playwright-extra#plugins) instead.

In this example, we'll show you how to use the Puppeteer Stealth [(`puppeteer-extra-plugin-stealth`)](https://www.npmjs.com/package/puppeteer-extra-plugin-stealth) plugin to help you avoid bot detections when crawling your target website.

* Puppeteer & puppeteer-extra
* Playwright & playwright-extra

Before you begin

Make sure you've installed the Puppeteer Extra (`puppeteer-extra`) and Puppeteer Stealth plugin(`puppeteer-extra-plugin-stealth`) packages via your preferred package manager

```
npm install puppeteer-extra puppeteer-extra-plugin-stealth
```

tip

To run this example on the Apify Platform, select the `apify/actor-node-puppeteer-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIgfSBmcm9tICdjcmF3bGVlJztcXG5pbXBvcnQgcHVwcGV0ZWVyRXh0cmEgZnJvbSAncHVwcGV0ZWVyLWV4dHJhJztcXG5pbXBvcnQgc3RlYWx0aFBsdWdpbiBmcm9tICdwdXBwZXRlZXItZXh0cmEtcGx1Z2luLXN0ZWFsdGgnO1xcblxcbi8vIEZpcnN0LCB3ZSB0ZWxsIHB1cHBldGVlci1leHRyYSB0byB1c2UgdGhlIHBsdWdpbiAob3IgcGx1Z2lucykgd2Ugd2FudC5cXG4vLyBDZXJ0YWluIHBsdWdpbnMgbWlnaHQgaGF2ZSBvcHRpb25zIHlvdSBjYW4gcGFzcyBpbiAtIHJlYWQgdXAgb24gdGhlaXIgZG9jdW1lbnRhdGlvbiFcXG4vLyBAdHMtZXhwZWN0LWVycm9yIC0gVGhlIGRlZmF1bHQgZXhwb3J0IHR5cGVzIGZvciBwdXBwZXRlZXItZXh0cmEgZG9uJ3QgcHJvcGVybHkgZXhwb3NlIHRoZSAndXNlJyBtZXRob2QgaW4gRVNNIGNvbnRleHRzXFxucHVwcGV0ZWVyRXh0cmEudXNlKHN0ZWFsdGhQbHVnaW4oKSk7XFxuXFxuLy8gQ3JlYXRlIGFuIGluc3RhbmNlIG9mIHRoZSBQdXBwZXRlZXJDcmF3bGVyIGNsYXNzIC0gYSBjcmF3bGVyXFxuLy8gdGhhdCBhdXRvbWF0aWNhbGx5IGxvYWRzIHRoZSBVUkxzIGluIGhlYWRsZXNzIENocm9tZSAvIFB1cHBldGVlci5cXG5jb25zdCBjcmF3bGVyID0gbmV3IFB1cHBldGVlckNyYXdsZXIoe1xcbiAgICBsYXVuY2hDb250ZXh0OiB7XFxuICAgICAgICAvLyAhISEgWW91IG5lZWQgdG8gc3BlY2lmeSB0aGlzIG9wdGlvbiB0byB0ZWxsIENyYXdsZWUgdG8gdXNlIHB1cHBldGVlci1leHRyYSBhcyB0aGUgbGF1bmNoZXIgISEhXFxuICAgICAgICBsYXVuY2hlcjogcHVwcGV0ZWVyRXh0cmEsXFxuICAgICAgICBsYXVuY2hPcHRpb25zOiB7XFxuICAgICAgICAgICAgLy8gT3RoZXIgcHVwcGV0ZWVyIG9wdGlvbnMgd29yayBhcyB1c3VhbFxcbiAgICAgICAgICAgIGhlYWRsZXNzOiB0cnVlLFxcbiAgICAgICAgfSxcXG4gICAgfSxcXG5cXG4gICAgLy8gU3RvcCBjcmF3bGluZyBhZnRlciBzZXZlcmFsIHBhZ2VzXFxuICAgIG1heFJlcXVlc3RzUGVyQ3Jhd2w6IDUwLFxcblxcbiAgICAvLyBUaGlzIGZ1bmN0aW9uIHdpbGwgYmUgY2FsbGVkIGZvciBlYWNoIFVSTCB0byBjcmF3bC5cXG4gICAgLy8gSGVyZSB5b3UgY2FuIHdyaXRlIHRoZSBQdXBwZXRlZXIgc2NyaXB0cyB5b3UgYXJlIGZhbWlsaWFyIHdpdGgsXFxuICAgIC8vIHdpdGggdGhlIGV4Y2VwdGlvbiB0aGF0IGJyb3dzZXJzIGFuZCBwYWdlcyBhcmUgYXV0b21hdGljYWxseSBtYW5hZ2VkIGJ5IENyYXdsZWUuXFxuICAgIC8vIFRoZSBmdW5jdGlvbiBhY2NlcHRzIGEgc2luZ2xlIHBhcmFtZXRlciwgd2hpY2ggaXMgYW4gb2JqZWN0IHdpdGggdGhlIGZvbGxvd2luZyBmaWVsZHM6XFxuICAgIC8vIC0gcmVxdWVzdDogYW4gaW5zdGFuY2Ugb2YgdGhlIFJlcXVlc3QgY2xhc3Mgd2l0aCBpbmZvcm1hdGlvbiBzdWNoIGFzIFVSTCBhbmQgSFRUUCBtZXRob2RcXG4gICAgLy8gLSBwYWdlOiBQdXBwZXRlZXIncyBQYWdlIG9iamVjdCAoc2VlIGh0dHBzOi8vcHB0ci5kZXYvI3Nob3c9YXBpLWNsYXNzLXBhZ2UpXFxuICAgIGFzeW5jIHJlcXVlc3RIYW5kbGVyKHsgcHVzaERhdGEsIHJlcXVlc3QsIHBhZ2UsIGVucXVldWVMaW5rcywgbG9nIH0pIHtcXG4gICAgICAgIGxvZy5pbmZvKGBQcm9jZXNzaW5nICR7cmVxdWVzdC51cmx9Li4uYCk7XFxuXFxuICAgICAgICAvLyBBIGZ1bmN0aW9uIHRvIGJlIGV2YWx1YXRlZCBieSBQdXBwZXRlZXIgd2l0aGluIHRoZSBicm93c2VyIGNvbnRleHQuXFxuICAgICAgICBjb25zdCBkYXRhID0gYXdhaXQgcGFnZS4kJGV2YWwoJy5hdGhpbmcnLCAoJHBvc3RzKSA9PiB7XFxuICAgICAgICAgICAgY29uc3Qgc2NyYXBlZERhdGE6IHsgdGl0bGU_OiBzdHJpbmc7IHJhbms_OiBzdHJpbmc7IGhyZWY_OiBzdHJpbmcgfVtdID0gW107XFxuXFxuICAgICAgICAgICAgLy8gV2UncmUgZ2V0dGluZyB0aGUgdGl0bGUsIHJhbmsgYW5kIFVSTCBvZiBlYWNoIHBvc3Qgb24gSGFja2VyIE5ld3MuXFxuICAgICAgICAgICAgJHBvc3RzLmZvckVhY2goKCRwb3N0KSA9PiB7XFxuICAgICAgICAgICAgICAgIHNjcmFwZWREYXRhLnB1c2goe1xcbiAgICAgICAgICAgICAgICAgICAgdGl0bGU6ICRwb3N0LnF1ZXJ5U2VsZWN0b3I8SFRNTEVsZW1lbnQ-KCcudGl0bGUgYScpPy5pbm5lclRleHQsXFxuICAgICAgICAgICAgICAgICAgICByYW5rOiAkcG9zdC5xdWVyeVNlbGVjdG9yPEhUTUxFbGVtZW50PignLnJhbmsnKT8uaW5uZXJUZXh0LFxcbiAgICAgICAgICAgICAgICAgICAgaHJlZjogJHBvc3QucXVlcnlTZWxlY3RvcjxIVE1MQW5jaG9yRWxlbWVudD4oJy50aXRsZSBhJyk_LmhyZWYsXFxuICAgICAgICAgICAgICAgIH0pO1xcbiAgICAgICAgICAgIH0pO1xcblxcbiAgICAgICAgICAgIHJldHVybiBzY3JhcGVkRGF0YTtcXG4gICAgICAgIH0pO1xcblxcbiAgICAgICAgLy8gU3RvcmUgdGhlIHJlc3VsdHMgdG8gdGhlIGRlZmF1bHQgZGF0YXNldC5cXG4gICAgICAgIGF3YWl0IHB1c2hEYXRhKGRhdGEpO1xcblxcbiAgICAgICAgLy8gRmluZCBhIGxpbmsgdG8gdGhlIG5leHQgcGFnZSBhbmQgZW5xdWV1ZSBpdCBpZiBpdCBleGlzdHMuXFxuICAgICAgICBjb25zdCBpbmZvcyA9IGF3YWl0IGVucXVldWVMaW5rcyh7XFxuICAgICAgICAgICAgc2VsZWN0b3I6ICcubW9yZWxpbmsnLFxcbiAgICAgICAgfSk7XFxuXFxuICAgICAgICBpZiAoaW5mb3MucHJvY2Vzc2VkUmVxdWVzdHMubGVuZ3RoID09PSAwKSBsb2cuaW5mbyhgJHtyZXF1ZXN0LnVybH0gaXMgdGhlIGxhc3QgcGFnZSFgKTtcXG4gICAgfSxcXG5cXG4gICAgLy8gVGhpcyBmdW5jdGlvbiBpcyBjYWxsZWQgaWYgdGhlIHBhZ2UgcHJvY2Vzc2luZyBmYWlsZWQgbW9yZSB0aGFuIG1heFJlcXVlc3RSZXRyaWVzKzEgdGltZXMuXFxuICAgIGZhaWxlZFJlcXVlc3RIYW5kbGVyKHsgcmVxdWVzdCwgbG9nIH0pIHtcXG4gICAgICAgIGxvZy5lcnJvcihgUmVxdWVzdCAke3JlcXVlc3QudXJsfSBmYWlsZWQgdG9vIG1hbnkgdGltZXMuYCk7XFxuICAgIH0sXFxufSk7XFxuXFxuYXdhaXQgY3Jhd2xlci5hZGRSZXF1ZXN0cyhbJ2h0dHBzOi8vbmV3cy55Y29tYmluYXRvci5jb20vJ10pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlciBhbmQgd2FpdCBmb3IgaXQgdG8gZmluaXNoLlxcbmF3YWl0IGNyYXdsZXIucnVuKCk7XFxuXFxuY29uc29sZS5sb2coJ0NyYXdsZXIgZmluaXNoZWQuJyk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6NDA5NiwidGltZW91dCI6MTgwfX0.erjCYsQpqyU70l6i3NR-y3_xN3CwLhF0PY0CWgkxF1Q\&asrc=run_on_apify)

src/crawler.ts

```
import { PuppeteerCrawler } from 'crawlee';
import puppeteerExtra from 'puppeteer-extra';
import stealthPlugin from 'puppeteer-extra-plugin-stealth';

// First, we tell puppeteer-extra to use the plugin (or plugins) we want.
// Certain plugins might have options you can pass in - read up on their documentation!
// @ts-expect-error - The default export types for puppeteer-extra don't properly expose the 'use' method in ESM contexts
puppeteerExtra.use(stealthPlugin());

// Create an instance of the PuppeteerCrawler class - a crawler
// that automatically loads the URLs in headless Chrome / Puppeteer.
const crawler = new PuppeteerCrawler({
    launchContext: {
        // !!! You need to specify this option to tell Crawlee to use puppeteer-extra as the launcher !!!
        launcher: puppeteerExtra,
        launchOptions: {
            // Other puppeteer options work as usual
            headless: true,
        },
    },

    // Stop crawling after several pages
    maxRequestsPerCrawl: 50,

    // This function will be called for each URL to crawl.
    // Here you can write the Puppeteer scripts you are familiar with,
    // with the exception that browsers and pages are automatically managed by Crawlee.
    // The function accepts a single parameter, which is an object with the following fields:
    // - request: an instance of the Request class with information such as URL and HTTP method
    // - page: Puppeteer's Page object (see https://pptr.dev/#show=api-class-page)
    async requestHandler({ pushData, request, page, enqueueLinks, log }) {
        log.info(`Processing ${request.url}...`);

        // A function to be evaluated by Puppeteer within the browser context.
        const data = await page.$$eval('.athing', ($posts) => {
            const scrapedData: { title?: string; rank?: string; href?: string }[] = [];

            // We're getting the title, rank and URL of each post on Hacker News.
            $posts.forEach(($post) => {
                scrapedData.push({
                    title: $post.querySelector<HTMLElement>('.title a')?.innerText,
                    rank: $post.querySelector<HTMLElement>('.rank')?.innerText,
                    href: $post.querySelector<HTMLAnchorElement>('.title a')?.href,
                });
            });

            return scrapedData;
        });

        // Store the results to the default dataset.
        await pushData(data);

        // Find a link to the next page and enqueue it if it exists.
        const infos = await enqueueLinks({
            selector: '.morelink',
        });

        if (infos.processedRequests.length === 0) log.info(`${request.url} is the last page!`);
    },

    // This function is called if the page processing failed more than maxRequestRetries+1 times.
    failedRequestHandler({ request, log }) {
        log.error(`Request ${request.url} failed too many times.`);
    },
});

await crawler.addRequests(['https://news.ycombinator.com/']);

// Run the crawler and wait for it to finish.
await crawler.run();

console.log('Crawler finished.');
```

Before you begin

Make sure you've installed the `playwright-extra` and `puppeteer-extra-plugin-stealth` packages via your preferred package manager

```
npm install playwright-extra puppeteer-extra-plugin-stealth
```

tip

To run this example on the Apify Platform, select the `apify/actor-node-puppeteer-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/6i5QsHBMtm3hKph70?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFBsYXl3cmlnaHRDcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuLy8gRm9yIHBsYXl3cmlnaHQtZXh0cmEgeW91IHdpbGwgbmVlZCB0byBpbXBvcnQgdGhlIGJyb3dzZXIgdHlwZSBpdHNlbGYgdGhhdCB5b3Ugd2FudCB0byB1c2UhXFxuLy8gQnkgZGVmYXVsdCwgUGxheXdyaWdodENyYXdsZXIgdXNlcyBjaHJvbWl1bSwgYnV0IHlvdSBjYW4gYWxzbyB1c2UgZmlyZWZveCBvciB3ZWJraXQuXFxuaW1wb3J0IHsgY2hyb21pdW0gfSBmcm9tICdwbGF5d3JpZ2h0LWV4dHJhJztcXG5pbXBvcnQgc3RlYWx0aFBsdWdpbiBmcm9tICdwdXBwZXRlZXItZXh0cmEtcGx1Z2luLXN0ZWFsdGgnO1xcblxcbi8vIEZpcnN0LCB3ZSB0ZWxsIHBsYXl3cmlnaHQtZXh0cmEgdG8gdXNlIHRoZSBwbHVnaW4gKG9yIHBsdWdpbnMpIHdlIHdhbnQuXFxuLy8gQ2VydGFpbiBwbHVnaW5zIG1pZ2h0IGhhdmUgb3B0aW9ucyB5b3UgY2FuIHBhc3MgaW4gLSByZWFkIHVwIG9uIHRoZWlyIGRvY3VtZW50YXRpb24hXFxuY2hyb21pdW0udXNlKHN0ZWFsdGhQbHVnaW4oKSk7XFxuXFxuLy8gQ3JlYXRlIGFuIGluc3RhbmNlIG9mIHRoZSBQbGF5d3JpZ2h0Q3Jhd2xlciBjbGFzcyAtIGEgY3Jhd2xlclxcbi8vIHRoYXQgYXV0b21hdGljYWxseSBsb2FkcyB0aGUgVVJMcyBpbiBoZWFkbGVzcyBDaHJvbWUgLyBQbGF5d3JpZ2h0LlxcbmNvbnN0IGNyYXdsZXIgPSBuZXcgUGxheXdyaWdodENyYXdsZXIoe1xcbiAgICBsYXVuY2hDb250ZXh0OiB7XFxuICAgICAgICAvLyAhISEgWW91IG5lZWQgdG8gc3BlY2lmeSB0aGlzIG9wdGlvbiB0byB0ZWxsIENyYXdsZWUgdG8gdXNlIHBsYXl3cmlnaHQtZXh0cmEgYXMgdGhlIGxhdW5jaGVyICEhIVxcbiAgICAgICAgbGF1bmNoZXI6IGNocm9taXVtLFxcbiAgICAgICAgbGF1bmNoT3B0aW9uczoge1xcbiAgICAgICAgICAgIC8vIE90aGVyIHBsYXl3cmlnaHQgb3B0aW9ucyB3b3JrIGFzIHVzdWFsXFxuICAgICAgICAgICAgaGVhZGxlc3M6IHRydWUsXFxuICAgICAgICB9LFxcbiAgICB9LFxcblxcbiAgICAvLyBTdG9wIGNyYXdsaW5nIGFmdGVyIHNldmVyYWwgcGFnZXNcXG4gICAgbWF4UmVxdWVzdHNQZXJDcmF3bDogNTAsXFxuXFxuICAgIC8vIFRoaXMgZnVuY3Rpb24gd2lsbCBiZSBjYWxsZWQgZm9yIGVhY2ggVVJMIHRvIGNyYXdsLlxcbiAgICAvLyBIZXJlIHlvdSBjYW4gd3JpdGUgdGhlIFB1cHBldGVlciBzY3JpcHRzIHlvdSBhcmUgZmFtaWxpYXIgd2l0aCxcXG4gICAgLy8gd2l0aCB0aGUgZXhjZXB0aW9uIHRoYXQgYnJvd3NlcnMgYW5kIHBhZ2VzIGFyZSBhdXRvbWF0aWNhbGx5IG1hbmFnZWQgYnkgQ3Jhd2xlZS5cXG4gICAgLy8gVGhlIGZ1bmN0aW9uIGFjY2VwdHMgYSBzaW5nbGUgcGFyYW1ldGVyLCB3aGljaCBpcyBhbiBvYmplY3Qgd2l0aCB0aGUgZm9sbG93aW5nIGZpZWxkczpcXG4gICAgLy8gLSByZXF1ZXN0OiBhbiBpbnN0YW5jZSBvZiB0aGUgUmVxdWVzdCBjbGFzcyB3aXRoIGluZm9ybWF0aW9uIHN1Y2ggYXMgVVJMIGFuZCBIVFRQIG1ldGhvZFxcbiAgICAvLyAtIHBhZ2U6IFB1cHBldGVlcidzIFBhZ2Ugb2JqZWN0IChzZWUgaHR0cHM6Ly9wcHRyLmRldi8jc2hvdz1hcGktY2xhc3MtcGFnZSlcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyBwdXNoRGF0YSwgcmVxdWVzdCwgcGFnZSwgZW5xdWV1ZUxpbmtzLCBsb2cgfSkge1xcbiAgICAgICAgbG9nLmluZm8oYFByb2Nlc3NpbmcgJHtyZXF1ZXN0LnVybH0uLi5gKTtcXG5cXG4gICAgICAgIC8vIEEgZnVuY3Rpb24gdG8gYmUgZXZhbHVhdGVkIGJ5IFB1cHBldGVlciB3aXRoaW4gdGhlIGJyb3dzZXIgY29udGV4dC5cXG4gICAgICAgIGNvbnN0IGRhdGEgPSBhd2FpdCBwYWdlLiQkZXZhbCgnLmF0aGluZycsICgkcG9zdHMpID0-IHtcXG4gICAgICAgICAgICBjb25zdCBzY3JhcGVkRGF0YTogeyB0aXRsZT86IHN0cmluZzsgcmFuaz86IHN0cmluZzsgaHJlZj86IHN0cmluZyB9W10gPSBbXTtcXG5cXG4gICAgICAgICAgICAvLyBXZSdyZSBnZXR0aW5nIHRoZSB0aXRsZSwgcmFuayBhbmQgVVJMIG9mIGVhY2ggcG9zdCBvbiBIYWNrZXIgTmV3cy5cXG4gICAgICAgICAgICAkcG9zdHMuZm9yRWFjaCgoJHBvc3QpID0-IHtcXG4gICAgICAgICAgICAgICAgc2NyYXBlZERhdGEucHVzaCh7XFxuICAgICAgICAgICAgICAgICAgICB0aXRsZTogJHBvc3QucXVlcnlTZWxlY3RvcjxIVE1MRWxlbWVudD4oJy50aXRsZSBhJyk_LmlubmVyVGV4dCxcXG4gICAgICAgICAgICAgICAgICAgIHJhbms6ICRwb3N0LnF1ZXJ5U2VsZWN0b3I8SFRNTEVsZW1lbnQ-KCcucmFuaycpPy5pbm5lclRleHQsXFxuICAgICAgICAgICAgICAgICAgICBocmVmOiAkcG9zdC5xdWVyeVNlbGVjdG9yPEhUTUxBbmNob3JFbGVtZW50PignLnRpdGxlIGEnKT8uaHJlZixcXG4gICAgICAgICAgICAgICAgfSk7XFxuICAgICAgICAgICAgfSk7XFxuXFxuICAgICAgICAgICAgcmV0dXJuIHNjcmFwZWREYXRhO1xcbiAgICAgICAgfSk7XFxuXFxuICAgICAgICAvLyBTdG9yZSB0aGUgcmVzdWx0cyB0byB0aGUgZGVmYXVsdCBkYXRhc2V0LlxcbiAgICAgICAgYXdhaXQgcHVzaERhdGEoZGF0YSk7XFxuXFxuICAgICAgICAvLyBGaW5kIGEgbGluayB0byB0aGUgbmV4dCBwYWdlIGFuZCBlbnF1ZXVlIGl0IGlmIGl0IGV4aXN0cy5cXG4gICAgICAgIGNvbnN0IGluZm9zID0gYXdhaXQgZW5xdWV1ZUxpbmtzKHtcXG4gICAgICAgICAgICBzZWxlY3RvcjogJy5tb3JlbGluaycsXFxuICAgICAgICB9KTtcXG5cXG4gICAgICAgIGlmIChpbmZvcy5wcm9jZXNzZWRSZXF1ZXN0cy5sZW5ndGggPT09IDApIGxvZy5pbmZvKGAke3JlcXVlc3QudXJsfSBpcyB0aGUgbGFzdCBwYWdlIWApO1xcbiAgICB9LFxcblxcbiAgICAvLyBUaGlzIGZ1bmN0aW9uIGlzIGNhbGxlZCBpZiB0aGUgcGFnZSBwcm9jZXNzaW5nIGZhaWxlZCBtb3JlIHRoYW4gbWF4UmVxdWVzdFJldHJpZXMrMSB0aW1lcy5cXG4gICAgZmFpbGVkUmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCBsb2cgfSkge1xcbiAgICAgICAgbG9nLmVycm9yKGBSZXF1ZXN0ICR7cmVxdWVzdC51cmx9IGZhaWxlZCB0b28gbWFueSB0aW1lcy5gKTtcXG4gICAgfSxcXG59KTtcXG5cXG5hd2FpdCBjcmF3bGVyLmFkZFJlcXVlc3RzKFsnaHR0cHM6Ly9uZXdzLnljb21iaW5hdG9yLmNvbS8nXSk7XFxuXFxuLy8gUnVuIHRoZSBjcmF3bGVyIGFuZCB3YWl0IGZvciBpdCB0byBmaW5pc2guXFxuYXdhaXQgY3Jhd2xlci5ydW4oKTtcXG5cXG5jb25zb2xlLmxvZygnQ3Jhd2xlciBmaW5pc2hlZC4nKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.qsuWDgcjPfimnhI0ONuIVCwKff0S-kQztvS65BTeKvg\&asrc=run_on_apify)

src/crawler.ts

```
import { PlaywrightCrawler } from 'crawlee';

// For playwright-extra you will need to import the browser type itself that you want to use!
// By default, PlaywrightCrawler uses chromium, but you can also use firefox or webkit.
import { chromium } from 'playwright-extra';
import stealthPlugin from 'puppeteer-extra-plugin-stealth';

// First, we tell playwright-extra to use the plugin (or plugins) we want.
// Certain plugins might have options you can pass in - read up on their documentation!
chromium.use(stealthPlugin());

// Create an instance of the PlaywrightCrawler class - a crawler
// that automatically loads the URLs in headless Chrome / Playwright.
const crawler = new PlaywrightCrawler({
    launchContext: {
        // !!! You need to specify this option to tell Crawlee to use playwright-extra as the launcher !!!
        launcher: chromium,
        launchOptions: {
            // Other playwright options work as usual
            headless: true,
        },
    },

    // Stop crawling after several pages
    maxRequestsPerCrawl: 50,

    // This function will be called for each URL to crawl.
    // Here you can write the Puppeteer scripts you are familiar with,
    // with the exception that browsers and pages are automatically managed by Crawlee.
    // The function accepts a single parameter, which is an object with the following fields:
    // - request: an instance of the Request class with information such as URL and HTTP method
    // - page: Puppeteer's Page object (see https://pptr.dev/#show=api-class-page)
    async requestHandler({ pushData, request, page, enqueueLinks, log }) {
        log.info(`Processing ${request.url}...`);

        // A function to be evaluated by Puppeteer within the browser context.
        const data = await page.$$eval('.athing', ($posts) => {
            const scrapedData: { title?: string; rank?: string; href?: string }[] = [];

            // We're getting the title, rank and URL of each post on Hacker News.
            $posts.forEach(($post) => {
                scrapedData.push({
                    title: $post.querySelector<HTMLElement>('.title a')?.innerText,
                    rank: $post.querySelector<HTMLElement>('.rank')?.innerText,
                    href: $post.querySelector<HTMLAnchorElement>('.title a')?.href,
                });
            });

            return scrapedData;
        });

        // Store the results to the default dataset.
        await pushData(data);

        // Find a link to the next page and enqueue it if it exists.
        const infos = await enqueueLinks({
            selector: '.morelink',
        });

        if (infos.processedRequests.length === 0) log.info(`${request.url} is the last page!`);
    },

    // This function is called if the page processing failed more than maxRequestRetries+1 times.
    failedRequestHandler({ request, log }) {
        log.error(`Request ${request.url} failed too many times.`);
    },
});

await crawler.addRequests(['https://news.ycombinator.com/']);

// Run the crawler and wait for it to finish.
await crawler.run();

console.log('Crawler finished.');
```
