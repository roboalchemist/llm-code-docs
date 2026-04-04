# Jsonnet Language Server

A **[Language Server Protocol (LSP)](https://langserver.org)** server for [Jsonnet](https://jsonnet.org).

Source: https://github.com/grafana/jsonnet-language-server

## Overview

Jsonnet Language Server is an official Grafana project that provides Language Server Protocol support for Jsonnet, enabling IDE-level features and enhanced developer experience when working with Jsonnet code.

## Features

The language server supports:

### Jump to Definition
Navigate directly to where variables, functions, and imports are defined. Supports navigation across multiple files and standard library references.

### Error/Warning Diagnostics
Real-time detection and reporting of syntax errors, type mismatches, and other issues as you type, with inline error messages in your editor.

### Linting Diagnostics
Code quality checks and best practice recommendations to help maintain clean, consistent Jsonnet code.

### Standard Library Hover and Autocomplete
Complete autocompletion suggestions for Jsonnet standard library functions and methods with hover documentation showing function signatures and descriptions.

### Formatting
Automatic code formatting with configurable style options to maintain consistent code style across your project.

## Installation

### Download Release Binary

Download the latest release binary from GitHub:
https://github.com/grafana/jsonnet-language-server/releases

### From Source

Install directly using Go:
```bash
go install github.com/grafana/jsonnet-language-server@latest
```

## Editor Integration

### Emacs
Refer to the [editor/emacs](https://github.com/grafana/jsonnet-language-server/tree/main/editor/emacs) directory in the repository.

### Vim
Refer to the [editor/vim](https://github.com/grafana/jsonnet-language-server/tree/main/editor/vim) documentation.

The LSP integration depends on your vim plugin:

- **mattn/vim-lsp-settings**: Follow the installation guide and use the `jsonnet-language-server.vim` configuration file
- **neoclide/coc.nvim**: Copy the `coc-settings.json` content to `~/.vim/coc-settings.json`
- **neovim/nvim-lspconfig**: Install the language server and configure via nvim-lspconfig with appropriate settings

### VSCode/VSCodium
Use the [Jsonnet Language Server extension](https://marketplace.visualstudio.com/items?itemName=Grafana.vscode-jsonnet) available in the marketplace.

Source: https://github.com/grafana/vscode-jsonnet

### JetBrains IDEs
Use the [Jsonnet Language Server plugin](https://plugins.jetbrains.com/plugin/18752-jsonnet-language-server) available in the JetBrains marketplace.

Source: https://github.com/zzehring/intellij-jsonnet

## Configuration

### Neovim LSPConfig Example

```lua
require'lspconfig'.jsonnet_ls.setup{
	settings = {
		ext_vars = {
			foo = 'bar',
		},
		formatting = {
			-- default values
			Indent              = 2,
			MaxBlankLines       = 2,
			StringStyle         = 'single',
			CommentStyle        = 'slash',
			PrettyFieldNames    = true,
			PadArrays           = false,
			PadObjects          = true,
			SortImports         = true,
			UseImplicitPlus     = true,
			StripEverything     = false,
			StripComments       = false,
			StripAllButComments = false,
		},
	},
}
```

### Configuration Notes

- Both Vim configurations are preset to run `jsonnet-language-server -t` with automatic support for [Tanka](https://tanka.dev/) import paths
- You may need to add `--jpath <JPATH>` additional search paths for library imports depending on your project structure
- External variables can be passed via the `ext_vars` setting
- Formatting options allow fine-grained control over code style

## External Variables

Pass external variables to the language server via the `ext_vars` setting in your editor configuration:

```lua
ext_vars = {
    foo = 'bar',
    environment = 'production',
}
```

## Formatting Options

The language server supports comprehensive formatting options:

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `Indent` | number | 2 | Number of spaces for indentation |
| `MaxBlankLines` | number | 2 | Maximum consecutive blank lines |
| `StringStyle` | string | 'single' | String quote style ('single' or 'double') |
| `CommentStyle` | string | 'slash' | Comment style ('slash' for //) |
| `PrettyFieldNames` | bool | true | Format field names for readability |
| `PadArrays` | bool | false | Add padding around array brackets |
| `PadObjects` | bool | true | Add padding around object braces |
| `SortImports` | bool | true | Automatically sort import statements |
| `UseImplicitPlus` | bool | true | Use implicit + operator |
| `StripEverything` | bool | false | Strip all whitespace/comments |
| `StripComments` | bool | false | Strip comment-only lines |
| `StripAllButComments` | bool | false | Keep only comments |

## Contributing

Contributions are welcome. When contributing:

### Commits
Individual commits should be meaningful with useful commit messages. Refer to [How to write a commit message](https://chris.beams.io/posts/git-commit/) for guidance. Contributions will be rebased before merge to ensure fast-forward merges.

### Developer Certificate of Origin (DCO)
Contributors must sign the DCO for their contributions to be accepted. See the [DCO documentation](https://github.com/probot/dco#how-it-works).

### Code Style
- Go code should be formatted with `gofmt`
- Code should be linted with [golangci-lint](https://golangci-lint.run/)

## Releases

### Nix Flake Support

A [Nix Flake](https://nixos.wiki/wiki/Flakes) is provided for installation via the Nix package manager.

On each release:
1. Update the `version` attribute with the release tag
2. Update the `vendorSha256` attribute with the checksum for the fixed output derivation

```console
cd nix
nix develop
./release <major>.<minor>.<patch>
```

You can also use Docker:

```console
docker run -it -v /tmp:/tmp -v $(pwd):/workdir -w /workdir nixos/nix
cd nix
nix develop --extra-experimental-features nix-command --extra-experimental-features flakes
./release <major>.<minor>.<patch>
```

## Resources

- **GitHub Repository**: https://github.com/grafana/jsonnet-language-server
- **Jsonnet Official Website**: https://jsonnet.org
- **Language Server Protocol**: https://langserver.org
- **Tanka**: https://tanka.dev/
- **golangci-lint**: https://golangci-lint.run/

## License

This project is provided under the MIT License. See the repository for license details.
