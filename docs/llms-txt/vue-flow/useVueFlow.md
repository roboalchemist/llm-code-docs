# Source: https://vueflow.dev/typedocs/functions/useVueFlow.md

---
url: /typedocs/functions/useVueFlow.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Function: useVueFlow()

## useVueFlow(id)

> **useVueFlow**(`id`?): [`VueFlowStore`](../type-aliases/VueFlowStore.md)

Composable that provides access to a store instance

If no id is provided, the store instance is injected from context

If no store instance is found in context, a new store instance is created and registered in storage

### Parameters

• **id?**: `string`

### Returns

[`VueFlowStore`](../type-aliases/VueFlowStore.md)

a vue flow store instance

## useVueFlow(options)

> **useVueFlow**(`options`?): [`VueFlowStore`](../type-aliases/VueFlowStore.md)

### Parameters

• **options?**: [`FlowProps`](../interfaces/FlowProps.md)

### Returns

[`VueFlowStore`](../type-aliases/VueFlowStore.md)
