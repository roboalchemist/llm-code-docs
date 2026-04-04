# Source: https://github.com/opennota/check

# varcheck

**varcheck** is a Go source code analysis utility designed to identify unused global variables and constants in your Go codebase.

## Overview

varcheck is part of the opennota-check suite—a collection of Go source inspection utilities. The project provides three command-line tools for code analysis:

1. **aligncheck** - Identifies inefficiently packed structs to optimize memory usage
2. **structcheck** - Detects unused fields within struct definitions
3. **varcheck** - Finds unused global variables and constants

## Installation

Install varcheck via:

```bash
go get github.com/opennota/check/cmd/varcheck
```

## Usage

The tool accepts command-line flags:

```bash
varcheck [flags] [path]
```

### Flags

- `-e=false`: Report exported variables and constants (disabled by default)

By default, varcheck only reports unexported (private) variables and constants. Use the `-e` flag to also report exported (public) identifiers.

## Example

When analyzing the `image/jpeg` package, varcheck identifies unused declarations:

```
image/jpeg: /usr/lib/go/src/image/jpeg/reader.go:74:2: adobeTransformYCbCr
image/jpeg: /usr/lib/go/src/image/jpeg/reader.go:75:2: adobeTransformYCbCrK
image/jpeg: /usr/lib/go/src/image/jpeg/writer.go:54:2: quantIndexLuminance
```

The output format shows:
- **Package name**
- **File path**
- **Line and column position**
- **Unused variable or constant identifier**

## Purpose

varcheck is designed to help you:

- **Identify dead code** - Find variables and constants that are declared but never used
- **Clean up codebase** - Remove unused declarations to improve code maintainability
- **Optimize memory usage** - Eliminate unnecessary global state
- **Improve code quality** - Detect variables that may have been forgotten or left behind

## Project Status

The opennota-check repository was archived in April 2025 and is now read-only. However, the tools remain functional for analyzing Go code using Go 1.8+ versions.

## License

GPL-3.0

## Related Tools

- **aligncheck** - Part of the same opennota-check suite for detecting inefficiently packed structs
- **structcheck** - Also in opennota-check for detecting unused struct fields
- **go vet** - Built-in Go tool for detecting suspicious constructs
- **golangci-lint** - Popular meta-linter that includes varcheck integration

## Integration

varcheck can be integrated into:
- **GOMETalinter** - Meta-linter framework
- **GoReporter** - Go code quality assessment tool
- **golangci-lint** - Comprehensive linting framework
- **Continuous Integration** - Automated code analysis pipelines

## Limitations

- The opennota-check repository is archived and no longer actively maintained
- Works with Go 1.8+ versions
- Only analyzes global variables and constants (not function-level variables)
- Does not handle some complex scenarios in struct field detection
