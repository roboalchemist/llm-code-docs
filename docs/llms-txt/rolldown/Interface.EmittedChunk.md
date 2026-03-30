# Source: https://rolldown.rs/reference/Interface.EmittedChunk.md

---
url: /reference/Interface.EmittedChunk.md
---
# Interface: EmittedChunk

Either a [`name`](#name) or a [`fileName`](#filename) can be supplied.
If a [`fileName`](#filename) is provided, it will be used unmodified as the name
of the generated file, throwing an error if this causes a conflict.
Otherwise, if a [`name`](#name) is supplied, this will be used as substitution
for `[name]` in the corresponding
[`output.chunkFileNames`](Interface.OutputOptions.md#chunkfilenames) pattern, possibly
adding a unique number to the end of the file name to avoid conflicts.
If neither a [`name`](#name) nor [`fileName`](#filename) is supplied, a default name will be used.

## Properties

### fileName?

* **Type**: `string`
* **Optional**

***

### id

* **Type**: `string`

The module id of the entry point of the chunk.

It will be passed through build hooks just like regular entry points,
starting with [`resolveId`](Interface.Plugin.md#resolveid).

***

### importer?

* **Type**: `string`
* **Optional**

The value to be passed to [`resolveId`](Interface.Plugin.md#resolveid)'s [`importer`](#importer) parameter when resolving the entry point.
This is important to properly resolve relative paths. If it is not provided,
paths will be resolved relative to the current working directory.

***

### name?

* **Type**: `string`
* **Optional**

***

### preserveSignature?

* **Type**: `false` | `"strict"` | `"allow-extension"` | `"exports-only"`
* **Optional**

When provided, this will override
[`preserveEntrySignatures`](Interface.InputOptions.md#preserveentrysignatures) for this particular
chunk.

***

### type

* **Type**: `"chunk"`
