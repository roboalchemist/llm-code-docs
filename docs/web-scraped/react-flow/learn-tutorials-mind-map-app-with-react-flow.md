# Source: https://reactflow.dev/learn/tutorials/mind-map-app-with-react-flow

2023/01/10

## Build a Mind Map App with React Flow 

[![](https://github.com/moklick.png)](https://twitter.com/moklick)

[Moritz Klack](https://twitter.com/moklick)

Co-Founder

In this tutorial, you will learn to create a simple mind map tool with React Flow that can be used for brainstorming, organizing an idea, or mapping your thoughts in a visual way. To build this app, we'll be using state management, custom nodes and edges, and more.

## [🎬] It's Demo Time\![](#-its-demo-time) 

Before we get our hands dirty, I want to show you the mind-mapping tool we'll have by the end of this tutorial:

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

If you'd like to live dangerously and dive right into the code, you can find the source code on [Github ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/react-flow-mindmap-app).

## [👩🏻‍💻] Getting started[](#-getting-started) 

To do this tutorial you will need some knowledge of [React ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://reactjs.org/docs/getting-started.html) and [React Flow](/learn/concepts/terms-and-definitions) (hi, that's us! [😁] it's an open source library for building node-based UIs like workflow tools, ETL pipelines, and [more](/showcase).)

We'll be using [Vite ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://vitejs.dev/) to develop our app, but you can also use [Create React App ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://create-react-app.dev/) or any other tool you like. To scaffold a new React app with Vite you need to do:

npm

pnpm

yarn

bun

``` 
npm create vite@latest reactflow-mind-map -- --template react
```

``` 
npm create vite@latest reactflow-mind-map -- --template react
# couldn't auto-convert command
```

``` 
npm create vite@latest reactflow-mind-map -- --template react
# couldn't auto-convert command
```

``` 
bunx create-vite@latest reactflow-mind-map --template react
```

if you would like to use Typescript:

npm

pnpm

yarn

bun

``` 
npm create vite@latest reactflow-mind-map -- --template react-ts
```

``` 
npm create vite@latest reactflow-mind-map -- --template react-ts
# couldn't auto-convert command
```

``` 
npm create vite@latest reactflow-mind-map -- --template react-ts
# couldn't auto-convert command
```

``` 
bunx create-vite@latest reactflow-mind-map --template react-ts
```

After the initial setup, you need to install some packages:

npm

pnpm

yarn

bun

``` 
npm install reactflow zustand classcat nanoid
```

``` 
pnpm add reactflow zustand classcat nanoid
```

``` 
yarn add reactflow zustand classcat nanoid
```

``` 
bun add reactflow zustand classcat nanoid
```

We are using [Zustand ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/pmndrs/zustand) for managing the state of our application. It's a bit like Redux but way smaller and there's less boilerplate code to write. React Flow also uses Zustand, so the installation comes with no additional cost. (For this tutorial we are using Typescript but you can also use plain Javascript.)

To keep it simple we are putting all of our code in the `src/App` folder. For this you need to create the `src/App` folder and add an index file with the following content:

#### src/App/index.tsx[](#srcappindextsx) 

``` 
import  from '@xyflow/react';
 
// we have to import the React Flow styles for it to work
import '@xyflow/react/dist/style.css';
 
function Flow()  />
      <Panel position="top-left">React Flow Mind Map</Panel>
    </ReactFlow>
  );
}
 
export default Flow;
```

This will be our main component for rendering the mind map. There are no nodes or edges yet, but we added the React Flow [`Controls`](/api-reference/components/controls) component and a [`Panel`](/api-reference/components/panel) to display the title of our app.

To be able to use React Flow hooks, we need to wrap the application with the [`ReactFlowProvider`](/api-reference/react-flow-provider) component in our main.tsx (entry file for vite). We are also importing the newly created `App/index.tsx` and render it inside the `ReactFlowProvider.` Your main file should look like this:

#### src/main.tsx[](#srcmaintsx) 

``` 
import React from 'react';
import ReactDOM from 'react-dom/client';
import  from '@xyflow/react';
 
import App from './App';
 
import './index.css';
 
ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <ReactFlowProvider>
      <App />
    </ReactFlowProvider>
  </React.StrictMode>,
);
```

The parent container of the React Flow component needs a width and a height to work properly. Our app is a fullscreen app, so we add these rules to the `index.css` file:

#### src/index.css[](#srcindexcss) 

``` 
body 
 
html,
body,
#root 
```

We are adding all styles of our app to the `index.css` file (you could also use [Tailwind](/examples/styling/tailwind)). Now you can start the development server with `npm run dev` and you should see the following:

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

## [🏪] A store for nodes and edges[](#-a-store-for-nodes-and-edges) 

As mentioned above, we are using Zustand for state management. For this, we create a new file in our `src/App` folder called `store.ts`:

#### src/App/store.ts[](#srcappstorets) 

``` 
import  from '@xyflow/react';
import  from 'zustand/traditional';
 
export type RFState = ;
 
const useStore = createWithEqualityFn<RFState>((set, get) => (,
      position: ,
    },
  ],
  edges: [],
  onNodesChange: (changes: NodeChange[]) => );
  },
  onEdgesChange: (changes: EdgeChange[]) => );
  },
}));
 
export default useStore;
```

It seems like a lot of code, but it's mostly types [😇] The store keeps track of the nodes and edges and handles the change events. When a user drags a node, React Flow fires a change event, the store then applies the changes and the updated nodes get rendered. (You can read more about this in our [state management library guide](/api-reference/hooks/use-store).)

As you can see we start with one initial node placed at `` of type 'mindmap'. To connect the store with our app, we use the `useStore` hook:

#### src/App/index.tsx[](#srcappindextsx-1) 

``` 
import  from '@xyflow/react';
import  from 'zustand/shallow';
 
import useStore,  from './store';
 
// we have to import the React Flow styles for it to work
import '@xyflow/react/dist/style.css';
 
const selector = (state: RFState) => ();
 
// this places the node origin in the center of a node
const nodeOrigin: NodeOrigin = [0.5, 0.5];
 
function Flow()  = useStore(selector, shallow);
 
  return (
    <ReactFlow
      nodes=
      edges=
      onNodesChange=
      onEdgesChange=
      nodeOrigin=
      fitView
    >
      <Controls showInteractive= />
      <Panel position="top-left">React Flow Mind Map</Panel>
    </ReactFlow>
  );
}
 
export default Flow;
```

We access the nodes, edges and change handlers from the store and pass them to the React Flow component. We also use the `fitView` prop to make sure that the initial node is centered in the view and set the node origin to `[0.5, 0.5]` to set the origin to the center of a node. After this, your app should look like this:

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

You can move the node around and zoom in and out, we are getting somewhere [🚀] Now let's add some more functionality.

## [✨] Custom nodes and edges[](#-custom-nodes-and-edges) 

We want to use a custom type called 'mindmap' for our nodes. We need to add a new component for this. Let's create a new folder called `MindMapNode` with an index file under `src/App` with the following content:

#### src/App/MindMapNode/index.tsx[](#srcappmindmapnodeindextsx) 

``` 
import  from '@xyflow/react';
 
export type NodeData = ;
 
function MindMapNode(: NodeProps<NodeData>)  />
 
      <Handle type="target" position= />
      <Handle type="source" position= />
    </>
  );
}
 
export default MindMapNode;
```

We are using an input for displaying and editing the labels of our mind map nodes, and two handles for connecting them. This is necessary for React Flow to work; the handles are used as the start and end position of the edges.

We also add some CSS to the `index.css` file to make the nodes look a bit prettier:

#### src/index.css[](#srcindexcss-1) 

``` 
.react-flow__node-mindmap 
```

(For more on this, you can read the [guide to custom nodes](/learn/customization/custom-nodes) in our docs.)

Let's do the same for the custom edge. Create a new folder called `MindMapEdge` with an index file under `src/App`:

#### src/App/MindMapEdge/index.tsx[](#srcappmindmapedgeindextsx) 

``` 
import  from '@xyflow/react';
 
function MindMapEdge(props: EdgeProps)  = props;
 
  const [edgePath] = getStraightPath();
 
  return <BaseEdge path=  />;
}
 
export default MindMapEdge;
```

I will get into more detail about the custom nodes and edges in the next section. For now it's important that we can use the new types in our app, by adding the following to our `Flow` component:

``` 
import MindMapNode from './MindMapNode';
import MindMapEdge from './MindMapEdge';
 
const nodeTypes = ;
 
const edgeTypes = ;
```

and then pass the newly created types to the React Flow component.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

Nice! We can already change the labels of our nodes by clicking in the input field and typing something.

## [🆕] New nodes[](#-new-nodes) 

We want to make it super quick for a user to create a new node. The user should be able to add a new node by clicking on a node and drag to the position where a new node should be placed. This functionality is not built into React Flow, but we can implement it by using the [`onConnectStart` and `onConnectEnd`](/api-reference/react-flow#onconnectstart) handlers.

We are using the start handler to remember the node that was clicked and the end handler to create the new node:

#### Add to src/App/index.tsx[](#add-to-srcappindextsx) 

``` 
const connectingNodeId = useRef<string | null>(null);
 
const onConnectStart: OnConnectStart = useCallback((_, ) => , []);
 
const onConnectEnd: OnConnectEnd = useCallback((event) => `);
  }
}, []);
```

Since our nodes are managed by the store, we create an action to add a new node and its edge. This is how our `addChildNode` action looks:

#### New action in src/store.ts[](#new-action-in-srcstorets) 

``` 
addChildNode: (parentNode: Node, position: XYPosition) => ,
    position,
    parentNode: parentNode.id,
  };
 
  const newEdge = ;
 
  set();
};
```

We are using the passed node as a parent. Normally this feature is used to implement [grouping](/examples/nodes/dynamic-grouping) or [sub flows](/examples/grouping/sub-flows). Here we are using it to move all child nodes when their parent is moved. It enables us to clean up and re-order the mind map so that we don't have to move all child nodes manually. Let's use the new action in our `onConnectEnd` handler:

#### Adjustments in src/App/index.tsx[](#adjustments-in-srcappindextsx) 

``` 
const store = useStoreApi();
 
