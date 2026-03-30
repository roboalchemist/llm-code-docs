# Source: https://vueflow.dev/typedocs/type-aliases/ValidConnectionFunc.md

---
url: /typedocs/type-aliases/ValidConnectionFunc.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Type Alias: ValidConnectionFunc()

> **ValidConnectionFunc**: (`connection`, `elements`) => `boolean`

A valid connection function can determine if an attempted connection is valid or not, i.e. abort creating a new edge

## Parameters

• **connection**: [`Connection`](../interfaces/Connection.md)

• **elements**

• **elements.edges**: [`GraphEdge`](GraphEdge.md)\[]

• **elements.nodes**: [`GraphNode`](../interfaces/GraphNode.md)\[]

• **elements.sourceNode**: [`GraphNode`](../interfaces/GraphNode.md)

• **elements.targetNode**: [`GraphNode`](../interfaces/GraphNode.md)

## Returns

`boolean`
