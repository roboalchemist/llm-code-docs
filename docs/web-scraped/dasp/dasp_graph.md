# dasp_graph Documentation
# Source: https://docs.rs/dasp_graph/latest/dasp_graph/

# Crate dasp_graphCopy item path

[Source](../src/dasp_graph/lib.rs.html#1-374)

Expand description

A crate for dynamically creating and editing audio graphs.

`dasp_graph` is targeted towards users who require an efficient yet flexible
and dynamically configurable audio graph. Use cases might include virtual
mixers, digital audio workstations, game audio systems, virtual modular
synthesizers and more.

## §Overview

A `dasp` graph is composed of **nodes** and **edges**.

Each node contains an instance of a type that implements the [`Node`
trait](./node/trait.Node.html). This is normally an audio source (input),
processor (effect) or sink (output). The `Node` trait is the core abstraction
of `dasp_graph` and allows for trivial re-use of audio nodes between projects
and libraries. By implementing `Node` for your audio instruments, effects,
generators and processors, they can be easily composed together within a graph
and shared with future projects or other `dasp` users. `dasp_graph` provides a
suite of popular node implementations out of the box, each of which may be
accessed by enabling [their associated features](./index.html#optional-
features).

The edges of a `dasp` graph are empty and simply describe the direction of
audio flow through the graph. That is, the edge _a - > b_ describes that the
audio output of node _a_ will be used as an input to node _b_.

Once we have added our nodes and edges describing the flow of audio through
our graph, we can repeatedly process and retrieve audio from it using the
[`Processor`](./struct.Processor.html) type.

## §Comparison to `dasp_signal`

While [`dasp_signal`](https://docs.rs/dasp_signal) and its [`Signal`
trait](https://docs.rs/dasp_signal/latest/dasp_signal/trait.Signal.html) are
already well suited towards composing audio graphs, there are certain use
cases where they can cause friction. Use cases that require dynamically adding
or removing nodes, mapping between dynamically changing channel layouts, or
writing the output of one node to multiple others are all difficult to achieve
in an elegant manner using `dasp_signal`.

`dasp_graph` is designed in a manner that better handles these cases. The flat
ownership model where the graph owns all nodes makes it trivial to add or
remove nodes and edges at runtime. Nodes can specify the number of buffers
that they support during construction, making it easy to handle different
channel layouts. Adding multiple outputs to a node (including predecessors to
enable cycles) is trivial due to `dasp_graph`’s requirement for a fixed sample
rate across the whole graph.

On the other hand, `dasp_graph`’s requirement for a fixed sample rate can also
be a limitation. A `dasp_graph` cannot be composed of nodes with differing
input sample rates meaning it is unsuitable for writing a streaming sample
rate converter. `dasp_graph`’s fixed buffer size results in another
limitation. It implies that when creating a cycle within the graph, a minimum
delay of `Buffer::LEN` is incurred at the edge causing the cycle. This makes
it tricky to compose per-sample feedback delays by using cycles in the graph.

Feature| `dasp_graph`| `dasp_signal`  
---|---|---  
Easily dynamically add/remove nodes/edges| ✓| ✗  
Easily write output of node to multiple others| ✓| ✗  
Dynamic channel layout| ✓| ✗  
Efficiently implement per-sample feedback| ✗| ✓  
Support variable input sample rate per node| ✗| ✓  
  
In general, `dasp_signal` tends to be better suited towards the composition of
fixed or static graphs where the number of channels are known ahead of time.
It is perfect for small, fixed, static graph structures like a simple
standalone synthesizer/sampler or small processors/effects like sample-rate
converters or pitch shifters. `dasp_graph` on the other hand is better suited
at a higher level where flexibility is a priority, e.g. a virtual mixing
console or, the underlying graph for a digital audio workstation or a virtual
modular synthesizer.

Generally, it is likely that `dasp_signal` will be more useful for writing
`Node` implementations for audio sources and effects, while `dasp_graph` will
be well suited to dynamically composing these nodes together in a flexible
manner.

## §Graph types

Rather than providing a fixed type of graph to work with, `dasp_graph`
utilises the `petgraph` traits to expose a generic interface allowing users to
select the graph type that bests suits their application or implement their
own.

**Graph**

The
[`petgraph::graph::Graph`](https://docs.rs/petgraph/latest/petgraph/graph/struct.Graph.html)
type is a standard graph type exposed by `petgraph`. The type is simply an
interface around two `Vec`s, one containing the nodes and one containing the
edges. Adding nodes returns a unique identifier that can be used to index into
the graph. As long as the graph is intialised with a sufficient capacity for
both `Vec`s, adding nodes while avoiding dynamic allocation is simple.

**StableGraph**

One significant caveat with the `Graph` type is that removing a node
invalidates any existing indices that refer to the following nodes stored
within the graph’s node `Vec`. The
[`petgraph::stable_graph::StableGraph`](https://docs.rs/petgraph/latest/petgraph/stable_graph/struct.StableGraph.html)
type avoids this issue by storing each node in and enum. When a node is
“removed”, the element simply switches to a variant that indicates its slot is
available for use the next time `add_node` is called.

In summary, if you require the ability to dynamically remove nodes from your
graph you should prefer the `StableGraph` type. Otherwise, the `Graph` type is
likely well suited.

If neither of these graphs fit your use case, consider implementing the
necessary petgraph traits for your own graph type. You can find the necessary
traits by checking the trait bounds on the graph argument to the `dasp_graph`
functions you intend to use.

## §Optional Features

Each of the provided node implementations are available by default, however
these may be disabled by disabling default features. You can then enable only
the implementations you require with the following features:

  * The **node-boxed** feature provides a `Node` implementation for `Box<dyn Node>`. This is particularly useful for working with a graph composed of many different node types.
  * The **node-graph** feature provides an implementation of `Node` for a type that encapsulates another `dasp` graph type. This allows for composing individual nodes from graphs of other nodes.
  * The **node-signal** feature provides an implementation of `Node` for `dyn Signal`. This is useful when designing nodes using `dasp_signal`.
  * The **node-delay** feature provides a simple multi-channel `Delay` node.
  * The **node-pass** feature provides a `Pass` node that simply passes audio from its inputs to its outputs.
  * The **node-sum** feature provides `Sum` and `SumBuffers` `Node` implementations. These are useful for mixing together multiple inputs, and for simple mappings between different channel layouts.

#### §no_std

*TODO: Adding support for `no_std` is pending the addition of support for `no_std` in petgraph. See https://github.com/petgraph/petgraph/pull/238.

## Re-exports§

`pub use node::[Input](node/struct.Input.html "struct
dasp_graph::node::Input");`

`pub use node::[Node](node/trait.Node.html "trait dasp_graph::node::Node");`

`pub use node::[BoxedNode](node/struct.BoxedNode.html "struct
dasp_graph::node::BoxedNode");`

`pub use node::[BoxedNodeSend](node/struct.BoxedNodeSend.html "struct
dasp_graph::node::BoxedNodeSend");`

## Modules§

[node](node/index.html "mod dasp_graph::node")

## Structs§

[Buffer](struct.Buffer.html "struct dasp_graph::Buffer")

    The fixed-size buffer used for processing the graph.
[NodeData](struct.NodeData.html "struct dasp_graph::NodeData")

    For use as the node weight within a dasp graph. Contains the node and its buffers.
[Processor](struct.Processor.html "struct dasp_graph::Processor")

    State related to the processing of an audio graph of type `G`.

## Functions§

[process](fn.process.html "fn dasp_graph::process")

    Process audio through the subgraph ending at the node with the given ID.
[sinks](fn.sinks.html "fn dasp_graph::sinks")

    Produce an iterator yielding IDs for all **sink** nodes within the graph.
[sources](fn.sources.html "fn dasp_graph::sources")

    Produce an iterator yielding IDs for all **source** nodes within the graph.

