# Source: https://reactflow.dev/api-reference/hooks/use-update-node-internals

# useUpdateNodeInternals() 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useUpdateNodeInternals.ts)

When you programmatically add or remove handles to a node or update a node's handle position, you need to let React Flow know about it using this hook. This will update the internal dimensions of the node and properly reposition handles on the canvas if necessary.

``` 
import  from 'react';
import  from '@xyflow/react';
 
export default function RandomHandleNode() , [id, updateNodeInternals]);
 
  return (
    <>
      ).map((_, index) => (
        <Handle
          key=
          type="target"
          position="left"
          id=`}
        />
      ))}
 
      <div>
        <button onClick=>Randomize handle count</button>
        <p>There are  handles on this node.</p>
      </div>
    </>
  );
}
```

## Signature[](#signature) 

**Parameters:**

This function does not accept any parameters.

**Returns:**

[](#returns)`UpdateNodeInternals`

Use this function to tell React Flow to update the internal state of one or more nodes that you have changed programmatically.

## Notes[](#notes) 

- This hook can only be used in a component that is a child of a [`<ReactFlowProvider />`](/api-reference/react-flow-provider) or a [`<ReactFlow />`](/api-reference/react-flow) component.