# go-toml/v2 API Reference

Source: <https://pkg.go.dev/github.com/pelletier/go-toml/v2>

## Package Overview

Package `toml` is a library to read and write TOML documents. This library supports [TOML v1.0.0](https://toml.io/en/v1.0.0).

**Import Path:**

```go
import "github.com/pelletier/go-toml/v2"
```

**Module:** github.com/pelletier/go-toml/v2 v2.3.0

**License:** MIT

**Published:** Mar 24, 2026

## Key Features

- **Stdlib behavior**: Designed to behave similarly to `encoding/json`
- **Performance**: Optimized for speed while maintaining usability
- **Strict mode**: Error on unknown fields in target struct
- **Contextualized errors**: `DecodeError` with human-readable context
- **Local date/time support**: `LocalDate`, `LocalTime`, `LocalDateTime` types
- **Commented config**: Support for comments and commented-out values in output

## Functions

### Marshal

```go
func Marshal(v interface{}) ([]byte, error)
```

Serializes a Go value as a TOML document. Shortcut for `Encoder.Encode()` with default options.

**Example:**

```go
type MyConfig struct {
    Version int
    Name    string
    Tags    []string
}

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

// Output:
// Version = 2
// Name = 'go-toml'
// Tags = ['go', 'toml']
```

### Unmarshal

```go
func Unmarshal(data []byte, v interface{}) error
```

Deserializes a TOML document into a Go value. Shortcut for `Decoder.Decode()` with default options.

**Example:**

```go
type MyConfig struct {
    Version int
    Name    string
    Tags    []string
}

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

// Output:
// version: 2
// name: go-toml
// tags: [go toml]
```

## Types

### DecodeError

```go
type DecodeError struct {
    // contains filtered or unexported fields
}
```

Represents an error encountered during parsing or decoding of a TOML document. Contains position information and human-readable representation.

#### DecodeError.Error

```go
func (e *DecodeError) Error() string
```

Returns the error message.

#### DecodeError.Position

```go
func (e *DecodeError) Position() (row int, column int)
```

Returns the (line, column) pair where the error occurred. Positions are 1-indexed.

#### DecodeError.Key

```go
func (e *DecodeError) Key() Key
```

Returns the key being processed when the error occurred (only set for `StrictMissingError`).

#### DecodeError.String

```go
func (e *DecodeError) String() string
```

Returns human-readable contextualized error with multi-line output.

**Example:**

```go
doc := `name = 123__456`

s := map[string]interface{}{}
err := Unmarshal([]byte(doc), &s)

fmt.Println(err)

var derr *DecodeError
if errors.As(err, &derr) {
    fmt.Println(derr.String())
    row, col := derr.Position()
    fmt.Println("error occurred at row", row, "column", col)
}

// Output:
// toml: number must have at least one digit between underscores
// 1| name = 123__456
//  |           ~~ number must have at least one digit between underscores
// error occurred at row 1 column 11
```

### Decoder

```go
type Decoder struct {
    // contains filtered or unexported fields
}
```

Reads and decodes a TOML document from an input stream.

#### NewDecoder

```go
func NewDecoder(r io.Reader) *Decoder
```

Creates a new Decoder that reads from `r`.

#### Decoder.Decode

```go
func (d *Decoder) Decode(v interface{}) error
```

Decodes the whole content of the reader into `v`.

By default, values in the document that don't exist in the target Go value are ignored. Use `DisallowUnknownFields()` to change this.

**Type Mapping:**

| TOML Type | Go Type |
|-----------|---------|
| String | string |
| Integer | uint*, int* (depending on size) |
| Float | float* (depending on size) |
| Boolean | bool |
| Offset Date-Time | time.Time |
| Local Date-time | LocalDateTime, time.Time |
| Local Date | LocalDate, time.Time |
| Local Time | LocalTime, time.Time |
| Array | slice and array |
| Table | map and struct |
| Inline Table | map and struct |
| Array of Tables | slice of map/struct |

#### Decoder.DisallowUnknownFields

```go
func (d *Decoder) DisallowUnknownFields() *Decoder
```

Returns an error when the destination is a struct and the input contains a key that doesn't match a non-ignored field. Returns `StrictMissingError` to retrieve individual errors.

**Example:**

```go
type S struct {
    Key1 string
    Key3 string
}
doc := `
key1 = "value1"
key2 = "value2"
key3 = "value3"
`
r := strings.NewReader(doc)
d := toml.NewDecoder(r)
d.DisallowUnknownFields()
s := S{}
err := d.Decode(&s)

fmt.Println(err.Error())

var details *toml.StrictMissingError
if !errors.As(err, &details) {
    panic(fmt.Sprintf("err should have been a *toml.StrictMissingError, but got %s (%T)", err, err))
}

fmt.Println(details.String())

// Output:
// strict mode: fields in the document are missing in the target struct
// 2| key1 = "value1"
// 3| key2 = "value2"
//  | ~~~~ missing field
// 4| key3 = "value3"
```

#### Decoder.EnableUnmarshalerInterface

Added in v2.2.0.

```go
func (d *Decoder) EnableUnmarshalerInterface() *Decoder
```

Enables the unstable `Unmarshaler` interface. Types implementing this interface can be decoded from any document structure. The `UnmarshalTOML` method receives raw TOML bytes:

- For single values: raw value bytes (e.g., `"hello"` for a string)
- For tables: all key-value lines belonging to that table
- For inline tables/arrays: raw bytes of the inline structure

**Unstable**: Does not follow semver compatibility guarantees.

**Example (RawMessage):**

```go
doc := `
[plugin]
name = "example"
version = "1.0"
enabled = true
`

type Config struct {
    Plugin unstable.RawMessage `toml:"plugin"`
}

var cfg Config
err := toml.NewDecoder(strings.NewReader(doc)).
    EnableUnmarshalerInterface().
    Decode(&cfg)
if err != nil {
    panic(err)
}

// cfg.Plugin contains the raw TOML bytes
fmt.Printf("Raw TOML captured:\n%s", cfg.Plugin)

// You can later decode it into a specific type
var plugin struct {
    Name    string `toml:"name"`
    Version string `toml:"version"`
    Enabled bool   `toml:"enabled"`
}
if err := toml.Unmarshal(cfg.Plugin, &plugin); err != nil {
    panic(err)
}
fmt.Printf("Decoded: name=%s version=%s enabled=%v\n",
    plugin.Name, plugin.Version, plugin.Enabled)

// Output:
// Raw TOML captured:
// name = "example"
// version = "1.0"
// enabled = true
// Decoded: name=example version=1.0 enabled=true
```

**Example (DynamicConfig):**

```go
doc := `
[[plugins]]
type = "database"
host = "localhost"
port = 5432

[[plugins]]
type = "cache"
ttl = 300
`
type Config struct {
    Plugins []pluginConfig `toml:"plugins"`
}

var cfg Config
err := toml.NewDecoder(strings.NewReader(doc)).
    EnableUnmarshalerInterface().
    Decode(&cfg)
if err != nil {
    panic(err)
}

for _, p := range cfg.Plugins {
    fmt.Printf("type=%s config=%v\n", p.Type, p.Config)
}

// Output:
// type=database config=map[host:localhost port:5432]
// type=cache config=map[ttl:300]
```

### Encoder

```go
type Encoder struct {
    // contains filtered or unexported fields
}
```

Writes a TOML document to an output stream.

#### NewEncoder

```go
func NewEncoder(w io.Writer) *Encoder
```

Returns a new Encoder that writes to `w`.

#### Encoder.Encode

```go
func (enc *Encoder) Encode(v interface{}) error
```

Writes a TOML representation of `v` to the stream.

**Encoding Rules:**

- Top-level slice containing only maps/structs becomes `[[table array]]`
- All other slices become `[array]` (contained maps/structs become inline tables)
- Nil interfaces and nil pointers are not supported
- Keys always have one part
- Intermediate tables always printed
- By default, strings are literal unless containing newline or single quote (then quoted)
- Unsigned integers > math.MaxInt64 produce an error
- Struct fields encoded in definition order with exact name
- Tables/array tables separated by empty lines; consecutive subtables not separated

**Struct Tags:**

| Tag | Description |
|-----|-------------|
| `toml:"name"` | Field name in TOML |
| `multiline:"true"` or `multiline` | Emit strings as multi-line |
| `inline` | Emit tables as inline tables |
| `omitempty` | Prevent empty values from being emitted |
| `omitzero` | Prevent zero values from being emitted |
| `commented` | Prefix with comment symbol |
| `comment:"text"` | Add TOML comment before value |

#### Encoder.SetTablesInline

```go
func (enc *Encoder) SetTablesInline(inline bool) *Encoder
```

Forces encoder to emit all tables inline. Can be controlled per-field with `toml:",inline"` tag.

#### Encoder.SetArraysMultiline

```go
func (enc *Encoder) SetArraysMultiline(multiline bool) *Encoder
```

Forces encoder to emit all arrays with one element per line. Can be controlled per-field with `multiline:"true"` tag.

#### Encoder.SetIndentSymbol

```go
func (enc *Encoder) SetIndentSymbol(s string) *Encoder
```

Defines string for indentation. Repeated for each indentation level. Defaults to two spaces.

#### Encoder.SetIndentTables

```go
func (enc *Encoder) SetIndentTables(indent bool) *Encoder
```

Forces encoder to indent tables and array tables.

#### Encoder.SetMarshalJSONNumbers

Added in v2.3.0.

```go
func (enc *Encoder) SetMarshalJSONNumbers(indent bool) *Encoder
```

Forces encoder to serialize `json.Number` as float or integer instead of relying on `TextMarshaler` to emit a string.

**Unstable**: Does not follow semver compatibility guarantees.

### LocalDate

```go
type LocalDate struct {
    Year  int
    Month int
    Day   int
}
```

Represents a calendar day in no specific timezone.

#### LocalDate.AsTime

```go
func (d LocalDate) AsTime(zone *time.Location) time.Time
```

Converts LocalDate into a time.Time instance at midnight in the specified zone.

#### LocalDate.String

```go
func (d LocalDate) String() string
```

Returns RFC 3339 representation.

#### LocalDate.MarshalText

```go
func (d LocalDate) MarshalText() ([]byte, error)
```

Returns RFC 3339 representation as bytes.

#### LocalDate.UnmarshalText

```go
func (d *LocalDate) UnmarshalText(b []byte) error
```

Parses RFC 3339 bytes to fill LocalDate.

### LocalTime

```go
type LocalTime struct {
    Hour       int // [0; 24[
    Minute     int // [0; 60[
    Second     int // [0; 59]
    Nanosecond int // [0, 1000000000[
    Precision  int // Number of digits to display for Nanosecond
}
```

Represents a time of day in no specific timezone.

#### LocalTime.String

```go
func (d LocalTime) String() string
```

Returns RFC 3339 representation. If Nanosecond and Precision are zero, no nanosecond component. If Nanosecond > 0 but Precision = 0, minimum digits for nanoseconds provided.

#### LocalTime.MarshalText

```go
func (d LocalTime) MarshalText() ([]byte, error)
```

Returns RFC 3339 representation as bytes.

#### LocalTime.UnmarshalText

```go
func (d *LocalTime) UnmarshalText(b []byte) error
```

Parses RFC 3339 bytes to fill LocalTime.

### LocalDateTime

```go
type LocalDateTime struct {
    LocalDate
    LocalTime
}
```

Represents a time of a specific day in no specific timezone.

#### LocalDateTime.AsTime

```go
func (d LocalDateTime) AsTime(zone *time.Location) time.Time
```

Converts LocalDateTime into a time.Time instance in the specified zone.

#### LocalDateTime.String

```go
func (d LocalDateTime) String() string
```

Returns RFC 3339 representation.

#### LocalDateTime.MarshalText

```go
func (d LocalDateTime) MarshalText() ([]byte, error)
```

Returns RFC 3339 representation as bytes.

#### LocalDateTime.UnmarshalText

```go
func (d *LocalDateTime) UnmarshalText(data []byte) error
```

Parses RFC 3339 bytes to fill LocalDateTime.

### Key

```go
type Key []string
```

Represents a TOML key as a sequence of key parts.

### StrictMissingError

```go
type StrictMissingError struct {
    // One error per field that could not be found.
    Errors []*DecodeError
}
```

Occurs when a TOML document has fields without corresponding fields in the target struct. Contains all missing fields in `Errors`.

Emitted by Decoder when `DisallowUnknownFields()` was called.

#### StrictMissingError.Error

```go
func (s *StrictMissingError) Error() string
```

Returns the canonical error string.

#### StrictMissingError.String

```go
func (s *StrictMissingError) String() string
```

Returns human-readable description of all errors.

#### StrictMissingError.Unwrap

Added in v2.3.0.

```go
func (s *StrictMissingError) Unwrap() []error
```

Returns wrapped decode errors. Implements `errors.Join()` interface.

## Source Files

- decode.go
- doc.go
- errors.go
- localtime.go
- marshaler.go
- strict.go
- types.go
- unmarshaler.go

## Command-Line Tools

- **tomljson**: Converts TOML to JSON
- **jsontoml**: Converts JSON to TOML
- **tomll**: TOML linter and reformatter
- **gotoml-test-decoder**: Minimal decoder for comparing implementations
- **gotoml-test-encoder**: Minimal encoder for comparing implementations
- **tomltestgen**: Generates test cases from language-agnostic TOML test suite

All available as Docker image: `ghcr.io/pelletier/go-toml:v2`
