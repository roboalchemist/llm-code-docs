# Source: https://rolldown.rs/reference/Interface.WatcherFileWatcherOptions.md

---
url: /reference/Interface.WatcherFileWatcherOptions.md
---
# Interface: WatcherFileWatcherOptions

## Properties

### compareContentsForPolling?

* **Type**: `boolean`
* **Optional**

Whether to compare file contents for poll-based watchers.
When enabled, poll watchers will check file contents to determine if they actually changed.

This option is only used when [`usePolling`](#usepolling) is `true`.

#### Default

```ts
false
```

***

### debounceDelay?

* **Type**: `number`
* **Optional**

Debounce delay in milliseconds for fs-level debounced watchers.
Only used when [`useDebounce`](#usedebounce) is `true`.

#### Default

```ts
10
```

***

### debounceTickRate?

* **Type**: `number`
* **Optional**

Tick rate in milliseconds for the debouncer's internal polling.
Only used when [`useDebounce`](#usedebounce) is `true`.
When undefined, auto-selects 1/4 of debounceDelay.

***

### pollInterval?

* **Type**: `number`
* **Optional**

Interval between each poll in milliseconds.

This option is only used when [`usePolling`](#usepolling) is `true`.

#### Default

```ts
100
```

***

### useDebounce?

* **Type**: `boolean`
* **Optional**

Whether to use debounced event delivery at the filesystem level.
This coalesces rapid filesystem events before they reach the build coordinator.

#### Default

```ts
false
```

***

### usePolling?

* **Type**: `boolean`
* **Optional**

Whether to use polling-based file watching instead of native OS events.

Polling is useful for environments where native FS events are unreliable,
such as network mounts, Docker volumes, or WSL2.

#### Default

```ts
false
```
