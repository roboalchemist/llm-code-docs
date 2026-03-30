# Migration Guide

Source: https://retejs.org/docs/migration

---

Migration - Rete.js

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
[API](/docs/api)[Overview](/docs/api/overview)[rete](/docs/api/rete)[rete-area-plugin](/docs/api/rete-area-plugin)[rete-area-3d-plugin](/docs/api/rete-area-3d-plugin)[rete-connection-plugin](/docs/api/rete-connection-plugin)[rete-auto-arrange-plugin](/docs/api/rete-auto-arrange-plugin)[rete-context-menu-plugin](/docs/api/rete-context-menu-plugin)[rete-engine](/docs/api/rete-engine)[rete-history-plugin](/docs/api/rete-history-plugin)[rete-minimap-plugin](/docs/api/rete-minimap-plugin)[rete-readonly-plugin](/docs/api/rete-readonly-plugin)[rete-angular-plugin](/docs/api/rete-angular-plugin)[@retejs/lit-plugin](/docs/api/rete-lit-plugin)[rete-react-plugin](/docs/api/rete-react-plugin)[rete-svelte-plugin](/docs/api/rete-svelte-plugin)[rete-vue-plugin](/docs/api/rete-vue-plugin)[rete-render-utils](/docs/api/rete-render-utils)[rete-scopes-plugin](/docs/api/rete-scopes-plugin)[rete-dock-plugin](/docs/api/rete-dock-plugin)[rete-comment-plugin](/docs/api/rete-comment-plugin)[rete-connection-path-plugin](/docs/api/rete-connection-path-plugin)[rete-connection-reroute-plugin](/docs/api/rete-connection-reroute-plugin)[FAQ](/docs/faq)[Migration](/docs/migration)# Migration[Rete.js v1](https://rete.js.org)
The current version of the framework contains numerous breaking changes compared to its predecessor.
Let&#39;s, start by exploring  the differences between v1 and v2, both from a developer&#39;s and user&#39;s point of view:
Contextv1v2ReferenceTypeScriptPartial supportTypeScript-firstQuick startCodepen examplesDevKit, Codesandbox examplesArchitectureEvent-basedMiddleware-like signalsTools`rete-cli``rete-cli`, `rete-kit`, `rete-qa`Testingunit testingunit + E2E testing**UI**Nodes orderfixed orderbring forward picked nodesSelectionbuilt-in for nodes onlyadvanced selection + custom elementsControlsno built-in controls providedbuilt-in classic input controlArrange nodeslimitedpowered by `elkjs`**Code**Node creationComponent-based approachup to youEditor/Engine identifiersmandatory, required for import/exportup to youNode identifierincremental decimal idunique idImport/exportBuilt-in, limitedup to youValidationSocket-based validationup to youDataflow processinglimited (no recursion)`DataflowEngine` with dynamic fetchingControl flow processingsimulated by Task plugin with limitations`ControlFlowEngine`Modules`rete-module-plugin`up to youConnection pluginresponsible for both rendering and interactionresponsible for interaction only## [Connecting plugins](#connect-plugins)Connect the plugin by importing it by default import.
The second parameter is used for passing the plugin&#39;s options/parameters:
ts// v1
import HistoryPlugin from &#39;rete-history-plugin&#39;;

editor.use(HistoryPlugin, { keyboard: true });
All plugins are implemented as classes and can be extended, providing flexible customization without modifying the core.
ts// v2
import { HistoryPlugin, HistoryExtensions, Presets } from &#39;rete-history-plugin&#39;

const history = new HistoryPlugin<Schemes>()

history.addPreset(Presets.classic.setup())

HistoryExtensions.keyboard(history)

area.use(history)
## [Creating nodes](#create-nodes)In the v1, nodes are generated via components that were registered within the editor, which enabled the creation of numerous instances of nodes belonging to the same Component type.
ts// v1
class NumComponent extends Rete.Component {
  constructor(){
    super("Number");
  }

