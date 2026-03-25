# Source: https://vueflow.dev/typedocs/type-aliases/EdgeEventsEmit.md

---
url: /typedocs/type-aliases/EdgeEventsEmit.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Type Alias: EdgeEventsEmit\<CustomEvents>

> **EdgeEventsEmit**<`CustomEvents`>: `{ [key in keyof EdgeEventsHandler]: EventHookTrigger<EdgeEventsHandler[key] extends Function ? Event : never> }` & `CustomEventHandlers`<`CustomEvents`>

## Type Parameters

• **CustomEvents** = `object`
