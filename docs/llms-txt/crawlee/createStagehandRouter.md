# Source: https://crawlee.dev/js/api/stagehand-crawler/function/createStagehandRouter.md

# createStagehandRouter<!-- -->

### Callable

* ****createStagehandRouter**\<Context, UserData>(routes): [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>

***

* Creates a new router for StagehandCrawler with type-safe route handlers.

  * **@example**

    ```
    const router = createStagehandRouter();

    router.addHandler('product', async ({ page, request, log }) => {
      log.info(`Processing product: ${request.url}`);
      const data = await page.extract('Get product info', schema);
    });

    router.addDefaultHandler(async ({ page, enqueueLinks }) => {
      await enqueueLinks({ globs: ['https://example.com/products/*'] });
    });

    const crawler = new StagehandCrawler({
      requestHandler: router,
    });
    ```

  ***

  #### Parameters

  * ##### optionalroutes: [RouterRoutes](https://crawlee.dev/js/api/core.md#RouterRoutes)\<Context, UserData>

  #### Returns [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<Context>

  Configured router instance
