# Source: https://crawlee.dev/js/api/cheerio-crawler/function/createCheerioRouter.md

# createCheerioRouter<!-- -->

### Callable

* ****createCheerioRouter**\<Context, UserData>(routes): [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>

***

* Creates new [Router](https://crawlee.dev/js/api/core/class/Router.md) instance that works based on request labels. This instance can then serve as a `requestHandler` of your [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md). Defaults to the [CheerioCrawlingContext](https://crawlee.dev/js/api/cheerio-crawler/interface/CheerioCrawlingContext.md).

  > Serves as a shortcut for using `Router.create<CheerioCrawlingContext>()`.

  ```
  import { CheerioCrawler, createCheerioRouter } from 'crawlee';

  const router = createCheerioRouter();
  router.addHandler('label-a', async (ctx) => {
     ctx.log.info('...');
  });
  router.addDefaultHandler(async (ctx) => {
     ctx.log.info('...');
  });

  const crawler = new CheerioCrawler({
      requestHandler: router,
  });
  await crawler.run();
  ```

  ***

  #### Parameters

  * ##### optionalroutes: [RouterRoutes](https://crawlee.dev/js/api/core.md#RouterRoutes)\<Context, UserData>

  #### Returns [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>
