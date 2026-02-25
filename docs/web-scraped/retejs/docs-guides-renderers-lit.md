# Guide - Lit Renderer

Source: https://retejs.org/docs/guides/renderers/lit

---

Lit - Rete.js

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
[API](/docs/api)[Overview](/docs/api/overview)[rete](/docs/api/rete)[rete-area-plugin](/docs/api/rete-area-plugin)[rete-area-3d-plugin](/docs/api/rete-area-3d-plugin)[rete-connection-plugin](/docs/api/rete-connection-plugin)[rete-auto-arrange-plugin](/docs/api/rete-auto-arrange-plugin)[rete-context-menu-plugin](/docs/api/rete-context-menu-plugin)[rete-engine](/docs/api/rete-engine)[rete-history-plugin](/docs/api/rete-history-plugin)[rete-minimap-plugin](/docs/api/rete-minimap-plugin)[rete-readonly-plugin](/docs/api/rete-readonly-plugin)[rete-angular-plugin](/docs/api/rete-angular-plugin)[@retejs/lit-plugin](/docs/api/rete-lit-plugin)[rete-react-plugin](/docs/api/rete-react-plugin)[rete-svelte-plugin](/docs/api/rete-svelte-plugin)[rete-vue-plugin](/docs/api/rete-vue-plugin)[rete-render-utils](/docs/api/rete-render-utils)[rete-scopes-plugin](/docs/api/rete-scopes-plugin)[rete-dock-plugin](/docs/api/rete-dock-plugin)[rete-comment-plugin](/docs/api/rete-comment-plugin)[rete-connection-path-plugin](/docs/api/rete-connection-path-plugin)[rete-connection-reroute-plugin](/docs/api/rete-connection-reroute-plugin)[FAQ](/docs/faq)[Migration](/docs/migration)# LitThis guide is an extension of the [Basic](/docs/guides/basic) guide and provides instructions for using the `@retejs/lit-plugin` instead of `rete-react-plugin`
[Basic](/examples/basic/lit)[Customization](/examples/customization/lit)[Controls](/examples/controls/lit)[Plugin](https://github.com/retejs/lit-plugin)[Lit](https://lit.dev/)[Context menu](/docs/guides/context-menu)[Minimap](/docs/guides/minimap)[Reroute](/docs/guides/reroute)
This plugin offers a classic preset that comes with visual components for nodes, connections, sockets, and input controls.
Supports Lit version 3

## Install dependencies

Want to start faster? Use [Rete Kit](/docs/development/rete-kit) to create a fully configured project in minutes!

```bash
npm i @retejs/lit-plugin rete-render-utils lit
```

## Plugin connection

```ts
import { AreaPlugin } from "rete-area-plugin";

import { LitPlugin, Presets, LitArea2D } from "@retejs/lit-plugin";

type AreaExtra = LitArea2D<Schemes>;

// ....

const render = new LitPlugin<Schemes, AreaExtra>();

render.addPreset(Presets.classic.setup());

area.use(render);
```

Check out the [Lit](/examples/basic/lit) page for an example usage of this render plugin.

## Controls

This plugin provides built-in controls that are displayed based on the following objects:

- `ClassicPreset.InputControl` as `<input type="number" />` or `<input type="text" />`

Simply add the control to the node:

```ts
node.addControl(&#39;my-control&#39;, new ClassicPreset.InputControl("number", {
  initial: 0,
  readonly: false,
  change(value) { }
}))
```

If you want to add different types of controls, you can return the necessary component in the `control` handler of `customize` property.

```ts
import { MyButtonElement } from &#39;./MyButton&#39;

customElements.define("my-button", MyButtonElement);

render.addPreset(Presets.classic.setup({
  customize: {
    control(context) {
      if (context.payload.isButton) {
        const { payload } = context;

        return () => html`<my-button .data=${payload}></my-button>`;
      }
      if (context.payload instanceof ClassicPreset.InputControl) { // don&#39;t forget to explicitly specify the built-in <rete-control>
        return () => html`<rete-control .data=${payload}></rete-control>`;
      }
    }
  }
}));

node.addControl(&#39;my-button&#39;, { isButton: true, label: &#39;Click&#39;, onClick() {} })
```

### MyButton.ts

```ts
export class CustomButton extends LitElement {
  static get properties() {
    return {
      data: { type: Object },
    };
  }

  declare data: object;

  render() {
    return html`
      <button
        @pointerdown=${(e: MouseEvent) => e.stopPropagation()}
        @doubleclick=${(e: MouseEvent) => e.stopPropagation()}
        @click=${this.data.onClick}
      >${this.data.label}</button>
    `;
  }
}
```

This is a simplified version suitable for introductory purposes. For projects, it is recommended to follow the approach demonstrated in [the example](/examples/controls/lit)

Make sure to specify `@pointerdown` and `@doubleclick` to prevent the area from intercepting events such as `@click`.

## Customization

In a similar manner to the approach outlined above, you can replace node, connection, or socket components.

### Customization of all nodes

If you want to completely change the node structure, you can implement your own component similar to [node.ts](https://github.com/retejs/lit-plugin/blob/main/src/presets/classic/components/node.ts) from the classic preset.

```ts
import { CustomNodeElement } from &#39;./CustomNode&#39;

customElements.define("custom-node", CustomNodeElement)

render.addPreset(Presets.classic.setup({
  customize: {
    node(context) {
      return ({ emit }) => html`<custom-node .data=${context.payload} .emit=${emit}></custom-node>`;
    }
  }
}))
```

The implementation of `CustomNodeElement` is available in the **CustomNode.ts** file of the [Customization for Lit](/examples/customization/lit) example.

### Specific nodes

You can add an extra condition to apply this component only to specific nodes.

```ts
render.addPreset(Presets.classic.setup({
  customize: {
    node(context) {
      if (context.payload.label === "Custom") {
        return ({ emit }) => html`<custom-node .data=${context.payload} .emit=${emit}></custom-node>`;
      }
      return ({ emit }) => html`<rete-node .data=${context.payload} .emit=${emit}></rete-node>`;
    }
  }
}))

await editor.addNode(new ClassicPreset.Node(&#39;White&#39;))
```

### Connection customization

Use **connection.ts** as a starting point from the [presets/classic/components](https://github.com/retejs/lit-plugin/blob/main/src/presets/classic/components/connection.ts) directory of the plugin's source code.

```ts
import { CustomConnectionElement } from &#39;./CustomConnection&#39;

customElements.define("custom-connection", CustomConnectionElement);

render.addPreset(Presets.classic.setup({
  customize: {
    connection() {
      return ({ path }) => html`<custom-connection .path=${path}></custom-connection>`;
    }
  }
}))
```

### Socket customization

Use **socket.ts** as a starting point from the [presets/classic/components](https://github.com/retejs/lit-plugin/blob/main/src/presets/classic/components/socket.ts) directory of the plugin's source code.

```ts
import { CustomSocketElement } from &#39;./CustomSocket&#39;

customElements.define("custom-socket", CustomSocketElement);

render.addPreset(Presets.classic.setup({
  customize: {
    socket(context) {
      return () => html`<custom-socket .data=${context.payload}></custom-socket>`;
    }
  }
}))
```

## Other presets

- [context menu](/docs/guides/context-menu)

- [minimap](/docs/guides/minimap)
- [reroute](/docs/guides/reroute)

Check out the complete result on the [Customization for Lit](/examples/customization/lit) example page.

Released under the [MIT License](https://opensource.org/license/mit/)
Copyright © 2018-2026 Vitaliy Stoliarov
