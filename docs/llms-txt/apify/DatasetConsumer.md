# Source: https://docs.apify.com/sdk/js/reference/interface/DatasetConsumer.md

# externalDatasetConsumer<!-- --> \<Data>

User-function used in the `Dataset.forEach()` API.

### Callable

* ****DatasetConsumer**(item, index): Awaitable\<void>

***

* #### Parameters

  * ##### externalitem: Data

    Current [Dataset](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md) entry being processed.

  * ##### externalindex: number

    Position of current [Dataset](https://docs.apify.com/sdk/js/sdk/js/reference/class/Dataset.md) entry.

  #### Returns Awaitable\<void>
