# Source: https://vueflow.dev/typedocs/functions/useEdgesData.md

---
url: /typedocs/functions/useEdgesData.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Function: useEdgesData()

## useEdgesData(edgeId)

> **useEdgesData**<`EdgeType`>(`edgeId`): `ComputedRef`<`EdgeData`<`EdgeType`> | `null`>

Composable for receiving data of one or multiple nodes

### Type Parameters

• **EdgeType** *extends* [`Edge`](../type-aliases/Edge.md) = [`GraphEdge`](../type-aliases/GraphEdge.md)

### Parameters

• **edgeId**: `MaybeRefOrGetter`<`string`>

The id (or ids) of the node to get the data from

### Returns

`ComputedRef`<`EdgeData`<`EdgeType`> | `null`>

An array of data objects

## useEdgesData(edgeIds)

> **useEdgesData**<`EdgeType`>(`edgeIds`): `ComputedRef`<`EdgeData`<`EdgeType`>\[]>

### Type Parameters

• **EdgeType** *extends* [`Edge`](../type-aliases/Edge.md) = [`GraphEdge`](../type-aliases/GraphEdge.md)

### Parameters

• **edgeIds**: `MaybeRefOrGetter`<`string`\[]>

### Returns

`ComputedRef`<`EdgeData`<`EdgeType`>\[]>

## useEdgesData(edgeIds, guard)

> **useEdgesData**<`EdgeType`>(`edgeIds`, `guard`): `ComputedRef`<`EdgeData`<`EdgeType`>\[]>

### Type Parameters

• **EdgeType** *extends* [`Edge`](../type-aliases/Edge.md) = [`GraphEdge`](../type-aliases/GraphEdge.md)

### Parameters

• **edgeIds**: `MaybeRefOrGetter`<`string`\[]>

• **guard**

### Returns

`ComputedRef`<`EdgeData`<`EdgeType`>\[]>
