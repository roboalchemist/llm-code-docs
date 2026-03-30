# Source: https://vueflow.dev/typedocs/functions/useNodesData.md

---
url: /typedocs/functions/useNodesData.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Function: useNodesData()

## useNodesData(nodeId)

> **useNodesData**<`NodeType`>(`nodeId`): `ComputedRef`<`NodeData`<`NodeType`> | `null`>

Composable for receiving data of one or multiple nodes

### Type Parameters

• **NodeType** *extends* [`Node`](../interfaces/Node.md)<`any`, `any`, `string`> = [`GraphNode`](../interfaces/GraphNode.md)<`any`, `any`, `string`>

### Parameters

• **nodeId**: `MaybeRefOrGetter`<`string`>

The id (or ids) of the node to get the data from

### Returns

`ComputedRef`<`NodeData`<`NodeType`> | `null`>

An array of data objects

## useNodesData(nodeIds)

> **useNodesData**<`NodeType`>(`nodeIds`): `ComputedRef`<`NodeData`<`NodeType`>\[]>

### Type Parameters

• **NodeType** *extends* [`Node`](../interfaces/Node.md)<`any`, `any`, `string`> = [`GraphNode`](../interfaces/GraphNode.md)<`any`, `any`, `string`>

### Parameters

• **nodeIds**: `MaybeRefOrGetter`<`string`\[]>

### Returns

`ComputedRef`<`NodeData`<`NodeType`>\[]>

## useNodesData(nodeIds, guard)

> **useNodesData**<`NodeType`>(`nodeIds`, `guard`): `ComputedRef`<`NodeData`<`NodeType`>\[]>

### Type Parameters

• **NodeType** *extends* [`Node`](../interfaces/Node.md)<`any`, `any`, `string`> = [`GraphNode`](../interfaces/GraphNode.md)<`any`, `any`, `string`>

### Parameters

• **nodeIds**: `MaybeRefOrGetter`<`string`\[]>

• **guard**

### Returns

`ComputedRef`<`NodeData`<`NodeType`>\[]>
