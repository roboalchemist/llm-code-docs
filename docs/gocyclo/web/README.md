# gocyclo - Cyclomatic Complexity Analyzer for Go

## Overview

**gocyclo** is a command-line tool that measures cyclomatic complexity of functions in Go source code. Cyclomatic complexity is a code quality metric that indicates the number of linearly independent paths through a function's source code, helping identify code that needs refactoring.

The tool implements McCabe's Cyclomatic Complexity metric (also known as McCabe metric), which is a widely used code quality standard in software engineering.

## Repository

- **GitHub:** https://github.com/fzipp/gocyclo
- **Language:** Go
- **License:** BSD 3-Clause License
- **Main Topics:** code-metrics, cyclomatic-complexity, go, golang, mccabe, mccabe-metric, software-metrics

## Installation

### Via Go

Install the latest version:

```bash
go install github.com/fzipp/gocyclo/cmd/gocyclo@latest
```

This will place the `gocyclo` binary in your Go workspace's `bin` directory (typically `$GOPATH/bin` or `$HOME/go/bin`).

Ensure your PATH includes the Go bin directory:

```bash
export PATH=$PATH:$(go env GOPATH)/bin
```

## Usage

### Basic Syntax

```bash
gocyclo [options] <packages or files>
```

### Command-Line Options

#### Display Filters

- **`-over N`** - Display only functions with cyclomatic complexity exceeding `N`
  - Example: `gocyclo -over 10 ./...` shows only functions with complexity > 10

- **`-top N`** - Display the top `N` most complex functions
  - Example: `gocyclo -top 5 ./...` shows the 5 most complex functions

#### Analysis Options

- **`-avg`** - Calculate and display the average cyclomatic complexity
  - Example: `gocyclo -avg ./...` shows average complexity across all functions

- **`-avg-short`** - Display average complexity in a compact format
  - Example: `gocyclo -avg-short ./...`

#### File Filtering

- **`-ignore REGEX`** - Exclude files matching the regular expression
  - Example: `gocyclo -ignore "_test\.go$" ./...` excludes test files

#### Package Specification

- **`./...`** - Analyze the current package and all subpackages recursively

### Output Format

The standard output format is:

```
<complexity> <package> <function> <file:line:column>
```

Example output:

```
3 main main main.go:1:1
5 main processData main.go:15:1
12 main complexFunction main.go:42:1
```

## Complexity Calculation

Cyclomatic complexity is calculated using the following formula:

- **Base complexity:** 1 for any function
- **Additional complexity:** +1 for each of the following statements:
  - `if` statement
  - `for` loop
  - `while` loop (implemented as `for` in Go)
  - `case` in a `switch` statement
  - `&&` (logical AND operator)
  - `||` (logical OR operator)

### Example

```go
func Example(x int) int {
    // Base: 1
    if x > 0 {           // +1
        return x
    } else if x < 0 {    // +1
        return -x
    }
    return 0
}
// Total complexity: 3
```

## Advanced Features

### Ignore Individual Functions

Use the `//gocyclo:ignore` directive to exclude specific functions from complexity analysis:

```go
//gocyclo:ignore
func HighlyComplexFunction() {
    // This function's complexity will not be reported
}
```

### Automatic Directory Filtering

gocyclo automatically ignores:
- Directories named `vendor`
- Directories named `testdata`
- Directories beginning with `.` (e.g., `.git`, `.github`)
- Directories beginning with `_` (e.g., `_test`)

These directories are skipped during analysis without requiring explicit filters.

## Common Use Cases

### 1. Find All Complex Functions (Complexity > 10)

```bash
gocyclo -over 10 ./...
```

This helps identify functions that might benefit from refactoring due to high complexity.

### 2. Identify the Top 10 Most Complex Functions

```bash
gocyclo -top 10 ./...
```

Use this to prioritize refactoring efforts on the most problematic areas.

### 3. Calculate Project Average Complexity

```bash
gocyclo -avg ./...
```

This provides a baseline metric for your entire codebase.

### 4. Analyze Specific Package

```bash
gocyclo ./path/to/package
```

Focus on a particular package or module.

### 5. Exclude Test Files

```bash
gocyclo -ignore "_test\.go$" ./...
```

Analyze only production code and exclude test files.

### 6. CI/CD Integration

```bash
gocyclo -over 15 ./... || exit 1
```

Use in build pipelines to enforce complexity thresholds and fail the build if exceeded.

## Integration with Other Tools

### Using with golangci-lint

