# Guide - Control Flow Engine

Source: https://retejs.org/docs/guides/processing/control-flow

---

Control flow - Rete.js

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
[API](/docs/api)[Overview](/docs/api/overview)[rete](/docs/api/rete)[rete-area-plugin](/docs/api/rete-area-plugin)[rete-area-3d-plugin](/docs/api/rete-area-3d-plugin)[rete-connection-plugin](/docs/api/rete-connection-plugin)[rete-auto-arrange-plugin](/docs/api/rete-auto-arrange-plugin)[rete-context-menu-plugin](/docs/api/rete-context-menu-plugin)[rete-engine](/docs/api/rete-engine)[rete-history-plugin](/docs/api/rete-history-plugin)[rete-minimap-plugin](/docs/api/rete-minimap-plugin)[rete-readonly-plugin](/docs/api/rete-readonly-plugin)[rete-angular-plugin](/docs/api/rete-angular-plugin)[@retejs/lit-plugin](/docs/api/rete-lit-plugin)[rete-react-plugin](/docs/api/rete-react-plugin)[rete-svelte-plugin](/docs/api/rete-svelte-plugin)[rete-vue-plugin](/docs/api/rete-vue-plugin)[rete-render-utils](/docs/api/rete-render-utils)[rete-scopes-plugin](/docs/api/rete-scopes-plugin)[rete-dock-plugin](/docs/api/rete-dock-plugin)[rete-comment-plugin](/docs/api/rete-comment-plugin)[rete-connection-path-plugin](/docs/api/rete-connection-path-plugin)[rete-connection-reroute-plugin](/docs/api/rete-connection-reroute-plugin)[FAQ](/docs/faq)[Migration](/docs/migration)# Control flowNot familiar with Control flow concept? Check out the [Control flow](/docs/concepts/engine#control-flow) article to get up to speed
[Control flow](/examples/processing/control-flow)[Plugin](https://github.com/retejs/engine)
## [Install dependencies](#install-dependencies)Want to start faster? Use [Rete Kit](/docs/development/rete-kit) to create a fully configured project in minutes!Copy the command npx rete-kit app to clipboard[Learn More](/docs/development/rete-kit)bashnpm i rete rete-engine
## [Prepare nodes](#prepare-nodes)Let&#39;s take a simple example of a graph with two types of nodes: `Log` and `Delay`. These nodes can perform specific operations and pass control to outgoing nodes in a certain way
At the end of the article, you can find a link to the full example that includes visual components.
Defining a node class that logs a message and passes control to outgoing nodes via the `exec` port:
tsconst socket = new ClassicPreset.Socket("socket");

class Log extends ClassicPreset.Node {
  constructor(public message: string) {
    super("Log");

    this.addInput("exec", new ClassicPreset.Input(socket, "Exec", true));
    this.addOutput("exec", new ClassicPreset.Output(socket, "Exec"));
  }

  execute(input: "exec", forward: (output: "exec") => void) {
    console.log(this.message);
    forward("exec");
  }
}
Defining a class that handles delays, where the only purpose is to pass control to outgoing nodes through the `exec` port after a specified timeout:
tsclass Delay extends ClassicPreset.Node {
  constructor(private seconds: number) {
    super("Delay");
    this.addInput("exec", new ClassicPreset.Input(socket, "Exec", true));
    this.addOutput("exec", new ClassicPreset.Output(socket, "Exec"));
  }

  execute(input: "exec" | undefined, forward: (output: "exec") => void) {
    setTimeout(() => forward("exec"), seconds * 1000)
  }
}

class Connection<A extends NodeProps, B extends NodeProps> extends ClassicPreset.Connection<A, B> {}

type NodeProps = Start | Log | Delay;
type ConnProps =
  | Connection<Start, Log>
  | Connection<Delay, Log>
  | Connection<Log, Delay>
  | Connection<Log, Log>
  | Connection<Delay, Delay>;
type Schemes = GetSchemes<NodeProps, ConnProps>;
## [Connect](#connect)tsimport { ControlFlowEngine } from "rete-engine";
import { NodeEditor } from "rete";

const editor = new NodeEditor<Schemes>();
const engine = new ControlFlowEngine<Schemes>();

editor.use(engine);
## [Add nodes and connections](#add-nodes-and-connections)Let&#39;s add a sequence of nodes in the form of Log -> Delay -> Log
tsconst log1 = new Log("log before delay");
const delay = new Delay(2);
const log2 = new Log("log after delay");

const con2 = new Connection(log1, "exec", delay, "exec");
const con3 = new Connection(delay, "exec", log2, "exec");

await editor.addNode(log1);
await editor.addNode(delay);
await editor.addNode(log2);

await editor.addConnection(con2);
await editor.addConnection(con3);
## [Execution](#execution)The node `log1` serves as the starting point for the graph execution.
tsengine.execute(log1.id);
This operation triggers the `execute` method of the `Log` class, with `undefined` as the `input` parameter because the node was directly called, without being passed from an incoming node.
Then, calling `forward("exec")` passes control to all the outgoing nodes. In our case, the `Delay` node does the same thing but after a delay using `setTimeout`.
Logs:
log"log before delay"
// delay for 2 seconds
"log after delay"
Check out the complete result on the [Control flow](/examples/processing/control-flow) example page.
Released under the [MIT License](https://opensource.org/license/mit/)Copyright © 2018-2026 Vitaliy Stoliarov