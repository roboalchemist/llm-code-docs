# Source: https://vueflow.dev/typedocs/interfaces/FlowProps.md

---
url: /typedocs/interfaces/FlowProps.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: FlowProps

## Properties

### ~~applyDefault?~~

> `optional` **applyDefault**: `boolean`

apply default change handlers for position, dimensions, adding/removing nodes. set this to false if you want to apply the changes manually

#### Deprecated

* will be removed in the next major version, changes will not be auto applied in the future

***

### ~~autoConnect?~~

> `optional` **autoConnect**: `boolean` | [`Connector`](../type-aliases/Connector.md)

automatically create an edge when connection is triggered

#### Deprecated

* will be removed in the next major version

***

### autoPanOnConnect?

> `optional` **autoPanOnConnect**: `boolean`

***

### autoPanOnNodeDrag?

> `optional` **autoPanOnNodeDrag**: `boolean`

***

### autoPanSpeed?

> `optional` **autoPanSpeed**: `number`

***

### connectionLineOptions?

> `optional` **connectionLineOptions**: [`ConnectionLineOptions`](ConnectionLineOptions.md)

***

### ~~connectionLineStyle?~~

> `optional` **connectionLineStyle**: `null` | `CSSProperties`

#### Deprecated

use [ConnectionLineOptions.style](ConnectionLineOptions.md#style)

***

### ~~connectionLineType?~~

> `optional` **connectionLineType**: `null` | [`ConnectionLineType`](../enumerations/ConnectionLineType.md)

#### Deprecated

use [ConnectionLineOptions.type](ConnectionLineOptions.md#type)

***

### connectionMode?

> `optional` **connectionMode**: [`ConnectionMode`](../enumerations/ConnectionMode.md)

***

### connectionRadius?

> `optional` **connectionRadius**: `number`

***

### connectOnClick?

> `optional` **connectOnClick**: `boolean`

allow connection with click handlers, i.e. support touch devices

***

### defaultEdgeOptions?

> `optional` **defaultEdgeOptions**: [`DefaultEdgeOptions`](../type-aliases/DefaultEdgeOptions.md)

does not work for the `addEdge` utility!

***

### defaultMarkerColor?

> `optional` **defaultMarkerColor**: `string`

***

### defaultViewport?

> `optional` **defaultViewport**: `Partial`<[`ViewportTransform`](ViewportTransform.md)>

***

### deleteKeyCode?

> `optional` **deleteKeyCode**: `null` | `KeyFilter`

***

### disableKeyboardA11y?

> `optional` **disableKeyboardA11y**: `boolean`

***

### edges?

> `optional` **edges**: [`Edge`](../type-aliases/Edge.md)\[]

***

### edgesFocusable?

> `optional` **edgesFocusable**: `boolean`

***

### edgesUpdatable?

> `optional` **edgesUpdatable**: [`EdgeUpdatable`](../type-aliases/EdgeUpdatable.md)

***

### edgeTypes?

> `optional` **edgeTypes**: [`EdgeTypesObject`](../type-aliases/EdgeTypesObject.md)

either use the edgeTypes prop to define your edge-types or use slots (\<template #edge-mySpecialType="props">)

***

### edgeUpdaterRadius?

> `optional` **edgeUpdaterRadius**: `number`

***

### elementsSelectable?

> `optional` **elementsSelectable**: `boolean`

***

### elevateEdgesOnSelect?

> `optional` **elevateEdgesOnSelect**: `boolean`

elevates edges when selected and applies z-Index to put them above their nodes

***

### elevateNodesOnSelect?

> `optional` **elevateNodesOnSelect**: `boolean`

elevates nodes when selected and applies z-Index + 1000

***

### fitViewOnInit?

> `optional` **fitViewOnInit**: `boolean`

will be renamed to `fitView`

***

### id?

> `optional` **id**: `string`

***

### isValidConnection?

> `optional` **isValidConnection**: `null` | [`ValidConnectionFunc`](../type-aliases/ValidConnectionFunc.md)

***

### maxZoom?

> `optional` **maxZoom**: `number`

***

### minZoom?

> `optional` **minZoom**: `number`

***

### ~~modelValue?~~

> `optional` **modelValue**: [`Elements`](../type-aliases/Elements.md)<`any`, `any`, `any`, `any`>

all elements (nodes + edges)

#### Deprecated

use [FlowProps.nodes](FlowProps.md#nodes) & [FlowProps.nodes](FlowProps.md#nodes) instead

***

### multiSelectionKeyCode?

> `optional` **multiSelectionKeyCode**: `null` | `KeyFilter`

***

### nodeDragThreshold?

> `optional` **nodeDragThreshold**: `number`

***

### nodeExtent?

> `optional` **nodeExtent**: [`CoordinateExtent`](../type-aliases/CoordinateExtent.md) | [`CoordinateExtentRange`](CoordinateExtentRange.md)

***

### nodes?

> `optional` **nodes**: [`Node`](Node.md)<`any`, `any`, `string`>\[]

***

### nodesConnectable?

> `optional` **nodesConnectable**: `boolean`

***

### nodesDraggable?

> `optional` **nodesDraggable**: `boolean`

***

### nodesFocusable?

> `optional` **nodesFocusable**: `boolean`

***

### nodeTypes?

> `optional` **nodeTypes**: [`NodeTypesObject`](../type-aliases/NodeTypesObject.md)

either use the nodeTypes prop to define your node-types or use slots (\<template #node-mySpecialType="props">)

***

### noDragClassName?

> `optional` **noDragClassName**: `string`

***

### noPanClassName?

> `optional` **noPanClassName**: `string`

***

### noWheelClassName?

> `optional` **noWheelClassName**: `string`

***

### onlyRenderVisibleElements?

> `optional` **onlyRenderVisibleElements**: `boolean`

***

### panActivationKeyCode?

> `optional` **panActivationKeyCode**: `null` | `KeyFilter`

***

### paneClickDistance?

> `optional` **paneClickDistance**: `number`

Distance that the mouse can move between mousedown/up that will trigger a click

#### Default

```ts
0
```

***

### panOnDrag?

> `optional` **panOnDrag**: `boolean` | `number`\[]

move pane on drag, replaced prop `paneMovable`

***

### panOnScroll?

> `optional` **panOnScroll**: `boolean`

***

### panOnScrollMode?

> `optional` **panOnScrollMode**: [`PanOnScrollMode`](../enumerations/PanOnScrollMode.md)

***

### panOnScrollSpeed?

> `optional` **panOnScrollSpeed**: `number`

***

### preventScrolling?

> `optional` **preventScrolling**: `boolean`

If set to false, scrolling inside the viewport will be disabled and instead the page scroll will be used

***

### selectionKeyCode?

> `optional` **selectionKeyCode**: `null` | `false` | `KeyFilter`

***

### selectionMode?

> `optional` **selectionMode**: [`SelectionMode`](../enumerations/SelectionMode.md)

***

### selectNodesOnDrag?

> `optional` **selectNodesOnDrag**: `boolean`

***

### snapGrid?

> `optional` **snapGrid**: [`SnapGrid`](../type-aliases/SnapGrid.md)

***

### snapToGrid?

> `optional` **snapToGrid**: `boolean`

***

### translateExtent?

> `optional` **translateExtent**: [`CoordinateExtent`](../type-aliases/CoordinateExtent.md)

***

### zoomActivationKeyCode?

> `optional` **zoomActivationKeyCode**: `null` | `KeyFilter`

***

### zoomOnDoubleClick?

> `optional` **zoomOnDoubleClick**: `boolean`

***

### zoomOnPinch?

> `optional` **zoomOnPinch**: `boolean`

***

### zoomOnScroll?

> `optional` **zoomOnScroll**: `boolean`