The `gocyclo` linter is integrated into [golangci-lint](https://golangci-lint.run/). Configure it in `.golangci.yml`:

```yaml
linters:
  enable:
    - gocyclo

linters-settings:
  gocyclo:
    min-complexity: 10  # Adjust threshold as needed
```

Run with:

```bash
golangci-lint run
```

### Output Parsing

The output format is suitable for parsing by scripts and tools:

```bash
# Extract just function names with high complexity
gocyclo -over 20 ./... | awk '{print $3}'

# Count functions with complexity > 15
gocyclo -over 15 ./... | wc -l

# Get functions from specific package
gocyclo ./mypackage | grep mypackage
```

## Version History

### v0.6.0 (June 15, 2022)

- **Breaking Change:** Removed meaningless `-total` and `-total-short` options

### v0.5.1 (April 6, 2022)

- Fixed issue where directories `.` and `..` were being skipped during analysis

### v0.5.0 (March 22, 2022)

- Improved directory filtering: now ignores `vendor`, `testdata`, and directories with names beginning with `.` or `_`

### v0.4.0 (December 19, 2021)

- Added support for method receivers with type parameters (Go 1.18+)
- Switched to more efficient `filepath.WalkDir` function for directory traversal

### v0.3.1 (October 20, 2020)

- Introduced test coverage for the project
- Fixed cyclomatic complexity calculation error for function literals

### v0.3.0 (October 17, 2020)

- Added `-avg-short` and `-total-short` output format options
- Exported `AnalyzeASTFile` function for library use
- Fixed handling of `default` cases in switch statements

### v0.2.0 (October 17, 2020)

- Added package-level support
- Introduced `gocyclo:ignore` directive for individual functions
- Added `-total` and `-ignore` command-line options
- Added function literal analysis

### v0.1.0 (October 17, 2020)

- Initial release with versioning and `go.mod` support

## Go Versions Supported

- **Minimum Go version:** Go 1.11 (for module support)
- **Latest tested:** Go 1.18+ (with type parameter support)

## Use Cases and Best Practices

### Code Quality Metrics

- **Understanding Complexity:** Higher cyclomatic complexity indicates:
  - More test cases needed for full coverage
  - Increased likelihood of bugs
  - Difficulty in maintenance and understanding

- **Refactoring Guidelines:**
  - Complexity > 10: Consider refactoring
  - Complexity > 15: Strongly recommend refactoring
  - Complexity > 20: Critical - function likely needs major restructuring

### Development Workflow

1. **Establish Baseline:** Run `gocyclo -avg ./...` to know your project's baseline
2. **Set Thresholds:** Decide acceptable complexity limits for your project
3. **Monitor in CI/CD:** Prevent complexity growth by enforcing limits in build pipeline
4. **Refactor Proactively:** Use `-top N` to identify refactoring candidates
5. **Track Progress:** Monitor average complexity over time

### Team Standards

Example `.golangci.yml` configuration for team standards:

```yaml
linters-settings:
  gocyclo:
    min-complexity: 12  # Warn above 12
```

Example pre-commit hook:

```bash
#!/bin/bash
COMPLEX=$(gocyclo -over 15 ./... | wc -l)
if [ "$COMPLEX" -gt 0 ]; then
    echo "Warning: Found $COMPLEX functions with complexity > 15"
    exit 1
fi
```

## Related Tools and Metrics

- **McCabe Cyclomatic Complexity:** Industry standard metric for code complexity
- **Cognitive Complexity:** Alternative metric focusing on understandability
- **golangci-lint:** All-in-one Go linter including gocyclo
- **GoMetaLinter:** Predecessor to golangci-lint
- **go-critic:** Additional Go code analysis tool

## Limitations

- Analyzes only syntactic complexity, not algorithmic or semantic complexity
- Function literals (anonymous functions) are analyzed but may not always reflect actual runtime complexity
- Does not account for nested complexity in some edge cases
- Complexity scores are relative and should be compared within your codebase

## Performance Considerations

- **Speed:** gocyclo is very fast and can analyze large codebases in seconds
- **Memory:** Minimal memory footprint, suitable for CI/CD pipelines
- **Parallelization:** Not built-in, but can be parallelized at the file/package level using shell scripts

## License

gocyclo is released under the **BSD 3-Clause License**, making it suitable for both open-source and commercial projects.

## Source

- **Project:** https://github.com/fzipp/gocyclo
- **Package Documentation:** https://pkg.go.dev/github.com/fzipp/gocyclo
- **Go Package Registry:** https://pkg.go.dev/github.com/fzipp/gocyclo/cmd/gocyclo
