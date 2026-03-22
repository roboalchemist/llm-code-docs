# Source: https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerRequestInterception.md

# puppeteerRequestInterception<!-- -->

## Index[**](#Index)

### Type Aliases

* [**InterceptHandler](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerRequestInterception.md#InterceptHandler)

### Functions

* [**addInterceptRequestHandler](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerRequestInterception.md#addInterceptRequestHandler)
* [**removeInterceptRequestHandler](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerRequestInterception.md#removeInterceptRequestHandler)

## Type Aliases<!-- -->[**](<#Type Aliases>)

### [**](#InterceptHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_request_interception.ts#L9)InterceptHandler

**InterceptHandler: (request) => unknown

#### Type declaration

* * **(request): unknown

  - #### Parameters

    * ##### request: PuppeteerRequest

    #### Returns unknown

## Functions<!-- -->[**](#Functions)

### [**](#addInterceptRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_request_interception.ts#L160)addInterceptRequestHandler

* ****addInterceptRequestHandler**(page, handler): Promise\<void>

- Adds request interception handler in similar to `page.on('request', handler);` but in addition to that supports multiple parallel handlers.

  All the handlers are executed sequentially in the order as they were added. Each of the handlers must call one of `request.continue()`, `request.abort()` and `request.respond()`. In addition to that any of the handlers may modify the request object (method, postData, headers) by passing its overrides to `request.continue()`. If multiple handlers modify same property then the last one wins. Headers are merged separately so you can override only a value of specific header.

  If one the handlers calls `request.abort()` or `request.respond()` then request is not propagated further to any of the remaining handlers.

  **Example usage:**

  ```
  // Replace images with placeholder.
  await addInterceptRequestHandler(page, (request) => {
      if (request.resourceType() === 'image') {
          return request.respond({
              statusCode: 200,
              contentType: 'image/jpeg',
              body: placeholderImageBuffer,
          });
      }
      return request.continue();
  });

  // Abort all the scripts.
  await addInterceptRequestHandler(page, (request) => {
      if (request.resourceType() === 'script') return request.abort();
      return request.continue();
  });

  // Change requests to post.
  await addInterceptRequestHandler(page, (request) => {
      return request.continue({
           method: 'POST',
      });
  });

  await page.goto('http://example.com');
  ```

  ***

  #### Parameters

  * ##### page: Page

    Puppeteer [`Page`](https://pptr.dev/#?product=Puppeteer\&show=api-class-page) object.

  * ##### handler: [InterceptHandler](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerRequestInterception.md#InterceptHandler)

    Request interception handler.

  #### Returns Promise\<void>

### [**](#removeInterceptRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_request_interception.ts#L203)removeInterceptRequestHandler

* ****removeInterceptRequestHandler**(page, handler): Promise\<void>

- Removes request interception handler for given page.

  ***

  #### Parameters

  * ##### page: Page

    Puppeteer [`Page`](https://pptr.dev/#?product=Puppeteer\&show=api-class-page) object.

  * ##### handler: [InterceptHandler](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerRequestInterception.md#InterceptHandler)

    Request interception handler.

  #### Returns Promise\<void>
