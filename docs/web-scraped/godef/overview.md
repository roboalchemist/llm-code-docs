# Godef - Go Definition Locator

## Overview

Godef is a command-line utility for the Go programming language that identifies and displays the source location of definitions within Go programs. When given an expression or source file location, it prints the exact location where the symbol is defined.

**Source:** https://github.com/rogpeppe/godef

## Purpose and Use Cases

Godef is designed to help developers navigate Go source code by quickly locating where symbols (functions, types, variables, methods, etc.) are defined. This is particularly useful for:

- Jump-to-definition workflows in editors and IDEs
- Understanding code structure and dependencies
- Integrating with development tools and IDE plugins
- Automated code analysis and documentation generation

## Installation and Setup

Godef is a standalone Go tool that can be installed using Go's build tools:

```bash
go install github.com/rogpeppe/godef@latest
```

## Command-Line Flags

Godef supports the following command-line options:

### Basic Flags

- **`-i`** (or `-read-stdin`): Read source file content from standard input instead of reading from disk. Useful for unsaved files in editors.

- **`-o offset`**: Specify the character position (offset) within a file where you want to find the definition. Useful when the exact identifier location is known numerically.

- **`-f file`**: Designate the source file to analyze. This tells godef which Go source file contains the identifier you're looking for.

- **`-acme`**: Use this flag to retrieve offset, filename, and contents from an active acme window (Plan 9 editor integration).

### Output Flags

- **`-json`**: Output the definition location in JSON format. This is useful for programmatic consumption and tool integration. When this flag is used, the `-t` flag is ignored.

### Deprecated Flags (Ignored for Backward Compatibility)

- **`-debug`**: Previously used for debug output, now ignored.
- **`-t`**: Previously output type information, now deprecated.
- **`-a`**: Previously listed all public members, now deprecated.
- **`-A`**: Previously included private members, now deprecated.

### Profiling Flags (Development/Debugging)

- **`-cpuprofile file`**: Write CPU profile data to the specified file for performance analysis.
- **`-memprofile file`**: Write memory profile data to the specified file for memory analysis.
- **`-trace file`**: Write execution trace data to the specified file for detailed performance investigation.

## Input Requirements

To use godef, you must provide one of the following:

1. **An identifier or Go expression** (terminated with a field selector)
2. **An offset** pointing to a location within a file

Additionally, you must specify:

- Either a file via `-f file` flag, or
- Source code via standard input with `-i` flag (optionally with `-o offset` for the identifier position)

## Usage Examples

### Basic Usage: Find Definition by Expression

Find where `NewParser().Skip` is defined in a specific file:

```bash
godef -f src/pkg/xml/read.go 'NewParser().Skip'
```

Output:
```
src/pkg/xml/read.go:384:18
```

This output means:
- **File:** `src/pkg/xml/read.go`
- **Line:** 384
- **Column:** 18

### Using File Offset

If you know the exact character offset in a file where an identifier starts, use the `-o` flag:

```bash
godef -f myfile.go -o 1234
```

### Reading from Standard Input

For integration with editors that haven't saved the file to disk:

```bash
cat myfile.go | godef -i -f myfile.go -o 100
```

### JSON Output

Get the result in JSON format for tool integration:

```bash
godef -json -f myfile.go 'MyType'
```

This outputs structured JSON that can be parsed by other tools.

## Output Format

Godef produces simple, line-oriented output:

```
filename:line:column
```

### Example Outputs

```
/home/user/project/main.go:42:5
/home/user/project/types.go:87:1
$GOROOT/src/fmt/print.go:234:6
```

The output includes:
- **filename**: Absolute or relative path to the source file
- **line**: 1-indexed line number where the definition starts
- **column**: 1-indexed column number where the definition starts

## Known Limitations

Godef has two documented constraints:

1. **No support for "." imports**: When Go code uses dot imports (`import . "package"`), godef may not properly resolve identifiers imported that way.

2. **Test file definitions**: Definitions found in test files (files ending with `_test.go`) may not be properly located in some cases.

## Implementation Details

### Architecture

Godef uses the Go standard library's type checking and parsing facilities:

- **`go/ast`**: Abstract Syntax Tree parsing
- **`go/types`**: Type information and object tracking
- **`golang.org/x/tools/go/packages`**: Package loading and analysis

### Key Components

**godefPackages()**: Core function that:
1. Parses the source file containing the identifier
2. Loads and type-checks related packages
3. Locates the exact AST node at the search position
4. Uses type information to find the definition location

**parseFile()**: Handles:
- File parsing with optional source replacement (for stdin input)
- Function body filtering to optimize for the search position
- Identifier matching at the specified offset

**Embedded Field Handling**: Special logic to handle embedded fields - when an identifier refers to an embedded type field, godef attempts to follow the type definition chain to provide more meaningful results.

### Performance Optimizations

- **GC Tuning**: Sets garbage collection percentage to 1600 (very permissive) to avoid GC pauses during normal operation
- **Lazy Parsing**: Only parses function bodies that contain the search position
- **Profiling Support**: Built-in support for CPU, memory, and execution tracing for performance analysis

## Type Resolution

Godef performs full type checking to resolve identifiers correctly. It can handle:

- **Function definitions**: Locates function declarations
- **Method receivers**: Finds method definitions including their receivers
- **Type aliases**: Resolves alias definitions to the actual type
- **Package-level variables/constants**: Locates declarations at package scope
- **Local scope variables**: Can find variables defined within functions
- **Imported identifiers**: Follows imports to locate definitions in other packages
- **Struct fields and methods**: Locates field and method definitions in types

## Tool Integration

Godef's simple output format and JSON mode make it suitable for integration with:

- Editor plugins and IDE extensions
- Build system analyzers
- Documentation generators
- Code search tools
- Automated refactoring tools
- Language server implementations

### Example Integration: Editor Plugin

An editor plugin can:

1. Detect cursor position when user invokes "go to definition"
2. Calculate character offset in current file
3. Call: `godef -json -f filename -o offset`
4. Parse JSON output
5. Open the file at the returned location

## Development and Contribution

Godef is actively maintained and accepts contributions. The project:

- Uses Go modules for dependency management
- Includes comprehensive test suite (`godef_test.go`)
- Integrates with acme window manager for Plan 9 compatibility
- Supports multiple usage patterns (acme, CLI, stdin)

For issues, bug reports, and contributions, see: https://github.com/rogpeppe/godef

## Related Tools

Similar tools in the Go ecosystem:

- **gogetdoc**: Returns documentation for Go identifiers
- **go-def**: LSP implementation of definition lookup
- **guru**: Oracle-style analysis tool for Go
- **gopls**: Official Go language server (includes definition support)
