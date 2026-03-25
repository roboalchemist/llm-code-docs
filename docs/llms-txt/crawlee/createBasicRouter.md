# Source: https://crawlee.dev/js/api/basic-crawler/function/createBasicRouter.md

# createBasicRouter<!-- -->

### Callable

* ****createBasicRouter**\<Context, UserData>(routes): [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>

***

* Creates new [Router](https://crawlee.dev/js/api/core/class/Router.md) instance that works based on request labels. This instance can then serve as a [`requestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestHandler) of our [BasicCrawler](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md). Defaults to the [BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md).

  > Serves as a shortcut for using `Router.create<BasicCrawlingContext>()`.

  ```
  import { BasicCrawler, createBasicRouter } from 'crawlee';

  const router = createBasicRouter();
  router.addHandler('label-a', async (ctx) => {
     ctx.log.info('...');
  });
  router.addDefaultHandler(async (ctx) => {
     ctx.log.info('...');
  });

  const crawler = new BasicCrawler({
      requestHandler: router,
  });
  await crawler.run();
  ```

  ***

  #### Parameters

  * ##### optionalroutes: [RouterRoutes](https://crawlee.dev/js/api/core.md#RouterRoutes)\<Context, UserData>

  #### Returns [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>
