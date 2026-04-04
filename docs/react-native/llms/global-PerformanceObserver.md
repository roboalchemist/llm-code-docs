# Source: https://reactnative.dev/docs/global-PerformanceObserver.md

# PerformanceObserver

The global [`PerformanceObserver`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver) class, as defined in Web specifications.

## Example[​](#example "Direct link to Example")

ts

```
const observer = new PerformanceObserver(
  (list, observer, options) => {
    for (const entry of list.getEntries()) {
      console.log(
        'Received entry with type',
        entry.entryType,
        'and name',
        entry.name,
        'that started at',
        entry.startTime,
        'and took',
        entry.duration,
        'ms',
      );
    }
  },
);

observer.observe({entryTypes: ['mark', 'measure']});
```

***

# Reference

## Constructor[​](#constructor "Direct link to Constructor")

### `PerformanceObserver()`[​](#performanceobserver "Direct link to performanceobserver")

See [documentation in MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver/PerformanceObserver).

## Static properties[​](#static-properties "Direct link to Static properties")

### `supportedEntryTypes`[​](#supportedentrytypes "Direct link to supportedentrytypes")

See [documentation in MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver/supportedEntryTypes).

Returns `['mark', 'measure', 'event', 'longtask']`.

## Instance methods[​](#instance-methods "Direct link to Instance methods")

### `observe()`[​](#observe "Direct link to observe")

See [documentation in MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver/observe).

### `disconnect()`[​](#disconnect "Direct link to disconnect")

See [documentation in MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver/disconnect).
