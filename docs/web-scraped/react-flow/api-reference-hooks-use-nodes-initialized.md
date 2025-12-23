# Source: https://reactflow.dev/api-reference/hooks/use-nodes-initialized

# useNodesInitialized() 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useNodesInitialized.ts)

This hook tells you whether all the nodes in a flow have been measured and given a width and height. When you add a node to the flow, this hook will return `false` and then `true` again once the node has been measured.

``` 
import  from '@xyflow/react';
import  from 'react';
 
const options = ;
 
export default function useLayout()  = useReactFlow();
  const nodesInitialized = useNodesInitialized(options);
  const [layoutedNodes, setLayoutedNodes] = useState(getNodes());
 
  useEffect(() => 
  }, [nodesInitialized]);
 
  return layoutedNodes;
}
```

## Signature[](#signature) 

**Parameters:**

  Name                                                                                                                                                                                                                                                                                                                                                                              Type                                Default
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------- ------------------------------------------------------------------------
  [](#optionsincludehiddennodes)`options.includeHiddenNodes`   `boolean`   `false`

**Returns:**

[](#returns)`boolean`

Whether or not the nodes have been initialized by the `<ReactFlow />` component and given a width and height.

## Notes[](#notes) 

- This hook always returns `false` if the internal nodes array is empty.