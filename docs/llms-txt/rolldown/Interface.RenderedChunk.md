# Source: https://rolldown.rs/reference/Interface.RenderedChunk.md

---
url: /reference/Interface.RenderedChunk.md
---
# Interface: RenderedChunk

The information about the chunk being rendered.

Unlike [OutputChunk](Interface.OutputChunk.md), `code` and `map` are not set as the chunk has not been rendered yet.
All referenced chunk file names in each property that would contain hashes will contain hash placeholders instead.

## Extends

* `Omit`<`BindingRenderedChunk`, `"modules"`>

## Properties

### dynamicImports

* **Type**: `string`\[]

External modules imported dynamically by this chunk.

#### Overrides

`Omit.dynamicImports`

***

### exports

* **Type**: `string`\[]

Exported variable names from this chunk.

#### Overrides

`Omit.exports`

***

### facadeModuleId

* **Type**: `string` | `null`

The id of a module that this chunk corresponds to.

#### Overrides

`Omit.facadeModuleId`

***

### fileName

* **Type**: `string`

The preliminary file name of this chunk with hash placeholders.

#### Overrides

`Omit.fileName`

***

### imports

* **Type**: `string`\[]

External modules imported statically by this chunk.

#### Overrides

`Omit.imports`

***

### isDynamicEntry

* **Type**: `boolean`

Whether this chunk is a dynamic entry point.

#### Overrides

`Omit.isDynamicEntry`

***

### isEntry

* **Type**: `boolean`

Whether this chunk is a static entry point.

#### Overrides

`Omit.isEntry`

***

### moduleIds

* **Type**: `string`\[]

The list of ids of modules included in this chunk.

#### Overrides

`Omit.moduleIds`

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

#### Overrides

`Omit.name`

***

### type

* **Type**: `"chunk"`
