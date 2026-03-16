# Source: https://crawlee.dev/js/docs/examples/crawl-some-links.md

# Crawl some links on a website

Copy for LLM

This [`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md) example uses the [`globs`](https://crawlee.dev/js/api/core/interface/EnqueueLinksOptions.md#globs) property in the [`enqueueLinks()`](https://crawlee.dev/js/api/cheerio-crawler/interface/CheerioCrawlingContext.md#enqueueLinks) method to only add links to the [`RequestQueue`](https://crawlee.dev/js/api/core/class/RequestQueue.md) queue if they match the specified pattern.

[Run on](https://console.apify.com/actors/kk67IcZkKSSBTslXI?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IENoZWVyaW9DcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuLy8gQ3JlYXRlIGEgQ2hlZXJpb0NyYXdsZXJcXG5jb25zdCBjcmF3bGVyID0gbmV3IENoZWVyaW9DcmF3bGVyKHtcXG4gICAgLy8gTGltaXRzIHRoZSBjcmF3bGVyIHRvIG9ubHkgMTAgcmVxdWVzdHMgKGRvIG5vdCB1c2UgaWYgeW91IHdhbnQgdG8gY3Jhd2wgYWxsIGxpbmtzKVxcbiAgICBtYXhSZXF1ZXN0c1BlckNyYXdsOiAxMCxcXG4gICAgLy8gRnVuY3Rpb24gY2FsbGVkIGZvciBlYWNoIFVSTFxcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcih7IHJlcXVlc3QsIGVucXVldWVMaW5rcywgbG9nIH0pIHtcXG4gICAgICAgIGxvZy5pbmZvKHJlcXVlc3QudXJsKTtcXG4gICAgICAgIC8vIEFkZCBzb21lIGxpbmtzIGZyb20gcGFnZSB0byB0aGUgY3Jhd2xlcidzIFJlcXVlc3RRdWV1ZVxcbiAgICAgICAgYXdhaXQgZW5xdWV1ZUxpbmtzKHtcXG4gICAgICAgICAgICBnbG9iczogWydodHRwPyhzKTovL2NyYXdsZWUuZGV2LyovKiddLFxcbiAgICAgICAgfSk7XFxuICAgIH0sXFxufSk7XFxuXFxuLy8gRGVmaW5lIHRoZSBzdGFydGluZyBVUkxcXG5hd2FpdCBjcmF3bGVyLmFkZFJlcXVlc3RzKFsnaHR0cHM6Ly9jcmF3bGVlLmRldiddKTtcXG5cXG4vLyBSdW4gdGhlIGNyYXdsZXJcXG5hd2FpdCBjcmF3bGVyLnJ1bigpO1xcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjEwMjQsInRpbWVvdXQiOjE4MH19.VVfWBrP6w-lmqCKIsnpIZMak9PCZ9HoTchf7mqrbVUo\&asrc=run_on_apify)

```
import { CheerioCrawler } from 'crawlee';

// Create a CheerioCrawler
const crawler = new CheerioCrawler({
    // Limits the crawler to only 10 requests (do not use if you want to crawl all links)
    maxRequestsPerCrawl: 10,
    // Function called for each URL
    async requestHandler({ request, enqueueLinks, log }) {
        log.info(request.url);
        // Add some links from page to the crawler's RequestQueue
        await enqueueLinks({
            globs: ['http?(s)://crawlee.dev/*/*'],
        });
    },
});

// Define the starting URL
await crawler.addRequests(['https://crawlee.dev']);

// Run the crawler
await crawler.run();
```
