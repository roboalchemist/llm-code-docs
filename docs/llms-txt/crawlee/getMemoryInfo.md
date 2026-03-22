# Source: https://crawlee.dev/js/api/utils/function/getMemoryInfo.md

# getMemoryInfo<!-- -->

### Callable

* ****getMemoryInfo**(): Promise<[MemoryInfo](https://crawlee.dev/js/api/utils/interface/MemoryInfo.md)>

***

* Returns memory statistics of the process and the system, see [MemoryInfo](https://crawlee.dev/js/api/utils/interface/MemoryInfo.md).

  If the process runs inside of Docker, the `getMemoryInfo` gets container memory limits, otherwise it gets system memory limits.

  Beware that the function is quite inefficient because it spawns a new process. Therefore you shouldn't call it too often, like more than once per second.

  ***

  #### Returns Promise<[MemoryInfo](https://crawlee.dev/js/api/utils/interface/MemoryInfo.md)>
