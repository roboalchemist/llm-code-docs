# Source: https://reactflow.dev/api-reference/hooks/use-nodes-data

# useNodesData() 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useNodesData.ts)

This hook lets you subscribe to changes of a specific nodes `data` object.

``` 
import  from '@xyflow/react';
 
export default function () 
```

## Signature[](#signature) 

Function Signature 1

Function Signature 2

**Parameters:**

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+-----------------------+
| Name                                                                                                                                                                                                                                                                                                            | Type                                     | Default               |
+=================================================================================================================================================================================================================================================================================================================+==========================================+=======================+
| [](#nodeid)`nodeId` | `string`         |                       |
|                                                                                                                                                                                                                                                                                                                 |                                          |                       |
|                                                                                                                                                                                                                                                                                                                 | ::: x:mt-2                               |                       |
|                                                                                                                                                                                                                                                                                                                 | The id of the node to get the data from. |                       |
|                                                                                                                                                                                                                                                                                                                 | :::                                      |                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+-----------------------+

**Returns:**

[](#returns1)`Pick<`[`NodeType`](/api-reference/types/node)`, "id" | "type" | "data"> | null`

An object (or array of object) with `id`, `type`, `data` representing each node.

**Parameters:**

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------+-----------------------+
| Name                                                                                                                                                                                                                                                                                                              | Type                                       | Default               |
+===================================================================================================================================================================================================================================================================================================================+============================================+=======================+
| [](#nodeids)`nodeIds` | `string[]`         |                       |
|                                                                                                                                                                                                                                                                                                                   |                                            |                       |
|                                                                                                                                                                                                                                                                                                                   | ::: x:mt-2                                 |                       |
|                                                                                                                                                                                                                                                                                                                   | The ids of the nodes to get the data from. |                       |
|                                                                                                                                                                                                                                                                                                                   | :::                                        |                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------+-----------------------+

**Returns:**

[](#returns2)`Pick<`[`NodeType`](/api-reference/types/node)`, "id" | "type" | "data">[]`

An object (or array of object) with `id`, `type`, `data` representing each node.

## TypeScript[](#typescript) 

This hook accepts a generic type argument of custom node types. See this [section in our TypeScript guide](/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

``` 
const nodesData = useNodesData<NodesType>(['nodeId-1', 'nodeId-2']);
```