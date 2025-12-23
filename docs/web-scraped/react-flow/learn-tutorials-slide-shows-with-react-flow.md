# Source: https://reactflow.dev/learn/tutorials/slide-shows-with-react-flow

2024/01/07

## Create a slide show presentation with React Flow 

[![](https://github.com/hayleigh-dot-dev.png)](https://twitter.com/hayleighdotdev)

[Hayleigh Thompson](https://twitter.com/hayleighdotdev)

Software Engineer

We recently published the findings from our React Flow 2023 end-of-year survey with an [interactive presentation](/developer-survey-2023) of the key findings, using React Flow itself. There were lots of useful bits built into this slideshow app, so we wanted to share how we built it!

<figure class="my-8 mx-0">
<img src="/_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fsurvey.png&amp;w=3840&amp;q=75" class="w-full h-auto rounded-xl" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" sizes="100vw" srcset="/_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fsurvey.png&amp;w=640&amp;q=75 640w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fsurvey.png&amp;w=750&amp;q=75 750w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fsurvey.png&amp;w=828&amp;q=75 828w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fsurvey.png&amp;w=1080&amp;q=75 1080w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fsurvey.png&amp;w=1200&amp;q=75 1200w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fsurvey.png&amp;w=1920&amp;q=75 1920w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fsurvey.png&amp;w=2048&amp;q=75 2048w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fsurvey.png&amp;w=3840&amp;q=75 3840w" width="0" height="0" alt="Screenshot of slides laid out on an infinite canvas, each with information pulled from a survey of React Flow users" />
<figcaption>Our 2023 end of year survey app was made up of many static nodes and buttons to navigate between them.</figcaption>
</figure>

By the end of this tutorial, you will have built a presentation app with

- Support for markdown slides
- Keyboard navigation around the viewport
- Automatic layouting
- Click-drag panning navigation (à la Prezi)

Along the way, you'll learn a bit about the basics of layouting algorithms, creating static flows, and custom nodes.

Once you're done, the app will look like this!

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

To follow along with this tutorial we'll assume you have a basic understanding of [React ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://reactjs.org/docs/getting-started.html) and [React Flow](/learn/concepts/terms-and-definitions), but if you get stuck on the way feel free to reach out to us on [Discord ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://discord.com/invite/RVmnytFmGW)!

Here's the [repo with the final code ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/react-flow-slide-show) if you'd like to skip ahead or refer to it as we go.

Let's get started!

## Setting up the project[](#setting-up-the-project) 

We like to recommend using [Vite ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://vitejs.dev) when starting new React Flow projects, and this time we'll use TypeScript too. You can scaffold a new project with the following command:

npm

pnpm

yarn

bun

``` 
npm create vite@latest -- --template react-ts
```

``` 
npm create vite@latest -- --template react-ts
# couldn't auto-convert command
```

``` 
npm create vite@latest -- --template react-ts
# couldn't auto-convert command
```

``` 
bunx create-vite@latest --template react-ts
```

If you'd prefer to follow along with JavaScript feel free to use the `react` template instead. You can also follow along in your browser by using our Codesandbox templates:

[[]](https://new.reactflow.dev/js)

JS

[new.reactflow.dev/js][[]](https://new.reactflow.dev/ts)

TS

[new.reactflow.dev/ts]

Besides React Flow we only need to pull in one dependency, [`react-remark`](https://www.npmjs.com/package/react-remark), to help us render markdown in our slides.

npm

pnpm

yarn

bun

``` 
npm install @xyflow/react react-remark
```

``` 
pnpm add @xyflow/react react-remark
```

``` 
yarn add @xyflow/react react-remark
```

``` 
bun add @xyflow/react react-remark
```

We'll modify the generated `main.tsx` to include React Flow's styles, as well as wrap the app in a `<ReactFlowProvider />` to make sure we can access the React Flow instance inside our components;

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[main.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import React from 'react';
import ReactDOM from 'react-dom/client';
import  from '@xyflow/react';
 
import App from './App';
 
import '@xyflow/react/dist/style.css';
import './index.css';
 
ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <ReactFlowProvider>
      
      <div style=}>
        <App />
      </div>
    </ReactFlowProvider>
  </React.StrictMode>,
);
```

This tutorial is going to gloss over the styling of the app, so feel free to use any CSS framework or styling solution you're familiar with. If you're going to style your app differently from just writing CSS, [Tailwind CSS](/examples/styling/tailwind), you can skip the import to `index.css`.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik04IDEuNWMtMi4zNjMgMC00IDEuNjktNCAzLjc1IDAgLjk4NC40MjQgMS42MjUuOTg0IDIuMzA0bC4yMTQuMjUzYy4yMjMuMjY0LjQ3LjU1Ni42NzMuODQ4LjI4NC40MTEuNTM3Ljg5Ni42MjEgMS40OWEuNzUuNzUgMCAwIDEtMS40ODQuMjExYy0uMDQtLjI4Mi0uMTYzLS41NDctLjM3LS44NDdhOC40NTYgOC40NTYgMCAwIDAtLjU0Mi0uNjhjLS4wODQtLjEtLjE3My0uMjA1LS4yNjgtLjMyQzMuMjAxIDcuNzUgMi41IDYuNzY2IDIuNSA1LjI1IDIuNSAyLjMxIDQuODYzIDAgOCAwczUuNSAyLjMxIDUuNSA1LjI1YzAgMS41MTYtLjcwMSAyLjUtMS4zMjggMy4yNTktLjA5NS4xMTUtLjE4NC4yMi0uMjY4LjMxOS0uMjA3LjI0NS0uMzgzLjQ1My0uNTQxLjY4MS0uMjA4LjMtLjMzLjU2NS0uMzcuODQ3YS43NTEuNzUxIDAgMCAxLTEuNDg1LS4yMTJjLjA4NC0uNTkzLjMzNy0xLjA3OC42MjEtMS40ODkuMjAzLS4yOTIuNDUtLjU4NC42NzMtLjg0OC4wNzUtLjA4OC4xNDctLjE3My4yMTMtLjI1My41NjEtLjY3OS45ODUtMS4zMi45ODUtMi4zMDQgMC0yLjA2LTEuNjM3LTMuNzUtNC0zLjc1Wk01Ljc1IDEyaDQuNWEuNzUuNzUgMCAwIDEgMCAxLjVoLTQuNWEuNzUuNzUgMCAwIDEgMC0xLjVaTTYgMTUuMjVhLjc1Ljc1IDAgMCAxIC43NS0uNzVoMi41YS43NS43NSAwIDAgMSAwIDEuNWgtMi41YS43NS43NSAwIDAgMS0uNzUtLjc1WiIgLz48L3N2Zz4=)

How you style your app is up to you, but you must **always** include React Flow's styles! If you don't need the default styles, at a minimum you should include the base styles from `@xyflow/react/dist/base.css`.

Each slide of our presentation will be a node on the canvas, so let's create a new file `Slide.tsx` that will be our custom node used to render each slide.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[Slide.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from '@xyflow/react';
 
export const SLIDE_WIDTH = 1920;
export const SLIDE_HEIGHT = 1080;
 
export type SlideNode = Node<SlideData, 'slide'>;
 
export type SlideData = ;
 
const style = px`,
  height: `$px`,
} satisfies React.CSSProperties;
 
export function Slide(: NodeProps<SlideNode>) >
      <div>Hello, React Flow!</div>
    </article>
  );
}
```

We're setting the slide width and height as constants here (rather than styling the node in CSS) because we'll want access to those dimensions later on. We've also stubbed out the `SlideData` type so we can properly type the component's props.

The last thing to do is to register our new custom node and show something on the screen.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[App.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from '@xyflow/react';
import  from './Slide.tsx';
 
const nodeTypes = ;
 
export default function App() , data:  }];
 
  return <ReactFlow nodes= nodeTypes= fitView />;
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik04IDEuNWMtMi4zNjMgMC00IDEuNjktNCAzLjc1IDAgLjk4NC40MjQgMS42MjUuOTg0IDIuMzA0bC4yMTQuMjUzYy4yMjMuMjY0LjQ3LjU1Ni42NzMuODQ4LjI4NC40MTEuNTM3Ljg5Ni42MjEgMS40OWEuNzUuNzUgMCAwIDEtMS40ODQuMjExYy0uMDQtLjI4Mi0uMTYzLS41NDctLjM3LS44NDdhOC40NTYgOC40NTYgMCAwIDAtLjU0Mi0uNjhjLS4wODQtLjEtLjE3My0uMjA1LS4yNjgtLjMyQzMuMjAxIDcuNzUgMi41IDYuNzY2IDIuNSA1LjI1IDIuNSAyLjMxIDQuODYzIDAgOCAwczUuNSAyLjMxIDUuNSA1LjI1YzAgMS41MTYtLjcwMSAyLjUtMS4zMjggMy4yNTktLjA5NS4xMTUtLjE4NC4yMi0uMjY4LjMxOS0uMjA3LjI0NS0uMzgzLjQ1My0uNTQxLjY4MS0uMjA4LjMtLjMzLjU2NS0uMzcuODQ3YS43NTEuNzUxIDAgMCAxLTEuNDg1LS4yMTJjLjA4NC0uNTkzLjMzNy0xLjA3OC42MjEtMS40ODkuMjAzLS4yOTIuNDUtLjU4NC42NzMtLjg0OC4wNzUtLjA4OC4xNDctLjE3My4yMTMtLjI1My41NjEtLjY3OS45ODUtMS4zMi45ODUtMi4zMDQgMC0yLjA2LTEuNjM3LTMuNzUtNC0zLjc1Wk01Ljc1IDEyaDQuNWEuNzUuNzUgMCAwIDEgMCAxLjVoLTQuNWEuNzUuNzUgMCAwIDEgMC0xLjVaTTYgMTUuMjVhLjc1Ljc1IDAgMCAxIC43NS0uNzVoMi41YS43NS43NSAwIDAgMSAwIDEuNWgtMi41YS43NS43NSAwIDAgMS0uNzUtLjc1WiIgLz48L3N2Zz4=)

It's important to remember to define your `nodeTypes` object *outside* of the component (or to use React's `useMemo` hook)! When the `nodeTypes` object changes, the entire flow is re-rendered.

With the basics put together, you can start the development server by running `npm run dev` and see the following:

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

Not super exciting yet, but let's add markdown rendering and create a few slides side by side!

## Rendering markdown[](#rendering-markdown) 

We want to make it easy to add content to our slides, so we'd like the ability to write [Markdown ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://www.markdownguide.org/basic-syntax/) in our slides. If you're not familiar, Markdown is a simple markup language for creating formatted text documents. If you've ever written a README on GitHub, you've used Markdown!

Thanks to the `react-remark` package we installed earlier, this step is a simple one. We can use the `<Remark />` component to render a string of markdown content into our slides.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[Slide.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from '@xyflow/react';
import  from 'react-remark';
 
export const SLIDE_WIDTH = 1920;
export const SLIDE_HEIGHT = 1080;
 
export type SlideNode = Node<SlideData, 'slide'>;
 
export type SlideData = ;
 
const style = px`,
  height: `$px`,
} satisfies React.CSSProperties;
 
export function Slide(: NodeProps<SlideNode>) >
      <Remark></Remark>
    </article>
  );
}
```

In React Flow, nodes can have data stored on them that can be used during rendering. In this case we're storing the markdown content to display by adding a `source` property to the `SlideData` type and passing that to the `<Remark />` component. We can update our hardcoded nodes with some markdown content to see it in action:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[App.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from '@xyflow/react';
import  from './Slide';
 
const nodeTypes = ;
 
export default function App() ,
      data: ,
    },
    ,
      data: ,
    },
    ,
      data: ,
    },
  ];
 
  return <ReactFlow nodes= nodeTypes= fitView minZoom= />;
}
```

