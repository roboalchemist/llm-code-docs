# Source: https://vueflow.dev/typedocs/type-aliases/NodeEventsOn.md

---
url: /typedocs/type-aliases/NodeEventsOn.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Type Alias: NodeEventsOn\<CustomEvents>

> **NodeEventsOn**<`CustomEvents`>: `{ [key in keyof NodeEventsHandler]: EventHookOn<NodeEventsHandler[key] extends Function ? Event : never> }` & `CustomEventHandlers`<`CustomEvents`>

## Type Parameters

• **CustomEvents** = `object`
