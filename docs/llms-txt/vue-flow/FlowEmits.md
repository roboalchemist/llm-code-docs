# Source: https://vueflow.dev/typedocs/interfaces/FlowEmits.md

---
url: /typedocs/interfaces/FlowEmits.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: FlowEmits()

> **FlowEmits**(`event`, `changes`): `void`

## Parameters

• **event**: `"nodesChange"`

• **changes**: [`NodeChange`](../type-aliases/NodeChange.md)\[]

## Returns

`void`

> **FlowEmits**(`event`, `changes`): `void`

## Parameters

• **event**: `"edgesChange"`

• **changes**: [`EdgeChange`](../type-aliases/EdgeChange.md)\[]

## Returns

`void`

> **FlowEmits**(`event`): `void`

## Parameters

• **event**: `"nodesInitialized"`

## Returns

`void`

> **FlowEmits**(`event`, `paneEvent`): `void`

## Parameters

• **event**: `"paneReady"`

• **paneEvent**: [`VueFlowStore`](../type-aliases/VueFlowStore.md)

## Returns

`void`

## Deprecated

use `init` instead

> **FlowEmits**(`event`, `paneEvent`): `void`

## Parameters

• **event**: `"init"`

• **paneEvent**: [`VueFlowStore`](../type-aliases/VueFlowStore.md)

## Returns

`void`

> **FlowEmits**(`event`): `void`

## Parameters

• **event**: `"updateNodeInternals"`

## Returns

`void`

> **FlowEmits**(`event`, `error`): `void`

## Parameters

• **event**: `"error"`

• **error**: [`VueFlowError`](../classes/VueFlowError.md)<[`ErrorCode`](../enumerations/ErrorCode.md), \[] | \[`string`] | \[`null` | `string`] | \[`string`, `string`] | \[`string`] | \[`string`] | \[`string`] | \[`string`, `string`] | \[`string`, `string`] | \[`string`] | \[`string`, `string`, `string`] | \[`string`, `string`, `string`] | \[`string`] | \[`string`]>

## Returns

`void`

> **FlowEmits**(`event`, `connectionEvent`): `void`

## Parameters

• **event**: `"connect"`

• **connectionEvent**: [`Connection`](Connection.md)

## Returns

`void`

> **FlowEmits**(`event`, `connectionEvent`): `void`

## Parameters

• **event**: `"connectStart"`

• **connectionEvent**: `object` & [`OnConnectStartParams`](OnConnectStartParams.md)

## Returns

`void`

> **FlowEmits**(`event`, `connectionEvent`?): `void`

## Parameters

• **event**: `"connectEnd"`

• **connectionEvent?**: `MouseEvent`

## Returns

`void`

> **FlowEmits**(`event`, `connectionEvent`): `void`

## Parameters

• **event**: `"clickConnectStart"`

• **connectionEvent**: `object` & [`OnConnectStartParams`](OnConnectStartParams.md)

## Returns

`void`

> **FlowEmits**(`event`, `connectionEvent`?): `void`

## Parameters

• **event**: `"clickConnectEnd"`

• **connectionEvent?**: `MouseEvent`

## Returns

`void`

> **FlowEmits**(`event`, `moveEvent`): `void`

## Parameters

• **event**: `"moveStart"`

• **moveEvent**

• **moveEvent.event**: `D3ZoomEvent`<`HTMLDivElement`, `any`>

• **moveEvent.flowTransform**: [`ViewportTransform`](ViewportTransform.md)

## Returns

`void`

> **FlowEmits**(`event`, `moveEvent`): `void`

## Parameters

• **event**: `"move"`

• **moveEvent**

• **moveEvent.event**: `D3ZoomEvent`<`HTMLDivElement`, `any`>

• **moveEvent.flowTransform**: [`ViewportTransform`](ViewportTransform.md)

## Returns

`void`

> **FlowEmits**(`event`, `moveEvent`): `void`

## Parameters

• **event**: `"moveEnd"`

• **moveEvent**

• **moveEvent.event**: `D3ZoomEvent`<`HTMLDivElement`, `any`>

• **moveEvent.flowTransform**: [`ViewportTransform`](ViewportTransform.md)

## Returns

`void`

> **FlowEmits**(`event`, `selectionEvent`): `void`

## Parameters

• **event**: `"selectionDragStart"`

• **selectionEvent**: [`NodeDragEvent`](NodeDragEvent.md)

## Returns

`void`

> **FlowEmits**(`event`, `selectionEvent`): `void`

## Parameters

• **event**: `"selectionDrag"`

• **selectionEvent**: [`NodeDragEvent`](NodeDragEvent.md)

## Returns

