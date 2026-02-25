# Guide - Data Structures

Source: https://retejs.org/docs/guides/data-structures

---

Data structures - Rete.js

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
[API](/docs/api)[Overview](/docs/api/overview)[rete](/docs/api/rete)[rete-area-plugin](/docs/api/rete-area-plugin)[rete-area-3d-plugin](/docs/api/rete-area-3d-plugin)[rete-connection-plugin](/docs/api/rete-connection-plugin)[rete-auto-arrange-plugin](/docs/api/rete-auto-arrange-plugin)[rete-context-menu-plugin](/docs/api/rete-context-menu-plugin)[rete-engine](/docs/api/rete-engine)[rete-history-plugin](/docs/api/rete-history-plugin)[rete-minimap-plugin](/docs/api/rete-minimap-plugin)[rete-readonly-plugin](/docs/api/rete-readonly-plugin)[rete-angular-plugin](/docs/api/rete-angular-plugin)[@retejs/lit-plugin](/docs/api/rete-lit-plugin)[rete-react-plugin](/docs/api/rete-react-plugin)[rete-svelte-plugin](/docs/api/rete-svelte-plugin)[rete-vue-plugin](/docs/api/rete-vue-plugin)[rete-render-utils](/docs/api/rete-render-utils)[rete-scopes-plugin](/docs/api/rete-scopes-plugin)[rete-dock-plugin](/docs/api/rete-dock-plugin)[rete-comment-plugin](/docs/api/rete-comment-plugin)[rete-connection-path-plugin](/docs/api/rete-connection-path-plugin)[rete-connection-reroute-plugin](/docs/api/rete-connection-reroute-plugin)[FAQ](/docs/faq)[Migration](/docs/migration)# Data structuresSimilar to a graph, this framework contains data as nodes and edges. One correction: in the editor&#39;s terminology, the graph edges are known as connections.
The `NodeEditor` instance stores this data in a normalized format, specifically as two distinct lists containing objects of the following type:
- `{ id: <string> }` for a nodes
- `{ id: <string>, source: <string>, target: <string> }` for a connections
NodeEditorInitializing the editor involves using a basic scheme without any supplementary fields to start with:
tsimport { NodeEditor, BaseSchemes, getUID } from &#39;rete&#39;

const editor = new NodeEditor<BaseSchemes>()
## [Add nodes and connections](#add-nodes-and-connections)When dealing with graph data, you have the option to create arbitrary identifiers for nodes and connections, or utilize the existing ones.
tsconst a = { id: getUID() }
const b = { id: getUID() }
const connection = { id: getUID(), source: a.id, target: b.id }

await editor.addNode(a)
await editor.addNode(b)
await editor.addConnection(connection)
## [Retrieve nodes and connections](#retrieve-nodes-and-connections)We can now retrieve a list of newly added nodes and connections
tseditor.getNodes() // returns [a, b]
editor.getConnections() // returns [connection]
You have all the necessary methods to process the graph, such as retrieving a list of input connections or all incoming nodes, as we will discuss in the following sections.
## [Incoming/outgoing connections](#incoming-outgoing-connections)Incoming/outgoing connectionsThe following code shows how to retrieve a list of incoming and outgoing connections for `node`:
tsconst connections = editor.getConnections()

const incomingConnections = connections.filter(connection => connection.target === node.id)
const outgoingConnections = connections.filter(connection => connection.source === node.id)
## [Incoming/outgoing nodes](#incoming-outgoing-nodes)Incoming/outgoing nodesWe can use variables from the previous section to retrieve incoming or outgoing nodes:
tsconst incomers = incomingConnections.map(connection => editor.getNode(connection.source))
const outgoers = outgoingConnections.map(connection => editor.getNode(connection.target))
In general, this is sufficient for simple cases, but if there are more than one connections between nodes, we will have to remove duplicates:
tsArray.from(new Set(incomers))
Array.from(new Set(outgoers))
## [Advanced methods](#advanced-methods)The previously mentioned approaches are fairly flexible, but they require the implementation of more advanced methods on your own. Fortunately, the [`rete-structures` package](https://github.com/retejs/structures) offers such methods divided into 4 categories:
- **Mapping**: iterating through a list of nodes while transforming or filtering it
- **Sets**: techniques for working with graphs as sets, including union, difference and intersection.
- **Subgraph**: graphs that have parent-child relationships between nodes.
- **Traverse**: traversing nodes by their connections, such as retrieving only incoming nodes or all predecessors.
rete-structures### [Usage](#rete-structures-usage)Install the dependency
bashnpm i rete-structures
Use the following import statement and declaration
tsimport { structures } from &#39;rete-structures&#39;