Note that we've added the `minZoom` prop to the `<ReactFlow />` component. Our slides are quite large, and the default minimum zoom level is not enough to zoom out and see multiple slides at once.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

In the nodes array above, we've made sure to space the slides out by doing some manual math with the `SLIDE_WIDTH` constant. In the next section we'll come up with an algorithm to automatically lay out the slides in a grid.

## Laying out the nodes[](#laying-out-the-nodes) 

We often get asked how to automatically lay out nodes in a flow, and we have some documentation on how to use common layouting libraries like dagre and d3-hierarchy in our [layouting guide](/learn/layouting/layouting). Here you'll be writing your own super-simple layouting algorithm, which gets a bit nerdy, but stick with us!

For our presentation app we'll construct a simple grid layout by starting from 0,0 and updating the x or y coordinates any time we have a new slide to the left, right, up, or down.

First, we need to update our `SlideData` type to include optional ids for the slides to the left, right, up, and down of the current slide.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[Slide.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
export type SlideData = ;
```

Storing this information on the node data directly gives us some useful benefits:

- We can write fully declarative slides without worrying about the concept of nodes and edges

- We can compute the layout of the presentation by visiting connecting slides

- We can add navigation buttons to each slide to navigate between them automatically. We'll handle that in a later step.

The magic happens in a function we're going to define called `slidesToElements`. This function will take an object containing all our slides addressed by their id, and an id for the slide to start at. Then it will work through each connecting slide to build an array of nodes and edges that we can pass to the `<ReactFlow />` component.

The algorithm will go something like this:

- Push the initial slide's id and the position `` onto a stack.
- While that stack is not empty...
  - Pop the current position and slide id off the stack.

  - Look up the slide data by id.

  - Push a new node onto the nodes array with the current id, position, and slide data.

  - Add the slide's id to a set of visited slides.

  - For every direction (left, right, up, down)...

    - Make sure the slide has not already been visited.

    - Take the current position and update the x or y coordinate by adding or subtracting `SLIDE_WIDTH` or `SLIDE_HEIGHT` depending on the direction.

    - Push the new position and the new slide's id onto a stack.

    - Push a new edge onto the edges array connecting the current slide to the new slide.

    - Repeat for the remaining directions...

If all goes to plan, we should be able to take a stack of slides shown below and turn them into a neatly laid out grid!

<figure class="my-8 mx-0 sm:-mx-[min(calc((100vw-768px)/2),12rem)]">
<img src="/_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fideal-layout.png&amp;w=3840&amp;q=75" class="w-full h-auto rounded-xl" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" sizes="100vw" srcset="/_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fideal-layout.png&amp;w=640&amp;q=75 640w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fideal-layout.png&amp;w=750&amp;q=75 750w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fideal-layout.png&amp;w=828&amp;q=75 828w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fideal-layout.png&amp;w=1080&amp;q=75 1080w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fideal-layout.png&amp;w=1200&amp;q=75 1200w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fideal-layout.png&amp;w=1920&amp;q=75 1920w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fideal-layout.png&amp;w=2048&amp;q=75 2048w, /_next/image?url=%2Fimg%2Ftutorials%2Fpresentation%2Fideal-layout.png&amp;w=3840&amp;q=75 3840w" width="0" height="0" />
</figure>

Let's see the code. In a file called `slides.ts` add the following:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[slides.ts]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from './Slide';
 
export const slidesToElements = (initial: string, slides: Record<string, SlideData>) => ` onto a stack.
  const stack = [ }];
  const visited = new Set();
  const nodes = [];
  const edges = [];
 
  // While that stack is not empty...
  while (stack.length)  = stack.pop();
    // Look up the slide data by id.
    const data = slides[id];
    const node = ;
 
    // Push a new node onto the nodes array with the current id, position, and slide
    // data.
    nodes.push(node);
    // add the slide's id to a set of visited slides.
    visited.add(id);
 
    // For every direction (left, right, up, down)...
    // Make sure the slide has not already been visited.
    if (data.left && !visited.has(data.left)) ;
 
      // Push the new position and the new slide's id onto a stack.
      stack.push();
      // Push a new edge onto the edges array connecting the current slide to the
      // new slide.
      edges.push(->$`, source: id, target: data.left });
    }
 
    // Repeat for the remaining directions...
  }
 
  return ;
};
```

We've left out the code for the right, up, and down directions for brevity, but the logic is the same for each direction. We've also included the same breakdown of the algorithm as comments, to help you navigate the code.

Below is a demo app of the layouting algorithm, you can edit the `slides` object to see how adding slides to different directions affects the layout. For example, try extending 4's data to include `down: '5'` and see how the layout updates.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

If you spend a little time playing with this demo, you'll likely run across two limitations of this algorithm:

1.  It is possible to construct a layout that overlaps two slides in the same position.

2.  The algorithm will ignore nodes that cannot be reached from the initial slide.

Addressing these shortcomings is totally possible, but a bit beyond the scope of this tutorial. If you give a shot, be sure to share your solution with us on the [discord server ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://discord.com/invite/RVmnytFmGW)!

With our layouting algorithm written, we can hop back to `App.tsx` and remove the hardcoded nodes array in favor of the new `slidesToElements` function.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[App.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from '@xyflow/react';
import  from './slides';
import  from './Slide';
 
const slides: Record<string, SlideData> = ,
  '1': ,
  '2': ,
};
 
const nodeTypes = ;
 
const initialSlide = '0';
const  = slidesToElements(initialSlide, slides);
 
export default function App() 
      nodeTypes=
      fitView
      fitViewOptions=] }}
      minZoom=
    />
  );
}
```

The slides in our flow are static, so we can move the `slidesToElements` call *outside* the component to make sure we're not recalculating the layout if the component re-renders. Alternatively, you could use React's `useMemo` hook to define things inside the component but only calculate them once.

Because we have the idea of an "initial" slide now, we're also using the `fitViewOptions` to ensure the initial slide is the one that is focused when the canvas is first loaded.

## Navigating between slides[](#navigating-between-slides) 

So far we have our presentation laid out in a grid but we have to manually pan the canvas to see each slide, which isn't very practical for a presentation! We're going to add three different ways to navigate between slides:

- Click-to-focus on nodes for jumping to different slides by clicking on them.

- Navigation buttons on each slide for moving sequentially between slides in any valid direction.

- Keyboard navigation using the arrow keys for moving around the presentation without using the mouse or interacting with a slide directly.

### Focus on click[](#focus-on-click) 

The `<ReactFlow />` element can receive an [`onNodeClick`](/api-reference/react-flow#on-node-click) callback that fires when *any* node is clicked. Along with the mouse event itself, we also receive a reference to the node that was clicked on, and we can use that to pan the canvas thanks to the `fitView` method.

[`fitView`](/api-reference/types/react-flow-instance#fit-view) is a method on the React Flow instance, and we can get access to it by using the [`useReactFlow`](/api-reference/types/react-flow-instance#use-react-flow) hook.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[App.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from 'react';
import  from '@xyflow/react';
import  from './Slide';
 
const slides: Record<string, SlideData> = 
 
const nodeTypes = ;
 
const initialSlide = '0';
const  = slidesToElements(initialSlide, slides);
 
export default function App()  = useReactFlow();
  const handleNodeClick = useCallback<NodeMouseHandler>(
    (_, node) => );
    },
    [fitView],
  );
 
  return (
    <ReactFlow
      ...
      fitViewOptions=] }}
      onNodeClick=
    />
  );
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik04IDEuNWMtMi4zNjMgMC00IDEuNjktNCAzLjc1IDAgLjk4NC40MjQgMS42MjUuOTg0IDIuMzA0bC4yMTQuMjUzYy4yMjMuMjY0LjQ3LjU1Ni42NzMuODQ4LjI4NC40MTEuNTM3Ljg5Ni42MjEgMS40OWEuNzUuNzUgMCAwIDEtMS40ODQuMjExYy0uMDQtLjI4Mi0uMTYzLS41NDctLjM3LS44NDdhOC40NTYgOC40NTYgMCAwIDAtLjU0Mi0uNjhjLS4wODQtLjEtLjE3My0uMjA1LS4yNjgtLjMyQzMuMjAxIDcuNzUgMi41IDYuNzY2IDIuNSA1LjI1IDIuNSAyLjMxIDQuODYzIDAgOCAwczUuNSAyLjMxIDUuNSA1LjI1YzAgMS41MTYtLjcwMSAyLjUtMS4zMjggMy4yNTktLjA5NS4xMTUtLjE4NC4yMi0uMjY4LjMxOS0uMjA3LjI0NS0uMzgzLjQ1My0uNTQxLjY4MS0uMjA4LjMtLjMzLjU2NS0uMzcuODQ3YS43NTEuNzUxIDAgMCAxLTEuNDg1LS4yMTJjLjA4NC0uNTkzLjMzNy0xLjA3OC42MjEtMS40ODkuMjAzLS4yOTIuNDUtLjU4NC42NzMtLjg0OC4wNzUtLjA4OC4xNDctLjE3My4yMTMtLjI1My41NjEtLjY3OS45ODUtMS4zMi45ODUtMi4zMDQgMC0yLjA2LTEuNjM3LTMuNzUtNC0zLjc1Wk01Ljc1IDEyaDQuNWEuNzUuNzUgMCAwIDEgMCAxLjVoLTQuNWEuNzUuNzUgMCAwIDEgMC0xLjVaTTYgMTUuMjVhLjc1Ljc1IDAgMCAxIC43NS0uNzVoMi41YS43NS43NSAwIDAgMSAwIDEuNWgtMi41YS43NS43NSAwIDAgMS0uNzUtLjc1WiIgLz48L3N2Zz4=)

It's important to remember to include `fitView` as in the dependency array of our `handleNodeClick` callback. That's because the `fitView` function is replaced once React Flow has initialized the viewport. If you forget this step you'll likely find out that `handleNodeClick` does nothing at all (and yes, we also forget this ourselves sometimes too [🫠] ).

Calling `fitView` with no arguments would attempt to fit every node in the graph into view, but we only want to focus on the node that was clicked! The [`FitViewOptions`](/api-reference/types/fit-view-options) object lets us provide an array of just the nodes we want to focus on: in this case, that's just the node that was clicked.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

### Slide controls[](#slide-controls) 

Clicking to focus a node is handy for zooming out to see the big picture before focusing back in on a specific slide, but it's not a very practical way for navigating around a presentation. In this step we'll add some controls to each slide that allow us to move to a connected slide in any direction.

Let's add a `<footer>` to each slide that conditionally renders a button in any direction with a connected slide. We'll also preemptively create a `moveToNextSlide` callback that we'll use in a moment.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[Slide.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from '@xyflow/react';
import  from 'react-remark';
import  from 'react';
 
...
 
export function Slide(: NodeProps<SlideNide>) , []);
 
  return (
    <article className="slide nodrag" style=>
      <Remark></Remark>
      <footer className="slide__controls nopan">
        >←</button>)}
        >↑</button>)}
        >↓</button>)}
        >→</button>)}
      </footer>
    </article>
  );
}
```

