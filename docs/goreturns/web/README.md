# Source: https://github.com/sqs/goreturns

# goreturns

A `gofmt`/`goimports`-like tool for Go programmers that automatically fills in Go return statements with zero values to match the function return types.

## Overview

goreturns is a tool inspired by and based on [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports). It saves time when writing Go by automatically completing incomplete return statements by adding the zero values for missing return values.

### Example

For example, the following incomplete return statement:

```go
func F() (*MyType, int, error) { return errors.New("foo") }
```

is made complete by adding `nil` and `0` returns (the zero values for `*MyType` and `int`):

```go
func F() (*MyType, int, error) { return nil, 0, errors.New("foo") }
```

This eliminates the need to manually type out all return values, especially useful when a function has multiple return types.

## Installation

### Using Go

```bash
go get -u github.com/sqs/goreturns
```

This installs the `goreturns` command in your `$GOPATH/bin` directory.

## Usage

### Basic Usage

Run goreturns on a file:

```bash
goreturns file.go
```

This will output the reformatted code to stdout.

### Flags and Options

goreturns accepts the following command-line flags (same as `gofmt`):

| Flag | Description |
|------|-------------|
| `-l` | List files whose formatting differs from goreturns's output |
| `-w` | Write result to (source) file instead of stdout |
| `-d` | Display diffs instead of rewriting files |
| `-srcdir dir` | Choose imports as if source code is from `dir`. When operating on a single file, dir may instead be the complete file name. |
| `-i` | (Default: true) Run goimports on the file prior to processing |
| `-p` | Print non-fatal typechecking errors to stderr |
| `-e` | Report all errors (not just the first 10 on different lines) |
| `-b` | Remove bare returns |
| `-local prefix` | Put imports beginning with this string after 3rd-party packages (see goimports) |

### Common Usage Examples

#### View diff of changes:

```bash
goreturns -d file.go
```

#### Modify file in place:

```bash
goreturns -w file.go
```

#### List files that need formatting:

```bash
goreturns -l *.go
```

#### View sample changes:

```bash
goreturns -d $GOPATH/github.com/sqs/goreturns/_sample/a.go
```

## Editor Integration

goreturns can be integrated into your editor's workflow as a post-save hook. Simply replace `gofmt` or `goimports` with `goreturns` in your editor's configuration.

### Example Editor Configurations

#### Vim

You can add this to your `.vimrc`:

```vim
autocmd BufWritePre *.go :silent !goreturns -w %
```

#### VS Code

In `.vscode/settings.json`:

```json
{
  "[go]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "golang.go",
    "go.formatTool": "goreturns",
    "go.useLanguageServer": true,
    "go.lintOnSave": "package"
  }
}
```

#### Emacs

Add to your Emacs config:

```lisp
(add-hook 'go-mode-hook
  (lambda ()
    (add-hook 'before-save-hook #'goreturns-before-save nil 'local)))
```

## How It Works

### Processing Flow

1. **goimports Pass**: By default (with `-i` flag), goreturns first runs `goimports` on the file to organize imports
2. **Return Analysis**: It then analyzes each function to identify incomplete return statements
3. **Zero Value Filling**: For each incomplete return, it adds the zero values for missing return types:
   - `nil` for pointer types, slices, maps, interfaces, channels
   - `0` for numeric types
   - `""` for strings
   - `false` for booleans
4. **Output**: The modified code is either written to stdout, to the file (with `-w`), or as a diff (with `-d`)

### Supported Return Types

goreturns automatically determines the zero value for:

- Pointer types: `nil`
- Slice types: `nil`
- Map types: `nil`
- Interface types: `nil`
- Channel types: `nil`
- Numeric types (int, int8, ..., uint, uint8, ..., float32, float64): `0`
- Complex types (complex64, complex128): `0`
- String type: `""`
- Boolean type: `false`
- Custom struct types: struct with zero-valued fields
- Array types: array of zero values

## Features

- **gofmt-compatible**: Uses the same command-line interface as `gofmt`
- **goimports integration**: Automatically runs `goimports` before processing
- **Type-aware**: Understands Go types and generates appropriate zero values
- **Fragment mode**: Can process code fragments via stdin
- **Error reporting**: Multiple error reporting modes for debugging
- **Bare return removal**: Optional removal of bare returns (naked returns in named return functions)

## Configuration

### Via Flags

All behavior is controlled via command-line flags (see Flags and Options section above).

### Via Editor Configuration

Most editors allow you to specify goreturns as your Go formatter. Refer to your editor's documentation for specific instructions.

## Limitations

- Only processes `return` statements that explicitly return values (handles incomplete returns)
- Works best with properly typed functions that have named or explicit return types
- Requires valid Go syntax to function correctly
- Type information must be resolvable from the code context

## License

goreturns is licensed under a BSD-style license similar to the Go standard library. See the LICENSE file in the repository for details.

## Repository

- **GitHub**: https://github.com/sqs/goreturns
- **Original Author**: Quinn Slack (@sqs)
- **Status**: Active (as of September 2025)

## Related Tools

- **goimports**: Go tool that adds missing imports and removes unused ones
- **gofmt**: Go's standard code formatter
- **golangci-lint**: Go linter aggregator
- **gopls**: Go language server

## See Also

- [Go Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments)
- [Go Standard Library - fmt package](https://pkg.go.dev/fmt)
- [golang.org/x/tools/cmd/goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports)
