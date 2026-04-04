# Source: https://github.com/python-lsp/python-lsp-black

# API Reference

## Configuration Options

python-lsp-black provides the following configuration keys for the Python LSP Server:

### pylsp.plugins.black.enabled
- **Type**: boolean
- **Default**: `true`
- **Description**: Enable or disable the Black code formatter plugin.
- **Example**:
  ```json
  {
    "pylsp.plugins.black.enabled": true
  }
  ```

### pylsp.plugins.black.cache_config
- **Type**: boolean
- **Default**: `false`
- **Description**: Enable configuration caching to improve performance. When enabled, Black configuration is cached and LSP server restart is required if Black settings change.
- **Example**:
  ```json
  {
    "pylsp.plugins.black.cache_config": false
  }
  ```

### pylsp.plugins.black.line_length
- **Type**: integer
- **Default**: `88`
- **Description**: Set the maximum line length for code formatting.
- **Example**:
  ```json
  {
    "pylsp.plugins.black.line_length": 88
  }
  ```

### pylsp.plugins.black.preview
- **Type**: boolean
- **Default**: `false`
- **Description**: Enable Black's preview-style formatting (features that are experimental or not yet stable).
- **Example**:
  ```json
  {
    "pylsp.plugins.black.preview": false
  }
  ```

### pylsp.plugins.black.skip_string_normalization
- **Type**: boolean
- **Default**: `false`
- **Description**: Disable string quote normalization. When enabled, Black will not normalize quote characters in strings.
- **Example**:
  ```json
  {
    "pylsp.plugins.black.skip_string_normalization": false
  }
  ```

### pylsp.plugins.black.skip_magic_trailing_comma
- **Type**: boolean
- **Default**: `false`
- **Description**: Control trailing comma handling. When enabled, Black will not use magic trailing commas.
- **Example**:
  ```json
  {
    "pylsp.plugins.black.skip_magic_trailing_comma": false
  }
  ```

## LSP Formatting Methods

### Document Formatting

python-lsp-black integrates with the LSP document formatting protocol. When enabled, it formats entire files.

**Method**: `textDocument/formatting`

**Supported in**:
- VSCode via python-lsp-client extensions
- Vim/Neovim via coc-pyls or similar
- Emacs via lsp-pyls
- Other LSP-compatible editors

### Range Formatting

python-lsp-black supports formatting specific ranges of code within a document.

**Method**: `textDocument/rangeFormatting`

**Note**: Text selections are treated as separate Python files, so indented code blocks within functions may not format correctly if selected in isolation.

## Integration with python-lsp-server

python-lsp-black is a plugin for python-lsp-server and must be installed in the same virtual environment:

```bash
# Install python-lsp-server and python-lsp-black together
pip install python-lsp-server python-lsp-black
```

### Disabling Conflicting Formatters

If you have other formatting plugins enabled, you should disable them to avoid conflicts:

```json
{
  "pylsp.plugins.black.enabled": true,
  "pylsp.plugins.autopep8.enabled": false,
  "pylsp.plugins.yapf.enabled": false
}
```

### Configuration in Editor Settings

#### VSCode

In `.vscode/settings.json`:
```json
{
  "pylsp.plugins.black.enabled": true,
  "pylsp.plugins.black.line_length": 100
}
```

#### Vim/Neovim (with coc-pyls)

In `coc-settings.json`:
```json
{
  "pylsp.plugins.black.enabled": true,
  "pylsp.plugins.black.line_length": 100
}
```

## Behavior Notes

- **Syntactically Valid Code Only**: Black (and therefore python-lsp-black) only formats syntactically valid Python code. Incomplete or malformed code will not be formatted.
- **Configuration Files**: The plugin respects project-level `pyproject.toml` configurations for Black settings.
- **Performance**: Use `cache_config: true` for better performance in large projects, but remember to restart the LSP server when Black settings change.

## See Also

- [Black Documentation](https://black.readthedocs.io/)
- [Python LSP Server](https://github.com/python-lsp/python-lsp-server)
- [python-lsp-black GitHub Repository](https://github.com/python-lsp/python-lsp-black)
