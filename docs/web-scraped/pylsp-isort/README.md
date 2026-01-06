# python-lsp-isort

Source: https://github.com/chantera/python-lsp-isort

python-lsp-isort is an [isort](https://github.com/PyCQA/isort) plugin for the [Python LSP Server](https://github.com/python-lsp/python-lsp-server) that provides automatic import sorting and formatting in compatible editors.

## Overview

isort is a Python utility to sort imports alphabetically and automatically separate them into sections. python-lsp-isort integrates this functionality into the Python Language Server Protocol (LSP), making import sorting available in any editor that supports LSP.

## Features

- **Automatic Import Sorting**: Sorts imports alphabetically and groups them by section (future, stdlib, third-party, local)
- **Document Formatting**: Integrates with the LSP document formatting protocol
- **Range Formatting**: Supports formatting specific ranges of code
- **Configuration Support**: Respects isort configuration from `pyproject.toml`, `setup.cfg`, `.isort.cfg`, and other isort config files
- **LSP Server Integration**: Works seamlessly with python-lsp-server and its plugin ecosystem

## Installation

Install python-lsp-isort in the same virtual environment as python-lsp-server:

```shell
pip install python-lsp-isort
```

### Dependencies

- `python-lsp-server`: The core LSP server
- `isort>=5.0`: Import sorting utility

### Python Version Support

Requires Python 3.7 or higher.

## Configuration

python-lsp-isort follows the [python-lsp-server configuration](https://github.com/python-lsp/python-lsp-server/#configuration) pattern.

### Configuration Keys

- **`pylsp.plugins.isort.enabled`**: Boolean to enable/disable the plugin (default: `true`)
- **`pylsp.plugins.isort.*`**: Any other key-value pairs under `pylsp.plugins.isort` are passed to `isort.settings.Config`

### Configuration Sources

Configuration can be provided through:

1. **LSP Client Settings**: Settings passed via the LSP client (e.g., editor configuration)
2. **isort Config Files**: When isort detects a config file, configurations passed via LSP are ignored:
   - `pyproject.toml` (recommended)
   - `setup.cfg`
   - `.isort.cfg`
   - `tox.ini`
   - `.editorconfig`

### Example Configuration

#### In pyproject.toml

```toml
[tool.isort]
profile = "black"
line_length = 99
multi_line_mode = 3
include_trailing_comma = true

[tool.pylsp.plugins.isort]
enabled = true
```

#### In LSP Client Settings (e.g., Neovim)

```lua
pylsp = {
  plugins = {
    isort = {
      enabled = true,
      -- isort configuration
      profile = "black",
      line_length = 99,
    }
  }
}
```

### Configuration Notes

- Any configurations passed to isort via `pylsp.plugins.isort` are **ignored** when isort detects a config file (such as `pyproject.toml`)
- Configuration searches start from the file being edited and traverse up the directory tree
- The `settings_path` configuration allows you to specify a custom directory for searching config files
- All isort settings are supported via the `pylsp.plugins.isort.*` namespace

## Usage

### Document Formatting

Most editors support formatting commands that trigger LSP document formatting:

- **VS Code**: `Ctrl+Shift+F` (Windows/Linux) or `Cmd+Shift+F` (macOS)
- **Neovim**: `:lua vim.lsp.buf.format()`
- **Vim (vim-lsp)**: `:LspDocumentFormat`

When invoked, the entire document's imports will be sorted according to isort's rules.

### Range Formatting

Format only a specific range of code (if your editor supports it):

- **VS Code**: Select code and use the format command
- **Neovim**: Use visual selection with `:lua vim.lsp.buf.format()`

## Plugin Architecture

python-lsp-isort integrates with python-lsp-server through two main hooks:

### pylsp_format_document

Formats the entire document by:
1. Running isort on the document source code
2. Comparing the result with the original
3. Returning edit ranges if changes are needed

### pylsp_format_range

Formats a specific range by:
1. Extracting the requested range from the document
2. Running isort on that text
3. Returning the formatted result for just that range

### Configuration Processing

The plugin processes configuration as follows:

1. Retrieves settings from the LSP client under `pylsp.plugins.isort`
2. Filters out the `enabled` key (internal control)
3. Passes remaining settings to `isort.Config`
4. Checks for existing isort configuration files in the target file's directory tree
5. If config file found, uses that instead of LSP settings
6. Returns formatted text using isort's code formatter

## Isort Settings Reference

For a complete list of isort configuration options, see the [isort settings reference](https://pycqa.github.io/isort/reference/isort/settings.html#config).

Common settings include:

- **profile**: Predefined configuration profiles (black, django, flask, etc.)
- **line_length**: Maximum line length (default: 79)
- **multi_line_mode**: How to format imports across multiple lines
- **include_trailing_comma**: Add trailing comma to imports
- **force_single_line**: Force each import to be on its own line
- **skip**: Modules to skip
- **skip_glob**: Glob patterns for files to skip
- **known_first_party**: Modules to treat as first-party
- **known_third_party**: Modules to treat as third-party

## Supported Editors

python-lsp-isort works with any editor that supports the Language Server Protocol and has a python-lsp-server client:

- **VS Code**: With Python extension
- **Vim**: With vim-lsp or coc.nvim
- **Neovim**: With lspconfig or Neovim's built-in LSP client
- **Emacs**: With lsp-mode or eglot
- **Sublime Text**: With LSP client
- **PyCharm/IntelliJ**: Native support (doesn't need LSP)
- **Jupyter**: With appropriate LSP support

## Development

The plugin includes development dependencies for testing and linting:

```shell
pip install python-lsp-isort[dev]
```

Development tools:
- **pytest**: Testing framework
- **ruff**: Python linter and formatter
- **mypy**: Static type checker

### Running Tests

```shell
pytest
```

### Code Quality

The project uses:
- **Ruff** for linting and formatting
- **MyPy** for type checking
- **isort** itself for import sorting (using black profile, 99 character line length)

## Troubleshooting

### Imports Not Sorting

1. **Check if plugin is enabled**: Verify `pylsp.plugins.isort.enabled` is `true`
2. **Check config conflicts**: If you have a `.isort.cfg` or `pyproject.toml` in your project, LSP settings will be ignored
3. **Check Python version**: Requires Python 3.7+
4. **Verify isort installation**: Run `python -c "import isort; print(isort.__version__)"`

### Unexpected Formatting

1. **Check isort profile**: Different profiles (black, django, etc.) format differently
2. **Check line_length**: May affect how imports are split
3. **Run isort directly**: `isort --check-only --diff your_file.py` to see what isort would do

### Configuration Not Applied

1. **LSP client settings ignored**: If a config file exists, LSP settings are ignored (this is by design)
2. **Settings path issue**: Ensure `settings_path` points to the correct directory
3. **Setting name typo**: Check against [isort settings reference](https://pycqa.github.io/isort/reference/isort/settings.html#config)

## Performance Considerations

- Import sorting is lightweight and runs quickly on most files
- Configuration file searching starts from the document's directory and traverses up
- Large projects with complex import structures process efficiently
- No caching issues due to LSP document model

## Related Projects

- **isort**: The underlying import sorting utility - https://github.com/PyCQA/isort
- **python-lsp-server**: The core LSP server - https://github.com/python-lsp/python-lsp-server
- **pylsp-flake8**: Flake8 plugin for LSP
- **pylsp-mypy**: MyPy plugin for LSP
- **python-lsp-black**: Black formatter plugin for LSP

## License

MIT License - See LICENSE file in repository

## Author

Hiroki Teranishi (teranishi.hiroki@gmail.com)

## Repository

https://github.com/chantera/python-lsp-isort

## Contributing

Contributions are welcome! Please submit issues and pull requests on GitHub.
