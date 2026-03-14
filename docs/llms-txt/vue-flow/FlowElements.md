# Source: https://vueflow.dev/typedocs/type-aliases/FlowElements.md

---
url: /typedocs/type-aliases/FlowElements.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Type Alias: ~~FlowElements\<NodeData, EdgeData, NodeEvents, EdgeEvents>~~

> **FlowElements**<`NodeData`, `EdgeData`, `NodeEvents`, `EdgeEvents`>: [`FlowElement`](FlowElement.md)<`NodeData`, `EdgeData`, `NodeEvents`, `EdgeEvents`>\[]

## Type Parameters

• **NodeData** = [`ElementData`](ElementData.md)

• **EdgeData** = [`ElementData`](ElementData.md)

• **NodeEvents** *extends* `Record`<`string`, [`CustomEvent`](CustomEvent.md)> = `any`

• **EdgeEvents** *extends* `Record`<`string`, [`CustomEvent`](CustomEvent.md)> = `any`

## Deprecated

* will be removed in the next major version
  An array of flow elements (after parsing into state)
