# Source: https://github.com/python-lsp/python-lsp-server/blob/develop/pylsp/plugins/flake8_lint.py

# pylsp-flake8: Flake8 Integration for Python LSP Server

## Overview

**pylsp-flake8** is the built-in flake8 plugin for **python-lsp-server** (formerly python-language-server). It integrates the popular [flake8](https://flake8.pycqa.org/) linter into your Language Server Protocol (LSP) client, enabling real-time Python code linting and diagnostics.

Unlike standalone flake8, pylsp-flake8 provides:
- Real-time linting feedback in LSP-compatible editors (VS Code, Vim, Neovim, Emacs, etc.)
- Configuration via Language Server settings (no separate .flake8 config needed)
- Integration with other python-lsp-server plugins
- Customizable error filtering and complexity thresholds

## What is flake8?

[Flake8](https://flake8.pycqa.org/) is a Python linter that combines three tools:
1. **PyCodeStyle** (PEP 8) - Style guide enforcement
2. **Pyflakes** - Logical errors detection (undefined names, unused imports)
3. **McCabe** - Cyclomatic complexity checking

## Installation

### Prerequisites

- Python 3.7 or later
- python-lsp-server installed

```bash
# Install python-lsp-server (includes flake8 plugin)
pip install python-lsp-server

# Or install with flake8 explicitly
pip install python-lsp-server[flake8]

# Flake8 and dependencies will be installed automatically
```

### Standalone Flake8 Installation

If flake8 is not installed, you can install it separately:

```bash
pip install flake8
```

## Configuration

### Enable/Disable the Plugin

By default, flake8 is disabled in python-lsp-server (pycodestyle is enabled instead). To enable flake8:

**VS Code example (.vscode/settings.json):**
```json
{
  "pylsp": {
    "plugins": {
      "flake8": {
        "enabled": true
      },
      "pycodestyle": {
        "enabled": false
      }
    }
  }
}
```

**Neovim/Vim example (via nvim-lspconfig or vim-lsp):**
```lua
-- lua configuration
require('lspconfig').pylsp.setup{
  settings = {
    pylsp = {
      plugins = {
        flake8 = { enabled = true },
        pycodestyle = { enabled = false }
      }
    }
  }
}
```

### Configuration Options

All flake8 plugin settings are under `pylsp.plugins.flake8.*`:

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `enabled` | boolean | `false` | Enable/disable the flake8 plugin |
| `config` | string | `null` | Path to .flake8, setup.cfg, or tox.ini config file |
| `ignore` | array | `[]` | Error codes to ignore (e.g., `["E501", "W503"]`) |
| `select` | array | `null` | Only check these error codes (whitelist) |
| `extendIgnore` | array | `[]` | Additional codes to ignore (appended to `ignore`) |
| `extendSelect` | array | `[]` | Additional codes to select (appended to `select`) |
| `exclude` | array | `[]` | Patterns to exclude from checking |
| `executable` | string | `"flake8"` | Path to flake8 executable |
| `filename` | string | `null` | Filename patterns to check |
| `maxLineLength` | integer | `null` | Maximum line length (E501) |
| `maxComplexity` | integer | `null` | Maximum cyclomatic complexity (C901) |
| `hangClosing` | boolean | `null` | Hang closing bracket in formatting |
| `indentSize` | integer | `null` | Indentation size in spaces |
| `perFileIgnores` | array | `[]` | Per-file ignore patterns (e.g., `["test_*.py:F401"]`) |

### Example Configurations

**Strict Style Checking:**
```json
{
  "pylsp": {
    "plugins": {
      "flake8": {
        "enabled": true,
        "maxLineLength": 88,
        "ignore": ["W503"]
      }
    }
  }
}
```

**Relaxed Checking (Common for Data Science):**
```json
{
  "pylsp": {
    "plugins": {
      "flake8": {
        "enabled": true,
        "maxLineLength": 120,
        "ignore": ["E501", "W503", "E703", "E231"]
      }
    }
  }
}
```

**Per-File Ignores:**
```json
{
  "pylsp": {
    "plugins": {
      "flake8": {
        "enabled": true,
        "perFileIgnores": [
          "__init__.py:F401",
          "tests/*:F841,E501"
        ]
      }
    }
  }
}
```

## Using External Configuration Files

Instead of inline settings, you can use flake8's standard config files:

### .flake8 File

```ini
[flake8]
max-line-length = 100
exclude = .git,__pycache__,build,dist
ignore = E501,W503
```

### setup.cfg File

```ini
[flake8]
max-line-length = 100
exclude = .git,__pycache__,build,dist
ignore = E501,W503
```

### pyproject.toml File

```toml
[tool.flake8]
max-line-length = 100
exclude = [".git", "__pycache__", "build", "dist"]
ignore = ["E501", "W503"]
```

### Tell python-lsp-server to Use Config File

```json
{
  "pylsp": {
    "plugins": {
      "flake8": {
        "enabled": true,
        "config": "/path/to/.flake8"
      }
    },
    "configurationSources": ["flake8"]
  }
}
```

## Common Flake8 Error Codes

| Code | Tool | Description | Example |
|------|------|-------------|---------|
| **E*** | pycodestyle | Style issues | E501 (line too long) |
| **W*** | pycodestyle | Warnings | W503 (line break before binary operator) |
| **F*** | pyflakes | Undefined/unused names | F401 (unused import) |
| **C901** | mccabe | Complexity too high | Function has complexity > threshold |

### Common Ignores

- **E501** - Line too long (conflicts with formatting tools like Black)
- **W503** - Line break before binary operator (PEP 8 opinion changed)
- **E203** - Whitespace before ':' (conflicts with Black)
- **F401** - Unused imports in `__init__.py` files
- **E731** - Lambda assignment (sometimes intentional)

## Usage in Different Editors

### VS Code

Install the **Pylance** extension or **Python** extension with LSP support:

```json
{
  "python.linting.enabled": true,
  "python.linting.lspNotebookCellExecutionOrder": ["python"],
  "[python]": {
    "defaultInterpreterPath": "${workspaceFolder}/venv/bin/python"
  },
  "pylsp": {
    "plugins": {
      "flake8": {
        "enabled": true
      }
    }
  }
}
```

### Neovim

Use **nvim-lspconfig** with python-lsp-server:

```lua
require('lspconfig').pylsp.setup {
  settings = {
    pylsp = {
      plugins = {
        flake8 = { enabled = true }
      }
    }
  }
}
```

### Vim

Use **vim-lsp** or **coc-nvim**:

```vim
" .vimrc - configure via language server initialization
let g:lsp_settings = {
  \ 'pylsp-all': {
  \   'workspace_config': {
  \     'pylsp': {
  \       'plugins': {
  \         'flake8': { 'enabled': 1 }
  \       }
  \     }
  \   }
  \ }
```

### Emacs

Use **lsp-mode** with **lsp-pylsp**:

```elisp
(use-package lsp-pylsp
  :ensure t
  :config
  (setq lsp-pylsp-plugins-flake8-enabled t))
```

## Troubleshooting

### Flake8 Plugin Not Working

1. **Check if enabled:**
   ```json
   { "pylsp": { "plugins": { "flake8": { "enabled": true } } } }
   ```

2. **Verify flake8 is installed:**
   ```bash
   python -m flake8 --version
   ```

3. **Check if pycodestyle is disabled** (they conflict):
   ```json
   { "pylsp": { "plugins": { "pycodestyle": { "enabled": false } } } }
   ```

4. **Verify LSP server is using correct Python:**
   ```bash
   # Check which python flake8 uses
   which flake8
   flake8 --version
   ```

### Missing Diagnostic Messages

- Check `.flake8` or `setup.cfg` doesn't exclude your file
- Verify error code is not in `ignore` list
- Check file extension is `.py` or matches `filename` pattern

### Performance Issues

- Large `maxComplexity` threshold reduces overhead
- Use `exclude` to skip large directories
- Consider using per-file ignores for test files

## Integration with Other Tools

### Combining with Black (Code Formatter)

Black and flake8 have some conflicting rules:

```json
{
  "pylsp": {
    "plugins": {
      "flake8": {
        "enabled": true,
        "maxLineLength": 88,
        "ignore": ["E501", "W503", "E203"]
      },
      "autopep8": {
        "enabled": false
      },
      "yapf": {
        "enabled": false
      }
    }
  }
}
```

### Combining with Pylint

Both flake8 and pylint can be enabled for comprehensive linting:

```json
{
  "pylsp": {
    "plugins": {
      "flake8": {
        "enabled": true
      },
      "pylint": {
        "enabled": true
      }
    }
  }
}
```

### Combining with isort (Import Sorter)

flake8 can check import order when combined with isort plugin:

```json
{
  "pylsp": {
    "plugins": {
      "flake8": {
        "enabled": true,
        "ignore": ["F401"]
      },
      "isort": {
        "enabled": true
      }
    }
  }
}
```

## Related Documentation

- **[python-lsp-server Repository](https://github.com/python-lsp/python-lsp-server)** - Main project
- **[flake8 Official Documentation](https://flake8.pycqa.org/)** - Complete flake8 reference
- **[PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)** - Python style conventions
- **[CONFIGURATION.md](./CONFIGURATION.md)** - Full python-lsp-server plugin configuration

## See Also

- **[pycodestyle plugin](./CONFIGURATION.md)** - Alternative PEP 8 checker
- **[pylint plugin](./CONFIGURATION.md)** - More comprehensive static analysis
- **[autopep8 plugin](./CONFIGURATION.md)** - Auto-formatting

## Version Information

- **python-lsp-server**: Maintains flake8 plugin for all recent versions
- **flake8**: Requires flake8 >= 3.0
- **Note**: pylsp-flake8 is NOT a separate package; it's built into python-lsp-server

To check your python-lsp-server version:
```bash
pip show python-lsp-server
```

To check your flake8 version:
```bash
flake8 --version
```
