# Source: https://vueflow.dev/typedocs/interfaces/State.md

---
url: /typedocs/interfaces/State.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: State

## Extends

* `Omit`<[`FlowProps`](FlowProps.md), `"id"` | `"modelValue"`>

## Properties

### ~~applyDefault~~

> **applyDefault**: `boolean`

apply default change handlers for position, dimensions, adding/removing nodes. set this to false if you want to apply the changes manually

#### Deprecated

* will be removed in the next major version, changes will not be auto applied in the future

#### Overrides

`Omit.applyDefault`

***

### ariaLiveMessage

> **ariaLiveMessage**: `string`

***

### ~~autoConnect~~

> **autoConnect**: `boolean` | [`Connector`](../type-aliases/Connector.md)

automatically create an edge when connection is triggered

#### Deprecated

* will be removed in the next major version

#### Overrides

`Omit.autoConnect`

***

### autoPanOnConnect

> **autoPanOnConnect**: `boolean`

#### Overrides

`Omit.autoPanOnConnect`

***

### autoPanOnNodeDrag

> **autoPanOnNodeDrag**: `boolean`

#### Overrides

`Omit.autoPanOnNodeDrag`

***

### autoPanSpeed

> **autoPanSpeed**: `number`

The speed at which the viewport pans while dragging a node or a selection box.

#### Default

```ts
15
```

#### Overrides

`Omit.autoPanSpeed`

***

### connectionClickStartHandle

> **connectionClickStartHandle**: `null` | [`ConnectingHandle`](ConnectingHandle.md)

***

### connectionEndHandle

> **connectionEndHandle**: `null` | [`ConnectingHandle`](ConnectingHandle.md)

***

### connectionLineOptions

> **connectionLineOptions**: [`ConnectionLineOptions`](ConnectionLineOptions.md)

#### Overrides

`Omit.connectionLineOptions`

***

### ~~connectionLineStyle~~

> **connectionLineStyle**: `null` | `CSSProperties`

#### Deprecated

