# Source: https://reactflow.dev/api-reference/hooks/use-react-flow

# useReactFlow() 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useReactFlow.ts)

This hook returns a [`ReactFlowInstance`](/api-reference/types/react-flow-instance) that can be used to update nodes and edges, manipulate the viewport, or query the current state of the flow.

``` 
import  from 'react';
import  from '@xyflow/react';
 
export function NodeCounter() , [reactFlow]);
 
  return (
    <div>
      <button onClick=>Update count</button>
      <p>There are  nodes in the flow.</p>
    </div>
  );
}
```

## Signature[](#signature) 

**Parameters:**

This function does not accept any parameters.

**Returns:**

[](#returns)[`ReactFlowInstance`](/api-reference/types/react-flow-instance)`<`[`NodeType`](/api-reference/types/node)`, `[`EdgeType`](/api-reference/types/edge)`>`

## TypeScript[](#typescript) 

This hook accepts a generic type argument of custom node & edge types. See this [section in our TypeScript guide](/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

``` 
const reactFlow = useReactFlow<CustomNodeType, CustomEdgeType>();
```

## Notes[](#notes) 

- This hook can only be used in a component that is a child of a [`<ReactFlowProvider />`](/api-reference/react-flow-provider) or a [`<ReactFlow />`](/api-reference/react-flow) component.
- Unlike [`useNodes`](/api-reference/hooks/use-nodes) or [`useEdges`](/api-reference/hooks/use-edges), this hook won't cause your component to re-render when state changes. Instead, you can query the state when you need it by using methods on the [`ReactFlowInstance`](/api-reference/types/react-flow-instance) this hook returns.