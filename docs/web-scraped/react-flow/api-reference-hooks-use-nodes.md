# Source: https://reactflow.dev/api-reference/hooks/use-nodes

# useNodes() 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useNodes.ts)

This hook returns an array of the current nodes. Components that use this hook will re-render **whenever any node changes**, including when a node is selected or moved.

``` 
import  from '@xyflow/react';
 
export default function ()  nodes!</div>;
}
```

## Signature[](#signature) 

**Parameters:**

This function does not accept any parameters.

**Returns:**

[](#returns)[`NodeType`](/api-reference/types/node)`[]`

An array of all nodes currently in the flow.

## TypeScript[](#typescript) 

This hook accepts a generic type argument of custom node types. See this [section in our TypeScript guide](/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

``` 
const nodes = useNodes<CustomNodeType>();
```

## Notes[](#notes) 

- Relying on `useNodes` unnecessarily can be a common cause of performance issues. Whenever any node changes, this hook will cause the component to re-render. Often we actually care about something more specific, like when the *number* of nodes changes: where possible try to use [`useStore`](/api-reference/hooks/use-store) instead.