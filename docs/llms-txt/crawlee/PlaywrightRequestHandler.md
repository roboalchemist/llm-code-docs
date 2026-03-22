# Source: https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightRequestHandler.md

# PlaywrightRequestHandler<!-- -->

### Hierarchy

* [BrowserRequestHandler](https://crawlee.dev/js/api/browser-crawler.md#BrowserRequestHandler)\<LoadedContext<[PlaywrightCrawlingContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlingContext.md)>>
  * *PlaywrightRequestHandler*

### Callable

* ****PlaywrightRequestHandler**(inputs): Awaitable\<void>

***

* #### Parameters

  * ##### inputs: { request: [LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>> } & Omit<{ request: [LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>> } & Omit<[PlaywrightCrawlingContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlingContext.md)\<Dictionary>, request>, request>

  #### Returns Awaitable\<void>
