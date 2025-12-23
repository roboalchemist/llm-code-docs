# Source: https://reactflow.dev/learn/advanced-use/hooks-providers

# Hooks and Providers 

React Flow provides several [hooks](/api-reference/hooks) and a context provider for you to enhance the functionality of your flow. These tools help you to manage state, access internal methods, and create custom components more effectively.

## ReactFlowProvider[](#reactflowprovider) 

The ReactFlowProvider is a context provider that allows you to access the internal state of the flow, such as nodes, edges, and viewport, from anywhere in your component tree even outside the [`ReactFlow`](/api-reference/react-flow) component. It is typically used at the top level of your application.

There are several cases where you might need to use the [`ReactFlowProvider`](/api-reference/react-flow-provider) component:

- Many of the [hooks](/api-reference/hooks) we provide rely on this component to work.
- You want to access the internal state of the flow outside of the `ReactFlow` component.
- You are working with multiple flows on a page.
- You are using a client-side router.

App.jsx

Sidebar.jsx

xy-theme.css

index.css

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNS42NjYgMy44ODhBMi4yNSAyLjI1IDAgMCAwIDEzLjUgMi4yNWgtM2MtMS4wMyAwLTEuOS42OTMtMi4xNjYgMS42MzhtNy4zMzIgMGMuMDU1LjE5NC4wODQuNC4wODQuNjEydjBhLjc1Ljc1IDAgMCAxLS43NS43NUg5YS43NS43NSAwIDAgMS0uNzUtLjc1djBjMC0uMjEyLjAzLS40MTguMDg0LS42MTJtNy4zMzIgMGMuNjQ2LjA0OSAxLjI4OC4xMSAxLjkyNy4xODQgMS4xLjEyOCAxLjkwNyAxLjA3NyAxLjkwNyAyLjE4NVYxOS41YTIuMjUgMi4yNSAwIDAgMS0yLjI1IDIuMjVINi43NUEyLjI1IDIuMjUgMCAwIDEgNC41IDE5LjVWNi4yNTdjMC0xLjEwOC44MDYtMi4wNTcgMS45MDctMi4xODVhNDguMjA4IDQ4LjIwOCAwIDAgMSAxLjkyNy0uMTg0IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

``` 
import React,  from 'react';
import  from '@xyflow/react';
 
import Sidebar from './Sidebar';
import '@xyflow/react/dist/style.css';
 
const initialNodes = [
  ,
    position: ,
  },
  , position:  },
  , position:  },
  , position:  },
];
 
const initialEdges = [
  ,
  ,
];
 
const ProviderFlow = () => 
            edges=
            onNodesChange=
            onEdgesChange=
            onConnect=
            fitView
          >
            <Controls />
            <Background />
          </ReactFlow>
        </div>
        <Sidebar nodes= setNodes= />
      </ReactFlowProvider>
    </div>
  );
};
 
export default ProviderFlow;
```

## useReactFlow[](#usereactflow) 

The [`useReactFlow`](/api-reference/hooks/use-react-flow) hook provides access to the [`ReactFlowInstance`](/api-reference/types/react-flow-instance) and its methods. It allows you to manipulate nodes, edges, and the viewport programmatically.

This example illustrates how to use the `useReactFlow` hook.

App.jsx

Buttons.jsx

xy-theme.css

index.css

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNS42NjYgMy44ODhBMi4yNSAyLjI1IDAgMCAwIDEzLjUgMi4yNWgtM2MtMS4wMyAwLTEuOS42OTMtMi4xNjYgMS42MzhtNy4zMzIgMGMuMDU1LjE5NC4wODQuNC4wODQuNjEydjBhLjc1Ljc1IDAgMCAxLS43NS43NUg5YS43NS43NSAwIDAgMS0uNzUtLjc1djBjMC0uMjEyLjAzLS40MTguMDg0LS42MTJtNy4zMzIgMGMuNjQ2LjA0OSAxLjI4OC4xMSAxLjkyNy4xODQgMS4xLjEyOCAxLjkwNyAxLjA3NyAxLjkwNyAyLjE4NVYxOS41YTIuMjUgMi4yNSAwIDAgMS0yLjI1IDIuMjVINi43NUEyLjI1IDIuMjUgMCAwIDEgNC41IDE5LjVWNi4yNTdjMC0xLjEwOC44MDYtMi4wNTcgMS45MDctMi4xODVhNDguMjA4IDQ4LjIwOCAwIDAgMSAxLjkyNy0uMTg0IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

``` 
import React,  from 'react';
import  from '@xyflow/react';
 
import Buttons from './Buttons';
import '@xyflow/react/dist/style.css';
 
const initialNodes = [
  ,
    position: ,
  },
  , position:  },
  , position:  },
  , position:  },
];
 
const initialEdges = [
  ,
  ,
];
 
const ProviderFlow = () => 
        edges=
        onNodesChange=
        onEdgesChange=
        onConnect=
        fitView
      >
        <Buttons />
        <Background />
      </ReactFlow>
    </ReactFlowProvider>
  );
};
 
export default ProviderFlow;
```