You can style the footer however you like, but it's important to add the `"nopan"` class to prevent prevent the canvas from panning as you interact with any of the buttons.

To implement `moveToSlide`, we'll make use of `fitView` again. Previously we had a reference to the actual node that was clicked on to pass to `fitView`, but this time we only have a node's id. You might be tempted to look up the target node by its id, but actually that's not necessary! If we look at the type of [`FitViewOptions`](/api-reference/types/fit-view-options) we can see that the array of nodes we pass in only *needs* to have an `id` property:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTAgMi42NjY2N1YyMS4zMzMzQzAgMjIuODA2NyAxLjE5MzMzIDI0IDIuNjY2NjcgMjRIMjEuMzMzM0MyMi44MDY3IDI0IDI0IDIyLjgwNjcgMjQgMjEuMzMzM1YyLjY2NjY3QzI0IDEuMTkzMzMgMjIuODA2NyAwIDIxLjMzMzMgMEgyLjY2NjY3QzEuMTkzMzMgMCAwIDEuMTkzMzMgMCAyLjY2NjY3Wk0xNC4yMjEzIDEyLjYwMTNIMTEuMzk3M1YyMS4zMzMzSDkuMTIxMzNWMTIuNjAxM0g2LjM1NlYxMC42NjY3SDE0LjIyMTNWMTIuNjAxM1pNMTQuNjY0IDIwLjgzNDdWMTguNUMxNC42NjQgMTguNSAxNS45Mzg3IDE5LjQ2MTMgMTcuNDY5MyAxOS40NjEzQzE5IDE5LjQ2MTMgMTguOTQgMTguNDYxMyAxOC45NCAxOC4zMjRDMTguOTQgMTYuODcyIDE0LjYwNTMgMTYuODcyIDE0LjYwNTMgMTMuNjU2QzE0LjYwNTMgOS4yODEzMyAyMC45MjEzIDExLjAwOCAyMC45MjEzIDExLjAwOEwyMC44NDI3IDEzLjA4NjdDMjAuODQyNyAxMy4wODY3IDE5Ljc4NCAxMi4zOCAxOC41ODY3IDEyLjM4QzE3LjM5MDcgMTIuMzggMTYuOTU4NyAxMi45NDkzIDE2Ljk1ODcgMTMuNTU3M0MxNi45NTg3IDE1LjEyNjcgMjEuMzMzMyAxNC45NjkzIDIxLjMzMzMgMTguMTI4QzIxLjMzMzMgMjIuOTkyIDE0LjY2NCAyMC44MzQ3IDE0LjY2NCAyMC44MzQ3WiIgLz48L3N2Zz4=)[https://reactflow.dev/api-reference/types/fit-view-options]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
export type FitViewOptions = )[];
};
```

`Partial<Node>` means that all of the fields of the `Node` object type get marked as optional, and then we intersect that with `` to ensure that the `id` field is always required. This means we can just pass in an object with an `id` property and nothing else, and `fitView` will know what to do with it!

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[Slide.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from '@xyflow/react';
 
export function Slide(: NodeProps<SlideNide>)  = useReactFlow();
 
  const moveToNextSlide = useCallback(
    (id: string) => fitView(] }),
    [fitView],
  );
 
  return (
    <article className="slide" style=>
      ...
    </article>
  );
}
```

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

