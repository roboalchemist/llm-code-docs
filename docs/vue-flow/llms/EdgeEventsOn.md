# Source: https://vueflow.dev/typedocs/type-aliases/EdgeEventsOn.md

---
url: /typedocs/type-aliases/EdgeEventsOn.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Type Alias: EdgeEventsOn\<CustomEvents>

> **EdgeEventsOn**<`CustomEvents`>: `{ [key in keyof EdgeEventsHandler]: EventHookOn<EdgeEventsHandler[key] extends Function ? Event : never> }` & `CustomEventHandlers`<`CustomEvents`>

## Type Parameters

• **CustomEvents** = `object`
