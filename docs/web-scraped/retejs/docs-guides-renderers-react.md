# Guide - React Renderer

Source: https://retejs.org/docs/guides/renderers/react

---

React.js - Rete.js

**[Docs](/docs)[Examples](/examples)[Studio](https://studio.retejs.org)[Sponsor](/sponsor)[GitHub](https://github.com/retejs)[YouTube](https://www.youtube.com/@rete_js)[Twitter](https://twitter.com/rete_js)[Discord](https://discord.gg/cxSFkPZdsV)**[Introduction](/docs)[Getting started](/docs/getting-started)- Concepts**
[Plugin system](/docs/concepts/plugin-system)[Presets](/docs/concepts/presets)[Editor](/docs/concepts/editor)[Engine](/docs/concepts/engine)[Integration](/docs/concepts/integration)- Guides**
[Basic editor](/docs/guides/basic)- Renderers**
[React.js](/docs/guides/renderers/react)[Vue.js](/docs/guides/renderers/vue)[Angular](/docs/guides/renderers/angular)[Svelte](/docs/guides/renderers/svelte)[Lit](/docs/guides/renderers/lit)- Processing**
[Dataflow](/docs/guides/processing/dataflow)[Control flow](/docs/guides/processing/control-flow)[Hybrid Engine](/docs/guides/processing/hybrid)[Codegen](/docs/guides/processing/codegen)- 3D**
[3D](/docs/guides/3d)[Data structures](/docs/guides/data-structures)[Arrange nodes](/docs/guides/arrange)- Selectable**
[Selectable](/docs/guides/selectable)[Selectable connections](/docs/guides/selectable/connections)[Connections](/docs/guides/connections)[Context menu](/docs/guides/context-menu)[Readonly](/docs/guides/readonly)[Modules](/docs/guides/modules)[Scopes](/docs/guides/scopes)[Import/export](/docs/guides/import-export)[Validation](/docs/guides/validation)[Minimap](/docs/guides/minimap)[Dock menu](/docs/guides/dock-menu)[Connection path](/docs/guides/connection-path)[Reroute](/docs/guides/reroute)[Undo/Redo](/docs/guides/undo-redo)[Comments](/docs/guides/comments)- Best Practices**
[Performance](/docs/best-practices/performance)[Quality assurance](/docs/quality-assurance)- Development**
[Development](/docs/development)[Rete CLI](/docs/development/rete-cli)[Rete Kit](/docs/development/rete-kit)- AI Assistance**
[AI Assistance](/docs/development/ai-assistance)[LLMs.txt](/docs/development/ai-assistance/llms)[Rete Kit AI](/docs/development/ai-assistance/rete-kit-ai)[Troubleshooting](/docs/troubleshooting)[Licensing](/docs/licensing)[Code of Conduct](/docs/code-of-conduct)[Contribution](/docs/contribution)- API**
[API](/docs/api)[Overview](/docs/api/overview)[rete](/docs/api/rete)[rete-area-plugin](/docs/api/rete-area-plugin)[rete-area-3d-plugin](/docs/api/rete-area-3d-plugin)[rete-connection-plugin](/docs/api/rete-connection-plugin)[rete-auto-arrange-plugin](/docs/api/rete-auto-arrange-plugin)[rete-context-menu-plugin](/docs/api/rete-context-menu-plugin)[rete-engine](/docs/api/rete-engine)[rete-history-plugin](/docs/api/rete-history-plugin)[rete-minimap-plugin](/docs/api/rete-minimap-plugin)[rete-readonly-plugin](/docs/api/rete-readonly-plugin)[rete-angular-plugin](/docs/api/rete-angular-plugin)[@retejs/lit-plugin](/docs/api/rete-lit-plugin)[rete-react-plugin](/docs/api/rete-react-plugin)[rete-svelte-plugin](/docs/api/rete-svelte-plugin)[rete-vue-plugin](/docs/api/rete-vue-plugin)[rete-render-utils](/docs/api/rete-render-utils)[rete-scopes-plugin](/docs/api/rete-scopes-plugin)[rete-dock-plugin](/docs/api/rete-dock-plugin)[rete-comment-plugin](/docs/api/rete-comment-plugin)[rete-connection-path-plugin](/docs/api/rete-connection-path-plugin)[rete-connection-reroute-plugin](/docs/api/rete-connection-reroute-plugin)[FAQ](/docs/faq)[Migration](/docs/migration)

      [Rete.js](/)[GitHub](https://github.com/retejs)[YouTube](https://www.youtube.com/@rete_js)[Twitter](https://twitter.com/rete_js)[Discord](https://discord.gg/cxSFkPZdsV)[Docs](/docs)[Examples](/examples)[Studio](https://studio.retejs.org)[Sponsor](/sponsor)en# Documentation[Introduction](/docs)[Getting started](/docs/getting-started)- Concepts**
[Plugin system](/docs/concepts/plugin-system)[Presets](/docs/concepts/presets)[Editor](/docs/concepts/editor)[Engine](/docs/concepts/engine)[Integration](/docs/concepts/integration)- Guides**
[Basic editor](/docs/guides/basic)- Renderers**
[React.js](/docs/guides/renderers/react)[Vue.js](/docs/guides/renderers/vue)[Angular](/docs/guides/renderers/angular)[Svelte](/docs/guides/renderers/svelte)[Lit](/docs/guides/renderers/lit)- Processing**
[Dataflow](/docs/guides/processing/dataflow)[Control flow](/docs/guides/processing/control-flow)[Hybrid Engine](/docs/guides/processing/hybrid)[Codegen](/docs/guides/processing/codegen)- 3D**
[3D](/docs/guides/3d)[Data structures](/docs/guides/data-structures)[Arrange nodes](/docs/guides/arrange)- Selectable**
[Selectable](/docs/guides/selectable)[Selectable connections](/docs/guides/selectable/connections)[Connections](/docs/guides/connections)[Context menu](/docs/guides/context-menu)[Readonly](/docs/guides/readonly)[Modules](/docs/guides/modules)[Scopes](/docs/guides/scopes)[Import/export](/docs/guides/import-export)[Validation](/docs/guides/validation)[Minimap](/docs/guides/minimap)[Dock menu](/docs/guides/dock-menu)[Connection path](/docs/guides/connection-path)[Reroute](/docs/guides/reroute)[Undo/Redo](/docs/guides/undo-redo)[Comments](/docs/guides/comments)- Best Practices**
[Performance](/docs/best-practices/performance)[Quality assurance](/docs/quality-assurance)- Development**
[Development](/docs/development)[Rete CLI](/docs/development/rete-cli)[Rete Kit](/docs/development/rete-kit)- AI Assistance**
[AI Assistance](/docs/development/ai-assistance)[LLMs.txt](/docs/development/ai-assistance/llms)[Rete Kit AI](/docs/development/ai-assistance/rete-kit-ai)[Troubleshooting](/docs/troubleshooting)[Licensing](/docs/licensing)[Code of Conduct](/docs/code-of-conduct)[Contribution](/docs/contribution)- API**
[API](/docs/api)[Overview](/docs/api/overview)[rete](/docs/api/rete)[rete-area-plugin](/docs/api/rete-area-plugin)[rete-area-3d-plugin](/docs/api/rete-area-3d-plugin)[rete-connection-plugin](/docs/api/rete-connection-plugin)[rete-auto-arrange-plugin](/docs/api/rete-auto-arrange-plugin)[rete-context-menu-plugin](/docs/api/rete-context-menu-plugin)[rete-engine](/docs/api/rete-engine)[rete-history-plugin](/docs/api/rete-history-plugin)[rete-minimap-plugin](/docs/api/rete-minimap-plugin)[rete-readonly-plugin](/docs/api/rete-readonly-plugin)[rete-angular-plugin](/docs/api/rete-angular-plugin)[@retejs/lit-plugin](/docs/api/rete-lit-plugin)[rete-react-plugin](/docs/api/rete-react-plugin)[rete-svelte-plugin](/docs/api/rete-svelte-plugin)[rete-vue-plugin](/docs/api/rete-vue-plugin)[rete-render-utils](/docs/api/rete-render-utils)[rete-scopes-plugin](/docs/api/rete-scopes-plugin)[rete-dock-plugin](/docs/api/rete-dock-plugin)[rete-comment-plugin](/docs/api/rete-comment-plugin)[rete-connection-path-plugin](/docs/api/rete-connection-path-plugin)[rete-connection-reroute-plugin](/docs/api/rete-connection-reroute-plugin)[FAQ](/docs/faq)[Migration](/docs/migration)# React.jsThis guide is an extension of the [Basic](/docs/guides/basic) guide and provides in-depth instructions for using the `rete-react-plugin`
[Basic](/examples/basic/react)[Controls](/examples/controls/react)[Customization](/examples/customization/react)[Plugin](https://github.com/retejs/react-plugin)[React.js](https://react.dev/)[Context menu](/docs/guides/context-menu)[Minimap](/docs/guides/minimap)[Reroute](/docs/guides/reroute)
This plugin uses a classic preset that includes visual components for nodes, connections, sockets, and input controls. It leverages `styled-components` to design these components.
This plugin can be used in any application, regardless of your stack (**React.js**, **Vue.js**, **Angular**, etc.).

## Install dependencies

Want to start faster? Use [Rete Kit](/docs/development/rete-kit) to create a fully configured project in minutes!

```bash
npm i rete-react-plugin rete-render-utils styled-components
```

If you're using this plugin in an application that doesn't utilize **React.js**, make sure to install the required **React.js** dependencies as well.

```bash
npm i react@19 react-dom@19
```

## Plugin connection

```ts
import { createRoot } from "react-dom/client"

import { AreaPlugin } from "rete-area-plugin";
import { ReactPlugin, Presets, ReactArea2D } from "rete-react-plugin";

type AreaExtra = ReactArea2D<Schemes>;

// ....

const render = new ReactPlugin<Schemes, AreaExtra>({ createRoot });

render.addPreset(Presets.classic.setup());

area.use(render);
**React 19 Requirement**: When using React 19, passing `createRoot` as a parameter is **mandatory** when initializing ReactPlugin. This is required due to changes in React 19&#39;s rendering system.
Check out the [Basic](/examples/basic/react) page for an example of how to use this rendering plugin.

## Using React.js 16-17

In case you&#39;re using React.js version 16 or 17, the `createRoot` method is optional

```ts
const render = new ReactPlugin<Schemes, AreaExtra>();

## "useRete" hook

When working with React app, `useRete` hook eliminates the need for boilerplate code that binds an editor to HTML element. This becomes particularly crucial for dynamic app updates where the old instance of the editor must be removed and replaced with a new one

```ts
ximport { useRete } from &#39;rete-react-plugin&#39;;

function App() {
  const [ref, editor] = useRete(createEditor)

  return <div ref={ref} className="rete"></div>
}
where `createEditor` should return object with `destroy` method (usually it has `area.destroy()` call)

## Controls

This plugin provides built-in controls that are displayed based on the following objects

- `ClassicPreset.InputControl` as `<input type="number" />` or `<input type="text" />`
Simply add the control to the node
```ts
node.addControl(&#39;my-control&#39;, new ClassicPreset.InputControl("number", {
  initial: 0,
  readonly: false,
  change(value) { }
}))
If you want to add different types of controls, you can return the necessary functional component in the `control` handler of `customize` property.
```ts
xrender.addPreset(Presets.classic.setup({
  customize: {
    control(context) {
      if (context.payload.isButton) {
        return (props: { data: { isButton: true, label: string, onClick: () => void }}) => (
          <button
            onPointerDown={(e) => e.stopPropagation()}
            onClick={props.data.onClick}
          >
            {props.data.label}
          </button>
        )
      }
      if (context.payload instanceof ClassicPreset.InputControl) { // don&#39;t forget to explicitly specify the built-in Presets.classic.Control
        return Presets.classic.Control;
      }
    }
  }
}));

node.addControl(&#39;my-button&#39;, { isButton: true, label: &#39;Click&#39;, onClick() {} })
This is a simplified version suitable for introductory purposes. For projects, it is recommended to follow the approach demonstrated in [the example](/examples/controls/react)
Make sure to call `stopPropagation` in `onPointerDown` to prevent the area from intercepting events such as `click`. If you are encountering this issue in React 16 or your interactive elements are added to a custom node instead of a control, try the following solution:
```ts
ximport { Drag } from "rete-react-plugin";

<Drag.NoDrag>
  <button>
    {props.data.label}
  </button>
</Drag.NoDrag>
Or use a hook to avoid extra nesting
```ts
xconst ref = React.useRef(null)

Drag.useNoDrag(ref)

<button ref={ref}>
  {props.data.label}
</button>

## Customization

In a similar manner to the approach outlined above, you can replace node, connection, or socket components
### Node styles

The easiest approach is to extend the current component and use `styled-components` to add extra styles

```ts
ximport { Presets } from "rete-react-plugin";
import { css } from "styled-components";

const myStyles = css<{ selected?: boolean }>`
  background: white;
  ${(props) => props.selected && css`
    border-color: red;
  `}
`;

function StyledNode(props: { data: Schemes[&#39;Node&#39;] }) {
  return <Presets.classic.Node styles={() => myStyles} {...props} />;
}

render.addPreset(Presets.classic.setup({
  customize: {
    node() {
      return StyledNode
    }
  }
}))
Implementing this will result in all your nodes using `myStyles`.

### Specific nodes

You can add an extra condition to apply these styles only to specific nodes

```ts
render.addPreset(Presets.classic.setup({
  customize: {
    node(context) {
      if (context.payload.label === "White") {
        return StyledNode;
      }
      return Presets.classic.Node;
    }
  }
}))

await editor.addNode(new ClassicPreset.Node(&#39;White&#39;))

### Full node customization

If you want to completely change the node structure, you can implement your own component similar to [Node.tsx](https://github.com/retejs/react-plugin/blob/next/src/presets/classic/components/Node.tsx) from the classic preset

```ts
import { CustomNode } from &#39;./CustomNode&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    node() {
      return CustomNode
    }
  }
}))
The implementation of `CustomNode` is available in the **CustomNode.tsx** file of the [Customization for React.js](/examples/customization/react) example.

