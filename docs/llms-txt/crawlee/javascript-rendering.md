# Source: https://crawlee.dev/js/docs/guides/javascript-rendering.md

# JavaScript rendering

Copy for LLM

JavaScript rendering is the process of executing JavaScript on a page to make changes in the page's structure or content. It's also called client-side rendering, the opposite of server-side rendering. Some modern websites render on the client, some on the server and many cutting edge websites render some things on the server and other things on the client.

The Crawlee website does not use JavaScript rendering to display its content, so we have to look for an example elsewhere. [Apify Store](https://apify.com/store) is a library of scrapers and automations called **actors** that anyone can grab and use for free. It uses JavaScript rendering to display the list of actors, so let's use it to demonstrate how it works.

src/main.mjs

```
import { CheerioCrawler } from 'crawlee';

const crawler = new CheerioCrawler({
    async requestHandler({ $, request }) {
        // Extract text content of an actor card
        const actorText = $('.ActorStoreItem').text();
        console.log(`ACTOR: ${actorText}`);
    }
})

await crawler.run(['https://apify.com/store']);
```

Run the code, and you'll see that the crawler won't print the content of the actor card.

```
ACTOR:
```

That's because Apify Store uses client-side JavaScript to render its content and `CheerioCrawler` can't execute it, so the text never appears in the page's HTML.

You can confirm this using Chrome DevTools. If you go to <https://apify.com/store>, right-click anywhere in the page, select **View Page Source** and search for **ActorStoreItem** you won't find any results. Then, if you right-click again, select **Inspect** and search for the same **ActorStoreItem**, you will find many of them.

How's this possible? Because **View Page Source** shows the original HTML, before any JavaScript executions. That's what `CheerioCrawler` gets. Whereas with **Inspect** you see the current HTML - after JavaScript execution. When you understand this, it's not a huge surprise that `CheerioCrawler` can't find the data. For that we need a headless browser.

## Headless browsers[​](#headless-browsers "Direct link to Headless browsers")

To get the contents of `.ActorStoreItem`, you will have to use a headless browser. You can choose from two libraries to control your browser: [Puppeteer](https://github.com/puppeteer/puppeteer) or [Playwright](https://github.com/microsoft/playwright). The choice is simple. If you know one of them, choose the one you know. If you know both, or none, choose Playwright, because it's better in most cases.

## Waiting for elements to render[​](#waiting-for-elements-to-render "Direct link to Waiting for elements to render")

No matter which library you pick, here's example code for both. Playwright is a little more pleasant to use, but both libraries will get the job done. The big difference between them is that Playwright will automatically wait for elements to appear, whereas in Puppeteer, you have to explicitly wait for them.

* PlaywrightCrawler
* PuppeteerCrawler

src/main.mjs

```
import { PlaywrightCrawler } from 'crawlee';

const crawler = new PlaywrightCrawler({
    async requestHandler({ page }) {
        // page.locator points to an element in the DOM
        // using a CSS selector, but it does not access it yet.
        const actorCard = page.locator('.ActorStoreItem').first();
        // Upon calling one of the locator methods Playwright
        // waits for the element to render and then accesses it.
        const actorText = await actorCard.textContent();
        console.log(`ACTOR: ${actorText}`);
    },
});

await crawler.run(['https://apify.com/store']);
```

src/main.mjs

```
import { PuppeteerCrawler } from 'crawlee';

const crawler = new PuppeteerCrawler({
    async requestHandler({ page }) {
        // Puppeteer does not have the automatic waiting functionality
        // of Playwright, so we have to explicitly wait for the element.
        await page.waitForSelector('.ActorStoreItem');
        // Puppeteer does not have helper methods like locator.textContent,
        // so we have to manually extract the value using in-page JavaScript.
        const actorText = await page.$eval('.ActorStoreItem', (el) => {
            return el.textContent;
        });
        console.log(`ACTOR: ${actorText}`);
    },
});

await crawler.run(['https://apify.com/store']);
```

When you run the code, you'll see the *badly formatted* content of the first actor card printed to console:

```
ACTOR: Web Scraperapify/web-scraperCrawls arbitrary websites using [...]
```

### We're not kidding[​](#were-not-kidding "Direct link to We're not kidding")

If you don't believe us that the elements need to be waited for, run the following code which skips the waiting.

* PlaywrightCrawler
* PuppeteerCrawler

src/main.mjs

```
import { PlaywrightCrawler } from 'crawlee';

const crawler = new PlaywrightCrawler({
    async requestHandler({ page }) {
        // Here we don't wait for the selector and immediately
        // extract the text content from the page.
        const actorText = await page.$eval('.ActorStoreItem', (el) => {
            return el.textContent;
        });
        console.log(`ACTOR: ${actorText}`);
    },
});

await crawler.run(['https://apify.com/store']);
```

src/main.mjs

```
import { PuppeteerCrawler } from 'crawlee';

const crawler = new PuppeteerCrawler({
    async requestHandler({ page }) {
        // Here we don't wait for the selector and immediately
        // extract the text content from the page.
        const actorText = await page.$eval('.ActorStoreItem', (el) => {
            return el.textContent;
        });
        console.log(`ACTOR: ${actorText}`);
    },
});

await crawler.run(['https://apify.com/store']);
```

In both cases, the request will be retried a few times and eventually fail with an error like this:

```
ERROR [...] Error: failed to find element matching selector ".ActorStoreItem"
```

That's because when you try to access the element in the browser, it's not been rendered in the DOM yet.

tip

This guide only touches the concept of JavaScript rendering and use of headless browsers. To learn more, continue with the [Puppeteer & Playwright course](https://developers.apify.com/academy/puppeteer-playwright) in the Apify Academy. **It's free and open-source** ❤️.
