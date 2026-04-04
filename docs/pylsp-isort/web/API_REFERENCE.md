# python-lsp-isort API Reference

Source: https://github.com/chantera/python-lsp-isort

## Module: pylsp_isort.plugin

The main plugin module that integrates isort with python-lsp-server through LSP hooks.

### Hook Functions

#### pylsp_settings() -> Dict[str, Any]

Returns the default plugin settings for python-lsp-isort.

**Returns:**
```python
{
    "plugins": {
        "isort": {
            "enabled": True,
        },
    },
}
```

**Description:**
This hook is called by python-lsp-server during initialization to register the plugin's default configuration. The plugin is enabled by default.

---

#### pylsp_format_document(config: Config, workspace: Workspace, document: Document) -> Generator

Hook for formatting an entire document.

**Parameters:**
- `config` (pylsp.config.config.Config): LSP server configuration
- `workspace` (pylsp.workspace.Workspace): The workspace containing the document
- `document` (pylsp.workspace.Document): The document to format

**Returns:**
Generator that yields formatting results. Result format:
```python
[{
    "range": {
        "start": {"line": 0, "character": 0},
        "end": {"line": <end_line>, "character": 0}
    },
    "newText": "<formatted_source_code>"
}]
```

**Description:**
Formats the entire document using isort. This hook chains with other formatters in python-lsp-server through the plugin system. Reports progress to the LSP client as "format: isort".

---

#### pylsp_format_range(config: Config, workspace: Workspace, document: Document, range: Range) -> Generator

Hook for formatting a specific range within a document.

**Parameters:**
- `config` (pylsp.config.config.Config): LSP server configuration
- `workspace` (pylsp.workspace.Workspace): The workspace containing the document
- `document` (pylsp.workspace.Document): The document to format
- `range` (Range): The range to format
  - `start` (Position): Start position {line, character}
  - `end` (Position): End position {line, character}

**Returns:**
Generator that yields formatting results for the specified range.

**Description:**
Formats a specific range of lines within the document. Useful for formatting just the imports section or a selected range.

---

### Core Functions

#### run_isort(text: str, settings: Optional[Dict[str, Any]] = None, file_path: Optional[Union[str, bytes, os.PathLike]] = None) -> str

Runs isort formatting on the given text.

**Parameters:**
- `text` (str): The Python source code to format
- `settings` (Optional[Dict[str, Any]]): isort configuration settings. If None, defaults to empty dict.
- `file_path` (Optional[Union[str, bytes, os.PathLike]]): Path to the file being formatted. Used for searching isort config files.

**Returns:**
(str) The formatted Python source code

**Description:**
This is the core function that performs import sorting. It:
1. Builds an isort configuration from the provided settings
2. Calls `isort.code()` to format the text
3. Returns the formatted result

**Example:**
```python
from pylsp_isort.plugin import run_isort

code = """
import sys
import os
from pathlib import Path
"""

formatted = run_isort(code, settings={"profile": "black"})
print(formatted)
# Output:
# import os
# import sys
# from pathlib import Path
```

---

#### isort_config(settings: Dict[str, Any], target_path: Optional[Union[str, bytes, os.PathLike]] = None) -> isort.Config

Builds an isort configuration object from settings.

**Parameters:**
- `settings` (Dict[str, Any]): Configuration dictionary with isort settings
- `target_path` (Optional[Union[str, bytes, os.PathLike]]): Path to search for isort configuration files

**Returns:**
(isort.Config) An isort configuration object ready for use

**Description:**
This function:
1. Validates setting names against isort's recognized fields
2. Filters out unsupported settings (logs a warning)
3. Searches for existing isort config files if `target_path` is provided
4. If a config file is found, ignores passed settings (logs a message)
5. Returns an `isort.Config` instance

**Process:**
1. Extracts valid isort configuration keys from the settings dict
2. Handles the special `settings_path` key by converting file paths to directory paths
3. Checks for existing isort config files using `isort.settings._find_config()`
4. If config file found, discards all passed settings and uses file configuration instead
5. Logs debug information about the final configuration

