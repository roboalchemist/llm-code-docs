# Source: https://reactflow.dev/learn/concepts/terms-and-definitions

# Overview 

At its core, React Flow is about creating interactive flowgraphs --- a collection of nodes connected by edges. To help you understand the terminology we use throughout the documentation, let's take a look at the example flow below.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

### Nodes[](#nodes) 

React Flow has a few default node types out of the box, but customization is where the magic of React Flow truly happens. You can design your nodes to work exactly the way you need them to---whether that's embedding interactive form elements, displaying dynamic data visualizations, or even incorporating multiple connection handles. React Flow lays the foundation, and your imagination does the rest.

We have a guide on creating your own [Custom Nodes](/learn/customization/custom-nodes) and you can find all the options for customizing your nodes in the [Node](/api-reference/types/node) reference.

### Handles[](#handles) 

A handle (also known as a "port" in other libraries) is the attachment point where an edge connects to a node. By default, they appear as grey circles on the top, bottom, left, or right sides of a node. But they are just `div` elements, and can be positioned and styled any way you'd like. When creating a custom node, you can include as many handles as needed. For more information, refer to the [Handle](/learn/customization/handles) page.

### Edges[](#edges) 

Edges connect nodes. Every edge needs a target and a source node. React Flow comes with four built-in [edge types](/examples/edges/edge-types): `default` (bezier), `smoothstep`, `step`, and `straight`. An edge is a SVG path that can be styled with CSS and is completely customizable. If you are using multiple handles, you can reference them individually to create multiple connections for a node.

Like custom nodes, you can also customize edges. Things that people do with custom edges include:

- Adding buttons to remove edges
- Custom routing behavior
- Complex styling or interactions that cannot be solved with just one SVG path

For more information, refer to the [Edges](/learn/customization/custom-edges) page.

### Selection[](#selection) 

You can select an edge or a node by clicking on it. If you want to select multiple nodes/edges via clicking, you can hold the `Meta/Control` key and click on multiple elements to select them. If you want to change the keyboard key for multiselection to something else, you can use the [`multiSelectionKeyCode`](/api-reference/react-flow#multiselectionkeycode) prop.

You can also select multiple edges/nodes by holding down `Shift` and dragging the mouse to make a selection box. When you release the mouse, any node or edge that falls within the selection box is selected. If you want to change the keyboard key for this behavior, you can use the [`selectionKeyCode`](/api-reference/react-flow#selectionkeycode) prop.

Selected nodes and edges are elevated (assigned a higher `zIndex` than other elements), so that they are shown on top of all the other elements.

For default edges and nodes, selection is shown by a darker stroke/border than usual. If you are using a custom node/edge, you can use the `selected` prop to customize selection appearance inside your custom component.

### Connection line[](#connection-line) 

React Flow has built-in functionality that allows you to click and drag from one handle to another to create a new edge. While dragging, the placeholder edge is referred to as a connection line. The connection line comes with the same four built-in types as edges and is customizable. You can find the props for configuring the connection line in the [connection props](/api-reference/react-flow#connection-line-props) reference.

### Viewport[](#viewport) 

All of React Flow is contained within the viewport. Each node has an x- and y-coordinate, which indicates its position within the viewport. The viewport has x, y, and zoom values. When you drag the pane, you change the x and y coordinates. When you zoom in or out, you alter the zoom level.