# Source: https://reactflow.dev/learn/troubleshooting/migrate-to-v10

# Migrate to React Flow v10 

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

You can find the docs for old versions of React Flow here: [v11 ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://v11.reactflow.dev), [v10 ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://v10.reactflow.dev), [v9 ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://v9.reactflow.dev)

Welcome to React Flow v10! With the major version update, there are coming many new features but also some breaking changes.

## New Features[](#new-features) 

- [**Sub Flows**](/learn/layouting/sub-flows): You can now add nodes to a parent node and create groups and nested flows
- **Node Type 'group'**: A new node type without handles that can be used as a group node
- **Touch Device Support**: It is now possible to connect nodes on touch devices
- **Fit View on Init**: You can use the new `fitView` prop to fit the initial view
- **Key Handling**: Not only single keys but also multiple keys and key combinations are possible now
- [**useKeyPress hook**](/api-reference/hooks/use-key-press): A util hook for handling keyboard events
- [**useReactFlow hook**](/api-reference/hooks/use-react-flow): Returns a React Flow instance that exposes functions to manipulate the flow
- **[useNodes](/api-reference/hooks/use-nodes), [useEdges](/api-reference/hooks/use-edges) and [useViewport](/api-reference/hooks/use-viewport) hooks**: Hooks for receiving nodes, edges and the viewport
- **Edge Marker**: More options to configure the start and end markers of an edge

## Breaking Changes[](#breaking-changes) 

TLDR:

- Split the `elements` array into `nodes` and `edges` arrays and implement `onNodesChange` and `onEdgesChange` handlers (detailed guide in the [core concepts section](/learn/concepts/core-concepts))
- Memoize your custom `nodeTypes` and `edgeTypes`
- Rename `onLoad` to `onInit`
- Rename `paneMoveable` to `panOnDrag`
- Rename `useZoomPanHelper` to `useReactFlow` (and `setTransform` to `setViewport`)
- Rename node and edge option `isHidden` to `hidden`

Detailed explanation of breaking changes:

### 1. ~~Elements~~ - Nodes and Edges[](#1-elements---nodes-and-edges) 

We saw that a lot of people struggle with the semi controlled `elements` prop. It was always a bit messy to sync the local user state with the internal state of React Flow. Some of you used the internal store that was never documented and always a kind of hacky solution. For the new version we offer two ways to use React Flow - uncontrolled and controlled.

### 1.1. Controlled `nodes` and `edges`[](#11-controlled-nodes-and-edges) 

If you want to have the full control and use nodes and edges from your local state or your store, you can use the `nodes`, `edges` props in combination with the `onNodesChange` and `onEdgesChange` handlers. You need to implement these handlers for an interactive flow (if you are fine with just pan and zoom you don't need them). You'll receive a change when a node(s) gets initialized, dragged, selected or removed. This means that you always know the exact position and dimensions of a node or if it's selected for example. We export the helper functions `applyNodeChanges` and `applyEdgeChanges` that you should use to apply the changes.

#### Old API[](#old-api) 

``` 
import  from 'react';
import  from 'react-flow-renderer';
 
const initialElements = [
  , position:  },
  , position:  },
  ,
];
 
const BasicFlow = () => 
      onElementsRemove=
      onConnect=
    />
  );
};
 
export default BasicFlow;
```

#### New API[](#new-api) 

``` 
import  from 'react';
import  from 'react-flow-renderer';
 
const initialNodes = [
  , position:  },
  , position:  },
];
 
const initialEdges = [];
 
const BasicFlow = () => 
      edges=
      onNodesChange=
      onEdgesChange=
      onConnect=
    />
  );
};
 
export default BasicFlow;
```

You can also use the new hooks `useNodesState` and `useEdgesState` for a quick start:

``` 
const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
```

related changes:

- `onElementsClick` -\>`onNodeClick` and `onEdgeClick`
- `onElementsRemove` -\> replaced by the `onNodesChange` and `onEdgesChange` handler

### 1.2 Uncontrolled `defaultNodes` and `defaultEdges`[](#12-uncontrolled-defaultnodes-and-defaultedges) 

The easiest way to get started is to use the `defaultNodes` and `defaultEdges` props. When you set these props, all actions are handled internally. You don't need to add any other handlers to get a fully interactive flow with the ability to drag nodes, connect nodes and remove nodes and edges:

#### New API[](#new-api-1) 

``` 
import ReactFlow from 'react-flow-renderer';
 
const defaultNodes = [
  , position:  },
  , position:  },
];
 
const defaultEdges = [];
 
const BasicFlow = () =>  defaultEdges= />;
};
 
export default BasicFlow;
```

If you want to add, remove or update a node or edge you can only do this by using the [ReactFlow instance](/api-reference/types/react-flow-instance) that you can receive either with the new `useReactFlow` hook or by using the `onInit` handler that gets the instance as a function param.

### 2. Memoize your custom `nodeTypes` and `edgeTypes`[](#2-memoize-your-custom-nodetypes-and-edgetypes) 

Whenever you pass new node or edge types, we create wrapped node or edge component types in the background. This means that you should not create a new `nodeType` or `edgeType` object on every render. **Memoize your nodeTypes and edgeTypes or define them outside of the component when they don't change**.

**Don't do this:**

This creates a new object on every render and leads to bugs and performance issues:

``` 
// this is bad! Don't do it.
<ReactFlow
  nodes=
  nodeTypes=}
/>
```

**Do this:**

``` 
function Flow() ), []);
 
  return <ReactFlow nodes= nodeTypes= />;
}
```

or create the types outside of the component when they don't change:

``` 
const nodeTypes = ;
 
function Flow()  nodeTypes= />;
}
```

### 3. ~~Redux~~ - Zustand[](#3-redux--zustand) 

We switched our state management library from Redux to [Zustand ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/pmndrs/zustand). With this change we could remove about 300LOC from our state related code. If you need to access the internal store, you can use the [`useStore` hook](/api-reference/hooks/use-store):

#### Old API[](#old-api-1) 

``` 
import  from 'react-flow-renderer';
 
...
 
const transform = useStoreState((store) => store.transform);
```

#### New API[](#new-api-2) 

``` 
import  from 'react-flow-renderer';
 
...
const transform = useStore((store) => store.transform);
```

You still need to wrap your component with the `<ReactFlowProvider />` if you want to access the internal store.

We are also exporting `useStoreApi` if you need to get the store in an event handler for example without triggering re-renders.

``` 
import  from 'react-flow-renderer';
 
...
 
const store = useStoreApi();
 
...
// in an event handler
const [x, y, zoom] = store.getState().transform;
```

### 4. ~~onLoad~~ - onInit[](#4-onload---oninit) 

The `onLoad` callback has been renamed to `onInit` and now fires when the nodes are initialized.

#### Old API[](#old-api-2) 

``` 
const onLoad = (reactFlowInstance: OnLoadParams) => reactFlowInstance.zoomTo(2);
...
<ReactFlow
   ...
  onLoad=
/>
```

#### New API[](#new-api-3) 

``` 
const onInit = (reactFlowInstance: ReactFlowInstance) => reactFlowInstance.zoomTo(2);
...
<ReactFlow
   ...
  onInit=
/>
```

### 5. ~~paneMoveable~~ - panOnDrag[](#5-panemoveable---panondrag) 

This is more consistent with the rest of the API (`panOnScroll`, `zoomOnScroll`, etc.)

#### Old API[](#old-api-3) 

``` 
<ReactFlow
   ...
  paneMoveable=
/>
```

#### New API[](#new-api-4) 

``` 
<ReactFlow
   ...
  panOnDrag=
/>
```

### 6. ~~useZoomPanHelper transform~~ - unified in `useReactFlow`[](#6-usezoompanhelper-transform---unified-in-usereactflow) 

As "transform" is also the variable name of the transform in the store and it's not clear that `transform` is a setter we renamed it to `setViewport`. This is also more consistent with the other functions. Also, all `useZoomPanHelper` functions have been moved to the [React Flow instance](/api-reference/types/react-flow-instance) that you get from the [`useReactFlow` hook](/api-reference/hooks/use-react-flow) or the `onInit` handler.

#### Old API[](#old-api-4) 

``` 
const  = useZoomPanHelper();
...
transform();
```

#### New API[](#new-api-5) 

``` 
const  = useReactFlow();
...
setViewport();
```

New viewport functions:

- `getZoom`
- `getViewport`

### 7. ~~isHidden~~ - hidden[](#7-ishidden---hidden) 

We mixed prefixed (`is...`) and non-prefixed boolean option names. All node and edge options are not prefixed anymore. So it's `hidden`, `animated`, `selected`, `draggable`, `selectable` and `connectable`.

#### Old API[](#old-api-5) 

``` 
const hiddenNode =  };
```

#### New API[](#new-api-6) 

``` 
const hiddenNode =  };
```

### 8. ~~arrowHeadType~~ ~~markerEndId~~ - markerStart / markerEnd[](#8-arrowheadtype-markerendid---markerstart--markerend) 

We improved the API for customizing the markers for an edge. With the new API you are able to set individual markers at the start and the end of an edge as well as customizing them with colors, strokeWidth etc. You still have the ability to set a markerEndId but instead of using different properties, the `markerStart` and `markerEnd` property accepts either a string (id for the svg marker that you need to define yourself) or a configuration object for using the built in arrowClosed or arrow markers.

#### Old API[](#old-api-6) 

``` 
const markerEdge = ;
```

#### New API[](#new-api-7) 

``` 
const markerEdge = ,
};
```

### 9. ~~ArrowHeadType~~ - MarkerType[](#9-arrowheadtype---markertype) 

This is just a wording change for making the marker API more consistent. As we are now able to set markers for the start of the edge, the name type ArrowHeadType has been renamed to MarkerType. In the future, this can also not only contain arrow shapes but others like circles, diamonds etc.

### 10. Attribution[](#10-attribution) 

This is not really a breaking change to the API but a little change in the general appearance of React Flow. We added a tiny "React Flow" attribution to the bottom right (the position is configurable via the `attributionPosition` prop). This change comes with the new "React Flow Pro" subscription model. If you want to remove the attribution in a commercial application, please subscribe to ["React Flow Pro"](/pro).