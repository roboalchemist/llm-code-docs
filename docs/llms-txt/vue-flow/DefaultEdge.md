# Source: https://vueflow.dev/typedocs/interfaces/DefaultEdge.md

---
url: /typedocs/interfaces/DefaultEdge.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: DefaultEdge\<Data, CustomEvents, Type>

## Extends

* [`EdgeLabelOptions`](EdgeLabelOptions.md)

## Type Parameters

• **Data** = [`ElementData`](../type-aliases/ElementData.md)

• **CustomEvents** *extends* `Record`<`string`, [`CustomEvent`](../type-aliases/CustomEvent.md)> = `any`

• **Type** *extends* `string` = `string`

## Properties

### animated?

> `optional` **animated**: `boolean`

Animated edge

***

### ariaLabel?

> `optional` **ariaLabel**: `null` | `string`

***

### class?

> `optional` **class**: `string` | `string`\[] | `Record`<`string`, `any`> | [`ClassFunc`](../type-aliases/ClassFunc.md)<[`GraphEdge`](../type-aliases/GraphEdge.md)<`Data`, `CustomEvents`, `string`>>

Additional class names, can be a string or a callback returning a string (receives current flow element)

***

### data?

> `optional` **data**: `Data`

Additional data that is passed to your custom components

***

### deletable?

> `optional` **deletable**: `boolean`

Disable/enable deleting edge

***

### domAttributes?

> `optional` **domAttributes**: `Omit`<`SVGAttributes`, `"id"` | `"style"` | `"className"` | `"role"` | `"aria-label"` | `"onClick"` | `"onMouseenter"` | `"onMousemove"` | `"onMouseleave"` | `"onContextmenu"` | `"onDblclick"` | `"onKeyDown"`>

General escape hatch for adding custom attributes to the edge's DOM element.

***

### ~~events?~~

> `optional` **events**: `Partial`<[`EdgeEventsHandler`](../type-aliases/EdgeEventsHandler.md)<`CustomEvents`>>

#### Deprecated

will be removed in the next major version

***

### focusable?

> `optional` **focusable**: `boolean`

Disable/enable focusing edge (a11y)

***

### hidden?

> `optional` **hidden**: `boolean`

Is edge hidden

***

### id

> **id**: `string`

Unique edge id

***

### interactionWidth?

> `optional` **interactionWidth**: `number`

Radius of mouse event triggers (to ease selecting edges), defaults to 2

***

### label?

> `optional` **label**: `string` | `VNode`<`RendererNode`, `RendererElement`, `object`> | `Component`<[`EdgeTextProps`](EdgeTextProps.md)>

An edge label

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

### markerEnd?

> `optional` **markerEnd**: [`EdgeMarkerType`](../type-aliases/EdgeMarkerType.md)

EdgeMarker

***

### markerStart?

> `optional` **markerStart**: [`EdgeMarkerType`](../type-aliases/EdgeMarkerType.md)

EdgeMarker

***

### selectable?

> `optional` **selectable**: `boolean`

Disable/enable selecting edge

***

### source

> **source**: `string`

Source node id

***

### sourceHandle?

> `optional` **sourceHandle**: `null` | `string`

Source handle id

***

### style?

> `optional` **style**: [`Styles`](../type-aliases/Styles.md) | [`StyleFunc`](../type-aliases/StyleFunc.md)<[`GraphEdge`](../type-aliases/GraphEdge.md)<`Data`, `CustomEvents`, `string`>>

Additional styles, can be an object or a callback returning an object (receives current flow element)

***

### target

> **target**: `string`

Target node id

***

### targetHandle?

> `optional` **targetHandle**: `null` | `string`

Target handle id

***

### template?

> `optional` **template**: [`EdgeComponent`](../type-aliases/EdgeComponent.md)

Overwrites current edge type

***

### type?

> `optional` **type**: `Type`

Edge type, can be a default type or a custom type

***

### updatable?

> `optional` **updatable**: [`EdgeUpdatable`](../type-aliases/EdgeUpdatable.md)

Disable/enable updating edge

***

### zIndex?

> `optional` **zIndex**: `number`

Aria label for edge (a11y)
