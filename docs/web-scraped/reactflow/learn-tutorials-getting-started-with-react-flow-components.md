# Source: https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components

Title: Getting started with React Flow UI - React Flow

URL Source: https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components

Markdown Content:
_**Update November 2025**: We have updated the tutorial to use the latest version of shadcn/ui, on React 19 and Tailwind 4!_

_**Update July 2025**: “React Flow UI” was formerly known as “React Flow Components”. We renamed it because it now includes both components and templates. Additionally, since it’s built on shadcn/ui, the “UI” naming makes it easier for developers to recognize the connection and understand what we offer._

Recently, we launched an exciting new addition to our open-source roster: React Flow UI (Previously known as React Flow Components). These are pre-built nodes, edges, and other ui elements that you can quickly add to your React Flow applications to get up and running. The catch is these components are built on top of [shadcn/ui](https://ui.shadcn.com/) and the shadcn CLI.

We’ve previously written about our experience and what led us to choosing shadcn over on the [xyflow blog](https://xyflow.com/blog/react-flow-components), but in this tutorial we’re going to focus on how to get started from scratch with shadcn, Tailwind CSS, and React Flow Components.

**Wait, what’s shadcn?**

No what, **who**! Shadcn is the author of a collection of pre-designed components known as `shadcn/ui`. Notice how we didn’t say _library_ there? Shadcn takes a different approach where components are added to your project’s source code and are “owned” by you: once you add a component you’re free to modify it to suit your needs!

Getting started[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#getting-started)
-------------------------------------------------------------------------------------------------------------------

To begin with, we will:

* Set up a new [`vite`](https://vite.dev/) project.
* Set up [shadcn/ui](https://ui.shadcn.com/) along with [Tailwind CSS](https://tailwindcss.com/).
* Add and configure React Flow.
* Create our custom React Flow components using the building blocks in our [UI components registry](https://reactflow.dev/ui).

### Setting up a new vite project[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#setting-up-a-new-vite-project)

`npm create vite@latest`

Vite is able to scaffold projects for many popular frameworks, but we only care about React! Additionally, make sure to set up a **TypeScript** project. React Flow’s documentation is a mix of JavaScript and TypeScript, but for shadcn components TypeScript is _required_!

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

### Setting up Tailwind CSS[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#setting-up-tailwind-css)

All shadcn and React Flow components are styled with [Tailwind CSS](https://tailwindcss.com/), so we’ll need to install that and a few other dependencies next.

We can follow the instructions in the [shadcn installation guide](https://ui.shadcn.com/docs/installation) to install shadcn and Tailwind CSS inside of a freshly scaffolded vite project.

`npm install tailwindcss @tailwindcss/vite`

It is now a lot simpler to set up Tailwind CSS in a vite project, and Tailwind 4 is configured completely in CSS. You can just replace the generated `src/index.css` file with this one line:

src/index.css

`@import "tailwindcss";`

### Importing Tailwind CSS as a Vite plugin[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#importing-tailwind-css-as-a-vite-plugin)

Starting with [Tailwind CSS v4](https://tailwindcss.com/blog/tailwindcss-v4), you can use the dedicated Vite plugin `@tailwindcss/vite` rather than the traditional PostCSS plugin. This plugin is configured in our `vite.config.ts` file, and makes things a lot simpler, both for us developers, and for the compilers.

We simply need to import the plugin and add it to the `plugins` array in our `vite.config.ts` file. We also need to add the `alias` property to the `resolve` object to tell Vite where to find our source files, as shadcn components use the `@` alias to refer to the `src` directory.

vite.config.ts

```
import path from "path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"
 
// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})
```

### Importing the Tailwind CSS file[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#importing-the-tailwind-css-file)

We now need to make sure that the only CSS file in our project is the Tailwind CSS file. In the generated `App.tsx`, you can safely remove the import of the `App.css` file, and remove everything else that is in the scaffolded `App.tsx` file.

To verify that Tailwind CSS is working, we can add a simple `div` and `h1` elements with Tailwind classes.

The updated `App.tsx` file should look like this:

src/App.tsx

```
export function App() {
  return (
    <div className="w-screen h-screen p-8">
      <h1 className="text-2xl font-bold">Hello World</h1>
    </div>
  );
}
export default App;
```

And, the `main.tsx` file should look like this:

src/main.tsx

```
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
 
createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

If you updated your `index.css` file and configured Vite to use the Tailwind CSS plugin, you should be able to run the project and see the “Hello World” message in your browser, in a nice, large, bold font.

The classes `w-screen` and `h-screen` are two examples of Tailwind’s utility classes. If you’re used to styling React apps using a different approach, you might find this a bit strange at first. You can think of Tailwind classes as supercharged inline styles: they’re constrained to a set design system and you have access to responsive media queries or pseudo-classes like `hover` and `focus`.

### Setting up shadcn/ui[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#setting-up-shadcnui)

Vite scaffolds some `tsconfig` files for us when generating a TypeScript project and we’ll need to make some changes to these so the shadcn components can work correctly. The shadcn CLI is pretty clever (we’ll get to that in a second) but it can’t account for every project structure so instead shadcn components that depend on one another make use of TypeScript’s import paths.

The current version of Vite splits TypeScript configuration into three files, two of which need to be edited. Add the `baseUrl` and `paths` properties to the `compilerOptions` section of the `tsconfig.json` and `tsconfig.app.json` files:

tsconfig.json

```
{
  // ...
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
  // ...
}
```

tsconfig.app.json

```
{
  "compilerOptions": {
    // ...
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
    // ...
  }
}
```

Nice! Now we’re ready to set up the `shadcn/ui` CLI and add our first components. Once the CLI is set up, we’ll be able to add new components to our project with a single command - even if they have dependencies or need to modify existing files!

We can now run the following command to set up shadcn/ui in our project:

`npx shadcn@latest init`

The CLI will perform a few tasks, first it will identify your project’s framework, tailwind version, and then ask you what color you would like to use as the base color for your project. It will then update your `index.css` file and generate a `components.json` file in the root of your project, which will be shadcn’s main configuration points.

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

Installing React Flow and importing its CSS.[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#installing-react-flow-and-importing-its-css)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now we can install React Flow and import its CSS.

`npm install @xyflow/react`

And then import its CSS in our `App.tsx` file:

src/App.tsx

```
import '@xyflow/react/dist/style.css';
 
export function App() {
  return (
    <div className="w-screen h-screen p-8">
      <h1 className="text-2xl font-bold">Hello World</h1>
    </div>
  );
}
export default App;
```

Adding your first components[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#adding-your-first-components)
---------------------------------------------------------------------------------------------------------------------------------------------

To demonstrate how powerful shadcn can be, let’s dive right into making a new **React Flow** app! Now everything is set up, we can add the [`<BaseNode />`](https://reactflow.dev/ui/components/base-node) component with a single command:

`npx shadcn@latest add https://ui.reactflow.dev/base-node`

This command will generate a new file `src/components/base-node.tsx`, and install the necessary dependencies.

That `<BaseNode />` component is not a React Flow node directly. Instead, as the name implies, it’s a base that many of our other nodes build upon. It also comes with additional components that you can use to provide a header and content for your nodes. These components are:

* `<BaseNodeHeader />`
* `<BaseNodeHeaderTitle />`
* `<BaseNodeContent />`
* `<BaseNodeFooter />`

You can use it to have a unified style for all of your nodes as well. Let’s see what it looks like by updating our `App.tsx` file:

src/App.tsx

```
import '@xyflow/react/dist/style.css';
 
import {
  BaseNode,
  BaseNodeContent,
  BaseNodeHeader,
  BaseNodeHeaderTitle,
} from "@/components/base-node";
 
function App() {
  return (
    <div className="w-screen h-screen p-8">
      <BaseNode>
        <BaseNodeHeader>
          <BaseNodeHeaderTitle>Base Node</BaseNodeHeaderTitle>
        </BaseNodeHeader>
        <BaseNodeContent>
          This is a base node component that can be used to build other nodes.
        </BaseNodeContent>
      </BaseNode>
    </div>
  );
}
 
export default App;
```

Ok, not super exciting…

![Image 1: A screenshot of a simple React application. It renders one element, a rounded container with a blue border and the text 'Hi! 👋' inside.](https://reactflow.dev/_next/image?url=%2Fimg%2Ftutorials%2Fcomponents%2Fbase-node.png&w=3840&q=75)
The `<BaseNode />` component is one of the most used components in our [UI components registry](https://reactflow.dev/ui). Some components may use it internally, to create custom nodes with a consistent style, while some other components can be used in combination with it to create more complex nodes.

For example, let’s add the `<NodeTooltip />` component to our project, to display a tooltip when hovering over a node.

`npx shadcn@latest add https://ui.reactflow.dev/node-tooltip`

And we’ll update our `App.tsx` file to render a proper flow. We’ll use the same basic setup as most of our examples so we won’t break down the individual pieces here. If you’re still new to React Flow and want to learn a bit more about how to set up a basic flow from scratch, check out our [quickstart guide](https://reactflow.dev/learn).

src/App.tsx

```
import { Position, ReactFlow, useNodesState, type Node } from "@xyflow/react";
 
import "@xyflow/react/dist/style.css";
 
import { BaseNode, BaseNodeContent } from "@/components/base-node";
import {
  NodeTooltip,
  NodeTooltipContent,
  NodeTooltipTrigger,
} from "@/components/node-tooltip";
 
function Tooltip() {
  return (
    <NodeTooltip>
      <NodeTooltipContent position={Position.Top}>
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
 
const nodeTypes = {
  tooltip: Tooltip,
};
 
const initialNodes: Node[] = [
  {
    id: "1",
    position: { x: 0, y: 0 },
    data: {},
    type: "tooltip",
  },
];
 
function Flow() {
  const [nodes, , onNodesChange] = useNodesState(initialNodes);
 
  return (
    <div className="h-screen w-screen p-8 bg-gray-50 rounded-xl">
      <ReactFlow
        nodes={nodes}
        nodeTypes={nodeTypes}
        onNodesChange={onNodesChange}
        fitView
      />
    </div>
  );
}
 
export default function App() {
  return <Flow />;
}
```

And would you look at that, the tooltip node we added automatically uses the `<BaseNode />` component we customized!

Moving fast and making things[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#moving-fast-and-making-things)
-----------------------------------------------------------------------------------------------------------------------------------------------

Now we’ve got a basic understanding of how shadcn/ui and the CLI works, we can begin to see how easy it is to add new components and build out a flow. To see everything React Flow Components has to offer let’s build out a simple calculator flow.

First let’s remove the `<NodeTooltip />` and undo our changes to `<BaseNode />`. In addition to pre-made nodes, React Flow UI also contains building blocks for creating your own custom nodes. To see them, we’ll add the `labeled-handle` component:

`npx shadcn@latest add https://ui.reactflow.dev/labeled-handle`

### The Number Node[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#the-number-node)

The first node we’ll create is a simple number node with some buttons to increment and decrement the value and a handle to connect it to other nodes. Create a folder `src/components/nodes` and then add a new file `src/components/nodes/num-node.tsx`.

We need to install the following `shadcn/ui` components:

`npx shadcn@latest add dropdown-menu button`

Now we can start building the node. We will need to access the `updateNodeData` function to update the node’s data and the `setNodes` function to delete the node, from the `useReactFlow` hook. The hook helps us make self-contained components that can be used in other parts of our application, while still giving us quick access to React Flow’s state and functions.

We will need to make four callbacks, to handle the different actions that can be performed on the node.

* Reset the node’s value to 0
* Delete the node
* Increment the node’s value by 1
* Decrement the node’s value by 1

We will also need to access the node’s data to get the current value and update it.

src/components/nodes/num-node.tsx

```
import { type Node, type NodeProps, Position, useReactFlow } from '@xyflow/react';
import { useCallback } from 'react';
 
import {
  BaseNode,
  BaseNodeContent,
  BaseNodeFooter,
  BaseNodeHeader,
  BaseNodeHeaderTitle,
} from '../base-node';
import { LabeledHandle } from '../labeled-handle';
 
import { EllipsisVertical } from 'lucide-react';
import { Button } from '../ui/button';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuTrigger,
} from '../ui/dropdown-menu';
 
export type NumNode = Node<{
  value: number;
}>;
 
export function NumNode({ id, data }: NodeProps<NumNode>) {
  const { updateNodeData, setNodes } = useReactFlow();
 
  const handleReset = useCallback(() => {
    updateNodeData(id, { value: 0 });
  }, [id, updateNodeData]);
 
  const handleDelete = useCallback(() => {
    setNodes((nodes) => nodes.filter((node) => node.id !== id));
  }, [id, setNodes]);
 
  const handleIncr = useCallback(() => {
    updateNodeData(id, { value: data.value + 1 });
  }, [id, data.value, updateNodeData]);
 
  const handleDecr = useCallback(() => {
    updateNodeData(id, { value: data.value - 1 });
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
            <DropdownMenuItem onSelect={handleReset}>Reset</DropdownMenuItem>
            <DropdownMenuItem onSelect={handleDelete}>Delete</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </BaseNodeHeader>
 
      <BaseNodeContent>
        <div className="flex gap-2 items-center">
          <Button onClick={handleDecr}>-</Button>
          <pre>{String(data.value).padStart(3, ' ')}</pre>
          <Button onClick={handleIncr}>+</Button>
        </div>
      </BaseNodeContent>
 
      <BaseNodeFooter className="bg-gray-100 items-end px-0 py-1 w-full  rounded-b-md">
        <LabeledHandle title="out" type="source" position={Position.Right} />
      </BaseNodeFooter>
    </BaseNode>
  );
}
```

### The Sum Node[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#the-sum-node)

The second node we can create is a simple sum node that adds the values of the two input nodes. Create a new file `src/components/nodes/sum-node.tsx` and paste the following into it:

Particularly, we will need to access the `getNodeConnections` function to get the values of the two connected input nodes and the `updateNodeData` function to update the node’s data with the sum of the two input nodes inside of a `useEffect` hook, whenever one of the values of the input nodes changes.

src/components/nodes/sum-node.tsx

```
import {
  type Node,
  type NodeProps,
  Position,
  useReactFlow,
  useStore,
} from '@xyflow/react';
import { useCallback, useEffect } from 'react';
 
import {
  BaseNode,
  BaseNodeContent,
  BaseNodeFooter,
  BaseNodeHeader,
  BaseNodeHeaderTitle,
} from '../base-node';
import { LabeledHandle } from '../labeled-handle';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuTrigger,
} from '../ui/dropdown-menu';
import { EllipsisVertical } from 'lucide-react';
import { Button } from '../ui/button';
 
export type SumNode = Node<{
  value: number;
}>;
 
export function SumNode({ id }: NodeProps<SumNode>) {
  const { updateNodeData, getNodeConnections, setNodes, setEdges } = useReactFlow();
  const { x, y } = useStore((state) => ({
    x: getHandleValue(
      getNodeConnections({ nodeId: id, handleId: 'x', type: 'target' }),
      state.nodeLookup,
    ),
    y: getHandleValue(
      getNodeConnections({ nodeId: id, handleId: 'y', type: 'target' }),
      state.nodeLookup,
    ),
  }));
 
  const handleDelete = useCallback(() => {
    setNodes((nodes) => nodes.filter((node) => node.id !== id));
    setEdges((edges) => edges.filter((edge) => edge.source !== id));
  }, [id, setNodes, setEdges]);
 
  useEffect(() => {
    updateNodeData(id, { value: x + y });
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
            <DropdownMenuItem onSelect={handleDelete}>Delete</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </BaseNodeHeader>
 
      <BaseNodeContent className="px-0">
        <LabeledHandle title="x" id="x" type="target" position={Position.Left} />
        <LabeledHandle title="y" id="y" type="target" position={Position.Left} />
      </BaseNodeContent>
      <BaseNodeFooter className="bg-gray-100 items-end px-0 py-1 w-full rounded-b-md">
        <LabeledHandle title="out" type="source" position={Position.Right} />
      </BaseNodeFooter>
    </BaseNode>
  );
}
 
function getHandleValue(
  connections: Array<{ source: string }>,
  lookup: Map<string, Node<any>>,
) {
  return connections.reduce((acc, { source }) => {
    const node = lookup.get(source)!;
    const value = node.data.value;
 
    return typeof value === 'number' ? acc + value : acc;
  }, 0);
}
```

### The Data Edge[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#the-data-edge)

React Flow UI doesn’t just provide components for building nodes. We also provide pre-built edges and other UI elements you can drop into your flows for quick building.

To better visualize data in our calculator flow, let’s pull in the `data-edge` component. This edge renders a field from the source node’s data object as a label on the edge itself. Add the `data-edge` component to your project:

`npx shadcn@latest add https://ui.reactflow.dev/data-edge`

The `<DataEdge />` component works by looking up a field from its source node’s `data` object. We’ve been storing the value of each node in our calculator field in a `"value"` property so we’ll update our `edgeType` object to include the new `data-edge` and we’ll update the `onConnect` handler to create a new edge of this type, making sure to set the edge’s `data` object correctly:

### The Flow[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#the-flow)

Now we can put everything together and create our flow.

We will start by defining the custom node and edge types, and the initial nodes and edges that will be displayed in our app.

src/App.tsx

```
import React, { useCallback } from 'react';
import {
  ReactFlow,
  type Node,
  type Edge,
  type OnConnect,
  addEdge,
  useNodesState,
  useEdgesState,
} from '@xyflow/react';
 
import { NumNode } from './components/nodes/num-node';
import { SumNode } from './components/nodes/sum-node';
 
import { DataEdge } from './components/data-edge';
 
import '@xyflow/react/dist/style.css';
 
const nodeTypes = {
  num: NumNode,
  sum: SumNode,
};
 
const initialNodes: Node[] = [
  { id: 'a', type: 'num', data: { value: 0 }, position: { x: 0, y: 0 } },
  { id: 'b', type: 'num', data: { value: 0 }, position: { x: 0, y: 200 } },
  { id: 'c', type: 'sum', data: { value: 0 }, position: { x: 300, y: 100 } },
  { id: 'd', type: 'num', data: { value: 0 }, position: { x: 0, y: 400 } },
  { id: 'e', type: 'sum', data: { value: 0 }, position: { x: 600, y: 400 } },
];
 
const edgeTypes = {
  data: DataEdge,
};
 
const initialEdges: Edge[] = [
  {
    id: 'a->c',
    type: 'data',
    data: { key: 'value' },
    source: 'a',
    target: 'c',
    targetHandle: 'x',
  },
  {
    id: 'b->c',
    type: 'data',
    data: { key: 'value' },
    source: 'b',
    target: 'c',
    targetHandle: 'y',
  },
  {
    id: 'c->e',
    type: 'data',
    data: { key: 'value' },
    source: 'c',
    target: 'e',
    targetHandle: 'x',
  },
  {
    id: 'd->e',
    type: 'data',
    data: { key: 'value' },
    source: 'd',
    target: 'e',
    targetHandle: 'y',
  },
];
 
function Flow() {
  const [nodes, , onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
 
  const onConnect: OnConnect = useCallback(
    (params) => {
      setEdges((edges) =>
        addEdge({ type: 'data', data: { key: 'value' }, ...params }, edges),
      );
    },
    [setEdges],
  );
 
  return (
    <div className="h-screen w-screen p-8 bg-gray-50 rounded-xl">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        nodeTypes={nodeTypes}
        edgeTypes={edgeTypes}
        fitView
      />
    </div>
  );
}
 
export function App() {
  return <Flow />;
}
```

Putting everything together we end up with quite a capable little calculator!

You could continue to improve this flow by adding nodes to perform other operations or to take user input using additional components from the [shadcn/ui registry](https://ui.shadcn.com/docs/components/slider). In fact, keep your eyes peeled soon for a follow-up to this guide where we’ll show a complete application built using React Flow Components .

Wrapping up[](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components#wrapping-up)
-----------------------------------------------------------------------------------------------------------

In just a short amount of time we’ve managed to build out a fairly complete flow using the components and building blocks provided by shadcn React Flow Components. We’ve learned:

* How to use building blocks like the [`<BaseNodeHeader />`](https://reactflow.dev/ui/components/base-node) and [`<LabeledHandle />`](https://reactflow.dev/ui/components/labeled-handle) components to build our own custom nodes without starting from scratch.

* That React Flow UI also provides custom edges like the [`<DataEdge />`](https://reactflow.dev/ui/components/data-edge) to drop into our applications.

And thanks to the power of Tailwind, tweaking the visual style of these components is as simple as editing the variables in your CSS file.

That’s all for now! You can see all the components we currently have available over on the [UI docs page](https://reactflow.dev/ui). If you have any suggestions or requests for new components we’d love to hear about them. Or perhaps you’re already starting to build something with shadcn and React Flow UI. Either way make sure you let us know on our [Discord server](https://discord.com/invite/RVmnytFmGW) or on [Twitter](https://twitter.com/xyflowdev)!
