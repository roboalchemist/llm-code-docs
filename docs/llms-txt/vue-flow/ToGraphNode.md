# Source: https://vueflow.dev/typedocs/type-aliases/ToGraphNode.md

---
url: /typedocs/type-aliases/ToGraphNode.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Type Alias: ToGraphNode\<T>

> **ToGraphNode**<`T`>: [`GraphNode`](../interfaces/GraphNode.md)<`T` *extends* [`Node`](../interfaces/Node.md)\<infer Data> ? `Data` : `never`, `T` *extends* [`Node`](../interfaces/Node.md)<`any`, infer Events> ? `Events` : `never`, `T` *extends* [`Node`](../interfaces/Node.md)<`any`, `any`, infer Type> ? `Type` : `never`>

Transform a Node type to a GraphNode type

## Type Parameters

• **T** *extends* [`Node`](../interfaces/Node.md)
