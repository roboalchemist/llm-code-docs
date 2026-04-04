# Source: https://crawlee.dev/js/docs/examples/skip-navigation.md

# Skipping navigations for certain requests

Copy for LLM

While crawling a website, you may encounter certain resources you'd like to save, but don't need the full power of a crawler to do so (like images delivered through a CDN).

By combining the [`Request#skipNavigation`](https://crawlee.dev/js/api/core/class/Request.md#skipNavigation) option with [`sendRequest`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md#sendRequest), we can fetch the image from the CDN, and save it to our key-value store without needing to use the full crawler.

info

For this example, we are using the [`PlaywrightCrawler`](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md) to showcase this, but this is available on all the crawlers we provide.

[Run on](https://console.apify.com/actors/6i5QsHBMtm3hKph70?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IFBsYXl3cmlnaHRDcmF3bGVyLCBLZXlWYWx1ZVN0b3JlIH0gZnJvbSAnY3Jhd2xlZSc7XFxuXFxuLy8gQ3JlYXRlIGEga2V5IHZhbHVlIHN0b3JlIGZvciBhbGwgaW1hZ2VzIHdlIGZpbmRcXG5jb25zdCBpbWFnZVN0b3JlID0gYXdhaXQgS2V5VmFsdWVTdG9yZS5vcGVuKCdpbWFnZXMnKTtcXG5cXG5jb25zdCBjcmF3bGVyID0gbmV3IFBsYXl3cmlnaHRDcmF3bGVyKHtcXG4gICAgYXN5bmMgcmVxdWVzdEhhbmRsZXIoeyByZXF1ZXN0LCBwYWdlLCBzZW5kUmVxdWVzdCB9KSB7XFxuICAgICAgICAvLyBUaGUgcmVxdWVzdCBzaG91bGQgaGF2ZSB0aGUgbmF2aWdhdGlvbiBza2lwcGVkXFxuICAgICAgICBpZiAocmVxdWVzdC5za2lwTmF2aWdhdGlvbikge1xcbiAgICAgICAgICAgIC8vIFJlcXVlc3QgdGhlIGltYWdlIGFuZCBnZXQgaXRzIGJ1ZmZlciBiYWNrXFxuICAgICAgICAgICAgY29uc3QgaW1hZ2VSZXNwb25zZSA9IGF3YWl0IHNlbmRSZXF1ZXN0KHsgcmVzcG9uc2VUeXBlOiAnYnVmZmVyJyB9KTtcXG5cXG4gICAgICAgICAgICAvLyBTYXZlIHRoZSBpbWFnZSBpbiB0aGUga2V5LXZhbHVlIHN0b3JlXFxuICAgICAgICAgICAgYXdhaXQgaW1hZ2VTdG9yZS5zZXRWYWx1ZShgJHtyZXF1ZXN0LnVzZXJEYXRhLmtleX0ucG5nYCwgaW1hZ2VSZXNwb25zZS5ib2R5KTtcXG5cXG4gICAgICAgICAgICAvLyBQcmV2ZW50IGV4ZWN1dGluZyB0aGUgcmVzdCBvZiB0aGUgY29kZSBhcyB3ZSBkbyBub3QgbmVlZCBpdFxcbiAgICAgICAgICAgIHJldHVybjtcXG4gICAgICAgIH1cXG5cXG4gICAgICAgIC8vIEdldCBhbGwgdGhlIGltYWdlIHNvdXJjZXMgaW4gdGhlIGN1cnJlbnQgcGFnZVxcbiAgICAgICAgY29uc3QgaW1hZ2VzID0gYXdhaXQgcGFnZS4kJGV2YWwoJ2ltZycsIChpbWdzKSA9PiBpbWdzLm1hcCgoaW1nKSA9PiBpbWcuc3JjKSk7XFxuXFxuICAgICAgICAvLyBBZGQgYWxsIHRoZSB1cmxzIGFzIHJlcXVlc3RzIGZvciB0aGUgY3Jhd2xlciwgZ2l2aW5nIGVhY2ggaW1hZ2UgYSBrZXlcXG4gICAgICAgIGF3YWl0IGNyYXdsZXIuYWRkUmVxdWVzdHMoaW1hZ2VzLm1hcCgodXJsLCBpKSA9PiAoeyB1cmwsIHNraXBOYXZpZ2F0aW9uOiB0cnVlLCB1c2VyRGF0YTogeyBrZXk6IGkgfSB9KSkpO1xcbiAgICB9LFxcbn0pO1xcblxcbmF3YWl0IGNyYXdsZXIuYWRkUmVxdWVzdHMoWydodHRwczovL2NyYXdsZWUuZGV2J10pO1xcblxcbi8vIFJ1biB0aGUgY3Jhd2xlclxcbmF3YWl0IGNyYXdsZXIucnVuKCk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6NDA5NiwidGltZW91dCI6MTgwfX0.cNsd2-DLQUjMSHwY8npJ3Im5Ffh-jGfcpADCVsdj91U\&asrc=run_on_apify)

```
import { PlaywrightCrawler, KeyValueStore } from 'crawlee';

// Create a key value store for all images we find
const imageStore = await KeyValueStore.open('images');

const crawler = new PlaywrightCrawler({
    async requestHandler({ request, page, sendRequest }) {
        // The request should have the navigation skipped
        if (request.skipNavigation) {
            // Request the image and get its buffer back
            const imageResponse = await sendRequest({ responseType: 'buffer' });

            // Save the image in the key-value store
            await imageStore.setValue(`${request.userData.key}.png`, imageResponse.body);

            // Prevent executing the rest of the code as we do not need it
            return;
        }

        // Get all the image sources in the current page
        const images = await page.$$eval('img', (imgs) => imgs.map((img) => img.src));

        // Add all the urls as requests for the crawler, giving each image a key
        await crawler.addRequests(images.map((url, i) => ({ url, skipNavigation: true, userData: { key: i } })));
    },
});

await crawler.addRequests(['https://crawlee.dev']);

// Run the crawler
await crawler.run();
```
