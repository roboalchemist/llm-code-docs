# Source: https://vueflow.dev/typedocs/type-aliases/UpdateNode.md

---
url: /typedocs/type-aliases/UpdateNode.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Type Alias: UpdateNode()

> **UpdateNode**: <`Data`, `CustomEvents`>(`id`, `nodeUpdate`, `options`?) => `void`

## Type Parameters

• **Data** = [`ElementData`](ElementData.md)

• **CustomEvents** *extends* `Record`<`string`, [`CustomEvent`](CustomEvent.md)> = `any`

## Parameters

• **id**: `string`

• **nodeUpdate**: `Partial`<[`Node`](../interfaces/Node.md)<`Data`, `CustomEvents`>> | (`node`) => `Partial`<[`Node`](../interfaces/Node.md)<`Data`, `CustomEvents`>>

• **options?**

• **options.replace?**: `boolean`

## Returns

`void`
