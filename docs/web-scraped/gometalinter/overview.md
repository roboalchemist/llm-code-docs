# Go Meta Linter (gometalinter) - Official Documentation

# Source: https://github.com/alecthomas/gometalinter

## Status: DEPRECATED

**gometalinter is deprecated and was archived on April 7, 2019.** The project maintainers recommend migrating to [golangci-lint](https://github.com/golangci/golangci-lint) as the successor tool. This documentation is provided for legacy projects still using gometalinter.

## Overview

gometalinter is a tool that **aggregates multiple Go linters into a single command-line interface**. It concurrently runs a collection of community and standard Go linting tools and normalizes their output to a consistent format, making it easier to manage code quality across projects.

The tool standardizes output from different linters to a consistent format:
```
<file>:<line>:[<column>]: <message> (<linter>)
```

## Core Features

### 1. Concurrent Execution
- Runs multiple linters in parallel for improved performance
- Significantly faster than invoking each linter individually
- Efficient resource utilization for large codebases

### 2. Standardized Output Format
- Normalizes output from different linters to a consistent, parseable format
- Makes it easier to integrate with CI/CD pipelines
- Supports multiple output formats including Checkstyle XML

### 3. Comment-Based Suppression
- Use `// nolint` directives to suppress specific linter messages
- Fine-grained control over which linters to ignore per file or line
- Helps manage false positives without disabling entire linters

### 4. Flexible Configuration
- Command-line options for quick customization
- `.gometalinter.json` configuration files for persistent settings
- Support for custom linters via `--linter=NAME:COMMAND:PATTERN` syntax

### 5. Editor Integration
- Sublime Text
- Atom
- Visual Studio Code
- GoLand/IntelliJ IDEA
- Vim/Neovim

## Installation

### Using Installation Script
```bash
curl -L https://git.io/vp6lP | sh
```

### Using Homebrew
```bash
brew tap alecthomas/homebrew-tap
brew install gometalinter
```

### From Source
```bash
go get -u gopkg.in/alecthomas/gometalinter.v1
cd $GOPATH/src/gopkg.in/alecthomas/gometalinter.v1
go install
```

## Supported Linters

### Enabled by Default (20+)
- **go vet** - The official Go static analysis tool
- **gotype** - Syntactic and semantic analysis for Go
- **deadcode** - Finds unused code
- **gocyclo** - Computes cyclomatic complexity
- **golint** - Finds style mistakes
- **errcheck** - Checks for unchecked errors
- **staticcheck** - Advanced static analysis
- **gosec** - Security issue scanner
- **misspell** - Finds commonly misspelled words
- **unconvert** - Detects unnecessary type conversions

### Available but Disabled by Default
- testify
- gofmt
- goimports
- lll (line length linter)

## Quick Start

### Basic Usage
```bash
# Lint current package
gometalinter ./...

# Lint specific package
gometalinter ./mypackage
```

### Enable Specific Linters
```bash
# Only run go vet and golint
gometalinter --disable-all --enable=vet --enable=golint ./...
```

### Suppress Specific Warnings
```go
// nolint
var unusedVariable string

// nolint: misspell
// This is a commond example (intentional misspelling)
```

### Configure Output
```bash
# Show Checkstyle XML output (for Jenkins/CI)
gometalinter --checkstyle ./...

# Show warnings and errors
gometalinter --severity=warning ./...
```

## Configuration File

Create `.gometalinter.json` in your project root:

```json
{
  "linters": {
    "vet": {
      "command": "go vet"
    }
  },
  "enable": ["vet", "gotype", "golint"],
  "disable": ["lll", "testify"],
  "severity": "warning",
  "checkstyle": false,
  "deadline": "1m"
}
```

### Configuration Options
- **linters** - Define custom linters with command and error pattern
- **enable** - List of enabled linters
- **disable** - List of disabled linters
- **severity** - Minimum severity level: "error" (default), "warning"
- **checkstyle** - Output Checkstyle XML format
- **deadline** - Maximum time to run all linters (e.g., "5s", "1m")
- **errors** - Pattern to match error messages
- **warnings** - Pattern to match warning messages

## Custom Linters

Add custom linters using the command-line or configuration file:

```bash
# Command-line syntax
gometalinter --linter="my-linter:COMMAND:PATTERN" ./...
```

Example pattern for matching `file:line: message` format:
```
^(?P<path>.*?\.go):(?P<line>\d+):\s*(?P<message>.*)$
```

## CI/CD Integration

### Jenkins / Checkstyle Plugin
```bash
gometalinter --checkstyle ./... > checkstyle-report.xml
```

### GitLab CI
```yaml
lint:
  script:
    - gometalinter ./...
```

### GitHub Actions
```yaml
- name: Run gometalinter
  run: gometalinter ./...
```

## Editor Plugins

### VS Code
Install the "Go" extension by Google, which includes gometalinter support.

### Vim/Neovim
Use vim-go plugin with gometalinter support:
```vim
let g:go_metalinter_enabled = ['vet', 'golint', 'errcheck']
```

### Sublime Text
Install GoSublime or GoTools packages with gometalinter integration.

## Common Issues and Solutions

### Linter Not Found
**Issue**: "linter X not found"
**Solution**: Install the missing linter or ensure it's in your `$PATH`

### Timeout Errors
**Issue**: "deadline exceeded"
**Solution**: Increase deadline with `--deadline=2m` or disable slow linters

### False Positives
**Issue**: Warnings that aren't real problems
**Solution**: Use `// nolint` comment directive to suppress specific warnings

## Migration Guide (to golangci-lint)

Since gometalinter is deprecated, projects should migrate to **golangci-lint**:

### Key Differences
- golangci-lint is actively maintained and faster
- Better performance and lower memory usage
- More linters and better integration with modern Go tools
- Configuration format: `.golangci.yml` instead of `.gometalinter.json`

### Migration Steps
1. Install golangci-lint: `brew install golangci-lint`
2. Convert configuration from `.gometalinter.json` to `.golangci.yml`
3. Update CI/CD pipelines to use `golangci-lint run ./...`
4. Test to ensure similar linter coverage

### Basic golangci-lint Equivalent
```yaml
# .golangci.yml
linters:
  enable:
    - vet
    - golint
    - errcheck
    - staticcheck
    - gosec
    - misspell
    - unconvert
```

## API and Programmatic Usage

gometalinter can be used as a library in Go programs:

```go
import "gopkg.in/alecthomas/gometalinter.v1"

// Configure and run linters
config := gometalinter.NewConfig()
config.Linters = []string{"vet", "golint"}
results, _ := gometalinter.Run([]string{"./..."}, config)

for _, result := range results {
    fmt.Printf("%s:%d: %s\n", result.Path, result.Line, result.Message)
}
```

## Performance Characteristics

- **Startup time**: ~100-500ms depending on linters enabled
- **Runtime**: Highly variable based on codebase size and linters enabled
- **Memory usage**: Moderate, scales with codebase size
- **Parallelization**: Good scalability across CPU cores

## Related Tools

- **golangci-lint** - Modern replacement, actively maintained
- **go vet** - Official static analysis tool
- **gopls** - Go Language Server with integrated linting
- **golint** - Individual style linter (now part of revive)

## References

- GitHub Repository: https://github.com/alecthomas/gometalinter
- pkg.go.dev: https://pkg.go.dev/gopkg.in/alecthomas/gometalinter.v1
- Go Linters Guide: https://blog.gopheracademy.com/advent-2016/some-tools-for-go-that-you-might-not-know-yet/
