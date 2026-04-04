# Source: https://crawlee.dev/js/api/core/interface/KeyConsumer.md

# KeyConsumer<!-- -->

User-function used in the [KeyValueStore.forEachKey](https://crawlee.dev/js/api/core/class/KeyValueStore.md#forEachKey) method.

### Callable

* ****KeyConsumer**(key, index, info): Awaitable\<void>

***

* #### Parameters

  * ##### key: string

    Current [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md) key being processed.

  * ##### index: number

    Position of the current key in [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md).

  * ##### info: { size: number }

    Information about the current [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md) entry.

    * ##### size: number

      Size of the value associated with the current key in bytes.

  #### Returns Awaitable\<void>
