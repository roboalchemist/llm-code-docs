# Source: https://crawlee.dev/js/api/puppeteer-crawler/function/createPuppeteerRouter.md

# createPuppeteerRouter<!-- -->

### Callable

* ****createPuppeteerRouter**\<Context, UserData>(routes): [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>

***

* Creates new [Router](https://crawlee.dev/js/api/core/class/Router.md) instance that works based on request labels. This instance can then serve as a `requestHandler` of your [PuppeteerCrawler](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md). Defaults to the [PuppeteerCrawlingContext](https://crawlee.dev/js/api/puppeteer-crawler/interface/PuppeteerCrawlingContext.md).

  > Serves as a shortcut for using `Router.create<PuppeteerCrawlingContext>()`.

  ```
  import { PuppeteerCrawler, createPuppeteerRouter } from 'crawlee';

  const router = createPuppeteerRouter();
  router.addHandler('label-a', async (ctx) => {
     ctx.log.info('...');
  });
  router.addDefaultHandler(async (ctx) => {
     ctx.log.info('...');
  });

  const crawler = new PuppeteerCrawler({
      requestHandler: router,
  });
  await crawler.run();
  ```

  ***

  #### Parameters

  * ##### optionalroutes: [RouterRoutes](https://crawlee.dev/js/api/core.md#RouterRoutes)\<Context, UserData>

  #### Returns [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>
