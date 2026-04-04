# Source: https://vueflow.dev/typedocs/interfaces/GraphNode.md

---
url: /typedocs/interfaces/GraphNode.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: GraphNode\<Data, CustomEvents, Type>

## Extends

* [`Node`](Node.md)<`Data`, `CustomEvents`, `Type`>

## Type Parameters

• **Data** = [`ElementData`](../type-aliases/ElementData.md)

• **CustomEvents** *extends* `Record`<`string`, [`CustomEvent`](../type-aliases/CustomEvent.md)> = `any`

• **Type** *extends* `string` = `string`

## Properties

### ariaLabel?

> `optional` **ariaLabel**: `string`

#### Inherited from

[`Node`](Node.md).[`ariaLabel`](Node.md#arialabel)

***

### class?

> `optional` **class**: `string` | `string`\[] | `Record`<`string`, `any`> | [`ClassFunc`](../type-aliases/ClassFunc.md)<[`GraphNode`](GraphNode.md)<`Data`, `CustomEvents`, `string`>>

Additional class names, can be a string or a callback returning a string (receives current flow element)

#### Inherited from

[`Node`](Node.md).[`class`](Node.md#class)

***

### computedPosition

> **computedPosition**: [`XYZPosition`](../type-aliases/XYZPosition.md)

absolute position in relation to parent elements + z-index

***

### connectable?

> `optional` **connectable**: [`HandleConnectable`](../type-aliases/HandleConnectable.md)

Disable/enable connecting node

#### Inherited from

[`Node`](Node.md).[`connectable`](Node.md#connectable)

***

### data

> **data**: `Data`

Additional data that is passed to your custom components

#### Overrides

[`Node`](Node.md).[`data`](Node.md#data)

***

### deletable?

> `optional` **deletable**: `boolean`

Disable/enable deleting node

#### Inherited from

[`Node`](Node.md).[`deletable`](Node.md#deletable)

***

### dimensions

> **dimensions**: [`Dimensions`](Dimensions.md)

node width, height

***

### domAttributes?

> `optional` **domAttributes**: `Omit`<`HTMLAttributes`, `"id"` | `"style"` | `"draggable"` | `"className"` | `"aria-label"` | `"onClick"` | `"onMouseenter"` | `"onMousemove"` | `"onMouseleave"` | `"onContextmenu"` | `"onDblclick"` | `"onKeydown"`>

General escape hatch for adding custom attributes to the node's DOM element.

#### Inherited from

[`Node`](Node.md).[`domAttributes`](Node.md#domattributes)

***

### draggable?

> `optional` **draggable**: `boolean`

Disable/enable dragging node

#### Inherited from

[`Node`](Node.md).[`draggable`](Node.md#draggable)

***

### dragging

> **dragging**: `boolean`

***

### dragHandle?

> `optional` **dragHandle**: `string`

element selector as drag handle for node (can only be dragged from the dragHandle el)

#### Inherited from

[`Node`](Node.md).[`dragHandle`](Node.md#draghandle)

***

### ~~events~~

> **events**: `Partial`<[`NodeEventsHandler`](../type-aliases/NodeEventsHandler.md)<`CustomEvents`>>

#### Deprecated

will be removed in the next major version

#### Overrides

[`Node`](Node.md).[`events`](Node.md#events)

***

### expandParent?

> `optional` **expandParent**: `boolean`

expands parent area to fit child node

#### Inherited from

[`Node`](Node.md).[`expandParent`](Node.md#expandparent)

***

### extent?

> `optional` **extent**: [`CoordinateExtent`](../type-aliases/CoordinateExtent.md) | [`CoordinateExtentRange`](CoordinateExtentRange.md) | `"parent"`

define node extent, i.e. area in which node can be moved

#### Inherited from

[`Node`](Node.md).[`extent`](Node.md#extent)

***

### focusable?

> `optional` **focusable**: `boolean`

Disable/enable focusing node (a11y)

#### Inherited from

[`Node`](Node.md).[`focusable`](Node.md#focusable)

***

### handleBounds

> **handleBounds**: [`NodeHandleBounds`](NodeHandleBounds.md)

***

### height?

> `optional` **height**: `string` | `number` | [`HeightFunc`](../type-aliases/HeightFunc.md)

Fixed height of node, applied as style
You can pass a number which will be used in pixel values (height: 300 -> height: 300px)
or pass a string with units (height: `10rem` -> height: 10rem)

#### Inherited from

[`Node`](Node.md).[`height`](Node.md#height)

***

### hidden?

> `optional` **hidden**: `boolean`

Is node hidden

#### Inherited from

[`Node`](Node.md).[`hidden`](Node.md#hidden)

***

### id

> **id**: `string`

Unique node id

#### Inherited from

[`Node`](Node.md).[`id`](Node.md#id)

***

### isParent

> **isParent**: `boolean`

***

### ~~isValidSourcePos?~~

> `optional` **isValidSourcePos**: [`ValidConnectionFunc`](../type-aliases/ValidConnectionFunc.md)

#### Deprecated

will be removed in next major release
called when used as source for new connection

#### Inherited from

[`Node`](Node.md).[`isValidSourcePos`](Node.md#isvalidsourcepos)

***

### ~~isValidTargetPos?~~

> `optional` **isValidTargetPos**: [`ValidConnectionFunc`](../type-aliases/ValidConnectionFunc.md)

#### Deprecated

will be removed in next major release
called when used as target for new connection

#### Inherited from

[`Node`](Node.md).[`isValidTargetPos`](Node.md#isvalidtargetpos)

***

### ~~label?~~

> `optional` **label**: `string` | `VNode`<`RendererNode`, `RendererElement`, `object`> | `Component`

#### Deprecated

* will be removed in next major release and replaced with `{ data: { label: string | VNode | Component } }`
  A node label

#### Inherited from

[`Node`](Node.md).[`label`](Node.md#label)

***

### parentNode?

> `optional` **parentNode**: `string`

todo: rename to `parentId` in next major release
define node as a child node by setting a parent node id

#### Inherited from

[`Node`](Node.md).[`parentNode`](Node.md#parentnode)

***

### position

> **position**: [`XYPosition`](XYPosition.md)

initial node position x, y

#### Inherited from

[`Node`](Node.md).[`position`](Node.md#position)

***

### resizing

> **resizing**: `boolean`

***

### selectable?

> `optional` **selectable**: `boolean`

Disable/enable selecting node

#### Inherited from

[`Node`](Node.md).[`selectable`](Node.md#selectable)

***

### selected

> **selected**: `boolean`

***

### sourcePosition?

> `optional` **sourcePosition**: [`Position`](../enumerations/Position.md)

handle position

#### Inherited from

[`Node`](Node.md).[`sourcePosition`](Node.md#sourceposition)

***

### style?

> `optional` **style**: [`Styles`](../type-aliases/Styles.md) | [`StyleFunc`](../type-aliases/StyleFunc.md)<[`GraphNode`](GraphNode.md)<`Data`, `CustomEvents`, `string`>>

Additional styles, can be an object or a callback returning an object (receives current flow element)

#### Inherited from

[`Node`](Node.md).[`style`](Node.md#style)

***

### targetPosition?

> `optional` **targetPosition**: [`Position`](../enumerations/Position.md)

handle position

#### Inherited from

[`Node`](Node.md).[`targetPosition`](Node.md#targetposition)

***

### ~~template?~~

> `optional` **template**: [`NodeComponent`](../type-aliases/NodeComponent.md)

#### Deprecated

* will be removed in the next major release
  overwrites current node type

#### Inherited from

[`Node`](Node.md).[`template`](Node.md#template)

***

### type

> **type**: `Type`

node type, can be a default type or a custom type

#### Overrides

[`Node`](Node.md).[`type`](Node.md#type)

***

### width?

> `optional` **width**: `string` | `number` | [`WidthFunc`](../type-aliases/WidthFunc.md)

Fixed width of node, applied as style
You can pass a number which will be used in pixel values (width: 300 -> width: 300px)
or pass a string with units (width: `10rem` -> width: 10rem)

#### Inherited from

[`Node`](Node.md).[`width`](Node.md#width)

***

### zIndex?

> `optional` **zIndex**: `number`

#### Inherited from

[`Node`](Node.md).[`zIndex`](Node.md#zindex)
