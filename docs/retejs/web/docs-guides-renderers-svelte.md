# Guide - Svelte Renderer

Source: https://retejs.org/docs/guides/renderers/svelte

---

Svelte - Rete.js

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
[API](/docs/api)[Overview](/docs/api/overview)[rete](/docs/api/rete)[rete-area-plugin](/docs/api/rete-area-plugin)[rete-area-3d-plugin](/docs/api/rete-area-3d-plugin)[rete-connection-plugin](/docs/api/rete-connection-plugin)[rete-auto-arrange-plugin](/docs/api/rete-auto-arrange-plugin)[rete-context-menu-plugin](/docs/api/rete-context-menu-plugin)[rete-engine](/docs/api/rete-engine)[rete-history-plugin](/docs/api/rete-history-plugin)[rete-minimap-plugin](/docs/api/rete-minimap-plugin)[rete-readonly-plugin](/docs/api/rete-readonly-plugin)[rete-angular-plugin](/docs/api/rete-angular-plugin)[@retejs/lit-plugin](/docs/api/rete-lit-plugin)[rete-react-plugin](/docs/api/rete-react-plugin)[rete-svelte-plugin](/docs/api/rete-svelte-plugin)[rete-vue-plugin](/docs/api/rete-vue-plugin)[rete-render-utils](/docs/api/rete-render-utils)[rete-scopes-plugin](/docs/api/rete-scopes-plugin)[rete-dock-plugin](/docs/api/rete-dock-plugin)[rete-comment-plugin](/docs/api/rete-comment-plugin)[rete-connection-path-plugin](/docs/api/rete-connection-path-plugin)[rete-connection-reroute-plugin](/docs/api/rete-connection-reroute-plugin)[FAQ](/docs/faq)[Migration](/docs/migration)# SvelteThis guide is an extension of the [Basic](/docs/guides/basic) guide and provides instructions for using the `rete-svelte-plugin` instead of `rete-react-plugin`
[Basic](/examples/basic/svelte)[Customization](/examples/customization/svelte)[Controls](/examples/controls/svelte)[Plugin](https://github.com/retejs/svelte-plugin)[Svelte](https://svelte.dev/)[Context menu](/docs/guides/context-menu)[Minimap](/docs/guides/minimap)[Reroute](/docs/guides/reroute)
This plugin offers a classic preset that comes with visual components for nodes, connections, sockets, and input controls.
Supports latest versions of Svelte: 5, 4 and 3

## Install dependencies

Want to start faster? Use [Rete Kit](/docs/development/rete-kit) to create a fully configured project in minutes!

```bash
npm i rete-svelte-plugin rete-render-utils sass
```

## Plugin connection

```ts
import { AreaPlugin } from "rete-area-plugin";

import { SveltePlugin, Presets, SvelteArea2D } from "rete-svelte-plugin/5"; // or "rete-svelte-plugin" for older versions

type AreaExtra = SvelteArea2D<Schemes>;

// ....

const render = new SveltePlugin<Schemes, AreaExtra>();

render.addPreset(Presets.classic.setup());

area.use(render);
Please note that this plugin is intended for client-side use only. Therefore, modules that use it within your `*.svelte` modules need to be dynamically imported.
```ts
onMount(async () => {
  const { createEditor } = await import("./editor");
})
Check out the [Svelte](/examples/basic/svelte) page for an example usage of this render plugin.

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
If you want to add different types of controls, you can return the necessary component in the `control` handler of `customize` property.
```ts
ximport MyButton from &#39;./MyButton.svelte&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    control(context) {
      if (context.payload.isButton) {
        return MyButton
      }
      if (context.payload instanceof ClassicPreset.InputControl) { // don&#39;t forget to explicitly specify the built-in Presets.classic.Control
        return Presets.classic.Control;
      }
    }
  }
}));

node.addControl(&#39;my-button&#39;, { isButton: true, label: &#39;Click&#39;, onClick() {} })
**MyButton.svelte**
svelte<button
  on:pointerdown|stopPropagation={() => null}
  on:click="data.onClick"
>
  {data.label}
</button>
This is a simplified version suitable for introductory purposes. For projects, it is recommended to follow the approach demonstrated in [the example](/examples/controls/svelte)
Make sure to specify `on:pointerdown|stopPropagation` to prevent the area from intercepting events such as `click`.

## Customization

In a similar manner to the approach outlined above, you can replace node, connection, or socket components
### Customization of all nodes

If you want to completely change the node structure, you can implement your own component similar to [Node.svelte](https://github.com/retejs/svelte-plugin/blob/main/src/presets/classic/components/Node.svelte) from the classic preset

```ts
import CustomNode from &#39;./CustomNode.svelte&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    node() {
      return CustomNode
    }
  }
}))
The implementation of `CustomNode` is available in the **CustomNode.svelte** file of the [Customization for Svelte](/examples/customization/svelte) example.

### Specific nodes

You can add an extra condition to apply this component only to specific nodes

```ts
render.addPreset(Presets.classic.setup({
  customize: {
    node(context) {
      if (context.payload.label === "Custom") {
        return CustomNode;
      }
      return Presets.classic.Node;
    }
  }
}))

await editor.addNode(new ClassicPreset.Node(&#39;White&#39;))

### Connection customization

Use **Connection.svelte** as a starting point from the [presets/classic/components](https://github.com/retejs/svelte-plugin/blob/main/src/presets/classic/components) directory of the plugin&#39;s source code

```ts
import CustomConnection from &#39;./CustomConnection.svelte&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    connection() {
      return CustomConnection
    }
  }
}))

### Socket customization

Use **Socket.svelte** as a starting point from the [presets/classic/components](https://github.com/retejs/svelte-plugin/blob/main/src/presets/classic/components) directory of the plugin&#39;s source code

```ts
import CustomSocket from &#39;./CustomSocket.svelte&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    socket() {
      return CustomSocket
    }
  }
}))

## Customize context menu

In order to customize the context menu for this rendering plugin, one can override styles using selectors (and it&#39;s important to consider the specificity of selectors in CSS)

scss.rete-context-menu {
  width: 320px !important;
  .block:first-child input {
    background: grey;
  }
  .block.item {
    background: grey;
  }
}

## Other presets

- [context menu](/docs/guides/context-menu)

- [minimap](/docs/guides/minimap)
- [reroute](/docs/guides/reroute)
Check out the complete result on the [Customization for Svelte](/examples/customization/svelte) example page.
Released under the [MIT License](https://opensource.org/license/mit/)Copyright © 2018-2026 Vitaliy Stoliarov