### Keyboard navigation[](#keyboard-navigation) 

The final piece of the puzzle is to add keyboard navigation to our presentation. It's not very convenient to have to *always* click on a slide to move to the next one, so we'll add some keyboard shortcuts to make it easier. React Flow lets us listen to keyboard events on the `<ReactFlow />` component through handlers like [`onKeyDown`](/api-reference/react-flow#on-key-down).

Up until now the slide currently focused is implied by the position of the canvas, but if we want to handle key presses on the entire canvas we need to *explicitly* track the current slide. We need to this because we need to know which slide to navigate to when an arrow key is pressed!

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[App.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from 'react';
import  from '@xyflow/react';
import  from './Slide';
 
const slides: Record<string, SlideData> = 
 
const nodeTypes = ;
 
const initialSlide = '0';
const  = slidesToElements(initialSlide, slides)
 
export default function App()  = useReactFlow();
 
  const handleNodeClick = useCallback<NodeMouseHandler>(
    (_, node) => );
      setCurrentSlide(node.id);
    },
    [fitView],
  );
 
  return (
    <ReactFlow
      ...
      onNodeClick=
    />
  );
}
```

Here we've added a bit of state, `currentSlide`, to our flow component and we're making sure to update it whenever a node is clicked. Next, we'll write a callback to handle keyboard events on the canvas:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[App.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
export default function App()  = useReactFlow();
 
  ...
 
  const handleKeyPress = useCallback<KeyboardEventHandler>(
    (event) => ] });
          }
      }
    },
    [currentSlide, fitView],
  );
 
  return (
    <ReactFlow
      ...
      onKeyPress=
    />
  );
}
```

