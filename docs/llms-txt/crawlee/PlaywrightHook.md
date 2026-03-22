# Source: https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightHook.md

# PlaywrightHook<!-- -->

### Hierarchy

* [BrowserHook](https://crawlee.dev/js/api/browser-crawler.md#BrowserHook)<[PlaywrightCrawlingContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlingContext.md), [PlaywrightGotoOptions](https://crawlee.dev/js/api/playwright-crawler.md#PlaywrightGotoOptions)>
  * *PlaywrightHook*

### Callable

* ****PlaywrightHook**(crawlingContext, gotoOptions): Awaitable\<void>

***

* #### Parameters

  * ##### crawlingContext: [PlaywrightCrawlingContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlingContext.md)\<Dictionary>
  * ##### gotoOptions: Dictionary & { referer?<!-- -->: string; timeout?<!-- -->: number; waitUntil?<!-- -->: domcontentloaded | load | networkidle | commit }

  #### Returns Awaitable\<void>