`void`

> **FlowEmits**(`event`, `selectionEvent`): `void`

## Parameters

• **event**: `"selectionDragStop"`

• **selectionEvent**: [`NodeDragEvent`](NodeDragEvent.md)

## Returns

`void`

> **FlowEmits**(`event`, `selectionEvent`): `void`

## Parameters

• **event**: `"selectionContextMenu"`

• **selectionEvent**

• **selectionEvent.event**: `MouseEvent`

• **selectionEvent.nodes**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

## Returns

`void`

> **FlowEmits**(`event`, `selectionEvent`): `void`

## Parameters

• **event**: `"selectionStart"`

• **selectionEvent**: `MouseEvent`

## Returns

`void`

> **FlowEmits**(`event`, `selectionEvent`): `void`

## Parameters

• **event**: `"selectionEnd"`

• **selectionEvent**: `MouseEvent`

## Returns

`void`

> **FlowEmits**(`event`, `viewport`): `void`

## Parameters

• **event**: `"viewportChangeStart"`

• **viewport**: [`ViewportTransform`](ViewportTransform.md)

## Returns

`void`

> **FlowEmits**(`event`, `viewport`): `void`

## Parameters

• **event**: `"viewportChange"`

• **viewport**: [`ViewportTransform`](ViewportTransform.md)

## Returns

`void`

> **FlowEmits**(`event`, `viewport`): `void`

## Parameters

• **event**: `"viewportChangeEnd"`

• **viewport**: [`ViewportTransform`](ViewportTransform.md)

## Returns

`void`

> **FlowEmits**(`event`, `paneScrollEvent`): `void`

## Parameters

• **event**: `"paneScroll"`

• **paneScrollEvent**: `undefined` | `WheelEvent`

## Returns

`void`

> **FlowEmits**(`event`, `paneMouseEvent`): `void`

## Parameters

• **event**: `"paneClick"` | `"paneContextMenu"` | `"paneMouseEnter"` | `"paneMouseMove"` | `"paneMouseLeave"`

• **paneMouseEvent**: `MouseEvent`

## Returns

`void`

> **FlowEmits**(`event`, `edgeUpdateEvent`): `void`

## Parameters

• **event**: `"edgeUpdate"`

• **edgeUpdateEvent**: [`EdgeUpdateEvent`](EdgeUpdateEvent.md)

## Returns

`void`

> **FlowEmits**(`event`, `edgeMouseEvent`): `void`

## Parameters

• **event**: `"edgeContextMenu"` | `"edgeMouseEnter"` | `"edgeMouseMove"` | `"edgeMouseLeave"` | `"edgeDoubleClick"` | `"edgeClick"` | `"edgeUpdateStart"` | `"edgeUpdateEnd"`

• **edgeMouseEvent**: [`EdgeMouseEvent`](EdgeMouseEvent.md)

## Returns

`void`

> **FlowEmits**(`event`, `nodeMouseEvent`): `void`

## Parameters

• **event**: `"nodeDoubleClick"` | `"nodeClick"` | `"nodeMouseEnter"` | `"nodeMouseMove"` | `"nodeMouseLeave"` | `"nodeContextMenu"`

• **nodeMouseEvent**: [`NodeMouseEvent`](NodeMouseEvent.md)

## Returns

`void`

> **FlowEmits**(`event`, `nodeDragEvent`): `void`

## Parameters

• **event**: `"nodeDragStart"` | `"nodeDrag"` | `"nodeDragStop"`

• **nodeDragEvent**: [`NodeDragEvent`](NodeDragEvent.md)

## Returns

`void`

> **FlowEmits**(`event`, `nodeMouseEvent`): `void`

## Parameters

• **event**: `"miniMapNodeClick"` | `"miniMapNodeDoubleClick"` | `"miniMapNodeMouseEnter"` | `"miniMapNodeMouseMove"` | `"miniMapNodeMouseLeave"`

• **nodeMouseEvent**: [`NodeMouseEvent`](NodeMouseEvent.md)

## Returns

`void`

> **FlowEmits**(`event`, `value`): `void`

v-model event definitions

## Parameters

• **event**: `"update:modelValue"`

• **value**: [`FlowElements`](../type-aliases/FlowElements.md)<`any`, `any`, `any`, `any`>

## Returns

`void`

> **FlowEmits**(`event`, `value`): `void`

## Parameters

• **event**: `"update:nodes"`

• **value**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

## Returns

`void`

> **FlowEmits**(`event`, `value`): `void`

## Parameters

• **event**: `"update:edges"`

• **value**: [`GraphEdge`](../type-aliases/GraphEdge.md)\[]

## Returns

`void`