const graph = structures(editor)

graph.nodes()
graph.connections()
There are other `graph` methods that serve distinct purposes, demonstrated below with code and an interactive preview. The resulting nodes are prominent and the preview allows users to select nodes and observe changes.
The execution of any of the methods usually yields nodes that were not discarded, as well as their connections if both of their nodes are present.
### [Traverse](#traverse)#### [Roots](#roots)Nodes without incoming connections are known as root nodes
tsstructures(graph).roots()
Preview needs JS to be enabled#### [Leaves](#leaves)Leaf nodes are those that have no outgoing connections
tsstructures(graph).leaves()
Preview needs JS to be enabled#### [Incomers](#incomers)Incoming nodes directly connected to the selected node
tsstructures(graph).incomers(selectedNodeId)
Preview needs JS to be enabled#### [Outgoers](#outgoers)Outgoing nodes directly connected to the selected node
tsstructures(graph).outgoers(selectedNodeId)
Preview needs JS to be enabled#### [Predecessors](#predecessors)Every incoming node, as well as its own incoming nodes and so on
tsstructures(graph).predecessors(selectedNodeId)
Preview needs JS to be enabled#### [Successors](#successors)Every outgoing node, as well as its own outgoing nodes and so on
tsstructures(graph).successors(selectedNodeId)
Preview needs JS to be enabled### [Mapping](#mapping)#### [Filter](#filter)Filtering can be applied to both nodes and connections
tsstructures(graph).filter(Boolean, ({ source, target }) => source === selectedNodeId || target === selectedNodeId)
Preview needs JS to be enabled### [Sets](#sets)The following examples shows the cases where selected node serves as the second graph.
#### [Union](#union)The union of a graph and a node from this graph gives the same graph
tsstructures(editor).union({ nodes: [selectedNode], connections: [] })
Preview needs JS to be enabled#### [Difference](#difference)By subtracting the node from the graph, you can obtain a new graph without that node
tsstructures(editor).difference({ nodes: [selectedNode], connections: [] })
Preview needs JS to be enabled#### [Intersection](#intersection)By intersecting the graph with the node from this graph, you&#39;ll get a new graph that includes only the selected node
tsstructures(editor).intersection({ nodes: [selectedNode], connections: [] })
Preview needs JS to be enabled### [Subgraph](#subgraph)This category pertains to graphs that contain nodes with a parent-child relationship, specifically, nodes that have a `parent` field defined and are nested within other nodes.
#### [Children](#children)The list of direct descendant, namely children
tsstructures(editor).children((n) => n.id === selectedNodeId);
Preview needs JS to be enabled#### [Parent](#parent)The list of parents
tsstructures(editor).parents((n) => n.id === selectedNodeId);
Preview needs JS to be enabled#### [Descendants](#descendants)The list of all descendants, including children, grandchildren and successive generations
tsstructures(editor).descendants((n) => n.id === selectedNodeId);
Preview needs JS to be enabled#### [Ancestors](#ancestors)The list of all ancestors, from parents to great-grandparents and beyond
tsstructures(editor).ancestors((n) => n.id === selectedNodeId);
Preview needs JS to be enabled#### [Orphans](#orphans)Nodes without a specified `parent` property
tsstructures(editor).orphans();
Preview needs JS to be enabled#### [Siblings](#siblings)Nodes that have a common parent with the selected node, even if it has no parent
tsstructures(editor).siblings((n) => n.id === selectedNodeId)
Preview needs JS to be enabledReleased under the [MIT License](https://opensource.org/license/mit/)Copyright © 2018-2026 Vitaliy Stoliarov