# Source: https://vueflow.dev/typedocs/interfaces/Actions.md

---
url: /typedocs/interfaces/Actions.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: Actions

## Extends

* `Omit`<`ViewportHelper`, `"viewportInitialized"`>

## Properties

### $destroy()

> **$destroy**: () => `void`

remove store instance from global storage and destroy it (will invalidate effect scopes)

#### Returns

`void`

***

### $reset()

> **$reset**: () => `void`

reset state to defaults

#### Returns

`void`

***

### addEdges

> **addEdges**: [`AddEdges`](../type-aliases/AddEdges.md)

parses edges and adds to state

***

### addNodes

> **addNodes**: [`AddNodes`](../type-aliases/AddNodes.md)

parses nodes and adds to state

***

### addSelectedEdges()

> **addSelectedEdges**: (`edges`) => `void`

manually select edges and add to state

#### Parameters

• **edges**: [`GraphEdge`](../type-aliases/GraphEdge.md)\[]

#### Returns

`void`

***

### ~~addSelectedElements()~~

> **addSelectedElements**: (`elements`) => `void`

manually select elements and add to state

#### Parameters

• **elements**: [`FlowElements`](../type-aliases/FlowElements.md)

#### Returns

`void`

#### Deprecated

will be removed in the next major, use [Actions.addSelectedNodes](Actions.md#addselectednodes) or [Actions.addSelectedEdges](Actions.md#addselectededges) instead

***

### addSelectedNodes()

> **addSelectedNodes**: (`nodes`) => `void`

manually select nodes and add to state

#### Parameters

• **nodes**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

#### Returns

`void`

***

### applyEdgeChanges()

> **applyEdgeChanges**: (`changes`) => [`GraphEdge`](../type-aliases/GraphEdge.md)\[]

applies default edge change handler

#### Parameters

• **changes**: [`EdgeChange`](../type-aliases/EdgeChange.md)\[]

#### Returns

[`GraphEdge`](../type-aliases/GraphEdge.md)\[]

***

### applyNodeChanges()

> **applyNodeChanges**: (`changes`) => [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

applies default node change handler

#### Parameters

• **changes**: [`NodeChange`](../type-aliases/NodeChange.md)\[]

#### Returns

[`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

***

### endConnection()

> **endConnection**: (`event`?, `isClick`?) => `void`

end (or cancel) a connection

#### Parameters

• **event?**: `MouseEvent` | `TouchEvent`

• **isClick?**: `boolean`

#### Returns

`void`

***

### findEdge

> **findEdge**: [`FindEdge`](../type-aliases/FindEdge.md)

find an edge by id

***

### findNode

> **findNode**: [`FindNode`](../type-aliases/FindNode.md)

find a node by id

***

### fitBounds

> **fitBounds**: [`FitBounds`](../type-aliases/FitBounds.md)

#### Inherited from

`Omit.fitBounds`

***

### fitView

> **fitView**: [`FitView`](../type-aliases/FitView.md)

#### Inherited from

`Omit.fitView`

***

### flowToScreenCoordinate

> **flowToScreenCoordinate**: [`Project`](../type-aliases/Project.md)

#### Inherited from

`Omit.flowToScreenCoordinate`

***

### fromObject()

> **fromObject**: (`obj`) => `Promise`<`boolean`>

load graph from export obj

#### Parameters

• **obj**: [`FlowImportObject`](../type-aliases/FlowImportObject.md)

#### Returns

`Promise`<`boolean`>

***

### getConnectedEdges()

> **getConnectedEdges**: (`nodesOrId`) => [`GraphEdge`](../type-aliases/GraphEdge.md)\[]

get a node's connected edges

#### Parameters

• **nodesOrId**: `string` | [`Node`](Node.md)<`any`, `any`, `string`>\[]

#### Returns

[`GraphEdge`](../type-aliases/GraphEdge.md)\[]

***

### getHandleConnections()

> **getHandleConnections**: (`__namedParameters`) => [`HandleConnection`](HandleConnection.md)\[]

get all connections of a handle belonging to a node

#### Parameters

• **\_\_namedParameters**

• **\_\_namedParameters.id?**: `null` | `string`

• **\_\_namedParameters.nodeId**: `string`

• **\_\_namedParameters.type**: [`HandleType`](../type-aliases/HandleType.md)

#### Returns

[`HandleConnection`](HandleConnection.md)\[]

***

### getIncomers()

> **getIncomers**: (`nodeOrId`) => [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

get a node's incomers

#### Parameters

• **nodeOrId**: `string` | [`Node`](Node.md)<`any`, `any`, `string`>

#### Returns

[`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

***

### getIntersectingNodes

> **getIntersectingNodes**: [`GetIntersectingNodes`](../type-aliases/GetIntersectingNodes.md)

returns all node intersections

***

### getOutgoers()

> **getOutgoers**: (`nodeOrId`) => [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

get a node's outgoers

#### Parameters

• **nodeOrId**: `string` | [`Node`](Node.md)<`any`, `any`, `string`>

#### Returns

[`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

***

### ~~getTransform~~

> **getTransform**: [`GetViewport`](../type-aliases/GetViewport.md)

#### Deprecated

use getViewport instead

#### Inherited from

`Omit.getTransform`

***

### getViewport

> **getViewport**: [`GetViewport`](../type-aliases/GetViewport.md)

#### Inherited from

`Omit.getViewport`

***

### isNodeIntersecting

> **isNodeIntersecting**: [`IsNodeIntersecting`](../type-aliases/IsNodeIntersecting.md)

check if a node is intersecting with a defined area

***

### panBy()

> **panBy**: (`delta`) => `boolean`

pan the viewport; return indicates if a transform has happened or not

#### Parameters

• **delta**: [`XYPosition`](XYPosition.md)

#### Returns

`boolean`

***

### project

> **project**: [`Project`](../type-aliases/Project.md)

#### Inherited from

`Omit.project`

***

### removeEdges

> **removeEdges**: [`RemoveEdges`](../type-aliases/RemoveEdges.md)

remove edges from state

***

### removeNodes

> **removeNodes**: [`RemoveNodes`](../type-aliases/RemoveNodes.md)

remove nodes (and possibly connected edges and children) from state

***

### removeSelectedEdges()

> **removeSelectedEdges**: (`edges`) => `void`

manually unselect edges and remove from state

#### Parameters

• **edges**: [`GraphEdge`](../type-aliases/GraphEdge.md)\[]

#### Returns

`void`

***

### removeSelectedElements()

> **removeSelectedElements**: (`elements`?) => `void`

unselect selected elements (if none are passed, all elements are unselected)

#### Parameters

• **elements?**: [`Elements`](../type-aliases/Elements.md)

#### Returns

`void`

***

### removeSelectedNodes()

> **removeSelectedNodes**: (`nodes`) => `void`

manually unselect nodes and remove from state

#### Parameters

• **nodes**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

#### Returns

`void`

***

### screenToFlowCoordinate

> **screenToFlowCoordinate**: [`Project`](../type-aliases/Project.md)

#### Inherited from

`Omit.screenToFlowCoordinate`

***

### setCenter

> **setCenter**: [`SetCenter`](../type-aliases/SetCenter.md)

#### Inherited from

`Omit.setCenter`

***

### setEdges

> **setEdges**: [`SetEdges`](../type-aliases/SetEdges.md)

parses edges and re-sets the state

***

### setElements

> **setElements**: [`SetElements`](../type-aliases/SetElements.md)

parses elements (nodes + edges) and re-sets the state

***

### setInteractive()

> **setInteractive**: (`isInteractive`) => `void`

enable/disable node interaction (dragging, selecting etc)

#### Parameters

• **isInteractive**: `boolean`

#### Returns

`void`

***

### setMaxZoom()

> **setMaxZoom**: (`zoom`) => `void`

apply max zoom value to d3

#### Parameters

• **zoom**: `number`

#### Returns

`void`

***

### setMinZoom()

> **setMinZoom**: (`zoom`) => `void`

apply min zoom value to d3

#### Parameters

• **zoom**: `number`

#### Returns

`void`

***

### setNodeExtent()

> **setNodeExtent**: (`nodeExtent`) => `void`

apply extent to nodes

#### Parameters

• **nodeExtent**: [`CoordinateExtent`](../type-aliases/CoordinateExtent.md) | [`CoordinateExtentRange`](CoordinateExtentRange.md)

#### Returns

`void`

***

### setNodes

> **setNodes**: [`SetNodes`](../type-aliases/SetNodes.md)

parses nodes and re-sets the state

***

### setPaneClickDistance()

> **setPaneClickDistance**: (`distance`) => `void`

#### Parameters

• **distance**: `number`

#### Returns

`void`

***

### setState

> **setState**: [`SetState`](../type-aliases/SetState.md)

set new state

***

### ~~setTransform~~

> **setTransform**: [`SetViewport`](../type-aliases/SetViewport.md)

#### Deprecated

use setViewport instead

#### Inherited from

`Omit.setTransform`

***

### setTranslateExtent()

> **setTranslateExtent**: (`translateExtent`) => `void`

apply translate extent to d3

#### Parameters

• **translateExtent**: [`CoordinateExtent`](../type-aliases/CoordinateExtent.md)

#### Returns

`void`

***

### setViewport

> **setViewport**: [`SetViewport`](../type-aliases/SetViewport.md)

#### Inherited from

`Omit.setViewport`

***

### startConnection()

> **startConnection**: (`startHandle`, `position`?, `isClick`?) => `void`

start a connection

#### Parameters

• **startHandle**: [`ConnectingHandle`](ConnectingHandle.md)

• **position?**: [`XYPosition`](XYPosition.md)

• **isClick?**: `boolean`

#### Returns

`void`

***

### toObject()

> **toObject**: () => [`FlowExportObject`](FlowExportObject.md)

return an object of graph values (elements, viewport transform) for storage and re-loading a graph

#### Returns

[`FlowExportObject`](FlowExportObject.md)

***

### updateConnection()

> **updateConnection**: (`position`, `result`?, `status`?) => `void`

update connection position

#### Parameters

• **position**: [`XYPosition`](XYPosition.md)

• **result?**: `null` | [`ConnectingHandle`](ConnectingHandle.md)

• **status?**: `null` | [`ConnectionStatus`](../type-aliases/ConnectionStatus.md)

#### Returns

`void`

***

### updateEdge

> **updateEdge**: [`UpdateEdge`](../type-aliases/UpdateEdge.md)

updates an edge

***

### updateEdgeData

> **updateEdgeData**: [`UpdateEdgeData`](../type-aliases/UpdateEdgeData.md)

updates the data of an edge

***

### updateNode

> **updateNode**: [`UpdateNode`](../type-aliases/UpdateNode.md)

updates a node

***

### updateNodeData

> **updateNodeData**: [`UpdateNodeData`](../type-aliases/UpdateNodeData.md)

updates the data of a node

***

### updateNodeDimensions

> **updateNodeDimensions**: [`UpdateNodeDimensions`](../type-aliases/UpdateNodeDimensions.md)

internal dimensions' updater, you probably don't want to use this

***

### updateNodeInternals

> **updateNodeInternals**: [`UpdateNodeInternals`](../type-aliases/UpdateNodeInternals.md)

force update node internal data, if handle bounds are incorrect, you might want to use this

***

### updateNodePositions

> **updateNodePositions**: [`UpdateNodePosition`](../type-aliases/UpdateNodePosition.md)

internal position updater, you probably don't want to use this

***

### viewportHelper

> **viewportHelper**: `ComputedRef`<`ViewportHelper`>

viewport helper instance

***

### zoomIn

> **zoomIn**: [`ZoomInOut`](../type-aliases/ZoomInOut.md)

#### Inherited from

`Omit.zoomIn`

***

### zoomOut

> **zoomOut**: [`ZoomInOut`](../type-aliases/ZoomInOut.md)

#### Inherited from

`Omit.zoomOut`

***

### zoomTo

> **zoomTo**: [`ZoomTo`](../type-aliases/ZoomTo.md)

#### Inherited from

`Omit.zoomTo`
