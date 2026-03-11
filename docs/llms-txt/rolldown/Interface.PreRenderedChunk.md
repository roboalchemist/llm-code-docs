# Source: https://rolldown.rs/reference/Interface.PreRenderedChunk.md

---
url: /reference/Interface.PreRenderedChunk.md
---
# Interface: PreRenderedChunk

## Properties

### exports

* **Type**: `string`\[]

Exported variable names from this chunk.

***

### facadeModuleId?

* **Type**: `string`
* **Optional**

The id of a module that this chunk corresponds to.

***

### isDynamicEntry

* **Type**: `boolean`

Whether this chunk is a dynamic entry point.

***

### isEntry

* **Type**: `boolean`

Whether this chunk is a static entry point.

***

### moduleIds

* **Type**: `string`\[]

The list of ids of modules included in this chunk.

***

### name

* **Type**: `string`

The name of this chunk, which is used in naming patterns.
