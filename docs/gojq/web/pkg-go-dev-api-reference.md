---
source: https://pkg.go.dev/github.com/itchyny/gojq
fetched: 2026-04-04
---

# gojq — pkg.go.dev API Reference

Package `gojq` is a pure Go implementation of [jq](https://github.com/jqlang/jq).

```go
import "github.com/itchyny/gojq"
```

## Overview

gojq is a pure Go implementation of the jq command-line JSON query language.
It can be used both as a standalone command and as a library that can be embedded
in Go applications.

### Key Features

- Pure Go implementation with no C dependencies
- Arbitrary-precision integer arithmetic
- Supports string indexing
- Improved date/time handling with nanosecond support
- YAML input/output support
- Context-aware execution with timeout support
- Custom function and iterator registration
- Module loading system

## Functions

### func Compare

```go
func Compare(l, r any) int
```

Compare compares two values for ordering. It returns -1, 0, or 1.
This is useful for implementing custom internal functions that need to compare values.

### func Marshal

```go
func Marshal(v any) ([]byte, error)
```

Marshal encodes a value to JSON in jq-flavored format.
This handles NaN and Infinity values that standard encoding/json cannot encode.

### func Parse

```go
func Parse(src string) (*Query, error)
```

Parse parses a jq query string and returns a Query AST node.
Returns a *ParseError on failure, which includes the offset and token.

#### Example (Parse)

```go
query, err := gojq.Parse(".foo | .bar")
if err != nil {
    log.Fatalln(err)
}
input := map[string]any{"foo": map[string]any{"bar": 42}}
iter := query.Run(input)
for {
    v, ok := iter.Next()
    if !ok {
        break
    }
    if err, ok := v.(error); ok {
        log.Fatalln(err)
    }
    fmt.Printf("%#v\n", v)
}
```

### func Preview

```go
func Preview(v any) string
```

Preview returns a short string representation of a value, suitable for error messages
in custom internal functions.

### func TypeOf

```go
func TypeOf(v any) string
```

TypeOf returns the jq type name of a value ("null", "boolean", "number", "string",
"array", or "object"). This is useful for implementing custom internal functions.

## Types

### type Array

```go
type Array struct {
    Query *Query
}
```

Array represents a jq array construction `[expr]`.

### type Code

```go
type Code struct {
    // contains filtered or unexported fields
}
```

Code is a compiled jq query. It can be reused against multiple inputs.

#### func Compile

```go
func Compile(q *Query, options ...CompilerOption) (*Code, error)
```

Compile compiles a query with compiler options.

#### Example (Variables)

```go
query, err := gojq.Parse("$x * 100 + $y, $z")
if err != nil {
    log.Fatalln(err)
}
code, err := gojq.Compile(
    query,
    gojq.WithVariables([]string{"$x", "$y", "$z"}),
)
if err != nil {
    log.Fatalln(err)
}
iter := code.Run(nil, 12, 42, 128)
for {
    v, ok := iter.Next()
    if !ok {
        break
    }
    if err, ok := v.(error); ok {
        log.Fatalln(err)
    }
    fmt.Printf("%v\n", v)
}
// Output:
// 1242
// 128
```

#### func (*Code) Run

```go
func (c *Code) Run(v any, values ...any) Iter
```

Run runs the compiled code with the given input value and variable values.
The variable values must be provided in the same order as WithVariables.

#### func (*Code) RunWithContext

```go
func (c *Code) RunWithContext(ctx context.Context, v any, values ...any) Iter
```

RunWithContext runs the compiled code with context for cancellation/timeout support.

#### Example (Context with Timeout)

```go
ctx, cancel := context.WithTimeout(context.Background(), 100*time.Millisecond)
defer cancel()
iter := code.RunWithContext(ctx, input)
```

### type CompilerOption

```go
type CompilerOption func(*compiler)
```

CompilerOption configures the compiler behavior.

#### func WithEnvironLoader

```go
func WithEnvironLoader(environLoader func() []string) CompilerOption
```

WithEnvironLoader allows to configure the environment variables referenced by
`env` and `$ENV`. By default, OS environment variables are not accessible
due to security reasons. You can use `gojq.WithEnvironLoader(os.Environ)` if
you want.

#### Example (WithEnvironLoader)

```go
code, err := gojq.Compile(
    query,
    gojq.WithEnvironLoader(func() []string {
        return []string{"foo=42", "bar=128"}
    }),
)
```

#### func WithFunction

```go
func WithFunction(name string, minarity, maxarity int,
    f func(any, []any) any) CompilerOption
```

WithFunction allows to add a custom internal function. An internal function can
return a single value (which can be an error) each invocation. To add a jq function
(which may include a comma operator to emit multiple values, `empty` function,
accept a filter for its argument, or call another built-in function), use
`LoadInitModules` of the module loader.

#### Example (WithFunction)

```go
code, err := gojq.Compile(
    query,
    gojq.WithFunction("double", 0, 0, func(x any, xs []any) any {
        if n, ok := x.(float64); ok {
            return n * 2
        }
        return fmt.Errorf("double requires a number")
    }),
)
```

#### func WithInputIter

```go
func WithInputIter(inputIter Iter) CompilerOption
```

WithInputIter allows to use `input` and `inputs` functions. By default,
these functions are disabled.

#### Example (WithInputIter)

```go
code, err := gojq.Compile(
    query,
    gojq.WithInputIter(gojq.NewIter(1, 2, 3, 4, 5)),
)
```

#### func WithIterFunction

```go
func WithIterFunction(name string, minarity, maxarity int,
    f func(any, []any) Iter) CompilerOption
```

WithIterFunction allows to add a custom iterator function. An iterator function
returns an iterator to emit multiple values. You cannot define both iterator and
non-iterator functions of the same name (with possibly different arities).
You can use `gojq.NewIter` to convert values or an error to a `gojq.Iter`.

#### Example (WithIterFunction)

```go
code, err := gojq.Compile(
    query,
    gojq.WithIterFunction("f", 2, 2, func(_ any, xs []any) gojq.Iter {
        if x, ok := xs[0].(int); ok {
            if y, ok := xs[1].(int); ok {
                return &rangeIter{x, y}
            }
        }
        return gojq.NewIter(fmt.Errorf("f cannot be applied"))
    }),
)
```

#### func WithModuleLoader

```go
func WithModuleLoader(moduleLoader ModuleLoader) CompilerOption
```

WithModuleLoader allows to load modules. By default, the module feature is
disabled. If you want to load modules from the file system, use
`gojq.NewModuleLoader`.

#### Example (WithModuleLoader)

```go
query, err := gojq.Parse(`import "module1" as m; m::g`)
code, err := gojq.Compile(
    query,
    gojq.WithModuleLoader(&customModuleLoader{}),
)
```

#### func WithVariables

```go
func WithVariables(variables []string) CompilerOption
```

WithVariables allows to configure the variables which can be used in the query.
Pass the values of the variables to `code.Run` in the same order.

### type ConstArray

```go
type ConstArray struct {
    Elems []*ConstTerm
}
```

ConstArray represents a constant array in module metadata.

### type ConstObject

```go
type ConstObject struct {
    KeyVals []*ConstObjectKeyVal
}
```

ConstObject represents a constant object in module metadata.

#### func (*ConstObject) ToValue

```go
func (e *ConstObject) ToValue() map[string]any
```

ToValue converts a ConstObject to a Go map.

### type ConstObjectKeyVal

```go
type ConstObjectKeyVal struct {
    Key       string
    KeyString string
    Val       *ConstTerm
}
```

ConstObjectKeyVal represents a key-value pair in a constant object.

### type ConstTerm

```go
type ConstTerm struct {
    Object *ConstObject
    Array  *ConstArray
    Number string
    Str    string
    Null   bool
    True   bool
    False  bool
}
```

ConstTerm represents a constant term in module metadata.

### type Foreach

```go
type Foreach struct {
    Query   *Query
    Pattern *Pattern
    Start   *Query
    Update  *Query
    Extract *Query
}
```

Foreach represents a `foreach` expression.

### type Func

```go
type Func struct {
    Name string
    Args []*Query
}
```

Func represents a function call.

### type FuncDef

```go
type FuncDef struct {
    Name string
    Args []string
    Body *Query
}
```

FuncDef represents a function definition (`def name(args): body;`).

### type HaltError

```go
type HaltError exitCodeError
```

HaltError is the error type returned by `halt` and `halt_error` functions.
Use this to detect halt errors and stop outer iteration.

#### func (*HaltError) Error

```go
func (err *HaltError) Error() string
```

Error returns the error message.

#### func (*HaltError) ExitCode

```go
func (err *HaltError) ExitCode() int
```

ExitCode returns the exit code of the halt error.

#### func (*HaltError) Value

```go
func (err *HaltError) Value() any
```

Value returns the value passed to `halt_error`. If the value is nil,
the halt was requested by the `halt` function (without an error value),
and the iteration should stop without reporting an error.

### type If

```go
type If struct {
    Cond *Query
    Then *Query
    Elif []*IfElif
    Else *Query
}
```

If represents an `if-then-elif-else-end` expression.

### type IfElif

```go
type IfElif struct {
    Cond *Query
    Then *Query
}
```

IfElif represents an `elif` clause.

### type Import

```go
type Import struct {
    ImportPath  string
    ImportAlias string
    IncludePath string
    Meta        *ConstObject
}
```

Import represents an `import` or `include` statement.

### type Index

```go
type Index struct {
    Name    string
    Str     *String
    Start   *Query
    End     *Query
    IsSlice bool
}
```

Index represents an index operation (`.foo`, `.[0]`, `.[2:4]`).

### type Iter

```go
type Iter interface {
    Next() (any, bool)
}
```

Iter is the interface for iterating over query results.
`Next()` returns the next value and true, or (nil, false) when iteration is done.
The returned value may be an error.

#### func NewIter

```go
func NewIter[T any](values ...T) Iter
```

NewIter creates a new iterator from values. This is a generic function.
You can pass values of any type including errors.

### type Label

```go
type Label struct {
    Ident string
    Body  *Query
}
```

Label represents a `label $ident | body` expression.

### type ModuleLoader

```go
type ModuleLoader any
```

ModuleLoader is the interface for loading modules. All methods are optional.
Implement the methods you need:

```go
LoadInitModules() ([]*Query, error)
LoadModule(string) (*Query, error)
LoadModuleWithMeta(string, map[string]any) (*Query, error)
LoadJSON(string) (any, error)
LoadJSONWithMeta(string, map[string]any) (any, error)
```

#### func NewModuleLoader

```go
func NewModuleLoader(paths []string) ModuleLoader
```

NewModuleLoader creates a new module loader that loads modules from the given
file system paths.

### type Object

```go
type Object struct {
    KeyVals []*ObjectKeyVal
}
```

Object represents a jq object construction `{key: value, ...}`.

### type ObjectKeyVal

```go
type ObjectKeyVal struct {
    Key       string
    KeyString *String
    KeyQuery  *Query
    Val       *Query
}
```

ObjectKeyVal represents a key-value pair in an object construction.

### type Operator

```go
type Operator int
```

Operator represents a binary or unary operator.

```go
const (
    OpPipe Operator = iota + 1
    OpComma
    OpAdd
    OpSub
    OpMul
    OpDiv
    OpMod
    OpEq
    OpNe
    OpGt
    OpLt
    OpGe
    OpLe
    OpAnd
    OpOr
    OpAlt
    OpAssign
    OpModify
    OpUpdateAdd
    OpUpdateSub
    OpUpdateMul
    OpUpdateDiv
    OpUpdateMod
    OpUpdateAlt
)
```

#### func (Operator) GoString

```go
func (op Operator) GoString() string
```

GoString returns the Go representation of the operator (for `%#v` formatting).

#### func (Operator) String

```go
func (op Operator) String() string
```

String returns the string representation of the operator (e.g., `|`, `,`, `+`).

### type ParseError

```go
type ParseError struct {
    Offset int
    Token  string
}
```

ParseError is the error type returned by Parse on failure.
It provides the offset and token where the parse error occurred.

#### func (*ParseError) Error

```go
func (err *ParseError) Error() string
```

Error returns the error message including the offset and unexpected token.

### type Pattern

```go
type Pattern struct {
    Name   string
    Array  []*Pattern
    Object []*PatternObject
}
```

Pattern represents a binding pattern (variable, array destructuring, or object destructuring).

### type PatternObject

```go
type PatternObject struct {
    Key       string
    KeyString *String
    KeyQuery  *Query
    Val       *Pattern
}
```

PatternObject represents a key-pattern pair in an object destructuring pattern.

### type Query

```go
type Query struct {
    Meta     *ConstObject
    Imports  []*Import
    FuncDefs []*FuncDef
    Term     *Term
    Left     *Query
    Right    *Query
    Patterns []*Pattern
    Op       Operator
}
```

Query represents a parsed jq query. This is the top-level AST node.

#### func (*Query) Run

```go
func (e *Query) Run(v any) Iter
```

Run runs the query on the given input value and returns an iterator over results.
The input value should be `[]any` for arrays and `map[string]any` for objects
(matching the types produced by `encoding/json` unmarshaling).

#### func (*Query) RunWithContext

```go
func (e *Query) RunWithContext(ctx context.Context, v any) Iter
```

RunWithContext runs the query with context support for cancellation and timeouts.

#### func (*Query) String

```go
func (e *Query) String() string
```

String returns the string representation of the query.

### type Reduce

```go
type Reduce struct {
    Query   *Query
    Pattern *Pattern
    Start   *Query
    Update  *Query
}
```

Reduce represents a `reduce` expression.

### type String

```go
type String struct {
    Str     string
    Queries []*Query
}
```

String represents a jq string, possibly with interpolations.

### type Suffix

```go
type Suffix struct {
    Index    *Index
    Iter     bool
    Optional bool
}
```

Suffix represents a suffix operation (indexing, iteration `[]`, or optional `?`).

### type Term

```go
type Term struct {
    Type       TermType
    Index      *Index
    Func       *Func
    Object     *Object
    Array      *Array
    Number     string
    Unary      *Unary
    Format     string
    Str        *String
    If         *If
    Try        *Try
    Reduce     *Reduce
    Foreach    *Foreach
    Label      *Label
    Break      string
    Query      *Query
    SuffixList []*Suffix
}
```

Term represents a term in the jq AST (the fundamental unit of a jq expression).

#### func (*Term) String

```go
func (e *Term) String() string
```

String returns the string representation of the term.

### type TermType

```go
type TermType int
```

TermType represents the type of a Term node.

```go
const (
    TermTypeIdentity TermType = iota + 1
    TermTypeRecurse
    TermTypeNull
    TermTypeTrue
    TermTypeFalse
    TermTypeIndex
    TermTypeFunc
    TermTypeObject
    TermTypeArray
    TermTypeNumber
    TermTypeUnary
    TermTypeFormat
    TermTypeString
    TermTypeIf
    TermTypeTry
    TermTypeReduce
    TermTypeForeach
    TermTypeLabel
    TermTypeBreak
    TermTypeQuery
)
```

#### func (TermType) GoString

```go
func (termType TermType) GoString() string
```

GoString returns the Go representation of the term type.

#### func (TermType) String

```go
func (termType TermType) String() string
```

String returns the string representation of the term type.

### type Try

```go
type Try struct {
    Body  *Query
    Catch *Query
}
```

Try represents a `try-catch` expression.

### type Unary

```go
type Unary struct {
    Op   Operator
    Term *Term
}
```

Unary represents a unary expression (`+x` or `-x`).

### type ValueError

```go
type ValueError interface {
    error
    Value() any
}
```

ValueError is an interface for errors with associated values. Custom internal
functions can return errors implementing this interface. `HaltError` implements
this interface.

## Differences from jq

- Does not preserve object key order (sorted by default)
- No `keys_unsorted` function or `--sort-keys` option
- Supports arbitrary-precision integer calculation
- Supports string indexing (`"abcde"[2]`)
- Improved time formatting with `%f` and timezone support
- Supports nanoseconds in date and time functions
- Does not support `NaN`, `Infinity` JSON extensions
- Does not support some regex features (backreferences, look-around assertions)
- Supports YAML input/output
- Default security model: environment variables not accessible unless
  explicitly enabled via `WithEnvironLoader`