use [ConnectionLineOptions.style](ConnectionLineOptions.md#style)

#### Overrides

`Omit.connectionLineStyle`

***

### ~~connectionLineType~~

> **connectionLineType**: `null` | [`ConnectionLineType`](../enumerations/ConnectionLineType.md)

#### Deprecated

use [ConnectionLineOptions.type](ConnectionLineOptions.md#type)

#### Overrides

`Omit.connectionLineType`

***

### connectionLookup

> **connectionLookup**: [`ConnectionLookup`](../type-aliases/ConnectionLookup.md)

***

### connectionMode

> **connectionMode**: [`ConnectionMode`](../enumerations/ConnectionMode.md)

#### Overrides

`Omit.connectionMode`

***

### connectionPosition

> **connectionPosition**: [`XYPosition`](XYPosition.md)

***

### connectionRadius

> **connectionRadius**: `number`

#### Overrides

`Omit.connectionRadius`

***

### connectionStartHandle

> **connectionStartHandle**: `null` | [`ConnectingHandle`](ConnectingHandle.md)

***

### connectionStatus

> **connectionStatus**: `null` | [`ConnectionStatus`](../type-aliases/ConnectionStatus.md)

***

### connectOnClick

> **connectOnClick**: `boolean`

allow connection with click handlers, i.e. support touch devices

#### Overrides

`Omit.connectOnClick`

***

### d3Selection

> `readonly` **d3Selection**: `null` | [`D3Selection`](../type-aliases/D3Selection.md)

***

### d3Zoom

> `readonly` **d3Zoom**: `null` | [`D3Zoom`](../type-aliases/D3Zoom.md)

***

### d3ZoomHandler

> `readonly` **d3ZoomHandler**: `null` | [`D3ZoomHandler`](../type-aliases/D3ZoomHandler.md)

***

### defaultEdgeOptions

> **defaultEdgeOptions**: `undefined` | [`DefaultEdgeOptions`](../type-aliases/DefaultEdgeOptions.md)

does not work for the `addEdge` utility!

#### Overrides

`Omit.defaultEdgeOptions`

***

### defaultMarkerColor

> **defaultMarkerColor**: `string`

#### Overrides

`Omit.defaultMarkerColor`

***

### defaultViewport

> **defaultViewport**: `Partial`<[`ViewportTransform`](ViewportTransform.md)>

#### Overrides

`Omit.defaultViewport`

***

### deleteKeyCode

> **deleteKeyCode**: `null` | `KeyFilter`

#### Overrides

`Omit.deleteKeyCode`

***

### dimensions

> `readonly` **dimensions**: [`Dimensions`](Dimensions.md)

viewport dimensions - do not change!

***

### disableKeyboardA11y

> **disableKeyboardA11y**: `boolean`

#### Overrides

`Omit.disableKeyboardA11y`

***

### edges

> **edges**: [`GraphEdge`](../type-aliases/GraphEdge.md)\[]

all stored edges

#### Overrides

`Omit.edges`

***

### edgesFocusable

> **edgesFocusable**: `boolean`

#### Overrides

`Omit.edgesFocusable`

***

### edgesUpdatable

> **edgesUpdatable**: [`EdgeUpdatable`](../type-aliases/EdgeUpdatable.md)

#### Overrides

`Omit.edgesUpdatable`

***

### edgeTypes?

> `optional` **edgeTypes**: [`EdgeTypesObject`](../type-aliases/EdgeTypesObject.md)

either use the edgeTypes prop to define your edge-types or use slots (\<template #edge-mySpecialType="props">)

#### Inherited from

`Omit.edgeTypes`

***

### edgeUpdaterRadius

> **edgeUpdaterRadius**: `number`

#### Overrides

`Omit.edgeUpdaterRadius`

***

### elementsSelectable

> **elementsSelectable**: `boolean`

#### Overrides

`Omit.elementsSelectable`

***

### elevateEdgesOnSelect

> **elevateEdgesOnSelect**: `boolean`

elevates edges when selected and applies z-Index to put them above their nodes

#### Overrides

`Omit.elevateEdgesOnSelect`

***

### elevateNodesOnSelect

> **elevateNodesOnSelect**: `boolean`

elevates nodes when selected and applies z-Index + 1000

#### Overrides

`Omit.elevateNodesOnSelect`

***

### fitViewOnInit

> **fitViewOnInit**: `boolean`

will be renamed to `fitView`

#### Overrides

`Omit.fitViewOnInit`

***

### fitViewOnInitDone

> **fitViewOnInitDone**: `boolean`

***

### hooks

> `readonly` **hooks**: `Readonly`<`object`>

Event hooks, you can manipulate the triggers at your own peril

#### Type declaration

##### clickConnectEnd

> **clickConnectEnd**: `EventHookExtended`<`undefined` | `MouseEvent` | `TouchEvent`>

##### clickConnectStart

> **clickConnectStart**: `EventHookExtended`<`object` & [`OnConnectStartParams`](OnConnectStartParams.md)>

##### connect

> **connect**: `EventHookExtended`<[`Connection`](Connection.md)>

##### connectEnd

> **connectEnd**: `EventHookExtended`<`undefined` | `MouseEvent` | `TouchEvent`>

##### connectStart

> **connectStart**: `EventHookExtended`<`object` & [`OnConnectStartParams`](OnConnectStartParams.md)>

##### edgeClick

> **edgeClick**: `EventHookExtended`<[`EdgeMouseEvent`](EdgeMouseEvent.md)>

##### edgeContextMenu

> **edgeContextMenu**: `EventHookExtended`<[`EdgeMouseEvent`](EdgeMouseEvent.md)>

##### edgeDoubleClick

> **edgeDoubleClick**: `EventHookExtended`<[`EdgeMouseEvent`](EdgeMouseEvent.md)>

##### edgeMouseEnter

> **edgeMouseEnter**: `EventHookExtended`<[`EdgeMouseEvent`](EdgeMouseEvent.md)>

##### edgeMouseLeave

> **edgeMouseLeave**: `EventHookExtended`<[`EdgeMouseEvent`](EdgeMouseEvent.md)>

##### edgeMouseMove

> **edgeMouseMove**: `EventHookExtended`<[`EdgeMouseEvent`](EdgeMouseEvent.md)>

##### edgesChange

> **edgesChange**: `EventHookExtended`<[`EdgeChange`](../type-aliases/EdgeChange.md)\[]>

##### edgeUpdate

> **edgeUpdate**: `EventHookExtended`<[`EdgeUpdateEvent`](EdgeUpdateEvent.md)>

##### edgeUpdateEnd

> **edgeUpdateEnd**: `EventHookExtended`<[`EdgeMouseEvent`](EdgeMouseEvent.md)>

##### edgeUpdateStart

> **edgeUpdateStart**: `EventHookExtended`<[`EdgeMouseEvent`](EdgeMouseEvent.md)>

##### error

> **error**: `EventHookExtended`<[`VueFlowError`](../classes/VueFlowError.md)<[`ErrorCode`](../enumerations/ErrorCode.md), \[] | \[`string`] | \[`null` | `string`] | \[`string`, `string`] | \[`string`] | \[`string`] | \[`string`] | \[`string`, `string`] | \[`string`, `string`] | \[`string`] | \[`string`, `string`, `string`] | \[`string`, `string`, `string`] | \[`string`] | \[`string`]>>

##### init

> **init**: `EventHookExtended`<[`VueFlowStore`](../type-aliases/VueFlowStore.md)>

##### miniMapNodeClick

> **miniMapNodeClick**: `EventHookExtended`<[`NodeMouseEvent`](NodeMouseEvent.md)>

##### miniMapNodeDoubleClick

> **miniMapNodeDoubleClick**: `EventHookExtended`<[`NodeMouseEvent`](NodeMouseEvent.md)>

##### miniMapNodeMouseEnter

> **miniMapNodeMouseEnter**: `EventHookExtended`<[`NodeMouseEvent`](NodeMouseEvent.md)>

##### miniMapNodeMouseLeave

> **miniMapNodeMouseLeave**: `EventHookExtended`<[`NodeMouseEvent`](NodeMouseEvent.md)>

##### miniMapNodeMouseMove

> **miniMapNodeMouseMove**: `EventHookExtended`<[`NodeMouseEvent`](NodeMouseEvent.md)>

##### move

> **move**: `EventHookExtended`<`object`>

###### Type declaration

###### event

> **event**: `WheelEvent` | `D3ZoomEvent`<`HTMLDivElement`, `any`>

###### flowTransform

> **flowTransform**: [`ViewportTransform`](ViewportTransform.md)

##### moveEnd

> **moveEnd**: `EventHookExtended`<`object`>

###### Type declaration

###### event

> **event**: `WheelEvent` | `D3ZoomEvent`<`HTMLDivElement`, `any`>

###### flowTransform

> **flowTransform**: [`ViewportTransform`](ViewportTransform.md)

##### moveStart

> **moveStart**: `EventHookExtended`<`object`>

###### Type declaration

###### event

> **event**: `WheelEvent` | `D3ZoomEvent`<`HTMLDivElement`, `any`>

###### flowTransform

> **flowTransform**: [`ViewportTransform`](ViewportTransform.md)

##### nodeClick

> **nodeClick**: `EventHookExtended`<[`NodeMouseEvent`](NodeMouseEvent.md)>

##### nodeContextMenu

> **nodeContextMenu**: `EventHookExtended`<[`NodeMouseEvent`](NodeMouseEvent.md)>

##### nodeDoubleClick

> **nodeDoubleClick**: `EventHookExtended`<[`NodeMouseEvent`](NodeMouseEvent.md)>

##### nodeDrag

> **nodeDrag**: `EventHookExtended`<[`NodeDragEvent`](NodeDragEvent.md)>

##### nodeDragStart

> **nodeDragStart**: `EventHookExtended`<[`NodeDragEvent`](NodeDragEvent.md)>

##### nodeDragStop

> **nodeDragStop**: `EventHookExtended`<[`NodeDragEvent`](NodeDragEvent.md)>

##### nodeMouseEnter

> **nodeMouseEnter**: `EventHookExtended`<[`NodeMouseEvent`](NodeMouseEvent.md)>

##### nodeMouseLeave

> **nodeMouseLeave**: `EventHookExtended`<[`NodeMouseEvent`](NodeMouseEvent.md)>

##### nodeMouseMove

> **nodeMouseMove**: `EventHookExtended`<[`NodeMouseEvent`](NodeMouseEvent.md)>

##### nodesChange

> **nodesChange**: `EventHookExtended`<[`NodeChange`](../type-aliases/NodeChange.md)\[]>

##### nodesInitialized

> **nodesInitialized**: `EventHookExtended`<[`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]>

##### paneClick

> **paneClick**: `EventHookExtended`<`MouseEvent`>

##### paneContextMenu

> **paneContextMenu**: `EventHookExtended`<`MouseEvent`>

##### paneMouseEnter

> **paneMouseEnter**: `EventHookExtended`<`PointerEvent`>

##### paneMouseLeave

> **paneMouseLeave**: `EventHookExtended`<`PointerEvent`>

##### paneMouseMove

> **paneMouseMove**: `EventHookExtended`<`PointerEvent`>

##### ~~paneReady~~

> **paneReady**: `EventHookExtended`<[`VueFlowStore`](../type-aliases/VueFlowStore.md)>

###### Deprecated

use `init` instead

##### paneScroll

> **paneScroll**: `EventHookExtended`<`undefined` | `WheelEvent`>

##### selectionContextMenu

> **selectionContextMenu**: `EventHookExtended`<`object`>

###### Type declaration

###### event

> **event**: `MouseEvent`

###### nodes

> **nodes**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

##### selectionDrag

> **selectionDrag**: `EventHookExtended`<[`NodeDragEvent`](NodeDragEvent.md)>

##### selectionDragStart

> **selectionDragStart**: `EventHookExtended`<[`NodeDragEvent`](NodeDragEvent.md)>

##### selectionDragStop

> **selectionDragStop**: `EventHookExtended`<[`NodeDragEvent`](NodeDragEvent.md)>

##### selectionEnd

> **selectionEnd**: `EventHookExtended`<`MouseEvent`>

##### selectionStart

> **selectionStart**: `EventHookExtended`<`MouseEvent`>

##### updateNodeInternals

> **updateNodeInternals**: `EventHookExtended`<`string`\[]>

##### viewportChange

> **viewportChange**: `EventHookExtended`<[`ViewportTransform`](ViewportTransform.md)>

##### viewportChangeEnd

> **viewportChangeEnd**: `EventHookExtended`<[`ViewportTransform`](ViewportTransform.md)>

##### viewportChangeStart

> **viewportChangeStart**: `EventHookExtended`<[`ViewportTransform`](ViewportTransform.md)>

***

### initialized

> **initialized**: `boolean`

***

### isValidConnection

> **isValidConnection**: `null` | [`ValidConnectionFunc`](../type-aliases/ValidConnectionFunc.md)

#### Overrides

`Omit.isValidConnection`

***

### maxZoom

> **maxZoom**: `number`

use setMaxZoom action to change maxZoom

#### Overrides

`Omit.maxZoom`

***

### minZoom

> **minZoom**: `number`

use setMinZoom action to change minZoom

#### Overrides

`Omit.minZoom`

***

### multiSelectionActive

> **multiSelectionActive**: `boolean`

***

### multiSelectionKeyCode

> **multiSelectionKeyCode**: `null` | `KeyFilter`

#### Overrides

`Omit.multiSelectionKeyCode`

***

### nodeDragThreshold

> **nodeDragThreshold**: `number`

#### Overrides

`Omit.nodeDragThreshold`

***

### nodeExtent

> **nodeExtent**: [`CoordinateExtent`](../type-aliases/CoordinateExtent.md) | [`CoordinateExtentRange`](CoordinateExtentRange.md)

#### Overrides

`Omit.nodeExtent`

***

### nodes

> **nodes**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

all stored nodes

#### Overrides

`Omit.nodes`

***

### nodesConnectable

> **nodesConnectable**: `boolean`

#### Overrides

`Omit.nodesConnectable`

***

### nodesDraggable

> **nodesDraggable**: `boolean`

#### Overrides

`Omit.nodesDraggable`

***

### nodesFocusable

> **nodesFocusable**: `boolean`

#### Overrides

`Omit.nodesFocusable`

***

### nodesSelectionActive

> **nodesSelectionActive**: `boolean`

***

### nodeTypes?

> `optional` **nodeTypes**: [`NodeTypesObject`](../type-aliases/NodeTypesObject.md)

either use the nodeTypes prop to define your node-types or use slots (\<template #node-mySpecialType="props">)

#### Inherited from

`Omit.nodeTypes`

***

### noDragClassName

> **noDragClassName**: `string`

#### Overrides

`Omit.noDragClassName`

***

### noPanClassName

> **noPanClassName**: `string`

#### Overrides

`Omit.noPanClassName`

***

### noWheelClassName

> **noWheelClassName**: `string`

#### Overrides

`Omit.noWheelClassName`

***

### onlyRenderVisibleElements

> **onlyRenderVisibleElements**: `boolean`

if true will skip rendering any elements currently not inside viewport until they become visible

#### Overrides

`Omit.onlyRenderVisibleElements`

***

### panActivationKeyCode

> **panActivationKeyCode**: `null` | `KeyFilter`

#### Overrides

`Omit.panActivationKeyCode`

***

### paneClickDistance

> **paneClickDistance**: `number`

Distance that the mouse can move between mousedown/up that will trigger a click

#### Default

```ts
0
```

#### Overrides

`Omit.paneClickDistance`

***

### paneDragging

> **paneDragging**: `boolean`

***

### panOnDrag

> **panOnDrag**: `boolean` | `number`\[]

move pane on drag, replaced prop `paneMovable`

#### Overrides

`Omit.panOnDrag`

***

### panOnScroll

> **panOnScroll**: `boolean`

#### Overrides

`Omit.panOnScroll`

***

### panOnScrollMode

> **panOnScrollMode**: [`PanOnScrollMode`](../enumerations/PanOnScrollMode.md)

#### Overrides

`Omit.panOnScrollMode`

***

### panOnScrollSpeed

> **panOnScrollSpeed**: `number`

#### Overrides

`Omit.panOnScrollSpeed`

***

### preventScrolling

> **preventScrolling**: `boolean`

If set to false, scrolling inside the viewport will be disabled and instead the page scroll will be used

#### Overrides

`Omit.preventScrolling`

***

### selectionKeyCode

> **selectionKeyCode**: `null` | `false` | `KeyFilter`

#### Overrides

`Omit.selectionKeyCode`

***

### selectionMode

> **selectionMode**: [`SelectionMode`](../enumerations/SelectionMode.md)

#### Overrides

`Omit.selectionMode`

***

### selectNodesOnDrag

> **selectNodesOnDrag**: `boolean`

#### Overrides

`Omit.selectNodesOnDrag`

***

### snapGrid

> **snapGrid**: [`SnapGrid`](../type-aliases/SnapGrid.md)

#### Overrides

`Omit.snapGrid`

***

### snapToGrid

> **snapToGrid**: `boolean`

#### Overrides

`Omit.snapToGrid`

***

### translateExtent

> **translateExtent**: [`CoordinateExtent`](../type-aliases/CoordinateExtent.md)

use setTranslateExtent action to change translateExtent

#### Overrides

`Omit.translateExtent`

***

### userSelectionActive

> **userSelectionActive**: `boolean`

***

### userSelectionRect

> **userSelectionRect**: `null` | [`SelectionRect`](SelectionRect.md)

***

### viewport

> `readonly` **viewport**: [`ViewportTransform`](ViewportTransform.md)

viewport transform x, y, z - do not change!

***

### viewportRef

> **viewportRef**: `null` | `HTMLDivElement`

Vue flow viewport element

***

### vueFlowRef

> **vueFlowRef**: `null` | `HTMLDivElement`

Vue flow element ref

***

### zoomActivationKeyCode

> **zoomActivationKeyCode**: `null` | `KeyFilter`

#### Overrides

`Omit.zoomActivationKeyCode`

***

### zoomOnDoubleClick

> **zoomOnDoubleClick**: `boolean`

#### Overrides

`Omit.zoomOnDoubleClick`

***

### zoomOnPinch

> **zoomOnPinch**: `boolean`

#### Overrides

`Omit.zoomOnPinch`

***

### zoomOnScroll

> **zoomOnScroll**: `boolean`

#### Overrides

`Omit.zoomOnScroll`
