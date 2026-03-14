# Source: https://rolldown.rs/reference/Interface.PreRenderedAsset.md

---
url: /reference/Interface.PreRenderedAsset.md
---
# Interface: PreRenderedAsset

## Properties

### ~~name?~~

* **Type**: `string`
* **Optional**

#### Deprecated

Use [`names`](#names) instead.

***

### names

* **Type**: `string`\[]

***

### ~~originalFileName?~~

* **Type**: `string`
* **Optional**

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
