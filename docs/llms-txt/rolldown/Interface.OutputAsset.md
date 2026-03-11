# Source: https://rolldown.rs/reference/Interface.OutputAsset.md

---
url: /reference/Interface.OutputAsset.md
---
# Interface: OutputAsset

The information about an asset in the generated bundle.

## Extends

* `ExternalMemoryHandle`

## Properties

### fileName

* **Type**: `string`

The file name of this asset.

***

### ~~name~~

* **Type**: `string` | `undefined`

#### Deprecated

Use [`names`](#names) instead.

***

### names

* **Type**: `string`\[]

***

### ~~originalFileName~~

* **Type**: `string` | `null`

#### Deprecated

Use [`originalFileNames`](#originalfilenames) instead.

***

### originalFileNames

* **Type**: `string`\[]

The list of the absolute paths to the original file of this asset.

***

### source

* **Type**: `string` | `Uint8Array`<`ArrayBufferLike`>

The content of this asset.

***

### type

* **Type**: `"asset"`
