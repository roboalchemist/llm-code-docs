# Source: https://crawlee.dev/js/api/http-crawler/function/createHttpRouter.md

# createHttpRouter<!-- -->

### Callable

* ****createHttpRouter**\<Context, UserData>(routes): [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>

***

* Creates new [Router](https://crawlee.dev/js/api/core/class/Router.md) instance that works based on request labels. This instance can then serve as a `requestHandler` of your [HttpCrawler](https://crawlee.dev/js/api/http-crawler/class/HttpCrawler.md). Defaults to the [HttpCrawlingContext](https://crawlee.dev/js/api/http-crawler/interface/HttpCrawlingContext.md).

  > Serves as a shortcut for using `Router.create<HttpCrawlingContext>()`.

  ```
  import { HttpCrawler, createHttpRouter } from 'crawlee';

  const router = createHttpRouter();
  router.addHandler('label-a', async (ctx) => {
     ctx.log.info('...');
  });
  router.addDefaultHandler(async (ctx) => {
     ctx.log.info('...');
  });

  const crawler = new HttpCrawler({
      requestHandler: router,
  });
  await crawler.run();
  ```

  ***

  #### Parameters

  * ##### optionalroutes: [RouterRoutes](https://crawlee.dev/js/api/core.md#RouterRoutes)\<Context, UserData>

  #### Returns [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>
