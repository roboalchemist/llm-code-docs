# Source: https://docs.apify.com/sdk/js/docs/examples/puppeteer-with-proxy.md

# Puppeteer with proxy

Copy for LLM

This example demonstrates how to load pages in headless Chrome / Puppeteer over [Apify Proxy](https://docs.apify.com/proxy).

To make it work, you'll need an Apify account with access to the proxy. Visit the [Apify platform introduction](https://docs.apify.com/sdk/js/sdk/js/docs/guides/apify-platform.md) to find how to log into your account from the SDK.

tip

To run this example on the Apify Platform, select the `apify/actor-node-puppeteer-chrome` image for your Dockerfile.

[Run on](https://console.apify.com/actors/7tWSD8hrYzuc9Lte7?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IEFjdG9yIH0gZnJvbSAnYXBpZnknO1xcbmltcG9ydCB7IFB1cHBldGVlckNyYXdsZXIgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5hd2FpdCBBY3Rvci5pbml0KCk7XFxuXFxuLy8gUHJveHkgY29ubmVjdGlvbiBpcyBhdXRvbWF0aWNhbGx5IGVzdGFibGlzaGVkIGluIHRoZSBDcmF3bGVyXFxuY29uc3QgcHJveHlDb25maWd1cmF0aW9uID0gYXdhaXQgQWN0b3IuY3JlYXRlUHJveHlDb25maWd1cmF0aW9uKCk7XFxuXFxuY29uc3QgY3Jhd2xlciA9IG5ldyBQdXBwZXRlZXJDcmF3bGVyKHtcXG4gICAgcHJveHlDb25maWd1cmF0aW9uLFxcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcih7IHBhZ2UgfSkge1xcbiAgICAgICAgY29uc3Qgc3RhdHVzID0gYXdhaXQgcGFnZS4kZXZhbCgndGQuc3RhdHVzJywgKGVsKSA9PiBlbC50ZXh0Q29udGVudCk7XFxuICAgICAgICBjb25zb2xlLmxvZyhgUHJveHkgU3RhdHVzOiAke3N0YXR1c31gKTtcXG4gICAgfSxcXG59KTtcXG5cXG5jb25zb2xlLmxvZygnUnVubmluZyBQdXBwZXRlZXIgc2NyaXB0Li4uJyk7XFxuXFxuYXdhaXQgY3Jhd2xlci5ydW4oWydodHRwOi8vcHJveHkuYXBpZnkuY29tJ10pO1xcblxcbmNvbnNvbGUubG9nKCdQdXBwZXRlZXIgY2xvc2VkLicpO1xcblxcbmF3YWl0IEFjdG9yLmV4aXQoKTtcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.Z2NfopKj1DbaGy58OZ3N2Og8hM7AvkFTeEbBFCwOtGk\&asrc=run_on_apify)

```
import { Actor } from 'apify';
import { PuppeteerCrawler } from 'crawlee';

await Actor.init();

// Proxy connection is automatically established in the Crawler
const proxyConfiguration = await Actor.createProxyConfiguration();

const crawler = new PuppeteerCrawler({
    proxyConfiguration,
    async requestHandler({ page }) {
        const status = await page.$eval('td.status', (el) => el.textContent);
        console.log(`Proxy Status: ${status}`);
    },
});

console.log('Running Puppeteer script...');

await crawler.run(['http://proxy.apify.com']);

console.log('Puppeteer closed.');

await Actor.exit();
```
