# Source: https://crawlee.dev/js/api/core/interface/DatasetMapper.md

# DatasetMapper<!-- --> \<Data, R>

User-function used in the `Dataset.map()` API.

### Callable

* ****DatasetMapper**(item, index): Awaitable\<R>

***

* User-function used in the `Dataset.map()` API.

  ***

  #### Parameters

  * ##### item: Data

    Current [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) entry being processed.

  * ##### index: number

    Position of current [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) entry.

  #### Returns Awaitable\<R>
