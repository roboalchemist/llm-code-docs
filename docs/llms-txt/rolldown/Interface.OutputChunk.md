# Source: https://rolldown.rs/reference/Interface.OutputChunk.md

---
url: /reference/Interface.OutputChunk.md
---
# Interface: OutputChunk

The information about a chunk in the generated bundle.

## Extends

* `ExternalMemoryHandle`

## Properties

### code

* **Type**: `string`

The generated code of this chunk.

***

### dynamicImports

* **Type**: `string`\[]

External modules imported dynamically by this chunk.

***

### exports

* **Type**: `string`\[]

Exported variable names from this chunk.

***

### facadeModuleId

* **Type**: `string` | `null`

The id of a module that this chunk corresponds to.

***

### fileName

* **Type**: `string`

The file name of this chunk.

***

### imports

* **Type**: `string`\[]

External modules imported statically by this chunk.

***

### isDynamicEntry

* **Type**: `boolean`

Whether this chunk is a dynamic entry point.

***

### isEntry

* **Type**: `boolean`

Whether this chunk is a static entry point.

***

### map

* **Type**: [`SourceMap`](Interface.SourceMap.md) | `null`

The source map of this chunk if present.

***

### moduleIds

* **Type**: `string`\[]

***

### modules

* **Type**: {\[`id`: `string`]: [`RenderedModule`](Interface.RenderedModule.md); }

Information about the modules included in this chunk.

#### Index Signature

\[`id`: `string`]: [`RenderedModule`](Interface.RenderedModule.md)

***

### name

* **Type**: `string`

The name of this chunk, which is used in naming patterns.

***

### preliminaryFileName

* **Type**: `string`

The preliminary file name of this chunk with hash placeholders.

***

### sourcemapFileName

* **Type**: `string` | `null`

***

### type

* **Type**: `"chunk"`
