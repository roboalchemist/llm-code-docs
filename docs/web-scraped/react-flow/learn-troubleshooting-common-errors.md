# Source: https://reactflow.dev/learn/troubleshooting/common-errors

# Common Errors 

This guide contains warnings and errors that can occur when using React Flow. We are also adding common questions and pitfalls that we collect from our [Discord Server ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://discord.gg/RVmnytFmGW), [Github Issues ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/issues) and [Github Discussions ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/discussions).

### Warning: Seems like you have not used zustand provider as an ancestor.[](#warning-seems-like-you-have-not-used-zustand-provider-as-an-ancestor) 

This usually happens when:

**A:** You have two different versions of \@reactflow/core installed.\
**B:** You are trying to access the internal React Flow state outside of the React Flow context.

#### Solution for A[](#solution-for-a) 

Update reactflow and \@reactflow/node-resizer (in case you are using it), remove node_modules and package-lock.json and reinstall the dependencies.

#### Solution for B[](#solution-for-b) 

A possible solution is to wrap your component with a [`<ReactFlowProvider />`](/api-reference/react-flow-provider) or move the code that is accessing the state inside a child of your React Flow instance.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik00LjQ3LjIyQS43NDkuNzQ5IDAgMCAxIDUgMGg2Yy4xOTkgMCAuMzg5LjA3OS41My4yMmw0LjI1IDQuMjVjLjE0MS4xNC4yMi4zMzEuMjIuNTN2NmEuNzQ5Ljc0OSAwIDAgMS0uMjIuNTNsLTQuMjUgNC4yNUEuNzQ5Ljc0OSAwIDAgMSAxMSAxNkg1YS43NDkuNzQ5IDAgMCAxLS41My0uMjJMLjIyIDExLjUzQS43NDkuNzQ5IDAgMCAxIDAgMTFWNWMwLS4xOTkuMDc5LS4zODkuMjItLjUzWm0uODQgMS4yOEwxLjUgNS4zMXY1LjM4bDMuODEgMy44MWg1LjM4bDMuODEtMy44MVY1LjMxTDEwLjY5IDEuNVpNOCA0YS43NS43NSAwIDAgMSAuNzUuNzV2My41YS43NS43NSAwIDAgMS0xLjUgMHYtMy41QS43NS43NSAwIDAgMSA4IDRabTAgOGExIDEgMCAxIDEgMC0yIDEgMSAwIDAgMSAwIDJaIiAvPjwvc3ZnPg==)

This will cause an error:

``` 
import  from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
function FlowWithoutProvider(props)  />;
}
 
export default FlowWithoutProvider;
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik00LjQ3LjIyQS43NDkuNzQ5IDAgMCAxIDUgMGg2Yy4xOTkgMCAuMzg5LjA3OS41My4yMmw0LjI1IDQuMjVjLjE0MS4xNC4yMi4zMzEuMjIuNTN2NmEuNzQ5Ljc0OSAwIDAgMS0uMjIuNTNsLTQuMjUgNC4yNUEuNzQ5Ljc0OSAwIDAgMSAxMSAxNkg1YS43NDkuNzQ5IDAgMCAxLS41My0uMjJMLjIyIDExLjUzQS43NDkuNzQ5IDAgMCAxIDAgMTFWNWMwLS4xOTkuMDc5LS4zODkuMjItLjUzWm0uODQgMS4yOEwxLjUgNS4zMXY1LjM4bDMuODEgMy44MWg1LjM4bDMuODEtMy44MVY1LjMxTDEwLjY5IDEuNVpNOCA0YS43NS43NSAwIDAgMSAuNzUuNzV2My41YS43NS43NSAwIDAgMS0xLjUgMHYtMy41QS43NS43NSAwIDAgMSA4IDRabTAgOGExIDEgMCAxIDEgMC0yIDEgMSAwIDAgMSAwIDJaIiAvPjwvc3ZnPg==)

This will cause an error, too:

``` 
import  from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
function Flow(props)  />
    </ReactFlowProvider>
  );
}
 
export default FlowWithProvider;
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

This works:

As soon as you want to access the internal state of React Flow (for example by using the `useReactFlow` hook), you need to wrap your component with a `<ReactFlowProvider />`. Here the wrapping is done outside of the component:

``` 
import  from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
function Flow(props)  />;
}
 
// wrapping with ReactFlowProvider is done outside of the component
function FlowWithProvider(props)  />
    </ReactFlowProvider>
  );
}
 
export default FlowWithProvider;
```

