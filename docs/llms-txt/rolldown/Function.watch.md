# Source: https://rolldown.rs/reference/Function.watch.md

---
url: /reference/Function.watch.md
---
# Function: watch()

* **Type**: (`input`: [`WatchOptions`](Interface.WatchOptions.md) | [`WatchOptions`](Interface.WatchOptions.md)\[]) => [`RolldownWatcher`](Interface.RolldownWatcher.md)
* **Experimental**

The API compatible with Rollup's `watch` function.

This function will rebuild the bundle when it detects that the individual modules have changed on disk.

Note that when using this function, it is your responsibility to call `event.result.close()` in response to the `BUNDLE_END` event to avoid resource leaks.

## Parameters

### input

The watch options object or the list of them.

[`WatchOptions`](Interface.WatchOptions.md) | [`WatchOptions`](Interface.WatchOptions.md)\[]

## Returns

[`RolldownWatcher`](Interface.RolldownWatcher.md)

A watcher object.

## Example

```js
import { watch } from 'rolldown';

const watcher = watch({ /* ... */ });
watcher.on('event', (event) => {
  if (event.code === 'BUNDLE_END') {
    console.log(event.duration);
    event.result.close();
  }
});

// Stop watching
watcher.close();
```
