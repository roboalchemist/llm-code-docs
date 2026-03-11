# Source: https://rolldown.rs/reference/InputOptions.onwarn.md

---
url: /reference/InputOptions.onwarn.md
---
# ~~onwarn()~~

* **Type**: (`warning`, `defaultHandler`) => `void`
* **Optional**

A function that will intercept warning messages.

If the default handler is invoked, the log will be handled as a warning. If both an `onLog` and `onwarn` handler are provided, the `onwarn` handler will only be invoked if `onLog` calls its default handler with a `level` of `"warn"`.

## Parameters

### warning

[`RolldownLog`](Interface.RolldownLog.md)

### defaultHandler

(`warning`) => `void`

## Returns

`void`

## Deprecated

This is a legacy API. Consider using [`onLog`](./InputOptions.onLog) instead for better control over all log types.

To migrate from `onwarn` to `onLog`, check the `level` parameter to filter for warnings:

```js
// Before: Using `onwarn`
export default {
  onwarn(warning, defaultHandler) {
    // Suppress certain warnings
    if (warning.code === 'CIRCULAR_DEPENDENCY') return;
    // Handle other warnings with default behavior
    defaultHandler(warning);
  },
};
```

```js
// After: Using `onLog`
export default {
  onLog(level, log, defaultHandler) {
    // Handle only warnings (same behavior as `onwarn`)
    if (level === 'warn') {
      // Suppress certain warnings
      if (log.code === 'CIRCULAR_DEPENDENCY') return;
      // Handle other warnings with default behavior
      defaultHandler(level, log);
    } else {
      // Let other log levels pass through
      defaultHandler(level, log);
    }
  },
};
```