const onConnectEnd: OnConnectEnd = useCallback(
  (event) =>  = store.getState();
    const targetIsPane = (event.target as Element).classList.contains('react-flow__pane');
 
    if (targetIsPane && connectingNodeId.current) 
    }
  },
  [getChildNodePosition],
);
```

First we are getting the `nodeLookup` from the React Flow store via `store.getState()`. `nodeLookup` is a map that contains all nodes and their current state. We need it to get the position and dimensions of the clicked node. Then we check if the target of the onConnectEnd event is the React Flow pane. If it is, we want to add a new node. For this we are using our `addChildNode` and the newly created `getChildNodePosition` helper function.

#### Helper function in src/App/index.tsx[](#helper-function-in-srcappindextsx) 

``` 
const getChildNodePosition = (event: MouseEvent, parentNode?: Node) =>  = store.getState();
 
  if (
    !domNode ||
    // we need to check if these properties exist, because when a node is not initialized yet,
    // it doesn't have a positionAbsolute nor a width or height
    !parentNode?.computed?.positionAbsolute ||
    !parentNode?.computed?.width ||
    !parentNode?.computed?.height
  ) 
 
  const panePosition = screenToFlowPosition();
 
  // we are calculating with positionAbsolute here because child nodes are positioned relative to their parent
  return ;
};
```

This function returns the position of the new node we want to add to our store. We are using the [`project` function](/api-reference/types/react-flow-instance#project) to convert screen coordinates into React Flow coordinates. As mentioned earlier, child nodes are positioned relative to their parents. That's why we need to subtract the parent position from the child node position. That was a lot to take in, let's see it in action:

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

To test the new functionality you can start a connection from a handle and then end it on the pane. You should see a new node being added to the mind map.

## [🤝] Keep data in sync[](#-keep-data-in-sync) 

We can already update the labels but we are not updating the nodes data object. This is important to keep our app in sync and if we want to save our nodes on the server for example. To achieve this we add a new action called `updateNodeLabel` to the store. This action takes a node id and a label. The implementation is pretty straight forward: we iterate over the existing nodes and update the matching one with the passed label:

#### src/store.ts[](#srcstorets) 

``` 
updateNodeLabel: (nodeId: string, label: string) => ;
      }
 
      return node;
    }),
  });
},
```

Let's use the new action in our `MindmapNode` component:

#### src/App/MindmapNode/index.tsx[](#srcappmindmapnodeindextsx-1) 

``` 
import  from '@xyflow/react';
 
