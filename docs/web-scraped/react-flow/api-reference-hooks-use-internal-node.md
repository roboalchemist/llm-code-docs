# Source: https://reactflow.dev/api-reference/hooks/use-internal-node

# useInternalNode() 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useInternalNode.ts)

This hook returns the internal representation of a specific node. Components that use this hook will re-render **whenever any node changes**, including when a node is selected or moved.

``` 
import  from '@xyflow/react';
 
export default function () </p>
      <p>y: </p>
    </div>
  );
}
```

## Signature[](#signature) 

**Parameters:**

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+-----------------------+
| Name                                                                                                                                                                                                                                                                                                    | Type                                  | Default               |
+=========================================================================================================================================================================================================================================================================================================+=======================================+=======================+
| [](#id)`id` | `string`      |                       |
|                                                                                                                                                                                                                                                                                                         |                                       |                       |
|                                                                                                                                                                                                                                                                                                         | ::: x:mt-2                            |                       |
|                                                                                                                                                                                                                                                                                                         | The ID of a node you want to observe. |                       |
|                                                                                                                                                                                                                                                                                                         | :::                                   |                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+-----------------------+

**Returns:**

[](#returns)[`InternalNode`](/api-reference/types/internal-node)`<`[`NodeType`](/api-reference/types/node)`> | undefined`

The `InternalNode` object for the node with the given ID.

## TypeScript[](#typescript) 

This hook accepts a generic type argument of custom node types. See this [section in our TypeScript guide](/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

``` 
const internalNode = useInternalNode<CustomNodeType>();
```