# Source: https://rolldown.rs/reference/InputOptions.onLog.md

---
url: /reference/InputOptions.onLog.md
---
# onLog()

* **Type**: (`level`, `log`, `defaultHandler`) => `void`
* **Optional**

A function that intercepts log messages. If not supplied, logs are printed to the console.

This handler will not be invoked if logs are filtered out by the [`logLevel`](/reference/InputOptions.logLevel) option. I.e. by default, `"debug"` logs will be swallowed.

If the default handler is not invoked, the log will not be printed to the console. Moreover, you can change the log level by invoking the default handler with a different level. Using the additional level `"error"` will turn the log into a thrown error that has all properties of the log attached.

## Parameters

### level

`"info"` | `"debug"` | `"warn"`

### log

[`RolldownLog`](Interface.RolldownLog.md)

### defaultHandler

[`LogOrStringHandler`](TypeAlias.LogOrStringHandler.md)

## Returns

`void`

## Example

```js
export default defineConfig({
  onLog(level, log, defaultHandler) {
    if (log.code === 'CIRCULAR_DEPENDENCY') {
      return; // Ignore circular dependency warnings
    }
    if (level === 'warn') {
      defaultHandler('error', log); // turn other warnings into errors
    } else {
      defaultHandler(level, log); // otherwise, just print the log
    }
  }
})
```
