# Source: https://docs.apify.com/sdk/js/reference/interface/DatasetMapper.md

# externalDatasetMapper<!-- --> \<Data, R>

User-function used in the `Dataset.map()` API.

### Callable

* ****DatasetMapper**(item, index): Awaitable\<R>

***

* User-function used in the `Dataset.map()` API.

  ***

  #### Parameters

  * ##### externalitem: Data

    Current [Dataset](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md) entry being processed.

  * ##### externalindex: number

    Position of current [Dataset](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md) entry.

  #### Returns Awaitable\<R>
