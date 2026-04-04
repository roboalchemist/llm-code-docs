# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph

Title: testgraph package - gonum.org/v1/gonum/graph/testgraph - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph

Markdown Content:
Package testgraph provides a set of testing helper functions that test Gonum graph interface implementations.

*   [func AddArbitraryNodes(t *testing.T, g NodeAdder, add graph.Nodes)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#AddArbitraryNodes)
*   [func AddEdges(t *testing.T, n int, g EdgeAdder, newNode func(id int64) graph.Node, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#AddEdges)
*   [func AddLines(t *testing.T, n int, g LineAdder, newNode func(id int64) graph.Node, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#AddLines)
*   [func AddNodes(t *testing.T, g NodeAdder, n int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#AddNodes)
*   [func AddWeightedEdges(t *testing.T, n int, g WeightedEdgeAdder, w float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#AddWeightedEdges)
*   [func AddWeightedLines(t *testing.T, n int, g WeightedLineAdder, w float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#AddWeightedLines)
*   [func AdjacencyMatrix(t *testing.T, b Builder)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#AdjacencyMatrix)
*   [func EdgeExistence(t *testing.T, b Builder, reversedEdge bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#EdgeExistence)
*   [func LineExistence(t *testing.T, b Builder, useEmpty, reversedLine bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#LineExistence)
*   [func NoLoopAddEdges(t *testing.T, n int, g EdgeAdder, newNode func(id int64) graph.Node)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#NoLoopAddEdges)
*   [func NoLoopAddWeightedEdges(t *testing.T, n int, g WeightedEdgeAdder, w float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#NoLoopAddWeightedEdges)
*   [func NodeExistence(t *testing.T, b Builder)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#NodeExistence)
*   [func RemoveEdges(t *testing.T, g EdgeRemover, remove graph.Edges)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RemoveEdges)
*   [func RemoveLines(t *testing.T, g LineRemover, remove graph.Lines)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RemoveLines)
*   [func RemoveNodes(t *testing.T, g NodeRemover)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RemoveNodes)
*   [func ReturnAdjacentNodes(t *testing.T, b Builder, useEmpty, reversedEdge bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#ReturnAdjacentNodes)
*   [func ReturnAllEdges(t *testing.T, b Builder, useEmpty bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#ReturnAllEdges)
*   [func ReturnAllLines(t *testing.T, b Builder, useEmpty bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#ReturnAllLines)
*   [func ReturnAllNodes(t *testing.T, b Builder, useEmpty bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#ReturnAllNodes)
*   [func ReturnAllWeightedEdges(t *testing.T, b Builder, useEmpty bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#ReturnAllWeightedEdges)
*   [func ReturnAllWeightedLines(t *testing.T, b Builder, useEmpty bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#ReturnAllWeightedLines)
*   [func ReturnEdgeSlice(t *testing.T, b Builder, useEmpty bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#ReturnEdgeSlice)
*   [func ReturnNodeSlice(t *testing.T, b Builder, useEmpty bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#ReturnNodeSlice)
*   [func ReturnWeightedEdgeSlice(t *testing.T, b Builder, useEmpty bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#ReturnWeightedEdgeSlice)
*   [func Weight(t *testing.T, b Builder)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#Weight)
*   [type Builder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#Builder)
*   [type Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#Edge)
*   [type EdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#EdgeAdder)
*   [type EdgeRemover](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#EdgeRemover)
*   [type LineAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#LineAdder)
*   [type LineRemover](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#LineRemover)
*   [type NodeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#NodeAdder)
*   [type NodeRemover](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#NodeRemover)
*   [type RandomNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RandomNodes)
*       *   [func NewRandomNodes(n int, seed uint64, new func(id int64) graph.Node) *RandomNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#NewRandomNodes)

*       *   [func (n *RandomNodes) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RandomNodes.Len)
    *   [func (n *RandomNodes) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RandomNodes.Next)
    *   [func (n *RandomNodes) Node() graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RandomNodes.Node)
    *   [func (n *RandomNodes) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RandomNodes.Reset)

*   [type WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#WeightedEdgeAdder)
*   [type WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#WeightedLine)
*   [type WeightedLineAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#WeightedLineAdder)
*   [Bugs](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#pkg-note-BUG)

This section is empty.

This section is empty.

AddArbitraryNodes tests whether g correctly implements the AddNode method. Not all graph.NodeAdder graphs are expected to implement the semantics of this test. AddArbitraryNodes iterates over add, adding each node to the graph. The existence of each added node in the graph is confirmed.

AddEdges tests whether g correctly implements the graph.EdgeAdder interface. AddEdges creates n pairs of nodes with random IDs in [0,n) and joins edges each node in the pair using SetEdge. AddEdges confirms that the end point nodes are added to the graph and that the edges are stored in the graph. If canLoop is true, self edges may be created. If canSet is true, a second call to SetEdge is made for each edge to confirm that the nodes corresponding the end points are updated.

AddLines tests whether g correctly implements the graph.LineAdder interface. AddLines creates n pairs of nodes with random IDs in [0,n) and joins edges each node in the pair using SetLine. AddLines confirms that the end point nodes are added to the graph and that the edges are stored in the graph. If canSet is true, a second call to SetLine is made for each edge to confirm that the nodes corresponding the end points are updated.

AddNodes tests whether g correctly implements the graph.NodeAdder interface. AddNodes gets a new node from g and adds it to the graph, repeating this pair of operations n times. The existence of added nodes is confirmed in the graph. AddNodes also checks that re-adding each of the added nodes causes a panic. If g satisfies NodeWithIDer, the NodeWithID method is tested for an additional n rounds of node addition using NodeWithID to create new nodes as well as confirming that NodeWithID returns existing nodes.

AddWeightedEdges tests whether g correctly implements the graph.WeightedEdgeAdder interface. AddWeightedEdges creates n pairs of nodes with random IDs in [0,n) and joins edges each node in the pair using SetWeightedEdge with weight w. AddWeightedEdges confirms that the end point nodes are added to the graph and that the edges are stored in the graph. If canLoop is true, self edges may be created. If canSet is true, a second call to SetWeightedEdge is made for each edge to confirm that the nodes corresponding the end points are updated.

AddWeightedLines tests whether g correctly implements the graph.WeightedEdgeAdder interface. AddWeightedLines creates n pairs of nodes with random IDs in [0,n) and joins edges each node in the pair using SetWeightedLine with weight w. AddWeightedLines confirms that the end point nodes are added to the graph and that the edges are stored in the graph. If canSet is true, a second call to SetWeightedLine is made for each edge to confirm that the nodes corresponding the end points are updated.

AdjacencyMatrix tests the constructed graph for the ability to correctly return an adjacency matrix that matches the weights returned by the graphs Weight method.

The self and absent values returned by the Builder should match the values used by the Weight method.

EdgeExistence tests the constructed graph for the ability to correctly return the existence of edges within the graph. This is a check of the Edge methods of graph.Graph, the EdgeBetween method of graph.Undirected and the EdgeFromTo method of graph.Directed. EdgeExistence also checks that the nodes and traversed edges exist within the graph, checking the Node, Edge, EdgeBetween and HasEdgeBetween methods of graph.Graph, the EdgeBetween method of graph.Undirected and the HasEdgeFromTo method of graph.Directed. If reversedEdge is true, edges will be checked to make sure edges returned match the orientation of an Edge or WeightedEdge call.

func LineExistence(t *[testing](https://pkg.go.dev/testing).[T](https://pkg.go.dev/testing#T), b [Builder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#Builder), useEmpty, reversedLine [bool](https://pkg.go.dev/builtin#bool))

LineExistence tests the constructed graph for the ability to correctly return the existence of lines within the graph. This is a check of the Line methods of graph.Multigraph, the EdgeBetween method of graph.Undirected and the EdgeFromTo method of graph.Directed. LineExistence also checks that the nodes and traversed edges exist within the graph, checking the Node, Edge, EdgeBetween and HasEdgeBetween methods of graph.Graph, the EdgeBetween method of graph.Undirected and the HasEdgeFromTo method of graph.Directed. If reversedLine is true, lines will be checked to make sure lines returned match the orientation of an Line or WeightedLine call.

NoLoopAddEdges tests whether g panics for self-loop addition. NoLoopAddEdges adds n nodes with IDs in [0,n) and creates an edge from the graph with NewEdge. NoLoopAddEdges confirms that this does not panic and then adds the edge to the graph to ensure that SetEdge will panic when adding a self-loop.

NoLoopAddWeightedEdges tests whether g panics for self-loop addition. NoLoopAddWeightedEdges adds n nodes with IDs in [0,n) and creates an edge from the graph with NewWeightedEdge. NoLoopAddWeightedEdges confirms that this does not panic and then adds the edge to the graph to ensure that SetWeightedEdge will panic when adding a self-loop.

NodeExistence tests the constructed graph for the ability to correctly return the existence of nodes within the graph. This is a check of the Node method of graph.Graph.

RemoveEdges tests whether g correctly implements the graph.EdgeRemover interface. The input graph g must contain a set of nodes with some edges between them. RemoveEdges iterates over remove, which must contain edges in g, removing each edge. RemoveEdges confirms that the edge is removed, leaving its end-point nodes and all other edges in the graph.

RemoveLines tests whether g correctly implements the graph.LineRemover interface. The input graph g must contain a set of nodes with some lines between them. RemoveLines iterates over remove, which must contain lines in g, removing each line. RemoveLines confirms that the line is removed, leaving its end-point nodes and all other lines in the graph.

RemoveNodes tests whether g correctly implements the graph.NodeRemover interface. The input graph g must contain a set of nodes with some edges between them.

func ReturnAdjacentNodes(t *[testing](https://pkg.go.dev/testing).[T](https://pkg.go.dev/testing#T), b [Builder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#Builder), useEmpty, reversedEdge [bool](https://pkg.go.dev/builtin#bool))

ReturnAdjacentNodes tests the constructed graph for the ability to correctly return the nodes reachable from each node within the graph. This is a check of the From method of graph.Graph and the To method of graph.Directed. ReturnAdjacentNodes also checks that the nodes and traversed edges exist within the graph, checking the Node, Edge, EdgeBetween and HasEdgeBetween methods of graph.Graph, the EdgeBetween method of graph.Undirected and the HasEdgeFromTo method of graph.Directed. If useEmpty is true, graph iterators will be checked for the use of graph.Empty if they are empty. If reversedEdge is true, edges will be checked to make sure edges returned match the orientation of an Edge or WeightedEdge call.

ReturnAllEdges tests the constructed graph for the ability to return all the edges it claims it has used in its construction. This is a check of the Edges method of graph.Graph and the iterator that is returned. ReturnAllEdges also checks that the edge end nodes exist within the graph, checking the Node method of graph.Graph. If useEmpty is true, graph iterators will be checked for the use of graph.Empty if they are empty.

ReturnAllLines tests the constructed graph for the ability to return all the edges it claims it has used in its construction and then recover all the lines that contribute to those edges. This is a check of the Edges method of graph.Graph and the iterator that is returned and the graph.Lines implementation of those edges. ReturnAllLines also checks that the edge end nodes exist within the graph, checking the Node method of graph.Graph.

The edges used within and returned by the Builder function should be graph.Line. The edge parameter passed to b will contain only graph.Line. If useEmpty is true, graph iterators will be checked for the use of graph.Empty if they are empty.

ReturnAllNodes tests the constructed graph for the ability to return all the nodes it claims it has used in its construction. This is a check of the Nodes method of graph.Graph and the iterator that is returned. If useEmpty is true, graph iterators will be checked for the use of graph.Empty if they are empty.

ReturnAllWeightedEdges tests the constructed graph for the ability to return all the edges it claims it has used in its construction. This is a check of the Edges method of graph.Graph and the iterator that is returned. ReturnAllWeightedEdges also checks that the edge end nodes exist within the graph, checking the Node method of graph.Graph.

The edges used within and returned by the Builder function should be graph.WeightedEdge. The edge parameter passed to b will contain only graph.WeightedEdge. If useEmpty is true, graph iterators will be checked for the use of graph.Empty if they are empty.

ReturnAllWeightedLines tests the constructed graph for the ability to return all the edges it claims it has used in its construction and then recover all the lines that contribute to those edges. This is a check of the Edges method of graph.Graph and the iterator that is returned and the graph.Lines implementation of those edges. ReturnAllWeightedLines also checks that the edge end nodes exist within the graph, checking the Node method of graph.Graph.

The edges used within and returned by the Builder function should be graph.WeightedLine. The edge parameter passed to b will contain only graph.WeightedLine. If useEmpty is true, graph iterators will be checked for the use of graph.Empty if they are empty.

ReturnEdgeSlice tests the constructed graph for the ability to return all the edges it claims it has used in its construction using the EdgeSlicer interface. This is a check of the Edges method of graph.Graph and the iterator that is returned. ReturnEdgeSlice also checks that the edge end nodes exist within the graph, checking the Node method of graph.Graph. If useEmpty is true, graph iterators will be checked for the use of graph.Empty if they are empty.

ReturnNodeSlice tests the constructed graph for the ability to return all the nodes it claims it has used in its construction using the NodeSlicer interface. This is a check of the Nodes method of graph.Graph and the iterator that is returned. If useEmpty is true, graph iterators will be checked for the use of graph.Empty if they are empty.

ReturnWeightedEdgeSlice tests the constructed graph for the ability to return all the edges it claims it has used in its construction using the WeightedEdgeSlicer interface. This is a check of the Edges method of graph.Graph and the iterator that is returned. ReturnWeightedEdgeSlice also checks that the edge end nodes exist within the graph, checking the Node method of graph.Graph.

The edges used within and returned by the Builder function should be graph.WeightedEdge. The edge parameter passed to b will contain only graph.WeightedEdge. If useEmpty is true, graph iterators will be checked for the use of graph.Empty if they are empty.

Weight tests the constructed graph for the ability to correctly return the weight between to nodes, checking the Weight method of graph.Weighted.

The self and absent values returned by the Builder should match the values used by the Weight method.

A Builder function returns a graph constructed from the nodes, edges and default weights passed in, potentially altering the nodes and edges to conform to the requirements of the graph. The graph is returned along with the nodes, edges and default weights used to construct the graph. The returned edges may be any of graph.Edge, graph.WeightedEdge, graph.Line or graph.WeightedLine depending on what the graph requires. The client may skip a test case by returning ok=false when the input is not a valid graph construction.

Edge supports basic edge operations.

EdgeAdder is a graph.EdgeAdder graph.

EdgeRemover is a graph.EdgeRemover graph.

LineAdder is a graph.LineAdder multigraph.

LineRemover is a graph.EdgeRemove graph.

NodeAdder is a graph.NodeAdder graph.

NodeRemover is a graph.NodeRemover graph.

#### type [RandomNodes](https://github.com/gonum/gonum/blob/v0.17.0/graph/testgraph/testgraph.go#L2093)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RandomNodes "Go to RandomNodes")

type RandomNodes struct {
	
}

RandomNodes implements the graph.Nodes interface for a set of random nodes.

#### func [NewRandomNodes](https://github.com/gonum/gonum/blob/v0.17.0/graph/testgraph/testgraph.go#L2110)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#NewRandomNodes "Go to NewRandomNodes")

NewRandomNodes returns a new implicit node iterator containing a set of n nodes with IDs generated from a PRNG seeded by the given seed. The provided new func maps the id to a graph.Node.

#### func (*RandomNodes) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/testgraph/testgraph.go#L2123)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RandomNodes.Len "Go to RandomNodes.Len")

Len returns the remaining number of nodes to be iterated over.

#### func (*RandomNodes) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/testgraph/testgraph.go#L2128)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RandomNodes.Next "Go to RandomNodes.Next")

Next returns whether the next call of Node will return a valid node.

#### func (*RandomNodes) [Node](https://github.com/gonum/gonum/blob/v0.17.0/graph/testgraph/testgraph.go#L2148)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RandomNodes.Node "Go to RandomNodes.Node")

Node returns the current node of the iterator. Next must have been called prior to a call to Node.

#### func (*RandomNodes) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/testgraph/testgraph.go#L2156)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RandomNodes.Reset "Go to RandomNodes.Reset")

func (n *[RandomNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/testgraph#RandomNodes)) Reset()

Reset returns the iterator to its initial state.

WeightedEdgeAdder is a graph.EdgeAdder graph.

WeightedLine is a generalized graph edge that supports all graph edge operations except reversal.

WeightedLineAdder is a graph.WeightedLineAdder multigraph.

*   Edge equality is tested in part with reflect.DeepEqual and direct equality of weight values. This means that edges returned by graphs must not contain NaN values. Weights returned by the Weight method are compared with NaN-awareness, so they may be NaN when there is no edge associated with the Weight call.
