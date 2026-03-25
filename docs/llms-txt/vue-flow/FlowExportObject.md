# Source: https://vueflow.dev/typedocs/interfaces/FlowExportObject.md

---
url: /typedocs/interfaces/FlowExportObject.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: FlowExportObject

## Properties

### edges

> **edges**: [`Edge`](../type-aliases/Edge.md)\[]

exported edges

***

### nodes

> **nodes**: [`Node`](Node.md)<`any`, `any`, `string`>\[]

exported nodes

***

### ~~position~~

> **position**: \[`number`, `number`]

exported viewport position

#### Deprecated

use [FlowExportObject.viewport](FlowExportObject.md#viewport) instead

***

### viewport

> **viewport**: [`ViewportTransform`](ViewportTransform.md)

exported viewport (position + zoom)

***

### ~~zoom~~

> **zoom**: `number`

exported zoom level

#### Deprecated

use [FlowExportObject.viewport](FlowExportObject.md#viewport) instead
