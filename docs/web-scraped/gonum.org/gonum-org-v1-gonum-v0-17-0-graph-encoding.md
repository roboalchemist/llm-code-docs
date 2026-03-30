# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding

Title: encoding package - gonum.org/v1/gonum/graph/encoding - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding

Markdown Content:
1.   [Discover Packages](https://pkg.go.dev/)
2.   [gonum.org/v1/gonum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0)
3.   [graph](https://pkg.go.dev/gonum.org/v1/gonum/graph@v0.17.0)
4.   [encoding](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding)

package

*   [Documentation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#section-documentation)
    *   [Overview](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#pkg-overview)
    *   [Index](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#pkg-index)
    *   [Constants](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#pkg-constants)
    *   [Variables](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#pkg-variables)
    *   [Functions](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#pkg-functions)
    *   [Types](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#pkg-types)
        *   [type Attribute](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attribute "type Attribute")
        *   [type AttributeSetter](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#AttributeSetter "type AttributeSetter")
        *   [type Attributer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attributer "type Attributer")
        *   [type Attributes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attributes "type Attributes")
            *   [(a) Attributes()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attributes.Attributes "(a) Attributes()")
            *   [(a) SetAttribute(attr)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attributes.SetAttribute "(a) SetAttribute(attr)")

        *   [type Builder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Builder "type Builder")
        *   [type MultiBuilder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#MultiBuilder "type MultiBuilder")

*   [Source Files](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#section-sourcefiles)
*   [Directories](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#section-directories)

![Image 1](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#section-documentation "Go to Documentation")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Package encoding provides a common graph encoding API.

*   [type Attribute](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attribute)
*   [type AttributeSetter](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#AttributeSetter)
*   [type Attributer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attributer)
*   [type Attributes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attributes)
*       *   [func (a *Attributes) Attributes() []Attribute](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attributes.Attributes)
    *   [func (a *Attributes) SetAttribute(attr Attribute) error](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attributes.SetAttribute)

*   [type Builder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Builder)
*   [type MultiBuilder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#MultiBuilder)

This section is empty.

This section is empty.

This section is empty.

type Attribute struct {
 Key, Value [string](https://pkg.go.dev/builtin#string)}

Attribute is an encoded key value attribute pair use in graph encoding.

type AttributeSetter interface {
 SetAttribute([Attribute](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attribute)) [error](https://pkg.go.dev/builtin#error)}

AttributeSetter is implemented by types that can set an encoded graph attribute.

type Attributer interface {
 Attributes() [][Attribute](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attribute)}

Attributer defines graph.Node or graph.Edge values that can specify graph attributes.

type Attributes [][Attribute](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attribute)

Attributes is a helper type providing simple attribute handling.

func (a *[Attributes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attributes)) Attributes() [][Attribute](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attribute)

Attributes returns all of the receiver's attributes.

func (a *[Attributes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attributes)) SetAttribute(attr [Attribute](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#Attribute)) [error](https://pkg.go.dev/builtin#error)

SetAttribute sets attr in the receiver. Calling SetAttribute with an Attribute with a Key that is in the collection replaces the existing value and calling with an empty Value removes the attribute from the collection if it exists. SetAttribute always returns nil.

Builder is a graph that can have user-defined nodes and edges added.

MultiBuilder is a graph that can have user-defined nodes and edges added.

![Image 2](https://pkg.go.dev/static/shared/icon/folder_gm_grey_24dp.svg) Directories [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding#section-directories "Go to Directories")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| Path | Synopsis |
| --- | --- |
| [digraph6](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding/digraph6) Package digraph6 implements graphs specified by digraph6 strings. | Package digraph6 implements graphs specified by digraph6 strings. |
| [dot](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding/dot) Package dot implements GraphViz DOT marshaling and unmarshaling of graphs. | Package dot implements GraphViz DOT marshaling and unmarshaling of graphs. |
| [graph6](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding/graph6) Package graph6 implements graphs specified by graph6 strings. | Package graph6 implements graphs specified by graph6 strings. |
| [graphql](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/encoding/graphql) Package graphql implements JSON marshaling and unmarshaling of graph as used by GraphQL | Package graphql implements JSON marshaling and unmarshaling of graph as used by GraphQL |
