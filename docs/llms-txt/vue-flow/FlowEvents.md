# Source: https://vueflow.dev/typedocs/interfaces/FlowEvents.md

---
url: /typedocs/interfaces/FlowEvents.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: FlowEvents

## Properties

### clickConnectEnd

> **clickConnectEnd**: `undefined` | `MouseEvent` | `TouchEvent`

***

### clickConnectStart

> **clickConnectStart**: `object` & [`OnConnectStartParams`](OnConnectStartParams.md)

#### Type declaration

##### event?

> `optional` **event**: `MouseEvent` | `TouchEvent`

***

### connect

> **connect**: [`Connection`](Connection.md)

***

### connectEnd

> **connectEnd**: `undefined` | `MouseEvent` | `TouchEvent`

***

### connectStart

> **connectStart**: `object` & [`OnConnectStartParams`](OnConnectStartParams.md)

#### Type declaration

##### event?

> `optional` **event**: `MouseEvent` | `TouchEvent`

***

### edgeClick

> **edgeClick**: [`EdgeMouseEvent`](EdgeMouseEvent.md)

***

### edgeContextMenu

> **edgeContextMenu**: [`EdgeMouseEvent`](EdgeMouseEvent.md)

***

### edgeDoubleClick

> **edgeDoubleClick**: [`EdgeMouseEvent`](EdgeMouseEvent.md)

***

### edgeMouseEnter

> **edgeMouseEnter**: [`EdgeMouseEvent`](EdgeMouseEvent.md)

***

### edgeMouseLeave

> **edgeMouseLeave**: [`EdgeMouseEvent`](EdgeMouseEvent.md)

***

### edgeMouseMove

> **edgeMouseMove**: [`EdgeMouseEvent`](EdgeMouseEvent.md)

***

### edgesChange

> **edgesChange**: [`EdgeChange`](../type-aliases/EdgeChange.md)\[]

***

### edgeUpdate

> **edgeUpdate**: [`EdgeUpdateEvent`](EdgeUpdateEvent.md)

***

### edgeUpdateEnd

> **edgeUpdateEnd**: [`EdgeMouseEvent`](EdgeMouseEvent.md)

***

### edgeUpdateStart

> **edgeUpdateStart**: [`EdgeMouseEvent`](EdgeMouseEvent.md)

***

### error

> **error**: [`VueFlowError`](../classes/VueFlowError.md)<[`ErrorCode`](../enumerations/ErrorCode.md), \[] | \[`string`] | \[`null` | `string`] | \[`string`, `string`] | \[`string`] | \[`string`] | \[`string`] | \[`string`, `string`] | \[`string`, `string`] | \[`string`] | \[`string`, `string`, `string`] | \[`string`, `string`, `string`] | \[`string`] | \[`string`]>

***

### init

> **init**: [`VueFlowStore`](../type-aliases/VueFlowStore.md)

***

### miniMapNodeClick

> **miniMapNodeClick**: [`NodeMouseEvent`](NodeMouseEvent.md)

***

### miniMapNodeDoubleClick

> **miniMapNodeDoubleClick**: [`NodeMouseEvent`](NodeMouseEvent.md)

***

### miniMapNodeMouseEnter

> **miniMapNodeMouseEnter**: [`NodeMouseEvent`](NodeMouseEvent.md)

***

### miniMapNodeMouseLeave

> **miniMapNodeMouseLeave**: [`NodeMouseEvent`](NodeMouseEvent.md)

***

### miniMapNodeMouseMove

> **miniMapNodeMouseMove**: [`NodeMouseEvent`](NodeMouseEvent.md)

***

### move

> **move**: `object`

#### event

> **event**: `WheelEvent` | `D3ZoomEvent`<`HTMLDivElement`, `any`>

#### flowTransform

> **flowTransform**: [`ViewportTransform`](ViewportTransform.md)

***

### moveEnd

> **moveEnd**: `object`

#### event

> **event**: `WheelEvent` | `D3ZoomEvent`<`HTMLDivElement`, `any`>

#### flowTransform

> **flowTransform**: [`ViewportTransform`](ViewportTransform.md)

***

### moveStart

> **moveStart**: `object`

#### event

> **event**: `WheelEvent` | `D3ZoomEvent`<`HTMLDivElement`, `any`>

#### flowTransform

> **flowTransform**: [`ViewportTransform`](ViewportTransform.md)

***

### nodeClick

> **nodeClick**: [`NodeMouseEvent`](NodeMouseEvent.md)

***

### nodeContextMenu

> **nodeContextMenu**: [`NodeMouseEvent`](NodeMouseEvent.md)

***

### nodeDoubleClick

> **nodeDoubleClick**: [`NodeMouseEvent`](NodeMouseEvent.md)

***

### nodeDrag

> **nodeDrag**: [`NodeDragEvent`](NodeDragEvent.md)

***

### nodeDragStart

> **nodeDragStart**: [`NodeDragEvent`](NodeDragEvent.md)

***

### nodeDragStop

> **nodeDragStop**: [`NodeDragEvent`](NodeDragEvent.md)

***

### nodeMouseEnter

> **nodeMouseEnter**: [`NodeMouseEvent`](NodeMouseEvent.md)

***

### nodeMouseLeave

> **nodeMouseLeave**: [`NodeMouseEvent`](NodeMouseEvent.md)

***

### nodeMouseMove

> **nodeMouseMove**: [`NodeMouseEvent`](NodeMouseEvent.md)

***

### nodesChange

> **nodesChange**: [`NodeChange`](../type-aliases/NodeChange.md)\[]

***

### nodesInitialized

> **nodesInitialized**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

***

### paneClick

> **paneClick**: `MouseEvent`

***

### paneContextMenu

> **paneContextMenu**: `MouseEvent`

***

### paneMouseEnter

> **paneMouseEnter**: `PointerEvent`

***

### paneMouseLeave

> **paneMouseLeave**: `PointerEvent`

***

### paneMouseMove

> **paneMouseMove**: `PointerEvent`

***

### ~~paneReady~~

> **paneReady**: [`VueFlowStore`](../type-aliases/VueFlowStore.md)

#### Deprecated

use `init` instead

***

### paneScroll

> **paneScroll**: `undefined` | `WheelEvent`

***

### selectionContextMenu

> **selectionContextMenu**: `object`

#### event

> **event**: `MouseEvent`

#### nodes

> **nodes**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

***

### selectionDrag

> **selectionDrag**: [`NodeDragEvent`](NodeDragEvent.md)

***

### selectionDragStart

> **selectionDragStart**: [`NodeDragEvent`](NodeDragEvent.md)

***

### selectionDragStop

> **selectionDragStop**: [`NodeDragEvent`](NodeDragEvent.md)

***

### selectionEnd

> **selectionEnd**: `MouseEvent`

***

### selectionStart

> **selectionStart**: `MouseEvent`

***

### updateNodeInternals

> **updateNodeInternals**: `string`\[]

***

### viewportChange

> **viewportChange**: [`ViewportTransform`](ViewportTransform.md)

***

### viewportChangeEnd

> **viewportChangeEnd**: [`ViewportTransform`](ViewportTransform.md)

***

### viewportChangeStart

> **viewportChangeStart**: [`ViewportTransform`](ViewportTransform.md)
