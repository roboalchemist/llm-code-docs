# Source: https://pkg.go.dev/golang.org/x/tools

# Go Rename User Guide

Comprehensive guide to using gorename for safe identifier refactoring in Go projects.

## Getting Started

### Installation

Install gorename with the Go toolchain:

```bash
go install golang.org/x/tools/cmd/gorename@latest
```

Verify installation:

```bash
gorename -help
```

### Quick Start

The basic pattern is:

```bash
gorename -offset <file>:<byte-offset> -to <new-name>
```

Example:

```bash
gorename -offset main.go:#142 -to NewName
```

## Understanding Offsets

gorename uses byte offsets to locate identifiers. The offset format has two variants:

### Variant 1: Byte Offset

```bash
gorename -offset filename.go:#<byte-offset>
```

- Byte offset from the start of the file
- Useful for programmatic tools
- Zero-indexed

Example:
```bash
# Rename identifier at byte 142 in main.go
gorename -offset main.go:#142 -to newName
```

### Variant 2: Line and Column

```bash
gorename -offset filename.go:#<line>:<column>
```

- Line and column numbers (1-indexed)
- More human-readable
- Easier to use with editor information

Example:
```bash
# Rename identifier at line 42, column 5 in main.go
gorename -offset main.go:#42:5 -to newName
```

### Finding the Offset

Use your editor to find line and column numbers:

- **VS Code**: Position cursor on identifier, see "Ln X, Col Y" in status bar
- **Vim**: Position on identifier, press `g` then `Ctrl+G` to see position
- **Emacs**: `C-x =` displays position
- **GoLand**: Hover over identifier to see position

Or use tools to find offsets:

```bash
# Show line numbers with grep
grep -n "myFunction" main.go

# Use sed to show positions
sed -n '42p' main.go
```

## Common Renaming Tasks

### Rename a Local Variable

Local variables can be safely renamed within their scope:

```bash
# In myfile.go at line 25, column 5, rename 'x' to 'count'
gorename -offset myfile.go:#25:5 -to count

# Preview first
gorename -offset myfile.go:#25:5 -to count -diff
```

### Rename a Function

Functions can be renamed within a package. If exported, ensure all imports are updated:

```bash
# Rename myFunc to calculateValue
gorename -offset main.go:#100:6 -to calculateValue

# For exported functions, gorename updates all imports
```

### Rename a Type

Renaming types (struct, interface, custom type) updates all usages:

```bash
# Rename UserData type to User
gorename -offset types.go:#15:6 -to User

# All fields and methods are automatically renamed
```

### Rename a Method

Methods are renamed within their receiver type:

```bash
# Rename String() method to Format()
gorename -offset myfile.go:#50:6 -to Format
```

### Rename a Package

Rename a package by updating import paths:

```bash
# Rename package 'util' to 'utilities'
gorename -from "mypackage/util" -to "mypackage/utilities"

# Updates all imports: import "mypackage/utilities"
```

### Rename an Interface

Interface renames update all implementations:

```bash
# Rename Reader interface to InputReader
gorename -offset types.go:#30:6 -to InputReader

# All implementing types must satisfy new name
```

## Preview Changes Before Applying

Always preview changes on large refactorings:

```bash
# Show diffs without modifying files
gorename -offset main.go:#42:5 -to newName -diff

# Examine output carefully
# Only run without -diff if satisfied
```

### Custom Diff Command

Use a different diff tool:

```bash
# Use meld for visual diff
gorename -offset main.go:#42:5 -to newName -diff -diffcmd "meld"

# Use vimdiff
gorename -offset main.go:#42:5 -to newName -diff -diffcmd "vimdiff"
```

## Advanced Usage

### Verbose Output

Enable detailed logging:

```bash
# Show what gorename is doing
gorename -v -offset main.go:#42:5 -to newName
```

Output includes:
- Files being processed
- Conflicts detected
- Progress of analysis
- Statistics

### Force Override Conflicts

When conflicts are detected, force the rename (not recommended):

```bash
# Override conflict detection
gorename -force -offset main.go:#42:5 -to newName
```

**Warning:** Using -force may produce incorrect code. Only use if you understand the implications.

### Handling Large Codebases

For large projects, consider these strategies:

1. **Rename in stages**: Break large refactorings into smaller pieces
2. **Preview first**: Always use -diff on large changes
3. **Commit before renaming**: Ensure clean git state
4. **Test thoroughly**: Run tests after each rename

```bash
# Safe workflow for large changes
git add . && git commit -m "Before refactoring"
gorename -diff -offset file.go:#42:5 -to newName  # Preview
gorename -offset file.go:#42:5 -to newName        # Apply
go test ./...                                       # Verify
```

