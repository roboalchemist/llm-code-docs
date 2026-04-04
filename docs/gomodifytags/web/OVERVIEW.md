# gomodifytags Documentation

## Overview

**gomodifytags** is a command-line tool and Go package for modifying struct field tags in Go code. It makes it easy to add, update, remove, or transform struct tags programmatically or via editor integration.

## Key Characteristics

- **Purpose**: Add, remove, update, and transform struct field tags in Go code
- **Type**: Go command-line tool and library
- **Author**: Fatih Arslan (fatih)
- **License**: 3-Clause BSD
- **GitHub**: https://github.com/fatih/gomodifytags
- **Status**: Active and maintained
- **Latest Release**: v1.17.0 (July 2024)

## Problem It Solves

Manually editing struct tags is tedious and error-prone, especially when:
- Adding tags like `json`, `xml`, `db` to existing structs
- Changing tag values across multiple fields
- Transforming field names (snake_case to camelCase or vice versa)
- Removing tags from fields

gomodifytags automates these operations with support for transformations and editor integration.

## Main Features

1. **Add Tags** - Add new tags to struct fields with automatic value generation
2. **Remove Tags** - Remove specific tags from struct fields
3. **Modify Tags** - Update existing tag values and options
4. **Transformations** - Automatic naming conventions (snake_case, camelCase, pascalcase, lowerCamelCase)
5. **Clear Tags** - Remove all tags from fields
6. **Field Selection** - Target specific fields, lines, or entire structs
7. **Editor Integration** - Supported by vim-go, VS Code, Atom, Acme, Emacs, TextMate2
8. **Tag Options** - Add, remove, or clear tag options (e.g., omitempty)

## Installation

gomodifytags is a Go tool that can be installed using:

```bash
go install github.com/fatih/gomodifytags@latest
```

## Basic Usage

### Adding Tags

Add JSON tags to a struct:

```bash
gomodifytags -file demo.go -struct Server -add-tags json
```

### Adding Multiple Tags

Add both JSON and XML tags:

```bash
gomodifytags -file demo.go -struct Server -add-tags json,xml
```

### Transform Field Names

Use camelCase instead of the default snake_case:

```bash
gomodifytags -file demo.go -struct Server -add-tags json -transform camelcase
```

### Selecting Fields

Select by field name:

```bash
gomodifytags -file demo.go -struct Server -field Name -add-tags json
```

Select by line number:

```bash
gomodifytags -file demo.go -line 4 -add-tags json
```

Select by byte offset (useful for editors):

```bash
gomodifytags -file demo.go -offset 548 -add-tags json
```

### Removing Tags

Remove specific tags:

```bash
gomodifytags -file demo.go -struct Server -remove-tags json
```

### Modifying Tag Options

Add the omitempty option to JSON tags:

```bash
gomodifytags -file demo.go -struct Server -add-options json=omitempty
```

### Write Changes

Print results by default (dry-run). Write to file with the `-w` flag:

```bash
gomodifytags -file demo.go -struct Server -add-tags json -w
```

### Quiet Mode

Suppress output to stdout:

```bash
gomodifytags -file demo.go -struct Server -add-tags json -w --quiet
```

## Supported Transformations

- `snake_case` - Default, converts FieldName to field_name
- `camelcase` - Converts FieldName to fieldName (lowerCamelCase)
- `pascalcase` - Converts fieldName to FieldName
- `lowerCamelCase` - Same as camelcase

## Editor Integration

### vim-go

Commands:
- `:GoAddTags [tag_keys]` - Add tags to struct fields
- `:GoRemoveTags [tag_keys]` - Remove tags from struct fields

### VS Code (vscode-go)

Commands:
- `Go: Add Tags` - Opens quick menu to add tags
- `Go: Remove Tags` - Opens quick menu to remove tags

### Atom (go-plus)

Commands:
- `golang:add-tags`
- `golang:remove-tags`

### Acme (A)

Commands:
- `addtags`
- `rmtags`

### Emacs (emacs-go-tag)

Commands:
- `go-tag-add`
- `go-tag-remove`

### TextMate2

Support via TextMate2 bundle integration

## Use Cases

### REST API Development

Add JSON tags for marshaling/unmarshaling HTTP requests and responses:

```bash
gomodifytags -file models.go -struct User -add-tags json
```

### Database Mapping

Add database tags for ORM libraries like GORM:

```bash
gomodifytags -file models.go -struct User -add-tags db,gorm
```

### XML Processing

Add XML tags for XML parsing:

```bash
gomodifytags -file data.go -struct Message -add-tags xml
```

### Configuration Management

Add tags for configuration file parsing:

```bash
gomodifytags -file config.go -struct Config -add-tags yaml,env,json
```

## Command-Line Reference

### Flags

- `-file string` - Go source file to process (required)
- `-struct string` - Struct name to process
- `-field string` - Field name to process (requires -struct)
- `-line string` - Line numbers to process (e.g., "4" or "5,8")
- `-offset int` - Byte offset to process (for editors)
- `-all` - Process all structs in file
- `-add-tags string` - Comma-separated tags to add
- `-remove-tags string` - Comma-separated tags to remove
- `-add-options string` - Tag options to add (format: tag=option)
- `-remove-options string` - Tag options to remove
- `-clear-tags` - Remove all tags from fields
- `-clear-options` - Remove all tag options from fields
- `-transform string` - Transform rule for tag values (snake_case, camelcase, etc.)
- `-w` - Write changes to file (default: dry-run to stdout)
- `--quiet` - Suppress stdout output

## Library Usage

gomodifytags can be used as a Go library:

```go
import "github.com/fatih/gomodifytags"

// Parse and modify struct tags
result := gomodifytags.Apply(params)
```

Refer to the GitHub repository for detailed API documentation.

## Resources

- **GitHub Repository**: https://github.com/fatih/gomodifytags
- **Issue Tracker**: https://github.com/fatih/gomodifytags/issues
- **License**: BSD-3-Clause

## See Also

Related Go development tools:
- **godef** - Go definition finder (find where symbols are defined)
- **gogetdoc** - Documentation retriever for Go symbols
- **goreturns** - Adds missing import returns to Go source
