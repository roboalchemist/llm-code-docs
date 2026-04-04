# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12

Title: gexf12 package - gonum.org/v1/gonum/graph/formats/gexf12 - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12

Markdown Content:
Package gexf12 implements marshaling and unmarshaling of GEXF1.2 documents.

For details of GEXF see [https://gephi.org/gexf/format/](https://gephi.org/gexf/format/).

*   [type AttValue](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#AttValue)
*   [type AttValues](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#AttValues)
*   [type Attribute](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Attribute)
*   [type Attributes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Attributes)
*   [type Color](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Color)
*   [type Content](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Content)
*   [type Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Edge)
*   [type Edges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Edges)
*   [type Edgeshape](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Edgeshape)
*   [type Graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Graph)
*   [type Meta](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Meta)
*       *   [func (t *Meta) MarshalXML(e *xml.Encoder, start xml.StartElement) error](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Meta.MarshalXML)
    *   [func (t *Meta) UnmarshalXML(d *xml.Decoder, start xml.StartElement) error](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Meta.UnmarshalXML)

*   [type Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Node)
*   [type NodeShape](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#NodeShape)
*   [type Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Nodes)
*   [type Parent](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Parent)
*   [type Parents](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Parents)
*   [type Position](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Position)
*   [type Size](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Size)
*   [type Spell](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Spell)
*   [type Spells](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Spells)
*   [type Thickness](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Thickness)
*   [Bugs](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#pkg-note-BUG)

This section is empty.

This section is empty.

This section is empty.

type AttValue struct {
 For [string](https://pkg.go.dev/builtin#string) `xml:"for,attr"`  Value [string](https://pkg.go.dev/builtin#string) `xml:"value,attr"`  Start [string](https://pkg.go.dev/builtin#string) `xml:"start,attr,omitempty"`  StartOpen [string](https://pkg.go.dev/builtin#string) `xml:"startopen,attr,omitempty"`  End [string](https://pkg.go.dev/builtin#string) `xml:"end,attr,omitempty"`  EndOpen [string](https://pkg.go.dev/builtin#string) `xml:"endopen,attr,omitempty"` }

AttValue holds a single attribute value and its associated dynamics.

type AttValues struct {
 AttValues [][AttValue](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#AttValue) `xml:"attvalue,omitempty"` }

AttValues holds a collection of attribute values.

type Attribute struct {
 ID [string](https://pkg.go.dev/builtin#string) `xml:"id,attr"`  Title [string](https://pkg.go.dev/builtin#string) `xml:"title,attr"` 	
	
 Type [string](https://pkg.go.dev/builtin#string) `xml:"type,attr"`  Default [string](https://pkg.go.dev/builtin#string) `xml:"default,omitempty"`  Options [string](https://pkg.go.dev/builtin#string) `xml:"options,omitempty"` }

Attribute holds a single graph attribute.

type Attributes struct {
 Attributes [][Attribute](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Attribute) `xml:"attribute,omitempty"` 	Class [string](https://pkg.go.dev/builtin#string) `xml:"class,attr"`
	
 Mode [string](https://pkg.go.dev/builtin#string) `xml:"mode,attr,omitempty"`  Start [string](https://pkg.go.dev/builtin#string) `xml:"start,attr,omitempty"`  StartOpen [string](https://pkg.go.dev/builtin#string) `xml:"startopen,attr,omitempty"`  End [string](https://pkg.go.dev/builtin#string) `xml:"end,attr,omitempty"`  EndOpen [string](https://pkg.go.dev/builtin#string) `xml:"endopen,attr,omitempty"` }

Attributes holds a collection of potentially dynamic attributes associated with a graph.

type Color struct {
 Spells *[Spells](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Spells) `xml:"spells,omitempty"`  R [byte](https://pkg.go.dev/builtin#byte) `xml:"r,attr"`  G [byte](https://pkg.go.dev/builtin#byte) `xml:"g,attr"`  B [byte](https://pkg.go.dev/builtin#byte) `xml:"b,attr"`  A [float64](https://pkg.go.dev/builtin#float64) `xml:"a,attr,omitempty"`  Start [string](https://pkg.go.dev/builtin#string) `xml:"start,attr,omitempty"`  StartOpen [string](https://pkg.go.dev/builtin#string) `xml:"startopen,attr,omitempty"`  End [string](https://pkg.go.dev/builtin#string) `xml:"end,attr,omitempty"`  EndOpen [string](https://pkg.go.dev/builtin#string) `xml:"endopen,attr,omitempty"` }

Color represents a node or edge color and its associated dynamics.

#### type [Content](https://github.com/gonum/gonum/blob/v0.17.0/graph/formats/gexf12/gexf.go#L21)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Content "Go to Content")

type Content struct {
 XMLName [xml](https://pkg.go.dev/encoding/xml).[Name](https://pkg.go.dev/encoding/xml#Name) `xml:"http://www.gexf.net/1.2draft gexf"`  Meta *[Meta](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Meta) `xml:"meta,omitempty"`  Graph [Graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Graph) `xml:"graph"` 	
 Version [string](https://pkg.go.dev/builtin#string) `xml:"version,attr"`  Variant [string](https://pkg.go.dev/builtin#string) `xml:"variant,attr,omitempty"` }

Content holds a GEFX graph and metadata.

type Edge struct {
 ID [string](https://pkg.go.dev/builtin#string) `xml:"id,attr,omitempty"`  AttValues *[AttValues](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#AttValues) `xml:"attvalues"`  Spells *[Spells](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Spells) `xml:"spells"`  Color *[Color](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Color) `xml:"http://www.gexf.net/1.2draft/viz color"`  Thickness *[Thickness](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Thickness) `xml:"http://www.gexf.net/1.2draft/viz thickness"`  Shape *[Edgeshape](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Edgeshape) `xml:"http://www.gexf.net/1.2draft/viz shape"`  Start [string](https://pkg.go.dev/builtin#string) `xml:"start,attr,omitempty"`  StartOpen [string](https://pkg.go.dev/builtin#string) `xml:"startopen,attr,omitempty"`  End [string](https://pkg.go.dev/builtin#string) `xml:"end,attr,omitempty"`  EndOpen [string](https://pkg.go.dev/builtin#string) `xml:"endopen,attr,omitempty"` 	
 Type [string](https://pkg.go.dev/builtin#string) `xml:"type,attr,omitempty"`  Label [string](https://pkg.go.dev/builtin#string) `xml:"label,attr,omitempty"`  Source [string](https://pkg.go.dev/builtin#string) `xml:"source,attr"`  Target [string](https://pkg.go.dev/builtin#string) `xml:"target,attr"`  Weight [float64](https://pkg.go.dev/builtin#float64) `xml:"weight,attr,omitempty"` }

Edge is a single edge and its associated attributes.

type Edges struct {
 Count [int](https://pkg.go.dev/builtin#int) `xml:"count,attr,omitempty"`  Edges [][Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Edge) `xml:"edge,omitempty"` }

Edges holds a collection of edges constituting a graph or subgraph.

type Edgeshape struct {
	
 Shape [string](https://pkg.go.dev/builtin#string) `xml:"value,attr"`  Spells *[Spells](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Spells) `xml:"spells,omitempty"`  Start [string](https://pkg.go.dev/builtin#string) `xml:"start,attr,omitempty"`  StartOpen [string](https://pkg.go.dev/builtin#string) `xml:"startopen,attr,omitempty"`  End [string](https://pkg.go.dev/builtin#string) `xml:"end,attr,omitempty"`  EndOpen [string](https://pkg.go.dev/builtin#string) `xml:"endopen,attr,omitempty"` }

Edgeshape holds the visual representation of an edge with associated dynamics.

type Graph struct {
 Attributes [][Attributes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Attributes) `xml:"attributes"`  Nodes [Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Nodes) `xml:"nodes"`  Edges [Edges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Edges) `xml:"edges"` 	
 TimeFormat [string](https://pkg.go.dev/builtin#string) `xml:"timeformat,attr,omitempty"`  Start [string](https://pkg.go.dev/builtin#string) `xml:"start,attr,omitempty"`  StartOpen [string](https://pkg.go.dev/builtin#string) `xml:"startopen,attr,omitempty"`  End [string](https://pkg.go.dev/builtin#string) `xml:"end,attr,omitempty"`  EndOpen [string](https://pkg.go.dev/builtin#string) `xml:"endopen,attr,omitempty"` 	DefaultEdgeType [string](https://pkg.go.dev/builtin#string) `xml:"defaultedgetype,attr,omitempty"`
	IDType [string](https://pkg.go.dev/builtin#string) `xml:"idtype,attr,omitempty"`
	Mode [string](https://pkg.go.dev/builtin#string) `xml:"mode,attr,omitempty"`
}

Graph stores the graph nodes, edges, dynamics and visualization data.

type Meta struct {
 Creator [string](https://pkg.go.dev/builtin#string) `xml:"creator,omitempty"`  Keywords [string](https://pkg.go.dev/builtin#string) `xml:"keywords,omitempty"`  Description [string](https://pkg.go.dev/builtin#string) `xml:"description,omitempty"`  LastModified [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time) `xml:"lastmodifieddate,attr,omitempty"` }

Meta holds optional metadata associated with the graph.

MarshalXML implements the xml.Marshaler interface.

UnmarshalXML implements the xml.Unmarshaler interface.

type Node struct {
 ID [string](https://pkg.go.dev/builtin#string) `xml:"id,attr,omitempty"`  Label [string](https://pkg.go.dev/builtin#string) `xml:"label,attr,omitempty"`  AttValues *[AttValues](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#AttValues) `xml:"attvalues"`  Spells *[Spells](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Spells) `xml:"spells"`  Nodes *[Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Nodes) `xml:"nodes"`  Edges *[Edges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Edges) `xml:"edges"`  ParentID [string](https://pkg.go.dev/builtin#string) `xml:"pid,attr,omitempty"`  Parents *[Parents](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Parents) `xml:"parents"`  Color *[Color](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Color) `xml:"http://www.gexf.net/1.2draft/viz color"`  Position *[Position](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Position) `xml:"http://www.gexf.net/1.2draft/viz position"`  Size *[Size](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Size) `xml:"http://www.gexf.net/1.2draft/viz size"`  Shape *[NodeShape](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#NodeShape) `xml:"http://www.gexf.net/1.2draft/viz shape"`  Start [string](https://pkg.go.dev/builtin#string) `xml:"start,attr,omitempty"`  StartOpen [string](https://pkg.go.dev/builtin#string) `xml:"startopen,attr,omitempty"`  End [string](https://pkg.go.dev/builtin#string) `xml:"end,attr,omitempty"`  EndOpen [string](https://pkg.go.dev/builtin#string) `xml:"endopen,attr,omitempty"` }

Node is a single node and its associated attributes.

type NodeShape struct {
 Spells *[Spells](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Spells) `xml:"spells,omitempty"` 	
	
 Shape [string](https://pkg.go.dev/builtin#string) `xml:"value,attr"`  URI [string](https://pkg.go.dev/builtin#string) `xml:"uri,attr,omitempty"`  Start [string](https://pkg.go.dev/builtin#string) `xml:"start,attr,omitempty"`  StartOpen [string](https://pkg.go.dev/builtin#string) `xml:"startopen,attr,omitempty"`  End [string](https://pkg.go.dev/builtin#string) `xml:"end,attr,omitempty"`  EndOpen [string](https://pkg.go.dev/builtin#string) `xml:"endopen,attr,omitempty"` }

NodeShape holds the visual representation of a node with associated dynamics.

type Nodes struct {
 Count [int](https://pkg.go.dev/builtin#int) `xml:"count,attr,omitempty"`  Nodes [][Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Node) `xml:"node,omitempty"` }

Nodes holds a collection of nodes constituting a graph or subgraph.

type Parent struct {
 For [string](https://pkg.go.dev/builtin#string) `xml:"for,attr"` }

Parent is a single parent relationship.

type Parents struct {
 Parents [][Parent](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Parent) `xml:"parent,omitempty"` }

Parents holds parent relationships between nodes in a hierarchical graph.

type Position struct {
 X [float64](https://pkg.go.dev/builtin#float64) `xml:"x,attr"`  Y [float64](https://pkg.go.dev/builtin#float64) `xml:"y,attr"`  Z [float64](https://pkg.go.dev/builtin#float64) `xml:"z,attr"`  Spells *[Spells](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Spells) `xml:"spells,omitempty"`  Start [string](https://pkg.go.dev/builtin#string) `xml:"start,attr,omitempty"`  StartOpen [string](https://pkg.go.dev/builtin#string) `xml:"startopen,attr,omitempty"`  End [string](https://pkg.go.dev/builtin#string) `xml:"end,attr,omitempty"`  EndOpen [string](https://pkg.go.dev/builtin#string) `xml:"endopen,attr,omitempty"` }

Position hold the spatial position of a node and its dynamics.

type Size struct {
 Value [float64](https://pkg.go.dev/builtin#float64) `xml:"value,attr"`  Spells *[Spells](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Spells) `xml:"http://www.gexf.net/1.2draft/viz spells,omitempty"`  Start [string](https://pkg.go.dev/builtin#string) `xml:"start,attr,omitempty"`  StartOpen [string](https://pkg.go.dev/builtin#string) `xml:"startopen,attr,omitempty"`  End [string](https://pkg.go.dev/builtin#string) `xml:"end,attr,omitempty"`  EndOpen [string](https://pkg.go.dev/builtin#string) `xml:"endopen,attr,omitempty"` }

Size hold the visual size of a node and its dynamics.

type Spell struct {
 Start [string](https://pkg.go.dev/builtin#string) `xml:"start,attr,omitempty"`  StartOpen [string](https://pkg.go.dev/builtin#string) `xml:"startopen,attr,omitempty"`  End [string](https://pkg.go.dev/builtin#string) `xml:"end,attr,omitempty"`  EndOpen [string](https://pkg.go.dev/builtin#string) `xml:"endopen,attr,omitempty"` }

Spell is a time interval.

type Spells struct {
 Spells [][Spell](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Spell) `xml:"spell"` }

Spells holds a collection of time dynamics for a graph entity.

type Thickness struct {
 Value [float64](https://pkg.go.dev/builtin#float64) `xml:"value,attr"`  Spells *[Spells](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/formats/gexf12#Spells) `xml:"http://www.gexf.net/1.2draft/viz spells,omitempty"`  Start [string](https://pkg.go.dev/builtin#string) `xml:"start,attr,omitempty"`  StartOpen [string](https://pkg.go.dev/builtin#string) `xml:"startopen,attr,omitempty"`  End [string](https://pkg.go.dev/builtin#string) `xml:"end,attr,omitempty"`  EndOpen [string](https://pkg.go.dev/builtin#string) `xml:"endopen,attr,omitempty"` }

Thickness hold the visual thickness of an edge and its dynamics.

*   The namespace for GEFX1.2 is 1.2draft, though it has already been deprecated. There is no specification for 1.3, although it is being used in the wild.