**Config File Search Order:**
When searching from a target path, isort looks for config in this order:
1. `pyproject.toml` (with `[tool.isort]` section)
2. `setup.cfg` (with `[isort]` section)
3. `.isort.cfg`
4. `tox.ini` (with `[isort]` section)
5. `.editorconfig` (with `[*.py]` section)

**Example:**
```python
from pylsp_isort.plugin import isort_config

# With explicit settings
config = isort_config(
    settings={"profile": "black", "line_length": 99},
    target_path="/path/to/project"
)

# With settings_path
config = isort_config(
    settings={"settings_path": "/path/to/config/dir"}
)
```

---

### Type Definitions

#### Position (TypedDict)

Represents a position in a document (used in LSP).

```python
class Position(TypedDict):
    line: int        # 0-based line number
    character: int   # 0-based character position in the line
```

---

#### Range (TypedDict)

Represents a range in a document (used in LSP).

```python
class Range(TypedDict):
    start: Position   # Start of the range
    end: Position     # End of the range
```

---

### Internal Implementation Details

#### _format() Function

Internal function that handles the actual formatting logic.

**Signature:**
```python
def _format(
    outcome,
    config: Config,
    document: Document,
    range: Optional[Range] = None
) -> None
```

**Description:**
This internal function:
1. Checks if there's a previous formatting result from other formatters
2. If yes, uses that result as input
3. If no, extracts the text from the document (full or range)
4. Retrieves isort settings from the LSP configuration
5. Filters out the `enabled` key
6. Runs isort on the text
7. If changes were made, forces the formatting result into the outcome

**Process Flow:**
```
1. Check for previous formatter output → outcome.get_result()
2. If exists: use its newText
3. Else if range provided: extract lines from that range
4. Else: use full document source
5. Get isort settings from config
6. Run isort.code() on the text
7. Compare: if different, set as outcome result
```

---

## Integration with python-lsp-server

### Plugin Registration

python-lsp-isort registers as a plugin for python-lsp-server through the entry point in `pyproject.toml`:

```toml
[project.entry-points.pylsp]
isort = "pylsp_isort.plugin"
```

This tells python-lsp-server to:
1. Load the module `pylsp_isort.plugin`
2. Scan it for functions decorated with `@hookimpl`
3. Register those functions as hook implementations

### Hook Chain Execution

When a client requests document formatting:
1. python-lsp-server collects all `pylsp_format_document` implementations
2. Executes them in a chain using pytest-hookimpl
3. Each hook can modify or pass through the result
4. python-lsp-isort integrates with this chain:
   - Runs isort on the result (if any from other formatters)
   - Or runs isort on the full document (if no prior result)
   - Passes result to any subsequent formatters

This allows python-lsp-isort to work with other formatters like black or autopep8.

---

## Configuration File Detection

When `isort_config()` is called with a `target_path`:

1. **Extract directory**: If path is a file, get its parent directory
2. **Search for config**: Start from that directory and traverse up
3. **On found**: Stop searching and use that config file
4. **On not found**: Use only the passed settings

This matches isort's standard behavior and allows project-wide configuration to take precedence.

---

## Error Handling

The plugin implements graceful error handling:

### Configuration Errors
- Invalid setting names are logged as warnings but don't break execution
- Unsupported kwargs are logged but isort still runs with valid settings

### File Path Errors
- Files that can't be opened are handled by isort itself
- Path normalization handles both string and bytes paths

### Formatting Errors
- isort exceptions are not caught (they propagate to LSP client)
- This allows proper error reporting to the user

---

## Performance Notes

### Configuration Caching
- Config file searches are done per-format request
- No explicit caching (relies on file system caching)
- For large projects, consider using explicit config files

### Scope of Changes
- Only formats imports, doesn't touch other code
- Safe to run multiple times (idempotent)
- No side effects on the file system

### Memory Usage
- Text is passed as strings (not streaming)
- Works efficiently with large files (Python handles it)
- Suitable for real-time editor integration