## Working with Modules

**Important:** gorename has limitations with Go modules.

### Module-Aware Workaround

For module-based projects, consider:

1. Using **gopls rename** instead (recommended)
2. Working with vendored code
3. Using other refactoring tools

```bash
# Recommended modern approach
gopls rename file.go:42:0 newName
```

## Integration with Editors

### VS Code

1. Right-click identifier
2. Select "Rename Symbol" or press F2
3. VS Code uses gopls (which has gorename-like functionality)
4. Enter new name
5. Confirm changes

### Vim/Neovim with gopls

```vim
" Using LSP client (e.g., coc.nvim, vim-lsp)
:call CocActionAsync('rename')

" Or with vim-go
:GoRename
```

### Emacs

```elisp
;; Using eglot
(eglot-rename <new-name>)

;; Or with go-mode
(go-rename)
```

### GoLand/IntelliJ

1. Right-click on identifier
2. Select Refactor > Rename
3. Enter new name
4. Review changes
5. Click Refactor

## Troubleshooting

### "offset: No such file or directory"

**Problem:** File path is incorrect or file doesn't exist.

**Solution:**
```bash
# Use absolute path
gorename -offset /full/path/to/file.go:#42:5 -to newName

# Verify file exists
ls -la /path/to/file.go
```

### "could not parse offset"

**Problem:** Offset format is incorrect.

**Solution:**
```bash
# Use one of these formats:
gorename -offset file.go:#142          # Byte offset
gorename -offset file.go:#42:5         # Line:Column

# Not: file.go:42:5 (missing # prefix)
```

### "no packages found"

**Problem:** Go build context cannot find packages.

**Solution:**
```bash
# Ensure you're in a Go project directory
pwd
ls go.mod

# Check go.mod is valid
go mod tidy

# Try again
gorename -offset main.go:#42:5 -to newName
```

### "Conflict: name XYZ already exists"

**Problem:** New name collides with existing identifier.

**Solution:**
```bash
# Use -diff to see the conflict
gorename -diff -offset main.go:#42:5 -to newName

# Choose a different name
gorename -offset main.go:#42:5 -to differentName

# Or use -force (not recommended)
gorename -force -offset main.go:#42:5 -to newName
```

### "identifier not found"

**Problem:** Identifier at specified offset not found.

**Solution:**
```bash
# Verify position with editor
# Show context around offset
sed -n '40,45p' main.go

# Use correct offset
gorename -offset main.go:#42:5 -to newName

# Consider using gopls instead for easier location
```

## Best Practices

### 1. Always Preview Large Changes

```bash
gorename -diff -offset main.go:#42:5 -to newName | less
```

### 2. Commit Before Refactoring

```bash
git add .
git commit -m "Checkpoint: before gorename refactoring"
gorename -offset main.go:#42:5 -to newName
```

### 3. Run Tests After Refactoring

```bash
gorename -offset main.go:#42:5 -to newName
go test ./...
go vet ./...
```

### 4. Use Version Control to Undo

```bash
# If something goes wrong:
git checkout .

# Or review changes before committing:
git status
git diff
```

### 5. Rename Incrementally

Don't rename many things at once. Handle one identifier at a time.

```bash
# Good: one at a time
gorename -offset file1.go:#10:5 -to newName1
gorename -offset file2.go:#20:5 -to newName2

# Avoid: trying to rename multiple at once
# (gorename handles one at a time anyway)
```

### 6. Document Renames in Commit Messages

```bash
git commit -m "Refactor: rename calculateTotal to computeTotal

- Renamed function for clarity
- Updated all 12 call sites
- All tests passing"
```

## Migrating to gopls

For new projects or when updating, use gopls instead:

### Command Line

```bash
# Modern way (recommended)
gopls rename -w file.go:42:0 newName
```

### Editor Integration

Most modern editors automatically use gopls for rename:
- VS Code: F2
- Vim/Neovim: LSP rename
- Emacs: eglot-rename
- GoLand: Refactor > Rename

## Performance Tips

1. **Smaller scope**: Rename within single file/package when possible
2. **During development**: Do refactoring during active development, not at end
3. **Parallel processing**: Let gorename process multiple files
4. **Index cache**: First run may be slower as it builds indexes

## Related Tools

| Tool | Purpose |
|------|---------|
| gopls | Modern rename via LSP (recommended) |
| gofmt | Code formatting |
| go vet | Code analysis |
| go fix | Automatic fixes |
| goimports | Auto-import management |

## See Also

- [API Reference](API_REFERENCE.md)
- [README](README.md)
- [gopls Documentation](https://github.com/golang/tools/tree/master/gopls)
- [Go Code Review Comments](https://golang.org/doc/effective_go#names)
