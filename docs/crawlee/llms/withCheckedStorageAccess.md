# Source: https://crawlee.dev/js/api/core/function/withCheckedStorageAccess.md

# withCheckedStorageAccess<!-- -->

Define a storage access checker function that should be used by calls to [checkStorageAccess](https://crawlee.dev/js/api/core/function/checkStorageAccess.md) in the callbacks.

### Callable

* ****withCheckedStorageAccess**\<T>(checkFunction, callback): Promise\<T>

***

* #### Parameters

  * ##### checkFunction: () => void

    The check function that should be invoked by [checkStorageAccess](https://crawlee.dev/js/api/core/function/checkStorageAccess.md) calls

  *

    ##### callback: () => Awaitable\<T>

    The code that should be invoked with the `checkFunction` setting



  #### Returns Promise\<T>
