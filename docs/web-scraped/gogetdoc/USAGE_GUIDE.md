# gogetdoc Usage Guide

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
  "doc": "RuneCountInString is like RuneCount but its input is a string.
",
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
echo -ne "myfile.go
150
package main

func main() {
  fmt.Println("hello")
}
" |   gogetdoc -pos "myfile.go:#50" -modified
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
