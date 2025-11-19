# Source: https://docs.apify.com/sdk/js/reference/interface/DatasetReducer.md

# externalDatasetReducer<!-- --> \<T, Data>

User-function used in the `Dataset.reduce()` API.

### Callable

* ****DatasetReducer**(memo, item, index): Awaitable\<T>

***

* #### Parameters

  * ##### externalmemo: T

    Previous state of the reduction.

  * ##### externalitem: Data

    Current [Dataset](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md) entry being processed.

  * ##### externalindex: number

    Position of current [Dataset](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md) entry.

  #### Returns Awaitable\<T>
