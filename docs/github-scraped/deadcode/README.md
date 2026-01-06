# Deadcode - Go Tool for Finding Unused Code

**Source:** https://pkg.go.dev/golang.org/x/tools/cmd/deadcode

**Repository:** golang.org/x/tools (https://go.googlesource.com/tools/)

## Overview

The `deadcode` command is a Go tool that reports unreachable functions in Go programs using Rapid Type Analysis (RTA) to build a call graph from the program's main function.

## What It Does

- Loads a Go program from source
- Builds a call graph of all functions reachable from the main function
- Reports any functions that are not reachable as dead code, grouped by package
- Only analyzes executable (main) packages by default

## Installation

```bash
go install golang.org/x/tools/cmd/deadcode@latest
```

## Usage

### Basic Syntax

```
deadcode [flags] package...
```

### Command-Line Flags

| Flag | Purpose |
|------|---------|
| `-test` | Analyze test executables; tests may use functions appearing as dead code |
| `-filter=regex` | Restrict results to packages matching the regex (default matches listed packages and their modules) |
| `-filter=` | Display all results |
| `-generated` | Include dead functions in generated files (excluded by default) |
| `-json` | Output results as JSON |
| `-f=template` | Format output using Go template |
| `-whylive=function` | Explain why a named function is not dead; shows shortest path from main |

## Output Formats

### Default Format (Compiler Diagnostic Style)

Shows dead code using standard Go compiler error format:

```
gopls/internal/protocol/command.go:1206:6: unreachable func: openClientEditor
gopls/internal/template/parse.go:414:18: unreachable func: Parsed.WriteNode
```

This format includes:
- File path and location
- "unreachable func:" label
- Function name

### Template Format

Custom output using Go text/template syntax:

```
{{println .Path}}{{range .Funcs}}{{printf "\t%s\n" .Name}}{{end}}{{println}}
```

Available template variables:
- `.Path` - Package import path
- `.Funcs` - List of dead functions in package
  - `.Name` - Function name
  - `.Position` - File location
  - `.Generated` - Whether in generated file

### JSON Format

Enable with `-json` flag to get structured output:

```json
[
  {
    "Path": "golang.org/x/tools/cmd/deadcode",
    "Name": "deadcode",
    "Funcs": [
      {
        "Name": "unusedFunction",
        "Position": {
          "Filename": "main.go",
          "Line": 42,
          "Column": 5
        },
        "Generated": false,
        "Marker": false
      }
    ]
  }
]
```

### Why-Live Format

Show call chain explaining why a function is reachable:

```
                 golang.org/x/tools/cmd/deadcode.main
static@L0117 --> golang.org/x/tools/go/packages.Load
static@L0262 --> golang.org/x/tools/go/packages.defaultDriver
```

Call path notation:
- `static@LINE` - Statically reachable function call
- `dynamic@LINE` - Dynamically reachable (via interface, reflection, etc.)
- Arrow shows call direction

## Example Commands

### Find All Dead Code in a Module

```bash
# Show all dead code within gopls module with tests
deadcode -test golang.org/x/tools/gopls/...
```

### Explain Why a Function is Alive

```bash
# Show the call chain proving a function is reachable
deadcode -whylive=bytes.Buffer.String -test ./cmd/deadcode/...
```

### JSON Output for Processing

```bash
# Get structured output for integration with other tools
deadcode -json ./...
```

### Custom Output Format

```bash
# Show only package paths with dead function counts
deadcode -f='{{.Path}}: {{len .Funcs}} dead functions' ./...
```

### Include Generated Code

```bash
# Don't exclude functions in generated .go files
deadcode -generated ./...
```

## Data Structures

### Package Report

```go
type Package struct {
	Name  string       // declared name
	Path  string       // full import path
	Funcs []Function   // list of dead functions
}
```

### Function

```go
type Function struct {
	Name      string   // name (sans package qualifier)
	Position  Position // file/line/column
	Generated bool     // in generated .go file
	Marker    bool     // marker interface method
}
```

### Position

```go
type Position struct {
	Filename string // file path
	Line     int    // line number
	Column   int    // column number
}
```

### Call Edge (for -whylive)

```go
type Edge struct {
	Initial  string   // main or init entrypoint
	Kind     string   // "static" or "dynamic"
	Position Position // call site location
	Callee   string   // target function
}
```

## Important Limitations and Caveats

### False Positives

- **`//go:linkname` directives**: Not understood by deadcode, may report false positives for linked functions
- **Reflection**: Functions called via reflection may be reported as dead
- **Cgo**: C-linked functions may be reported as dead

### Configuration Sensitivity

- Results are valid only for a single `GOOS`/`GOARCH`/`-tags` configuration
- Different build configurations may have different dead code

### Marker Interfaces

- Marker interface methods are not reported as dead by default (prevents false positives breaking interface implementations)
- Use `-f` template to customize this behavior

### Safety Considerations

- Dead code report doesn't mean it's always safe to delete:
  - May be referenced by other dead functions
  - May satisfy interface implementations
  - May be used in other build configurations
  - May have external references (cgo, linkname, reflection)

## Common Use Cases

### Code Cleanup

Identify unused functions for removal during refactoring:

```bash
deadcode ./... | grep -E '\.go:[0-9]+' | head -20
```

### Analyze Public APIs

Find unexported functions that can be safely removed:

```bash
deadcode -filter='mypackage' ./...
```

### Include Test Code

When analyzing with tests enabled, understand test-only dependencies:

```bash
deadcode -test -whylive=myFunc ./...
```

### Batch Processing

Export results for analysis in other tools:

```bash
deadcode -json ./... | jq '.[] | select(.Path | contains("mypackage"))'
```

## Integration with Development Tools

### Use in CI/CD

Add to pipeline to prevent dead code accumulation:

```bash
deadcode ./... | grep -q . && { echo "Found dead code"; exit 1; }
```

### IDE Integration

Modern IDEs (gopls, GoLand) integrate deadcode analysis:
- Shows warnings in editor
- Can trigger on save or manually
- Often integrated with other static analysis tools

### Pre-commit Hooks

```bash
#!/bin/bash
deadcode -test ./... | grep -q . && {
  echo "⚠️  Dead code detected - please review:"
  deadcode -test ./...
  exit 1
}
```

## Performance Notes

- Analyzes only main packages by default (faster)
- `-test` flag includes test packages (slower)
- Uses Rapid Type Analysis (RTA) for efficiency
- May be slow on large codebases; consider using `-filter` to restrict scope

## Related Tools

- **`go vet`** - General linting tool (doesn't detect dead code specifically)
- **`staticcheck`** - Extended static analysis (includes unused code detection)
- **`golangci-lint`** - Aggregates multiple linters including deadcode analyzers
- **`gopls`** - Official Go language server (integrates deadcode analysis)

## See Also

- Official Tool Documentation: https://pkg.go.dev/golang.org/x/tools/cmd/deadcode
- golang.org/x/tools Repository: https://go.googlesource.com/tools
- Rapid Type Analysis (RTA): https://github.com/golang/tools/wiki/Deadcode
- Go Blog Post: https://go.dev/blog/deadcode
