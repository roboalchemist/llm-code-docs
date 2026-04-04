# Source: https://pkg.go.dev/golang.org/x/tools/refactor/rename

# Go Rename API Reference

Complete API reference for the `golang.org/x/tools/refactor/rename` package.

## Package Overview

```go
import "golang.org/x/tools/refactor/rename"
```

The rename package provides identifier renaming functionality for Go source code.

**Module:** `golang.org/x/tools`
**Version:** v0.40.0
**License:** BSD-3-Clause

## Constants

None exported at the package level.

## Variables

### Configuration Variables

```go
var (
    // Force controls whether to patch files even if conflicts exist
    Force bool

    // Diff enables diff mode - displays diffs instead of rewriting files
    Diff bool

    // DiffCmd specifies the diff command to use
    DiffCmd string = "diff"

    // Verbose enables extra logging output
    Verbose bool
)
```

### Error Variables

```go
var ConflictError error
```
Returned when renaming aborts due to identifier conflicts.

## Functions

### Main

```go
func Main(ctxt *build.Context, offsetFlag, fromFlag, to string) error
```

**Purpose:** Entry point for the rename operation.

**Parameters:**
- `ctxt` (*build.Context) - Build context specifying compilation environment
- `offsetFlag` (string) - Location of identifier to rename (format: `file:#offset` or `file:#line:column`)
- `fromFlag` (string) - Import path context for the identifier
- `to` (string) - New name for the identifier

**Returns:** Error if operation fails, including ConflictError if conflicts detected.

**Example:**
```go
import (
    "go/build"
    "golang.org/x/tools/refactor/rename"
)

ctx := build.Default
err := rename.Main(&ctx, "main.go:#142", "", "newName")
if err != nil {
    log.Fatal(err)
}
```

### Move

```go
func Move(ctxt *build.Context, from, to, moveTmpl string) error
```

**Purpose:** Moves a package from one import path to another, updating all imports.

**Parameters:**
- `ctxt` (*build.Context) - Build context for the operation
- `from` (string) - Current import path of package to move
- `to` (string) - New import path for the package
- `moveTmpl` (string) - Template string for constructing moved paths

**Returns:** Error if move operation fails.

**Functionality:**
1. Validates that destination path is available
2. Builds complete import graph of the codebase
3. Finds all imports of the package being moved
4. Updates all import statements
5. Relocates package files
6. Updates internal package references

**Example:**
```go
// Move github.com/old/path to github.com/new/path
err := rename.Move(&build.Default,
    "github.com/old/path",
    "github.com/new/path",
    "")
```

## Types

### ObjectSpec

The rename logic operates on Go AST specifications:

- Identifiers (variables, constants)
- Functions and methods
- Types (structs, interfaces, custom types)
- Named imports

## Implementation Details

### Source Files

| File | Purpose |
|------|---------|
| `rename.go` | Core renaming algorithm and identifier analysis |
| `check.go` | Conflict detection and validation logic |
| `mvpkg.go` | Package move functionality and import graph building |
| `spec.go` | Go AST specification handling |
| `util.go` | Utility functions for path handling and Go operations |

### How Renaming Works

1. **Parse**: Locate the identifier at the specified offset
2. **Analyze**: Determine identifier type and scope
3. **Search**: Find all references to the identifier
4. **Check**: Detect conflicts (name shadowing, collisions)
5. **Update**: Apply renaming to all files
6. **Write/Diff**: Either modify files or display diffs

### Import Graph

For package-level operations, the rename package builds a complete import graph:

```
Package A imports Package B
Package C imports Package B
Package B imports Package D
...
```

This allows the tool to:
- Find all packages importing a moved package
- Update import statements consistently
- Detect circular dependencies

## Error Handling

### ConflictError

Returned when the rename operation detects conflicts:

```go
if err := rename.Main(&ctx, offset, fromFlag, newName); err != nil {
    if err == rename.ConflictError {
        // Handle conflict - name already exists
        fmt.Println("Name conflict detected")
    } else {
        // Handle other errors
        log.Fatal(err)
    }
}
```

### Force Override

When conflicts are detected, you can override with the Force flag:

```go
rename.Force = true
err := rename.Main(&ctx, offset, fromFlag, newName)
```

**Warning:** Force mode may produce incorrect code if there are legitimate conflicts.

## Type Safety Guarantees

The rename package ensures:

1. **Scope Awareness**: Only renames identifiers in the correct scope
2. **Type Matching**: Ensures renamed identifier matches the original type
3. **Reference Tracking**: Updates all references, not just some
4. **Collision Detection**: Prevents renaming to names that would create conflicts
5. **Context Preservation**: Maintains identifier semantics

## Performance Characteristics

### Time Complexity

- Building import graph: O(n) where n = number of files
- Finding references: O(m) where m = total symbols in codebase
- Updating references: O(r) where r = number of references

### Space Complexity

- Maintains parse tree for all files: O(s) where s = total source size
- Import graph: O(p) where p = number of packages

## Limitations

- Does not work correctly with Go modules (deprecated)
- Scope limited to the Go build context
- May have issues with complex import patterns
- No support for complex template-based refactoring

## Migration Path

For modern development, migrate to **gopls**:

```bash
# Old way (deprecated)
gorename -offset file.go:#42 -to newName

# New way (recommended)
gopls rename file.go:42:0 newName
```

## Related Packages

- `golang.org/x/tools/go/loader` - Package loading and analysis
- `golang.org/x/tools/refactor` - Refactoring utilities
- `golang.org/x/tools/go/types` - Type checking
- `golang.org/x/tools/go/ast` - AST utilities

## Build Constraints

No special build constraints. Standard Go toolchain required.

## Thread Safety

The rename package is **not thread-safe**. Access must be serialized if using from multiple goroutines.

## Deprecation Notice

⚠️ **This package is deprecated and will be removed in a future version.**

**Reason:** Implementation has not worked properly since Go modules became standard.

**Recommendation:** Use [gopls](https://github.com/golang/tools/tree/master/gopls) for all modern Go refactoring needs.

## Examples

### Simple Rename

```go
package main

import (
    "go/build"
    "golang.org/x/tools/refactor/rename"
)

func main() {
    ctx := build.Default

    // Rename oldFunc to newFunc at line 42, column 5
    err := rename.Main(&ctx, "main.go:#42:5", "", "newFunc")
    if err != nil {
        panic(err)
    }
}
```

### Rename with Conflict Detection

```go
func safeRename(filename string, offset int, newName string) error {
    ctx := build.Default

    rename.Diff = true // Preview changes first
    err := rename.Main(&ctx, filename + ":#" + string(rune(offset)), "", newName)

    if err == rename.ConflictError {
        return fmt.Errorf("conflict: name %s already exists", newName)
    }
    return err
}
```

### Move Package

```go
func movePackage(oldPath, newPath string) error {
    ctx := build.Default
    return rename.Move(&ctx, oldPath, newPath, "")
}
```

## See Also

- [gorename Command](https://pkg.go.dev/golang.org/x/tools/cmd/gorename)
- [gopls - Go Language Server](https://pkg.go.dev/golang.org/x/tools/gopls)
- [Go Build Package](https://pkg.go.dev/go/build)
- [Go Parser](https://pkg.go.dev/go/parser)
