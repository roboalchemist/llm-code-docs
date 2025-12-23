# Source: https://reactflow.dev/learn/advanced-use/whiteboard

# Whiteboard Features 

React Flow is designed for building node-based UIs like workflow editors, flowcharts and diagrams. Even if React Flow is not made for creating whiteboard applications, you might want to integrate common whiteboard features. These examples show how to add drawing capabilities to your applications when you need to annotate or sketch alongside your nodes and edges.

## Examples[](#examples) 

### ✏️ Freehand draw (Pro)[](#️-freehand-draw-pro) 

Draw smooth curves on your React Flow pane. Useful for annotations or sketching around existing nodes.

**Features:**

- Mouse/touch drawing
- Adjustable brush size and color
- converts drawn paths into custom nodes

**Common uses:**

- Annotating flowcharts
- Adding notes to diagrams
- Sketching ideas around nodes

**This is a Pro example.** Get [all pro examples](/pro/examples), templates, 1:1 support from the xyflow team and prioritized Github issues with a React Flow Pro subscription.

[See Pricing Plans](/pro)[Sign In](https://pro.reactflow.dev/examples/react/freehand-draw)

### 🎯 Lasso selection[](#-lasso-selection) 

Select multiple elements by drawing a freeform selection area with an option to include partially selected elements.

**Features:**

- Freeform selection shapes
- partial selection of elements

**Common uses:**

- Selecting nodes and annotations together
- Complex selections in mixed content

App.jsx

Lasso.tsx

xy-theme.css

index.css

utils.ts

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNS42NjYgMy44ODhBMi4yNSAyLjI1IDAgMCAwIDEzLjUgMi4yNWgtM2MtMS4wMyAwLTEuOS42OTMtMi4xNjYgMS42MzhtNy4zMzIgMGMuMDU1LjE5NC4wODQuNC4wODQuNjEydjBhLjc1Ljc1IDAgMCAxLS43NS43NUg5YS43NS43NSAwIDAgMS0uNzUtLjc1djBjMC0uMjEyLjAzLS40MTguMDg0LS42MTJtNy4zMzIgMGMuNjQ2LjA0OSAxLjI4OC4xMSAxLjkyNy4xODQgMS4xLjEyOCAxLjkwNyAxLjA3NyAxLjkwNyAyLjE4NVYxOS41YTIuMjUgMi4yNSAwIDAgMS0yLjI1IDIuMjVINi43NUEyLjI1IDIuMjUgMCAwIDEgNC41IDE5LjVWNi4yNTdjMC0xLjEwOC44MDYtMi4wNTcgMS45MDctMi4xODVhNDguMjA4IDQ4LjIwOCAwIDAgMSAxLjkyNy0uMTg0IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

``` 
import  from 'react';
import  from '@xyflow/react';
import  from './Lasso';
 
import '@xyflow/react/dist/style.css';
 
const initialNodes = [
  ,
    data: ,
  },
  ,
    data: ,
  },
];
 
const initialEdges = [];
 
export default function LassoSelectionFlow() 
      edges=
      onNodesChange=
      onEdgesChange=
      onConnect=
      fitView
    >
      <Controls />
      <Background />
       />}
 
      <Panel position="top-left" className="lasso-controls">
        <div className="xy-theme__button-group">
          <button
            className=`}
            onClick=
          >
            Lasso Mode
          </button>
          <button
            className=`}
            onClick=
          >
            Selection Mode
          </button>
        </div>
 
        <label>
          <input
            type="checkbox"
            checked=
            onChange=
            className="xy-theme__checkbox"
          />
          Partial selection
        </label>
      </Panel>
    </ReactFlow>
  );
}
```

### 🧹 Eraser[](#-eraser) 

Remove items by "erasing" over them. Uses collision detection to determine what to delete.

**Features:**

- Collision-based erasing
- Visual eraser cursor

**Common uses:**

- Removing parts of a flow

App.jsx

ErasableEdge.tsx

ErasableNode.tsx

Eraser.tsx

xy-theme.css

index.css

