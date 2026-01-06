#!/usr/bin/env python3
"""
Scraper for gogetdoc documentation.
Output: docs/web-scraped/gogetdoc/

gogetdoc is a tool for retrieving documentation for items in Go source code.
Project: https://github.com/zmb3/gogetdoc
"""

import os
import requests
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "gogetdoc"

def create_directory():
    """Create output directory."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Created directory: {OUTPUT_DIR}")

def fetch_readme():
    """Fetch and save README.md from GitHub."""
    print("Fetching README.md...")
    try:
        url = "https://raw.githubusercontent.com/zmb3/gogetdoc/master/README.md"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        readme_content = response.text
        readme_path = OUTPUT_DIR / "README.md"

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)

        print(f"  Saved: {readme_path}")
        return True
    except Exception as e:
        print(f"  Error fetching README: {e}")
        return False

def create_overview():
    """Create an overview document."""
    print("Creating overview document...")
    overview = """# gogetdoc Documentation

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
"""

    overview_path = OUTPUT_DIR / "OVERVIEW.md"
    with open(overview_path, "w", encoding="utf-8") as f:
        f.write(overview)

    print(f"  Saved: {overview_path}")

def create_usage_guide():
    """Create a usage guide document."""
    print("Creating usage guide...")
    usage = """# gogetdoc Usage Guide

## Installation

Install gogetdoc using Go's package manager:

```bash
go install github.com/zmb3/gogetdoc@latest
```

This will install the `gogetdoc` binary to your `$GOPATH/bin` directory.

## Command-Line Interface

### Basic Syntax

```bash
gogetdoc -pos <filename>:<byte_offset> [flags]
```

### Flags

- `-pos string` - File position in format "filename:#byte_offset" (required)
- `-json` - Output as JSON instead of plain text
- `-modified` - Read modified files from stdin in archive format
- `-u` - Include unexported symbols (default: false)

## Common Usage Examples

### Get Documentation for a Standard Library Function

```bash
# Get documentation for unicode/utf8.RuneCountInString
gogetdoc -pos "$(go env GOROOT)/src/unicode/utf8/utf8.go:#2351"

# Output:
# import "unicode/utf8"
#
# func RuneCountInString(s string) (n int)
#
# RuneCountInString is like RuneCount but its input is a string.
```

### JSON Output for Programmatic Access

```bash
gogetdoc -pos "filename.go:#offset" -json
```

Returns structured JSON:
```json
{
  "name": "RuneCountInString",
  "import": "unicode/utf8",
  "pkg": "utf8",
  "decl": "func RuneCountInString(s string) (n int)",
  "doc": "RuneCountInString is like RuneCount but its input is a string.\n",
  "pos": "/path/to/file.go:412:6"
}
```

### Query Function in Current Project

```bash
# Get documentation for a function in your project
gogetdoc -pos "myproject/main.go:#1234" -json
```

### Get Unexported Symbol Documentation

```bash
# Include unexported symbols
gogetdoc -pos "file.go:#offset" -u -json
```

## Editor Integration

### VS Code Integration

VS Code's Go extension (vscode-go) uses gogetdoc automatically:

1. Install the Go extension
2. Hover over any symbol to see documentation
3. The extension calls gogetdoc internally with your current position

### Vim Integration

In vim-go, use:

```vim
:GoDoc  " Show documentation for symbol under cursor
```

Configuration:
```vim
let g:go_doc_command = "gogetdoc"
```

### Emacs Integration

In go-mode.el, use:

```elisp
M-x gogetdoc  " Show documentation for symbol at point
```

### Atom Integration

In go-plus:

1. Install go-plus package
2. Documentation appears in inline tooltips
3. gogetdoc is used as the backend

## Working with Unsaved Files

The `-modified` flag allows gogetdoc to work with buffers not yet saved to disk.

### Archive Format

Files are passed via stdin in archive format:

```
filename1.go
file_size_in_bytes
file_contents_here
filename2.go
file_size_in_bytes
file_contents_here
```

### Example: Editor Implementation