To save some typing we're extracting the direction from the key pressed - if the user pressed `'ArrowLeft'` we'll get `'left'` and so on. Then, if there is actually a slide connected in that direction we'll update the current slide and call `fitView` to navigate to it!

We're also preventing the default behavior of the arrow keys to prevent the window from scrolling up and down. This is necessary for this tutorial because the canvas is only one part of the page, but for an app where the canvas is the entire viewport you might not need to do this.

And that's everything! To recap let's look at the final result and talk about what we've learned.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

## Final thoughts[](#final-thoughts) 

Even if you're not planning on making the next [Prezi ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://prezi.com), we've still looked at a few useful features of React Flow in this tutorial:

- The [`useReactFlow`](/api-reference/hooks/use-react-flow) hook to access the `fitView` method.

- The [`onNodeClick`](/api-reference/react-flow#on-node-click) event handler to listen to clicks on every node in a flow.

- The [`onKeyPress`](/api-reference/react-flow#on-key-press) event handler to listen to keyboard events on the entire canvas.

We've also looked at how to implement a simple layouting algorithm ourselves. Layouting is a *really* common question we get asked about, but if your needs aren't that complex you can get quite far rolling your own solution!

If you're looking for ideas on how to extend this project, you could try addressing the issues we pointed out with the layouting algorithm, coming up with a more sophisticated `Slide` component with different layouts, or something else entirely.

You can use the completed [source code ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/react-flow-slide-show) as a starting point, or you can just keep building on top of what we've made today. We'd love to see what you build so please share it with us over on our [Discord server ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://discord.com/invite/RVmnytFmGW) or [Twitter ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://twitter.com/reactflowdev).

### Get Pro examples, prioritized bug reports, 1:1 support from the maintainers, and more with React Flow Pro 

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0idy01IGgtNSBtci0xIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik05LjgxMyAxNS45MDQgOSAxOC43NWwtLjgxMy0yLjg0NmE0LjUgNC41IDAgMCAwLTMuMDktMy4wOUwyLjI1IDEybDIuODQ2LS44MTNhNC41IDQuNSAwIDAgMCAzLjA5LTMuMDlMOSA1LjI1bC44MTMgMi44NDZhNC41IDQuNSAwIDAgMCAzLjA5IDMuMDlMMTUuNzUgMTJsLTIuODQ2LjgxM2E0LjUgNC41IDAgMCAwLTMuMDkgMy4wOVpNMTguMjU5IDguNzE1IDE4IDkuNzVsLS4yNTktMS4wMzVhMy4zNzUgMy4zNzUgMCAwIDAtMi40NTUtMi40NTZMMTQuMjUgNmwxLjAzNi0uMjU5YTMuMzc1IDMuMzc1IDAgMCAwIDIuNDU1LTIuNDU2TDE4IDIuMjVsLjI1OSAxLjAzNWEzLjM3NSAzLjM3NSAwIDAgMCAyLjQ1NiAyLjQ1NkwyMS43NSA2bC0xLjAzNS4yNTlhMy4zNzUgMy4zNzUgMCAwIDAtMi40NTYgMi40NTZaTTE2Ljg5NCAyMC41NjcgMTYuNSAyMS43NWwtLjM5NC0xLjE4M2EyLjI1IDIuMjUgMCAwIDAtMS40MjMtMS40MjNMMTMuNSAxOC43NWwxLjE4My0uMzk0YTIuMjUgMi4yNSAwIDAgMCAxLjQyMy0xLjQyM2wuMzk0LTEuMTgzLjM5NCAxLjE4M2EyLjI1IDIuMjUgMCAwIDAgMS40MjMgMS40MjNsMS4xODMuMzk0LTEuMTgzLjM5NGEyLjI1IDIuMjUgMCAwIDAtMS40MjMgMS40MjNaIiAvPjwvc3ZnPg==)React Flow Pro](https://reactflow.dev/pro)