utils.ts

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNS42NjYgMy44ODhBMi4yNSAyLjI1IDAgMCAwIDEzLjUgMi4yNWgtM2MtMS4wMyAwLTEuOS42OTMtMi4xNjYgMS42MzhtNy4zMzIgMGMuMDU1LjE5NC4wODQuNC4wODQuNjEydjBhLjc1Ljc1IDAgMCAxLS43NS43NUg5YS43NS43NSAwIDAgMS0uNzUtLjc1djBjMC0uMjEyLjAzLS40MTguMDg0LS42MTJtNy4zMzIgMGMuNjQ2LjA0OSAxLjI4OC4xMSAxLjkyNy4xODQgMS4xLjEyOCAxLjkwNyAxLjA3NyAxLjkwNyAyLjE4NVYxOS41YTIuMjUgMi4yNSAwIDAgMS0yLjI1IDIuMjVINi43NUEyLjI1IDIuMjUgMCAwIDEgNC41IDE5LjVWNi4yNTdjMC0xLjEwOC44MDYtMi4wNTcgMS45MDctMi4xODVhNDguMjA4IDQ4LjIwOCAwIDAgMSAxLjkyNy0uMTg0IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

``` 
import  from 'react';
import  from '@xyflow/react';
 
import  from './ErasableNode';
import  from './ErasableEdge';
import  from './Eraser';
 
import '@xyflow/react/dist/style.css';
 
const initialNodes = [
  ,
    data: ,
  },
  ,
    data: ,
  },
];
 
const initialEdges = [
  ,
];
 
const nodeTypes = ;
 
const edgeTypes = ;
 
const defaultEdgeOptions = ;
 
export default function EraserFlow() 
      nodeTypes=
      edges=
      edgeTypes=
      onNodesChange=
      onEdgesChange=
      onConnect=
      fitView
      defaultEdgeOptions=
    >
      <Controls />
      <Background />
 
      
 
      <Panel position="top-left">
        <div className="xy-theme__button-group">
          <button
            className=`}
            onClick=
          >
            Eraser Mode
          </button>
          <button
            className=`}
            onClick=
          >
            Selection Mode
          </button>
        </div>
      </Panel>
    </ReactFlow>
  );
}
```

### 📐 Rectangle draw[](#-rectangle-draw) 

Create rectangular shapes by clicking and dragging. Good for highlighting areas or creating backgrounds for node groups.

**Features:**

- Click-and-drag rectangle creation
- Customizable colors

**Common uses:**

- Creating background containers
- Grouping related nodes visually
- Highlighting sections of diagrams

App.jsx

RectangleNode.tsx

RectangleTool.tsx

xy-theme.css

index.css

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNS42NjYgMy44ODhBMi4yNSAyLjI1IDAgMCAwIDEzLjUgMi4yNWgtM2MtMS4wMyAwLTEuOS42OTMtMi4xNjYgMS42MzhtNy4zMzIgMGMuMDU1LjE5NC4wODQuNC4wODQuNjEydjBhLjc1Ljc1IDAgMCAxLS43NS43NUg5YS43NS43NSAwIDAgMS0uNzUtLjc1djBjMC0uMjEyLjAzLS40MTguMDg0LS42MTJtNy4zMzIgMGMuNjQ2LjA0OSAxLjI4OC4xMSAxLjkyNy4xODQgMS4xLjEyOCAxLjkwNyAxLjA3NyAxLjkwNyAyLjE4NVYxOS41YTIuMjUgMi4yNSAwIDAgMS0yLjI1IDIuMjVINi43NUEyLjI1IDIuMjUgMCAwIDEgNC41IDE5LjVWNi4yNTdjMC0xLjEwOC44MDYtMi4wNTcgMS45MDctMi4xODVhNDguMjA4IDQ4LjIwOCAwIDAgMSAxLjkyNy0uMTg0IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

``` 
import  from 'react';
import  from '@xyflow/react';
 
import  from './RectangleNode';
import  from './RectangleTool';
 
import '@xyflow/react/dist/style.css';
 
const initialNodes = [
  ,
    data: ,
    width: 150,
    height: 100,
  },
];
const initialEdges = [];
 
const nodeTypes = ;
 
export default function RectangleFlow() 
      nodeTypes=
      edges=
      onNodesChange=
      onEdgesChange=
      onConnect=
      fitView
    >
      <Controls />
      <Background />
 
      
 
      <Panel position="top-left">
        <div className="xy-theme__button-group">
          <button
            className=`}
            onClick=
          >
            Rectangle Mode
          </button>
          <button
            className=`}
            onClick=
          >
            Selection Mode
          </button>
        </div>
      </Panel>
    </ReactFlow>
  );
}
```

## Whiteboard libraries[](#whiteboard-libraries) 

If you are looking for a more complete whiteboard solution, consider using libraries that are specifically designed for whiteboard applications like [tldraw ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://tldraw.dev/) or [Excalidraw ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://docs.excalidraw.com/). These libraries provide a full set of features for collaborative drawing, shapes, text, and more.