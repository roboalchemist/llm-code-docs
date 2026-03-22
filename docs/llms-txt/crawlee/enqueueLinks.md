# Source: https://crawlee.dev/js/api/core/function/enqueueLinks.md

# enqueueLinks<!-- -->

### Callable

* ****enqueueLinks**(options): Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

***

* This function enqueues the urls provided to the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) provided. If you want to automatically find and enqueue links, you should use the context-aware `enqueueLinks` function provided on the crawler contexts.

  Optionally, the function allows you to filter the target links' URLs using an array of globs or regular expressions and override settings of the enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

  **Example usage**

  ```
  await enqueueLinks({
    urls: aListOfFoundUrls,
    requestQueue,
    selector: 'a.product-detail',
    globs: [
        'https://www.example.com/handbags/*',
        'https://www.example.com/purses/*'
    ],
  });
  ```

  ***

  #### Parameters

  * ##### options: { baseUrl?<!-- -->: string; exclude?<!-- -->: readonly<!-- --> ([GlobInput](https://crawlee.dev/js/api/core.md#GlobInput) | [RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput))\[]; forefront?<!-- -->: boolean; globs?<!-- -->: readonly<!-- --> [GlobInput](https://crawlee.dev/js/api/core.md#GlobInput)\[]; label?<!-- -->: string; limit?<!-- -->: number; onSkippedRequest?<!-- -->: [SkippedRequestCallback](https://crawlee.dev/js/api/core.md#SkippedRequestCallback); pseudoUrls?<!-- -->: readonly<!-- --> [PseudoUrlInput](https://crawlee.dev/js/api/core.md#PseudoUrlInput)\[]; regexps?<!-- -->: readonly<!-- --> [RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput)\[]; robotsTxtFile?<!-- -->: Pick<[RobotsTxtFile](https://crawlee.dev/js/api/utils/class/RobotsTxtFile.md), isAllowed>; selector?<!-- -->: string; skipNavigation?<!-- -->: boolean; strategy?<!-- -->: [EnqueueStrategy](https://crawlee.dev/js/api/core/enum/EnqueueStrategy.md) | all | same-domain | same-hostname | same-origin; transformRequestFunction?<!-- -->: [RequestTransform](https://crawlee.dev/js/api/core/interface/RequestTransform.md); urls: readonly<!-- --> string\[]; userData?<!-- -->: Dictionary; waitForAllRequestsToBeAdded?<!-- -->: boolean } & { requestQueue: { addRequestsBatched: (requests, options) => Promise<[AddRequestsBatchedResult](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md)> } }

    All `enqueueLinks()` parameters are passed via an options object.

  #### Returns Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

  Promise that resolves to [BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md) object.
