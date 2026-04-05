# go-toml v2 - GitHub README

Source: https://github.com/pelletier/go-toml

Go library for the [TOML](https://toml.io/en/) format.

This library supports [TOML v1.0.0](https://toml.io/en/v1.0.0).

## Features

### Strict mode

Detect typos in your TOML documents by using strict mode. `Decoder.DisallowUnknownFields()` will error when parts of the TOML document don't match the target structure.

### Contextualized errors

When decoding errors occur, go-toml provides a human-readable error that indicates where in the document the error happened:

```
1| [server]
2| path = 100
 |        ~~~ cannot decode TOML integer into struct field
 |            .Server.Path of type string
```

### Local date and time support

TOML supports native local date/times. go-toml provides `LocalDate`, `LocalTime`, and `LocalDateTime` types, which can be transformed to and from `time.Time`.

### Commented config

Emit configuration files with comment annotations and commented-out default values:

```go
type Config struct {
    Host string `toml:"host" comment:"Host IP to connect to."`
    Port int    `toml:"port" comment:"Port of the remote server."`
    TLS  *struct {
        Cipher  string `toml:"cipher"`
        Version string `toml:"version"`
    } `toml:"TLS,commented"`
}
```

### Performance

go-toml v2 is designed for speed. Benchmarks (go-toml v2.0.6 vs other TOML libraries on a comparable dataset):

#### Unmarshal

| Library | Time/op | Bytes/op | Allocs/op |
|---------|---------|----------|-----------|
| pelletier/go-toml/v2 | 750.0ns | 304B | 11 |
| BurntSushi/toml | 3248ns | 1536B | 49 |
| pelletier/go-toml/v1 | 3533ns | 1280B | 40 |

#### Marshal

| Library | Time/op | Bytes/op | Allocs/op |
|---------|---------|----------|-----------|
| pelletier/go-toml/v2 | 476.6ns | 131B | 3 |
| BurntSushi/toml | 958.8ns | 432B | 10 |
| pelletier/go-toml/v1 | 1005ns | 720B | 20 |

Speedup vs BurntSushi/toml (unmarshal): ~4.3x
Speedup vs go-toml v1 (unmarshal): ~4.7x
Speedup vs BurntSushi/toml (marshal): ~2.0x
Speedup vs go-toml v1 (marshal): ~2.1x

## Getting started

Given the following struct, let's see how to read it and write it as TOML:

```go
type MyConfig struct {
    Version int
    Name    string
    Tags    []string
}
```

### Unmarshaling

```go
package main

import (
    "fmt"
    "github.com/pelletier/go-toml/v2"
)

func main() {
    doc := `
version = 2
name = "go-toml"
tags = ["go", "toml"]
`
    var cfg MyConfig
    err := toml.Unmarshal([]byte(doc), &cfg)
    if err != nil {
        panic(err)
    }
    fmt.Println("version:", cfg.Version)
    fmt.Println("name:", cfg.Name)
    fmt.Println("tags:", cfg.Tags)
}
```

### Marshaling

```go
package main

import (
    "fmt"
    "github.com/pelletier/go-toml/v2"
)

func main() {
    cfg := MyConfig{
        Version: 2,
        Name:    "go-toml",
        Tags:    []string{"go", "toml"},
    }

    b, err := toml.Marshal(cfg)
    if err != nil {
        panic(err)
    }
    fmt.Println(string(b))
}
```

## Unstable API

The `unstable` sub-package provides an unstable API for advanced TOML handling without backward compatibility guarantees. It provides access to go-toml's AST parser.

## Command line tools

Three command-line tools are provided:

### tomljson

Convert TOML to JSON:

```bash
go install github.com/pelletier/go-toml/v2/cmd/tomljson@latest
cat example.toml | tomljson
```

### jsontoml

Convert JSON to TOML:

```bash
go install github.com/pelletier/go-toml/v2/cmd/jsontoml@latest
cat example.json | jsontoml
```

### tomll

Lint and reformat TOML:

```bash
go install github.com/pelletier/go-toml/v2/cmd/tomll@latest
tomll --help
```

### Docker image

All three tools are available via Docker:

```bash
docker run -i ghcr.io/pelletier/go-toml:v2 tomljson < example.toml
```

## Migrating from v1

### Decoder

#### Strict mode

`toml.Decoder` strict mode has been renamed to `DisallowUnknownFields`, matching `encoding/json` behavior.

#### Unmarshal interface

In v1, custom `toml.Unmarshaler` interface was supported. In v2, use the `unstable.Unmarshaler` interface with `EnableUnmarshalerInterface()`.

#### Default values

In v1, `default` struct tag set a default value for the field. In v2, pre-fill your struct with defaults before unmarshaling.

#### Decoding into interface{}

In v1, decoding into `interface{}` created `*toml.Tree`. In v2, it creates `map[string]interface{}` (matching `encoding/json` behavior).

### Encoder

#### Struct field order

In v1, struct fields were alphabetically sorted. In v2, fields are emitted in definition order (matching `encoding/json` behavior).

### Other changes

- `toml.Tree` has been removed. Use the `unstable` package's AST parser for low-level operations.
- The `query` package has been removed.
- `Position` information is no longer available on decoded values.

## Versioning

go-toml follows [Semantic Versioning](https://semver.org). The supported Go versions are the last two major versions of Go.

## License

MIT License.
