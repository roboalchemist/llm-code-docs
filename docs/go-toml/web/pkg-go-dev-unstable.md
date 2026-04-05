# Package unstable - go-toml v2

Source: https://pkg.go.dev/github.com/pelletier/go-toml/v2/unstable

## Overview

Package `unstable` provides APIs that do not meet the backward compatibility guarantees yet. It is part of the `github.com/pelletier/go-toml/v2` module.

**Import:**
```go
import "github.com/pelletier/go-toml/v2/unstable"
```

**License:** MIT

---

## Functions

### func NewParserError

```go
func NewParserError(highlight []byte, format string, args ...interface{}) error
```

`NewParserError` is a convenience function to create a `ParserError`.

**Warning:** Highlight needs to be a subslice of `Parser.data`, so only slices returned by `Parser.Raw` are valid candidates.

---

## Types

### type Iterator

```go
type Iterator struct {
	// contains filtered or unexported fields
}
```

`Iterator` over a sequence of nodes.

Starts uninitialized, you need to call `Next()` first.

**Example usage:**
```go
it := n.Children()
for it.Next() {
	n := it.Node()
	// do something with n
}
```

#### func (*Iterator) IsLast

```go
func (c *Iterator) IsLast() bool
```

`IsLast` returns true if the current node of the iterator is the last one. Subsequent calls to `Next()` will return false.

#### func (*Iterator) Next

```go
func (c *Iterator) Next() bool
```

`Next` moves the iterator forward and returns true if points to a node, false otherwise.

#### func (*Iterator) Node

```go
func (c *Iterator) Node() *Node
```

`Node` returns a pointer to the node pointed at by the iterator.

---

### type Kind

```go
type Kind int
```

`Kind` represents the type of TOML structure contained in a given Node.

**Constants:**
```go
const (
	// Invalid represents an invalid meta node.
	Invalid Kind = iota
	// Comment represents a comment meta node.
	Comment
	// Key represents a key meta node.
	Key

	// Table represents a top-level table.
	Table
	// ArrayTable represents a top-level array table.
	ArrayTable
	// KeyValue represents a top-level key value.
	KeyValue

	// Array represents an array container value.
	Array
	// InlineTable represents an inline table container value.
	InlineTable

	// String represents a string value.
	String
	// Bool represents a boolean value.
	Bool
	// Float represents a floating point value.
	Float
	// Integer represents an integer value.
	Integer
	// LocalDate represents a local date value.
	LocalDate
	// LocalTime represents a local time value.
	LocalTime
	// LocalDateTime represents a local date/time value.
	LocalDateTime
	// DateTime represents a date/time value.
	DateTime
)
```

#### func (Kind) String

```go
func (k Kind) String() string
```

`String` implementation of `fmt.Stringer`.

---

### type Node

```go
type Node struct {
	Kind Kind
	Raw  Range      // Raw bytes from the input.
	Data []byte     // Node value (either allocated or referencing the input).
	// contains filtered or unexported fields
}
```

`Node` in a TOML expression AST.

Depending on Kind, its sequence of children should be interpreted differently:

- **Array:** have one child per element in the array.
- **InlineTable:** have one child per key-value in the table (each of kind InlineTable).
- **KeyValue:** have at least two children. The first one is the value. The rest make a potentially dotted key.
- **Table and ArrayTable:** children represent a dotted key (same as KeyValue, but without the first node being the value).

When relevant, `Raw` describes the range of bytes this node is referring to in the input document. Use `Parser.Raw()` to retrieve the actual bytes.

#### func (*Node) Child

```go
func (n *Node) Child() *Node
```

`Child` returns a pointer to the first child node of this node. Other children can be accessed calling `Next` on the first child. Returns nil if this Node has no child.

#### func (*Node) Children

```go
func (n *Node) Children() Iterator
```

`Children` returns an iterator over a node's children.

#### func (*Node) Key

```go
func (n *Node) Key() Iterator
```

`Key` returns the children nodes making the Key on a supported node. Panics otherwise. They are guaranteed to be all be of the Kind Key. A simple key would return just one element.

#### func (*Node) Next

```go
func (n *Node) Next() *Node
```

`Next` returns a pointer to the next node, or nil if there is no next node.

#### func (*Node) Valid

```go
func (n *Node) Valid() bool
```

`Valid` returns true if the node's kind is set (not to Invalid).

#### func (*Node) Value

```go
func (n *Node) Value() *Node
```

`Value` returns a pointer to the value node of a KeyValue. Guaranteed to be non-nil. Panics if not called on a KeyValue node, or if the Children are malformed.

---

### type Parser

```go
type Parser struct {
	KeepComments bool
	// contains filtered or unexported fields
}
```

`Parser` scans over a TOML-encoded document and generates an iterative AST.