import useStore from '../store';
 
export type NodeData = ;
 
function MindMapNode(: NodeProps<NodeData>) 
        onChange=
        className="input"
      />
 
      <Handle type="target" position= />
      <Handle type="source" position= />
    </>
  );
}
 
export default MindMapNode;
```

That was quick! The input fields of the custom nodes now display the current label of the nodes. You could take your nodes data, save it on the server and then load it again.

## [💅] Simpler UX and nicer styling[](#-simpler-ux-and-nicer-styling) 

Functionality-wise we are finished with our mind map app! We can add new nodes, update their labels and move them around. But the UX and styling could use some improvements. Let's make it easier to drag the nodes and to create new nodes!

### 1. A node as handle[](#1-a-node-as-handle) 

Let's use the whole node as a handle, rather than displaying the default handles. This makes it easier to create nodes, because the area where you can start a new connection gets bigger. We need to style the source handle to be the size of the node and hide the target handle visually. React Flow still needs it to connect the nodes but we don't need to display it since we are creating new nodes by dropping an edge on the pane. We use plain old CSS to hide the target handle and position it in the center of the node:

#### src/index.css[](#srcindexcss-2) 

``` 
.react-flow__handle.target 
```

In order to make the whole node a handle, we also update the style of the source:

#### src/index.css[](#srcindexcss-3) 

``` 
.react-flow__handle.source 
```

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

This works but we can't move the nodes anymore because the source handle is now the whole node and covers the input field. We fix that by using the [`dragHandle` node option](/api-reference/types/node#drag-handle). It allows us to specify a selector for a DOM element that should be used as a drag handle. For this we adjust the custom node a bit:

#### src/App/MindmapNode/index.tsx[](#srcappmindmapnodeindextsx-2) 

``` 
import  from '@xyflow/react';
 
