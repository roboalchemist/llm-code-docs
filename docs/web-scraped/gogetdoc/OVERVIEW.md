# gogetdoc Documentation

## Overview

**gogetdoc** is a command-line tool for retrieving documentation for items in Go source code. It's designed for seamless editor integration, allowing developers to quickly access documentation for symbols without leaving their development environment.

## Key Characteristics

- **Purpose**: Retrieve Go documentation for code items by filename and byte offset
- **Type**: Go command-line tool
- **License**: 3-Clause BSD
- **GitHub**: https://github.com/zmb3/gogetdoc
- **Status**: Active and maintained

## Problem It Solves

Traditional Go documentation tools (godoc, go doc, pkg.go.dev) require users to know what they're looking for. gogetdoc solves the editor integration problem by accepting a filename and offset, automatically identifying the symbol, and returning its documentation.

## Main Features

1. **Symbol-based lookup** - Specify a filename and byte offset to get documentation
2. **JSON output** - Structured output with metadata (name, import path, declaration, documentation)
3. **Unsaved file support** - Support for editor buffers not yet saved to disk
4. **Editor integration** - Used by Atom, VS Code, Vim, and Emacs plugins

## Installation

gogetdoc is a Go tool that can be installed using:

```bash
go install github.com/zmb3/gogetdoc@latest
```

## Basic Usage

Retrieve documentation for a symbol at a specific location:

```bash
gogetdoc -pos "$(go env GOROOT)/src/fmt/format.go:#2351"
```

This returns the import statement and documentation for the symbol at that position.

## JSON Output Mode

For programmatic use, enable JSON output:

```bash
gogetdoc -pos <filename>#<byte_offset> -json
```

Returns JSON object with:
- `name` - Symbol name
- `import` - Import path
- `pkg` - Package name
- `decl` - Full declaration
- `doc` - Documentation text
- `pos` - Source location

## Unsaved Files

gogetdoc supports the same archive format as `guru` for handling unsaved buffers. Editors can supply file contents via stdin using the `-modified` flag.

Archive format:
```
filename
file_size_in_bytes
file_contents
```

## Editor Integrations

Known implementations in editor plugins:

- **Atom**: go-plus (https://github.com/joefitzgerald/go-plus)
- **VS Code**: vscode-go (https://github.com/Microsoft/vscode-go)
- **Vim**: vim-go (https://github.com/fatih/vim-go)
- **Emacs**: go-mode (https://github.com/dominikh/go-mode.el)

## Use Cases

1. **IDE Documentation Lookup** - Quick inline documentation access in code editors
2. **Refactoring Tools** - Understanding code structure during refactoring
3. **Code Comprehension** - Fast lookups while reading unfamiliar code
4. **Language Server Protocol** - Integration with LSP-based editors

## Related Tools

- **godoc** - HTTP server-based documentation browser
- **go doc** - Command-line documentation tool
- **pkg.go.dev** - Web-based Go documentation repository
- **go/types** - Go's type analysis package (foundation for gogetdoc)

## Contributing

The project welcomes contributions. For:
- Small changes: Open a pull request
- Larger changes or features: Open an issue first for discussion

## Credits

Inspiration and implementation help from:
- Alan Donovan's GothamGo talk "Using go/types for Code Comprehension and Refactoring Tools"
- Fatih Arslan's dotGo 2015 talk "Tools for working with Go Code"
- Go project's go/types examples

## Source

This documentation is compiled from:
- GitHub Repository: https://github.com/zmb3/gogetdoc
- Official README: https://raw.githubusercontent.com/zmb3/gogetdoc/master/README.md
