# Source: https://rolldown.rs/reference/Interface.EmittedPrebuiltChunk.md

---
url: /reference/Interface.EmittedPrebuiltChunk.md
---
# Interface: EmittedPrebuiltChunk

## Properties

### code

* **Type**: `string`

The code of this chunk.

***

### exports?

* **Type**: `string`\[]
* **Optional**

The list of exported variable names from this chunk.

This should be provided if the chunk exports any variables.

***

### facadeModuleId?

* **Type**: `string`
* **Optional**

The module id of the facade module for this chunk, if any.

***

### fileName

* **Type**: `string`

***

### isDynamicEntry?

* **Type**: `boolean`
* **Optional**

Whether this chunk corresponds to a dynamic entry point.

***

### isEntry?

* **Type**: `boolean`
* **Optional**

Whether this chunk corresponds to an entry point.

***

### map?

* **Type**: [`SourceMap`](Interface.SourceMap.md)
* **Optional**

The corresponding source map for this chunk.

***

### name?

* **Type**: `string`
* **Optional**

A semantic name for the chunk. If not provided, `fileName` will be used.

***

### sourcemapFileName?

* **Type**: `string`
* **Optional**

***

### type

* **Type**: `"prebuilt-chunk"`
