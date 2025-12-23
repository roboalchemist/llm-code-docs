# Source: https://reactflow.dev/learn/advanced-use/ssr-ssg-configuration

# Server side rendering, server side generation 

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

Server side rendering is supported since React Flow 12

This is an advanced use case and assumes you are already familiar with React Flow. If you're new to React Flow, check out our [getting started guide](/learn/getting-started/installation-and-requirements).

In this guide you will learn how to configure React Flow to render a flow on the server, which will allow you to

- Display static HTML diagrams in documentation
- Render React Flow diagrams in non-js environments
- Dynamically generate open graph images that appear as embeds when sharing a link to your flow

(If you want to download an image of your flow, there's an easier way to do that on the client-side in our [download image example](/examples/misc/download-image).)

### Node dimensions[](#node-dimensions) 

You need to configure a few things to make React Flow work on the server, the most important being the node dimensions. React Flow only renders nodes if they have a width and height. Usually you pass nodes without a specific `width` and `height`, they are then measured and the dimensions get written to `measured.width` and `measured.height`. Since we can't measure the dimensions on the server, we need to pass them explicitly. This can be done with the `width` and `height` or the `initialWidth` and `initialHeight` node properties.

``` 
const nodes = [
  ,
    data: ,
    width: 100,
    height: 50,
  },
];
```

React Flow now knows the dimensions of the node and can render it on the server. The `width` and `height` properties are used as an inline style for the node. If you expect nodes to have different dimensions on the client or if the dimensions should by dynamic based on the content, you can use the `initialWidth` and `initialHeight` properties. They are only used for the first render (on the server or on the client) as long as the nodes are not measured and `measured.width` and `measured.height` are not set.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik04IDEuNWMtMi4zNjMgMC00IDEuNjktNCAzLjc1IDAgLjk4NC40MjQgMS42MjUuOTg0IDIuMzA0bC4yMTQuMjUzYy4yMjMuMjY0LjQ3LjU1Ni42NzMuODQ4LjI4NC40MTEuNTM3Ljg5Ni42MjEgMS40OWEuNzUuNzUgMCAwIDEtMS40ODQuMjExYy0uMDQtLjI4Mi0uMTYzLS41NDctLjM3LS44NDdhOC40NTYgOC40NTYgMCAwIDAtLjU0Mi0uNjhjLS4wODQtLjEtLjE3My0uMjA1LS4yNjgtLjMyQzMuMjAxIDcuNzUgMi41IDYuNzY2IDIuNSA1LjI1IDIuNSAyLjMxIDQuODYzIDAgOCAwczUuNSAyLjMxIDUuNSA1LjI1YzAgMS41MTYtLjcwMSAyLjUtMS4zMjggMy4yNTktLjA5NS4xMTUtLjE4NC4yMi0uMjY4LjMxOS0uMjA3LjI0NS0uMzgzLjQ1My0uNTQxLjY4MS0uMjA4LjMtLjMzLjU2NS0uMzcuODQ3YS43NTEuNzUxIDAgMCAxLTEuNDg1LS4yMTJjLjA4NC0uNTkzLjMzNy0xLjA3OC42MjEtMS40ODkuMjAzLS4yOTIuNDUtLjU4NC42NzMtLjg0OC4wNzUtLjA4OC4xNDctLjE3My4yMTMtLjI1My41NjEtLjY3OS45ODUtMS4zMi45ODUtMi4zMDQgMC0yLjA2LTEuNjM3LTMuNzUtNC0zLjc1Wk01Ljc1IDEyaDQuNWEuNzUuNzUgMCAwIDEgMCAxLjVoLTQuNWEuNzUuNzUgMCAwIDEgMC0xLjVaTTYgMTUuMjVhLjc1Ljc1IDAgMCAxIC43NS0uNzVoMi41YS43NS43NSAwIDAgMSAwIDEuNWgtMi41YS43NS43NSAwIDAgMS0uNzUtLjc1WiIgLz48L3N2Zz4=)

There are two ways to specify node dimensions for server side rendering:

1.  `width` and `height` for static dimensions that are known in advance and don't change.

2.  `initialWidth` and `initialHeight` for dynamic dimensions that are not known in advance or change.

### Handle positions[](#handle-positions) 

You probably also want to render the edges on the server. On the client, React Flow checks the positions of the handles and stores that information to draw the edges. Since we can't measure the handle positions on the server, we need to pass this information, too. This can be done with the `handles` property of a node.

``` 
const nodes: Node[] = [
  ,
    data: ,
    width: 100,
    height: 50,
    handles: [
      ,
      ,
    ],
  },
];
```

With this additional information, React Flow knows enough about the handles to render the edges on the server. If you are fine with just rendering the nodes, you can skip this step.

### Using `fitView` on the server[](#using-fitview-on-the-server) 

If you know the dimensions of the React Flow container itself, you can even use `fitView` on the server. For this, you need to pass the `width` and `height` of the container to the `ReactFlow` component.

``` 
<ReactFlow nodes= edges= fitView width= height= />
```

This will calculate the viewport and set the `transform` on the server in order to include all nodes in the viewport.

### Usage with the `<ReactFlowProvider>`[](#usage-with-the-reactflowprovider) 

If you are using the `ReactFlowProvider`, you can pass `initialNodes`, `initialEdges` and optional wrapper dimensions (`initialWidth` and `initialHeight`) and `fitView` to the provider.

``` 
<ReactFlowProvider
  initialNodes=
  initialEdges=
  initialWidth=
  initialHeight=
  fitView
>
  <App />
</ReactFlowProvider>
```

The `initial-` prefix means that these values are only used for the first render. After that, the provider will use the `nodes` and `edges` from the context.

### Creating static HTML[](#creating-static-html) 

If you want to create static HTML, you can use the `renderToStaticMarkup` function from React. This will render the React Flow component to a string of HTML. You can then use this string to create a static HTML file or send it as a response to an HTTP request.

``` 
import React from 'react';
import  from 'react-dom/server';
import  from '@xyflow/react';
 
function toHTML() ,
      React.createElement(Background, null),
    ),
  );
 
  return html;
}
```