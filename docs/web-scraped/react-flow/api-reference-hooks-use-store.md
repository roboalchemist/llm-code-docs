# Source: https://reactflow.dev/api-reference/hooks/use-store

# useStore() 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useStore.ts)

This hook can be used to subscribe to internal state changes of the React Flow component. The `useStore` hook is re-exported from the [Zustand ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/pmndrs/zustand) state management library, so you should check out their docs for more details.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

This hook should only be used if there is no other way to access the internal state. For many of the common use cases, there are dedicated hooks available such as [`useReactFlow`](/api-reference/hooks/use-react-flow), [`useViewport`](/api-reference/hooks/use-viewport), etc.

``` 
import  from '@xyflow/react';
 
const nodesLengthSelector = (state) =>
  state.nodes.length || 0;
 
const NodesLengthDisplay = () => </div>;
};
 
function Flow() >
      <NodesLengthDisplay />
    </ReactFlow>
  );
}
```

This example computes the number of nodes eagerly. Whenever the number of nodes in the flow changes, the `<NodesLengthDisplay />` component will re-render. This is in contrast to the example in the [`useStoreApi`](/api-reference/hooks/use-store-api) hook that only computes the number of nodes when a button is clicked.

Choosing whether to calculate values on-demand or to subscribe to changes as they happen is a bit of a balancing act. On the one hand, putting too many heavy calculations in an event handler can make your app feel sluggish or unresponsive. On the other hand, computing values eagerly can lead to slow or unnecessary re-renders.

We make both this hook and [`useStoreApi`](/api-reference/hooks/use-store-api) available so that you can choose the approach that works best for your use-case.

## Signature[](#signature) 

**Parameters:**

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| Name                                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                     | Default               |
+==================================================================================================================================================================================================================================================================================================================================================+==========================================================================================================================================================================================================================================================================================+=======================+
| [](#selector)`selector`                              | `(state: ReactFlowState) => StateSlice`                                                                                                                                                                                                                          |                       |
|                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                          |                       |
|                                                                                                                                                                                                                                                                                                                                                  | ::: x:mt-2                                                                                                                                                                                                                                                                               |                       |
|                                                                                                                                                                                                                                                                                                                                                  | A selector function that returns a slice of the flow's internal state. Extracting or transforming just the state you need is a good practice to avoid unnecessary re-renders.                                                                                                            |                       |
|                                                                                                                                                                                                                                                                                                                                                  | :::                                                                                                                                                                                                                                                                                      |                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| [](#equalityfn)`equalityFn` | `(a: StateSlice, b: StateSlice) => boolean`                                                                                                                                                                                                                      |                       |
|                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                          |                       |
|                                                                                                                                                                                                                                                                                                                                                  | ::: x:mt-2                                                                                                                                                                                                                                                                               |                       |
|                                                                                                                                                                                                                                                                                                                                                  | A function to compare the previous and next value. This is incredibly useful for preventing unnecessary re-renders. Good sensible defaults are using `Object.is` or importing `zustand/shallow`, but you can be as granular as you like. |                       |
|                                                                                                                                                                                                                                                                                                                                                  | :::                                                                                                                                                                                                                                                                                      |                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+

**Returns:**

[](#returns)`StateSlice`

The selected state slice.

## Examples[](#examples) 

### Triggering store actions[](#triggering-store-actions) 

You can manipulate the internal React Flow state by triggering internal actions through the `useStore` hook. These actions are already used internally throughout the library, but you can also use them to implement custom functionality.

``` 
import  from '@xyflow/react';
 
const setMinZoomSelector = (state) => state.setMinZoom;
 
function MinZoomSetter() >set min zoom</button>;
}
```

## TypeScript[](#typescript) 

This hook can be typed by typing the selector function. See this [section in our TypeScript guide](/learn/advanced-use/typescript#nodetype-edgetype-unions) for more information.

``` 
const nodes = useStore((s: ReactFlowState<CustomNodeType>) => s.nodes);
```