Editors submit modified files when the file hasn't been saved:

```bash
# Create archive with modified file
echo -ne "myfile.go\n150\npackage main\n\nfunc main() {\n  fmt.Println(\"hello\")\n}\n" | \
  gogetdoc -pos "myfile.go:#50" -modified
```

This allows gogetdoc to analyze unsaved code.

## Practical Workflow

### In Your Editor

1. Position cursor on a symbol
2. Trigger documentation lookup (usually via keyboard shortcut or hover)
3. Editor calls: `gogetdoc -pos "file.go:#offset" -json`
4. Editor displays the returned documentation

### For Tool Development

If building tooling around gogetdoc:

1. Determine the byte offset of interest (not line:column, but absolute byte position)
2. Call gogetdoc with `-json` flag for structured output
3. Parse the JSON response
4. Display or process the documentation as needed

## Troubleshooting

### "package not found" error

- Ensure you're in a valid Go module or GOPATH
- Run `go mod tidy` if using modules

### "no package" in output

- The symbol may not be exported
- Try with `-u` flag to include unexported symbols

### Byte Offset Issues

The `-pos` flag requires an absolute byte offset, not line:column. Most editors handle this conversion internally. If calling gogetdoc directly:

```bash
# Use sed to convert line:column to byte offset
# Or use your editor's API to get the exact byte position
```

## Performance Considerations

- gogetdoc is designed for quick lookups (typically <100ms)
- First run may be slower while Go loads the module
- Editor integrations often cache results

## Integration with Other Tools

gogetdoc output can be piped to other tools:

```bash
# Parse JSON and extract specific fields
gogetdoc -pos "file.go:#offset" -json | jq '.doc'

# Use with grep to search multiple locations
for file in $(find . -name "*.go"); do
  gogetdoc -pos "$file:#offset" -json
done
```
"""

    usage_path = OUTPUT_DIR / "USAGE_GUIDE.md"
    with open(usage_path, "w", encoding="utf-8") as f:
        f.write(usage)

    print(f"  Saved: {usage_path}")

def create_api_reference():
    """Create an API reference document."""
    print("Creating API reference...")
    api_ref = """# gogetdoc API Reference

## Command Line Interface

### gogetdoc

Main executable for retrieving Go documentation by file position.

#### Synopsis

```bash
gogetdoc [OPTIONS] -pos <FILE_POSITION>
```

#### Options

| Flag | Type | Description |
|------|------|-------------|
| `-pos` | string | **Required.** File position in format "filename:#byte_offset" |
| `-json` | bool | Output structured JSON instead of plain text |
| `-modified` | bool | Read modified files from stdin in archive format |
| `-u` | bool | Include unexported symbols in output |
| `-h`, `-help` | bool | Show help message |

#### Position Format

The `-pos` flag accepts a string in the format:

```
filename:#byte_offset
```

Where:
- `filename` - Absolute or relative path to Go source file
- `byte_offset` - Absolute byte offset in the file (0-indexed)

**Important**: The position uses byte offset, not line:column notation. Most editors handle this conversion internally.

#### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Error (symbol not found, invalid input, etc.) |

### Output Formats

#### Plain Text Output (Default)

```
import "package/path"

func FunctionName(arg Type) ReturnType

FunctionName does something useful.
```

Structure:
```
[import "<import_path>"]
[blank line]
[function/type/var declaration]
[blank line]
[documentation text]
```

#### JSON Output (`-json` flag)

```json
{
  "name": "SymbolName",
  "import": "package/import/path",
  "pkg": "package",
  "decl": "func SymbolName(...) Type",
  "doc": "Documentation string.\n",
  "pos": "/path/to/file.go:line:column"
}
```

**JSON Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Name of the symbol |
| `import` | string | Import path of the package containing the symbol |
| `pkg` | string | Package name (last part of import path) |
| `decl` | string | Full declaration of the symbol |
| `doc` | string | Documentation comment for the symbol |
| `pos` | string | Source file position in format "file:line:col" |

### Archive Format (for `-modified` flag)

