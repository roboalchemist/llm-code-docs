# Source: https://rolldown.rs/reference/InputOptions.watch.md

---
url: /reference/InputOptions.watch.md
---
# watch

* **Type**: `false` | object with the properties below
* **Optional**
* **Experimental**

Watch mode related options.

These options only take effect when running with the [`--watch`](/apis/cli#w-watch) flag, or using [`watch()`](Function.watch.md) API.

## buildDelay?

* **Type**: `number`
* **Optional**

Configures how long Rolldown will wait for further changes until it triggers
a rebuild in milliseconds.

Even if this value is set to 0, there's a small debounce timeout configured
in the file system watcher. Setting this to a value greater than 0 will mean
that Rolldown will only trigger a rebuild if there was no change for the
configured number of milliseconds. If several configurations are watched,
Rolldown will use the largest configured build delay.

This option is useful if you use a tool that regenerates multiple source files
very slowly. Rebuilding immediately after the first change could cause Rolldown
to generate a broken intermediate build before generating a successful final
build, which can be confusing and distracting.

### Default

```ts
0
```

## clearScreen?

* **Type**: `boolean`
* **Optional**

Whether to clear the screen when a rebuild is triggered.

### Default

```ts
true
```

## exclude?

* **Type**: `string` | `RegExp` | (`string` | `RegExp`)\[]
* **Optional**

Filter to prevent files from being watched.

Strings are treated as glob patterns.

### Example

```js
export default defineConfig({
  watch: {
    exclude: 'node_modules/**',
  },
})
```

### Default

```ts
[]
```

## include?

* **Type**: `string` | `RegExp` | (`string` | `RegExp`)\[]
* **Optional**

Filter to limit the file-watching to certain files.

Strings are treated as glob patterns.
Note that this only filters the module graph but does not allow adding
additional watch files.

### Example

```js
export default defineConfig({
  watch: {
    include: 'src/**',
  },
})
```

### Default

```ts
[]
```

## ~~notify?~~

* **Type**: [`WatcherFileWatcherOptions`](Interface.WatcherFileWatcherOptions.md)
* **Optional**

### Deprecated

Use [`watcher`](#watcher) instead.

## onInvalidate()?

* **Type**: (`id`) => `void`
* **Optional**

An optional function that will be called immediately every time
a module changes that is part of the build.

This is different from the [`watchChange`](Interface.Plugin.md#watchchange) plugin hook, which is
only called once the running build has finished. This may for
instance be used to prevent additional steps from being performed
if we know another build will be started anyway once the current
build finished. This callback may be called multiple times per
build as it tracks every change.

### Parameters

##### id

`string`

The id of the changed module.

### Returns

`void`

## skipWrite?

* **Type**: `boolean`
* **Optional**

Whether to skip the [`bundle.write()`](Interface.RolldownBuild.md#write) step when a rebuild is triggered.

### Default

```ts
false
```

## watcher?

* **Type**: [`WatcherFileWatcherOptions`](Interface.WatcherFileWatcherOptions.md)
* **Optional**

File watcher options for configuring how file changes are detected.