### Full customization of connections

Use **Connection.tsx** as a starting point from the [presets/classic/components](https://github.com/retejs/react-plugin/blob/next/src/presets/classic/components) directory of the plugin&#39;s source code

```ts
import { CustomConnection } from &#39;./CustomConnection&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    connection() {
      return CustomConnection
    }
  }
}))

### Full socket customization

Use **Socket.tsx** as a starting point from the [presets/classic/components](https://github.com/retejs/react-plugin/blob/next/src/presets/classic/components) directory of the plugin&#39;s source code

```ts
import { CustomSocket } from &#39;./CustomSocket&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    socket() {
      return CustomSocket
    }
  }
}))

## Customize context menu

As the context menu components utilize `styled-components`, you can customize their styles by

```ts
import styled from "styled-components";

const { Menu, Common, Search, Item, Subitems } = Presets.contextMenu

const CustomMenu = styled(Menu)`
  width: 320px;
`
const CustomItem = styled(Item)`
  background: grey;
`

render.addPreset(Presets.contextMenu.setup({
  customize: {
    main: () => CustomMenu,
    item: () => CustomItem,
    common: () => Common,
    search: () => Search,
    subitems: () => Subitems
  }
}))

## Other presets

- [context menu](/docs/guides/context-menu)

- [minimap](/docs/guides/minimap)
- [reroute](/docs/guides/reroute)
Check out the complete result on the [Customization for React.js](/examples/customization/react) example page.
Released under the [MIT License](https://opensource.org/license/mit/)Copyright © 2018-2026 Vitaliy Stoliarov
