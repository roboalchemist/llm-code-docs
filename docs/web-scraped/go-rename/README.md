# Source: https://pkg.go.dev/golang.org/x/tools/cmd/gorename

# Go Rename (gorename) - Identifier Refactoring Tool

**gorename** is a command-line tool from the Go tools package that performs **precise type-safe renaming of identifiers in Go source code**. It was a key refactoring tool for Go developers before the advent of Language Server Protocol (LSP) and gopls.

## Overview

The gorename tool enables safe refactoring of Go programs by renaming identifiers (variables, functions, types, methods, constants, etc.) while maintaining type safety and ensuring all references are updated correctly across your entire codebase.

**Module:** `golang.org/x/tools/cmd/gorename`
**Package:** `golang.org/x/tools/refactor/rename`
**Repository:** [cs.opensource.google/go/x/tools](https://cs.opensource.google/go/x/tools)
**License:** BSD-3-Clause

### Current Status

⚠️ **Deprecated:** The gorename tool implementation has not worked properly since the advent of Go modules. The package is marked for deletion and is no longer maintained.

**Recommendation:** For modern Go development, use **gopls** instead, either via:
- The Rename LSP method in your editor
- The `"gopls rename"` subcommand in the CLI

## Installation

To install gorename from source:

```bash
go install golang.org/x/tools/cmd/gorename@latest
```

The tool will be installed to your `$GOPATH/bin` directory.

## Usage

### Basic Syntax

```bash
gorename -help
```

### Command-Line Flags

The tool accepts the following flags:

| Flag | Type | Description |
|------|------|-------------|
| `-offset` | string | Byte offset of the identifier to rename (format: `filename:#column:line`) |
| `-from` | string | Import path of the package containing the identifier |
| `-to` | string | New name for the identifier |
| `-force` | bool | Patch files even if conflicts exist |
| `-diff` | bool | Display diffs instead of rewriting files |
| `-diffcmd` | string | Diff command to use (default: "diff") |
| `-v` | bool | Enable verbose logging |

### Common Examples

#### Rename a function at a specific location

```bash
# Rename 'oldFunc' to 'newFunc' at a specific file location
gorename -offset myfile.go:#15:5 -to newFunc
```

#### Rename with explicit package and symbol

```bash
# Rename using from flag to specify the symbol location
gorename -from "github.com/myuser/myproject" -to newName
```

#### Preview changes before applying

```bash
# Show diffs without modifying files
gorename -offset myfile.go:#15:5 -to newName -diff
```

## Implementation

gorename is implemented through the `golang.org/x/tools/refactor/rename` package, which provides the core renaming logic.

### Key Components

#### Main Functions

**`Main(ctxt *build.Context, offsetFlag, fromFlag, to string) error`**
- Entry point for the renaming functionality
- Parses the offset/from flags and performs the rename operation

**`Move(ctxt *build.Context, from, to, moveTmpl string) error`**
- Moves a package from one import path to another
- Checks for conflicts preventing the move
- Builds an import graph to find all imports
- Renames all imports to point to new paths
- Moves packages to their new locations

#### Configuration Variables

```go
var (
    Force      bool   // Patch files even if conflicts exist
    Diff       bool   // Display diffs instead of rewriting files
    DiffCmd    string // Diff command (default: "diff")
    Verbose    bool   // Enable extra logging
)
```

#### Error Handling

```go
var ConflictError error // Returned when renaming aborts due to conflicts
```

### Source Files

The rename package consists of these implementation files:

- `rename.go` - Core renaming logic
- `check.go` - Conflict detection and validation
- `mvpkg.go` - Package move functionality
- `spec.go` - Go AST specification handling
- `util.go` - Utility functions

## How It Works

1. **Identifier Location**: You specify the identifier to rename using the `-offset` flag (file location + byte offset)
2. **Type Analysis**: gorename analyzes the type information to identify all references to the identifier
3. **Conflict Detection**: It checks for potential conflicts (e.g., name collisions with existing identifiers)
4. **Safe Refactoring**: All references across the codebase are updated atomically
5. **Application**: Changes are written to files or displayed as diffs

## Limitations

- **Module Awareness**: The implementation has not worked properly since Go modules became standard
- **Scope**: Works within the bounds of the Go build context
- **Import Paths**: May have issues with complex import configurations

## Migration to gopls

For modern Go development, the recommended approach is to use **gopls** (Go Language Server):

### Using gopls rename

```bash
# Interactive rename using gopls
gopls rename -w <file>:<line>:<column> <new-name>
```

### In Your Editor

Most modern editors (VS Code, GoLand, Vim with LSP) provide rename functionality through gopls:

- **VS Code**: Right-click > Rename Symbol or press F2
- **Vim/Neovim**: `:GoRename` (with vim-go) or LSP rename
- **Emacs**: `eglot-rename`
- **GoLand**: Right-click > Refactor > Rename

## API Reference

### rename Package Functions

#### Building Import Graph

The tool builds an import graph to understand dependencies:

```go
// Pseudocode - actual implementation in check.go
graph := buildImportGraph(context)
for each package in graph:
    if contains(identifier):
        update(package)
```

#### Handling Package Moves

When moving packages:

1. Check destination doesn't already exist
2. Build import graph for the old package
3. Update all imports pointing to old path
4. Move files to new location
5. Update internal references

## Type Safety

gorename uses Go's type information system to ensure:

- Only references to the actual identifier are renamed
- No accidental shadowing or collision
- Scope is correctly identified (local, function, package, exported)

## Examples

### Renaming a Local Variable

```bash
# First, open the file and identify the line and column
# Then use gorename to rename it across the scope

gorename -offset myfile.go:#42:10 -to newVarName
```

### Renaming an Exported Function

```bash
# Rename an exported function that might be imported elsewhere

gorename -offset main.go:#100:6 -to NewFunctionName
```

### Renaming a Type

```bash
# Rename a struct or interface type

gorename -offset types.go:#15:6 -to NewTypeName
```

### Preview Changes

```bash
# Always preview large refactorings first

gorename -offset main.go:#50:5 -to newName -diff
```

## Related Tools

- **gopls** - Modern Language Server Protocol implementation for Go (recommended)
- **gofmt** - Code formatting
- **go vet** - Code analysis
- **go fix** - Automated fixes for deprecated code

## Troubleshooting

### "Offset not found"
- Verify the file path is correct
- Ensure the byte offset matches an actual identifier
- Check the file exists and is readable

### "No packages found"
- Verify you're in a Go project directory
- Check that the package structure is valid
- Ensure `go.mod` is present (for modules)

### Conflicts detected
- Use `-diff` to see what would change
- Use `-force` to override conflicts (not recommended)
- Consider doing the rename in stages

## Performance Considerations

- gorename must parse and analyze all files in the package
- Large projects may take significant time
- Complexity increases with package interdependencies
- Preview with `-diff` before applying large refactorings

## See Also

- [gopls Documentation](https://github.com/golang/tools/tree/master/gopls)
- [Go Language Server Protocol](https://github.com/golang/tools/tree/master/cmd/gopls)
- [golang.org/x/tools Package](https://pkg.go.dev/golang.org/x/tools)
- [Go Refactoring Tools](https://golang.org/doc/effective_go#names)

## License

gorename is part of the Go tools project and is licensed under the BSD 3-Clause License.
