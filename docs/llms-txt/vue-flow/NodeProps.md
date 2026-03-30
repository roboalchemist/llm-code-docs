# Source: https://vueflow.dev/typedocs/interfaces/NodeProps.md

---
url: /typedocs/interfaces/NodeProps.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: NodeProps\<Data, CustomEvents, Type>

these props are passed to node components

## Type Parameters

• **Data** = [`ElementData`](../type-aliases/ElementData.md)

• **CustomEvents** = `object`

• **Type** *extends* `string` = `string`

## Properties

### connectable

> **connectable**: [`HandleConnectable`](../type-aliases/HandleConnectable.md)

can node handles be connected, you need to forward this to your handles for this prop to have any effect

***

### data

> **data**: `Data`

additional data of node

***

### dimensions

> **dimensions**: [`Dimensions`](Dimensions.md)

dom element dimensions (width, height)

***

### dragging

> **dragging**: `boolean`

is node currently dragging

***

### dragHandle?

> `optional` **dragHandle**: `string`

drag handle query selector

***

### ~~events~~

> **events**: [`NodeEventsOn`](../type-aliases/NodeEventsOn.md)<`CustomEvents`>

#### Deprecated

* will be removed in next major release
  contextual and custom events of node

***

### id

> **id**: `string`

unique node id

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

> `optional` **label**: `string` | `object` | `VNode`<`RendererNode`, `RendererElement`, `object`> | `Component`

#### Deprecated

* will be removed in next major release and replaced with `{ data: { label: string | VNode | Component } }`
  node label, either pass a string or a VNode
  For example like this: `h('div', props, children)`)
  Object is just a type-hack for Vue, ignore that

***

### ~~parent?~~

> `optional` **parent**: `string`

#### Deprecated

* will be removed in next major release. Use `parentNodeId` instead
  parent node id

***

### parentNodeId?

> `optional` **parentNodeId**: `string`

todo: rename to `parentId` in next major release
parent node id

***

### ~~position~~

> **position**: [`XYPosition`](XYPosition.md)

#### Deprecated

* will be removed in next major release and replaced with `computedPosition`
  node x, y (relative) position on graph

***

### resizing

> **resizing**: `boolean`

is node currently resizing

***

### selected

> **selected**: `boolean`

is node selected

***

### sourcePosition?

> `optional` **sourcePosition**: [`Position`](../enumerations/Position.md)

handle position

***

### targetPosition?

> `optional` **targetPosition**: [`Position`](../enumerations/Position.md)

handle position

***

### type

> **type**: `Type`

node type

***

### zIndex

> **zIndex**: `number`

node z-index
