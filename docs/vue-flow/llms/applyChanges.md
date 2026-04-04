# Source: https://vueflow.dev/typedocs/functions/applyChanges.md

---
url: /typedocs/functions/applyChanges.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Function: applyChanges()

> **applyChanges**<`T`, `C`>(`changes`, `elements`): `T`\[]

## Type Parameters

• **T** *extends* [`FlowElement`](../type-aliases/FlowElement.md) = [`FlowElement`](../type-aliases/FlowElement.md)

• **C** *extends* [`ElementChange`](../type-aliases/ElementChange.md) = `T` *extends* [`GraphNode`](../interfaces/GraphNode.md)<`any`, `any`, `string`> ? [`NodeChange`](../type-aliases/NodeChange.md) : [`EdgeChange`](../type-aliases/EdgeChange.md)

## Parameters

• **changes**: `C`\[]

• **elements**: `T`\[]

## Returns

`T`\[]
