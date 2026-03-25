# Source: https://crawlee.dev/js/api/core/interface/RequestTransform.md

# RequestTransform<!-- -->

Takes an Apify [RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md) object and changes its attributes in a desired way. This user-function is used enqueueLinks to modify requests before enqueuing them.

### Callable

* ****RequestTransform**(original): undefined | null | false | [RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)\<Dictionary>

***

- ***

  #### Parameters

  * ##### original: [RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)\<Dictionary>

    Request options to be modified.

  #### Returns undefined | null | false | [RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)\<Dictionary>

  The modified request options to enqueue.
