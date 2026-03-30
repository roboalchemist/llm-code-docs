# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community

Title: community package - gonum.org/v1/gonum/graph/community - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community

Markdown Content:
Package community provides graph community detection functions.

*   [func KCliqueCommunities(k int, g graph.Undirected) [][]graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#KCliqueCommunities)
*   [func ModularMultiplexScore(g Multiplex, weights []float64, all bool, score func(ReducedMultiplex) float64, ...) func(float64) (float64, Reduced)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ModularMultiplexScore)
*   [func ModularScore(g graph.Graph, score func(ReducedGraph) float64, effort int, src rand.Source) func(float64) (float64, Reduced)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ModularScore)
*   [func Q(g graph.Graph, communities [][]graph.Node, resolution float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#Q)
*   [func QMultiplex(g Multiplex, communities [][]graph.Node, weights, resolutions []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#QMultiplex)
*   [func Size(g ReducedGraph) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#Size)
*   [func SizeMultiplex(g ReducedMultiplex) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#SizeMultiplex)
*   [func Weight(g ReducedGraph) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#Weight)
*   [func WeightMultiplex(g ReducedMultiplex) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#WeightMultiplex)
*   [type DirectedLayers](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#DirectedLayers)
*       *   [func NewDirectedLayers(layers ...graph.Directed) (DirectedLayers, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#NewDirectedLayers)

*       *   [func (g DirectedLayers) Depth() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#DirectedLayers.Depth)
    *   [func (g DirectedLayers) Layer(l int) graph.Directed](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#DirectedLayers.Layer)
    *   [func (g DirectedLayers) Nodes() graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#DirectedLayers.Nodes)

*   [type DirectedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#DirectedMultiplex)
*   [type Interval](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#Interval)
*       *   [func Profile(fn func(float64) (float64, Reduced), log bool, grain, low, high float64) (profile []Interval, err error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#Profile)

*   [type Multiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#Multiplex)
*   [type Reduced](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#Reduced)
*   [type ReducedDirected](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected)
*       *   [func (g *ReducedDirected) Communities() [][]graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.Communities)
    *   [func (g *ReducedDirected) Edge(uid, vid int64) graph.Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.Edge)
    *   [func (g *ReducedDirected) Expanded() ReducedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.Expanded)
    *   [func (g *ReducedDirected) From(uid int64) graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.From)
    *   [func (g *ReducedDirected) HasEdgeBetween(xid, yid int64) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.HasEdgeBetween)
    *   [func (g *ReducedDirected) HasEdgeFromTo(uid, vid int64) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.HasEdgeFromTo)
    *   [func (g *ReducedDirected) Node(id int64) graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.Node)
    *   [func (g *ReducedDirected) Nodes() graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.Nodes)
    *   [func (g *ReducedDirected) Structure() [][]graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.Structure)
    *   [func (g *ReducedDirected) To(vid int64) graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.To)
    *   [func (g *ReducedDirected) Weight(xid, yid int64) (w float64, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.Weight)
    *   [func (g *ReducedDirected) WeightedEdge(uid, vid int64) graph.WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.WeightedEdge)

*   [type ReducedDirectedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirectedMultiplex)
*       *   [func (g *ReducedDirectedMultiplex) Communities() [][]graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirectedMultiplex.Communities)
    *   [func (g *ReducedDirectedMultiplex) Depth() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirectedMultiplex.Depth)
    *   [func (g *ReducedDirectedMultiplex) Expanded() ReducedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirectedMultiplex.Expanded)
    *   [func (g *ReducedDirectedMultiplex) Layer(l int) graph.Directed](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirectedMultiplex.Layer)
    *   [func (g *ReducedDirectedMultiplex) Nodes() graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirectedMultiplex.Nodes)
    *   [func (g *ReducedDirectedMultiplex) Structure() [][]graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirectedMultiplex.Structure)

*   [type ReducedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedGraph)
*       *   [func Modularize(g graph.Graph, resolution float64, src rand.Source) ReducedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#Modularize)

*   [type ReducedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedMultiplex)
*       *   [func ModularizeMultiplex(g Multiplex, weights, resolutions []float64, all bool, src rand.Source) ReducedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ModularizeMultiplex)

*   [type ReducedUndirected](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected)
*       *   [func (g *ReducedUndirected) Communities() [][]graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.Communities)
    *   [func (g *ReducedUndirected) Edge(uid, vid int64) graph.Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.Edge)
    *   [func (g *ReducedUndirected) EdgeBetween(xid, yid int64) graph.Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.EdgeBetween)
    *   [func (g *ReducedUndirected) Expanded() ReducedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.Expanded)
    *   [func (g *ReducedUndirected) From(uid int64) graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.From)
    *   [func (g *ReducedUndirected) HasEdgeBetween(xid, yid int64) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.HasEdgeBetween)
    *   [func (g *ReducedUndirected) Node(id int64) graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.Node)
    *   [func (g *ReducedUndirected) Nodes() graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.Nodes)
    *   [func (g *ReducedUndirected) Structure() [][]graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.Structure)
    *   [func (g *ReducedUndirected) Weight(xid, yid int64) (w float64, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.Weight)
    *   [func (g *ReducedUndirected) WeightedEdge(uid, vid int64) graph.WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.WeightedEdge)
    *   [func (g *ReducedUndirected) WeightedEdgeBetween(xid, yid int64) graph.WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.WeightedEdgeBetween)

*   [type ReducedUndirectedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirectedMultiplex)
*       *   [func (g *ReducedUndirectedMultiplex) Communities() [][]graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirectedMultiplex.Communities)
    *   [func (g *ReducedUndirectedMultiplex) Depth() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirectedMultiplex.Depth)
    *   [func (g *ReducedUndirectedMultiplex) Expanded() ReducedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirectedMultiplex.Expanded)
    *   [func (g *ReducedUndirectedMultiplex) Layer(l int) graph.Undirected](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirectedMultiplex.Layer)
    *   [func (g *ReducedUndirectedMultiplex) Nodes() graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirectedMultiplex.Nodes)
    *   [func (g *ReducedUndirectedMultiplex) Structure() [][]graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirectedMultiplex.Structure)

*   [type UndirectedLayers](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#UndirectedLayers)
*       *   [func NewUndirectedLayers(layers ...graph.Undirected) (UndirectedLayers, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#NewUndirectedLayers)

*       *   [func (g UndirectedLayers) Depth() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#UndirectedLayers.Depth)
    *   [func (g UndirectedLayers) Layer(l int) graph.Undirected](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#UndirectedLayers.Layer)
    *   [func (g UndirectedLayers) Nodes() graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#UndirectedLayers.Nodes)

*   [type UndirectedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#UndirectedMultiplex)

*   [Profile (Multiplex)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#example-Profile-Multiplex)
*   [Profile (Simple)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#example-Profile-Simple)

This section is empty.

This section is empty.

KCliqueCommunities returns the k-clique communities of the undirected graph g for k greater than zero. The returned communities are identified by linkage via k-clique adjacency, where adjacency is defined as having k-1 common nodes. KCliqueCommunities returns a single component including the full set of nodes of g when k is 1, and the classical connected components of g when k is 2. Note that k-clique communities may contain common nodes from g.

k-clique communities are described in Palla et al. doi:10.1038/nature03607.

ModularMultiplexScore returns a modularized scoring function for Profile based on the graph g and the given score function. The effort parameter determines how many attempts will be made to get an improved score for any given resolution.

ModularScore returns a modularized scoring function for Profile based on the graph g and the given score function. The effort parameter determines how many attempts will be made to get an improved score for any given resolution.

Q returns the modularity Q score of the graph g subdivided into the given communities at the given resolution. If communities is nil, the unclustered modularity score is returned. The resolution parameter is γ as defined in Reichardt and Bornholdt doi:10.1103/PhysRevE.74.016110. Q will panic if g has any edge with negative edge weight.

If g is undirected, Q is calculated according to

Q = 1/2m \sum_{ij} [ A_{ij} - (\gamma k_i k_j)/2m ] \delta(c_i,c_j),

If g is directed, it is calculated according to

Q = 1/m \sum_{ij} [ A_{ij} - (\gamma k_i^in k_j^out)/m ] \delta(c_i,c_j).

graph.Undirect may be used as a shim to allow calculation of Q for directed graphs with the undirected modularity function.

QMultiplex returns the modularity Q score of the multiplex graph layers subdivided into the given communities at the given resolutions and weights. Q is returned as the vector of weighted Q scores for each layer of the multiplex graph. If communities is nil, the unclustered modularity score is returned. If weights is nil layers are equally weighted, otherwise the length of weights must equal the number of layers. If resolutions is nil, a resolution of 1.0 is used for all layers, otherwise either a single element slice may be used to specify a global resolution, or the length of resolutions must equal the number of layers. The resolution parameter is γ as defined in Reichardt and Bornholdt doi:10.1103/PhysRevE.74.016110. QMultiplex will panic if the graph has any layer weight-scaled edge with negative edge weight.

If g is undirected, Q is calculated according to

Q_{layer} = w_{layer} \sum_{ij} [ A_{layer}*_{ij} - (\gamma_{layer} k_i k_j)/2m_{layer} ] \delta(c_i,c_j),

If g is directed, it is calculated according to

Q_{layer} = w_{layer} \sum_{ij} [ A_{layer}*_{ij} - (\gamma_{layer} k_i^in k_j^out)/m_{layer} ] \delta(c_i,c_j).

Note that Q values for multiplex graphs are not scaled by the total layer edge weight.

graph.Undirect may be used as a shim to allow calculation of Q for directed graphs.

Size is a score function that is the reciprocal of the number of communities.

SizeMultiplex is a score function that is the reciprocal of the number of communities.

Weight is a score function that is the sum of community weights. The concrete type of g must be a pointer to a ReducedUndirected or a ReducedDirected, otherwise Weight will panic.

WeightMultiplex is a score function that is the sum of community weights. The concrete type of g must be pointer to a ReducedUndirectedMultiplex or a ReducedDirectedMultiplex, otherwise WeightMultiplex will panic.

DirectedLayers implements DirectedMultiplex.

NewDirectedLayers returns a DirectedLayers using the provided layers ensuring there is a match between IDs for each layer.

Depth returns the depth of the multiplex graph.

Layer returns the lth layer of the multiplex graph.

Nodes returns the nodes of the receiver.

DirectedMultiplex is a directed multiplex graph.

Interval is an interval of resolutions with a common score.

Profile returns an approximate profile of score values in the resolution domain [low,high) at the given granularity. The score is calculated by bisecting calls to fn. If log is true, log space bisection is used, otherwise bisection is linear. The function fn should be monotonically decreasing in at least 1/grain evaluations. Profile will attempt to detect non-monotonicity during the bisection.

Since exact modularity optimization is known to be NP-hard and Profile calls modularization routines repeatedly, it is unlikely to return the exact resolution profile.

Output:

Low:0.1 High:0.72 Score:26 Communities:[[0] [1 7 9 12] [2 8 11] [3 4 5 10] [6]] Q=[24.7 1.97] Low:0.72 High:1.1 Score:24 Communities:[[0 6] [1 7 9 12] [2 8 11] [3 4 5 10]] Q=[16.9 14.1] Low:1.1 High:1.2 Score:18 Communities:[[0 2 6 11] [1 7 9 12] [3 4 5 8 10]] Q=[9.16 25.1] Low:1.2 High:1.6 Score:10 Communities:[[0 3 4 5 6 10] [1 7 9 12] [2 8 11]] Q=[10.7 26] Low:1.6 High:1.6 Score:8 Communities:[[0 1 6 7 9 12] [2 8 11] [3 4 5 10]] Q=[5.56 39.8] Low:1.6 High:1.8 Score:2 Communities:[[0 2 3 4 5 6 10] [1 7 8 9 11 12]] Q=[-1.82 48.6] Low:1.8 High:2.3 Score:-6 Communities:[[0 2 3 4 5 6 8 10 11] [1 7 9 12]] Q=[-5.02 57.5] Low:2.3 High:2.4 Score:-10 Communities:[[0 1 2 6 7 8 9 11 12] [3 4 5 10]] Q=[-11.2 79] Low:2.4 High:4.3 Score:-52 Communities:[[0 1 2 3 4 5 6 7 8 9 10 11 12]] Q=[-46.1 117] Low:4.3 High:10 Score:-54 Communities:[[0 1 2 3 4 6 7 8 9 10 11 12] [5]] Q=[-82 254] 

Output:

Low:0.1 High:0.29 Score:14 Communities:[[0 1 2 3 4 5]] Q=0.9 Low:0.29 High:2.3 Score:12 Communities:[[0 1 2] [3 4 5]] Q=0.714 Low:2.3 High:3.5 Score:4 Communities:[[0 1] [2] [3] [4 5]] Q=-0.31 Low:3.5 High:10 Score:0 Communities:[[0] [1] [2] [3] [4] [5]] Q=-0.607 

Multiplex is a multiplex graph.

type Reduced interface {
	
	Communities() [][][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)
}

Reduced is a graph reduction.

type ReducedDirected struct {
	
}

ReducedDirected is a directed graph of communities derived from a parent graph by reduction.

Communities returns the community memberships of the nodes in the graph used to generate the reduced graph.

Edge returns the edge from u to v if such an edge exists and nil otherwise. The node v must be directly reachable from u as defined by the From method.

#### func (*ReducedDirected) [Expanded](https://github.com/gonum/gonum/blob/v0.17.0/graph/community/louvain_directed.go#L167)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected.Expanded "Go to ReducedDirected.Expanded")

func (g *[ReducedDirected](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirected)) Expanded() [ReducedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedGraph)

Expanded returns the next lower level of the module clustering or nil if at the lowest level.

From returns all nodes in g that can be reached directly from u.

HasEdgeBetween returns whether an edge exists between nodes x and y.

HasEdgeFromTo returns whether an edge exists from node u to v.

Node returns the node with the given ID if it exists in the graph, and nil otherwise.

Nodes returns all the nodes in the graph.

Structure returns the community structure of the current level of the module clustering. The first index of the returned value corresponds to the index of the nodes in the next higher level if it exists. The returned value should not be mutated.

To returns all nodes in g that can reach directly to v.

Weight returns the weight for the edge between x and y if Edge(x, y) returns a non-nil Edge. If x and y are the same node the internal node weight is returned. If there is no joining edge between the two nodes the weight value returned is zero. Weight returns true if an edge exists between x and y or if x and y have the same ID, false otherwise.

WeightedEdge returns the weighted edge from u to v if such an edge exists and nil otherwise. The node v must be directly reachable from u as defined by the From method.

type ReducedDirectedMultiplex struct {
	
}

ReducedDirectedMultiplex is a directed graph of communities derived from a parent graph by reduction.

Communities returns the community memberships of the nodes in the graph used to generate the reduced graph.

Depth returns the number of layers in the multiplex graph.

#### func (*ReducedDirectedMultiplex) [Expanded](https://github.com/gonum/gonum/blob/v0.17.0/graph/community/louvain_directed_multiplex.go#L280)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirectedMultiplex.Expanded "Go to ReducedDirectedMultiplex.Expanded")

func (g *[ReducedDirectedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedDirectedMultiplex)) Expanded() [ReducedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedMultiplex)

Expanded returns the next lower level of the module clustering or nil if at the lowest level.

Layer returns the lth layer of the multiplex graph.

Nodes returns all the nodes in the graph.

Structure returns the community structure of the current level of the module clustering. The first index of the returned value corresponds to the index of the nodes in the next higher level if it exists. The returned value should not be mutated.

ReducedGraph is a modularised graph.

Modularize returns the hierarchical modularization of g at the given resolution using the Louvain algorithm. If src is nil, rand.IntN is used as the random generator. Modularize will panic if g has any edge with negative edge weight.

If g is undirected it is modularised to minimise

Q = 1/2m \sum_{ij} [ A_{ij} - (\gamma k_i k_j)/2m ] \delta(c_i,c_j),

If g is directed it is modularised to minimise

Q = 1/m \sum_{ij} [ A_{ij} - (\gamma k_i^in k_j^out)/m ] \delta(c_i,c_j).

The concrete type of the ReducedGraph will be a pointer to either a ReducedUndirected or a ReducedDirected depending on the type of g.

graph.Undirect may be used as a shim to allow modularization of directed graphs with the undirected modularity function.

type ReducedMultiplex interface {
	[Multiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#Multiplex)

	
	
	Communities() [][][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

	
	
	
	
	
	
	
	
	
	
	Structure() [][][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

	
	
	
	
	Expanded() [ReducedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedMultiplex)
}

ReducedMultiplex is a modularised multiplex graph.

ModularizeMultiplex returns the hierarchical modularization of g at the given resolution using the Louvain algorithm. If all is true and g have negatively weighted layers, all communities will be searched during the modularization. If src is nil, rand.IntN is used as the random generator. ModularizeMultiplex will panic if g has any edge with edge weight that does not sign-match the layer weight.

If g is undirected it is modularised to minimise

Q = \sum w_{layer} \sum_{ij} [ A_{layer}*_{ij} - (\gamma_{layer} k_i k_j)/2m ] \delta(c_i,c_j).

If g is directed it is modularised to minimise

Q = \sum w_{layer} \sum_{ij} [ A_{layer}*_{ij} - (\gamma_{layer} k_i^in k_j^out)/m_{layer} ] \delta(c_i,c_j).

The concrete type of the ReducedMultiplex will be a pointer to a ReducedUndirectedMultiplex.

graph.Undirect may be used as a shim to allow modularization of directed graphs with the undirected modularity function.

type ReducedUndirected struct {
	
}

ReducedUndirected is an undirected graph of communities derived from a parent graph by reduction.

Communities returns the community memberships of the nodes in the graph used to generate the reduced graph.

Edge returns the edge from u to v if such an edge exists and nil otherwise. The node v must be directly reachable from u as defined by the From method.

EdgeBetween returns the edge between nodes x and y.

#### func (*ReducedUndirected) [Expanded](https://github.com/gonum/gonum/blob/v0.17.0/graph/community/louvain_undirected.go#L165)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected.Expanded "Go to ReducedUndirected.Expanded")

func (g *[ReducedUndirected](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirected)) Expanded() [ReducedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedGraph)

Expanded returns the next lower level of the module clustering or nil if at the lowest level.

From returns all nodes in g that can be reached directly from u.

HasEdgeBetween returns whether an edge exists between nodes x and y.

Node returns the node with the given ID if it exists in the graph, and nil otherwise.

Nodes returns all the nodes in the graph.

Structure returns the community structure of the current level of the module clustering. The first index of the returned value corresponds to the index of the nodes in the next higher level if it exists. The returned value should not be mutated.

Weight returns the weight for the edge between x and y if Edge(x, y) returns a non-nil Edge. If x and y are the same node the internal node weight is returned. If there is no joining edge between the two nodes the weight value returned is zero. Weight returns true if an edge exists between x and y or if x and y have the same ID, false otherwise.

WeightedEdge returns the weighted edge from u to v if such an edge exists and nil otherwise. The node v must be directly reachable from u as defined by the From method.

WeightedEdgeBetween returns the weighted edge between nodes x and y.

type ReducedUndirectedMultiplex struct {
	
}

ReducedUndirectedMultiplex is an undirected graph of communities derived from a parent graph by reduction.

Communities returns the community memberships of the nodes in the graph used to generate the reduced graph.

Depth returns the number of layers in the multiplex graph.

#### func (*ReducedUndirectedMultiplex) [Expanded](https://github.com/gonum/gonum/blob/v0.17.0/graph/community/louvain_undirected_multiplex.go#L276)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirectedMultiplex.Expanded "Go to ReducedUndirectedMultiplex.Expanded")

func (g *[ReducedUndirectedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedUndirectedMultiplex)) Expanded() [ReducedMultiplex](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/community#ReducedMultiplex)

Expanded returns the next lower level of the module clustering or nil if at the lowest level.

Layer returns the lth layer of the multiplex graph.

Nodes returns all the nodes in the graph.

Structure returns the community structure of the current level of the module clustering. The first index of the returned value corresponds to the index of the nodes in the next higher level if it exists. The returned value should not be mutated.

UndirectedLayers implements UndirectedMultiplex.

NewUndirectedLayers returns an UndirectedLayers using the provided layers ensuring there is a match between IDs for each layer.

Depth returns the depth of the multiplex graph.

Layer returns the lth layer of the multiplex graph.

Nodes returns the nodes of the receiver.

UndirectedMultiplex is an undirected multiplex graph.
