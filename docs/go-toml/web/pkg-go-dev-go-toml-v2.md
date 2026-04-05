# go-toml v2 - Complete Package Documentation

Source: https://pkg.go.dev/github.com/pelletier/go-toml/v2

## Overview

`go-toml/v2` is a Go library for reading and writing TOML documents. It supports [TOML v1.0.0](https://toml.io/en/v1.0.0) and is designed to behave similarly to the standard library's `encoding/json`.

**Import:**
```go
import "github.com/pelletier/go-toml/v2"
```

---

## Core Functions

### func Marshal

```go
func Marshal(v interface{}) ([]byte, error)
```

Serializes a Go value as a TOML document. It is a shortcut for `Encoder.Encode()` with default options.

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

### func Unmarshal

```go
func Unmarshal(data []byte, v interface{}) error
```

Deserializes a TOML document into a Go value. It is a shortcut for `Decoder.Decode()` with default options.

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

---

## Types

### type DecodeError

```go
type DecodeError struct {
	// contains filtered or unexported fields
}
```

Represents an error encountered during parsing or decoding of a TOML document. Contains position information and human-readable contextualized error representation.

#### Methods

**func (e \*DecodeError) Error() string**

Returns the error message contained in the DecodeError.

**func (e \*DecodeError) Key() Key**

Returns the key that was being processed when the error occurred (present only if this DecodeError is part of a StrictMissingError).

**func (e \*DecodeError) Position() (row int, column int)**

Returns the (line, column) pair indicating where the error occurred. Positions are 1-indexed.

**func (e \*DecodeError) String() string**

Returns the human-readable contextualized error as a multi-line string.

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

---

### type Decoder

```go
type Decoder struct {
	// contains filtered or unexported fields
}
```

Reads and decodes a TOML document from an input stream.

#### func NewDecoder

```go
func NewDecoder(r io.Reader) *Decoder
```

Creates a new Decoder that will read from `r`.

#### func (d \*Decoder) Decode

```go
func (d *Decoder) Decode(v interface{}) error
```

Decodes the whole content of the reader into `v`.

By default, values in the document that don't exist in the target Go value are ignored. Use `Decoder.DisallowUnknownFields()` to change this behavior.

When a TOML local date, time, or date-time is decoded into a `time.Time`, its value is represented in `time.Local` timezone. Otherwise the appropriate `Local*` structure is used. For time values, precision up to nanosecond is supported by truncating extra digits.

Empty tables decoded in an `interface{}` create an empty initialized `map[string]interface{}`.

Types implementing `encoding.TextUnmarshaler` interface are decoded from a TOML string.

When decoding a number, go-toml returns an error if the number is out of bounds for the target type.

Returns `toml.DecodeError` on decoding errors, `toml.StrictMissingError` when using strict mode and a field is missing, or a standard Go error otherwise.

**Type Mapping:**

| TOML Type | Go Type |
|-----------|---------|
| String | string |
| Integer | uint*, int*, depending on size |
| Float | float*, depending on size |
| Boolean | bool |
| Offset Date-Time | time.Time |
| Local Date-time | LocalDateTime, time.Time |
| Local Date | LocalDate, time.Time |
| Local Time | LocalTime, time.Time |
| Array | slice and array, depending on elements types |
| Table | map and struct |
| Inline Table | same as Table |
| Array of Tables | same as Array and Table |

#### func (d \*Decoder) DisallowUnknownFields

```go
func (d *Decoder) DisallowUnknownFields() *Decoder
```

Causes the Decoder to return an error when the destination is a struct and the input contains a key that does not match a non-ignored field.

Returns a `StrictMissingError` that can be used to retrieve individual errors and generate a human-readable description of missing fields.

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

#### func (d \*Decoder) EnableUnmarshalerInterface

```go
func (d *Decoder) EnableUnmarshalerInterface() *Decoder
```

Allows types implementing the `unstable.Unmarshaler` interface to be decoded from any structure of the document. The `UnmarshalTOML` method receives raw TOML bytes:

- For single values: raw value bytes (e.g., `"hello"` for a string)
- For tables: all key-value lines belonging to that table
- For inline tables/arrays: raw bytes of the inline structure

The `unstable.RawMessage` type can be used to capture raw TOML bytes for later processing, similar to `json.RawMessage`.

**Unstable:** This method does not follow semver compatibility guarantees.

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

// Decode it into a specific type later
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

---

### type Encoder

```go
type Encoder struct {
	// contains filtered or unexported fields
}
```

Writes a TOML document to an output stream.

#### func NewEncoder

```go
func NewEncoder(w io.Writer) *Encoder
```

Returns a new Encoder that writes to `w`.

#### func (enc \*Encoder) Encode

```go
func (enc *Encoder) Encode(v interface{}) error
```

Writes a TOML representation of `v` to the stream. Returns an error if `v` cannot be represented as TOML.

**Encoding Rules:**

- A top-level slice containing only maps or structs is encoded as `[[table array]]`
- All other slices are encoded as `[array]`, and any map or struct they contain is encoded as an inline table
- Nil interfaces and nil pointers are not supported
- Keys in key-values always have one part
- Intermediate tables are always printed
- By default, strings are encoded as literal strings, unless they contain a newline or single quote (then double-quoted)
- Unsigned integers larger than `math.MaxInt64` cannot be encoded
- Struct fields are encoded in definition order with their exact name
- Tables and array tables are separated by empty lines; consecutive subtables are not

**Struct Tags:**

The encoding of each public struct field can be customized via the `"toml"` tag:

- Format: field name optionally followed by comma-separated options
- `"multiline"`: emit strings as multi-line TOML strings
- `"inline"`: turn tables into inline tables
- `"omitempty"`: prevent empty values/groups from being emitted
- `"omitzero"`: prevent zero values/groups from being emitted
- `"commented"`: prefix value and children with comment symbol

A `"comment"` tag can emit TOML comments before values (ignored in inline tables, only before first array element).

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

#### func (enc \*Encoder) SetTablesInline

```go
func (enc *Encoder) SetTablesInline(inline bool) *Encoder
```

Forces the encoder to emit all tables inline. This behavior can be controlled per-field with `toml:",inline"` tag.

#### func (enc \*Encoder) SetArraysMultiline

```go
func (enc *Encoder) SetArraysMultiline(multiline bool) *Encoder
```

Forces the encoder to emit all arrays with one element per line. Can be controlled per-field with `multiline:"true"` tag.

#### func (enc \*Encoder) SetIndentSymbol

```go
func (enc *Encoder) SetIndentSymbol(s string) *Encoder
```

Defines the string used for indentation (repeated for each level). Defaults to two spaces.

#### func (enc \*Encoder) SetIndentTables

```go
func (enc *Encoder) SetIndentTables(indent bool) *Encoder
```

Forces the encoder to indent tables and array tables.

#### func (enc \*Encoder) SetMarshalJSONNumbers

```go
func (enc *Encoder) SetMarshalJSONNumbers(indent bool) *Encoder
```

Forces the encoder to serialize `json.Number` as a float or integer instead of relying on `TextMarshaler` to emit a string.

**Unstable:** This method does not follow semver compatibility guarantees.

---

### type Key

```go
type Key []string
```

Represents a TOML key as a sequence of key parts.

---

### type LocalDate

```go
type LocalDate struct {
	Year  int
	Month int
	Day   int
}
```

Represents a calendar day in no specific timezone.

#### func (d LocalDate) AsTime

```go
func (d LocalDate) AsTime(zone *time.Location) time.Time
```

Converts `d` into a specific time instance at midnight in `zone`.

#### func (d LocalDate) String

```go
func (d LocalDate) String() string
```

Returns RFC 3339 representation of `d`.

#### func (d LocalDate) MarshalText

```go
func (d LocalDate) MarshalText() ([]byte, error)
```

Returns RFC 3339 representation of `d`.

#### func (d \*LocalDate) UnmarshalText

```go
func (d *LocalDate) UnmarshalText(b []byte) error
```

Parses `b` using RFC 3339 to fill `d`.

---

### type LocalTime

```go
type LocalTime struct {
	Hour       int // Hour of the day: [0; 24[
	Minute     int // Minute of the hour: [0; 60[
	Second     int // Second of the minute: [0; 59]
	Nanosecond int // Nanoseconds within the second: [0, 1000000000[
	Precision  int // Number of digits to display for Nanosecond
}
```

Represents a time of day of no specific day in no specific timezone.

#### func (d LocalTime) String

```go
func (d LocalTime) String() string
```

Returns RFC 3339 representation of `d`. If `d.Nanosecond` and `d.Precision` are zero, the time won't have a nanosecond component. If `d.Nanosecond > 0` but `d.Precision = 0`, then the minimum number of digits for nanoseconds is provided.

#### func (d LocalTime) MarshalText

```go
func (d LocalTime) MarshalText() ([]byte, error)
```

Returns RFC 3339 representation of `d`.

#### func (d \*LocalTime) UnmarshalText

```go
func (d *LocalTime) UnmarshalText(b []byte) error
```

Parses `b` using RFC 3339 to fill `d`.

---

### type LocalDateTime

```go
type LocalDateTime struct {
	LocalDate
	LocalTime
}
```

Represents a time of a specific day in no specific timezone.

#### func (d LocalDateTime) AsTime

```go
func (d LocalDateTime) AsTime(zone *time.Location) time.Time
```

Converts `d` into a specific time instance in `zone`.

#### func (d LocalDateTime) String

```go
func (d LocalDateTime) String() string
```

Returns RFC 3339 representation of `d`.

#### func (d LocalDateTime) MarshalText

```go
func (d LocalDateTime) MarshalText() ([]byte, error)
```

Returns RFC 3339 representation of `d`.

#### func (d \*LocalDateTime) UnmarshalText

```go
func (d *LocalDateTime) UnmarshalText(data []byte) error
```

Parses `data` using RFC 3339 to fill `d`.

---

### type StrictMissingError

```go
type StrictMissingError struct {
	// One error per field that could not be found.
	Errors []*DecodeError
}
```

Occurs in a TOML document that does not have a corresponding field in the target value. Contains all missing fields in `Errors`. Emitted by `Decoder` when `DisallowUnknownFields()` was called.

#### func (s \*StrictMissingError) Error

```go
func (s *StrictMissingError) Error() string
```

Returns the canonical string for this error.

#### func (s \*StrictMissingError) String

```go
func (s *StrictMissingError) String() string
```

Returns a human-readable description of all errors.

#### func (s \*StrictMissingError) Unwrap

```go
func (s *StrictMissingError) Unwrap() []error
```

Returns wrapped decode errors. Implements `errors.Join()` interface.

---

## Features

### Performance

go-toml v2 is optimized for performance. Benchmarks show 2-6x speedups compared to other Go TOML libraries.

### Strict Mode

Use `Decoder.DisallowUnknownFields()` to enable strict mode, which errors when parts of the TOML document don't match the target structure -- great for catching typos.

### Local Date/Time Support

TOML supports native local date/times without timezone. go-toml provides `LocalDate`, `LocalTime`, and `LocalDateTime` types that can be transformed to/from `time.Time`.

### Commented Configuration

Generate configuration files with comments and commented-out sections:

```go
type Config struct {
	Host string `toml:"host" comment:"Host IP to connect to."`
	Port int    `toml:"port" comment:"Port of the remote server."`
	TLS  *struct {
		Cipher  string `toml:"cipher"`
		Version string `toml:"version"`
	} `toml:"TLS,commented"`
}

cfg := &Config{
	Host: "127.0.0.1",
	Port: 4242,
}

b, _ := toml.Marshal(cfg)
fmt.Println(string(b))
// Output:
// # Host IP to connect to.
// host = '127.0.0.1'
// # Port of the remote server.
// port = 4242
//
// # Encryption parameters (optional)
// # [TLS]
// # cipher = ''
// # version = ''
```

---

## Installation

Go >= 1.16:
```bash
go get github.com/pelletier/go-toml/v2
```

For Go >= 1.13:
```bash
GO111MODULE=on go get github.com/pelletier/go-toml/v2
```

---

## Command-Line Tools

Three tools are provided:

**tomljson:** Convert TOML to JSON
```bash
go install github.com/pelletier/go-toml/v2/cmd/tomljson@latest
tomljson example.toml
```

**jsontoml:** Convert JSON to TOML
```bash
go install github.com/pelletier/go-toml/v2/cmd/jsontoml@latest
jsontoml example.json
```

**tomll:** Lint and reformat TOML
```bash
go install github.com/pelletier/go-toml/v2/cmd/tomll@latest
tomll example.toml
```

**Docker:**
```bash
docker run -i ghcr.io/pelletier/go-toml:v2 tomljson < example.toml
```

---

## Versioning

go-toml follows [Semantic Versioning](https://semver.org). The last two major versions of Go are supported.

## License

MIT License.
