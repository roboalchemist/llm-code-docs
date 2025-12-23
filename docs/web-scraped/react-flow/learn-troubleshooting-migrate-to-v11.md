# Source: https://reactflow.dev/learn/troubleshooting/migrate-to-v11

# Migrate to React Flow v11 

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

You can find the docs for old versions of React Flow here: [v11 ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://v11.reactflow.dev), [v10 ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://v10.reactflow.dev), [v9 ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://v9.reactflow.dev)

A lot changed in v11 but this time we've tried to keep the breaking changes small. The biggest change is the new package name `reactflow` and the new repo structure. React Flow is now managed as a monorepo and separated into multiple packages that can be installed separately. In addition to that, there are some API changes and new APIs introduced in v11. This guide explains the changes in detail and helps you to migrate from v10 to v11.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik04IDEuNWMtMi4zNjMgMC00IDEuNjktNCAzLjc1IDAgLjk4NC40MjQgMS42MjUuOTg0IDIuMzA0bC4yMTQuMjUzYy4yMjMuMjY0LjQ3LjU1Ni42NzMuODQ4LjI4NC40MTEuNTM3Ljg5Ni42MjEgMS40OWEuNzUuNzUgMCAwIDEtMS40ODQuMjExYy0uMDQtLjI4Mi0uMTYzLS41NDctLjM3LS44NDdhOC40NTYgOC40NTYgMCAwIDAtLjU0Mi0uNjhjLS4wODQtLjEtLjE3My0uMjA1LS4yNjgtLjMyQzMuMjAxIDcuNzUgMi41IDYuNzY2IDIuNSA1LjI1IDIuNSAyLjMxIDQuODYzIDAgOCAwczUuNSAyLjMxIDUuNSA1LjI1YzAgMS41MTYtLjcwMSAyLjUtMS4zMjggMy4yNTktLjA5NS4xMTUtLjE4NC4yMi0uMjY4LjMxOS0uMjA3LjI0NS0uMzgzLjQ1My0uNTQxLjY4MS0uMjA4LjMtLjMzLjU2NS0uMzcuODQ3YS43NTEuNzUxIDAgMCAxLTEuNDg1LS4yMTJjLjA4NC0uNTkzLjMzNy0xLjA3OC42MjEtMS40ODkuMjAzLS4yOTIuNDUtLjU4NC42NzMtLjg0OC4wNzUtLjA4OC4xNDctLjE3My4yMTMtLjI1My41NjEtLjY3OS45ODUtMS4zMi45ODUtMi4zMDQgMC0yLjA2LTEuNjM3LTMuNzUtNC0zLjc1Wk01Ljc1IDEyaDQuNWEuNzUuNzUgMCAwIDEgMCAxLjVoLTQuNWEuNzUuNzUgMCAwIDEgMC0xLjVaTTYgMTUuMjVhLjc1Ljc1IDAgMCAxIC43NS0uNzVoMi41YS43NS43NSAwIDAgMSAwIDEuNWgtMi41YS43NS43NSAwIDAgMS0uNzUtLjc1WiIgLz48L3N2Zz4=)

React Flow 11 only works with **React 17** or greater

## New Features[](#new-features) 

- **Better [Accessibility](/learn/advanced-use/accessibility)**
  - Nodes and edges are focusable, selectable, moveable and deletable with the keyboard.
  - `aria-` default attributes for all elements and controllable via `ariaLabel` options
  - Keyboard controls can be disabled with the new `disableKeyboardA11y` prop
- **Better selectable edges** via new edge option: `interactionWidth` - renders invisible edge that makes it easier to interact
- **Better routing for smoothstep and step edges**: [https://twitter.com/reactflowdev/status/1567535405284614145 ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://twitter.com/reactflowdev/status/1567535405284614145)
- **Nicer edge updating behavior**: [https://twitter.com/reactflowdev/status/1564966917517021184 ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://twitter.com/reactflowdev/status/1564966917517021184)
- **Node origin**: The new `nodeOrigin` prop lets you control the origin of a node. Useful for layouting.
- **New background pattern**: `BackgroundVariant.Cross` variant
- **[`useOnViewportChange`](/api-reference/hooks/use-on-viewport-change) hook** - handle viewport changes within a component
- **[`use-on-selection-change`](/api-reference/hooks/use-on-selection-change) hook** - handle selection changes within a component
- **[`useNodesInitialized`](/api-reference/hooks/use-nodes-initialized) hook** - returns true if all nodes are initialized and if there is more than one node
- **Deletable option** for Nodes and edges
- **New Event handlers**: `onPaneMouseEnter`, `onPaneMouseMove` and `onPaneMouseLeave`
- **Edge `pathOptions`** for `smoothstep` and `default` edges
- **Nicer cursor defaults**: Cursor is grabbing, while dragging a node or panning
- **Pane moveable** with middle mouse button
- **Pan over nodes** when they are not draggable (`draggable=false` or `nodesDraggable` false)
  - you can disable this behavior by adding the class name `nopan` to a wrapper of a custom node
- **[`<BaseEdge />`](/api-reference/components/base-edge) component** that makes it easier to build custom edges
- **[Separately installable packages](/learn/concepts/built-in-components)**
  - \@reactflow/core
  - \@reactflow/background
  - \@reactflow/controls
  - \@reactflow/minimap

## Breaking Changes[](#breaking-changes) 

### 1. New npm package name[](#1-new-npm-package-name) 

The package `react-flow-renderer` has been renamed to `reactflow`.

#### Old API[](#old-api) 

``` 
// npm install react-flow-renderer
import ReactFlow from 'react-flow-renderer';
```

#### New API[](#new-api) 

``` 
// npm install reactflow
import  from '@xyflow/react';
```

### 2. Importing CSS is mandatory[](#2-importing-css-is-mandatory) 

We are not injecting CSS anymore. **React Flow won't work if you are not loading the styles!**

``` 
// default styling
import '@xyflow/react/dist/style.css';
 
// or if you just want basic styles
import '@xyflow/react/dist/base.css';
```

#### 2.1. Removal of the nocss entrypoint[](#21-removal-of-the-nocss-entrypoint) 

This change also means that there is no `react-flow-renderer/nocss` entry point anymore. If you used that, you need to adjust the CSS entry points as mentioned above.

### 3. `defaultPosition` and `defaultZoom` have been merged to `defaultViewport`[](#3-defaultposition-and-defaultzoom-have-been-merged-to-defaultviewport) 

#### Old API[](#old-api-1) 

``` 
import ReactFlow from 'react-flow-renderer';
 
const Flow = () =>  defaultZoom= />;
};
 
export default Flow;
```

#### New API[](#new-api-1) 

``` 
import  from '@xyflow/react';
 
const defaultViewport: Viewport = ;
 
const Flow = () =>  />;
};
 
export default Flow;
```

### 4. Removal of `getBezierEdgeCenter`, `getSimpleBezierEdgeCenter` and `getEdgeCenter`[](#4-removal-of-getbezieredgecenter-getsimplebezieredgecenter-and-getedgecenter) 

In v10 we had `getBezierEdgeCenter`, `getSimpleBezierEdgeCenter` and `getEdgeCenter` for getting the center of a certain edge type. In v11 we changed the helper function for creating the path, so that it also returns the center / label position of an edge.

Let's say you want to get the path and the center / label position of a bezier edge:

#### Old API[](#old-api-2) 

``` 
import  from 'react-flow-renderer';
 
const path = getBezierPath(edgeParams);
const [centerX, centerY] = getBezierEdgeCenter(params);
```

#### New API[](#new-api-2) 

``` 
import  from '@xyflow/react';
 
const [path, labelX, labelY] = getBezierPath(edgeParams);
```

We avoid to call it `centerX` and `centerY` anymore, because it's actually the label position and not always the center for every edge type.

### 5. Removal of `onClickConnectStop` and `onConnectStop`[](#5-removal-of-onclickconnectstop-and-onconnectstop) 

#### Old API[](#old-api-3) 

``` 
import ReactFlow from 'react-flow-renderer';
 
const Flow = () => 
      defaultEdges=
      onConnectStop=
      onClickConnectStop=
    />
  );
};
 
export default Flow;
```

#### New API[](#new-api-3) 

``` 
import  from '@xyflow/react';
 
const Flow = () => 
      defaultEdges=
      onConnectEnd=
      onClickConnectEnd=
    />
  );
};
 
export default Flow;
```

### 6. Pan over nodes[](#6-pan-over-nodes) 

In the previous versions you couldn't pan over nodes even if they were not draggable. In v11, you can pan over nodes when `nodesDraggable=false` or node option `draggable=false`. If you want the old behavior back, you can add the class name `nopan` to the wrappers of your custom nodes.