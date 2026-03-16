# Source: https://crawlee.dev/js/api/stagehand-crawler/interface/StagehandRequestHandler.md

# StagehandRequestHandler<!-- -->

Request handler for StagehandCrawler.

### Hierarchy

* [BrowserRequestHandler](https://crawlee.dev/js/api/browser-crawler.md#BrowserRequestHandler)\<LoadedContext<[StagehandCrawlingContext](https://crawlee.dev/js/api/stagehand-crawler/interface/StagehandCrawlingContext.md)>>
  * *StagehandRequestHandler*

### Callable

* ****StagehandRequestHandler**(inputs): Awaitable\<void>

***

* #### Parameters

  * ##### inputs: { request: [LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>> } & Omit<{ request: [LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>> } & Omit<[StagehandCrawlingContext](https://crawlee.dev/js/api/stagehand-crawler/interface/StagehandCrawlingContext.md)\<Dictionary>, request>, request>

  #### Returns Awaitable\<void>
