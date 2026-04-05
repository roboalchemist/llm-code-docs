# gojq - pkg.go.dev API Reference

Package gojq is a pure Go implementation of jq.

- **Repository**: [github.com/itchyny/gojq](https://github.com/itchyny/gojq)
- **Module**: github.com/itchyny/gojq
- **Version**: v0.12.19
- **License**: MIT
- **Imports**: 26 packages
- **Imported by**: 615 packages

## Overview

You can embed gojq as a library to your Go products.

## Installation

```bash
go install github.com/itchyny/gojq/cmd/gojq@latest
```

## Core Functions

### Parse

```go
func Parse(src string) (*Query, error)
```

Parse parses a jq query string and returns a `*Query`. On failure, returns a `*ParseError` with offset and token information.

### Compile

```go
func Compile(q *Query, options ...CompilerOption) (*Code, error)
```

Compile compiles a query for reuse across multiple inputs. Accepts compiler options for customization.

### Compare

```go
func Compare(l, r any) int
```

Compare performs jq-flavored comparison of two values. Returns -1, 0, or 1.

### Marshal

```go
func Marshal(v any) ([]byte, error)
```

Marshal performs jq-flavored JSON encoding of a value.

### Preview

```go
func Preview(v any) string
```

Preview returns a truncated preview string of a value.

### TypeOf

```go
func TypeOf(v any) string
```

TypeOf returns the jq type name of a value (e.g., "null", "boolean", "number", "string", "array", "object").

## Types

### Query

```go
type Query struct {
    // Abstract syntax tree of a jq query
}
```

Query represents the parsed abstract syntax tree of a jq query.

#### Methods

```go
func (q *Query) Run(v any) Iter
```

Run runs the query against the input value and returns an iterator of results.

```go
func (q *Query) RunWithContext(ctx context.Context, v any) Iter
```

RunWithContext runs the query with a context for cancellation and timeout support.

### Code

```go
type Code struct {
    // Compiled query code
}
```

Code represents a compiled query that can be reused across multiple inputs.

#### Code Methods

```go
func (c *Code) Run(v any, values ...any) Iter
```

Run runs the compiled code against the input value. Additional values correspond to variables defined with `WithVariables`.

```go
func (c *Code) RunWithContext(ctx context.Context, v any, values ...any) Iter
```

RunWithContext runs the compiled code with a context for cancellation and timeout support.

### Iter

```go
type Iter interface {
    Next() (any, bool)
}
```

Iter is the interface for iterating over query results. The `Next` method returns the next value and a boolean indicating whether a value was available. When the boolean is false, iteration is complete.

The iterator can emit errors (as values of type `error`), so make sure to handle them. The return type is not `(any, error)` because the iterator may emit multiple errors.

#### NewIter

```go
func NewIter[T any](values ...T) Iter
```

NewIter creates an iterator from the given values. Values may include errors.

### CompilerOption

```go
type CompilerOption func(*compiler)
```

CompilerOption configures the compiler behavior.

#### WithVariables

```go
func WithVariables(variables []string) CompilerOption
```

WithVariables configures variables which can be used in the query. Pass the values of the variables to `code.Run` in the same order.

Example:

```go
code, err := gojq.Compile(
    query,
    gojq.WithVariables([]string{"$x", "$y", "$z"}),
)
iter := code.Run(nil, 12, 42, 128)
```

#### WithFunction

```go
func WithFunction(name string, minarity, maxarity int, f func(any, []any) any) CompilerOption
```

WithFunction adds a custom internal function. An internal function can return a single value (which can be an error) each invocation.

Example:

```go
code, err := gojq.Compile(
    query,
    gojq.WithFunction("f", 0, 1, func(x any, xs []any) any {
        // Custom function implementation
        return result
    }),
)
```

#### WithIterFunction

```go
func WithIterFunction(name string, minarity, maxarity int, f func(any, []any) Iter) CompilerOption
```

WithIterFunction adds a custom iterator function. An iterator function returns an iterator to emit multiple values. You cannot define both iterator and non-iterator functions of the same name (with possibly different arities).

Example:

```go
code, err := gojq.Compile(
    query,
    gojq.WithIterFunction("f", 2, 2, func(_ any, xs []any) gojq.Iter {
        return gojq.NewIter(val1, val2, val3)
    }),
)
```

#### WithModuleLoader

```go
func WithModuleLoader(loader ModuleLoader) CompilerOption
```

WithModuleLoader allows to load modules. By default, the module feature is disabled. If you want to load modules from the file system, use `NewModuleLoader`.

Example:

```go
code, err := gojq.Compile(
    query,
    gojq.WithModuleLoader(gojq.NewModuleLoader([]string{"./modules"})),
)
```

#### WithEnvironLoader

```go
func WithEnvironLoader(environLoader func() []string) CompilerOption
```

WithEnvironLoader configures the environment variables referenced by `env` and `$ENV`. By default, OS environment variables are not accessible due to security reasons.

Example:

```go
code, err := gojq.Compile(
    query,
    gojq.WithEnvironLoader(os.Environ),
)
```

#### WithInputIter

```go
func WithInputIter(inputIter Iter) CompilerOption
```

WithInputIter allows to use `input` and `inputs` functions. By default, these functions are disabled.

Example:

```go
code, err := gojq.Compile(
    query,
    gojq.WithInputIter(gojq.NewIter(1, 2, 3, 4, 5)),
)
```

### ModuleLoader

```go
type ModuleLoader interface {
    LoadInitModules() ([]*Query, error)
    LoadModule(string) (*Query, error)
    LoadModuleWithMeta(string, map[string]any) (*Query, error)
    LoadJSON(string) (any, error)
    LoadJSONWithMeta(string, map[string]any) (any, error)
}
```

ModuleLoader is the interface for loading modules. All methods are optional; implement only what you need. Modules can be loaded from the filesystem or custom sources.

#### NewModuleLoader

```go
func NewModuleLoader(paths []string) ModuleLoader
```

NewModuleLoader creates a module loader that loads modules from the given filesystem paths.

### Error Types

#### ParseError

```go
type ParseError struct {
    Offset int    // bytes read when error occurred
    Token  string // token that caused error
}

func (err *ParseError) Error() string
```

ParseError is returned by `Parse` when the query string is invalid. Contains the byte offset and the problematic token.

#### HaltError

```go
type HaltError struct {
    // ...
}

func (err *HaltError) Error() string
func (err *HaltError) ExitCode() int
func (err *HaltError) Value() any
```

HaltError is emitted by `halt` and `halt_error` functions. If `Value()` returns nil, discard the error and stop iteration without reporting it.

#### ValueError

```go
type ValueError interface {
    error
    Value() any
}
```

ValueError is the interface for errors with associated values, used by try-catch and custom functions. `HaltError` implements this interface.

### Query AST Types

#### Term

```go
type Term struct {
    Type TermType
    // ...
}
```

Term represents a single query term (identity, recurse, literals, functions, etc.).

#### TermType

```go
type TermType int

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

#### Operator

```go
type Operator int

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
    OpNot
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

Operator represents binary operators (pipe, comma, arithmetic, comparison, logical, assignment).

#### ConstTerm

Represents constant values (null, true, false, numbers, strings).

#### ConstArray

Represents constant array literals.

#### ConstObject / ConstObjectKeyVal

Represents constant object literals and their key-value pairs.

#### If / IfElif

Represents conditional expressions (`if-then-elif-else-end`).

#### Try

Represents error handling with catch (`try-catch`).

#### Reduce

Represents reduction operations (`reduce .[] as $x (init; update)`).

#### Foreach

Represents iteration with state (`foreach .[] as $x (init; update; extract)`).

#### Label / Break

Represents loop control (`label $name | ...` and `break $name`).

#### Array

Represents array construction (`[expr]`).

#### Object / ObjectKeyVal

Represents object construction (`{key: value}`).

#### String

Represents string interpolation (`"text \(expr) text"`).

#### Index

Represents array/object indexing and slicing (`.foo`, `.[0]`, `.[2:4]`).

#### Func

Represents function calls (`.`, `length`, `map(f)`, etc.).

#### FuncDef

Represents function definitions (`def name(args): body;`).

#### Pattern / PatternObject

Represents destructuring patterns used in `as` patterns.

#### Import

Represents import/include declarations for modules.

#### Suffix

Represents optional operator (`?`) and other suffixes.

#### Unary

Represents unary operators (positive `+`, negative `-`).

## Input Type Constraints

When using gojq as a library:

- Input must be `[]any` for arrays or `map[string]any` for objects
- Custom types must be marshaled to JSON first, then unmarshaled to `any`
- You cannot use `[]int` or `map[string]string` directly
- Number types accepted: `int`, `float64`, `*big.Int`, `json.Number`

## Complete Type Index

- `Array`
- `Code`
- `CompilerOption`
- `ConstArray`
- `ConstObject`
- `ConstObjectKeyVal`
- `ConstTerm`
- `Foreach`
- `Func`
- `FuncDef`
- `HaltError`
- `If`
- `IfElif`
- `Import`
- `Index`
- `Iter`
- `Label`
- `ModuleLoader`
- `Object`
- `ObjectKeyVal`
- `Operator`
- `ParseError`
- `Pattern`
- `PatternObject`
- `Query`
- `Reduce`
- `String`
- `Suffix`
- `Term`
- `TermType`
- `Try`
- `Unary`
- `ValueError`
