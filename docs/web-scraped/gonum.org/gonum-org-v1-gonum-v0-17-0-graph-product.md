# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product

Title: product package - gonum.org/v1/gonum/graph/product - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product

Markdown Content:
Package product implements graph product functions.

All the graph products in this package are graphs with order n₁n₂ where n₁ and n₂ are the orders of the input graphs. This is the order of the set of the Cartesian product of the two input graphs' nodes.

The nodes of the product hold the original input graphs' nodes in the A and B fields in product.Nodes. This allows a mapping between the input graphs and their products.

See [https://en.wikipedia.org/wiki/Graph_product](https://en.wikipedia.org/wiki/Graph_product) for more details about graph products.

*   [func Cartesian(dst graph.Builder, a, b graph.Graph)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product#Cartesian)
*   [func CoNormal(dst graph.Builder, a, b graph.Graph)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product#CoNormal)
*   [func Lexicographical(dst graph.Builder, a, b graph.Graph)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product#Lexicographical)
*   [func Modular(dst graph.Builder, a, b graph.Graph)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product#Modular)
*   [func ModularExt(dst graph.Builder, a, b graph.Graph, agree func(eA, eB graph.Edge) bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product#ModularExt)
*   [func Strong(dst graph.Builder, a, b graph.Graph)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product#Strong)
*   [func Tensor(dst graph.Builder, a, b graph.Graph)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product#Tensor)
*   [type Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product#Node)
*       *   [func (n Node) ID() int64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product#Node.ID)

*   [Modular (SubgraphIsomorphism)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product#example-Modular-SubgraphIsomorphism)
*   [ModularExt (SubgraphIsomorphism)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/product#example-ModularExt-SubgraphIsomorphism)

This section is empty.

This section is empty.

Cartesian constructs the Cartesian product of a and b in dst.

The Cartesian product of G₁ and G₂, G₁□G₂ has edges (u₁, u₂)~(v₁, v₂) when (u₁=v₁ and u₂~v₂) or (u₁~v₁ and u₂=v₂). The Cartesian product has size m₂n₁+m₁n₂ where m is the size of the input graphs and n is their order.

CoNormal constructs the Co-normal product of a and b in dst.

The Co-normal product of G₁ and G₂, G₁*G₂ (or G₁[G₂]) has edges (u₁, u₂)~(v₁, v₂) when u₁~v₁ or u₂~v₂. The Co-normal product is non-commutative.

Lexicographical constructs the Lexicographical product of a and b in dst.

The Lexicographical product of G₁ and G₂, G₁·G₂ has edges (u₁, u₂)~(v₁, v₂) when u₁~v₁ or (u₁=v₁ and u₂~v₂). The Lexicographical product has size m₂n₁+m₁n₂² where m is the size of the input graphs and n is their order.

Modular constructs the Modular product of a and b in dst.

The Modular product of G₁ and G₂, G₁◊G₂ has edges (u₁, u₂)~(v₁, v₂) when (u₁~v₁ and u₂~v₂) or (u₁≁v₁ and u₂≁v₂), and (u₁≠v₁ and u₂≠v₂).

Modular is O(n^2) time where n is the order of the Cartesian product of a and b.

package main

import (
	"fmt"
	"os"
	"sort"
	"text/tabwriter"

	"gonum.org/v1/gonum/graph"
	"gonum.org/v1/gonum/graph/product"
	"gonum.org/v1/gonum/graph/simple"
	"gonum.org/v1/gonum/graph/topo"
)

// atom is a graph.Node representing an atom in a molecule.
type atom struct {
	name string // name is the name of the atom.
	pos  int    // pos is the position number of the atom.
	id   int64
}

// ID satisfies the graph.Node interface.
func (n atom) ID() int64 { return n.id }

func main() {
	// The modular product can be used to find subgraph isomorphisms.
	// See https://doi.org/10.1016/0020-0190(76)90049-1 and for a
	// theoretical perspective, https://doi.org/10.1145/990524.990529.

	// We can find the common structure between two organic molecules.
	// For example the purines adenine and guanine from nucleic acids.

	// Make a graph for adenine.
	adenine := simple.NewUndirectedGraph()
	for _, bond := range []simple.Edge{
		// Purine nucleus.
		{F: atom{name: "N", pos: 1, id: 0}, T: atom{name: "C", pos: 2, id: 1}},
		{F: atom{name: "N", pos: 1, id: 0}, T: atom{name: "C", pos: 6, id: 5}},
		{F: atom{name: "C", pos: 2, id: 1}, T: atom{name: "N", pos: 3, id: 2}},
		{F: atom{name: "N", pos: 3, id: 2}, T: atom{name: "C", pos: 4, id: 3}},
		{F: atom{name: "C", pos: 4, id: 3}, T: atom{name: "C", pos: 5, id: 4}},
		{F: atom{name: "C", pos: 4, id: 3}, T: atom{name: "N", pos: 9, id: 8}},
		{F: atom{name: "C", pos: 5, id: 4}, T: atom{name: "C", pos: 6, id: 5}},
		{F: atom{name: "C", pos: 5, id: 4}, T: atom{name: "N", pos: 7, id: 6}},
		{F: atom{name: "N", pos: 7, id: 6}, T: atom{name: "C", pos: 8, id: 7}},
		{F: atom{name: "C", pos: 8, id: 7}, T: atom{name: "N", pos: 9, id: 8}},

		// Amino modification in adenine.
		//
		// Note that the position number of the N is non-standard.
		{F: atom{name: "C", pos: 6, id: 5}, T: atom{name: "N", pos: 10, id: 9}},
	} {
		adenine.SetEdge(bond)
	}

	// Make a graph for guanine.
	//
	// Note that node IDs here have no intersection with
	// the adenine graph to show that they are not being
	// used to map between the graphs.
	guanine := simple.NewUndirectedGraph()
	for _, bond := range []simple.Edge{
		// Purine nucleus.
		{F: atom{name: "N", pos: 1, id: 10}, T: atom{name: "C", pos: 2, id: 11}},
		{F: atom{name: "N", pos: 1, id: 10}, T: atom{name: "C", pos: 6, id: 15}},
		{F: atom{name: "C", pos: 2, id: 11}, T: atom{name: "N", pos: 3, id: 12}},
		{F: atom{name: "N", pos: 3, id: 12}, T: atom{name: "C", pos: 4, id: 13}},
		{F: atom{name: "C", pos: 4, id: 13}, T: atom{name: "C", pos: 5, id: 14}},
		{F: atom{name: "C", pos: 4, id: 13}, T: atom{name: "N", pos: 9, id: 18}},
		{F: atom{name: "C", pos: 5, id: 14}, T: atom{name: "C", pos: 6, id: 15}},
		{F: atom{name: "C", pos: 5, id: 14}, T: atom{name: "N", pos: 7, id: 16}},
		{F: atom{name: "N", pos: 7, id: 16}, T: atom{name: "C", pos: 8, id: 17}},
		{F: atom{name: "C", pos: 8, id: 17}, T: atom{name: "N", pos: 9, id: 18}},

		// Amino and keto modifications in guanine.
		//
		// Note that the position number of the N and O is non-standard.
		{F: atom{name: "C", pos: 2, id: 11}, T: atom{name: "N", pos: 11, id: 19}},
		{F: atom{name: "C", pos: 6, id: 15}, T: atom{name: "O", pos: 10, id: 20}},
	} {
		guanine.SetEdge(bond)
	}

	// Produce the modular product of the two graphs.
	p := simple.NewUndirectedGraph()
	product.Modular(p, adenine, guanine)

	// Find the maximal cliques in the modular product.
	mc := topo.BronKerbosch(p)

	// Report the largest.
	sortByLengthDescending(mc)
	max := len(mc[0])
	w := tabwriter.NewWriter(os.Stdout, 5, 0, 0, ' ', tabwriter.AlignRight)
	fmt.Println("  Adenine   Guanine")
	fmt.Fprintln(w, "Atom\tPos\tAtom\tPos\t")
	for _, c := range mc {
		if len(c) < max {
			break
		}
		for _, p := range c {
			// Extract the mapping between the
			// inputs from the product.
			p := p.(product.Node)
			adenine := p.A.(atom)
			guanine := p.B.(atom)
			fmt.Fprintf(w, "%s\t%d\t%s\t%d\t\n", adenine.name, adenine.pos, guanine.name, guanine.pos)
		}
	}
	w.Flush()

}

func sortByLengthDescending(mc [][]graph.Node) {
	sort.Slice(mc, func(i, j int) bool { return len(mc[i]) > len(mc[j]) })
}
Output:

 Adenine Guanine Atom Pos Atom Pos N 3 N 3 N 7 N 7 N 10 O 10 C 6 C 6 C 2 C 2 C 8 C 8 C 5 C 5 N 9 N 9 N 1 N 1 C 4 C 4 

ModularExt constructs the Modular product of a and b in dst with additional control over assessing edge agreement.

In addition to the modular product conditions, agree(u₁v₁, u₂v₂) must return true when (u₁~v₁ and u₂~v₂) for an edge to be added between (u₁, u₂) and (v₁, v₂) in dst. If agree is nil, Modular is called.

ModularExt is O(n^2) time where n is the order of the Cartesian product of a and b.

package main

import (
	"fmt"

	"gonum.org/v1/gonum/graph"
	"gonum.org/v1/gonum/graph/iterator"
	"gonum.org/v1/gonum/graph/product"
	"gonum.org/v1/gonum/graph/simple"
	"gonum.org/v1/gonum/graph/topo"
)

// person is a graph.Node representing a person.
type person struct {
	name string // name is the name of the person.
	id   int64
}

// ID satisfies the graph.Node interface.
func (n person) ID() int64 { return n.id }

func main() {
	// Extended attributes of the graph can be used to refine
	// subgraph isomorphism identification. By filtering edge
	// agreement by weight we can identify social network
	// motifs within a larger graph.
	//
	// This example extracts sources of conflict from the
	// relationships of Julius Caesar, Mark Antony and
	// Cleopatra.

	// Make a graph describing people's relationships.
	//
	// Edge weight indicates love/animosity.
	people := simple.NewDirectedGraph()
	for _, relationship := range []simple.WeightedEdge{
		{F: person{name: "Julius Caesar", id: 0}, T: person{name: "Cleopatra", id: 1}, W: 1},
		{F: person{name: "Cleopatra", id: 1}, T: person{name: "Julius Caesar", id: 0}, W: 1},
		{F: person{name: "Julius Caesar", id: 0}, T: person{name: "Cornelia", id: 3}, W: 1},
		{F: person{name: "Cornelia", id: 3}, T: person{name: "Julius Caesar", id: 0}, W: 1},
		{F: person{name: "Mark Antony", id: 2}, T: person{name: "Cleopatra", id: 1}, W: 1},
		{F: person{name: "Cleopatra", id: 1}, T: person{name: "Mark Antony", id: 2}, W: 1},
		{F: person{name: "Fulvia", id: 4}, T: person{name: "Mark Antony", id: 2}, W: 1},
		{F: person{name: "Fulvia", id: 4}, T: person{name: "Cleopatra", id: 1}, W: -1},
		{F: person{name: "Octavia", id: 5}, T: person{name: "Mark Antony", id: 2}, W: 1},
		{F: person{name: "Octavia", id: 5}, T: person{name: "Cleopatra", id: 1}, W: -1},
	} {
		people.SetEdge(relationship)
	}

	// Make a graph for the query pattern: a love triangle.
	pattern := simple.NewDirectedGraph()
	for _, relationship := range []simple.WeightedEdge{
		{F: person{name: "A", id: -1}, T: person{name: "B", id: -2}, W: 1},
		{F: person{name: "B", id: -2}, T: person{name: "A", id: -1}, W: 1},
		{F: person{name: "C", id: -3}, T: person{name: "A", id: -1}, W: -1},
		{F: person{name: "C", id: -3}, T: person{name: "B", id: -2}, W: 1},
	} {
		pattern.SetEdge(relationship)
	}

	// Produce the modular product of the two graphs.
	p := simple.NewDirectedGraph()
	product.ModularExt(p, people, pattern, func(a, b graph.Edge) bool {
		return a.(simple.WeightedEdge).Weight() == b.(simple.WeightedEdge).Weight()
	})

	// Find the maximal cliques in the undirected induction
	// of the modular product.
	mc := topo.BronKerbosch(undirected{p})

	// Report the cliques that are identical in order to the pattern.
	fmt.Println("Person — Relationship position:")
	for _, c := range mc {
		if len(c) != pattern.Nodes().Len() {
			continue
		}
		for _, p := range c {
			// Extract the mapping between the
			// inputs from the product.
			p := p.(product.Node)
			people := p.A.(person)
			pattern := p.B.(person)
			fmt.Printf(" %s — %s\n", people.name, pattern.name)
		}
		fmt.Println()
	}

}

// undirected converts a directed graph to an undirected graph
// with edges between nodes only where directed edges exist in
// both directions in the original graph.
type undirected struct {
	graph.Directed
}

func (g undirected) From(uid int64) graph.Nodes {
	nodes := graph.NodesOf(g.Directed.From(uid))
	for i := 0; i < len(nodes); {
		if g.Directed.Edge(nodes[i].ID(), uid) != nil {
			i++
		} else {
			nodes[i], nodes = nodes[len(nodes)-1], nodes[:len(nodes)-1]
		}
	}
	return iterator.NewOrderedNodes(nodes)
}
func (g undirected) Edge(xid, yid int64) graph.Edge {
	e := g.Directed.Edge(xid, yid)
	if e != nil && g.Directed.Edge(yid, xid) != nil {
		return e
	}
	return nil
}
func (g undirected) EdgeBetween(xid, yid int64) graph.Edge {
	return g.Edge(xid, yid)
}
Output:

Person — Relationship position: Cleopatra — A Mark Antony — B Octavia — C Cleopatra — A Mark Antony — B Fulvia — C 

Strong constructs the Strong product of a and b in dst.

The Strong product of G₁ and G₂, G₁⊠G₂ has edges (u₁, u₂)~(v₁, v₂) when (u₁=v₁ and u₂~v₂) or (u₁~v₁ and u₂=v₂) or (u₁~v₁ and u₂~v₂). The Strong product has size n₁m₂+n₂m₁+2m₁m₂ where m is the size of the input graphs and n is their order.

Tensor constructs the Tensor product of a and b in dst.

The Tensor product of G₁ and G₂, G₁⨯G₂ has edges (u₁, u₂)~(v₁, v₂) when u₁~v₁ and u₂~v₂. The Tensor product has size 2m₁m₂ where m is the size of the input graphs.

Node is a product of two graph nodes. All graph products return this type directly via relevant graph.Graph method call, or indirectly via calls to graph.Edge methods from returned edges.

ID implements the graph.Node interface.