To prime the Parser, first reset it with the contents of a TOML document. Then, process all top-level expressions sequentially.

**Important notes:**
- Don't forget to check `Error()` after you're done parsing.
- Each top-level expression needs to be fully processed before calling `NextExpression()` again. Otherwise, calls to various Node methods may panic if the parser has moved on the next expression.
- For performance reasons, go-toml doesn't make a copy of the input bytes to the parser. Make sure to copy all the bytes you need to outlive the slice given to the parser.

#### Example: Basic Parsing

```go
doc := `
	hello = "world"
	value = 42
	`
p := Parser{}
p.Reset([]byte(doc))
for p.NextExpression() {
	e := p.Expression()
	fmt.Printf("Expression: %s\n", e.Kind)
	value := e.Value()
	it := e.Key()
	k := it.Node() // shortcut: we know there is no dotted key in the example
	fmt.Printf("%s -> (%s) %s\n", k.Data, value.Kind, value.Data)
}

// Output:
// Expression: KeyValue
// hello -> (String) world
// Expression: KeyValue
// value -> (Integer) 42
```

#### func (*Parser) Data

```go
func (p *Parser) Data() []byte
```

`Data` returns the slice provided to the last call to `Reset`.

#### func (*Parser) Error

```go
func (p *Parser) Error() error
```

`Error` returns any error that has occurred during parsing.

#### func (*Parser) Expression

```go
func (p *Parser) Expression() *Node
```

`Expression` returns a pointer to the node representing the last successfully parsed expression.

#### func (*Parser) NextExpression

```go
func (p *Parser) NextExpression() bool
```

`NextExpression` parses the next top-level expression. If an expression was successfully parsed, it returns true. If the parser is at the end of the document or an error occurred, it returns false.

Retrieve the parsed expression with `Expression()`.

#### func (*Parser) Range

```go
func (p *Parser) Range(b []byte) Range
```

`Range` returns a range description that corresponds to a given slice of the input. If the argument is not a subslice of the parser input, this function panics.

#### func (*Parser) Raw

```go
func (p *Parser) Raw(raw Range) []byte
```

`Raw` returns the slice corresponding to the bytes in the given range.

#### func (*Parser) Reset

```go
func (p *Parser) Reset(b []byte)
```

`Reset` brings the parser to its initial state for a given input. It wipes and reuses internal storage to reduce allocation.

#### func (*Parser) Shape

```go
func (p *Parser) Shape(r Range) Shape
```

`Shape` returns the shape of the given range in the input. Will panic if the range is not a subslice of the input.

*Added in v2.0.8*

---

### type ParserError

```go
type ParserError struct {
	Highlight []byte
	Message   string
	Key       []string // optional
}
```

`ParserError` describes an error relative to the content of the document.

**Warning:** It cannot outlive the instance of Parser it refers to, and may cause panics if the parser is reset.

#### func (*ParserError) Error

```go
func (e *ParserError) Error() string
```

`Error` is the implementation of the error interface.

---

### type Position

```go
type Position struct {
	// Number of bytes from the beginning of the input.
	Offset int
	// Line number, starting at 1.
	Line int
	// Column number, starting at 1.
	Column int
}
```

`Position` describes a position in the input.

*Added in v2.0.8*

---

### type Range

```go
type Range struct {
	Offset uint32
	Length uint32
}
```

`Range` of bytes in the document.

---

### type RawMessage

```go
type RawMessage []byte
```

`RawMessage` is a raw encoded TOML value. It implements `Unmarshaler` and can be used to delay TOML decoding or capture raw content.

*Added in v2.3.0*

**Example usage:**
```go
type Config struct {
    Plugin RawMessage `toml:"plugin"`
}

var cfg Config
toml.NewDecoder(r).EnableUnmarshalerInterface().Decode(&cfg)
// cfg.Plugin now contains the raw TOML bytes for [plugin]
```

#### func (*RawMessage) UnmarshalTOML

```go
func (m *RawMessage) UnmarshalTOML(data []byte) error
```

`UnmarshalTOML` implements `Unmarshaler`.

*Added in v2.3.0*

---

### type Shape

```go
type Shape struct {
	Start Position
	End   Position
}
```

`Shape` describes the position of a range in the input.

*Added in v2.0.8*

---

### type Unmarshaler

```go
type Unmarshaler interface {
	UnmarshalTOML(data []byte) error
}
```

`Unmarshaler` is implemented by types that can unmarshal a TOML description of themselves. The input is a valid TOML document containing the relevant portion of the parsed document.

For tables (including split tables defined in multiple places), the data contains the raw key-value bytes from the original document with adjusted table headers to be relative to the unmarshaling target.

*Added in v2.2.0*

---

## Source Files

- `ast.go`
- `builder.go`
- `doc.go`
- `kind.go`
- `parser.go`
- `scanner.go`
- `unmarshaler.go`
