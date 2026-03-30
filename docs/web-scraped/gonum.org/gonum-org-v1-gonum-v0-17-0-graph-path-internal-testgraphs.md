# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs

Title: testgraphs package - gonum.org/v1/gonum/graph/path/internal/testgraphs - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs

Markdown Content:
Package testgraphs provides a number of graphs used for testing routines in the path and path/dynamic packages.

*   [Constants](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#pkg-constants)
*   [Variables](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#pkg-variables)
*   [type Grid](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid)
*       *   [func NewGrid(r, c int, open bool) *Grid](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#NewGrid)
    *   [func NewGridFrom(rows ...string) *Grid](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#NewGridFrom)

*       *   [func (g *Grid) Dims() (r, c int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.Dims)
    *   [func (g *Grid) Edge(uid, vid int64) graph.Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.Edge)
    *   [func (g *Grid) EdgeBetween(uid, vid int64) graph.Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.EdgeBetween)
    *   [func (g *Grid) From(uid int64) graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.From)
    *   [func (g *Grid) HasEdgeBetween(uid, vid int64) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.HasEdgeBetween)
    *   [func (g *Grid) HasOpen(id int64) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.HasOpen)
    *   [func (g *Grid) Node(id int64) graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.Node)
    *   [func (g *Grid) NodeAt(r, c int) graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.NodeAt)
    *   [func (g *Grid) Nodes() graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.Nodes)
    *   [func (g *Grid) Render(path []graph.Node) ([]byte, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.Render)
    *   [func (g *Grid) RowCol(id int64) (r, c int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.RowCol)
    *   [func (g *Grid) Set(r, c int, open bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.Set)
    *   [func (g *Grid) String() string](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.String)
    *   [func (g *Grid) Weight(xid, yid int64) (w float64, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.Weight)
    *   [func (g *Grid) WeightedEdge(uid, vid int64) graph.WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.WeightedEdge)
    *   [func (g *Grid) WeightedEdgeBetween(uid, vid int64) graph.WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.WeightedEdgeBetween)
    *   [func (g *Grid) XY(id int64) (x, y float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid.XY)

*   [type LimitedVisionGrid](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid)
*       *   [func (l *LimitedVisionGrid) Edge(uid, vid int64) graph.Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.Edge)
    *   [func (l *LimitedVisionGrid) EdgeBetween(uid, vid int64) graph.Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.EdgeBetween)
    *   [func (l *LimitedVisionGrid) From(uid int64) graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.From)
    *   [func (l *LimitedVisionGrid) HasEdgeBetween(uid, vid int64) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.HasEdgeBetween)
    *   [func (l *LimitedVisionGrid) MoveTo(n graph.Node) (new, old []graph.Edge)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.MoveTo)
    *   [func (l *LimitedVisionGrid) Node(id int64) graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.Node)
    *   [func (l *LimitedVisionGrid) NodeAt(r, c int) graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.NodeAt)
    *   [func (l *LimitedVisionGrid) Nodes() graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.Nodes)
    *   [func (l *LimitedVisionGrid) Render(path []graph.Node) ([]byte, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.Render)
    *   [func (l *LimitedVisionGrid) RowCol(id int64) (r, c int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.RowCol)
    *   [func (l *LimitedVisionGrid) String() string](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.String)
    *   [func (l *LimitedVisionGrid) Weight(xid, yid int64) (w float64, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.Weight)
    *   [func (l *LimitedVisionGrid) WeightedEdge(uid, vid int64) graph.WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.WeightedEdge)
    *   [func (l *LimitedVisionGrid) WeightedEdgeBetween(uid, vid int64) graph.WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.WeightedEdgeBetween)
    *   [func (l *LimitedVisionGrid) XY(id int64) (x, y float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#LimitedVisionGrid.XY)

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/graph/path/internal/testgraphs/grid.go#L17)

const (
 Closed = '*'  Open = '.'  Unknown = '?' )

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/graph/path/internal/testgraphs/shortest.go#L17)

var ShortestPathTests = []struct { 	Name                   [string](https://pkg.go.dev/builtin#string)
	Graph                  func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder)
	Edges                  [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge)
	HasNegativeWeight      [bool](https://pkg.go.dev/builtin#bool)
	HasNegativeCycle       [bool](https://pkg.go.dev/builtin#bool)
	HasNegativeCycleInPath [bool](https://pkg.go.dev/builtin#bool)

	Query         [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge)
	Weight        [float64](https://pkg.go.dev/builtin#float64)
	WantPaths     [][][int64](https://pkg.go.dev/builtin#int64)
	HasUniquePath [bool](https://pkg.go.dev/builtin#bool)

	NoPathFor [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge)
}{

	{
		Name:  "empty directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1)},
		Weight: [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1)},
	},
	{
		Name:  "empty undirected",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedUndirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedUndirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1)},
		Weight: [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1)},
	},
	{
		Name:  "one edge directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1)},
		Weight: 1,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1},
		},
		HasUniquePath: [true](https://pkg.go.dev/builtin#true),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3)},
	},
	{
		Name:  "one edge self directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0)},
		Weight: 0,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0},
		},
		HasUniquePath: [true](https://pkg.go.dev/builtin#true),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3)},
	},
	{
		Name:  "one edge undirected",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedUndirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedUndirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1)},
		Weight: 1,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1},
		},
		HasUniquePath: [true](https://pkg.go.dev/builtin#true),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3)},
	},
	{
		Name:  "two paths directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 2},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2)},
		Weight: 2,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2},
			{0, 2},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1)},
	},
	{
		Name:  "two paths undirected",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedUndirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedUndirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 2},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2)},
		Weight: 2,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2},
			{0, 2},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4)},
	},
	{
		Name:  "confounding paths directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 1},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 4},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 2},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 4},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 0.25},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 5},
			{0, 2, 3, 5},
			{0, 5},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
	},
	{
		Name:  "confounding paths undirected",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedUndirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedUndirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 1},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 4},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 2},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 4},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 0.25},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 5},
			{0, 2, 3, 5},
			{0, 5},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6)},
	},
	{
		Name:  "confounding paths directed 2-step",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 1},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), W: 2},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 2},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 2},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 4},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 0.25},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 5},
			{0, 2, 3, 5},
			{0, 6, 5},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
	},
	{
		Name:  "confounding paths undirected 2-step",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedUndirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedUndirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 1},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), W: 2},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 2},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 2},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 4},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 0.25},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 5},
			{0, 2, 3, 5},
			{0, 6, 5},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(7)},
	},
	{
		Name:  "zero-weight cycle directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 1},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 0},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 4},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
	},
	{
		Name:  "zero-weight cycle^2 directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 1},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 0},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 4},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
	},
	{
		Name:  "zero-weight cycle^2 confounding directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 1},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 0},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 3},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 4},
			{0, 1, 5, 4},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
	},
	{
		Name:  "zero-weight cycle^3 directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 1},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 0},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(7), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(7), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), W: 0},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 4},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
	},
	{
		Name:  "zero-weight 3·cycle^2 confounding directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 1},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 0},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(7), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(7), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 3},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 3},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(7), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 3},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 4},
			{0, 1, 5, 4},
			{0, 1, 5, 6, 4},
			{0, 1, 5, 7, 4},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
	},
	{
		Name:  "zero-weight reversed 3·cycle^2 confounding directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 1},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 0},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(7), W: 0},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(7), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 0},

			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), W: 3},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6), W: 3},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(7), W: 3},
		},

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 4},
			{0, 5, 3, 4},
			{0, 6, 5, 3, 4},
			{0, 7, 5, 3, 4},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
	},
	{
		Name:  "zero-weight |V|·cycle^(n/|V|) directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: func() [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge) {
			e := [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

				{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
				{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
				{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
				{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 1},
			}
			next := [len](https://pkg.go.dev/builtin#len)(e) + 1

			
			const n = 100
			for i := 0; i < n; i++ {
				e = [append](https://pkg.go.dev/builtin#append)(e,
					[simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(next + i), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(i), W: 0},
					[simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(i), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(next + i), W: 0},
				)
			}
			return e
		}(),

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 4},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
	},
	{
		Name:  "zero-weight n·cycle directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: func() [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge) {
			e := [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

				{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
				{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
				{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
				{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 1},
			}
			next := [len](https://pkg.go.dev/builtin#len)(e) + 1

			
			const n = 100
			for i := 0; i < n; i++ {
				e = [append](https://pkg.go.dev/builtin#append)(e,
					[simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(next + i), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 0},
					[simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(next + i), W: 0},
				)
			}
			return e
		}(),

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 4},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
	},
	{
		Name:  "zero-weight bi-directional tree with single exit directed",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: func() [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge) {
			e := [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){

				{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
				{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: 1},
				{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
				{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 1},
			}

			
			
			
			const (
				depth     = 4
				branching = 4
			)

			next := [len](https://pkg.go.dev/builtin#len)(e) + 1
			src := 2
			var i, last [int](https://pkg.go.dev/builtin#int)
			for l := 0; l < depth; l++ {
				for i = 0; i < branching; i++ {
					last = next + i
					e = [append](https://pkg.go.dev/builtin#append)(e, [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(src), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(last), W: 0})
					e = [append](https://pkg.go.dev/builtin#append)(e, [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(last), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(src), W: 0})
				}
				src = next + 1
				next += branching
			}
			e = [append](https://pkg.go.dev/builtin#append)(e, [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(last), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 2})
			return e
		}(),

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4)},
		Weight: 4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1, 2, 3, 4},
			{0, 1, 2, 6, 10, 14, 20, 4},
		},
		HasUniquePath: [false](https://pkg.go.dev/builtin#false),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5)},
	},

	{
		Name:  "one edge directed negative",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: -1},
		},
		HasNegativeWeight: [true](https://pkg.go.dev/builtin#true),

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1)},
		Weight: -1,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1},
		},
		HasUniquePath: [true](https://pkg.go.dev/builtin#true),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3)},
	},
	{
		Name:  "one edge undirected negative",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedUndirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedUndirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: -1},
		},
		HasNegativeWeight: [true](https://pkg.go.dev/builtin#true),
		HasNegativeCycle:  [true](https://pkg.go.dev/builtin#true),

		Query:                  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1)},
		HasNegativeCycleInPath: [true](https://pkg.go.dev/builtin#true),
		Weight:                 [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(-1),
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 1},
		},

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3)},
	},
	{
		Name:  "two path directed negative cycle",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: -1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: -1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 1},
		},
		HasNegativeWeight: [true](https://pkg.go.dev/builtin#true),
		HasNegativeCycle:  [true](https://pkg.go.dev/builtin#true),

		Query:                  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3)},
		HasNegativeCycleInPath: [true](https://pkg.go.dev/builtin#true),
		Weight:                 [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(-1),
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{1, 2, 1, 3},
		},

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6)},
	},
	{
		Name:  "two path directed off-path negative cycle",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: -1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: -1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4), W: 10},
		},
		HasNegativeWeight: [true](https://pkg.go.dev/builtin#true),
		HasNegativeCycle:  [true](https://pkg.go.dev/builtin#true),

		Query:                  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(4)},
		HasNegativeCycleInPath: [false](https://pkg.go.dev/builtin#false),
		Weight:                 10,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{0, 4},
		},
		HasUniquePath: [true](https://pkg.go.dev/builtin#true),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6)},
	},
	{
		Name:  "two path directed diamond negative cycle",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), W: -1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), W: -1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(1), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3), W: 10},
		},
		HasNegativeWeight: [true](https://pkg.go.dev/builtin#true),
		HasNegativeCycle:  [true](https://pkg.go.dev/builtin#true),

		Query:                  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(0), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3)},
		HasNegativeCycleInPath: [true](https://pkg.go.dev/builtin#true),
		Weight:                 [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(-1),
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{1, 2, 1, 3},
		},

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(5), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(6)},
	},
	{
		Name:  "wp graph negative",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('w'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('z'), W: 2},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('x'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('w'), W: 6},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('x'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('y'), W: 3},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('y'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('w'), W: 4},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('y'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('z'), W: 5},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('z'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('x'), W: -7},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('z'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('y'), W: -3},
		},
		HasNegativeWeight: [true](https://pkg.go.dev/builtin#true),

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('z'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('y')},
		Weight: -4,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{'z', 'x', 'y'},
		},
		HasUniquePath: [true](https://pkg.go.dev/builtin#true),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3)},
	},
	{
		Name:  "roughgarden negative",
		Graph: func() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdgeAdder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdgeAdder) { return [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[NewWeightedDirectedGraph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#NewWeightedDirectedGraph)(0, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1)) },
		Edges: [][simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#WeightedEdge){
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('a'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('b'), W: -2},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('b'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('c'), W: -1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('c'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('a'), W: 4},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('c'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('x'), W: 2},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('c'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('y'), W: -3},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('z'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('x'), W: 1},
			{F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('z'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('y'), W: -4},
		},
		HasNegativeWeight: [true](https://pkg.go.dev/builtin#true),

		Query:  [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('a'), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)('y')},
		Weight: -6,
		WantPaths: [][][int64](https://pkg.go.dev/builtin#int64){
			{'a', 'b', 'c', 'y'},
		},
		HasUniquePath: [true](https://pkg.go.dev/builtin#true),

		NoPathFor: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Edge){F: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(2), T: [simple](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/simple#Node)(3)},
	},
}

ShortestPathTests are graphs used to test the static shortest path routines in path: BellmanFord, DijkstraAllPaths, DijkstraFrom, FloydWarshall and Johnson, and the static degenerate case for the dynamic shortest path routine in path/dynamic: DStarLite.

This section is empty.

type Grid struct {
	
	
	AllowDiagonal [bool](https://pkg.go.dev/builtin#bool)
	
	
	
	
	UnitEdgeWeight [bool](https://pkg.go.dev/builtin#bool)

	
	
	AllVisible [bool](https://pkg.go.dev/builtin#bool)
	
}

Grid is a 2D grid planar undirected graph.

NewGrid returns an r by c grid with all positions set to the specified open state.

func NewGridFrom(rows ...[string](https://pkg.go.dev/builtin#string)) *[Grid](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid)

NewGridFrom returns a grid specified by the rows strings. All rows must be the same length and must only contain the Open or Closed characters, NewGridFrom will panic otherwise.

func (g *[Grid](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/path/internal/testgraphs#Grid)) Dims() (r, c [int](https://pkg.go.dev/builtin#int))

Dims returns the dimensions of the grid.

Edge returns the edge between u and v.

EdgeBetween returns the edge between u and v.

From returns all the nodes reachable from u. Reachabilty requires that both ends of an edge must be open.

HasEdgeBetween returns whether there is an edge between u and v.

HasOpen returns whether n is an open node in the grid.

Node returns the node with the given ID if it exists in the graph, and nil otherwise.

NodeAt returns the node at (r, c). The returned node may be open or closed.

Nodes returns all the open nodes in the grid if AllVisible is false, otherwise all nodes are returned.

Render returns a text representation of the graph with the given path included. If the path is not a path in the grid Render returns a non-nil error and the path up to that point.

RowCol returns the row and column of the id. RowCol will panic if the node id is outside the range of the grid.

Set sets the node at position (r, c) to the specified open state.

String returns a string representation of the grid.

Weight returns the weight of the given edge.

WeightedEdge returns the weighted edge between u and v.

WeightedEdgeBetween returns the weighted edge between u and v.

XY returns the cartesian coordinates of n. If n is not a node in the grid, (NaN, NaN) is returned.

LimitedVisionGrid is a 2D grid planar undirected graph where the capacity to determine the presence of edges is dependent on the current and past positions on the grid. In the absence of information, the grid is optimistic.

Edge optimistically returns the edge from u to v.

EdgeBetween optimistically returns the edge between u and v.

From returns nodes that are optimistically reachable from u.

HasEdgeBetween optimistically returns whether an edge is exists between u and v.

MoveTo moves to the node n on the grid and returns a slice of newly seen and already known edges. MoveTo panics if n is nil.

Node returns the node with the given ID if it exists in the graph, and nil otherwise.

NodeAt returns the node at (r, c). The returned node may be open or closed.

Nodes returns all the nodes in the grid.

Render returns a text representation of the graph with the given path included. If the path is not a path in the grid Render returns a non-nil error and the path up to that point.

RowCol returns the row and column of the id. RowCol will panic if the node id is outside the range of the grid.

String returns a string representation of the grid.

Weight returns the weight of the given edge.

WeightedEdge optimistically returns the weighted edge from u to v.

WeightedEdgeBetween optimistically returns the weighted edge between u and v.

XY returns the cartesian coordinates of n. If n is not a node in the grid, (NaN, NaN) is returned.
