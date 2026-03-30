# Concepts - Integration

Source: https://retejs.org/docs/concepts/integration

---

Integration - Rete.js

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
[API](/docs/api)[Overview](/docs/api/overview)[rete](/docs/api/rete)[rete-area-plugin](/docs/api/rete-area-plugin)[rete-area-3d-plugin](/docs/api/rete-area-3d-plugin)[rete-connection-plugin](/docs/api/rete-connection-plugin)[rete-auto-arrange-plugin](/docs/api/rete-auto-arrange-plugin)[rete-context-menu-plugin](/docs/api/rete-context-menu-plugin)[rete-engine](/docs/api/rete-engine)[rete-history-plugin](/docs/api/rete-history-plugin)[rete-minimap-plugin](/docs/api/rete-minimap-plugin)[rete-readonly-plugin](/docs/api/rete-readonly-plugin)[rete-angular-plugin](/docs/api/rete-angular-plugin)[@retejs/lit-plugin](/docs/api/rete-lit-plugin)[rete-react-plugin](/docs/api/rete-react-plugin)[rete-svelte-plugin](/docs/api/rete-svelte-plugin)[rete-vue-plugin](/docs/api/rete-vue-plugin)[rete-render-utils](/docs/api/rete-render-utils)[rete-scopes-plugin](/docs/api/rete-scopes-plugin)[rete-dock-plugin](/docs/api/rete-dock-plugin)[rete-comment-plugin](/docs/api/rete-comment-plugin)[rete-connection-path-plugin](/docs/api/rete-connection-path-plugin)[rete-connection-reroute-plugin](/docs/api/rete-connection-reroute-plugin)[FAQ](/docs/faq)[Migration](/docs/migration)

## Integration

Architecture This framework is not bound to any UI rendering framework and can be integrated with the most popular frameworks/libraries such as **Angular**, **Svelte**, **Lit**, **Vue.js**, **React.js**. The following rendering packages are available:

- [`rete-react-plugin`](https://www.npmjs.com/package/rete-react-plugin)
- [`rete-vue-plugin`](https://www.npmjs.com/package/rete-vue-plugin)
- [`rete-angular-plugin`](https://www.npmjs.com/package/rete-angular-plugin)
- [`rete-svelte-plugin`](https://www.npmjs.com/package/rete-svelte-plugin)
- [`@retejs/lit-plugin`](https://www.npmjs.com/package/@retejs/lit-plugin)

The primary objective is to empower you to choose the visualization tools that align with your specific needs. Additionally, if you ever need to use the render plugin for a different framework within your application (such as during a project migration), you can easily do so. Please note that `rete-angular-plugin` is only compatible with Angular applications.

## Classic preset

By default, you can use the classic preset that has built-in components for:

- nodes
- connections
- some controls (numeric or text input fields)

```ts
import { AngularPlugin, AngularArea2D, Presets as AngularPresets } from 'rete-angular-plugin/21'

const angular = new AngularPlugin<Schemes, AngularArea2D<Schemes>>({ injector })

angular.addPreset(AngularPresets.classic.setup())

area.use(angular)
```

The framework allows you to swap out the pre-defined components with any other components as per your needs. The node component, in particular, can be customized extensively. Refer to the [Customization](/docs/guides/renderers/react#customization) guide for more details.

## Combining render plugins

This framework version has improved approaches for combining various rendering frameworks while ensuring TypeScript support. For instance, you can render one node using **Vue.js** and another using **React.js**.

```ts
import { createRoot } from "react-dom/client";
import { ReactArea2D, ReactPlugin, Presets as ReactPresets } from 'rete-react-plugin'
import { VueArea2D, VuePlugin, Presets as VuePresets } from 'rete-vue-plugin'

type AreaExtra =
  | ReactArea2D<Schemes>
  | VueArea2D<Schemes>

const reactPlugin = new ReactPlugin<Schemes, AreaExtra>({ createRoot })
const vuePlugin = new VuePlugin<Schemes, AreaExtra>()

reactPlugin.addPreset(ReactPresets.classic.setup({ customize: {
  node(data) {
    if (data.payload instanceof AddNode) return null // prevent rendering of AddNode by React.js
    return ReactPresets.classic.Node
  }
} }))
vuePlugin.addPreset(VuePresets.classic.setup({ customize: {
  node() {
    return VuePresets.classic.Node // render all nodes that weren't rendered by previously used render plugin
  }
} }))

// order matters
area.use(reactPlugin)
area.use(vuePlugin)
```

The `AddNode` node in this example is rendered using **Vue.js**, while all other nodes are rendered using **React.js**.

Using multiple frameworks at once may have performance drawbacks, but it can also offer a significant boost to prototyping speed when time-to-market is critical.

Released under the [MIT License](https://opensource.org/license/mit/)Copyright © 2018-2026 Vitaliy Stoliarov
