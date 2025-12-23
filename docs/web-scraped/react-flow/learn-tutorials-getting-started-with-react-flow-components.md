# Source: https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components

2024/01/20

## Getting started with React Flow UI 

[![](https://github.com/hayleigh-dot-dev.png)](https://twitter.com/hayleighdotdev)

[Hayleigh Thompson](https://twitter.com/hayleighdotdev)

Software Engineer

[![](https://cheli.dev/alessandro.jpg)](https://cheli.dev)

[Alessandro Cheli](https://cheli.dev)

Software Engineer

***Update November 2025**: We have updated the tutorial to use the latest version of shadcn/ui, on React 19 and Tailwind 4!*

***Update July 2025**: "React Flow UI" was formerly known as "React Flow Components". We renamed it because it now includes both components and templates. Additionally, since it's built on shadcn/ui, the "UI" naming makes it easier for developers to recognize the connection and understand what we offer.*

Recently, we launched an exciting new addition to our open-source roster: React Flow UI (Previously known as React Flow Components). These are pre-built nodes, edges, and other ui elements that you can quickly add to your React Flow applications to get up and running. The catch is these components are built on top of [shadcn/ui ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://ui.shadcn.com) and the shadcn CLI.

We've previously written about our experience and what led us to choosing shadcn over on the [xyflow blog ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://xyflow.com/blog/react-flow-components), but in this tutorial we're going to focus on how to get started from scratch with shadcn, Tailwind CSS, and React Flow Components.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik04IDEuNWMtMi4zNjMgMC00IDEuNjktNCAzLjc1IDAgLjk4NC40MjQgMS42MjUuOTg0IDIuMzA0bC4yMTQuMjUzYy4yMjMuMjY0LjQ3LjU1Ni42NzMuODQ4LjI4NC40MTEuNTM3Ljg5Ni42MjEgMS40OWEuNzUuNzUgMCAwIDEtMS40ODQuMjExYy0uMDQtLjI4Mi0uMTYzLS41NDctLjM3LS44NDdhOC40NTYgOC40NTYgMCAwIDAtLjU0Mi0uNjhjLS4wODQtLjEtLjE3My0uMjA1LS4yNjgtLjMyQzMuMjAxIDcuNzUgMi41IDYuNzY2IDIuNSA1LjI1IDIuNSAyLjMxIDQuODYzIDAgOCAwczUuNSAyLjMxIDUuNSA1LjI1YzAgMS41MTYtLjcwMSAyLjUtMS4zMjggMy4yNTktLjA5NS4xMTUtLjE4NC4yMi0uMjY4LjMxOS0uMjA3LjI0NS0uMzgzLjQ1My0uNTQxLjY4MS0uMjA4LjMtLjMzLjU2NS0uMzcuODQ3YS43NTEuNzUxIDAgMCAxLTEuNDg1LS4yMTJjLjA4NC0uNTkzLjMzNy0xLjA3OC42MjEtMS40ODkuMjAzLS4yOTIuNDUtLjU4NC42NzMtLjg0OC4wNzUtLjA4OC4xNDctLjE3My4yMTMtLjI1My41NjEtLjY3OS45ODUtMS4zMi45ODUtMi4zMDQgMC0yLjA2LTEuNjM3LTMuNzUtNC0zLjc1Wk01Ljc1IDEyaDQuNWEuNzUuNzUgMCAwIDEgMCAxLjVoLTQuNWEuNzUuNzUgMCAwIDEgMC0xLjVaTTYgMTUuMjVhLjc1Ljc1IDAgMCAxIC43NS0uNzVoMi41YS43NS43NSAwIDAgMSAwIDEuNWgtMi41YS43NS43NSAwIDAgMS0uNzUtLjc1WiIgLz48L3N2Zz4=)

**Wait, what's shadcn?**

No what, **who**! Shadcn is the author of a collection of pre-designed components known as `shadcn/ui`. Notice how we didn't say *library* there? Shadcn takes a different approach where components are added to your project's source code and are "owned" by you: once you add a component you're free to modify it to suit your needs!

## Getting started[](#getting-started) 

To begin with, we will:

- Set up a new [`vite`](https://vite.dev) project.
- Set up [shadcn/ui ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://ui.shadcn.com/) along with [Tailwind CSS ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://tailwindcss.com/).
- Add and configure React Flow.
- Create our custom React Flow components using the building blocks in our [UI components registry](/ui).

### Setting up a new vite project[](#setting-up-a-new-vite-project) 

npm

pnpm

yarn

bun

``` 
npm create vite@latest
```

``` 
npm create vite@latest
# couldn't auto-convert command
```

``` 
npm create vite@latest
# couldn't auto-convert command
```

``` 
bunx create-vite@latest
```

Vite is able to scaffold projects for many popular frameworks, but we only care about React! Additionally, make sure to set up a **TypeScript** project. React Flow's documentation is a mix of JavaScript and TypeScript, but for shadcn components TypeScript is *required*!

During the interactive setup, select `React` and `TypeScript`:

``` 
◇  Project name:
│  my-react-flow-app
│
◇  Select a framework:
│  React
│
◇  Select a variant:
│  TypeScript
│
◇  Use rolldown-vite (Experimental)?:
│  No
│
◇  Install with pnpm and start now?
│  Yes
│
◇  Scaffolding project in /Users/alessandro/src/xyflow/wip/component-style-test-2...
│
◇  Installing dependencies with pnpm...
```

### Setting up Tailwind CSS[](#setting-up-tailwind-css) 

All shadcn and React Flow components are styled with [Tailwind CSS ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://tailwindcss.com/), so we'll need to install that and a few other dependencies next.

We can follow the instructions in the [shadcn installation guide ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://ui.shadcn.com/docs/installation) to install shadcn and Tailwind CSS inside of a freshly scaffolded vite project.

npm

pnpm

yarn

bun

``` 
npm install tailwindcss @tailwindcss/vite
```

``` 
pnpm add tailwindcss @tailwindcss/vite
```

``` 
yarn add tailwindcss @tailwindcss/vite
```

``` 
bun add tailwindcss @tailwindcss/vite
```

It is now a lot simpler to set up Tailwind CSS in a vite project, and Tailwind 4 is configured completely in CSS. You can just replace the generated `src/index.css` file with this one line:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjIgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxNDMgMEwxOS44OTQzIDIxLjZMMTEuMjM3MSAyNEwyLjU4IDIxLjZMMC42NjAwMDQgMEgyMS44MTQzWk01LjQyNTcyIDEzLjcxNDNMNS43OTQyOSAxNy44OEwxMS4yMzcxIDE5LjQxNDNMMTYuNjYyOSAxNy45MTQzTDE3Ljg2MjkgNC40MTQyOUg0LjU5NDI5TDQuODM0MjkgNy4wNjI4NkgxNC45NTcxTDE0LjcxNzEgOS43OEg1LjA3NDI5TDUuMzA1NzIgMTIuNDI4NkgxNC40OTQzTDE0LjE4NTcgMTUuODU3MUwxMS4yMzcxIDE2LjY2MjlMOC4yOCAxNS44NjU3TDguMDgyODYgMTMuNzE0M0g1LjQyNTcyWiIgLz48L3N2Zz4=)[src/index.css]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
@import "tailwindcss";
```

### Importing Tailwind CSS as a Vite plugin[](#importing-tailwind-css-as-a-vite-plugin) 

Starting with [Tailwind CSS v4 ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://tailwindcss.com/blog/tailwindcss-v4), you can use the dedicated Vite plugin `@tailwindcss/vite` rather than the traditional PostCSS plugin. This plugin is configured in our `vite.config.ts` file, and makes things a lot simpler, both for us developers, and for the compilers.

We simply need to import the plugin and add it to the `plugins` array in our `vite.config.ts` file. We also need to add the `alias` property to the `resolve` object to tell Vite where to find our source files, as shadcn components use the `@` alias to refer to the `src` directory.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTAgMi42NjY2N1YyMS4zMzMzQzAgMjIuODA2NyAxLjE5MzMzIDI0IDIuNjY2NjcgMjRIMjEuMzMzM0MyMi44MDY3IDI0IDI0IDIyLjgwNjcgMjQgMjEuMzMzM1YyLjY2NjY3QzI0IDEuMTkzMzMgMjIuODA2NyAwIDIxLjMzMzMgMEgyLjY2NjY3QzEuMTkzMzMgMCAwIDEuMTkzMzMgMCAyLjY2NjY3Wk0xNC4yMjEzIDEyLjYwMTNIMTEuMzk3M1YyMS4zMzMzSDkuMTIxMzNWMTIuNjAxM0g2LjM1NlYxMC42NjY3SDE0LjIyMTNWMTIuNjAxM1pNMTQuNjY0IDIwLjgzNDdWMTguNUMxNC42NjQgMTguNSAxNS45Mzg3IDE5LjQ2MTMgMTcuNDY5MyAxOS40NjEzQzE5IDE5LjQ2MTMgMTguOTQgMTguNDYxMyAxOC45NCAxOC4zMjRDMTguOTQgMTYuODcyIDE0LjYwNTMgMTYuODcyIDE0LjYwNTMgMTMuNjU2QzE0LjYwNTMgOS4yODEzMyAyMC45MjEzIDExLjAwOCAyMC45MjEzIDExLjAwOEwyMC44NDI3IDEzLjA4NjdDMjAuODQyNyAxMy4wODY3IDE5Ljc4NCAxMi4zOCAxOC41ODY3IDEyLjM4QzE3LjM5MDcgMTIuMzggMTYuOTU4NyAxMi45NDkzIDE2Ljk1ODcgMTMuNTU3M0MxNi45NTg3IDE1LjEyNjcgMjEuMzMzMyAxNC45NjkzIDIxLjMzMzMgMTguMTI4QzIxLjMzMzMgMjIuOTkyIDE0LjY2NCAyMC44MzQ3IDE0LjY2NCAyMC44MzQ3WiIgLz48L3N2Zz4=)[vite.config.ts]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import path from "path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import  from "vite"
 
// https://vite.dev/config/
export default defineConfig(,
  },
})
```

### Importing the Tailwind CSS file[](#importing-the-tailwind-css-file) 

We now need to make sure that the only CSS file in our project is the Tailwind CSS file. In the generated `App.tsx`, you can safely remove the import of the `App.css` file, and remove everything else that is in the scaffolded `App.tsx` file.

To verify that Tailwind CSS is working, we can add a simple `div` and `h1` elements with Tailwind classes.

The updated `App.tsx` file should look like this:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[src/App.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
export function App() 
export default App;
```

And, the `main.tsx` file should look like this:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[src/main.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from 'react'
import  from 'react-dom/client'
import './index.css'
import App from './App.tsx'
 
createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

If you updated your `index.css` file and configured Vite to use the Tailwind CSS plugin, you should be able to run the project and see the "Hello World" message in your browser, in a nice, large, bold font.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik04IDEuNWMtMi4zNjMgMC00IDEuNjktNCAzLjc1IDAgLjk4NC40MjQgMS42MjUuOTg0IDIuMzA0bC4yMTQuMjUzYy4yMjMuMjY0LjQ3LjU1Ni42NzMuODQ4LjI4NC40MTEuNTM3Ljg5Ni42MjEgMS40OWEuNzUuNzUgMCAwIDEtMS40ODQuMjExYy0uMDQtLjI4Mi0uMTYzLS41NDctLjM3LS44NDdhOC40NTYgOC40NTYgMCAwIDAtLjU0Mi0uNjhjLS4wODQtLjEtLjE3My0uMjA1LS4yNjgtLjMyQzMuMjAxIDcuNzUgMi41IDYuNzY2IDIuNSA1LjI1IDIuNSAyLjMxIDQuODYzIDAgOCAwczUuNSAyLjMxIDUuNSA1LjI1YzAgMS41MTYtLjcwMSAyLjUtMS4zMjggMy4yNTktLjA5NS4xMTUtLjE4NC4yMi0uMjY4LjMxOS0uMjA3LjI0NS0uMzgzLjQ1My0uNTQxLjY4MS0uMjA4LjMtLjMzLjU2NS0uMzcuODQ3YS43NTEuNzUxIDAgMCAxLTEuNDg1LS4yMTJjLjA4NC0uNTkzLjMzNy0xLjA3OC42MjEtMS40ODkuMjAzLS4yOTIuNDUtLjU4NC42NzMtLjg0OC4wNzUtLjA4OC4xNDctLjE3My4yMTMtLjI1My41NjEtLjY3OS45ODUtMS4zMi45ODUtMi4zMDQgMC0yLjA2LTEuNjM3LTMuNzUtNC0zLjc1Wk01Ljc1IDEyaDQuNWEuNzUuNzUgMCAwIDEgMCAxLjVoLTQuNWEuNzUuNzUgMCAwIDEgMC0xLjVaTTYgMTUuMjVhLjc1Ljc1IDAgMCAxIC43NS0uNzVoMi41YS43NS43NSAwIDAgMSAwIDEuNWgtMi41YS43NS43NSAwIDAgMS0uNzUtLjc1WiIgLz48L3N2Zz4=)

The classes `w-screen` and `h-screen` are two examples of Tailwind's utility classes. If you're used to styling React apps using a different approach, you might find this a bit strange at first. You can think of Tailwind classes as supercharged inline styles: they're constrained to a set design system and you have access to responsive media queries or pseudo-classes like `hover` and `focus`.

### Setting up shadcn/ui[](#setting-up-shadcnui) 

Vite scaffolds some `tsconfig` files for us when generating a TypeScript project and we'll need to make some changes to these so the shadcn components can work correctly. The shadcn CLI is pretty clever (we'll get to that in a second) but it can't account for every project structure so instead shadcn components that depend on one another make use of TypeScript's import paths.

The current version of Vite splits TypeScript configuration into three files, two of which need to be edited. Add the `baseUrl` and `paths` properties to the `compilerOptions` section of the `tsconfig.json` and `tsconfig.app.json` files:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzAgMTAiIGZpbGw9ImN1cnJlbnRDb2xvciIgc3Ryb2tlPSJub25lIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48cGF0aCBkPSJNMzAgMFYxMEgyOEwyNiA0VjEwSDI0VjBIMjZMMjggNlYwSDMwWiIgLz48cGF0aCBkPSJNMjAuMzMzNSAxMEgxNy42NjY1QzE3LjIyNDcgOS45OTk1IDE2LjgwMTEgOS44MjM3NiAxNi40ODg3IDkuNTExMzRDMTYuMTc2MiA5LjE5ODkyIDE2LjAwMDUgOC43NzUzMyAxNiA4LjMzMzVWMS42NjY1QzE2LjAwMDUgMS4yMjQ2NyAxNi4xNzYyIDAuODAxMDgyIDE2LjQ4ODcgMC40ODg2NjJDMTYuODAxMSAwLjE3NjI0MSAxNy4yMjQ3IDAuMDAwNTAyODc2IDE3LjY2NjUgMEgyMC4zMzM1QzIwLjc3NTMgMC4wMDA1MDI4NzYgMjEuMTk4OSAwLjE3NjI0MSAyMS41MTEzIDAuNDg4NjYyQzIxLjgyMzggMC44MDEwODIgMjEuOTk5NSAxLjIyNDY3IDIyIDEuNjY2NVY4LjMzMzVDMjEuOTk5NSA4Ljc3NTMzIDIxLjgyMzggOS4xOTg5MiAyMS41MTEzIDkuNTExMzRDMjEuMTk4OSA5LjgyMzc2IDIwLjc3NTMgOS45OTk1IDIwLjMzMzUgMTBaTTE4IDhIMjBWMkgxOFY4WiIgLz48cGF0aCBkPSJNMTIuMzMzNSAxMEg4VjhIMTJWNkgxMEM5LjQ2OTczIDUuOTk5NDcgOC45NjEzMyA1Ljc4ODU5IDguNTg2MzcgNS40MTM2M0M4LjIxMTQxIDUuMDM4NjcgOC4wMDA1MyA0LjUzMDI3IDggNFYxLjY2NjVDOC4wMDA1IDEuMjI0NjcgOC4xNzYyNCAwLjgwMTA4MiA4LjQ4ODY2IDAuNDg4NjYyQzguODAxMDggMC4xNzYyNDEgOS4yMjQ2NyAwLjAwMDUwMjg3NiA5LjY2NjUgMEgxNFYySDEwVjRIMTJDMTIuNTMwMyA0LjAwMDUzIDEzLjAzODcgNC4yMTE0MSAxMy40MTM2IDQuNTg2MzdDMTMuNzg4NiA0Ljk2MTMzIDEzLjk5OTUgNS40Njk3MyAxNCA2VjguMzMzNUMxMy45OTk1IDguNzc1MzMgMTMuODIzOCA5LjE5ODkyIDEzLjUxMTMgOS41MTEzNEMxMy4xOTg5IDkuODIzNzYgMTIuNzc1MyA5Ljk5OTUgMTIuMzMzNSAxMFoiIC8+PHBhdGggZD0iTTQuMzMzNSAxMEgxLjY2NjVDMS4yMjQ2NyA5Ljk5OTUgMC44MDEwODIgOS44MjM3NiAwLjQ4ODY2MiA5LjUxMTM0QzAuMTc2MjQyIDkuMTk4OTIgMC4wMDA1MDI4NzYgOC43NzUzMyAwIDguMzMzNVY2SDJWOEg0VjBINlY4LjMzMzVDNS45OTk1IDguNzc1MzMgNS44MjM3NiA5LjE5ODkyIDUuNTExMzQgOS41MTEzNEM1LjE5ODkyIDkuODIzNzYgNC43NzUzMyA5Ljk5OTUgNC4zMzM1IDEwWiIgLz48L3N2Zz4=)[tsconfig.json]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 

  }
  // ...
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzAgMTAiIGZpbGw9ImN1cnJlbnRDb2xvciIgc3Ryb2tlPSJub25lIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48cGF0aCBkPSJNMzAgMFYxMEgyOEwyNiA0VjEwSDI0VjBIMjZMMjggNlYwSDMwWiIgLz48cGF0aCBkPSJNMjAuMzMzNSAxMEgxNy42NjY1QzE3LjIyNDcgOS45OTk1IDE2LjgwMTEgOS44MjM3NiAxNi40ODg3IDkuNTExMzRDMTYuMTc2MiA5LjE5ODkyIDE2LjAwMDUgOC43NzUzMyAxNiA4LjMzMzVWMS42NjY1QzE2LjAwMDUgMS4yMjQ2NyAxNi4xNzYyIDAuODAxMDgyIDE2LjQ4ODcgMC40ODg2NjJDMTYuODAxMSAwLjE3NjI0MSAxNy4yMjQ3IDAuMDAwNTAyODc2IDE3LjY2NjUgMEgyMC4zMzM1QzIwLjc3NTMgMC4wMDA1MDI4NzYgMjEuMTk4OSAwLjE3NjI0MSAyMS41MTEzIDAuNDg4NjYyQzIxLjgyMzggMC44MDEwODIgMjEuOTk5NSAxLjIyNDY3IDIyIDEuNjY2NVY4LjMzMzVDMjEuOTk5NSA4Ljc3NTMzIDIxLjgyMzggOS4xOTg5MiAyMS41MTEzIDkuNTExMzRDMjEuMTk4OSA5LjgyMzc2IDIwLjc3NTMgOS45OTk1IDIwLjMzMzUgMTBaTTE4IDhIMjBWMkgxOFY4WiIgLz48cGF0aCBkPSJNMTIuMzMzNSAxMEg4VjhIMTJWNkgxMEM5LjQ2OTczIDUuOTk5NDcgOC45NjEzMyA1Ljc4ODU5IDguNTg2MzcgNS40MTM2M0M4LjIxMTQxIDUuMDM4NjcgOC4wMDA1MyA0LjUzMDI3IDggNFYxLjY2NjVDOC4wMDA1IDEuMjI0NjcgOC4xNzYyNCAwLjgwMTA4MiA4LjQ4ODY2IDAuNDg4NjYyQzguODAxMDggMC4xNzYyNDEgOS4yMjQ2NyAwLjAwMDUwMjg3NiA5LjY2NjUgMEgxNFYySDEwVjRIMTJDMTIuNTMwMyA0LjAwMDUzIDEzLjAzODcgNC4yMTE0MSAxMy40MTM2IDQuNTg2MzdDMTMuNzg4NiA0Ljk2MTMzIDEzLjk5OTUgNS40Njk3MyAxNCA2VjguMzMzNUMxMy45OTk1IDguNzc1MzMgMTMuODIzOCA5LjE5ODkyIDEzLjUxMTMgOS41MTEzNEMxMy4xOTg5IDkuODIzNzYgMTIuNzc1MyA5Ljk5OTUgMTIuMzMzNSAxMFoiIC8+PHBhdGggZD0iTTQuMzMzNSAxMEgxLjY2NjVDMS4yMjQ2NyA5Ljk5OTUgMC44MDEwODIgOS44MjM3NiAwLjQ4ODY2MiA5LjUxMTM0QzAuMTc2MjQyIDkuMTk4OTIgMC4wMDA1MDI4NzYgOC43NzUzMyAwIDguMzMzNVY2SDJWOEg0VjBINlY4LjMzMzVDNS45OTk1IDguNzc1MzMgNS44MjM3NiA5LjE5ODkyIDUuNTExMzQgOS41MTEzNEM1LjE5ODkyIDkuODIzNzYgNC43NzUzMyA5Ljk5OTUgNC4zMzM1IDEwWiIgLz48L3N2Zz4=)[tsconfig.app.json]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 

    // ...
  }
}
```

Nice! Now we're ready to set up the `shadcn/ui` CLI and add our first components. Once the CLI is set up, we'll be able to add new components to our project with a single command - even if they have dependencies or need to modify existing files!

We can now run the following command to set up shadcn/ui in our project:

npm

pnpm

yarn

bun

``` 
npx shadcn@latest init
```

``` 
pnpm dlx shadcn@latest init
```

``` 
yarn dlx shadcn@latest init
```

``` 
bun x shadcn@latest init
```

The CLI will perform a few tasks, first it will identify your project's framework, tailwind version, and then ask you what color you would like to use as the base color for your project. It will then update your `index.css` file and generate a `components.json` file in the root of your project, which will be shadcn's main configuration points.

We can take all the default options for now

``` 
✔ Preflight checks.
✔ Verifying framework. Found Vite.
✔ Validating Tailwind CSS config. Found v4.
✔ Validating import alias.
✔ Which color would you like to use as the base color? › Neutral
✔ Writing components.json.
✔ Checking registry.
✔ Updating CSS variables in src/index.css
✔ Installing dependencies.
✔ Created 1 file:
  - src/lib/utils.ts

Success! Project initialization completed.
You may now add components.
```

## Installing React Flow and importing its CSS.[](#installing-react-flow-and-importing-its-css) 

Now we can install React Flow and import its CSS.

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

And then import its CSS in our `App.tsx` file:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[src/App.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import '@xyflow/react/dist/style.css';
 
export function App() 
export default App;
```

## Adding your first components[](#adding-your-first-components) 

To demonstrate how powerful shadcn can be, let's dive right into making a new **React Flow** app! Now everything is set up, we can add the [`<BaseNode />`](/ui/components/base-node) component with a single command:

npm

pnpm

yarn

bun

``` 
npx shadcn@latest add https://ui.reactflow.dev/base-node
```

``` 
pnpm dlx shadcn@latest add https://ui.reactflow.dev/base-node
```

``` 
yarn dlx shadcn@latest add https://ui.reactflow.dev/base-node
```

``` 
bun x shadcn@latest add https://ui.reactflow.dev/base-node
```

This command will generate a new file `src/components/base-node.tsx`, and install the necessary dependencies.

That `<BaseNode />` component is not a React Flow node directly. Instead, as the name implies, it's a base that many of our other nodes build upon. It also comes with additional components that you can use to provide a header and content for your nodes. These components are:

- `<BaseNodeHeader />`
- `<BaseNodeHeaderTitle />`
- `<BaseNodeContent />`
- `<BaseNodeFooter />`

You can use it to have a unified style for all of your nodes as well. Let's see what it looks like by updating our `App.tsx` file:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[src/App.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import '@xyflow/react/dist/style.css';
 
import  from "@/components/base-node";
 
function App() 
 
export default App;
```

Ok, not super exciting...

<figure class="my-8 mx-0">
<img src="/_next/image?url=%2Fimg%2Ftutorials%2Fcomponents%2Fbase-node.png&amp;w=3840&amp;q=75" class="w-full h-auto rounded-xl" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" sizes="100vw" srcset="/_next/image?url=%2Fimg%2Ftutorials%2Fcomponents%2Fbase-node.png&amp;w=640&amp;q=75 640w, /_next/image?url=%2Fimg%2Ftutorials%2Fcomponents%2Fbase-node.png&amp;w=750&amp;q=75 750w, /_next/image?url=%2Fimg%2Ftutorials%2Fcomponents%2Fbase-node.png&amp;w=828&amp;q=75 828w, /_next/image?url=%2Fimg%2Ftutorials%2Fcomponents%2Fbase-node.png&amp;w=1080&amp;q=75 1080w, /_next/image?url=%2Fimg%2Ftutorials%2Fcomponents%2Fbase-node.png&amp;w=1200&amp;q=75 1200w, /_next/image?url=%2Fimg%2Ftutorials%2Fcomponents%2Fbase-node.png&amp;w=1920&amp;q=75 1920w, /_next/image?url=%2Fimg%2Ftutorials%2Fcomponents%2Fbase-node.png&amp;w=2048&amp;q=75 2048w, /_next/image?url=%2Fimg%2Ftutorials%2Fcomponents%2Fbase-node.png&amp;w=3840&amp;q=75 3840w" width="0" height="0" alt="A screenshot of a simple React application. It renders one element, a rounded container with a blue border and the text &#39;Hi! 👋&#39; inside." />
</figure>

The `<BaseNode />` component is one of the most used components in our [UI components registry](/ui). Some components may use it internally, to create custom nodes with a consistent style, while some other components can be used in combination with it to create more complex nodes.

For example, let's add the `<NodeTooltip />` component to our project, to display a tooltip when hovering over a node.

npm

pnpm

yarn

bun

``` 
npx shadcn@latest add https://ui.reactflow.dev/node-tooltip
```

``` 
pnpm dlx shadcn@latest add https://ui.reactflow.dev/node-tooltip
```

``` 
yarn dlx shadcn@latest add https://ui.reactflow.dev/node-tooltip
```

``` 
bun x shadcn@latest add https://ui.reactflow.dev/node-tooltip
```

And we'll update our `App.tsx` file to render a proper flow. We'll use the same basic setup as most of our examples so we won't break down the individual pieces here. If you're still new to React Flow and want to learn a bit more about how to set up a basic flow from scratch, check out our [quickstart guide](/learn).

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[src/App.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from "@xyflow/react";
 
import "@xyflow/react/dist/style.css";
 
import  from "@/components/base-node";
import  from "@/components/node-tooltip";
 
function Tooltip() >
        Hidden Content
      </NodeTooltipContent>
      <BaseNode>
        <BaseNodeContent>
          <NodeTooltipTrigger>Hover</NodeTooltipTrigger>
        </BaseNodeContent>
      </BaseNode>
    </NodeTooltip>
  );
}
 
const nodeTypes = ;
 
const initialNodes: Node[] = [
  ,
    data: ,
    type: "tooltip",
  },
];
 
function Flow() 
        nodeTypes=
        onNodesChange=
        fitView
      />
    </div>
  );
}
 
export default function App() 
```

And would you look at that, the tooltip node we added automatically uses the `<BaseNode />` component we customized!

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

## Moving fast and making things[](#moving-fast-and-making-things) 

Now we've got a basic understanding of how shadcn/ui and the CLI works, we can begin to see how easy it is to add new components and build out a flow. To see everything React Flow Components has to offer let's build out a simple calculator flow.

First let's remove the `<NodeTooltip />` and undo our changes to `<BaseNode />`. In addition to pre-made nodes, React Flow UI also contains building blocks for creating your own custom nodes. To see them, we'll add the `labeled-handle` component:

npm

pnpm

yarn

bun

``` 
npx shadcn@latest add https://ui.reactflow.dev/labeled-handle
```

``` 
pnpm dlx shadcn@latest add https://ui.reactflow.dev/labeled-handle
```

``` 
yarn dlx shadcn@latest add https://ui.reactflow.dev/labeled-handle
```

``` 
bun x shadcn@latest add https://ui.reactflow.dev/labeled-handle
```

### The Number Node[](#the-number-node) 

The first node we'll create is a simple number node with some buttons to increment and decrement the value and a handle to connect it to other nodes. Create a folder `src/components/nodes` and then add a new file `src/components/nodes/num-node.tsx`.

We need to install the following `shadcn/ui` components:

npm

pnpm

yarn

bun

``` 
npx shadcn@latest add dropdown-menu button
```

``` 
pnpm dlx shadcn@latest add dropdown-menu button
```

``` 
yarn dlx shadcn@latest add dropdown-menu button
```

``` 
bun x shadcn@latest add dropdown-menu button
```

Now we can start building the node. We will need to access the `updateNodeData` function to update the node's data and the `setNodes` function to delete the node, from the `useReactFlow` hook. The hook helps us make self-contained components that can be used in other parts of our application, while still giving us quick access to React Flow's state and functions.

We will need to make four callbacks, to handle the different actions that can be performed on the node.

- Reset the node's value to 0
- Delete the node
- Increment the node's value by 1
- Decrement the node's value by 1

We will also need to access the node's data to get the current value and update it.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[src/components/nodes/num-node.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from '@xyflow/react';
import  from 'react';
 
import  from '../base-node';
import  from '../labeled-handle';
 
import  from 'lucide-react';
import  from '../ui/button';
import  from '../ui/dropdown-menu';
 
export type NumNode = Node<>;
 
export function NumNode(: NodeProps<NumNode>)  = useReactFlow();
 
  const handleReset = useCallback(() => );
  }, [id, updateNodeData]);
 
  const handleDelete = useCallback(() => , [id, setNodes]);
 
  const handleIncr = useCallback(() => );
  }, [id, data.value, updateNodeData]);
 
  const handleDecr = useCallback(() => );
  }, [id, data.value, updateNodeData]);
 
  return (
    <BaseNode>
      <BaseNodeHeader className="border-b">
        <BaseNodeHeaderTitle>Num</BaseNodeHeaderTitle>
 
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button
              variant="ghost"
              className="nodrag p-1"
              aria-label="Node Actions"
              title="Node Actions"
            >
              <EllipsisVertical className="size-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent>
            <DropdownMenuLabel className="font-bold">Node Actions</DropdownMenuLabel>
            <DropdownMenuItem onSelect=>Reset</DropdownMenuItem>
            <DropdownMenuItem onSelect=>Delete</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </BaseNodeHeader>
 
      <BaseNodeContent>
        <div className="flex gap-2 items-center">
          <Button onClick=>-</Button>
          <pre></pre>
          <Button onClick=>+</Button>
        </div>
      </BaseNodeContent>
 
      <BaseNodeFooter className="bg-gray-100 items-end px-0 py-1 w-full  rounded-b-md">
        <LabeledHandle title="out" type="source" position= />
      </BaseNodeFooter>
    </BaseNode>
  );
}
```

### The Sum Node[](#the-sum-node) 

The second node we can create is a simple sum node that adds the values of the two input nodes. Create a new file `src/components/nodes/sum-node.tsx` and paste the following into it:

Particularly, we will need to access the `getNodeConnections` function to get the values of the two connected input nodes and the `updateNodeData` function to update the node's data with the sum of the two input nodes inside of a `useEffect` hook, whenever one of the values of the input nodes changes.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[src/components/nodes/sum-node.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from '@xyflow/react';
import  from 'react';
 
import  from '../base-node';
import  from '../labeled-handle';
import  from '../ui/dropdown-menu';
import  from 'lucide-react';
import  from '../ui/button';
 
export type SumNode = Node<>;
 
export function SumNode(: NodeProps<SumNode>)  = useReactFlow();
  const  = useStore((state) => (),
      state.nodeLookup,
    ),
    y: getHandleValue(
      getNodeConnections(),
      state.nodeLookup,
    ),
  }));
 
  const handleDelete = useCallback(() => , [id, setNodes, setEdges]);
 
  useEffect(() => );
  }, [x, y]);
 
  return (
    <BaseNode className="w-32">
      <BaseNodeHeader className="border-b">
        <BaseNodeHeaderTitle>Sum</BaseNodeHeaderTitle>
 
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button
              variant="ghost"
              className="nodrag p-1"
              aria-label="Node Actions"
              title="Node Actions"
            >
              <EllipsisVertical className="size-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent>
            <DropdownMenuLabel className="font-bold">Node Actions</DropdownMenuLabel>
            <DropdownMenuItem onSelect=>Delete</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </BaseNodeHeader>
 
      <BaseNodeContent className="px-0">
        <LabeledHandle title="x" id="x" type="target" position= />
        <LabeledHandle title="y" id="y" type="target" position= />
      </BaseNodeContent>
      <BaseNodeFooter className="bg-gray-100 items-end px-0 py-1 w-full rounded-b-md">
        <LabeledHandle title="out" type="source" position= />
      </BaseNodeFooter>
    </BaseNode>
  );
}
 
function getHandleValue(
  connections: Array<>,
  lookup: Map<string, Node<any>>,
) ) => , 0);
}
```

### The Data Edge[](#the-data-edge) 

React Flow UI doesn't just provide components for building nodes. We also provide pre-built edges and other UI elements you can drop into your flows for quick building.

To better visualize data in our calculator flow, let's pull in the `data-edge` component. This edge renders a field from the source node's data object as a label on the edge itself. Add the `data-edge` component to your project:

npm

pnpm

yarn

bun

``` 
npx shadcn@latest add https://ui.reactflow.dev/data-edge
```

``` 
pnpm dlx shadcn@latest add https://ui.reactflow.dev/data-edge
```

``` 
yarn dlx shadcn@latest add https://ui.reactflow.dev/data-edge
```

``` 
bun x shadcn@latest add https://ui.reactflow.dev/data-edge
```

The `<DataEdge />` component works by looking up a field from its source node's `data` object. We've been storing the value of each node in our calculator field in a `"value"` property so we'll update our `edgeType` object to include the new `data-edge` and we'll update the `onConnect` handler to create a new edge of this type, making sure to set the edge's `data` object correctly:

### The Flow[](#the-flow) 

Now we can put everything together and create our flow.

We will start by defining the custom node and edge types, and the initial nodes and edges that will be displayed in our app.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[src/App.tsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import React,  from 'react';
import  from '@xyflow/react';
 
import  from './components/nodes/num-node';
import  from './components/nodes/sum-node';
 
import  from './components/data-edge';
 
import '@xyflow/react/dist/style.css';
 
const nodeTypes = ;
 
const initialNodes: Node[] = [
  , position:  },
  , position:  },
  , position:  },
  , position:  },
  , position:  },
];
 
const edgeTypes = ;
 
const initialEdges: Edge[] = [
  ,
    source: 'a',
    target: 'c',
    targetHandle: 'x',
  },
  ,
    source: 'b',
    target: 'c',
    targetHandle: 'y',
  },
  ,
    source: 'c',
    target: 'e',
    targetHandle: 'x',
  },
  ,
    source: 'd',
    target: 'e',
    targetHandle: 'y',
  },
];
 
function Flow() , ...params }, edges),
      );
    },
    [setEdges],
  );
 
  return (
    <div className="h-screen w-screen p-8 bg-gray-50 rounded-xl">
      <ReactFlow
        nodes=
        edges=
        onNodesChange=
        onEdgesChange=
        onConnect=
        nodeTypes=
        edgeTypes=
        fitView
      />
    </div>
  );
}
 
export function App() 
```

