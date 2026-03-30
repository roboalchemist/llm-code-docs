# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf

Title: rdf package - gonum.org/v1/gonum/graph/formats/rdf - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf

Markdown Content:
Package rdf implements decoding the RDF 1.1 N-Quads line-based plain text format for encoding an RDF dataset. N-Quad parsing is performed as defined by [http://www.w3.org/TR/n-quads/](http://www.w3.org/TR/n-quads/)

Output:

 digraph smiths { // Node definitions. "_:alice"; "_:bob"; "Alice"; "Smith"; "Bob"; // Edge definitions. "_:alice" -> "_:bob" [label=<http://xmlns.com/foaf/0.1/knows>]; "_:alice" -> "Alice" [label=<http://xmlns.com/foaf/0.1/givenName>]; "_:alice" -> "Smith" [label=<http://xmlns.com/foaf/0.1/familyName>]; "_:bob" -> "_:alice" [label=<http://xmlns.com/foaf/0.1/knows>]; "_:bob" -> "Smith" [label=<http://xmlns.com/foaf/0.1/familyName>]; "_:bob" -> "Bob" [label=<http://xmlns.com/foaf/0.1/givenName>]; } Term ID _:alice 1 _:bob 2 <http://xmlns.com/foaf/0.1/knows> 3 "Alice" 4 <http://xmlns.com/foaf/0.1/givenName> 5 "Smith" 6 <http://xmlns.com/foaf/0.1/familyName> 7 "Bob" 8 

*   [Variables](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#pkg-variables)
*   [func ConnectedByAny(e graph.Edge, with func(*Statement) bool) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#ConnectedByAny)
*   [func IsoCanonicalHashes(statements []*Statement, decomp, dist bool, h hash.Hash, zero []byte) (hashes map[string][]byte, terms map[string]map[string]bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#IsoCanonicalHashes)
*   [func Isomorphic(a, b []*Statement, decomp bool, h hash.Hash) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Isomorphic)
*   [type Decoder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Decoder)
*       *   [func NewDecoder(r io.Reader) *Decoder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#NewDecoder)

*       *   [func (dec *Decoder) Reset(r io.Reader)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Decoder.Reset)
    *   [func (dec *Decoder) Terms() map[string]int64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Decoder.Terms)
    *   [func (dec *Decoder) Unmarshal() (*Statement, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Decoder.Unmarshal)

*   [type Graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph)
*       *   [func NewGraph() *Graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#NewGraph)

*       *   [func (g *Graph) AddStatement(s *Statement)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.AddStatement)
    *   [func (g *Graph) AllStatements() *Statements](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.AllStatements)
    *   [func (g *Graph) Edge(uid, vid int64) graph.Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.Edge)
    *   [func (g *Graph) Edges() graph.Edges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.Edges)
    *   [func (g *Graph) From(id int64) graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.From)
    *   [func (g *Graph) FromSubject(t Term) graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.FromSubject)
    *   [func (g *Graph) HasEdgeBetween(xid, yid int64) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.HasEdgeBetween)
    *   [func (g *Graph) HasEdgeFromTo(uid, vid int64) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.HasEdgeFromTo)
    *   [func (g *Graph) Lines(uid, vid int64) graph.Lines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.Lines)
    *   [func (g *Graph) Node(id int64) graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.Node)
    *   [func (g *Graph) Nodes() graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.Nodes)
    *   [func (g *Graph) Predicates() []Term](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.Predicates)
    *   [func (g *Graph) Query(from ...Term) Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.Query)
    *   [func (g *Graph) RemoveStatement(s *Statement)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.RemoveStatement)
    *   [func (g *Graph) RemoveTerm(t Term)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.RemoveTerm)
    *   [func (g *Graph) Statements(uid, vid int64) *Statements](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.Statements)
    *   [func (g *Graph) TermFor(text string) (term Term, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.TermFor)
    *   [func (g *Graph) To(id int64) graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.To)
    *   [func (g *Graph) ToObject(t Term) graph.Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph.ToObject)

*   [type Kind](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Kind)
*       *   [func (i Kind) String() string](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Kind.String)

*   [type Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)
*       *   [func NewQuery(g graph.Directed, from ...Term) Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#NewQuery)

*       *   [func (q Query) And(p Query) Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.And)
    *   [func (q Query) HasAllIn(fn func(s *Statement) bool) Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.HasAllIn)
    *   [func (q Query) HasAllOut(fn func(s *Statement) bool) Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.HasAllOut)
    *   [func (q Query) HasAnyIn(fn func(s *Statement) bool) Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.HasAnyIn)
    *   [func (q Query) HasAnyOut(fn func(s *Statement) bool) Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.HasAnyOut)
    *   [func (q Query) In(fn func(s *Statement) bool) Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.In)
    *   [func (q Query) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.Len)
    *   [func (q Query) Not(p Query) Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.Not)
    *   [func (q Query) Or(p Query) Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.Or)
    *   [func (q Query) Out(fn func(s *Statement) bool) Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.Out)
    *   [func (q Query) Repeat(fn func(Query) (q Query, ok bool)) Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.Repeat)
    *   [func (q Query) Result() []Term](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.Result)
    *   [func (q Query) Unique() Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.Unique)

*   [type Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement)
*       *   [func C14n(dst, src []*Statement, terms map[string]map[string]bool) ([]*Statement, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#C14n)
    *   [func Deduplicate(s []*Statement) []*Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Deduplicate)
    *   [func Lean(g []*Statement) ([]*Statement, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Lean)
    *   [func ParseNQuad(statement string) (*Statement, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#ParseNQuad)
    *   [func URDNA2015(dst, src []*Statement) ([]*Statement, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#URDNA2015)
    *   [func URGNA2012(dst, src []*Statement) ([]*Statement, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#URGNA2012)

*       *   [func (s *Statement) From() graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement.From)
    *   [func (s *Statement) ID() int64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement.ID)
    *   [func (s *Statement) ReversedEdge() graph.Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement.ReversedEdge)
    *   [func (s *Statement) ReversedLine() graph.Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement.ReversedLine)
    *   [func (s *Statement) String() string](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement.String)
    *   [func (s *Statement) To() graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement.To)

*   [type Statements](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statements)
*       *   [func (s *Statements) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statements.Next)
    *   [func (s *Statements) Statement() *Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statements.Statement)

*   [type Term](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Term)
*       *   [func NewBlankTerm(label string) (Term, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#NewBlankTerm)
    *   [func NewIRITerm(iri string) (Term, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#NewIRITerm)
    *   [func NewLiteralTerm(text, qual string) (Term, error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#NewLiteralTerm)

*       *   [func (t Term) ID() int64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Term.ID)
    *   [func (t Term) Parts() (text, qual string, kind Kind, err error)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Term.Parts)

*   [Bugs](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#pkg-note-BUG)

*   [Package (Graph)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#example-package-Graph)
*   [C14n](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#example-C14n)
*   [Graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#example-Graph)
*   [IsoCanonicalHashes (IsomorphicParts)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#example-IsoCanonicalHashes-IsomorphicParts)
*   [IsoCanonicalHashes (Isomorphisms)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#example-IsoCanonicalHashes-Isomorphisms)
*   [Lean](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#example-Lean)
*   [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#example-Query)
*   [Statement.ReversedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#example-Statement.ReversedLine)
*   [URDNA2015](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#example-URDNA2015)
*   [URGNA2012](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#example-URGNA2012)

This section is empty.

ConnectedByAny is a helper function to for simplifying graph traversal conditions.

IsoCanonicalHashes returns a mapping between the nodes of the RDF graph dataset described by the given statements using the provided hash function. If decomp is true, the graphs are decomposed before hashing. If dist is true the input graph is decomposed into identical splits, the entire graph will be hashed to distinguish nodes. If decomp is false, dist has no effect. Blank node hashes are initially set to the value of zero. Hash values are provided for literal and IRI nodes as well as for blank node. The hash input for literal nodes includes the quotes and the input for IRI nodes first removes the angle quotes around the IRI, although these are included in the map keys.

Note that hashes returned by IsoCanonicalHashes with decomp=true are not comparable with hashes returned by IsoCanonicalHashes with decomp=false.

See [http://aidanhogan.com/docs/rdf-canonicalisation.pdf](http://aidanhogan.com/docs/rdf-canonicalisation.pdf) for details of the hashing algorithm.

Output:

 Node Hash _:a d4db6df055d5611e9d8aa6ea621561d1 _:a1 d4db6df055d5611e9d8aa6ea621561d1 _:b ad70e47f2b026064c7f0922060512b9a _:b1 ad70e47f2b026064c7f0922060512b9a _:c dafd81e6fa603d3e11c898d631e8673f _:c1 dafd81e6fa603d3e11c898d631e8673f _:d 7e318557b09444e88791721becc2a8e7 _:d1 7e318557b09444e88791721becc2a8e7 

Output:

 No blank nodes. Node Hash _:a d4db6df055d5611e9d8aa6ea621561d1 _:b ad70e47f2b026064c7f0922060512b9a _:c dafd81e6fa603d3e11c898d631e8673f _:d 7e318557b09444e88791721becc2a8e7 Node Hash _:a1 d4db6df055d5611e9d8aa6ea621561d1 _:b1 ad70e47f2b026064c7f0922060512b9a _:c1 dafd81e6fa603d3e11c898d631e8673f _:d1 7e318557b09444e88791721becc2a8e7 Node Hash _:a 44ad49b6df3aea91ddbcef932c93e3b4 _:b ba3ffd8b271a8545b1a3a9042e75ce4b _:c 34e1bd90b6758b4a766e000128caa6a6 _:d eb2a47c1032f623647d0497a2ff74052 _:e 1d9ed02f28d87e555feb904688bc2449 _:f d3b00d36ea503dcc8d234e4405feab81 _:g 55127e4624c0a4fe5990933a48840af8 Node Hash _:greet 0d9ba18a037a3fa67e46fce821fe51b4 

Isomorphic returns whether the RDF graph datasets a and b are isomorphic, where there is a bijective mapping between blank nodes in a and b using the given hash function. If decomp is true, the graphs are decomposed before canonicalization.

type Decoder struct {
	
}

Decoder is an RDF stream decoder. Statements returned by calls to the Unmarshal method have their Terms' UID fields set so that unique terms will have unique IDs and so can be used directly in a graph.Multi, or in a graph.Graph if all predicate terms are identical. IDs created by the decoder all exist within a single namespace and so Terms can be uniquely identified by their UID. Term UIDs are based from 1 to allow RDF-aware client graphs to assign ID if no ID has been assigned.

NewDecoder returns a new Decoder that takes input from r.

Reset resets the decoder to use the provided io.Reader, retaining the existing Term ID mapping.

Terms returns the mapping between terms and graph node IDs constructed during decoding the RDF statement stream.

func (dec *[Decoder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Decoder)) Unmarshal() (*[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement), [error](https://pkg.go.dev/builtin#error))

Unmarshal returns the next statement from the input stream.

type Graph struct {
	
}

Graph implements an RDF graph satisfying the graph.Graph and graph.Multigraph interfaces.

NewGraph returns a new empty Graph.

func (g *[Graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph)) AddStatement(s *[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement))

AddStatement adds s to the graph. It panics if Term UIDs in the statement are not consistent with existing terms in the graph. Statements must not be altered while being held by the graph. If the UID fields of the terms in s are zero, they will be set to values consistent with the rest of the graph on return, mutating the parameter, otherwise the UIDs must match terms that already exist in the graph. The statement must be a valid RDF statement otherwise AddStatement will panic.

func (g *[Graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph)) AllStatements() *[Statements](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statements)

AllStatements returns an iterator of the statements that make up the graph.

Edge returns the edge from u to v if such an edge exists and nil otherwise. The node v must be directly reachable from u as defined by the From method. The returned graph.Edge is a multi.Edge if an edge exists.

Edges returns all the edges in the graph. Each edge in the returned slice is a multi.Edge.

From returns all nodes in g that can be reached directly from n.

The returned graph.Nodes is only valid until the next mutation of the receiver.

FromSubject returns all nodes in g that can be reached directly from an RDF subject term.

The returned graph.Nodes is only valid until the next mutation of the receiver.

HasEdgeBetween returns whether an edge exists between nodes x and y without considering direction.

HasEdgeFromTo returns whether an edge exists in the graph from u to v.

Lines returns the lines from u to v if such any such lines exists and nil otherwise. The node v must be directly reachable from u as defined by the From method.

Node returns the node with the given ID if it exists in the graph, and nil otherwise.

Nodes returns all the nodes in the graph.

The returned graph.Nodes is only valid until the next mutation of the receiver.

func (g *[Graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph)) Predicates() [][Term](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Term)

Predicates returns a slice of all the predicates used in the graph.

func (g *[Graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph)) Query(from ...[Term](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Term)) [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)

Query returns a query of the receiver starting from the given nodes. Queries may not be mixed between distinct graphs.

func (g *[Graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph)) RemoveStatement(s *[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement))

RemoveStatement removes s from the graph, leaving the terminal nodes if they are part of another statement. If the statement does not exist in g it is a no-op.

func (g *[Graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph)) RemoveTerm(t [Term](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Term))

RemoveTerm removes t and any statements referencing t from the graph. If the term is a predicate, all statements with the predicate are removed. If the term does not exist it is a no-op.

func (g *[Graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Graph)) Statements(uid, vid [int64](https://pkg.go.dev/builtin#int64)) *[Statements](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statements)

Statements returns an iterator of the statements that connect the subject term node u to the object term node v.

TermFor returns the Term for the given text. The text must be an exact match for the Term's Value field.

To returns all nodes in g that can reach directly to n.

The returned graph.Nodes is only valid until the next mutation of the receiver.

ToObject returns all nodes in g that can reach directly to an RDF object term.

The returned graph.Nodes is only valid until the next mutation of the receiver.

Kind represents the kind of an RDF term.

const (
	Invalid [Kind](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Kind) = [iota](https://pkg.go.dev/builtin#iota)

	
	IRI

	
	Literal

	
	Blank
)

type Query struct {
	
}

Query represents a step in an RDF graph query. The methods on Query provide a simple graph query language.

Output:

 Heracles' grandfather: "Cronos" Heracles' lineage 0: "Zeus" Heracles' lineage 1: "Cronos" Heracles' parents' types: "god" Heracles' parents' types: "human" Heracles' antagonists' types: "monster" Heracles' antagonists' types: "monster" Heracles' antagonists' types: "monster" map[name:"Cerberus"] map[name:"Lernean Hydra"] map[name:"Nemean Lion"] Heracles' allies: "Theseus" Hades lives with: "Cerberus" map[god:"Zeus" place:"Olympus"] map[god:"Poseidon" place:"Sea"] map[god:"Zeus" place:"Olympus" reason:"he can see everything"] map[god:"Poseidon" place:"Sea" reason:"it was given to him"] 

NewQuery returns a query of g starting from the given nodes. Queries may not be mixed between distinct graphs. The type of g must be comparable. Query operations only consider edges that are represented by a *Statement or is an edge with lines held in a graph.Lines with at least one *Statement.

#### func (Query) [And](https://github.com/gonum/gonum/blob/v0.17.0/graph/formats/rdf/query.go#L145)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query.And "Go to Query.And")

func (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) And(p [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)

And returns a query that holds the conjunction of q and p.

func (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) HasAllIn(fn func(s *[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement)) [bool](https://pkg.go.dev/builtin#bool)) [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)

HasAllIn returns a query holding nodes from the receiver's initial set where all incoming statements satisfy fn. The query short circuits, so fn is not called after the first failure to match.

func (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) HasAllOut(fn func(s *[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement)) [bool](https://pkg.go.dev/builtin#bool)) [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)

HasAllOut returns a query holding nodes from the receiver's initial set where all outgoing statements satisfy fn. The query short circuits, so fn is not called after the first failure to match.

func (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) HasAnyIn(fn func(s *[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement)) [bool](https://pkg.go.dev/builtin#bool)) [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)

HasAnyIn returns a query holding nodes from the receiver's initial set where any incoming statements satisfies fn. The query short circuits, so fn is not called after the first match.

func (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) HasAnyOut(fn func(s *[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement)) [bool](https://pkg.go.dev/builtin#bool)) [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)

HasAnyOut returns a query holding nodes from the receiver's initial set where any outgoing statements satisfies fn. The query short circuits, so fn is not called after the first match.

func (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) In(fn func(s *[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement)) [bool](https://pkg.go.dev/builtin#bool)) [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)

In returns a query holding nodes reachable in from the receiver's starting nodes via statements that satisfy fn.

Len returns the number of terms held by the query.

func (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) Not(p [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)

Not returns a query that holds q less p.

func (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) Or(p [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)

Or returns a query that holds the disjunction of q and p.

func (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) Out(fn func(s *[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement)) [bool](https://pkg.go.dev/builtin#bool)) [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)

Out returns a query holding nodes reachable out from the receiver's starting nodes via statements that satisfy fn.

func (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) Repeat(fn func([Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query), ok [bool](https://pkg.go.dev/builtin#bool))) [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)

Repeat repeatedly calls fn on q until the set of results is empty or ok is false, and then returns the result. If the last non-empty result is wanted, fn should return its input and false when the partial traversal returns an empty result.

result := start.Repeat(func(q rdf.Query) (rdf.Query, bool) {
	r := q.Out(condition)
	if r.Len() == 0 {
		return q, false
	}
	return r, true
}).Result()

func (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) Result() [][Term](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Term)

Result returns the terms held by the query.

func (q [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)) Unique() [Query](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Query)

Unique returns a copy of the receiver that contains only one instance of each term.

type Statement struct {
 Subject [Term](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Term) Predicate [Term](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Term) Object [Term](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Term) Label [Term](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Term)}

Statement is an RDF statement. It implements the graph.Edge and graph.Line interfaces.

C14n performs a relabeling of the statements in src based on the terms obtained from IsoCanonicalHashes, placing the results in dst and returning them. The relabeling scheme is the same as for the Universal RDF Dataset Normalization Algorithm, blank terms are ordered lexically by their hash value and then given a blank label with the prefix "_:c14n" and an identifier counter corresponding to the label's sort rank.

If dst is nil, it is allocated, otherwise the length of dst must match the length of src.

Output:

 _:c14n0 <ex:p> _:c14n1 . _:c14n1 <ex:q> <ex:p> . _:c14n2 <ex:q> <ex:p> . _:c14n3 <ex:p> _:c14n2 . _:c14n3 <ex:r> _:c14n0 . _:c14n0 <ex:p> _:c14n1 . _:c14n1 <ex:q> <ex:p> . _:c14n2 <ex:q> <ex:p> . _:c14n3 <ex:p> _:c14n2 . _:c14n3 <ex:r> _:c14n0 . 

func Deduplicate(s []*[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement)) []*[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement)

Deduplicate removes duplicate statements in s, working in place, and returns the deduplicated slice with statements sorted in lexical order. Term UID fields are not considered and their values may be lost during deduplication.

Lean returns an RDF core of g that entails g. If g contains any non-zero labels, Lean will return a non-nil error and a core of g assuming no graph labels exist.

See [http://aidanhogan.com/docs/rdf-canonicalisation.pdf](http://aidanhogan.com/docs/rdf-canonicalisation.pdf) for details of the algorithm.

Output:

 0: _:c14n0 <ex:contributesTo> _:c14n1 . 1: _:c14n0 <ex:contributesTo> _:c14n1 . _:c14n0 <ex:contributesTo> _:c14n2 . _:c14n2 <ex:dependsOn> _:c14n1 . 2: _:c14n0 <ex:contributesTo> _:c14n1 . _:c14n0 <ex:contributesTo> _:c14n3 . _:c14n2 <ex:contributesTo> _:c14n1 . _:c14n2 <ex:notContributesTo> _:c14n3 . _:c14n3 <ex:dependsOn> _:c14n1 . 3: _:c14n0 <ex:contributesTo> _:c14n1 . _:c14n0 <ex:contributesTo> _:c14n3 . _:c14n2 <ex:contributesTo> _:c14n1 . _:c14n2 <ex:is> "Alice" . _:c14n3 <ex:dependsOn> _:c14n1 . 4: _:c14n0 <ex:contributesTo> _:c14n1 . _:c14n0 <ex:contributesTo> _:c14n2 . _:c14n2 <ex:dependsOn> _:c14n1 . _:c14n3 <ex:contributesTo> _:c14n1 . _:c14n3 <ex:notContributesTo> _:c14n2 . _:c14n4 <ex:contributesTo> _:c14n2 . _:c14n4 <ex:notContributesTo> _:c14n1 . 5: _:c14n1 <ex:contributesTo> _:c14n0 . _:c14n1 <ex:contributesTo> _:c14n3 . _:c14n1 <ex:is> "Bob" . _:c14n2 <ex:contributesTo> _:c14n0 . _:c14n2 <ex:is> "Alice" . _:c14n3 <ex:dependsOn> _:c14n0 . 6: _:c14n0 <ex:dependsOn> _:c14n1 . _:c14n2 <ex:contributesTo> _:c14n0 . _:c14n2 <ex:contributesTo> _:c14n1 . _:c14n2 <ex:is> "Bob" . _:c14n3 <ex:contributesTo> _:c14n1 . _:c14n3 <ex:is> "Alice" . _:c14n4 <ex:contributesTo> _:c14n0 . _:c14n4 <ex:is> "Charlie" . 

ParseNQuad parses the statement and returns the corresponding Statement. All Term UID fields are zero on return.

func URDNA2015(dst, src []*[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement)) ([]*[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement), [error](https://pkg.go.dev/builtin#error))

URDNA2015 applies the Universal RDF Dataset Normalization Algorithm 2015 to the statements in src, placing the result in dst and returning it. If dst is nil a slice of statements will be allocated. If dst is not nil and not the same length as src, URDNA2015 will return an error.

See [https://json-ld.github.io/rdf-dataset-canonicalization/spec/index.html](https://json-ld.github.io/rdf-dataset-canonicalization/spec/index.html) for details.

Output:

 _:c14n0 <ex:p> _:c14n2 . _:c14n1 <ex:p> _:c14n3 . _:c14n1 <ex:r> _:c14n0 . _:c14n2 <ex:q> <ex:p> . _:c14n3 <ex:q> <ex:p> . _:c14n0 <ex:p> _:c14n2 . _:c14n1 <ex:p> _:c14n3 . _:c14n1 <ex:r> _:c14n0 . _:c14n2 <ex:q> <ex:p> . _:c14n3 <ex:q> <ex:p> . 

func URGNA2012(dst, src []*[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement)) ([]*[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement), [error](https://pkg.go.dev/builtin#error))

URGNA2012 applies the Universal RDF Graph Normalization Algorithm 2012 to the statements in src, placing the result in dst and returning it. If dst is nil a slice of statements will be allocated. If dst is not nil and not the same length as src, URGNA2012 will return an error.

See [https://json-ld.github.io/rdf-dataset-canonicalization/spec/index.html](https://json-ld.github.io/rdf-dataset-canonicalization/spec/index.html) for details.

Output:

 _:c14n0 <ex:p> _:c14n3 . _:c14n0 <ex:r> _:c14n1 . _:c14n1 <ex:p> _:c14n2 . _:c14n2 <ex:q> <ex:p> . _:c14n3 <ex:q> <ex:p> . _:c14n0 <ex:p> _:c14n3 . _:c14n0 <ex:r> _:c14n1 . _:c14n1 <ex:p> _:c14n2 . _:c14n2 <ex:q> <ex:p> . _:c14n3 <ex:q> <ex:p> . 

From returns the subject of the statement.

ID returns the UID of the Predicate field.

ReversedEdge returns the receiver unaltered. If there is a semantically valid edge reversal operation for the data, the user should implement this by wrapping Statement in a type performing that operation. See the ReversedLine example for details.

ReversedLine returns the receiver unaltered. If there is a semantically valid line reversal operation for the data, the user should implement this by wrapping Statement in a type performing that operation.

Output:

 digraph "food web" { // Node definitions. "_:wolf"; "_:animal"; "Wolf" [tax=common]; "Canis lupus" [tax=binomial]; "_:sheep"; "Sheep" [tax=common]; "Ovis aries" [tax=binomial]; "_:grass"; "_:plant"; "Grass" [tax=common]; "Lolium perenne" [tax=binomial]; "Festuca rubra" [tax=binomial]; "Poa pratensis" [tax=binomial]; // Edge definitions. "_:wolf" -> "_:animal" [tax="is-a"]; "_:wolf" -> "Wolf" [tax=is]; "_:wolf" -> "Canis lupus" [tax=is]; "_:wolf" -> "_:sheep" [eco=eats]; "_:animal" -> "_:wolf" [tax=includes]; "_:animal" -> "_:sheep" [tax=includes]; "_:sheep" -> "_:wolf" [eco="eaten-by"]; "_:sheep" -> "_:animal" [tax="is-a"]; "_:sheep" -> "Sheep" [tax=is]; "_:sheep" -> "Ovis aries" [tax=is]; "_:sheep" -> "_:grass" [eco=eats]; "_:grass" -> "_:sheep" [eco="eaten-by"]; "_:grass" -> "_:plant" [tax="is-a"]; "_:grass" -> "Grass" [tax=is]; "_:grass" -> "Lolium perenne" [tax=is]; "_:grass" -> "Festuca rubra" [tax=is]; "_:grass" -> "Poa pratensis" [tax=is]; "_:plant" -> "_:grass" [tax=includes]; } 

String returns the RDF 1.1 N-Quad formatted statement.

To returns the object of the statement.

type Statements struct {
	
}

Statements is an RDF statement iterator.

Next returns whether the iterator holds any additional statements.

func (s *[Statements](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statements)) Statement() *[Statement](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/rdf#Statement)

Statement returns the current statement.

Term is an RDF term. It implements the graph.Node interface.

NewBlankTerm returns a Term based on the provided RDF blank node label. The label should not include the "_:" prefix. The returned Term will not have the UID set.

NewIRITerm returns a Term based on the provided IRI which must be valid and include a scheme. The returned Term will not have the UID set.

NewLiteralTerm returns a Term based on the literal text and an optional qualifier which may either be a "@"-prefixed language tag or a valid IRI. The text will be escaped if necessary and quoted, and if an IRI is given it will be escaped if necessary. The returned Term will not have the UID set.

ID returns the value of the Term's UID field.

Parts returns the parts of the term and the kind of the term. IRI node text is returned as a valid IRI with the quoting angle brackets removed and escape sequences interpreted, and blank nodes are stripped of the "_:" prefix. When the term is a literal, qual will either be empty, an unescaped IRI, or an RDF language tag prefixed with an @ symbol. The literal text is returned unquoted and unescaped.

*   Graph leaning does not take into account graph label terms since the formal semantics for a multiple graph data model have not been defined. See [https://www.w3.org/TR/rdf11-datasets/#declaring](https://www.w3.org/TR/rdf11-datasets/#declaring).
