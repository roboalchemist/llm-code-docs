# Source: https://vueflow.dev/typedocs/type-aliases/Element.md

---
url: /typedocs/type-aliases/Element.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Type Alias: Element\<NodeData, EdgeData, NodeEvents, EdgeEvents>

> **Element**<`NodeData`, `EdgeData`, `NodeEvents`, `EdgeEvents`>: [`Node`](../interfaces/Node.md)<`NodeData`, `NodeEvents`> | [`Edge`](Edge.md)<`EdgeData`, `EdgeEvents`>

Initial elements (before parsing into state)

## Type Parameters

• **NodeData** = [`ElementData`](ElementData.md)

• **EdgeData** = [`ElementData`](ElementData.md)

• **NodeEvents** *extends* `Record`<`string`, [`CustomEvent`](CustomEvent.md)> = `any`

• **EdgeEvents** *extends* `Record`<`string`, [`CustomEvent`](CustomEvent.md)> = `any`
