# Source: https://crawlee.dev/js/api/utils/function/sleep.md

# sleep<!-- -->

### Callable

* ****sleep**(millis): Promise\<void>

***

* Returns a `Promise` that resolves after a specific period of time. This is useful to implement waiting in your code, e.g. to prevent overloading of target website or to avoid bot detection.

  **Example usage:**

  ```
  import { sleep } from 'crawlee';

  ...

  // Sleep 1.5 seconds
  await sleep(1500);
  ```

  ***

  #### Parameters

  * ##### optionalmillis: number

    Period of time to sleep, in milliseconds. If not a positive number, the returned promise resolves immediately.

  #### Returns Promise\<void>
