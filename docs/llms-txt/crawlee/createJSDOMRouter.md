# Source: https://crawlee.dev/js/api/jsdom-crawler/function/createJSDOMRouter.md

# createJSDOMRouter<!-- -->

### Callable

* ****createJSDOMRouter**\<Context, UserData>(routes): [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>

***

* Creates new [Router](https://crawlee.dev/js/api/core/class/Router.md) instance that works based on request labels. This instance can then serve as a `requestHandler` of your [JSDOMCrawler](https://crawlee.dev/js/api/jsdom-crawler/class/JSDOMCrawler.md). Defaults to the [JSDOMCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlingContext.md).

  > Serves as a shortcut for using `Router.create<JSDOMCrawlingContext>()`.

  ```
  import { JSDOMCrawler, createJSDOMRouter } from 'crawlee';

  const router = createJSDOMRouter();
  router.addHandler('label-a', async (ctx) => {
     ctx.log.info('...');
  });
  router.addDefaultHandler(async (ctx) => {
     ctx.log.info('...');
  });

  const crawler = new JSDOMCrawler({
      requestHandler: router,
  });
  await crawler.run();
  ```

  ***

  #### Parameters

  * ##### optionalroutes: [RouterRoutes](https://crawlee.dev/js/api/core.md#RouterRoutes)\<Context, UserData>

  #### Returns [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>
