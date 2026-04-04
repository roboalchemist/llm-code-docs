# pylsp-mypy

MyPy type checking plugin for the Python LSP Server.

## Overview

pylsp-mypy is a plugin for the Python LSP Server (python-lsp-server) that integrates MyPy type checking. It allows real-time type checking as you edit Python code in any LSP-compatible editor.

**Repository:** https://github.com/python-lsp/pylsp-mypy
**PyPI:** https://pypi.org/project/pylsp-mypy/

## Installation

Install pylsp-mypy into the same virtualenv as python-lsp-server:

```bash
pip install pylsp-mypy
```

### Requirements

- Python 3.9 or newer (same as MyPy)
- python-lsp-server installed
- mypy

## Features

- Real-time type checking as you type (live mode)
- Optional dmypy daemon support for improved performance
- Strict type checking mode support
- Custom MyPy command configuration
- Configuration via pyproject.toml or LSP settings
- Code actions to add `# type: ignore` comments
- Progress reporting integration
- File exclusion patterns
- Configurable follow-imports behavior
- Custom dmypy status file support

## Configuration

### Via pyproject.toml (Recommended)

```toml
[tool.pylsp-mypy]
enabled = true
live_mode = true
strict = false
exclude = ["tests/*"]
```

### Via LSP Server Configuration

Configuration can be provided through your editor's LSP configuration. The base key is `pylsp.plugins.pylsp_mypy`.

### Configuration Options

| Option | Type | Description | Default |
|--------|------|-------------|---------|
| `live_mode` | boolean | Enables type checking as you type | true |
| `dmypy` | boolean | Use dmypy daemon instead of mypy | false |
| `strict` | boolean | Enable strict type checking mode | false |
| `overrides` | array | Additional mypy command-line options | `[true]` |
| `dmypy_status_file` | string | Path to dmypy status file | `.dmypy.json` |
| `config_sub_paths` | array | Sub-paths to search for mypy config | `[]` |
| `report_progress` | boolean | Report progress to LSP client | false |
| `exclude` | array | Regular expressions for files to exclude | `[]` |
| `follow-imports` | string | MyPy follow-imports setting (`normal`, `silent`, `skip`, `error`) | `silent` |
| `mypy_command` | array | Custom command to run mypy | `[]` |
| `dmypy_command` | array | Custom command to run dmypy | `[]` |

### Example Configurations

#### Standard Configuration

```toml
[tool.pylsp-mypy]
enabled = true
live_mode = true
strict = false
exclude = ["tests/*"]
```

#### With dmypy Daemon

```toml
[tool.pylsp-mypy]
enabled = true
live_mode = false
dmypy = true
strict = false
```

#### With Command Overrides

```toml
[tool.pylsp-mypy]
enabled = true
overrides = ["--python-executable", "/home/user/venv/bin/python", true]
```

#### With Custom dmypy Status File

```toml
[tool.pylsp-mypy]
enabled = true
dmypy = true
dmypy_status_file = ".custom_dmypy_status_file.json"
```

#### With Config Sub-Paths

```toml
[tool.pylsp-mypy]
enabled = true
config_sub_paths = [".config"]
```

#### With Progress Reporting

```toml
[tool.pylsp-mypy]
enabled = true
report_progress = true
```

## Live Mode vs. dmypy Mode

### Live Mode (Default)

- Provides real-time type checking as you type
- Writes temporary files for checking unsaved changes
- Works with all editors
- Lower performance impact for typical workflows

### dmypy Mode

- Uses the dmypy daemon for improved performance
- Better for large projects and frequent type checking
- Cannot be used with live mode simultaneously
- May require additional setup and daemon management

Enable dmypy mode by setting `dmypy = true` in your configuration.

## Custom mypy/dmypy Commands

By default, pylsp-mypy uses the `mypy` and `dmypy` executables from your PATH. For advanced use cases, you can specify custom commands.

To use custom commands, set the `mypy_command` or `dmypy_command` configuration options:

```toml
[tool.pylsp-mypy]
mypy_command = ["poetry", "run", "mypy"]
```

Or with dmypy:

```toml
[tool.pylsp-mypy]
dmypy_command = ["/path/to/venv/bin/dmypy"]
```

**Security Note:** Custom commands can execute arbitrary code. This feature requires the environment variable `PYLSP_MYPY_ALLOW_DANGEROUS_CODE_EXECUTION` to be set:

```bash
export PYLSP_MYPY_ALLOW_DANGEROUS_CODE_EXECUTION=1
```

## File Exclusion

Use regular expressions to exclude files from type checking:

```toml
[tool.pylsp-mypy]
exclude = ["tests/*", "migrations/*", "venv/*"]
```

## Code Actions

pylsp-mypy provides automatic code actions to add `# type: ignore` comments for specific error codes. When you have a type error, your editor's quick fix menu should offer an option to add an ignore comment:

```python
x = "string"
y: int = x  # type: ignore[assignment]
```

## Mypy Configuration

pylsp-mypy respects mypy configuration files in the following order:

1. `mypy.ini`
2. `.mypy.ini`
3. `pyproject.toml` (with `[tool.mypy]` section)
4. `setup.cfg` (with `[mypy]` section)
5. User's home directory: `~/.mypy.ini` or `~/.config/mypy/config`

You can also customize where mypy looks for configuration using `config_sub_paths`:

```toml
[tool.pylsp-mypy]
config_sub_paths = [".config", ".mypy"]
```

## Development

### Building and Testing

Install development dependencies:

```bash
pip install -r requirements.txt
```

### Code Formatting

The project uses:

- **black** for code formatting
- **isort** for import sorting
- **pre-commit** for automated hooks

Install pre-commit hooks:

```bash
pre-commit install
```

### Code Quality

- RST linting via pre-commit hook
- rstcheck in GitHub workflows
- Type checking with mypy

## Troubleshooting

### Live Mode Not Working

Live mode creates temporary files to check unsaved code. Ensure:
- The workspace directory is writable
- Temporary file creation is not blocked by antivirus software
- You have sufficient disk space

### dmypy Daemon Issues

If dmypy daemon becomes unresponsive:

```bash
# Kill the daemon manually
dmypy kill --status-file .dmypy.json
```

Or set up automatic daemon restart in your configuration.

### Type Errors Not Showing

- Verify pylsp-mypy is enabled in your editor configuration
- Check that mypy is installed: `mypy --version`
- Verify the Python file has proper syntax
- Check editor logs for pylsp-mypy error messages

### Custom Command Not Working

When using `mypy_command` or `dmypy_command`:

- Set `PYLSP_MYPY_ALLOW_DANGEROUS_CODE_EXECUTION=1`
- Verify the command is executable: `which mypy`
- Test the command manually outside of LSP

## Performance Tips

1. **Use dmypy for large projects:** Significantly faster incremental checking
2. **Configure follow-imports wisely:** Use `silent` to speed up checking
3. **Exclude test directories:** Reduces type checking overhead
4. **Use strict mode selectively:** Only for critical modules

## Integration with Editors

pylsp-mypy works with any editor that supports LSP:

- **VS Code** with Python LSP server extension
- **Vim** with vim-lsp or coc-lsp
- **Emacs** with lsp-mode
- **Sublime Text** with LSP package

Refer to your editor's documentation for LSP configuration.

## License

MIT License

## See Also

- [python-lsp-server](https://github.com/python-lsp/python-lsp-server)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [MyPy GitHub](https://github.com/python/mypy)
- [LSP Specification](https://microsoft.github.io/language-server-protocol/)
