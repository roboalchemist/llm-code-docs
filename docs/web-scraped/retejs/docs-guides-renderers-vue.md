# Guide - Vue Renderer

Source: https://retejs.org/docs/guides/renderers/vue

---

Vue.js - Rete.js

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
[API](/docs/api)[Overview](/docs/api/overview)[rete](/docs/api/rete)[rete-area-plugin](/docs/api/rete-area-plugin)[rete-area-3d-plugin](/docs/api/rete-area-3d-plugin)[rete-connection-plugin](/docs/api/rete-connection-plugin)[rete-auto-arrange-plugin](/docs/api/rete-auto-arrange-plugin)[rete-context-menu-plugin](/docs/api/rete-context-menu-plugin)[rete-engine](/docs/api/rete-engine)[rete-history-plugin](/docs/api/rete-history-plugin)[rete-minimap-plugin](/docs/api/rete-minimap-plugin)[rete-readonly-plugin](/docs/api/rete-readonly-plugin)[rete-angular-plugin](/docs/api/rete-angular-plugin)[@retejs/lit-plugin](/docs/api/rete-lit-plugin)[rete-react-plugin](/docs/api/rete-react-plugin)[rete-svelte-plugin](/docs/api/rete-svelte-plugin)[rete-vue-plugin](/docs/api/rete-vue-plugin)[rete-render-utils](/docs/api/rete-render-utils)[rete-scopes-plugin](/docs/api/rete-scopes-plugin)[rete-dock-plugin](/docs/api/rete-dock-plugin)[rete-comment-plugin](/docs/api/rete-comment-plugin)[rete-connection-path-plugin](/docs/api/rete-connection-path-plugin)[rete-connection-reroute-plugin](/docs/api/rete-connection-reroute-plugin)[FAQ](/docs/faq)[Migration](/docs/migration)# Vue.jsThis guide is an extension of the [Basic](/docs/guides/basic) guide and provides instructions for using the `rete-vue-plugin` instead of `rete-react-plugin`
[Basic](/examples/basic/vue)[Customization](/examples/customization/vue)[Controls](/examples/controls/vue)[Plugin](https://github.com/retejs/vue-plugin)[Vue.js](https://vuejs.org/)[Context menu](/docs/guides/context-menu)[Minimap](/docs/guides/minimap)[Reroute](/docs/guides/reroute)
This plugin offers a classic preset that comes with visual components for nodes, connections, sockets, and input controls.
Supports both versions of Vue.js: 2 and 3
You can use this plugin in any application, irrespective of the application stack (React.js, Vue.js, Angular). However, using SFC requires a bundler with a corresponding template compiler installed, which is a separate topic for discussion.

## Install dependencies

Want to start faster? Use [Rete Kit](/docs/development/rete-kit) to create a fully configured project in minutes!

```bash
npm i rete-vue-plugin rete-render-utils
```

## Plugin connection

```ts
import { AreaPlugin } from "rete-area-plugin";

import { VuePlugin, Presets, VueArea2D } from "rete-vue-plugin";

type AreaExtra = VueArea2D<Schemes>;

// ....

const render = new VuePlugin<Schemes, AreaExtra>();

render.addPreset(Presets.classic.setup());

area.use(render);
Check out the Vue page(/examples/basic/vue) page for an example usage of this render plugin.

## Using Vue.js 2

To use the plugin with Vue 2, add `/vue2` to the import statement

```ts
import { VuePlugin, Presets, VueArea2D } from "rete-vue-plugin/vue2";

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
ximport MyButton from &#39;./MyButton.vue&#39;

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
**MyButton.vue**
vue<template>
<button
  @pointerdown.stop=""
  @click="data.onClick"
>{{data.label}}</button>
</template>
This is a simplified version suitable for introductory purposes. For projects, it is recommended to follow the approach demonstrated in [the example](/examples/controls/vue)
Make sure to specify `@pointerdown.stop` to prevent the area from intercepting events such as `click`.

## Customization

In a similar manner to the approach outlined above, you can replace node, connection, or socket components
### Customization of all nodes

If you want to completely change the node structure, you can implement your own component similar to [Node.vue](https://github.com/retejs/vue-plugin/blob/next/src/presets/classic/components/Node.vue) from the classic preset

```ts
import CustomNode from &#39;./CustomNode.vue&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    node() {
      return CustomNode
    }
  }
}))
The implementation of `CustomNode` is available in the **CustomNode.vue** file of the [Customization for Vue.js](/examples/customization/vue) example.

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

Use **Connection.vue** as a starting point from the [presets/classic/components](https://github.com/retejs/vue-plugin/blob/next/src/presets/classic/components) directory of the plugin&#39;s source code

```ts
import CustomConnection from &#39;./CustomConnection.vue&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    connection() {
      return CustomConnection
    }
  }
}))

### Socket customization

Use **Socket.vue** as a starting point from the [presets/classic/components](https://github.com/retejs/vue-plugin/blob/next/src/presets/classic/components) directory of the plugin&#39;s source code

```ts
import CustomSocket from &#39;./CustomSocket.vue&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    socket() {
      return CustomSocket
    }
  }
}))

## Customize context menu

In order to customize the context menu for this rendering plugin, one can override styles using selectors (and it&#39;s important to consider the specificity of selectors in CSS)

scss[rete-context-menu] {
  width: 320px !important;
  .block:first-child input {
    background: grey;
  }
  .block.item {
    background: grey;
  }
}

## Use Vue.js plugins

Since `rete-vue-plugin` creates independent Vue.js instance for nodes, sockets, controls, etc., it doesn&#39;t inherit plugins from your project&#39;s main Vue instance. To bridge this gap, the plugin offers a solution: injecting a custom Vue application instance. This capability ensures that any Vue plugins or global components you wish to employ within your Rete-specific Vue components are accessible, enabling seamless sharing between your Vue.js application and Rete.js editor
### Vue.js 3

The following example demonstrates how to configure custom Vue.js 3 instance

```ts
import { Presets, VuePlugin } from "rete-vue-plugin";
import { createApp } from "vue";

const render = new VuePlugin<Schemes, AreaExtra>({
  setup(context) {
    const app = createApp(context);

    app.use(yourPlugin);

    return app;
  },
});
where `yourPlugin` is an instance of any plugin (like [Vuetify](https://vuetifyjs.com/en/getting-started) or [Vue I18N](https://vue-i18n.intlify.dev/))

### Vue.js 2

Since the initialization for Vue.js 2 is slightly different, let&#39;s take a look at the following example

```ts
import { Presets, VuePlugin } from "rete-vue-plugin";
import Vue from "vue";

const render = new VuePlugin<Schemes, AreaExtra>({
  setup(context) {
    const app = new Vue({ ...context, yourPlugin });

    return app;
  },
});
where `yourPlugin` is an instance of any plugin (like [Vuetify](https://vuetifyjs.com/en/getting-started) or [Vue I18N](https://kazupon.github.io/vue-i18n/))

## Other presets

- [context menu](/docs/guides/context-menu)

- [minimap](/docs/guides/minimap)
- [reroute](/docs/guides/reroute)
Check out the complete result on the [Customization for Vue.js](/examples/customization/vue) example page.
Released under the [MIT License](https://opensource.org/license/mit/)Copyright © 2018-2026 Vitaliy Stoliarov
