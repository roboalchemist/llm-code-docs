# Concepts - Editor

Source: https://retejs.org/docs/concepts/editor

---

Editor - Rete.js

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
[API](/docs/api)[Overview](/docs/api/overview)[rete](/docs/api/rete)[rete-area-plugin](/docs/api/rete-area-plugin)[rete-area-3d-plugin](/docs/api/rete-area-3d-plugin)[rete-connection-plugin](/docs/api/rete-connection-plugin)[rete-auto-arrange-plugin](/docs/api/rete-auto-arrange-plugin)[rete-context-menu-plugin](/docs/api/rete-context-menu-plugin)[rete-engine](/docs/api/rete-engine)[rete-history-plugin](/docs/api/rete-history-plugin)[rete-minimap-plugin](/docs/api/rete-minimap-plugin)[rete-readonly-plugin](/docs/api/rete-readonly-plugin)[rete-angular-plugin](/docs/api/rete-angular-plugin)[@retejs/lit-plugin](/docs/api/rete-lit-plugin)[rete-react-plugin](/docs/api/rete-react-plugin)[rete-svelte-plugin](/docs/api/rete-svelte-plugin)[rete-vue-plugin](/docs/api/rete-vue-plugin)[rete-render-utils](/docs/api/rete-render-utils)[rete-scopes-plugin](/docs/api/rete-scopes-plugin)[rete-dock-plugin](/docs/api/rete-dock-plugin)[rete-comment-plugin](/docs/api/rete-comment-plugin)[rete-connection-path-plugin](/docs/api/rete-connection-path-plugin)[rete-connection-reroute-plugin](/docs/api/rete-connection-reroute-plugin)[FAQ](/docs/faq)[Migration](/docs/migration)# EditorNodeEditor`NodeEditor` is a class that implements an interface for interacting with a graph. Similar to other modules, it extends `Scope`: can produce signals and provides the ability to connect plugins.
tsimport { NodeEditor, BaseSchemes } from &#39;rete&#39;

type Schemes = BaseSchemes // has Node { id: string } and Connection { id: string, source: string, target: string }

const editor = new NodeEditor<Schemes>()
The `Schemes` type will be used for further type inference purposes.
There is a [classic preset](/docs/concepts/presets#data-structures) that provides the interfaces for building nodes.
The editor is applicable on both the client and server sides. On the client side, it can provide data for visualization purposes. On the server side, it can provide data for graph processing, for example, through `rete-engine` or other interactions using `rete-structures`.
## [Node and Connection management](#node-connection-management)ClassicPresetWe can add nodes as a regular object with a mandatory `id` field, or as nodes from `ClassicPreset`
tsimport { ClassicPreset } from &#39;rete&#39;

const node = new ClassicPreset.Node(&#39;Label&#39;)

node.addOutput(&#39;output&#39;, new ClassicPreset.Output(socket, &#39;Title&#39;))

await editor.addNode(node)
Removing can be achieved with `id`
tsawait editor.removeNode(node.id)
To create a connection, you can use a basic object with mandatory fields (`id`, `source`, `target`) or a classic preset that requires the source and target nodes to be passed for TypeScript type checking.
tsimport { ClassicPreset } from &#39;rete&#39;

const connection = new ClassicPreset.Connection(sourceNode, &#39;portKey&#39;, targetNode, &#39;portKey&#39;)

await editor.addConnection(connection)
Removing the connection by `id`
tsawait editor.removeConnection(connection.id)
## [Create a 2D area](#create-2d-area)AreaPluginIn order to visualize on HTML, `rete-area-plugin` is necessary. This plugin is responsible for basic features, such as zooming and dragging, and serves as an entry point for other plugins for visualizing and interacting with users
tsimport { AreaPlugin } from &#39;rete-area-plugin&#39;

const area = new AreaPlugin<Schemes, AreaExtra>(container) // container is HTMLElement where the area will be inserted
The `AreaExtra` type is necessary for incorporating other signal types, such as rendering various types of elements aside from `node` and `connection`
This plugin includes extensions. Some of them implement the functionality of v1, but with one significant difference - they are optional. For instance, the node selection extension not only supports node selection, but it is expandable (check out [Comments](/examples/comments) example), but it can also be substituted with an alternative implementation.
tsimport { AreaExtensions } from &#39;rete-area-plugin&#39;

AreaExtensions.selectableNodes(area, AreaExtensions.selector(), {
  accumulating: AreaExtensions.accumulateOnCtrl()
})
## [Interaction with connections](#interaction-with-connections)ConnectionPluginThe `rete-connection-plugin` plugin is responsible for user interaction with connections (creation, deletion)
tsimport { BidirectFlow, ConnectionPlugin, Presets as ConnectionPresets } from &#39;rete-connection-plugin&#39;

const connection = new ConnectionPlugin<Schemes, AreaExtra>()

connection.addPreset(ConnectionPresets.classic.setup())
Unlike Rete.js v1, this plugin doesn&#39;t render connections.
## [Rendering](#rendering)RenderingThe rendering of the UI is exclusively handled by rendering plugins (with a few exceptions), which provide presets for various kinds of functionality.
Let&#39;s take a look at the example using `rete-react-plugin`
tsimport { createRoot } from "react-dom/client";
import { ReactArea2D, ReactPlugin, Presets as ReactPresets } from &#39;rete-react-plugin&#39;
import { MinimapExtra } from &#39;rete-minimap-plugin&#39;
import { ContextMenuExtra } from &#39;rete-context-menu-plugin&#39;

type AreaExtra =
  | ReactArea2D<Schemes>
  | ContextMenuExtra
  | MinimapExtra

const reactPlugin = new ReactPlugin<Schemes, AreaExtra>({ createRoot })

reactPlugin.addPreset(ReactPresets.classic.setup())
reactPlugin.addPreset(ReactPresets.contextMenu.setup())
reactPlugin.addPreset(ReactPresets.minimap.setup())

area.use(reactPlugin)
Every element in the editor, like node, control, socket, or connection, is technically an independent tree of elements, which offers flexibility in combining different rendering frameworks. More information is available in the [Integration](/docs/concepts/integration) article.
Released under the [MIT License](https://opensource.org/license/mit/)Copyright © 2018-2026 Vitaliy Stoliarov