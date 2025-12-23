# Source: https://reactflow.dev/learn/customization/custom-edges

# Custom Edges 

Like [custom nodes](/learn/customization/custom-nodes), parts of a custom edge in React Flow are just React components. That means you can render anything you want along an edge! This guide shows you how to implement a custom edge with some additional controls. For a comprehensive reference of props available for custom edges, see the [Edge](/api-reference/types/edge-props) reference.

## A basic custom edge[](#a-basic-custom-edge) 

An edge isn't much use to us if it doesn't render a path between two connected nodes. These paths are always SVG-based and are typically rendered using the [`<BaseEdge />`](/api-reference/components/base-edge) component. To calculate the actual SVG path to render, React Flow comes with some handy utility functions:

- [`getBezierPath`](/api-reference/utils/get-bezier-path)
- [`getSimpleBezierPath`](/api-reference/utils/get-simple-bezier-path)
- [`getSmoothStepPath`](/api-reference/utils/get-smooth-step-path)
- [`getStraightPath`](/api-reference/utils/get-straight-path)

To kickstart our custom edge, we'll just render a straight path between the source and target.

### Create the component[](#create-the-component) 

We start by creating a new React component called `CustomEdge`. Then we render the [`<BaseEdge />`](/api-reference/components/base-edge) component with the calculated path. This gives us a straight edge that behaves the same as the built-in default [edge version](/api-reference/types/edge#default-edge-types) `"straight"`.

``` 
import  from '@xyflow/react';
 
export function CustomEdge() );
 
  return (
    <>
      <BaseEdge id= path= />
    </>
  );
}
```

### Create `edgeTypes`[](#create-edgetypes) 

Outside of our component, we define an `edgeTypes` object. We name our new edge type `"custom-edge"` and assign the `CustomEdge` component we just created to it.

``` 
const edgeTypes = ;
```

### Pass the `edgeTypes` prop[](#pass-the-edgetypes-prop) 

To use it, we also need to update the [`edgeTypes`](/api-reference/react-flow#edge-types) prop on the `<ReactFlow />` component.

``` 
export function Flow()  />;
}
```

### Use the new edge type[](#use-the-new-edge-type) 

After defining the `edgeTypes` object, we can use our new custom edge by setting the `type` field of an edge to `"custom-edge"`.

``` 
const initialEdges = [
  ,
];
```

### Flow with a custom edge[](#flow-with-a-custom-edge) 

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

## Custom SVG edge paths[](#custom-svg-edge-paths) 

As discussed previously, if you want to make a custom edge in React Flow, you have to use either of the four path creation functions discussed above (e.g [`getBezierPath`](/api-reference/utils/get-bezier-path)). However if you want to make some other path shape like a Sinusoidal edge or some other edge type then you will have to make the edge path yourself.

The edge path we get from functions like [`getBezierPath`](/api-reference/utils/get-bezier-path) is just a path string which we pass into the `path` prop of the `<BaseEdge />` component. It contains the necessary information needed in order to draw that path, like where it should start from, where it should curve, where it should end, etc. A simple straight path string between two points `(x1, y1)` to `(x2, y2)` would look like:

``` 
M x1 y1 L x2 y2
```

An SVG path is a concatenated list of commands like `M`, `L`, `Q`, etc, along with their values. Some of these commands are listed below, along with their supported values.

- `M x1 y1` is the Move To command which moves the current point to the x1, y1 coordinate.
- `L x1 y1` is the Line To command which draws a line from the current point to x1, y1 coordinate.
- `Q x1 y1 x2 y2` is the Quadratic Bezier Curve command which draws a bezier curve from the current point to the x2, y2 coordinate. x1, y1 is the control point of the curve which determines the curviness of the curve.

Whenever we want to start a path for our custom edge, we use the `M` command to move our current point to `sourceX, sourceY` which we get as props in the custom edge component. Then based on the shape we want, we will use other commands like `L`(to make lines), `Q`(to make curves) and then finally end our path at `targetX, targetY` which we get as props in the custom edge component.

If you want to learn more about SVG paths, you can check out [SVG-Path-Editor ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://yqnn.github.io/svg-path-editor/). You can paste any SVG path there and analyze individual path commands via an intuitive UI.

Here is an example with two types of custom edge paths, a Step edge and a Sinusoidal edge. You should look at the Step edge first to get your hands dirty with custom SVG paths since it's simple, and then look at how the Sinusoidal edge is made. After going through this example, you will have the necessary knowledge to make custom SVG paths for your custom edges.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)