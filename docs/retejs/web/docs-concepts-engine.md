# Concepts - Engine

Source: https://retejs.org/docs/concepts/engine

---

Engine - Rete.js

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

## Engine

Architecture The `rete-engine` is a package that implements two approaches for processing graph: [Dataflow](#dataflow) and [Control flow](#control-flow).

## Dataflow

The dataflow approach is focused solely on data, where the target node requests data from incoming nodes. Graph processing proceeds from left to right, passing the output of nodes as input arguments to outgoing nodes
This approach is commonly used in products with node editors such as Blender.

The code below represents the basic constructs required for the `DataflowEngine` to work:

- **Nodes must implement a `data` method**: this method accepts data from incoming nodes
- **Connect the engine to the editor**: the engine will register every added node for further processing
- **Fetching node data**: `fetch` initiates a graph traversal starting from the target node and visiting all its predecessors

```ts
import { ClassicPreset } from 'rete-engine'
import { DataflowEngine } from &#39;rete-engine&#39;

const { Node, Socket } = ClassicPreset

class NodeAdd extends Node<{ left: Socket, right: Socket }, { value: Socket }, { }> {

  constructor() {
    // init controls and ports
  }

  // mandatory method
  data(inputs: { left?: number[], right?: number[] }): { value: number } {
    const left = inputs.left[0] || 0
    const right = inputs.right[0] || 0

  return {
      value: left + right
    }
  }
}

const engine = new DataflowEngine<Schemes>()

editor.use(engine)

const nodeOutput = await engine.fetch(resultNode.id)
```

## Control flow

Control flow is a node traversal approach that allows you to determine how to pass control to the next nodes. The processing starts at the start node, which specifies how control is passed through its outgoing connections. For instance, it can be a delay or a branching. The closest example is UE4 Blueprints.

```ts
import { ControlFlowEngine } from 'rete-engine'

const { Node, Socket } = ClassicPreset

class Log extends Node<{ enter: Socket }, { out: Socket }, {}> {
  constructor() {
    // init ports
  }

  // mandatory method
  execute(input: &#39;enter&#39;, forward: (output: &#39;out&#39;) => void) {
    console.log(&#39;log something&#39;)
    forward(&#39;out&#39;)
  }
}

const engine = new ControlFlowEngine<Schemes>()

editor.use(engine)

engine.execute(startNode.id)
```

## Hybrid

In addition, these approaches can be combined. For example, ports named 'exec' can be used to control flow, while other ports manage data.

```ts
const controlflow = new ControlFlowEngine<Schemes>(node => {
  return {
    inputs: () => [&#39;exec&#39;],
    outputs: () => [&#39;exec&#39;]
  }
})
const dataflow = new DataflowEngine<Schemes>(({ inputs, outputs }) => {
  return {
    inputs: () => Object.keys(inputs).filter(name => name !== &#39;exec&#39;),
    outputs: () => Object.keys(outputs).filter(name => name !== &#39;exec&#39;)
  }
})
```

Alternatively, you can use the `Dataflow` and `ControlFlow` classes directly, affording more precise control over the graph processing.

```ts
import { ControlFlow, Dataflow } from 'rete-engine'

const control = new ControlFlow(editor)
const dataflow = new Dataflow(editor)

control.add(startNode, {
  inputs: () => [],
  outputs: () => [&#39;exec&#39;],
  async execute(input, forward) {
    const inputs = await dataflow.fetchInputs(startNode.id)

    forward(&#39;exec&#39;)
  }
})
dataflow.add(startNode, {
  inputs: () => [&#39;data&#39;],
  outputs: () => [&#39;data&#39;],
  data(fetchInputs) {
    const inputs = await fetchInputs()
    const data = {
      data: inputs.data[0] // forward input data (assuming there is only one input connection to port "data")
    }

    return data
  }
})
```

## Conclusion

This engine version incorporates revised approaches to graph processing and addresses the shortcomings of the previous version, which was initially geared towards strict dataflow without recursion support.

When it comes to graph processing, there's no one-size-fits-all solution. In simple cases, you can use `DataflowEngine` and `ControlFlowEngine`, while in more complex cases, you can use `ControlFlow` and `Dataflow` or write your own solution by studying [the source code](https://github.com/retejs/engine) of the `rete-engine` package.

Released under the [MIT License](https://opensource.org/license/mit/)Copyright © 2018-2026 Vitaliy Stoliarov