### It looks like you have created a new nodeTypes or edgeTypes object.[](#it-looks-like-you-have-created-a-new-nodetypes-or-edgetypes-object) 

If this wasn't on purpose please define the nodeTypes/edgeTypes outside of the component or memoize them.

This warning appears when the `nodeTypes` or `edgeTypes` properties change after the initial render. The `nodeTypes` or `edgeTypes` should only be changed dynamically in very rare cases. Usually, they are defined once, along with all the types you use in your application. It can happen easily that you are defining the nodeTypes or edgeTypes object inside of your component render function, which will cause React Flow to re-render every time your component re-renders.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik00LjQ3LjIyQS43NDkuNzQ5IDAgMCAxIDUgMGg2Yy4xOTkgMCAuMzg5LjA3OS41My4yMmw0LjI1IDQuMjVjLjE0MS4xNC4yMi4zMzEuMjIuNTN2NmEuNzQ5Ljc0OSAwIDAgMS0uMjIuNTNsLTQuMjUgNC4yNUEuNzQ5Ljc0OSAwIDAgMSAxMSAxNkg1YS43NDkuNzQ5IDAgMCAxLS41My0uMjJMLjIyIDExLjUzQS43NDkuNzQ5IDAgMCAxIDAgMTFWNWMwLS4xOTkuMDc5LS4zODkuMjItLjUzWm0uODQgMS4yOEwxLjUgNS4zMXY1LjM4bDMuODEgMy44MWg1LjM4bDMuODEtMy44MVY1LjMxTDEwLjY5IDEuNVpNOCA0YS43NS43NSAwIDAgMSAuNzUuNzV2My41YS43NS43NSAwIDAgMS0xLjUgMHYtMy41QS43NS43NSAwIDAgMSA4IDRabTAgOGExIDEgMCAxIDEgMC0yIDEgMSAwIDAgMSAwIDJaIiAvPjwvc3ZnPg==)

Causes a warning:

``` 
import  from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
import MyCustomNode from './MyCustomNode';
 
function Flow(props) ;
 
  return <ReactFlow nodeTypes= />;
}
 
export default Flow;
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

Recommended implementation:

``` 
import  from '@xyflow/react';
import MyCustomNode from './MyCustomNode';
 
// defined outside of the component
const nodeTypes = ;
 
function Flow(props)  />;
}
 
export default Flow;
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

Alternative implementation:

You can use this if you want to change your nodeTypes dynamically without causing unnecessary re-renders.

``` 
import  from 'react';
import  from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
import MyCustomNode from './MyCustomNode';
 
function Flow(props) ),
    [],
  );
 
  return <ReactFlow nodeTypes= />;
}
 
export default Flow;
```

### Node type not found. Using fallback type "default".[](#node-type-not-found-using-fallback-type-default) 

This usually happens when you specify a custom node type for one of your nodes but do not pass the correct nodeTypes property to React Flow. The string for the type option of your custom node needs to be exactly the same as the key of the nodeTypes object.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik00LjQ3LjIyQS43NDkuNzQ5IDAgMCAxIDUgMGg2Yy4xOTkgMCAuMzg5LjA3OS41My4yMmw0LjI1IDQuMjVjLjE0MS4xNC4yMi4zMzEuMjIuNTN2NmEuNzQ5Ljc0OSAwIDAgMS0uMjIuNTNsLTQuMjUgNC4yNUEuNzQ5Ljc0OSAwIDAgMSAxMSAxNkg1YS43NDkuNzQ5IDAgMCAxLS41My0uMjJMLjIyIDExLjUzQS43NDkuNzQ5IDAgMCAxIDAgMTFWNWMwLS4xOTkuMDc5LS4zODkuMjItLjUzWm0uODQgMS4yOEwxLjUgNS4zMXY1LjM4bDMuODEgMy44MWg1LjM4bDMuODEtMy44MVY1LjMxTDEwLjY5IDEuNVpNOCA0YS43NS43NSAwIDAgMSAuNzUuNzV2My41YS43NS43NSAwIDAgMS0xLjUgMHYtMy41QS43NS43NSAwIDAgMSA4IDRabTAgOGExIDEgMCAxIDEgMC0yIDEgMSAwIDAgMSAwIDJaIiAvPjwvc3ZnPg==)

Doesn't work:

