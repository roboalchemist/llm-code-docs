# Source: https://crawlee.dev/js/api/core/interface/DatasetReducer.md

# DatasetReducer<!-- --> \<T, Data>

User-function used in the `Dataset.reduce()` API.

### Callable

* ****DatasetReducer**(memo, item, index): Awaitable\<T>

***

* #### Parameters

  * ##### memo: T

    Previous state of the reduction.

  * ##### item: Data

    Current [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) entry being processed.

  * ##### index: number

    Position of current [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) entry.

  #### Returns Awaitable\<T>
