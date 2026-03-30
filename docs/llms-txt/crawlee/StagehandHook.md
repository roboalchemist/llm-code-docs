# Source: https://crawlee.dev/js/api/stagehand-crawler/interface/StagehandHook.md

# StagehandHook<!-- -->

Hook function for StagehandCrawler.

### Hierarchy

* [BrowserHook](https://crawlee.dev/js/api/browser-crawler.md#BrowserHook)<[StagehandCrawlingContext](https://crawlee.dev/js/api/stagehand-crawler/interface/StagehandCrawlingContext.md), [StagehandGotoOptions](https://crawlee.dev/js/api/stagehand-crawler.md#StagehandGotoOptions)>
  * *StagehandHook*

### Callable

* ****StagehandHook**(crawlingContext, gotoOptions): Awaitable\<void>

***

* #### Parameters

  * ##### crawlingContext: [StagehandCrawlingContext](https://crawlee.dev/js/api/stagehand-crawler/interface/StagehandCrawlingContext.md)\<Dictionary>
  * ##### gotoOptions: Dictionary & { referer?<!-- -->: string; timeout?<!-- -->: number; waitUntil?<!-- -->: domcontentloaded | load | networkidle | commit }

  #### Returns Awaitable\<void>
