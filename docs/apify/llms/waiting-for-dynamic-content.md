# Source: https://docs.apify.com/academy/node-js/waiting-for-dynamic-content.md

# Waiting for dynamic content

Use these helper functions to wait for data:

* `page.waitFor` in [Puppeteer](https://pptr.dev/) (or Puppeteer Scraper ([apify/puppeteer-scraper](https://apify.com/apify/puppeteer-scraper))).

* `context.waitFor` in Web Scraper ([apify/web-scraper](https://apify.com/apify/web-scraper)).

Pass in time in milliseconds or a selector to wait for.

Examples:

* `await page.waitFor(10000)` - waits for 10 seconds.

* `await context.waitFor('my-selector')` - waits for `my-selector` to appear on the page.

For details, code examples, and advanced use cases, visit our [documentation](https://docs.apify.com/academy/puppeteer-playwright/page/waiting.md).
