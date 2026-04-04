# gogetdoc API Reference

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
  "doc": "Documentation string.
",
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

gogetdoc -pos "$file:#$offset" -json |   jq -r '.doc' | head -10
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
