# Source: https://crawlee.dev/js/api/utils/function/mergeAsyncIterables.md

# mergeAsyncIterables<!-- -->

### Callable

* ****mergeAsyncIterables**\<T>(...iterables): AsyncIterable\<T>

***

* Merges multiple async iterables into a single async iterable, yielding values concurrently.

  **Example usage:**

  ```
  const asyncIterable1 = async function* () {
    yield 1; yield 3; yield 5;
  };

  const asyncIterable2 = async function* () {
    yield 2; yield 4; yield 6;
  };

  for await (const value of mergeAsyncIterables(asyncIterable1(), asyncIterable2())) {
    console.log(value);
  }
  ```

  ***

  #### Parameters

  * ##### rest...iterables: AsyncIterable\<T, any, any>\[]

  #### Returns AsyncIterable\<T>