import useStore from '../store';
 
export type NodeData = ;
 
function MindMapNode(: NodeProps<NodeData>) 
          <svg viewBox="0 0 24 24">
            <path
              fill="#333"
              stroke="#333"
              strokeWidth="1"
              d="M15 5h2V3h-2v2zM7 5h2V3H7v2zm8 8h2v-2h-2v2zm-8 0h2v-2H7v2zm8 8h2v-2h-2v2zm-8 0h2v-2H7v2z"
            />
          </svg>
        </div>
        <input
          value=
          onChange=
          className="input"
        />
      </div>
 
      <Handle type="target" position= />
      <Handle type="source" position= />
    </>
  );
}
 
export default MindMapNode;
```

We add a wrapper div with the class name `inputWrapper` and a div with the class name `dragHandle` that acts as the drag handle (surprise!). Now we can style the new elements:

#### src/index.css[](#srcindexcss-4) 

``` 
.inputWrapper 
 
.dragHandle 
 
.input 
```

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

### 2. Activate input on focus[](#2-activate-input-on-focus) 

We are almost there but we need to adjust some more details. We want to start our new connection from the center of the node. For this we set the pointer events of the input to "none" and check if the user releases the button on top of the node. Only then we want to activate the input field. We can use our `onConnectEnd` function to achieve this:

#### src/App/index.tsx[](#srcappindextsx-2) 

``` 
const onConnectEnd: OnConnectEnd = useCallback(
  (event) =>  = store.getState();
    const targetIsPane = (event.target as Element).classList.contains('react-flow__pane');
    const node = (event.target as Element).closest('.react-flow__node');
 
    if (node) );
    } else if (targetIsPane && connectingNodeId.current) 
    }
  },
  [getChildNodePosition],
);
```

As you see we are focusing the input field if the user releases the mouse button on top of a node. We can now add some styling so that the input field is activated (pointerEvents: all) only when it's focused:

``` 
/* we want the connection line to be below the node */
.react-flow .react-flow__connectionline 
 
/* pointer-events: none so that the click for the connection goes through */
.inputWrapper 
 
/* pointer-events: all so that we can use the drag handle (here the user cant start a new connection) */
.dragHandle 
 
/* pointer-events: none by default */
.input 
 