  builder(node) {
    node.addControl(new NumControl(&#39;num&#39;))
    node.addOutput(new Rete.Output(&#39;num&#39;, "Number", numSocket))

    return node
  }
}

const numComponent = new NumComponent()
editor.register(numComponent);

const node = await numComponent.createNode({ num: 2 });
The current version doesn&#39;t include Component as an abstraction, but you can implement similar approach if needed.
ts// v2
const node = new ClassicPreset.Node(&#39;Number&#39;)

node.addControl(&#39;num&#39;, new NumControl(&#39;num&#39;))
node.addOutput(&#39;num&#39;, new ClassicPreset.Output(numSocket, "Number"));

await editor.addNode(node)
## [Saving data in a node](#save-data-in-nodes)

The data can be saved using method `putData`. It is expected that the data should be in a valid JSON format, as it may be used for import/export.

```ts
// v1
node.putData('myData', 'data')
control.putData('myData', 'data') // where control is part of node
```

There are no rigid import/export guidelines to follow in the current version, which means you have complete flexibility in how you store your data in nodes.

```ts
// v2
class MyNode extends ClassicPreset.Node {
  myData = 'data'
}
```

## [Import/export](#import-export)

Because of the limitations mentioned earlier, the editor can be effortlessly exported and imported.

```ts
// v1
const data = editor.toJSON();
await editor.fromJSON(data);
```

The current version incorporates a revised approach that requires implementation, as demonstrated in [Import/export](/docs/guides/import-export).

## [Selectable nodes](#selectable-nodes)

Selecting elements is a feature integrated within the editor

```ts
// v1
editor.selected.list

editor.selected.add(node, accumulate)
The downside to this implementation is its incapability to support anything other than node selection.
The selection of nodes (and other elements) looks like:
ts// v2
const selector = AreaExtensions.selector()
const accumulating = AreaExtensions.accumulateOnCtrl()

const nodeSelector = AreaExtensions.selectableNodes(area, selector, { accumulating });

editor.getNodes().filter(node => node.selected)
nodeSelector.select(add.id)
## [Events listening](#events-listening)

The typical way to listen to events that can be prevented

```ts
// v1
editor.on('nodecreate', node => {
 return node.canCreate
});
```

* unchanged

** moved to different package

*** removed

### [`rete` package events](#rete-package-events-v1)- nodecreate *
* nodecreated *
* noderemove *
* noderemoved *
* connectioncreate *
* connectioncreated *
* connectionremove *
* connectionremoved *
* translatenode ***
* nodetranslate **
* nodetranslated **
* nodedraged ***
* nodedragged **
* selectnode ***
* multiselectnode ***
* nodeselect ***
* nodeselected ***
* rendernode ** (renamed to 'render')
* rendersocket ** (renamed to 'render')
* rendercontrol ** (renamed to 'render')
* renderconnection ** (renamed to 'render')
* updateconnection ***
* keydown ***
* keyup ***
* translate **
* translated **
* zoom **
* zoomed **
* click ** (renamed to 'nodepicked')
* mousemove *** (renamed to 'pointermove')
* contextmenu **
* import ***
* export ***
* process ***
* clear **

### [`rete-connection-plugin` package events](#rete-connection-plugin-package-events-v1)

* connectionpath **
* connectiondrop *
* connectionpick *
* resetconnection ***

The current version uses a specific kind of signal implementation that involves object-based signals. Additionally, pipes are used to either manipulate these objects or prevent signal propagation.

```ts
// v2
editor.addPipe(context => {
  if (context.type === 'nodecreate') return
  return context
})
```
### [`rete` package events](#rete-package-events-v2)- nodecreate
- nodecreated
- noderemove
- noderemoved
- connectioncreate
- connectioncreated
- connectionremove
- connectionremoved
- clear
- clearcancelled
- cleared
### [`rete-area-plugin` package events](#rete-area-plugin-package-events)- nodepicked
- nodedragged
- nodetranslate
- nodetranslated
- contextmenu
- pointerdown
- pointermove
- pointerup
- noderesize
- noderesized
- render
- unmount
- reordered
- translate
- translated
- zoom
- zoomed
- resized
### [`rete-connection-plugin` package events](#rete-connection-plugin-package-events-v2)- connectionpick
- connectiondrop
### [`rete-angular-plugin` package events](#rete-angular-plugin-package-events)- connectionpath
### [`rete-vue-plugin` package events](#rete-vue-plugin-package-events)- connectionpath
### [`rete-react-plugin` package events](#rete-react-plugin-package-events)- connectionpath
## [Validate connections](#validate-connections)There is a built-in connection validation based on socket compatibility
ts// v1
const anyTypeSocket = new Rete.Socket(&#39;Any type&#39;);

numSocket.combineWith(anyTypeSocket);
This approach is simple but has some limitations.
Connection validation can be implemented independently, that provides more flexibility.
ts// v2
editor.addPipe(context => {
  if (context.type === &#39;connectioncreate&#39;) {
    if (canCreateConnection(context.data)) return false
  }
  return context
})
## [Engine (dataflow)](#engine)The component with defined `worker` method should be registered
ts// v1
const engine = new Rete.Engine(&#39;[[email&#160;protected]](/cdn-cgi/l/email-protection)&#39;);

engine.register(myComponent);
Define `worker` method of the component
ts// v1
worker(node, inputs, outputs){
  outputs[&#39;num&#39;] = node.data.num;
}
Trigger the processing
ts// v1
await engine.process(data);
Create the `DataflowEngine` instance to connect to the editor. Unlike the first version, there is no need to pass `data` with nodes and connections.
ts// v2
import { DataflowEngine } from &#39;rete-engine&#39;

const engine = new DataflowEngine<Schemes>()

editor.use(engine)
Node method example
ts// v2
data(inputs) {
  const { left, right } = inputs

  return { sum: left[0] + right[0] }
}
Start the processing
ts// v2
engine.fetch(node.id)
## [Task plugin (control flow)](#task-plugin)This approach is implemented using the `rete-task-plugin` and based on the `Rete.Engine`. Therefore, it has the aforementioned limitations
ts// v1
import TaskPlugin from &#39;rete-task-plugin&#39;;

editor.use(TaskPlugin);
Component&#39;s constructor has specified outputs that are intended for control flow or dataflow
ts// v1
this.task = {
    outputs: { exec: &#39;option&#39;, data: &#39;output&#39; },
    init(task) {
        task.run(&#39;any data&#39;);
        task.reset();
    }
}
Define the `worker` method, which returns data and specifies closed output ports for control flow
ts// v1
worker(node, inputs, data) {
    this.closed = [&#39;exec&#39;];
    return { data }
}
The `rete-engine` package is used, which has a separate implementation of the engine for control flow
ts// v2
import { ControlFlowEngine } from &#39;rete-engine&#39;

const engine = new ControlFlowEngine<Schemes>()

editor.use(engine)
By default, all ports are configured to pass control, but you can designate certain ones for this
ts// v2
const engine = new ControlFlowEngine<Schemes>(() => {
  return {
    inputs: () => ["exec"],
    outputs: () => ["exec"]
  };
});
The following serves as the node method:
ts// v2
execute(input: &#39;exec&#39;, forward: (output: &#39;exec&#39;) => void) {
  forward(&#39;exec&#39;)
}
Unlike the previous version, this approach is completely decoupled from the dataflow. Nevertheless, it can be used in conjunction with `DataflowEngine`.
ts// v2
async execute(input: &#39;exec&#39;, forward: (output: &#39;exec&#39;) => void) {
  const inputs = await dataflow.fetchInputs(this.id)

  forward(&#39;exec&#39;)
}
## [Render plugins](#render-plugins)As a demonstration, we have opted to use `rete-react-render-plugin`
ts// v1
import ReactRenderPlugin from &#39;rete-react-render-plugin&#39;;

editor.use(ReactRenderPlugin)
ts// v2
import { ReactPlugin } from &#39;rete-react-plugin&#39;
import { createRoot } from "react-dom/client";

const reactPlugin = new ReactPlugin<Schemes, AreaExtra>({ createRoot })

area.use(reactPlugin)
### [Custom nodes and controls](#custom)The following code is used to specify the components needed for specific nodes and controls
ts// v1
class AddComponent extends Rete.Component {
  constructor() {
    super("Add");
    this.data.component = MyNode;
  }
}

class MyControl extends Rete.Control {
  constructor(emitter, key, name) {
    super(key);
    this.render = &#39;react&#39;;
    this.component = MyReactControl;
    this.props = { emitter, name };
  }
}
Alternatively, component can be specified for all nodes
ts// v1
editor.use(ReactRenderPlugin, { component: MyNode });
In this version, the components to be visualized are defined in the classic preset that is connected
ts// v2
reactPlugin.addPreset(ReactPresets.classic.setup({ customize: {
  node(data) {
    return MyNode
  },
  control() {
    return MyReactControl
  }
}}))
This approach offers greater flexibility, enabling you to define additional conditions within the handlers
## [Translate nodes](#translate-nodes)Retrieve the view of the node and execute its `translate` method
ts// v1
editor.view.nodes.get(node).translate(x, y)
The plugin instance contains `translate` method that only needs the node identifier.
ts// v2
await area.translate(node.id, { x, y })
## [Arrange nodes](#arrange-nodes)The plugin offers approach for positioning nodes, but its functionality is significantly restricted.
ts// v1
import AutoArrangePlugin from &#39;rete-auto-arrange-plugin&#39;;

editor.use(AutoArrangePlugin, {});

editor.trigger(&#39;arrange&#39;);
The plugin leverages the advanced functionality of the `elkjs` package.
ts// v2
import { AutoArrangePlugin, Presets as ArrangePresets } from "rete-auto-arrange-plugin";

const arrange = new AutoArrangePlugin<Schemes>();

arrange.addPreset(ArrangePresets.classic.setup());

area.use(arrange);

await arrange.layout()
## [Fit viewport](#fit-viewport)The `zoomAt` method requires an editor instance that is responsible for visualization
ts// v1
import AreaPlugin from "rete-area-plugin";

AreaPlugin.zoomAt(editor);
For visualization purposes in this version, an instance of `AreaPlugin` is required.
ts// v2
import { AreaExtensions } from "rete-area-plugin";

AreaExtensions.zoomAt(area, editor.getNodes());
Released under the [MIT License](https://opensource.org/license/mit/)Copyright © 2018-2026 Vitaliy Stoliarov