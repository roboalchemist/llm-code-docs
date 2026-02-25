# Guide - Angular Renderer

Source: https://retejs.org/docs/guides/renderers/angular

---

Angular - Rete.js

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
[API](/docs/api)[Overview](/docs/api/overview)[rete](/docs/api/rete)[rete-area-plugin](/docs/api/rete-area-plugin)[rete-area-3d-plugin](/docs/api/rete-area-3d-plugin)[rete-connection-plugin](/docs/api/rete-connection-plugin)[rete-auto-arrange-plugin](/docs/api/rete-auto-arrange-plugin)[rete-context-menu-plugin](/docs/api/rete-context-menu-plugin)[rete-engine](/docs/api/rete-engine)[rete-history-plugin](/docs/api/rete-history-plugin)[rete-minimap-plugin](/docs/api/rete-minimap-plugin)[rete-readonly-plugin](/docs/api/rete-readonly-plugin)[rete-angular-plugin](/docs/api/rete-angular-plugin)[@retejs/lit-plugin](/docs/api/rete-lit-plugin)[rete-react-plugin](/docs/api/rete-react-plugin)[rete-svelte-plugin](/docs/api/rete-svelte-plugin)[rete-vue-plugin](/docs/api/rete-vue-plugin)[rete-render-utils](/docs/api/rete-render-utils)[rete-scopes-plugin](/docs/api/rete-scopes-plugin)[rete-dock-plugin](/docs/api/rete-dock-plugin)[rete-comment-plugin](/docs/api/rete-comment-plugin)[rete-connection-path-plugin](/docs/api/rete-connection-path-plugin)[rete-connection-reroute-plugin](/docs/api/rete-connection-reroute-plugin)[FAQ](/docs/faq)[Migration](/docs/migration)# AngularThis guide is an extension of the [Basic](/docs/guides/basic) guide and provides instructions for using the `rete-angular-plugin` instead of `rete-react-plugin`
[Basic](/examples/basic/angular)[Customization](/examples/customization/angular)[Controls](/examples/controls/angular)[Plugin](https://github.com/retejs/angular-plugin)[Angular](https://angular.io/)[Context menu](/docs/guides/context-menu)[Minimap](/docs/guides/minimap)[Reroute](/docs/guides/reroute)
This plugin offers a classic preset that comes with visual components for nodes, connections, sockets, and input controls.
Compatible with Angular 12, 13, 14, 15, 16, 17, 18, 19, 20 and 21
This plugin is **exclusively** designed for Angular applications as it requires an `Injector` instance, unlike other render plugins. Additionally, the plugin supports Standalone mode in integration starting from Angular 19, with enhanced features in Angular 20 and 21.
## [Install dependencies](#install-dependencies)Want to start faster? Use [Rete Kit](/docs/development/rete-kit) to create a fully configured project in minutes!Copy the command npx rete-kit app to clipboard[Learn More](/docs/development/rete-kit)bashnpm i rete-angular-plugin rete-render-utils @angular/elements@21
**Please note**: this plugin relies on `@angular/elements`, which is based on Web Components. However, Web Components have a limitation - they [cannot be unregistered](https://github.com/WICG/webcomponents/issues/754). This limitation may result in the reuse of the initial Angular component instead of creating a new one when a node with the same identifier is added, potentially leading to the use of outdated data within a custom node, such as data from an injected service.
## [Plugin connection](#connect-plugin)This is an example of integration in **Angular 21**, but you can specify a different version (12, 13, 14, 15, 16, 17, 18, 19, 20 or 21) in the import that matches the version of your application.
These versions have been compiled with Ivy.
tsimport { AreaPlugin } from "rete-area-plugin";
import { AngularPlugin, Presets, AngularArea2D } from "rete-angular-plugin/21";

type AreaExtra = AngularArea2D<Schemes>;

// ....

const render = new AngularPlugin<Schemes, AreaExtra>({ injector });

render.addPreset(Presets.classic.setup());

area.use(render);
where `injector` is an instance of `Injector` that can be obtained through dependency injection (DI).
## [Use Legacy View Engine](#legacy)Additionally, the plugin provides support for the legacy engine which can be imported in the following way
tsimport { AngularPlugin, Presets, AngularArea2D } from "rete-angular-plugin";
## [Controls](#controls)This plugin provides built-in controls that are displayed based on the following objects:
- `ClassicPreset.InputControl` as `<input type="number" />` or `<input type="text" />`
Simply add the control to the node
tsnode.addControl(&#39;my-control&#39;, new ClassicPreset.InputControl("number", {
  initial: 0,
  readonly: false,
  change(value) { }
}))
If you want to add different types of controls, you can return the necessary component in the `control` handler of `customize` property.
tsximport { ControlComponent } from "rete-angular-plugin/21";
import { MyButtonComponent } from &#39;./my-button.component&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    control(context) {
      if (context.payload.isButton) {
        return MyButtonComponent
      }
      if (context.payload instanceof ClassicPreset.InputControl) { // don&#39;t forget to explicitly specify the built-in ControlComponent
        return ControlComponent
      }
    }
  }
}));

