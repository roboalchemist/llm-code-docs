# Source: https://github.com/gordonklaus/ineffassign

# ineffassign

A Go linter for detecting ineffectual assignments in Go code.

## Overview

ineffassign detects when assignments to existing variables are not used. An assignment is ineffectual if the variable assigned is not thereafter used in the code.

This tool is useful for identifying dead code and optimization opportunities in Go programs.

## Installation

Install ineffassign using Go's package manager:

```bash
go install github.com/gordonklaus/ineffassign@latest
```

## Usage

For basic usage, run the following command from the root of your project:

```bash
ineffassign ./...
```

This will analyze all packages beneath the current directory.

### Exit Codes

- **0**: No issues found
- **1**: One or more ineffectual assignments were detected
- **3**: Invalid arguments were provided

## Limitations

This tool has some intentional limitations:

- **Struct field assignments**: The tool does not consider struct field assignments. This is by design since it requires type information.
- **No false positives**: The tool is designed to never produce false positives, prioritizing precision over recall.
- **Type information**: Since the analysis does not use full type information, some cases may be missed.

The tool prioritizes accuracy and reliability - it's better to miss some cases than to report false positives.

## Integration with golangci-lint

ineffassign is integrated into golangci-lint, a popular Go linter aggregator. You can use it as part of golangci-lint's suite of linters:

```bash
golangci-lint run
```

Configuration is available via the golangci-lint configuration file.

## How It Works

ineffassign analyzes Go code using the AST (Abstract Syntax Tree) to detect patterns where:

1. A variable is assigned a value
2. The variable is never used after that assignment
3. There's no subsequent assignment that would rely on the previous one

This pattern indicates dead code that can be removed or optimized.

## Example Cases

### Detected Cases

```go
func example() {
    x := 5      // ineffectual assignment
    x = 10      // real assignment, x is used after
    fmt.Println(x)
}
```

### Missed Cases (By Design)

```go
type Person struct {
    Name string
}

func example() {
    p := Person{}
    p.Name = "John"  // Not detected (struct field assignment)
    fmt.Println(p)
}
```

## Use Cases

- Code cleanup and optimization
- Detecting unreachable code patterns
- Pre-commit hooks for Go projects
- CI/CD pipeline integration
- Finding potential bugs and dead code paths

## Repository

- **GitHub**: https://github.com/gordonklaus/ineffassign
- **Go Package**: https://pkg.go.dev/github.com/gordonklaus/ineffassign
- **Module**: github.com/gordonklaus/ineffassign
- **Go Minimum Version**: Go 1.23.0

## License

Licensed under the License file in the repository.

## Related Tools

- **golangci-lint**: https://golangci-lint.run/ - Comprehensive Go linter
- **revive**: A linter for Go code
- **golint**: Legacy Go linter (deprecated)
- **gofmt**: Code formatter for Go