``` 
import  from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
import MyCustomNode from './MyCustomNode';
 
const nodes = [
  ,
];
 
function Flow(props)  />;
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik00LjQ3LjIyQS43NDkuNzQ5IDAgMCAxIDUgMGg2Yy4xOTkgMCAuMzg5LjA3OS41My4yMmw0LjI1IDQuMjVjLjE0MS4xNC4yMi4zMzEuMjIuNTN2NmEuNzQ5Ljc0OSAwIDAgMS0uMjIuNTNsLTQuMjUgNC4yNUEuNzQ5Ljc0OSAwIDAgMSAxMSAxNkg1YS43NDkuNzQ5IDAgMCAxLS41My0uMjJMLjIyIDExLjUzQS43NDkuNzQ5IDAgMCAxIDAgMTFWNWMwLS4xOTkuMDc5LS4zODkuMjItLjUzWm0uODQgMS4yOEwxLjUgNS4zMXY1LjM4bDMuODEgMy44MWg1LjM4bDMuODEtMy44MVY1LjMxTDEwLjY5IDEuNVpNOCA0YS43NS43NSAwIDAgMSAuNzUuNzV2My41YS43NS43NSAwIDAgMS0xLjUgMHYtMy41QS43NS43NSAwIDAgMSA4IDRabTAgOGExIDEgMCAxIDEgMC0yIDEgMSAwIDAgMSAwIDJaIiAvPjwvc3ZnPg==)

Doesn't work either:

``` 
import  from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
import MyCustomNode from './MyCustomNode';
 
const nodes = [
  ,
];
 
const nodeTypes = ;
 
function Flow(props)  nodeTypes= />;
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

This does work:

``` 
import  from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
import MyCustomNode from './MyCustomNode';
 
const nodes = [
  ,
];
 
const nodeTypes = ;
 
function Flow(props)  nodeTypes= />;
}
```

### The React Flow parent container needs a width and a height to render the graph.[](#the-react-flow-parent-container-needs-a-width-and-a-height-to-render-the-graph) 

Under the hood, React Flow measures the parent DOM element to adjust the renderer. If you try to render React Flow in a regular div without a height, we cannot display the graph. If you encounter this warning, you need to make sure that your wrapper component has some CSS attached to it so that it gets a fixed height or inherits the height of its parent.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik00LjQ3LjIyQS43NDkuNzQ5IDAgMCAxIDUgMGg2Yy4xOTkgMCAuMzg5LjA3OS41My4yMmw0LjI1IDQuMjVjLjE0MS4xNC4yMi4zMzEuMjIuNTN2NmEuNzQ5Ljc0OSAwIDAgMS0uMjIuNTNsLTQuMjUgNC4yNUEuNzQ5Ljc0OSAwIDAgMSAxMSAxNkg1YS43NDkuNzQ5IDAgMCAxLS41My0uMjJMLjIyIDExLjUzQS43NDkuNzQ5IDAgMCAxIDAgMTFWNWMwLS4xOTkuMDc5LS4zODkuMjItLjUzWm0uODQgMS4yOEwxLjUgNS4zMXY1LjM4bDMuODEgMy44MWg1LjM4bDMuODEtMy44MVY1LjMxTDEwLjY5IDEuNVpNOCA0YS43NS43NSAwIDAgMSAuNzUuNzV2My41YS43NS43NSAwIDAgMS0xLjUgMHYtMy41QS43NS43NSAwIDAgMSA4IDRabTAgOGExIDEgMCAxIDEgMC0yIDEgMSAwIDAgMSAwIDJaIiAvPjwvc3ZnPg==)

This will cause the warning:

``` 
import  from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
function Flow(props)  />
    </div>
  );
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

Working example:

``` 
import  from '@xyflow/react';
 
