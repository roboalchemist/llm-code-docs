# Source: https://github.com/python-lsp/python-lsp-server/tree/develop/pylsp/plugins

# Python LSP Server - Plugin System Guide

This document describes the built-in plugins available in python-lsp-server.

## Available Plugins

### flake8_lint.py
Flake8 integration plugin for linting Python code with flake8.

**Configuration Keys:**
- `pylsp.plugins.flake8.enabled` - Enable/disable flake8 plugin (default: false)
- `pylsp.plugins.flake8.config` - Path to .flake8 config file
- `pylsp.plugins.flake8.exclude` - Exclude patterns
- `pylsp.plugins.flake8.extendIgnore` - Error codes to ignore
- `pylsp.plugins.flake8.extendSelect` - Error codes to select
- `pylsp.plugins.flake8.executable` - Path to flake8 executable
- `pylsp.plugins.flake8.filename` - Filename patterns to check
- `pylsp.plugins.flake8.hangClosing` - Hang closing bracket
- `pylsp.plugins.flake8.ignore` - Error codes to ignore
- `pylsp.plugins.flake8.maxComplexity` - Max cyclomatic complexity
- `pylsp.plugins.flake8.maxLineLength` - Max line length
- `pylsp.plugins.flake8.indentSize` - Indentation size
- `pylsp.plugins.flake8.perFileIgnores` - Per-file ignore rules
- `pylsp.plugins.flake8.select` - Error codes to select

### Other Built-in Plugins
- autopep8 - Auto-formatting with autopep8
- jedi - Code completion with jedi
- mccabe - McCabe complexity checking
- pycodestyle - PEP 8 style checking
- pylint - Linting with pylint
- rope - Refactoring support with rope

## Plugin Configuration

Configuration is managed via Language Server Protocol's `workspace/didChangeConfiguration` method.
Typical configuration locations:
1. `.pylsp.cfg` or `.pylsprc`
2. `setup.cfg`
3. `pyproject.toml`
4. Language server client settings

## Example Configuration

```json
{
  "pylsp": {
    "plugins": {
      "flake8": {
        "enabled": true,
        "maxLineLength": 100,
        "ignore": ["E501", "W503"]
      }
    },
    "configurationSources": ["flake8"]
  }
}
```

## Plugin Development

Plugins can be created by implementing the `PylspPlugin` interface and registering
as a setuptools entry point in the `pylsp_plugins` group.

For details, see the source code at: https://github.com/python-lsp/python-lsp-server/tree/develop/pylsp/plugins
