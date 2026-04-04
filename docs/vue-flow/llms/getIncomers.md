# Source: https://vueflow.dev/typedocs/functions/getIncomers.md

---
url: /typedocs/functions/getIncomers.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Function: getIncomers()

## getIncomers(nodeOrId, nodes, edges)

> **getIncomers**<`N`>(`nodeOrId`, `nodes`, `edges`): `N`\[]

### Type Parameters

• **N** *extends* [`Node`](../interfaces/Node.md)<`any`, `any`, `string`>

### Parameters

• **nodeOrId**: `string` | [`Node`](../interfaces/Node.md)<`any`, `any`, `string`> | `object`

• **nodes**: `N`\[]

• **edges**: [`Edge`](../type-aliases/Edge.md)\[]

### Returns

`N`\[]

## getIncomers(nodeOrId, elements)

> **getIncomers**<`T`>(`nodeOrId`, `elements`): `T` *extends* [`FlowElements`](../type-aliases/FlowElements.md) ? [`GraphNode`](../interfaces/GraphNode.md)\[] : [`Node`](../interfaces/Node.md)\[]

### Type Parameters

• **T** *extends* [`Elements`](../type-aliases/Elements.md)

### Parameters

• **nodeOrId**: `string` | [`Node`](../interfaces/Node.md)<`any`, `any`, `string`> | `object`

• **elements**: `T`

### Returns

`T` *extends* [`FlowElements`](../type-aliases/FlowElements.md) ? [`GraphNode`](../interfaces/GraphNode.md)\[] : [`Node`](../interfaces/Node.md)\[]
