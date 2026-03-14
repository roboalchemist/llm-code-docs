# Source: https://rolldown.rs/reference/Interface.EmittedAsset.md

---
url: /reference/Interface.EmittedAsset.md
---
# Interface: EmittedAsset

Either a [`name`](#name) or a [`fileName`](#filename) can be supplied.
If a [`fileName`](#filename) is provided, it will be used unmodified as the name
of the generated file, throwing an error if this causes a conflict.
Otherwise, if a [`name`](#name) is supplied, this will be used as substitution
for `[name]` in the corresponding
[`output.assetFileNames`](Interface.OutputOptions.md#assetfilenames) pattern, possibly
adding a unique number to the end of the file name to avoid conflicts.
If neither a [`name`](#name) nor [`fileName`](#filename) is supplied, a default name will be used.

## Properties

### fileName?

* **Type**: `string`
* **Optional**

***

### name?

* **Type**: `string`
* **Optional**

***

### originalFileName?

* **Type**: `string`
* **Optional**

An absolute path to the original file if this asset corresponds to a file on disk.

This property will be passed on to subsequent plugin hooks that receive a
[`PreRenderedAsset`](Interface.PreRenderedAsset.md) or an [`OutputAsset`](Interface.OutputAsset.md) like
[`generateBundle`](Interface.Plugin.md#generatebundle).
In watch mode, Rolldown will also automatically watch this file for changes and
trigger a rebuild if it changes. Therefore, it is not necessary to call
[`this.addWatchFile`](Interface.PluginContext.md#addwatchfile) for this file.

***

### source

* **Type**: `string` | `Uint8Array`<`ArrayBufferLike`>

***

### type

* **Type**: `"asset"`
