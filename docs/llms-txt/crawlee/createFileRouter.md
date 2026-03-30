# Source: https://crawlee.dev/js/api/http-crawler/function/createFileRouter.md

# createFileRouter<!-- -->

### Callable

* ****createFileRouter**\<Context, UserData>(routes): [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>

***

* Creates new [Router](https://crawlee.dev/js/api/core/class/Router.md) instance that works based on request labels. This instance can then serve as a `requestHandler` of your [FileDownload](https://crawlee.dev/js/api/http-crawler/class/FileDownload.md). Defaults to the [FileDownloadCrawlingContext](https://crawlee.dev/js/api/http-crawler/interface/FileDownloadCrawlingContext.md).

  > Serves as a shortcut for using `Router.create<FileDownloadCrawlingContext>()`.

  ```
  import { FileDownload, createFileRouter } from 'crawlee';

  const router = createFileRouter();
  router.addHandler('label-a', async (ctx) => {
     ctx.log.info('...');
  });
  router.addDefaultHandler(async (ctx) => {
     ctx.log.info('...');
  });

  const crawler = new FileDownload({
      requestHandler: router,
  });
  await crawler.run();
  ```

  ***

  #### Parameters

  * ##### optionalroutes: [RouterRoutes](https://crawlee.dev/js/api/core.md#RouterRoutes)\<Context, UserData>

  #### Returns [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>
