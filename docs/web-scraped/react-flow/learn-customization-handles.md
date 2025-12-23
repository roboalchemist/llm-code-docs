# Source: https://reactflow.dev/learn/customization/handles

# Handles 

Handles are the connection points on [nodes](/learn/concepts/terms-and-definitions#nodes) in React Flow. Our built-in nodes include one source and one target handle, but you can customize your nodes with as many different handles as you need.

## Creating a node with handles[](#creating-a-node-with-handles) 

To create a [custom node](/learn/customization/custom-nodes) with handles, you can use the [`<Handle />`](/api-reference/components/handle) component provided by React Flow. This component allows you to define source and target handles for your custom nodes. Here's an example of how to implement a custom node with two handles:

``` 
import  from '@xyflow/react';
 
export function CustomNode()  />
      <Handle type="target" position= />
    </div>
  );
}
```

## Using multiple handles[](#using-multiple-handles) 

If you want to use multiple source or target handles in your custom node, you need to specify each handle with a unique `id`. This allows React Flow to differentiate between the handles when connecting edges.

``` 
  <Handle type="target" position= />
  <Handle type="source" position= id="a" />
  <Handle type="source" position= id="b" />
```

To connect an edge to a specific handle of a node, use the properties `sourceHandle` (for the edge's starting point) and `targetHandle` (for the edge's ending point). By defining `sourceHandle` or `targetHandle` with the appropriate handle `id`, you instruct React Flow to attach the edge to that specific handle, ensuring that connections are made where you intend.

``` 
const initialEdges = [
  ,
  ,
];
```

In this case, the source node is `n1` for both handles but the handle `id`s are different. One comes from handle id `a` and the other one from `b`. Both edges also have different target nodes:

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

By default React Flow positions a handle in the center of the specified side. If you want to display multiple handles on a side, you can adjust the position via inline styles or overwrite the default CSS and position it on your own.

## Custom handles[](#custom-handles) 

You can use any custom component as a Handle by wrapping it with the [`<Handle />`](/api-reference/components/handle) component. Follow these steps to integrate your custom component:

1.  Wrap your custom component with [`<Handle />`](/api-reference/components/handle) component.
2.  Hide the built-in [`<Handle />`](/api-reference/components/handle) appearance by setting `border` and `background` to `none`.
3.  Set the `width`and `height` of [`<Handle />`](/api-reference/components/handle) to match your custom component.
4.  Style the child component with `pointer-events: none`.
5.  Then, reposition the child custom component using CSS position properties like `top, left` if necessary to position it perfectly inside the [`<Handle />`](/api-reference/components/handle) component.

This example shows a Material UI icon `ArrowCircleRightIcon` used as a Handle.

``` 
import  from '@xyflow/react';
import ArrowCircleRightIcon from '@mui/icons-material/ArrowCircleRight';
 
export function CustomNode() 
        type="source"
        style=}
      >
        <ArrowCircleRightIcon
          style=}
        />
      </Handle>
      Custom Node
    </div>
  );
}
```

## Typeless handles[](#typeless-handles) 

If you want to create a handle that does not have a specific type (source or target), you can set [connectionMode](/api-reference/react-flow#connectionmode) to `Loose` in the `<ReactFlow />` component. This allows the handle to be used for both incoming and outgoing connections.

## Dynamic handles[](#dynamic-handles) 

If you are programmatically changing the position or number of handles in your custom node, you need to update the node internals with the [`useUpdateNodeInternals`](/api-reference/hooks/use-update-node-internals) hook.

## Custom handle styles[](#custom-handle-styles) 

Since the handle is a div, you can use CSS to style it or pass a style prop to customize a Handle. You can see this in the [Add Node On Edge Drop](/examples/nodes/add-node-on-edge-drop) and [Simple Floating Edges](/examples/edges/simple-floating-edges) examples.

### Styling handles when connecting[](#styling-handles-when-connecting) 

The handle receives the additional class names `connecting` when the connection line is above the handle and `valid` if the connection is valid. You can find an example which uses these classes [here](/examples/interaction/validation).

### Hiding handles[](#hiding-handles) 

If you need to hide a handle for some reason, you must use `visibility: hidden` or `opacity: 0` instead of `display: none`. This is important because React Flow needs to calculate the dimensions of the handle to work properly and using `display: none` will report a width and height of `0`!