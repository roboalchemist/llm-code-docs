### Overview ¶

Package parse implements the elvish parser.

The parser builds a hybrid of AST (abstract syntax tree) and parse tree
(a.k.a. concrete syntax tree). The AST part only includes parts that are
semantically significant -- i.e. skipping whitespaces and symbols that do not
alter the semantics, and is embodied in the fields of each *Node type. The
parse tree part corresponds to all the text in the original source text, and
is embodied in the children of each*Node type.

### Index ¶

-
        func IsInlineWhitespace(r rune) bool

-
        func IsWhitespace(r rune) bool

-
        func ParseAs(src Source, n Node, w io.Writer) error

-
        func Quote(s string) string

-
        func QuoteVariableName(s string) string

-
        func SourceText(n Node) string

-
        func ValidLHSVariable(p *Primary, allowSigil bool) bool

-
          type Array

-

-
            func (n *Array) Range() diag.Ranging

-
          type Assignment

-

-
            func (n *Assignment) Range() diag.Ranging

-
          type Chunk

-

-
            func (n *Chunk) Range() diag.Ranging

-
          type Compound

-

-
            func (n *Compound) Range() diag.Ranging

-
          type Error

-

-
            func GetError(e error) *Error

-

-
            func (er *Error) Error() string

-
            func (er *Error) Show(indent string) string

-
          type ExprCtx

-

-
            func (i ExprCtx) String() string

-
          type Form

-

-
            func (n *Form) Range() diag.Ranging

-
          type Indexing

-

-
            func (n *Indexing) Range() diag.Ranging

-
          type MapPair

-

-
            func (n *MapPair) Range() diag.Ranging

-
          type Node

-

-
            func Children(n Node) []Node

-
            func Parent(n Node) Node

-
          type Pipeline

-

-
            func (n *Pipeline) Range() diag.Ranging

-
          type Primary

-

-
            func (n *Primary) Range() diag.Ranging

-
          type PrimaryType

-

-
            func QuoteAs(s string, q PrimaryType) (string, PrimaryType)

-

-
            func (i PrimaryType) String() string

-
          type Redir

-

-
            func (n *Redir) Range() diag.Ranging

-
          type RedirMode

-

-
            func (i RedirMode) String() string

-
          type Sep

-

-
            func NewSep(src string, begin, end int) *Sep

-

-
            func (n *Sep) Range() diag.Ranging

-
          type Source

-

-
            func SourceForTest(code string) Source

-

-
            func (src Source) IsStructMap()

-
            func (src Source) Repr(int) string

-
          type Tree

-

-
            func Parse(src Source) (Tree, error)

-
            func ParseWithDeprecation(src Source, w io.Writer) (Tree, error)

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

####

      func IsInlineWhitespace ¶
  
    
  

    
    
      

```
func IsInlineWhitespace(r rune) bool
```

IsInlineWhitespace reports whether r is an inline whitespace character.
Currently this includes space (Unicode 0x20) and tab (Unicode 0x9).

####

      func IsWhitespace ¶
  
    
  

    
    
      

```
func IsWhitespace(r rune) bool
```

IsWhitespace reports whether r is a whitespace. Currently this includes
inline whitespace characters and newline (Unicode 0xa).

####

      func ParseAs ¶
  
    
      added in
      v0.14.0
    
  

    
    
      

```
func ParseAs(src Source, n Node, w io.Writer) error
```

ParseAs parses the given source as a node, depending on the dynamic type of
n, writing deprecation warnings to the given io.Writer if it is not nil. If
the error is not nil, it always has type *Error.

####

      func Quote ¶
  
    
  

    
    
      

```
func Quote(s string) string
```

Quote returns a valid Elvish expression that evaluates to the given string.
If s is a valid bareword, it is returned as is; otherwise it is quoted,
preferring the use of single quotes.

####

      func QuoteVariableName ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func QuoteVariableName(s string) string
```

QuoteVariableName is like Quote, but quotes s if it contains any character
that may not appear unquoted in variable names.

####

      func SourceText ¶
  
    
      added in
      v0.14.0
    
  

    
    
      

```
func SourceText(n Node) string
```

SourceText returns the part of the source text that parses to the node.

####

      func ValidLHSVariable ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func ValidLHSVariable(p *Primary, allowSigil bool) bool
```
