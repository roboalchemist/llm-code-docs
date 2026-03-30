# Source: https://vueflow.dev/typedocs/functions/useNode.md

---
url: /typedocs/functions/useNode.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Function: useNode()

> **useNode**<`Data`, `CustomEvents`>(`id`?): `object`

Composable that provides access to a node object, parent node object, connected edges and it's dom element

If no node id is provided, the node id is injected from context

If you do not provide an id, this composable has to be called in a child of your custom node component, or it will throw

## Type Parameters

• **Data** = `any`

• **CustomEvents** *extends* `Record`<`string`, [`CustomEvent`](../type-aliases/CustomEvent.md)> = `any`

## Parameters

• **id?**: `string`

The id of the node to access

## Returns

`object`

the node id, the node, the node dom element, it's parent and connected edges

### connectedEdges

> **connectedEdges**: `ComputedRef`<[`GraphEdge`](../type-aliases/GraphEdge.md)\[]>

### id

> **id**: `string` = `nodeId`

### node

> **node**: [`GraphNode`](../interfaces/GraphNode.md)<`Data`, `CustomEvents`, `string`>

### nodeEl

> **nodeEl**: `Ref`<`null` | `HTMLDivElement`>

### parentNode

> **parentNode**: `ComputedRef`<`undefined` | [`GraphNode`](../interfaces/GraphNode.md)<`any`, `any`, `string`>>
