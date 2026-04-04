# Source: https://github.com/sqs/goreturns

# goreturns Command Reference

Complete reference guide for the goreturns tool.

## Command Syntax

```
goreturns [flags] [path ...]
```

## Flags

### Output Control Flags

#### `-l` (List mode)
- **Type**: Boolean flag
- **Default**: false
- **Description**: List files whose formatting differs from goreturns's output
- **Exit Code**: Non-zero if any files differ
- **Usage**:
  ```bash
  goreturns -l *.go
  goreturns -l ./...
  ```

#### `-w` (Write mode)
- **Type**: Boolean flag
- **Default**: false
- **Description**: Write result to (source) file instead of stdout
- **Note**: Modifies files in place; use with caution
- **Usage**:
  ```bash
  goreturns -w file.go
  goreturns -w ./cmd/myapp/main.go
  ```

#### `-d` (Diff mode)
- **Type**: Boolean flag
- **Default**: false
- **Description**: Display diffs showing what changes would be made instead of rewriting files
- **Useful for**: Previewing changes before applying them
- **Usage**:
  ```bash
  goreturns -d file.go
  goreturns -d -srcdir=. main.go
  ```

### Import Management Flags

#### `-i` (Run goimports)
- **Type**: Boolean flag
- **Default**: true
- **Description**: Run goimports on the file prior to processing
- **Note**: Automatically adds missing imports and removes unused ones
- **Usage**:
  ```bash
  goreturns -i=false file.go  # Skip goimports
  goreturns file.go  # Runs goimports by default
  ```

#### `-local` (Local import prefix)
- **Type**: String value
- **Description**: Put imports beginning with this string after 3rd-party packages
- **Purpose**: Organizes imports into local and external groups
- **Usage**:
  ```bash
  goreturns -local=github.com/mycompany file.go
  goreturns -local=internal main.go
  ```

### Directory/File Flags

#### `-srcdir` (Source directory)
- **Type**: String value
- **Default**: "" (empty string - current directory)
- **Description**: Choose imports as if source code is from `dir`. When operating on a single file, dir may instead be the complete file name.
- **Purpose**: Used for import resolution and package context
- **Usage**:
  ```bash
  goreturns -srcdir=/path/to/src file.go
  goreturns -srcdir=. main.go
  goreturns -srcdir=/full/path/to/file.go file.go
  ```

### Error Reporting Flags

#### `-p` (Print errors)
- **Type**: Boolean flag
- **Default**: false
- **Description**: Print non-fatal typechecking errors to stderr
- **Useful for**: Debugging type resolution issues
- **Usage**:
  ```bash
  goreturns -p file.go 2>&1 | grep error
  goreturns -w -p file.go
  ```

#### `-e` (Report all errors)
- **Type**: Boolean flag
- **Default**: false
- **Description**: Report all errors (not just the first 10 on different lines)
- **Purpose**: See comprehensive error list instead of truncated errors
- **Usage**:
  ```bash
  goreturns -e -p file.go
  goreturns -e main.go 2>&1
  ```

### Return Processing Flags

#### `-b` (Remove bare returns)
- **Type**: Boolean flag
- **Default**: false
- **Description**: Remove bare returns (naked returns in named return functions)
- **Purpose**: Convert bare `return` statements to explicit returns
- **Example**:
  ```go
  // Before
  func Foo() (x int, err error) {
    x = 5
    return  // bare return
  }

  // After (with -b flag)
  func Foo() (x int, err error) {
    x = 5
    return x, err  // explicit return
  }
  ```
- **Usage**:
  ```bash
  goreturns -b -w file.go
  goreturns -b -d file.go
  ```

## Argument Types

### Path Arguments

goreturns accepts file and directory paths as positional arguments:

