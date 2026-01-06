# golangci-lint-langserver

Source: https://github.com/nametake/golangci-lint-langserver

golangci-lint-langserver is a Language Server Protocol (LSP) wrapper for [golangci-lint](https://github.com/golangci/golangci-lint), the fast linters runner for Go. It integrates golangci-lint into your editor through the LSP standard, enabling real-time linting feedback as you develop.

## Overview

golangci-lint-langserver bridges the gap between golangci-lint and LSP-compatible editors by acting as a language server. This allows editors like Neovim, VS Code, Vim, Emacs, and Helix to use golangci-lint for Go code analysis without direct integration.

## Installation

### Prerequisites

First, install [golangci-lint](https://golangci-lint.run). Follow the official installation instructions for your platform.

### Install golangci-lint-langserver

```console
go install github.com/nametake/golangci-lint-langserver@latest
```

This installs the binary to `$GOPATH/bin/golangci-lint-langserver` (typically `~/go/bin/golangci-lint-langserver`).

Ensure the binary is in your `$PATH`:

```bash
export PATH="$PATH:$(go env GOPATH)/bin"
```

## Command-line Options

```console
  -debug
        output debug log to stderr (useful for troubleshooting)

  -nolintername
        don't show a linter name in diagnostic messages
```

### Example Usage

```bash
# Enable debug output
golangci-lint-langserver -debug

# Suppress linter name in messages
golangci-lint-langserver -nolintername
```

## Configuration

golangci-lint-langserver requires golangci-lint to output JSON format. Configuration varies by editor.

### Universal Configuration Requirement

All configurations must set golangci-lint command to `initializationOptions` with `--output.json.path stdout` (or `--out-format json` for v1).

## Editor Configuration

### Neovim with nvim-lspconfig

**Requires Neovim v0.6.1 or later.**

Add this to your Neovim configuration (init.lua):

```lua
local lspconfig = require 'lspconfig'
local configs = require 'lspconfig/configs'

if not configs.golangcilsp then
	configs.golangcilsp = {
		default_config = {
			cmd = {'golangci-lint-langserver'},
			root_dir = lspconfig.util.root_pattern('.git', 'go.mod'),
			init_options = {
				command = { "golangci-lint", "run", "--output.json.path", "stdout", "--show-stats=false", "--issues-exit-code=1" }
			}
		}
	}
end

lspconfig.golangci_lint_ls.setup {
	filetypes = {'go', 'gomod'}
}
```

### Vim with vim-lsp

Add this to your `.vimrc` or `init.vim`:

```vim
augroup vim_lsp_golangci_lint_langserver
  au!
  autocmd User lsp_setup call lsp#register_server({
      \ 'name': 'golangci-lint-langserver',
      \ 'cmd': {server_info->['golangci-lint-langserver']},
      \ 'initialization_options': {'command': ['golangci-lint', 'run', '--output.json.path', 'stdout', '--show-stats=false', '--issues-exit-code=1']},
      \ 'whitelist': ['go'],
      \ })
augroup END
```

#### Using vim-lsp-settings

The [vim-lsp-settings](https://github.com/mattn/vim-lsp-settings) plugin provides an automatic installer:

```vim
" vim-lsp-settings will automatically install and configure golangci-lint-langserver
```

### Vim with coc.nvim

Add this to your `coc-settings.json` (`:CocConfig`):

```jsonc
{
  "languageserver": {
    "golangci-lint-languageserver": {
      "command": "golangci-lint-langserver",
      "filetypes": ["go"],
      "initializationOptions": {
        "command": ["golangci-lint", "run", "--output.json.path", "stdout", "--show-stats=false", "--issues-exit-code=1"]
      }
    }
  }
}
```

### Emacs with lsp-mode

Support for golangci-lint-langserver is built-in to [lsp-mode](https://github.com/emacs-lsp/lsp-mode) since late 2023.

When the `golangci-lint-langserver` executable is found in your `$PATH`, it is automatically started for Go buffers as an add-on server alongside the `gopls` language server.

No manual configuration needed - just ensure the binary is installed and in your PATH.

### Helix

Add this to your `languages.toml`:

```toml
[[language]]
name = "go"
auto-format = true
language-servers = [ "gopls", "golangci-lint-lsp" ]

[language-server.golangci-lint-lsp]
command = "golangci-lint-langserver"

[language-server.golangci-lint-lsp.config]
command = ["golangci-lint", "run", "--output.json.path", "stdout", "--show-stats=false", "--issues-exit-code=1"]
```

Project-specific configuration can be set in `.golangci.yaml` in the project root directory to enable other linters. See [golangci-lint linters documentation](https://golangci-lint.run/usage/linters/).

## golangci-lint Version Compatibility

golangci-lint-langserver supports both v1 and v2+ of golangci-lint with different command-line parameters:

### golangci-lint v2+

Use these parameters in your `initializationOptions`:

```bash
--output.json.path stdout --show-stats=false
```

### golangci-lint v1

Use this parameter instead:

```bash
--out-format json
```

Ensure your configuration uses the correct parameters for your installed version of golangci-lint.

## Usage Workflow

1. **Install Dependencies**: Install both golangci-lint and golangci-lint-langserver
2. **Configure Editor**: Add the appropriate configuration for your editor (see Editor Configuration section)
3. **Configure golangci-lint**: Create or update `.golangci.yaml` in your project root to customize linters and their settings
4. **Use in Editor**: Open Go files in your editor; diagnostics will appear automatically as you type

## Project Configuration

Create a `.golangci.yaml` file in your project root to customize linting behavior:

```yaml
linters:
  enable:
    - vet
    - golint
    - gofmt
    - goimports
    - misspell
    - ineffassign
    - unused
    - staticcheck

issues:
  exclude-rules:
    - path: _test\.go
      linters:
        - unparam
```

See [golangci-lint configuration documentation](https://golangci-lint.run/usage/configuration/) for complete options.

## Troubleshooting

### Debug Logging

Enable debug output to troubleshoot issues:

```bash
golangci-lint-langserver -debug
```

Then check your editor's LSP output logs (varies by editor).

### Common Issues

**Issue**: LSP server not starting
- **Solution**: Verify `golangci-lint-langserver` binary is in your `$PATH`
- **Solution**: Check that `golangci-lint` is installed and accessible

**Issue**: No diagnostics appearing
- **Solution**: Verify `initializationOptions` command is correctly set in your editor configuration
- **Solution**: For v2+, ensure you're using `--output.json.path stdout`, not `--out-format json`
- **Solution**: Check `.golangci.yaml` configuration is valid

**Issue**: Linter name not showing in diagnostics
- **Solution**: Use the `-nolintername` flag when starting the language server if you prefer shorter messages

## Related Projects

- [golangci-lint](https://github.com/golangci/golangci-lint) - The linter aggregator itself
- [gopls](https://github.com/golang/tools/tree/master/gopls) - Go's official language server
- [lsp-mode](https://github.com/emacs-lsp/lsp-mode) - Emacs LSP client
- [vim-lsp](https://github.com/prabirshrestha/vim-lsp) - Vim LSP client
- [vim-lsp-settings](https://github.com/mattn/vim-lsp-settings) - Automatic vim-lsp configuration

## License

See the repository for license details.

## Repository

https://github.com/nametake/golangci-lint-langserver
