# Source: https://reactflow.dev/learn/advanced-use/typescript

# Usage with TypeScript 

React Flow is written in TypeScript because we value the additional safety barrier it provides. We export all the types you need for correctly typing data structures and functions you pass to the React Flow component. We also provide a way to extend the types of nodes and edges.

## Basic usage[](#basic-usage) 

Let's start with the most basic types you need for a simple starting point. Typescript might already infer some of these types, but we will define them explicitly nonetheless.

``` 
import  from 'react';
import  from '@xyflow/react';
 
const initialNodes: Node[] = [
  , position:  },
  , position:  },
];
 
const initialEdges: Edge[] = [];
 
const fitViewOptions: FitViewOptions = ;
 
const defaultEdgeOptions: DefaultEdgeOptions = ;
 
const onNodeDrag: OnNodeDrag = (_, node) => ;
 
function Flow() 
      edges=
      onNodesChange=
      onEdgesChange=
      onConnect=
      onNodeDrag=
      fitView
      fitViewOptions=
      defaultEdgeOptions=
    />
  );
}
```

### Custom nodes[](#custom-nodes) 

When working with [custom nodes](/learn/customization/custom-nodes) you have the possibility to pass a custom `Node` type (or your `Node` union) to the `NodeProps` type. There are basically two ways to work with custom nodes:

1.  If you have **multiple custom nodes**, you want to pass a specific `Node` type as a generic to the `NodeProps` type:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[NumberNode.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import type  from '@xyflow/react';
 
type NumberNode = Node<, 'number'>;
 
export default function NumberNode(: NodeProps<NumberNode>) </div>;
}
```

⚠️ If you specify the node data separately, you need to use `type` (an `interface` would not work here):

``` 
type NumberNodeData = ;
type NumberNode = Node<NumberNodeData, 'number'>;
```

2.  If you have **one custom node** that renders different content based on the node type, you want to pass your `Node` union type as a generic to `NodeProps`:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[CustomNode.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import type  from '@xyflow/react';
 
type NumberNode = Node<, 'number'>;
type TextNode = Node<, 'text'>;
 
type AppNode = NumberNode | TextNode;
 
export default function CustomNode(: NodeProps<AppNode>) </div>;
  }
 
  return <div>A special text: </div>;
}
```

### Custom edges[](#custom-edges) 

For [custom edges](/learn/customization/custom-nodes) you have the same possibility as for custom nodes.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[CustomEdge.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from '@xyflow/react';
 
type CustomEdge = Edge<, 'custom'>;
 
export default function CustomEdge(: EdgeProps<CustomEdge>) );
 
  return <BaseEdge id= path= />;
}
```

## Advanced usage[](#advanced-usage) 

When creating complex applications with React Flow, you will have a number of custom nodes & edges, each with different kinds of data attached to them. When we operate on these nodes & edges through built in functions and hooks, we have to make sure that we [narrow down ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) the types of nodes & edges to prevent runtime errors.

### `Node` and `Edge` type unions[](#node-and-edge-type-unions) 

You will see many functions, callbacks and hooks (even the ReactFlow component itself) that expect a `NodeType` or `EdgeType` generic. These generics are simply [unions ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types) of all the different types of nodes & edges you have in your application. As long as you have typed the data objects correctly (see previous section), you can use their exported type.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

If you use any of the built-in nodes ('input', 'output', 'default') or edges ('straight', 'step', 'smoothstep', 'bezier'), you can add the `BuiltInNode` and `BuiltInEdge` types exported from `@xyflow/react` to your union type.

``` 
import type  from '@xyflow/react';
 
// Custom nodes
import NumberNode from './NumberNode';
import TextNode from './TextNode';
 
// Custom edge
import EditableEdge from './EditableEdge';
 
export type CustomNodeType = BuiltInNode | NumberNode | TextNode;
export type CustomEdgeType = BuiltInEdge | EditableEdge;
```

### Functions passed to `<ReactFlow />`[](#functions-passed-to-reactflow-) 

To receive correct types for callback functions, you can pass your union types to the `ReactFlow` component. By doing that you will have to type your callback functions explicitly.

``` 
import  from '@xyflow/react';
 
// ...
 
// Pass your union type here ...
const onNodeDrag: OnNodeDrag<CustomNodeType> = useCallback((_, node) => 
    console.log('drag event', node.data.number);
  }
}, []);
 
const onNodesChange: OnNodesChange<CustomNodeType> = useCallback(
  (changes) => setNodes((nds) => applyNodeChanges(changes, nds)),
  [setNodes],
);
```

### Hooks[](#hooks) 

The type unions can also be used to type the return values of many hooks.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[FlowComponent.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from '@xyflow/react';
 
export default function FlowComponent()  = useReactFlow<CustomNodeType, CustomEdgeType>();
 
  // You can type useStore by typing the selector function
  const nodes = useStore((s: ReactFlowState<CustomNodeType>) => s.nodes);
 
  const connections = useNodeConnections();
 
  const nodesData = useNodesData<CustomNodeType>(connections?.[0].source);
 
  nodeData.forEach(() => 
  });
  // ...
}
```

### Type guards[](#type-guards) 

There are multiple ways you can define [type guards ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#typeof-type-guards) in Typescript. One way is to define type guard functions like `isNumberNode` or `isTextNode` to filter out specific nodes from a list of nodes.

``` 
function isNumberNode(node: CustomNodeType): node is NumberNode 
 
// numberNodes is of type NumberNode[]
const numberNodes = nodes.filter(isNumberNode);
```