function Flow(props) }>
      <ReactFlow  />
    </div>
  );
}
```

### Only child nodes can use a parent extent.[](#only-child-nodes-can-use-a-parent-extent) 

This warning appears when you are trying to add the `extent` option to a node that does not have a parent node. Depending on what you are trying to do, you can remove the `extent` option or specify a `parentNode`.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik00LjQ3LjIyQS43NDkuNzQ5IDAgMCAxIDUgMGg2Yy4xOTkgMCAuMzg5LjA3OS41My4yMmw0LjI1IDQuMjVjLjE0MS4xNC4yMi4zMzEuMjIuNTN2NmEuNzQ5Ljc0OSAwIDAgMS0uMjIuNTNsLTQuMjUgNC4yNUEuNzQ5Ljc0OSAwIDAgMSAxMSAxNkg1YS43NDkuNzQ5IDAgMCAxLS41My0uMjJMLjIyIDExLjUzQS43NDkuNzQ5IDAgMCAxIDAgMTFWNWMwLS4xOTkuMDc5LS4zODkuMjItLjUzWm0uODQgMS4yOEwxLjUgNS4zMXY1LjM4bDMuODEgMy44MWg1LjM4bDMuODEtMy44MVY1LjMxTDEwLjY5IDEuNVpNOCA0YS43NS43NSAwIDAgMSAuNzUuNzV2My41YS43NS43NSAwIDAgMS0xLjUgMHYtMy41QS43NS43NSAwIDAgMSA4IDRabTAgOGExIDEgMCAxIDEgMC0yIDEgMSAwIDAgMSAwIDJaIiAvPjwvc3ZnPg==)

Does show a warning:

``` 
import  from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
const nodes = [
  ,
];
 
function Flow(props)  />;
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

Warning resolved:

``` 
const nodes = [
  ,
];
 
function Flow(props)  />;
}
```

### Can't create edge. An edge needs a source and a target.[](#cant-create-edge-an-edge-needs-a-source-and-a-target) 

This happens when you do not pass a `source` and a `target` option to the edge object. Without the source and target, the edge cannot be rendered.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik00LjQ3LjIyQS43NDkuNzQ5IDAgMCAxIDUgMGg2Yy4xOTkgMCAuMzg5LjA3OS41My4yMmw0LjI1IDQuMjVjLjE0MS4xNC4yMi4zMzEuMjIuNTN2NmEuNzQ5Ljc0OSAwIDAgMS0uMjIuNTNsLTQuMjUgNC4yNUEuNzQ5Ljc0OSAwIDAgMSAxMSAxNkg1YS43NDkuNzQ5IDAgMCAxLS41My0uMjJMLjIyIDExLjUzQS43NDkuNzQ5IDAgMCAxIDAgMTFWNWMwLS4xOTkuMDc5LS4zODkuMjItLjUzWm0uODQgMS4yOEwxLjUgNS4zMXY1LjM4bDMuODEgMy44MWg1LjM4bDMuODEtMy44MVY1LjMxTDEwLjY5IDEuNVpNOCA0YS43NS43NSAwIDAgMSAuNzUuNzV2My41YS43NS43NSAwIDAgMS0xLjUgMHYtMy41QS43NS43NSAwIDAgMSA4IDRabTAgOGExIDEgMCAxIDEgMC0yIDEgMSAwIDAgMSAwIDJaIiAvPjwvc3ZnPg==)

Will show a warning:

``` 
import  from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
const nodes = [
  /* ... */
];
 
const edges = [
  ,
];
 
function Flow(props)  edges= />;
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

This works:

``` 
import  from '@xyflow/react';
 
const nodes = [
  /* ... */
];
 
const edges = [
  ,
];
 
function Flow(props)  edges= />;
}
```

### The old edge with id="some-id" does not exist.[](#the-old-edge-with-idsome-id-does-not-exist) 

This can happen when you are trying to [reconnect an edge](/examples/edges/reconnect-edge) but the edge you want to update is already removed from the state. This is a very rare case. Please see the [Reconnect Edge example](/examples/edges/reconnect-edge) for implementation details.

### Couldn't create edge for source/target handle id: "some-id"; edge id: "some-id".[](#couldnt-create-edge-for-sourcetarget-handle-id-some-id-edge-id-some-id) 

This can happen if you are working with multiple handles and a handle is not found by its `id` property or if you haven't [updated the node internals after adding or removing handles](/api-reference/hooks/use-update-node-internals) programmatically. Please see the [Custom Node Example](/examples/nodes/custom-node) for an example of working with multiple handles.

### Marker type doesn't exist.[](#marker-type-doesnt-exist) 

This warning occurs when you are trying to specify a marker type that is not built into React Flow. The existing marker types are documented [here](/api-reference/types/edge#edgemarker).

### Handle: No node id found.[](#handle-no-node-id-found) 

This warning occurs when you try to use a `<Handle />` component outside of a custom node component.

### I get an error when building my app with webpack 4.[](#i-get-an-error-when-building-my-app-with-webpack-4) 

If you're using webpack 4, you'll likely run into an error like this:

``` 
ERROR in /node_modules/@reactflow/core/dist/esm/index.js 16:19
Module parse failed: Unexpected token (16:19)
You may need an appropriate loader to handle this file type, currently no loaders are configured to process this file. See https://webpack.js.org/concepts#loaders
```

React Flow is a modern JavaScript code base and makes use of lots of newer JavaScript features. By default, webpack 4 does not transpile your code and it doesn't know how to handle React Flow.

You need to add a number of babel plugins to your webpack config to make it work:

npm

pnpm

yarn

bun

``` 
npm i --save-dev babel-loader@8.2.5 @babel/preset-env @babel/preset-react @babel/plugin-proposal-optional-chaining @babel/plugin-proposal-nullish-coalescing-operator
```

``` 
pnpm add --save-dev babel-loader@8.2.5 @babel/preset-env @babel/preset-react @babel/plugin-proposal-optional-chaining @babel/plugin-proposal-nullish-coalescing-operator
```

``` 
yarn add --dev babel-loader@8.2.5 @babel/preset-env @babel/preset-react @babel/plugin-proposal-optional-chaining @babel/plugin-proposal-nullish-coalescing-operator
```

``` 
bun add --dev babel-loader@8.2.5 @babel/preset-env @babel/preset-react @babel/plugin-proposal-optional-chaining @babel/plugin-proposal-nullish-coalescing-operator
```

and configure the loader like this:

``` 

  }
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

