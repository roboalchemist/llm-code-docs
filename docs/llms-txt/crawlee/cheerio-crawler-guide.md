# Source: https://crawlee.dev/js/docs/guides/cheerio-crawler-guide.md

# CheerioCrawler guide

Copy for LLM

​[`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md) is our simplest and fastest crawler. If you're familiar with [jQuery](https://jquery.com/), you'll understand `CheerioCrawler` in minutes.

## What is Cheerio[​](#what-is-cheerio "Direct link to What is Cheerio")

[Cheerio](https://cheerio.js.org/) is essentially [jQuery](https://jquery.com/) for Node.js. It offers the same API, including the familiar `$` object. You can use it, as you would use jQuery for manipulating the DOM of an HTML page. In crawling, you'll mostly use it to select the needed elements and extract their values - the data you're interested in. But jQuery runs in a browser and attaches directly to the browser's DOM. Where does `cheerio` get its HTML? This is where the `Crawler` part of [`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md) comes in.

## How the crawler works[​](#how-the-crawler-works "Direct link to How the crawler works")

​[`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md) crawls by making plain HTTP requests to the provided URLs using the specialized [got-scraping](https://github.com/apify/got-scraping) HTTP client. The URLs are fed to the crawler using [`RequestQueue`](https://crawlee.dev/js/api/core/class/RequestQueue.md). The HTTP responses it gets back are usually HTML pages. The same pages you would get in your browser when you first load a URL. But it can handle any content types with the help of the [`additionalMimeTypes`](https://crawlee.dev/js/api/cheerio-crawler/interface/CheerioCrawlerOptions.md#additionalMimeTypes) option.

info

Modern web pages often do not serve all of their content in the first HTML response, but rather the first HTML contains links to other resources such as CSS and JavaScript that get downloaded afterwards, and together they create the final page. To crawl those, see [`PuppeteerCrawler`](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md) and [`PlaywrightCrawler`](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md).

Once the page's HTML is retrieved, the crawler will pass it to [Cheerio](https://github.com/cheeriojs/cheerio) for parsing. The result is the typical `$` function, which should be familiar to jQuery users. You can use the `$` function to do all sorts of lookups and manipulation of the page's HTML, but in scraping, you will mostly use it to find specific HTML elements and extract their data.

Example use of Cheerio and its `$` function in comparison to browser JavaScript:

```
// Return the text content of the <title> element.
document.querySelector('title').textContent; // plain JS
$('title').text(); // Cheerio

// Return an array of all 'href' links on the page.
Array.from(document.querySelectorAll('[href]')).map(el => el.href); // plain JS
$('[href]')
    .map((i, el) => $(el).attr('href'))
    .get(); // Cheerio
```

note

This is not to show that Cheerio is better than plain browser JavaScript. Some might actually prefer the more expressive way plain JS provides. Unfortunately, the browser JavaScript methods are not available in Node.js, so Cheerio is your best bet to do the parsing in Node.js.

## When to use `CheerioCrawler`[​](#when-to-use-cheeriocrawler "Direct link to when-to-use-cheeriocrawler")

`CheerioCrawler` really shines when you need to cope with extremely high workloads. With just 4 GBs of memory and a single CPU core, you can scrape 500 or more pages a minute! *(assuming each page contains approximately 400KB of HTML)*. To scrape this fast with a full browser scraper, such as the [`PlaywrightCrawler`](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md), you'd need significantly more computing power.

**Advantages:**

* Extremely fast and cheap to run
* Easy to set up
* Familiar for jQuery users
* Automatically avoids some anti-scraping bans

**Disadvantages:**

* Does not work for websites that require JavaScript rendering
* May easily overload the target website with requests
* Does not enable any manipulation of the website before scraping

## Web scraping with Cheerio: Examples[​](#web-scraping-with-cheerio-examples "Direct link to Web scraping with Cheerio: Examples")

### Get text content of an element[​](#get-text-content-of-an-element "Direct link to Get text content of an element")

Finds the first `<h2>` element and returns its text content.

```
$('h2').text()
```

### Find all links on a page[​](#find-all-links-on-a-page "Direct link to Find all links on a page")

This snippet finds all `<a>` elements which have the `href` attribute and extracts the hrefs into an array.

```
$('a[href]')
    .map((i, el) => $(el).attr('href'))
    .get();
```

### Other examples[​](#other-examples "Direct link to Other examples")

Visit the [Examples](https://crawlee.dev/js/docs/examples.md) section to browse examples of `CheerioCrawler` usage. Almost all examples show `CheerioCrawler` code in their code tabs.
