# Source: https://vueflow.dev/typedocs/type-aliases/GraphEdge.md

---
url: /typedocs/type-aliases/GraphEdge.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Type Alias: GraphEdge\<Data, CustomEvents, Type>

> **GraphEdge**<`Data`, `CustomEvents`, `Type`>: [`Edge`](Edge.md)<`Data`, `CustomEvents`> & `object` & [`EdgePositions`](../interfaces/EdgePositions.md)

Internal edge type

## Type declaration

### data

> **data**: `Data`

### ~~events~~

> **events**: `Partial`<[`EdgeEventsHandler`](EdgeEventsHandler.md)<`CustomEvents`>>

#### Deprecated

will be removed in the next major version

### selected

> **selected**: `boolean`

### sourceNode

> **sourceNode**: [`GraphNode`](../interfaces/GraphNode.md)

### targetNode

> **targetNode**: [`GraphNode`](../interfaces/GraphNode.md)

### type

> **type**: `Type`

## Type Parameters

• **Data** = [`ElementData`](ElementData.md)

• **CustomEvents** *extends* `Record`<`string`, [`CustomEvent`](CustomEvent.md)> = `any`

• **Type** *extends* `string` = `string`