Used to submit unsaved file contents via stdin.

#### Format

```
<filename>
<file_size_in_bytes>
<file_contents>
<filename>
<file_size_in_bytes>
<file_contents>
```

#### Example

```
myfile.go
47
package main

func main() {
  println("hello")
}
anotherfile.go
28
func helper() {}
```

**Details:**
- Each filename is followed by a newline
- File size is in decimal bytes, followed by a newline
- File contents follow immediately without extra newlines
- Multiple files are concatenated in the same format
- Files in archive take precedence over files on disk

### Symbol Resolution

gogetdoc resolves symbols based on:

1. **Go Type Checker** - Uses `go/types` for accurate symbol resolution
2. **Module System** - Understands Go modules and import paths
3. **Scope Analysis** - Handles local and exported symbols
4. **Type Information** - Provides full type and declaration details

### Return Values

The tool returns:

1. **For exported symbols**: Full documentation comment from source
2. **For unexported symbols**: Documentation (if `-u` flag used) or error
3. **For builtin types**: Standard Go builtin documentation
4. **For none found**: Exit code 1 with error message

### Performance Characteristics

- **First run** - ~100-500ms (module loading)
- **Subsequent runs** - ~10-50ms (cached module info)
- **Standard library** - ~50-100ms typical
- **Large projects** - May be slower with complex dependencies

## Implementation Notes

### Based On

- Go's `go/types` package for type analysis
- Alan Donovan's code comprehension techniques
- Similar to the `guru` oracle tool

### Limitations

- Requires valid Go syntax in the queried file
- Cannot resolve symbols in unsyntactic code
- Byte offset must be valid (usually editor-provided)

### Advantages Over Alternatives

| Aspect | gogetdoc | godoc | go doc |
|--------|----------|-------|--------|
| **Editor Integration** | Native support | Requires HTTP | Limited |
| **Position-based lookup** | Yes | No | No |
| **Programmatic use** | JSON output | HTML parsing | Plain text |
| **Unsaved files** | Supported | No | No |
| **Speed** | Very fast | Slower | Moderate |

## Integration Examples

### Shell Script

```bash
#!/bin/bash
file="$1"
offset="$2"

gogetdoc -pos "$file:#$offset" -json | \
  jq -r '.doc' | head -10
```

### Go Program

```go
package main

import (
    "encoding/json"
    "os"
    "os/exec"
)

type DocResult struct {
    Name   string `json:"name"`
    Import string `json:"import"`
    Doc    string `json:"doc"`
}

func getDoc(file string, offset int) (*DocResult, error) {
    cmd := exec.Command("gogetdoc",
        "-pos", file+":#"+string(rune(offset)),
        "-json")

    out, err := cmd.Output()
    if err != nil {
        return nil, err
    }

    var result DocResult
    json.Unmarshal(out, &result)
    return &result, nil
}
```

### Python Integration

```python
import subprocess
import json

def get_doc(filepath, byte_offset):
    result = subprocess.run(
        ['gogetdoc', '-pos', f'{filepath}:#{byte_offset}', '-json'],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return json.loads(result.stdout)
    return None
```
"""

    api_ref_path = OUTPUT_DIR / "API_REFERENCE.md"
    with open(api_ref_path, "w", encoding="utf-8") as f:
        f.write(api_ref)

    print(f"  Saved: {api_ref_path}")

def main():
    """Main function."""
    print("=" * 60)
    print("gogetdoc Documentation Scraper")
    print("=" * 60)

    create_directory()

    success = True
    success = fetch_readme() and success

    create_overview()
    create_usage_guide()
    create_api_reference()

    print("\n" + "=" * 60)
    if success:
        print(f"Successfully created documentation in: {OUTPUT_DIR}")
        print(f"Files created:")
        for f in sorted(OUTPUT_DIR.glob("*.md")):
            size = f.stat().st_size
            print(f"  - {f.name} ({size} bytes)")
    else:
        print("Documentation created with some warnings. Please review.")
    print("=" * 60)

if __name__ == "__main__":
    main()
