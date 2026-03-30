# Source: https://crawlee.dev/js/docs/guides/jsdom-crawler-guide.md

# JSDOMCrawler guide

Copy for LLM

​[`JSDOMCrawler`](https://crawlee.dev/js/api/jsdom-crawler/class/JSDOMCrawler.md) is very useful for scraping with the Window API.

## How the crawler works[​](#how-the-crawler-works "Direct link to How the crawler works")

​[`JSDOMCrawler`](https://crawlee.dev/js/api/jsdom-crawler/class/JSDOMCrawler.md) crawls by making plain HTTP requests to the provided URLs using the specialized [got-scraping](https://github.com/apify/got-scraping) HTTP client. The URLs are fed to the crawler using [`RequestQueue`](https://crawlee.dev/js/api/core/class/RequestQueue.md). The HTTP responses it gets back are usually HTML pages. The same pages you would get in your browser when you first load a URL. But it can handle any content types with the help of the [`additionalMimeTypes`](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlerOptions.md#additionalMimeTypes) option.

info

Modern web pages often do not serve all of their content in the first HTML response, but rather the first HTML contains links to other resources such as CSS and JavaScript that get downloaded afterwards, and together they create the final page. To crawl those, see [`PuppeteerCrawler`](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md) and [`PlaywrightCrawler`](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md).

Once the page's HTML is retrieved, the crawler will pass it to [JSDOM](https://www.npmjs.com/package/jsdom) for parsing. The result is a `window` property, which should be familiar to frontend developers. You can use the Window API to do all sorts of lookups and manipulation of the page's HTML, but in scraping, you will mostly use it to find specific HTML elements and extract their data.

Example use of browser JavaScript:

```
// Return the page title
document.title; // browsers
window.document.title; // JSDOM
```

## When to use `JSDOMCrawler`[​](#when-to-use-jsdomcrawler "Direct link to when-to-use-jsdomcrawler")

`JSDOMCrawler` really shines when `CheerioCrawler` is just not enough. There is an entire set of [APIs](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API) available!

**Advantages:**

* Easy to set up
* Familiar for frontend developers
* Content can be manipulated
* Automatically avoids some anti-scraping bans

**Disadvantages:**

* Slower than `CheerioCrawler`
* Does not work for websites that require JavaScript rendering
* May easily overload the target website with requests

## Example use of Element API[​](#example-use-of-element-api "Direct link to Example use of Element API")

### Find all links on a page[​](#find-all-links-on-a-page "Direct link to Find all links on a page")

This snippet finds all `<a>` elements which have the `href` attribute and extracts the hrefs into an array.

```
Array.from(document.querySelectorAll('a[href]')).map((a) => a.href);
```

### Other examples[​](#other-examples "Direct link to Other examples")

Visit the [Examples](https://crawlee.dev/js/docs/examples.md) section to browse examples of `JSDOMCrawler` usage. Almost all examples show `JSDOMCrawler` code in their code tabs.
