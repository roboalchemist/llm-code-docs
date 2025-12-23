# Source: https://reactflow.dev/learn

# Quick Start 

This page will take you from zero to a working React Flow app in a few minutes. If you just want to have a look around and get an impression of React Flow, check out our interactive no-code [Playground ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://play.reactflow.dev/).

## Installation[](#installation) 

First, spin up a new React project however you like --- we recommend using [Vite ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://vitejs.dev/)

npm

pnpm

yarn

bun

``` 
npm init vite my-react-flow-app -- --template react
```

``` 
pnpm create vite my-react-flow-app --template react
```

``` 
yarn create vite my-react-flow-app --template react
```

``` 
bunx create-vite my-react-flow-app --template react
```

Next `cd` into your new project folder and add [`@xyflow/react`](https://npmjs.com/package/@xyflow/react) as a dependency

npm

pnpm

yarn

bun

``` 
npm install @xyflow/react
```

``` 
pnpm add @xyflow/react
```

``` 
yarn add @xyflow/react
```

``` 
bun add @xyflow/react
```

Lastly, spin up the dev server and you're good to go!

## Usage[](#usage) 

We will render the [`<ReactFlow />`](/api-reference/react-flow) component from the `@xyflow/react` package. That and defining a handful of [node](/api-reference/types/node) objects, [edge](/api-reference/types/edge) objects and [event handlers](/api-reference/react-flow#event-handlers) are all we need to get something going! Get rid of everything inside `App.jsx` and add the following:

``` 
import  from 'react';
import  from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
const initialNodes = [
  , data:  },
  , data:  },
];
const initialEdges = [];
 
export default function App() }>
      <ReactFlow
        nodes=
        edges=
        onNodesChange=
        onEdgesChange=
        onConnect=
        fitView
      />
    </div>
  );
}
```

There are two things to pay attention to here:

- [🎨] You must import the css stylesheet for React Flow to work.
- [📐] The `<ReactFlow />` component must have a parent element with a width and height.

## Result[](#result) 

Et voila. You've already created your first interactive flow! [🎉]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

## Next steps[](#next-steps) 

[[[Core Concepts]]](/learn/concepts/terms-and-definitions)[[[Customization]]](/learn/customization/custom-nodes)[[[Examples]]](/examples)[[[API Reference]]](/api-reference)[[[Discord]]](https://discord.gg/RVmnytFmGW)[[[Template Projects]]](https://github.com/xyflow/react-flow-example-apps)