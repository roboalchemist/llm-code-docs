# Source: https://reactflow.dev/learn/customization/edge-labels

# Edge Labels 

One of the more common uses for [custom edges](/learn/customization/custom-edges) is rendering some controls or info along an edge's path. In React Flow we call that a *custom edge label* and unlike the edge path, edge labels can be any React component!

## Adding an edge label[](#adding-an-edge-label) 

To render a custom edge label we must wrap it in the [`<EdgeLabelRenderer />`](/api-reference/components/edge-label-renderer) component. This allows us to render the labels outside of the SVG world where the edges life. The edge label renderer is a portal to a single container that *all* edge labels are rendered into.

Let's add a button to our custom edge that can be used to delete the edge it's attached to:

``` 
import  from '@xyflow/react';
 
export default function CustomEdge()  = useReactFlow();
  const [edgePath] = getStraightPath();
 
  return (
    <>
      <BaseEdge id= path= />
      <EdgeLabelRenderer>
        <button onClick=] })}>delete</button>
      </EdgeLabelRenderer>
    </>
  );
}
```

If we try to use this edge now, we'll see that the button is rendered in the centre of the flow (it might be hidden behind "Node A"). Because of the edge label portal, we'll need to do some extra work to position the button ourselves.

<figure class="my-8 mx-0">
<img src="/_next/image?url=%2Fimg%2Flearn%2Fedge-label-renderer-position.png&amp;w=3840&amp;q=75" class="w-full h-auto rounded-xl" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" sizes="100vw" srcset="/_next/image?url=%2Fimg%2Flearn%2Fedge-label-renderer-position.png&amp;w=640&amp;q=75 640w, /_next/image?url=%2Fimg%2Flearn%2Fedge-label-renderer-position.png&amp;w=750&amp;q=75 750w, /_next/image?url=%2Fimg%2Flearn%2Fedge-label-renderer-position.png&amp;w=828&amp;q=75 828w, /_next/image?url=%2Fimg%2Flearn%2Fedge-label-renderer-position.png&amp;w=1080&amp;q=75 1080w, /_next/image?url=%2Fimg%2Flearn%2Fedge-label-renderer-position.png&amp;w=1200&amp;q=75 1200w, /_next/image?url=%2Fimg%2Flearn%2Fedge-label-renderer-position.png&amp;w=1920&amp;q=75 1920w, /_next/image?url=%2Fimg%2Flearn%2Fedge-label-renderer-position.png&amp;w=2048&amp;q=75 2048w, /_next/image?url=%2Fimg%2Flearn%2Fedge-label-renderer-position.png&amp;w=3840&amp;q=75 3840w" width="0" height="0" alt="A screen shot of a simple flow. The edge label renderer is highlighted in the DOM inspector and the button is rendered in the centre of the flow." />
</figure>

Fortunately, the path utils we've already seen can help us with this! Along with the SVG path to render, these functions also return the `x` and `y` coordinates of the path's midpoint. We can then use these coordinates to translate our custom edge label's into the right position!

``` 
export default function CustomEdge()  = useReactFlow();
  const [edgePath, labelX, labelY] = getStraightPath();
 
  return (
    ...
        <button
          style=px, $px)`,
            pointerEvents: 'all',
          }}
          className="nodrag nopan"
          onClick=] })}
        >
    ...
  );
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

To make sure our edge labels are interactive and not just for presentation, it is important to add `pointer-events: all` to the label's style. This will ensure that the label is clickable.

And just like with interactive controls in custom nodes, we need to remember to add the `nodrag` and `nopan` classes to the label to stop mouse events from controlling the canvas.

Here's an interactive example with our updated custom edge. Clicking the delete button will remove that edge from the flow. Creating a new edge will use the custom node.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)