Putting everything together we end up with quite a capable little calculator!

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

You could continue to improve this flow by adding nodes to perform other operations or to take user input using additional components from the [shadcn/ui registry ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://ui.shadcn.com/docs/components/slider). In fact, keep your eyes peeled soon for a follow-up to this guide where we'll show a complete application built using React Flow Components [👀].

## Wrapping up[](#wrapping-up) 

In just a short amount of time we've managed to build out a fairly complete flow using the components and building blocks provided by shadcn React Flow Components. We've learned:

- How to use building blocks like the [`<BaseNodeHeader />`](/ui/components/base-node) and [`<LabeledHandle />`](/ui/components/labeled-handle) components to build our own custom nodes without starting from scratch.

- That React Flow UI also provides custom edges like the [`<DataEdge />`](/ui/components/data-edge) to drop into our applications.

And thanks to the power of Tailwind, tweaking the visual style of these components is as simple as editing the variables in your CSS file.

That's all for now! You can see all the components we currently have available over on the [UI docs page](/ui). If you have any suggestions or requests for new components we'd love to hear about them. Or perhaps you're already starting to build something with shadcn and React Flow UI. Either way make sure you let us know on our [Discord server ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://discord.com/invite/RVmnytFmGW) or on [Twitter ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://twitter.com/xyflowdev)!

### Get Pro examples, prioritized bug reports, 1:1 support from the maintainers, and more with React Flow Pro 

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0idy01IGgtNSBtci0xIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik05LjgxMyAxNS45MDQgOSAxOC43NWwtLjgxMy0yLjg0NmE0LjUgNC41IDAgMCAwLTMuMDktMy4wOUwyLjI1IDEybDIuODQ2LS44MTNhNC41IDQuNSAwIDAgMCAzLjA5LTMuMDlMOSA1LjI1bC44MTMgMi44NDZhNC41IDQuNSAwIDAgMCAzLjA5IDMuMDlMMTUuNzUgMTJsLTIuODQ2LjgxM2E0LjUgNC41IDAgMCAwLTMuMDkgMy4wOVpNMTguMjU5IDguNzE1IDE4IDkuNzVsLS4yNTktMS4wMzVhMy4zNzUgMy4zNzUgMCAwIDAtMi40NTUtMi40NTZMMTQuMjUgNmwxLjAzNi0uMjU5YTMuMzc1IDMuMzc1IDAgMCAwIDIuNDU1LTIuNDU2TDE4IDIuMjVsLjI1OSAxLjAzNWEzLjM3NSAzLjM3NSAwIDAgMCAyLjQ1NiAyLjQ1NkwyMS43NSA2bC0xLjAzNS4yNTlhMy4zNzUgMy4zNzUgMCAwIDAtMi40NTYgMi40NTZaTTE2Ljg5NCAyMC41NjcgMTYuNSAyMS43NWwtLjM5NC0xLjE4M2EyLjI1IDIuMjUgMCAwIDAtMS40MjMtMS40MjNMMTMuNSAxOC43NWwxLjE4My0uMzk0YTIuMjUgMi4yNSAwIDAgMCAxLjQyMy0xLjQyM2wuMzk0LTEuMTgzLjM5NCAxLjE4M2EyLjI1IDIuMjUgMCAwIDAgMS40MjMgMS40MjNsMS4xODMuMzk0LTEuMTgzLjM5NGEyLjI1IDIuMjUgMCAwIDAtMS40MjMgMS40MjNaIiAvPjwvc3ZnPg==)React Flow Pro](https://reactflow.dev/pro)