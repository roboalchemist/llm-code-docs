# Source: https://vueflow.dev/typedocs/type-aliases/FlowElement.md

---
url: /typedocs/type-aliases/FlowElement.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Type Alias: ~~FlowElement\<NodeData, EdgeData, NodeEvents, EdgeEvents>~~

> **FlowElement**<`NodeData`, `EdgeData`, `NodeEvents`, `EdgeEvents`>: [`GraphNode`](../interfaces/GraphNode.md)<`NodeData`, `NodeEvents`> | [`GraphEdge`](GraphEdge.md)<`EdgeData`, `EdgeEvents`>

## Type Parameters

• **NodeData** = [`ElementData`](ElementData.md)

• **EdgeData** = [`ElementData`](ElementData.md)

• **NodeEvents** *extends* `Record`<`string`, [`CustomEvent`](CustomEvent.md)> = `any`

• **EdgeEvents** *extends* `Record`<`string`, [`CustomEvent`](CustomEvent.md)> = `any`

## Deprecated

* will be removed in the next major version
  A flow element (after parsing into state)
