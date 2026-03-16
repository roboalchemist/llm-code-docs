# Source: https://crawlee.dev/js/api/playwright-crawler/function/createPlaywrightRouter.md

# createPlaywrightRouter<!-- -->

### Callable

* ****createPlaywrightRouter**\<Context, UserData>(routes): [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>

***

* Creates new [Router](https://crawlee.dev/js/api/core/class/Router.md) instance that works based on request labels. This instance can then serve as a `requestHandler` of your [PlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md). Defaults to the [PlaywrightCrawlingContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlingContext.md).

  > Serves as a shortcut for using `Router.create<PlaywrightCrawlingContext>()`.

  ```
  import { PlaywrightCrawler, createPlaywrightRouter } from 'crawlee';

  const router = createPlaywrightRouter();
  router.addHandler('label-a', async (ctx) => {
     ctx.log.info('...');
  });
  router.addDefaultHandler(async (ctx) => {
     ctx.log.info('...');
  });

  const crawler = new PlaywrightCrawler({
      requestHandler: router,
  });
  await crawler.run();
  ```

  ***

  #### Parameters

  * ##### optionalroutes: [RouterRoutes](https://crawlee.dev/js/api/core.md#RouterRoutes)\<Context, UserData>

  #### Returns [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>