If you're using webpack 5, you don't need to do anything! React Flow will work out of the box.

### Mouse events aren't working consistently when my nodes contain a `<canvas />` element.[](#mouse-events-arent-working-consistently-when-my-nodes-contain-a-canvas--element) 

If you're using a `<canvas />` element inside your custom node, you might run into problems with seemingly incorrect coordinates in mouse events from the canvas.

React Flow uses CSS transforms to scale nodes as you zoom in and out. However, from the DOM's perspective, the element is still the same size. This can cause problems if you have event listeners that want to calculate the mouse position relative to the canvas element.

To remedy this in event handlers you control, you can scale your computed relative position by `1 / zoom` where `zoom` is the current zoom level of the flow. To get the current zoom level, you can use the `getZoom` method from the [`useReactFlow`](/api-reference/hooks/use-react-flow) hook.

### Edges are not displaying.[](#edges-are-not-displaying) 

If your edges are not displaying in React Flow, this might be due to one of the following reasons:

- You have not imported the React Flow stylesheet. If you haven't imported it, you can import it like `import '@xyflow/react/dist/style.css';`.
- If you have replaced your default nodes with a custom node, check if that custom node has appropriate `source/target` handles in the custom node component. An edge cannot be made without a handle.
- If you use an external styling library like Tailwind or Bulma, ensure it doesn't override the edge styles. For example, sometimes styling libraries override the `.react-flow__edges` SVG selector with `overflow: hidden`, which hides the edges.
- If you are using an async operation like a request to the backend, make sure to call the `updateNodeInternals` function returned by the [`useUpdateNodeInternal`](/api-reference/hooks/use-update-node-internals) hook after the async operation so React Flow updates the handle position internally.

### Edges are not displaying correctly.[](#edges-are-not-displaying-correctly) 

If your edges are not rendering as they should, this could be due to one of the following reasons:

- If you want to hide your handles, do not use `display: none` to hide them. Use either `opacity: 0` or `visibility: hidden`.
- If edges are not connected to the correct handle, check if you have added more than one handle of the same type(`source` or `target`) in your custom node component. If that is the case, assign IDs to them. Multiple handles of the same kind on a node need to have distinguishable IDs so that React Flow knows which handle an edge corresponds to.
- If you are changing the position of the handles (via reordering, etc.), make sure to call the `updateNodeInternals` function returned by the [`useUpdateNodeInternals`](/api-reference/hooks/use-update-node-internals) hook after so React Flow knows to update the handle position internally.
- If you are using a custom edge and want your edge to go from the source handle to a target handle, make sure to correctly pass the `sourceX, sourceY, targetX, and targetY` props you get from the custom edge component in the edge path creation function(e.g., [`getBezierPath`](/api-reference/utils/get-bezier-path), etc.). `sourceX, sourceY`, and `targetX, targetY` represent the `x,y` coordinates for the source and target handle, respectively.
- If the custom edge from the source or target side is not going towards the handle as expected (entering or exiting from a handle at a weird angle), make sure to pass the `sourcePosition` and `targetPosition` props you get from the custom edge component in the edge path creation function(e.g., [`getBezierPath`](/api-reference/utils/get-bezier-path)). Passing the source/target handle position in the path creation function is necessary for the edge to start or end properly at a handle.