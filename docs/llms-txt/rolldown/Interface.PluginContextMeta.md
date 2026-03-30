# Source: https://rolldown.rs/reference/Interface.PluginContextMeta.md

---
url: /reference/Interface.PluginContextMeta.md
---
# Interface: PluginContextMeta

## Properties

### rolldownVersion

* **Type**: `string`

The currently running version of Rolldown.

#### Example

```ts
`'1.0.0'`
```

***

### rollupVersion

* **Type**: `string`

A property for Rollup compatibility. A dummy value is set by Rolldown.

#### Example

```ts
`'4.23.0'`
```

***

### watchMode

* **Type**: `boolean`

Whether Rolldown was started via [`rolldown.watch()`](Function.watch.md) or
from the command line with `--watch`.