- **Single file**: `goreturns file.go`
- **Multiple files**: `goreturns file1.go file2.go file3.go`
- **Directory**: `goreturns ./cmd/` (processes all .go files recursively)
- **Pattern**: `goreturns ./...` (Go's recursive package pattern)
- **Wildcard**: `goreturns *.go` (shell-expanded pattern)
- **stdin**: `cat file.go | goreturns` (reads from standard input)

### Path Rules

- Only `.go` files are processed
- Files starting with `.` are skipped (hidden files)
- Directories are recursively traversed
- Symbolic links are resolved and followed

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success (no formatting issues with `-l`, all files processed) |
| 1 | Formatting differences found (with `-l` flag) |
| 2 | Fatal error (invalid flags, file not found, syntax error) |

## Usage Patterns

### Batch Processing

Process all Go files in a project:

```bash
# Check which files need formatting
goreturns -l ./...

# Apply formatting to all files
goreturns -w ./...

# Dry run with diffs
goreturns -d ./...
```

### CI/CD Integration

Use goreturns in continuous integration:

```bash
#!/bin/bash
# Fail if any files need formatting
if goreturns -l ./...; then
  echo "All files properly formatted"
  exit 0
else
  echo "Files need goreturns formatting"
  exit 1
fi
```

### Editor Pre-commit Hook

```bash
#!/bin/bash
# Run before committing
goreturns -w $(git diff --cached --name-only --diff-filter=ACM | grep '\.go$')
```

### Fragment Processing

Process code from stdin without a file:

```bash
# Paste code and pipe to goreturns
echo 'func Foo() (int, error) { return nil }' | goreturns
```

## Common Workflows

### Workflow 1: Preview Changes First

```bash
# 1. See what would change
goreturns -d file.go

# 2. If satisfied, apply changes
goreturns -w file.go

# 3. Verify changes
git diff file.go
```

### Workflow 2: Format All Project Files

```bash
# 1. Check status
goreturns -l ./...

# 2. Format all
goreturns -w ./...

# 3. Review changes
git diff
```

### Workflow 3: Troubleshoot Type Errors

```bash
# 1. Check with error reporting
goreturns -p -e file.go 2>&1

# 2. See what's wrong
# Review the errors and fix your code

# 3. Try again
goreturns -d file.go
```

### Workflow 4: Custom Import Organization

```bash
# With custom local imports
goreturns -local=github.com/myorg -w ./cmd/
```

## Integration Examples

### With Make

```makefile
.PHONY: fmt
fmt:
	goreturns -w ./...

.PHONY: fmt-check
fmt-check:
	! goreturns -l ./...
```

### With Git Hooks

In `.git/hooks/pre-commit`:

```bash
#!/bin/bash
CHANGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.go$')
if [ -z "$CHANGED_FILES" ]; then
  exit 0
fi

goreturns -w $CHANGED_FILES
git add $CHANGED_FILES
```

### With Docker

```dockerfile
FROM golang:1.21

RUN go install github.com/sqs/goreturns@latest

WORKDIR /app
COPY . .

RUN goreturns -w ./...
```

## Performance Notes

- Typical performance: 100-200 files per second
- goimports pass adds ~100ms per file
- Type checking may be slow on large packages
- Use `-i=false` to skip goimports if imports are already correct

## Troubleshooting

### "no such file or directory"

File doesn't exist or path is wrong:

```bash
# Check path exists
ls -la file.go

# Use correct path
goreturns ./path/to/file.go
```

### Type checking errors

Use error reporting flags:

```bash
goreturns -p -e file.go 2>&1 | head -20
```

### Changes not applied with `-w`

Make sure file is writable:

```bash
# Check permissions
ls -l file.go

# Fix permissions
chmod 644 file.go
goreturns -w file.go
```

### Import organization issues

Specify local package prefix:

```bash
goreturns -local=mypackage -w file.go
```

## See Also

- gofmt documentation: `gofmt -h`
- goimports documentation: https://pkg.go.dev/golang.org/x/tools/cmd/goimports
- Go Code Style: https://github.com/golang/go/wiki/CodeReviewComments
