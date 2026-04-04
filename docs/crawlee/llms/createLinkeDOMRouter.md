# Source: https://crawlee.dev/js/api/linkedom-crawler/function/createLinkeDOMRouter.md

# createLinkeDOMRouter<!-- -->

### Callable

* ****createLinkeDOMRouter**\<Context, UserData>(routes): [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>

***

* Creates new [Router](https://crawlee.dev/js/api/core/class/Router.md) instance that works based on request labels. This instance can then serve as a `requestHandler` of your [LinkeDOMCrawler](https://crawlee.dev/js/api/linkedom-crawler/class/LinkeDOMCrawler.md). Defaults to the [LinkeDOMCrawlingContext](https://crawlee.dev/js/api/linkedom-crawler/interface/LinkeDOMCrawlingContext.md).

  > Serves as a shortcut for using `Router.create<LinkeDOMCrawlingContext>()`.

  ```
  import { LinkeDOMCrawler, createLinkeDOMRouter } from 'crawlee';

  const router = createLinkeDOMRouter();
  router.addHandler('label-a', async (ctx) => {
     ctx.log.info('...');
  });
  router.addDefaultHandler(async (ctx) => {
     ctx.log.info('...');
  });

  const crawler = new LinkeDOMCrawler({
      requestHandler: router,
  });
  await crawler.run();
  ```

  ***

  #### Parameters

  * ##### optionalroutes: [RouterRoutes](https://crawlee.dev/js/api/core.md#RouterRoutes)\<Context, UserData>

  #### Returns [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>
