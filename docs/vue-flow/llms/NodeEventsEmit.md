# Source: https://vueflow.dev/typedocs/type-aliases/NodeEventsEmit.md

---
url: /typedocs/type-aliases/NodeEventsEmit.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Type Alias: NodeEventsEmit\<CustomEvents>

> **NodeEventsEmit**<`CustomEvents`>: `{ [key in keyof NodeEventsHandler]: EventHookTrigger<NodeEventsHandler[key] extends Function ? Event : never> }` & `CustomEventHandlers`<`CustomEvents`>

## Type Parameters

• **CustomEvents** = `object`
