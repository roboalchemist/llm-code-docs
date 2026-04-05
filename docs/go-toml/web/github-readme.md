# go-toml v2 README

Source: <https://github.com/pelletier/go-toml>

go-toml v2 is a Go library for parsing and generating TOML (Tom's Obvious, Minimal Language) files. It fully supports TOML v1.0.0.

## Documentation

Complete API documentation and examples are available at [pkg.go.dev](https://pkg.go.dev/github.com/pelletier/go-toml/v2).

## Key Features

**Standards-aligned behavior**: The library emulates Go's standard `encoding/json` package design patterns.

**Performance-focused**: While prioritizing usability, the implementation emphasizes efficient operations. Benchmarks show 2-6x speedups compared to other Go TOML libraries across common scenarios.

**Strict mode**: Decoders can flag unknown fields, helping catch typos in configuration files.

**Detailed error messages**: Parse errors include line/column context showing exactly where problems occur.

**Local date/time support**: Native types (`LocalDate`, `LocalTime`, `LocalDateTime`) represent TOML's timezone-independent temporal values.

**Annotated output**: When marshaling, you can include comments and commented-out configuration examples.

## Getting Started

### Basic Usage

```go
import "github.com/pelletier/go-toml/v2"

type Config struct {
    Version int
    Name string
    Tags []string
}

doc := `version = 2
name = "go-toml"
tags = ["go", "toml"]`

var cfg Config
err := toml.Unmarshal([]byte(doc), &cfg)
```

### Unmarshaling with Nested Structures

```go
doc := `age = 45
fruits = ["apple", "pear"]

[my-variables]
first = 1
second = 0.2
third = "abc"

[my-variables.b]
bfirst = 123`

var Document struct {
    Age int
    Fruits []string
    Myvariables struct {
        First int
        Second float64
        Third string
        B struct {
            Bfirst int
        }
    } `toml:"my-variables"`
}

err := toml.Unmarshal([]byte(doc), &Document)
```

### Marshaling to TOML

```go
cfg := MyConfig{
    Version: 2,
    Name: "go-toml",
    Tags: []string{"go", "toml"},
}

b, err := toml.Marshal(cfg)
fmt.Println(string(b))
// Output:
// Version = 2
// Name = 'go-toml'
// Tags = ['go', 'toml']
```

## Unstable API

The `unstable` package provides experimental features not yet guaranteed stable:

**Parser**: Enables iterative AST-level parsing of TOML documents. See [pkg.go.dev/github.com/pelletier/go-toml/v2/unstable](https://pkg.go.dev/github.com/pelletier/go-toml/v2/unstable).

## Performance Benchmarks

Speed improvements over alternatives (execution time):

| Benchmark | vs go-toml v1 | vs BurntSushi/toml |
|-----------|---------------|-------------------|
| Marshal/HugoFrontMatter | 2.1x | 2.0x |
| Unmarshal/ReferenceFile/struct | 4.8x | 5.0x |
| Unmarshal/SimpleDocument/struct | 5.9x | 4.4x |

Complete benchmark results available via `./ci.sh benchmark -a -html`.

## Module Installation

Go 1.16+: Simply import the package -- `go` handles dependency resolution automatically.

Go 1.13+: `GO111MODULE=on go get github.com/pelletier/go-toml/v2`

## Command-line Tools

Three utilities are available:

**tomljson**: Converts TOML to JSON

```bash
go install github.com/pelletier/go-toml/v2/cmd/tomljson@latest
tomljson --help
```

**jsontoml**: Converts JSON to TOML

```bash
go install github.com/pelletier/go-toml/v2/cmd/jsontoml@latest
jsontoml --help
```

**tomll**: Lints and reformats TOML

```bash
go install github.com/pelletier/go-toml/v2/cmd/tomll@latest
tomll --help
```

Docker images containing these tools are available at `ghcr.io/pelletier/go-toml:v2`.

## Migration from v1

### Decoding Changes

**Field name matching**: V2 uses case-insensitive matching (like `encoding/json`) rather than v1's multiple variant attempts. Use explicit `toml` struct tags for disambiguation.

**Interface{} handling**: V2 replaces interface{} contents with `map[string]interface{}` during unmarshaling, unlike v1's type preservation. This matches `encoding/json` behavior.

**Array bounds**: V2 silently truncates array values exceeding destination capacity; v1 returned errors.

**Removed features**:

- `toml.Unmarshaler` interface support dropped
- `default` struct tag support removed (use pre-filled structs instead)
- `toml.Tree` document model not provided
- Position retrieval API unavailable

### Encoding Changes

**Field ordering**: V2 emits struct fields in definition order, not alphabetically like v1.

## Additional Resources

- [Bug Reports](https://github.com/pelletier/go-toml/issues)
- [Discussions](https://github.com/pelletier/go-toml/discussions)
- [TOML Specification](https://toml.io/en/v1.0.0)