/* pointer-events: all when it's focused so that we can type in it */
.input:focus 
```

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

### 3. Dynamic width and auto focus[](#3-dynamic-width-and-auto-focus) 

Almost done! We want to have a dynamic width for the nodes based on the length of the text. To keep it simple we do a calculation based on the length of text for this:

#### Added effect in src/app/MindMapNode.tsx[](#added-effect-in-srcappmindmapnodetsx) 

``` 
useLayoutEffect(() => px`;
  }
}, [data.label.length]);
```

We also want to focus / activate a node right after it gets created:

#### Added effect in src/app/MindMapNode.tsx[](#added-effect-in-srcappmindmapnodetsx-1) 

``` 
useEffect(() => );
    }
  }, 1);
}, []);
```

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

Now when you adjust a node label, the width of the node will adjust accordingly. You can also create a new node and it will be focused right away.

### 4. Centered edges and styling details[](#4-centered-edges-and-styling-details) 

You may have noticed that the edges are not centered. We created a custom edge at the beginning for this, and now we can adjust it a bit so that the edge starts in the center of the node and not at the top of the handle (the default behavior):

#### src/App/MindMapEdge.tsx[](#srcappmindmapedgetsx) 

``` 
import  from '@xyflow/react';
 
function MindMapEdge(props: EdgeProps)  = props;
 
  const [edgePath] = getStraightPath();
 
  return <BaseEdge path=  />;
}
 
export default MindMapEdge;
```

We are passing all props to the [`getStraightPath`](/api-reference/utils/get-straight-path) helper function but adjust the sourceY so that it is in the center of the node.

More over we want the title to be a bit more subtle and choose a color for our background. We can do this by adjusting the color of the panel (we added the class name `"header"`) and the background color of the body element:

``` 
body 
 
.header 
```

Nicely done! [💯] You can find the final code here:

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

## [👋] Final thoughts[](#-final-thoughts) 

What a trip! We started with an empty pane and ended with a fully functional mind map app. If you want to move on you could work on some of the following features:

- Add new nodes by clicking on the pane
- Save and restore button to store current state to local storage
- Export and import UI
- Collaborative editing

I hope you enjoyed this tutorial and learned something new! If you have any questions or feedback, feel free to reach out to me on [Twitter ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://twitter.com/moklick) or join our [Discord server ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://discord.com/invite/RVmnytFmGW). React Flow is an independent company financed by its users. If you want to support us you can [sponsor us on Github ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/sponsors/xyflow) or [subscribe to one of our Pro plans](/pro).

### Get Pro examples, prioritized bug reports, 1:1 support from the maintainers, and more with React Flow Pro 

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0idy01IGgtNSBtci0xIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik05LjgxMyAxNS45MDQgOSAxOC43NWwtLjgxMy0yLjg0NmE0LjUgNC41IDAgMCAwLTMuMDktMy4wOUwyLjI1IDEybDIuODQ2LS44MTNhNC41IDQuNSAwIDAgMCAzLjA5LTMuMDlMOSA1LjI1bC44MTMgMi44NDZhNC41IDQuNSAwIDAgMCAzLjA5IDMuMDlMMTUuNzUgMTJsLTIuODQ2LjgxM2E0LjUgNC41IDAgMCAwLTMuMDkgMy4wOVpNMTguMjU5IDguNzE1IDE4IDkuNzVsLS4yNTktMS4wMzVhMy4zNzUgMy4zNzUgMCAwIDAtMi40NTUtMi40NTZMMTQuMjUgNmwxLjAzNi0uMjU5YTMuMzc1IDMuMzc1IDAgMCAwIDIuNDU1LTIuNDU2TDE4IDIuMjVsLjI1OSAxLjAzNWEzLjM3NSAzLjM3NSAwIDAgMCAyLjQ1NiAyLjQ1NkwyMS43NSA2bC0xLjAzNS4yNTlhMy4zNzUgMy4zNzUgMCAwIDAtMi40NTYgMi40NTZaTTE2Ljg5NCAyMC41NjcgMTYuNSAyMS43NWwtLjM5NC0xLjE4M2EyLjI1IDIuMjUgMCAwIDAtMS40MjMtMS40MjNMMTMuNSAxOC43NWwxLjE4My0uMzk0YTIuMjUgMi4yNSAwIDAgMCAxLjQyMy0xLjQyM2wuMzk0LTEuMTgzLjM5NCAxLjE4M2EyLjI1IDIuMjUgMCAwIDAgMS40MjMgMS40MjNsMS4xODMuMzk0LTEuMTgzLjM5NGEyLjI1IDIuMjUgMCAwIDAtMS40MjMgMS40MjNaIiAvPjwvc3ZnPg==)React Flow Pro](https://reactflow.dev/pro)