# Source: https://docs.apify.com/sdk/js/reference/interface/KeyConsumer.md

# externalKeyConsumer<!-- -->

User-function used in the [KeyValueStore.forEachKey](https://docs.apify.com/sdk/js/sdk/js/reference/class/KeyValueStore.md#forEachKey) method.

### Callable

* ****KeyConsumer**(key, index, info): Awaitable\<void>

***

* #### Parameters

  * ##### externalkey: string

    Current [KeyValueStore](https://docs.apify.com/sdk/js/sdk/js/reference/class/KeyValueStore.md) key being processed.

  * ##### externalindex: number

    Position of the current key in [KeyValueStore](https://docs.apify.com/sdk/js/sdk/js/reference/class/KeyValueStore.md).

  * ##### externalinfo: { size: number }

    Information about the current [KeyValueStore](https://docs.apify.com/sdk/js/sdk/js/reference/class/KeyValueStore.md) entry.

    * ##### externalsize: number

      Size of the value associated with the current key in bytes.

  #### Returns Awaitable\<void>
