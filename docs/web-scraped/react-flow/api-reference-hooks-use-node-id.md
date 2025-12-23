# Source: https://reactflow.dev/api-reference/hooks/use-node-id

# useNodeId() 

[Source on Github ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/v11/packages/core/src/contexts/NodeIdContext.ts/#L7)

You can use this hook to get the id of the node it is used inside. It is useful if you need the node's id deeper in the render tree but don't want to manually drill down the id as a prop.

``` 
import  from '@xyflow/react';
 
export default function CustomNode() 
 
function NodeIdDisplay() </span>;
}
```

## Signature[](#signature) 

**Parameters:**

This function does not accept any parameters.

**Returns:**

[](#returns)`string | null`

The id for a node in the flow.

## Notes[](#notes) 

- This hook should only be used within a custom node or its children.