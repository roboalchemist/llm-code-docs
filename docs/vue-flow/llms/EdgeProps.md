# Source: https://vueflow.dev/typedocs/interfaces/EdgeProps.md

---
url: /typedocs/interfaces/EdgeProps.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: EdgeProps\<Data, CustomEvents, Type>

these props are passed to edge components

## Extends

* [`EdgeLabelOptions`](EdgeLabelOptions.md).[`EdgePositions`](EdgePositions.md)

## Type Parameters

• **Data** = [`ElementData`](../type-aliases/ElementData.md)

• **CustomEvents** = `object`

• **Type** *extends* `string` = `string`

## Properties

### animated?

> `optional` **animated**: `boolean`

***

### curvature?

> `optional` **curvature**: `number`

***

### data

> **data**: `Data`

***

### events

> **events**: [`EdgeEventsOn`](../type-aliases/EdgeEventsOn.md)<`CustomEvents`>

contextual and custom events of edge

***

### id

> **id**: `string`

***

### interactionWidth?

> `optional` **interactionWidth**: `number`

***

### label?

> `optional` **label**: `string` | `object` | `VNode`<`RendererNode`, `RendererElement`, `object`> | `Component`<[`EdgeTextProps`](EdgeTextProps.md)>

***

### labelBgBorderRadius?

> `optional` **labelBgBorderRadius**: `number`

Label Bg border radius

#### Inherited from

[`EdgeLabelOptions`](EdgeLabelOptions.md).[`labelBgBorderRadius`](EdgeLabelOptions.md#labelbgborderradius)

***

### labelBgPadding?

> `optional` **labelBgPadding**: \[`number`, `number`]

Label Bg padding

#### Inherited from

[`EdgeLabelOptions`](EdgeLabelOptions.md).[`labelBgPadding`](EdgeLabelOptions.md#labelbgpadding)

***

### labelBgStyle?

> `optional` **labelBgStyle**: `CSSProperties`

Label Bg styles (CSSProperties)

#### Inherited from

[`EdgeLabelOptions`](EdgeLabelOptions.md).[`labelBgStyle`](EdgeLabelOptions.md#labelbgstyle)

***

### labelShowBg?

> `optional` **labelShowBg**: `boolean`

Show label bg

#### Inherited from

[`EdgeLabelOptions`](EdgeLabelOptions.md).[`labelShowBg`](EdgeLabelOptions.md#labelshowbg)

***

### labelStyle?

> `optional` **labelStyle**: `CSSProperties`

Label styles (CSSProperties)

#### Inherited from

[`EdgeLabelOptions`](EdgeLabelOptions.md).[`labelStyle`](EdgeLabelOptions.md#labelstyle)

***

### markerEnd

> **markerEnd**: `string`

***

### markerStart

> **markerStart**: `string`

***

### selected?

> `optional` **selected**: `boolean`

***

### source

> **source**: `string`

***

### sourceHandleId?

> `optional` **sourceHandleId**: `string`

***

### sourceNode

> **sourceNode**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>

***

### sourcePosition

> **sourcePosition**: [`Position`](../enumerations/Position.md)

***

### sourceX

> **sourceX**: `number`

#### Inherited from

[`EdgePositions`](EdgePositions.md).[`sourceX`](EdgePositions.md#sourcex)

***

### sourceY

> **sourceY**: `number`

#### Inherited from

[`EdgePositions`](EdgePositions.md).[`sourceY`](EdgePositions.md#sourcey)

***

### style?

> `optional` **style**: `CSSProperties`

***

### target

> **target**: `string`

***

### targetHandleId?

> `optional` **targetHandleId**: `string`

***

### targetNode

> **targetNode**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>

***

### targetPosition

> **targetPosition**: [`Position`](../enumerations/Position.md)

***

### targetX

> **targetX**: `number`

#### Inherited from

[`EdgePositions`](EdgePositions.md).[`targetX`](EdgePositions.md#targetx)

***

### targetY

> **targetY**: `number`

#### Inherited from

[`EdgePositions`](EdgePositions.md).[`targetY`](EdgePositions.md#targety)

***

### type

> **type**: `Type`

***

### updatable?

> `optional` **updatable**: `boolean`
