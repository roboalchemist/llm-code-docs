# Source: https://vueflow.dev/typedocs/interfaces/Getters.md

---
url: /typedocs/interfaces/Getters.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: Getters

## Properties

### ~~areNodesInitialized~~

> **areNodesInitialized**: `boolean`

returns a boolean flag whether all current nodes are initialized

#### Deprecated

* will be removed in next major version; use [useNodesInitialized](../functions/useNodesInitialized.md) instead

***

### ~~getEdge()~~

> **getEdge**: (`id`) => `undefined` | [`GraphEdge`](../type-aliases/GraphEdge.md)

returns an edge by id

#### Parameters

• **id**: `string`

#### Returns

`undefined` | [`GraphEdge`](../type-aliases/GraphEdge.md)

#### Deprecated

use [Actions.findEdge](Actions.md#findedge) instead

***

### getEdges

> **getEdges**: [`GraphEdge`](../type-aliases/GraphEdge.md)\[]

all visible edges

***

### getEdgeTypes

> **getEdgeTypes**: `Record`<`string`, [`EdgeComponent`](../type-aliases/EdgeComponent.md)>

returns object containing current edge types

***

### ~~getElements~~

> **getElements**: [`FlowElements`](../type-aliases/FlowElements.md)

get all elements

#### Deprecated

* will be removed in next major version

***

### ~~getNode()~~

> **getNode**: (`id`) => `undefined` | [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>

returns a node by id

#### Parameters

• **id**: `string`

#### Returns

`undefined` | [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>

#### Deprecated

use [Actions.findNode](Actions.md#findnode) instead

***

### getNodes

> **getNodes**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

all visible node

***

### ~~getNodesInitialized~~

> **getNodesInitialized**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

returns all nodes that are initialized, i.e. they have actual dimensions

#### Deprecated

* will be removed in next major version; use [useNodesInitialized](../functions/useNodesInitialized.md) instead

***

### getNodeTypes

> **getNodeTypes**: `Record`<`string`, [`NodeComponent`](../type-aliases/NodeComponent.md)>

returns object containing current node types

***

### getSelectedEdges

> **getSelectedEdges**: [`GraphEdge`](../type-aliases/GraphEdge.md)\[]

returns all currently selected edges

***

### getSelectedElements

> **getSelectedElements**: [`FlowElements`](../type-aliases/FlowElements.md)

returns all currently selected elements

***

### getSelectedNodes

> **getSelectedNodes**: [`GraphNode`](GraphNode.md)<`any`, `any`, `string`>\[]

returns all currently selected nodes
