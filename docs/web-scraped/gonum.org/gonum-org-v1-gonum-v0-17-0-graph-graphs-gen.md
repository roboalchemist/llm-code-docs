# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen

Title: gen package - gonum.org/v1/gonum/graph/graphs/gen - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen

Markdown Content:
Package gen provides random graph generation functions.

*   [func BipartitePowerLaw(dst graph.MultigraphBuilder, n, d int, src rand.Source) (p1, p2 []graph.Node, err error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#BipartitePowerLaw)
*   [func Complete(dst NodeIDGraphBuilder, ids IDer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#Complete)
*   [func Cycle(dst NodeIDGraphBuilder, cycle IDer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#Cycle)
*   [func Duplication(dst UndirectedMutator, n int, delta, alpha, sigma float64, src rand.Source) error](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#Duplication)
*   [func Gnm(dst GraphBuilder, n, m int, src rand.Source) error](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#Gnm)
*   [func Gnp(dst graph.Builder, n int, p float64, src rand.Source) error](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#Gnp)
*   [func NavigableSmallWorld(dst GraphBuilder, dims []int, p, q int, r float64, src rand.Source) (err error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#NavigableSmallWorld)
*   [func Path(dst NodeIDGraphBuilder, path IDer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#Path)
*   [func PowerLaw(dst graph.MultigraphBuilder, n, d int, src rand.Source) error](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#PowerLaw)
*   [func PreferentialAttachment(dst graph.UndirectedBuilder, n, m int, src rand.Source) error](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#PreferentialAttachment)
*   [func SmallWorldsBB(dst GraphBuilder, n, d int, p float64, src rand.Source) error](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#SmallWorldsBB)
*   [func Star(dst NodeIDGraphBuilder, center int64, leaves IDer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#Star)
*   [func Tree(dst NodeIDGraphBuilder, n int, nodes IDer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#Tree)
*   [func TunableClusteringScaleFree(dst graph.UndirectedBuilder, n, m int, p float64, src rand.Source) error](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#TunableClusteringScaleFree)
*   [func Wheel(dst NodeIDGraphBuilder, center int64, cycle IDer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#Wheel)
*   [type GraphBuilder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#GraphBuilder)
*   [type IDRange](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDRange)
*       *   [func (r IDRange) ID(i int) int64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDRange.ID)
    *   [func (r IDRange) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDRange.Len)

*   [type IDSet](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDSet)
*       *   [func (s IDSet) ID(i int) int64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDSet.ID)
    *   [func (s IDSet) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDSet.Len)

*   [type IDer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDer)
*   [type NodeIDGraphBuilder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#NodeIDGraphBuilder)
*   [type UndirectedMutator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#UndirectedMutator)

*   [Complete (BiDirectedSet)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#example-Complete-BiDirectedSet)
*   [Complete (DirectedSet)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#example-Complete-DirectedSet)
*   [Complete (UndirectedSet)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#example-Complete-UndirectedSet)
*   [Path (DirectedSet)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#example-Path-DirectedSet)
*   [Star (UndirectedRange)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#example-Star-UndirectedRange)
*   [Tree (UndirectedRange)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#example-Tree-UndirectedRange)
*   [Wheel (DirectedRange)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#example-Wheel-DirectedRange)

This section is empty.

This section is empty.

BipartitePowerLaw constructs a bipartite power-law degree graph by preferential attachment in dst with 2×n nodes and minimum degree d. BipartitePowerLaw does not consider nodes in dst prior to the call. The two partitions are returned in p1 and p2. If src is not nil it is used as the random source, otherwise rand.IntN is used. The graph is constructed in O(nd) — O(n+m) — time.

The algorithm used is described in [http://algo.uni-konstanz.de/publications/bb-eglrn-05.pdf](http://algo.uni-konstanz.de/publications/bb-eglrn-05.pdf)

func Complete(dst [NodeIDGraphBuilder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#NodeIDGraphBuilder), ids [IDer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDer))

Complete constructs a complete graph in dst using nodes with the given IDs. If any ID appears twice in ids, Complete will panic.

Output:

strict digraph complete { // Node definitions. 2; 4; 5; 9; // Edge definitions. 2 -> 4; 2 -> 5; 2 -> 9; 4 -> 2; 4 -> 5; 4 -> 9; 5 -> 2; 5 -> 4; 5 -> 9; 9 -> 2; 9 -> 4; 9 -> 5; } 

Output:

strict digraph complete { // Node definitions. 2; 4; 5; 9; // Edge definitions. 2 -> 4; 2 -> 5; 2 -> 9; 4 -> 5; 4 -> 9; 5 -> 9; } 

Output:

strict graph complete { // Node definitions. 2; 4; 5; 9; // Edge definitions. 2 -- 4; 2 -- 5; 2 -- 9; 4 -- 5; 4 -- 9; 5 -- 9; } 

func Cycle(dst [NodeIDGraphBuilder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#NodeIDGraphBuilder), cycle [IDer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDer))

Cycle constructs a cycle in dst using the node IDs in cycle. If dst is a directed graph, edges are directed from earlier nodes to later nodes in cycle. If any ID appears twice in cycle, Cycle will panic.

Duplication constructs a graph in the destination, dst, of order n. New nodes are created by duplicating an existing node and all its edges. Each new edge is deleted with probability delta. Additional edges are added between the new node and existing nodes with probability alpha/|V|. An exception to this addition rule is made for the parent node when sigma is not NaN; in this case an edge is created with probability sigma. With the exception of the sigma parameter, this corresponds to the completely correlated case in doi:10.1016/S0022-5193(03)00028-6. If src is not nil it is used as the random source, otherwise rand.Float64 is used.

Gnm constructs a Erdős-Rényi model subgraph in the destination, dst, of order n and size m. If src is not nil it is used as the random source, otherwise rand.IntN is used. The graph is constructed in O(m) expected time for m ≤ (n choose 2)/2.

Gnp constructs a Gilbert’s model subgraph in the destination, dst, of order n. Edges between nodes are formed with the probability, p. If src is not nil it is used as the random source, otherwise rand.Float64 is used. The graph is constructed in O(n+m) time where m is the number of edges added.

NavigableSmallWorld constructs an N-dimensional grid with guaranteed local connectivity and random long-range connectivity as a subgraph in the destination, dst. The dims parameters specifies the length of each of the N dimensions, p defines the Manhattan distance between local nodes, and q defines the number of out-going long-range connections from each node. Long-range connections are made with a probability proportional to |d(u,v)|^-r where d is the Manhattan distance between non-local nodes.

The algorithm is essentially as described on p4 of [http://www.cs.cornell.edu/home/kleinber/swn.pdf](http://www.cs.cornell.edu/home/kleinber/swn.pdf).

func Path(dst [NodeIDGraphBuilder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#NodeIDGraphBuilder), path [IDer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDer))

Path constructs a path graph in dst with If dst is a directed graph, edges are directed from earlier nodes to later nodes in path. If any ID appears twice in path, Path will panic.

Output:

strict digraph path { // Node definitions. 2; 4; 5; 9; // Edge definitions. 2 -> 4; 4 -> 5; 5 -> 9; } 

PowerLaw constructs a power-law degree graph by preferential attachment in dst with n nodes and minimum degree d. PowerLaw does not consider nodes in dst prior to the call. If src is not nil it is used as the random source, otherwise rand.IntN is used. The graph is constructed in O(nd) — O(n+m) — time.

The algorithm used is described in [http://algo.uni-konstanz.de/publications/bb-eglrn-05.pdf](http://algo.uni-konstanz.de/publications/bb-eglrn-05.pdf)

PreferentialAttachment constructs a graph in the destination, dst, of order n. The graph is constructed successively starting from an m order graph with one node having degree m-1. At each iteration of graph addition, one node is added with m additional edges joining existing nodes with probability proportional to the nodes' degrees. If src is not nil it is used as the random source, otherwise rand.Float64 is used for the random number generator.

The algorithm is essentially as described in [http://arxiv.org/abs/cond-mat/0110452](http://arxiv.org/abs/cond-mat/0110452) after 10.1126/science.286.5439.509.

SmallWorldsBB constructs a small worlds subgraph of order n in the destination, dst. Node degree is specified by d and edge replacement by the probability, p. If src is not nil it is used as the random source, otherwise rand.Float64 is used. The graph is constructed in O(nd) time.

The algorithm used is described in [http://algo.uni-konstanz.de/publications/bb-eglrn-05.pdf](http://algo.uni-konstanz.de/publications/bb-eglrn-05.pdf)

func Star(dst [NodeIDGraphBuilder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#NodeIDGraphBuilder), center [int64](https://pkg.go.dev/builtin#int64), leaves [IDer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDer))

Star constructs a star graph in dst with edges between the center node ID to node with IDs specified in leaves. If dst is a directed graph, edges are directed from the center node to the leaves. If any ID appears twice in leaves and center, Star will panic.

Output:

strict graph star { // Node definitions. 0; 1; 2; 3; 4; 5; 6; // Edge definitions. 0 -- 1; 0 -- 2; 0 -- 3; 0 -- 4; 0 -- 5; 0 -- 6; } 

func Tree(dst [NodeIDGraphBuilder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#NodeIDGraphBuilder), n [int](https://pkg.go.dev/builtin#int), nodes [IDer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDer))

Tree constructs an n-ary tree breadth-first in dst with the given fan-out, n. If the number of nodes does not equal \sum_{i=0}^h n^i, where h is an integer indicating the height of the tree, a partial tree will be constructed with not all nodes having zero or n children, and not all leaves being h from the root. If the number of nodes is greater than one, n must be non-zero and less than the number of nodes, otherwise Tree will panic. If dst is a directed graph, edges are directed from the root to the leaves. If any ID appears more than once in nodes, Tree will panic.

Output:

strict graph full_binary_tree_undirected { // Node definitions. 0; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; // Edge definitions. 0 -- 1; 0 -- 2; 1 -- 3; 1 -- 4; 2 -- 5; 2 -- 6; 3 -- 7; 3 -- 8; 4 -- 9; 4 -- 10; 5 -- 11; 5 -- 12; 6 -- 13; 6 -- 14; } 

TunableClusteringScaleFree constructs a subgraph in the destination, dst, of order n. The graph is constructed successively starting from an m order graph with one node having degree m-1. At each iteration of graph addition, one node is added with m additional edges joining existing nodes with probability proportional to the nodes' degrees. The edges are formed as a triad with probability, p. If src is not nil it is used as the random source, otherwise rand.Float64 and rand.IntN are used for the random number generators.

The algorithm is essentially as described in [http://arxiv.org/abs/cond-mat/0110452](http://arxiv.org/abs/cond-mat/0110452).

func Wheel(dst [NodeIDGraphBuilder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#NodeIDGraphBuilder), center [int64](https://pkg.go.dev/builtin#int64), cycle [IDer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDer))

Wheel constructs a wheel graph in dst with edges from the center node ID to node with IDs specified in cycle and between nodes with IDs adjacent in the cycle. If dst is a directed graph, edges are directed from the center node to the cycle and from earlier nodes to later nodes in cycle. If any ID appears twice in cycle and center, Wheel will panic.

Output:

strict digraph wheel { // Node definitions. 0; 1; 2; 3; 4; 5; 6; // Edge definitions. 0 -> 1; 0 -> 2; 0 -> 3; 0 -> 4; 0 -> 5; 0 -> 6; 1 -> 2; 2 -> 3; 3 -> 4; 4 -> 5; 5 -> 6; 6 -> 1; } 

GraphBuilder is a graph that can have nodes and edges added.

type IDRange struct{ First, Last [int64](https://pkg.go.dev/builtin#int64) }

IDRange is an IDer that provides a set of IDs in [First, Last].

func (r [IDRange](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/graphs/gen#IDRange)) Len() [int](https://pkg.go.dev/builtin#int)

IDSet is an IDer providing an explicit set of IDs.

IDer is a mapping from an index to a node ID.

NodeIDGraphBuilder is a graph that can create new nodes with specified IDs.

UndirectedMutator is an undirected graph builder that can remove edges.