node.addControl(&#39;my-button&#39;, { isButton: true, label: &#39;Click&#39;, onClick() {} })
tsimport { Component, Input } from "@angular/core";

@Component({
  selector: "app-button",
  template: `<button
    (pointerdown)="$event.stopPropagation()"
    (click)="data.onClick()"
  >
    {{ data.label }}
  </button>`
})
export class ButtonComponent {
  @Input() data!: { label: string, onClick: () => void };
}
This is a simplified version suitable for introductory purposes. For projects, it is recommended to follow the approach demonstrated in [the example](/examples/controls/angular)
Make sure to specify `(pointerdown)="$event.stopPropagation()"` to prevent the area from intercepting events such as `click`.
## [Customization](#customization)In a similar manner to the approach outlined above, you can replace node, connection, or socket components.
### [Customization of all nodes](#customize-all-nodes)If you want to completely change the node structure, you can implement your own component similar to [node](https://github.com/retejs/angular-plugin/blob/next/src/presets/classic/components/node) from the classic preset
tsimport { CustomNodeComponent } from &#39;./custom-node.component&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    node() {
      return CustomNodeComponent
    }
  }
}))
The implementation of `CustomNodeComponent` is available in the **custom-node.component.ts** file of the [Customization for Angular](/examples/customization/angular) example.
### [Specific nodes](#specific-nodes)You can add an extra condition to apply this component only to specific nodes.
tsimport { NodeComponent } from "rete-angular-plugin/21";

render.addPreset(Presets.classic.setup({
  customize: {
    node(context) {
      if (context.payload.label === "Custom") {
        return CustomNodeComponent;
      }
      return NodeComponent; // use built-in component
    }
  }
}))

await editor.addNode(new ClassicPreset.Node(&#39;White&#39;))
### [Connection customization](#customize-connection)Use **connection** as a starting point from the [presets/classic/components](https://github.com/retejs/angular-plugin/blob/next/src/presets/classic/components) directory of the plugin&#39;s source code.
tsimport { CustomConnectionComponent } from &#39;./custom-connection.component&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    connection() {
      return CustomConnectionComponent
    }
  }
}))
### [Socket customization](#customize-socket)Use **socket** as a starting point from the [presets/classic/components](https://github.com/retejs/angular-plugin/blob/next/src/presets/classic/components) directory of the plugin&#39;s source code.
tsimport { CustomSocketComponent } from &#39;./custom-socket.component&#39;

render.addPreset(Presets.classic.setup({
  customize: {
    socket() {
      return CustomSocketComponent
    }
  }
}))
## [Customize context menu](#customize-context-menu)In order to customize the context menu for this rendering plugin, one can override styles using selectors (and it&#39;s important to consider the specificity of selectors in CSS)
scss[rete-context-menu] {
  width: 320px;
  context-menu-search input.search {
    background: grey;
  }
  context-menu-item.block {
    background: grey;
  }
}
## [Other presets](#other-presets)- [context menu](/docs/guides/context-menu)
- [minimap](/docs/guides/minimap)
- [reroute](/docs/guides/reroute)
Check out the complete result on the [Customization for Angular](/examples/customization/angular) example page.
Released under the [MIT License](https://opensource.org/license/mit/)Copyright © 2018-2026 Vitaliy Stoliarov