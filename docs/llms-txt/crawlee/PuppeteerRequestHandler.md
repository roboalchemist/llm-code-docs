# Source: https://crawlee.dev/js/api/puppeteer-crawler/interface/PuppeteerRequestHandler.md

# PuppeteerRequestHandler<!-- -->

### Hierarchy

* [BrowserRequestHandler](https://crawlee.dev/js/api/browser-crawler.md#BrowserRequestHandler)\<LoadedContext<[PuppeteerCrawlingContext](https://crawlee.dev/js/api/puppeteer-crawler/interface/PuppeteerCrawlingContext.md)>>
  * *PuppeteerRequestHandler*

### Callable

* ****PuppeteerRequestHandler**(inputs): Awaitable\<void>

***

* #### Parameters

  * ##### inputs: { request: [LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>> } & Omit<{ request: [LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>> } & Omit<[PuppeteerCrawlingContext](https://crawlee.dev/js/api/puppeteer-crawler/interface/PuppeteerCrawlingContext.md)\<Dictionary>, request>, request>

  #### Returns Awaitable\<void>
