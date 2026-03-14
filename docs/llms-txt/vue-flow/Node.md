# Source: https://vueflow.dev/typedocs/interfaces/Node.md

---
url: /typedocs/interfaces/Node.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: Node\<Data, CustomEvents, Type>

## Extended by

* [`GraphNode`](GraphNode.md)

## Type Parameters

• **Data** = [`ElementData`](../type-aliases/ElementData.md)

• **CustomEvents** *extends* `Record`<`string`, [`CustomEvent`](../type-aliases/CustomEvent.md)> = `any`

• **Type** *extends* `string` = `string`

## Properties

### ariaLabel?

> `optional` **ariaLabel**: `string`

***

### class?

> `optional` **class**: `string` | `string`\[] | `Record`<`string`, `any`> | [`ClassFunc`](../type-aliases/ClassFunc.md)<[`GraphNode`](GraphNode.md)<`Data`, `CustomEvents`, `string`>>

Additional class names, can be a string or a callback returning a string (receives current flow element)

***

### connectable?

> `optional` **connectable**: [`HandleConnectable`](../type-aliases/HandleConnectable.md)

Disable/enable connecting node

***

### data?

> `optional` **data**: `Data`

Additional data that is passed to your custom components

***

### deletable?

> `optional` **deletable**: `boolean`

Disable/enable deleting node

***

### domAttributes?

> `optional` **domAttributes**: `Omit`<`HTMLAttributes`, `"id"` | `"style"` | `"draggable"` | `"className"` | `"aria-label"` | `"onClick"` | `"onMouseenter"` | `"onMousemove"` | `"onMouseleave"` | `"onContextmenu"` | `"onDblclick"` | `"onKeydown"`>

General escape hatch for adding custom attributes to the node's DOM element.

***

### draggable?

> `optional` **draggable**: `boolean`

Disable/enable dragging node

***

### dragHandle?

> `optional` **dragHandle**: `string`

element selector as drag handle for node (can only be dragged from the dragHandle el)

***

### ~~events?~~

> `optional` **events**: `Partial`<[`NodeEventsHandler`](../type-aliases/NodeEventsHandler.md)<`CustomEvents`>>

#### Deprecated

* will be removed in the next major release
  contextual and custom events that are passed to your custom components

***

### expandParent?

> `optional` **expandParent**: `boolean`

expands parent area to fit child node

***

### extent?

> `optional` **extent**: [`CoordinateExtent`](../type-aliases/CoordinateExtent.md) | [`CoordinateExtentRange`](CoordinateExtentRange.md) | `"parent"`

define node extent, i.e. area in which node can be moved

***

### focusable?

> `optional` **focusable**: `boolean`

Disable/enable focusing node (a11y)

***

### height?

> `optional` **height**: `string` | `number` | [`HeightFunc`](../type-aliases/HeightFunc.md)

Fixed height of node, applied as style
You can pass a number which will be used in pixel values (height: 300 -> height: 300px)
or pass a string with units (height: `10rem` -> height: 10rem)

***

### hidden?

> `optional` **hidden**: `boolean`

Is node hidden

***

### id

> **id**: `string`

Unique node id

***

### ~~isValidSourcePos?~~

> `optional` **isValidSourcePos**: [`ValidConnectionFunc`](../type-aliases/ValidConnectionFunc.md)

#### Deprecated

will be removed in next major release
called when used as source for new connection

***

### ~~isValidTargetPos?~~

> `optional` **isValidTargetPos**: [`ValidConnectionFunc`](../type-aliases/ValidConnectionFunc.md)

#### Deprecated

will be removed in next major release
called when used as target for new connection

***

### ~~label?~~

> `optional` **label**: `string` | `VNode`<`RendererNode`, `RendererElement`, `object`> | `Component`

#### Deprecated

* will be removed in next major release and replaced with `{ data: { label: string | VNode | Component } }`
  A node label

***

### parentNode?

> `optional` **parentNode**: `string`

todo: rename to `parentId` in next major release
define node as a child node by setting a parent node id

***

### position

> **position**: [`XYPosition`](XYPosition.md)

initial node position x, y

***

### selectable?

> `optional` **selectable**: `boolean`

Disable/enable selecting node

***

### sourcePosition?

> `optional` **sourcePosition**: [`Position`](../enumerations/Position.md)

handle position

***

### style?

> `optional` **style**: [`Styles`](../type-aliases/Styles.md) | [`StyleFunc`](../type-aliases/StyleFunc.md)<[`GraphNode`](GraphNode.md)<`Data`, `CustomEvents`, `string`>>

Additional styles, can be an object or a callback returning an object (receives current flow element)

***

### targetPosition?

> `optional` **targetPosition**: [`Position`](../enumerations/Position.md)

handle position

***

### ~~template?~~

> `optional` **template**: [`NodeComponent`](../type-aliases/NodeComponent.md)

#### Deprecated

* will be removed in the next major release
  overwrites current node type

***

### type?

> `optional` **type**: `Type`

node type, can be a default type or a custom type

***

### width?

> `optional` **width**: `string` | `number` | [`WidthFunc`](../type-aliases/WidthFunc.md)

Fixed width of node, applied as style
You can pass a number which will be used in pixel values (width: 300 -> width: 300px)
or pass a string with units (width: `10rem` -> width: 10rem)

***

### zIndex?

> `optional` **zIndex**: `number`
