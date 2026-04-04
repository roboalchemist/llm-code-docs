# Source: https://vueflow.dev/typedocs/functions/useEdge.md

---
url: /typedocs/functions/useEdge.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Function: useEdge()

> **useEdge**<`Data`, `CustomEvents`>(`id`?): `object`

Composable that provides access to an edge object and it's dom element

If no edge id is provided, the edge id is injected from context

If you do not provide an id, this composable has to be called in a child of your custom edge component, or it will throw

## Type Parameters

• **Data** = `any`

• **CustomEvents** *extends* `Record`<`string`, [`CustomEvent`](../type-aliases/CustomEvent.md)> = `any`

## Parameters

• **id?**: `string`

The id of the edge to access

## Returns

`object`

the edge id, the edge and the edge dom element

### edge

> **edge**: [`GraphEdge`](../type-aliases/GraphEdge.md)<`Data`, `CustomEvents`>

### edgeEl

> **edgeEl**: `Ref`<`null` | `SVGElement`>

### id

> **id**: `string` = `edgeId`
