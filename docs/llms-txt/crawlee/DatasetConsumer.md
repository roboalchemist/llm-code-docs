# Source: https://crawlee.dev/js/api/core/interface/DatasetConsumer.md

# DatasetConsumer<!-- --> \<Data>

User-function used in the `Dataset.forEach()` API.

### Callable

* ****DatasetConsumer**(item, index): Awaitable\<void>

***

* #### Parameters

  * ##### item: Data

    Current [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) entry being processed.

  * ##### index: number

    Position of current [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) entry.

  #### Returns Awaitable\<void>
