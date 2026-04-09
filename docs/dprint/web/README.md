# dprint Documentation

> A pluggable and configurable code formatting platform written in Rust

Source: https://dprint.dev/

dprint is a command line application that automatically formats code. It's an ultra-fast code formatter for JavaScript/TypeScript with a powerful plugin architecture supporting multiple programming languages and file types.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Configuration](#configuration)
5. [CLI Commands](#cli-commands)
6. [Plugins](#plugins)
7. [Editor Integration](#editor-integration)
8. [Advanced Usage](#advanced-usage)

## Overview

dprint is a command line application that automatically formats code. The tool can be invoked with the simple command:

```bash
dprint fmt
```

### Key Features

- **Fast Performance**: Ultra-fast code formatting due to Rust implementation and parallel processing
- **Plugin Architecture**: Extensible system with WebAssembly (WASM) and process-based plugins
- **Multi-Language Support**: Supports JavaScript, TypeScript, Python, PHP, Rust, CSS, HTML, JSON, YAML, TOML, Dockerfile, and more
- **Editor Integration**: Supports VS Code, IntelliJ, Neovim, and other editors via Language Server Protocol (LSP)
- **Format on Save**: Can be integrated into development workflows for automatic formatting
- **Configurable**: Comprehensive configuration options for fine-tuned formatting behavior

### Use Cases

1. **Editor Integration**: Format on save functionality in your development environment
2. **Command Line Usage**: Direct CLI access for formatting from the terminal
3. **CI/CD Integration**: Automated code formatting in continuous integration pipelines

## Installation

### Shell-based Installation

**Mac/Linux/WSL:**
```bash
curl -fsSL https://dprint.dev/install.sh | sh
```

**Windows PowerShell:**
```powershell
iwr https://dprint.dev/install.ps1 -useb | iex
```

### Package Managers

**Homebrew (macOS):**
```bash
brew install dprint
```

**Scoop (Windows):**
```bash
scoop install dprint
```

**npm:**
```bash
npm install dprint
# or globally
npm install -g dprint
```

**Cargo (Rust):**
```bash
cargo install --locked dprint
```

**asdf-vm:**
```bash
asdf plugin add dprint
asdf install dprint latest
```

**Arch Linux (AUR):**
```bash
paru -S dprint
```

**Python/uv:**
```bash
uv add dprint-py
```

**Deno:**
Configure as a task in `deno.json`

### Direct Download

Windows installer and precompiled binaries are available from the [GitHub releases page](https://github.com/dprint/dprint/releases).

### System Requirements

dprint is compatible with:
- macOS
- Linux
- Windows (x86_64)
- WSL environments

## Getting Started

### Quick Setup

Execute the following command in your project's root directory:

```bash
dprint init
```

This automatically generates a `dprint.json` file configured with the latest available plugins.

### Manual Setup

Alternatively, create a configuration file manually:

1. Create `dprint.json`, `dprint.jsonc`, or `.dprint.json` in your project root
2. Add plugin specifications and formatting options (see Configuration section)
3. Run `dprint fmt` to format your code

### Typical Workflow

1. **Install dprint**
2. **Run `dprint init`** to auto-generate configuration
3. **Review and customize** `dprint.json` as needed
4. **Run `dprint fmt`** to format files

## Configuration

### Configuration File

dprint uses JSON-based configuration files that specify:
1. Which plugins to activate
2. Formatting options for various file types
3. File inclusion and exclusion patterns

**File Names:**
- `dprint.json` (conventional)
- `dprint.jsonc` (with comments)
- `.dprint.json` (hidden)
- `.dprint.jsonc` (hidden with comments)

### Basic Configuration Structure

```json
{
  "extends": ["https://plugins.dprint.dev/latest/prettier-config.json"],
  "plugins": [
    "https://plugins.dprint.dev/typescript-0.91.2.wasm",
    "https://plugins.dprint.dev/json-0.19.3.wasm",
    "https://plugins.dprint.dev/markdown-0.17.3.wasm",
    "https://plugins.dprint.dev/toml-0.9.3.wasm"
  ],
  "includes": ["**/*.{ts,tsx,js,jsx,json,md,toml}"],
  "excludes": [
    "**/node_modules",
    "**/.git",
    "dist",
    "build"
  ],
  "indentWidth": 2,
  "lineWidth": 100,
  "newLineKind": "lf",
  "useTabs": false
}
```

### Configuration Properties

#### Plugin Specification

```json
{
  "plugins": [
    "https://plugins.dprint.dev/typescript-0.91.2.wasm",
    "./local-plugin.wasm"
  ]
}
```

Plugin order determines precedence when multiple plugins support the same file extension.

#### File Patterns

**Includes** (optional)
Limit formatting to specific file patterns:
```json
{
  "includes": ["**/*.{ts,js,json}"]
}
```

**Excludes**
Skip files matching these patterns (gitignore syntax):
```json
{
  "excludes": [
    "**/node_modules",
    "**/.git",
    "dist/**/*"
  ]
}
```

Gitignored files are excluded by default. Un-exclude files using negated globs:
```json
{
  "excludes": [
    "ignored-dir",
    "!ignored-dir/important-file.js"
  ]
}
```

**Associations**
Map file patterns to specific plugins:
```json
{
  "associations": {
    "**/*.custom-ext": "typescript"
  }
}
```

#### Global Options

These language-agnostic settings can be overridden per-plugin:

- **`lineWidth`**: Target line length (default: 120, may be exceeded in certain cases)
- **`indentWidth`**: Spaces per indent or tab character width (default: 2 or 4)
- **`newLineKind`**: `auto`, `crlf`, `lf`, or `system` (default: `lf`)
- **`useTabs`**: Use tabs instead of spaces (default: `false`)

#### Advanced Features

**Configuration Extension**

Extend or reference external configurations:
```json
{
  "extends": [
    "https://plugins.dprint.dev/latest/prettier-config.json",
    "./base-config.json"
  ]
}
```

**Incremental Formatting**

By default, dprint only reformats changed files. Disable with:
```json
{
  "incremental": false
}
```

**Locked Configuration**

Publishers can enforce opinionated configs by adding:
```json
{
  "locked": true
}
```

This prevents property overrides by users who extend the configuration.

**Configuration Variables**

- `${configDir}` - Current config's directory
- `${originConfigDir}` - Original config's directory (useful with extended configs)

#### Environment Variables

- **`DPRINT_CACHE_DIR`**: Override default system cache directory
- **`HTTPS_PROXY` / `HTTP_PROXY`**: Configure network proxy
- **`NO_PROXY`**: Specify no-proxy hosts
- **`DPRINT_CERT`**: Custom TLS certificate
- **`DPRINT_TLS_CA_STORE`**: TLS certificate store
- **`DPRINT_MAX_THREADS`**: Limit CPU core usage for parallelism

### Configuration Commands

CLI tools for managing configuration:

```bash
# Add plugins interactively
dprint config add

# Update plugins to latest versions
dprint config update

# Open config in designated editor
dprint config edit
```

### Custom Config Location

Specify a custom config file path:

```bash
dprint init --config path/to/dprint.json
```

Use the `--config` or `-c` flag during CLI operations:

```bash
dprint fmt --config custom-path/dprint.json
```

## CLI Commands

### Main Syntax

```
dprint <SUBCOMMAND> [OPTIONS] [--] [files]...
```

### Core Commands

#### fmt - Format Files

Format all configured files:
```bash
dprint fmt
```

Format specific file patterns:
```bash
dprint fmt **/*.js --excludes **/data
```

Format only git staged files (v0.47.0+):
```bash
dprint fmt --staged
```

Format from stdin:
```bash
dprint fmt --stdin file-path/name/extension
cat file.js | dprint fmt --stdin file.js
```

Disable incremental formatting:
```bash
dprint fmt --incremental=false
```

#### check - Verify Formatting

Report unformatted files:
```bash
dprint check
```

Show only file paths needing formatting:
```bash
dprint check --list-different
```

Stop on first failure (v0.51+):
```bash
dprint check --fail-fast
```

#### upgrade - Update Version

Update to the latest dprint version:
```bash
dprint upgrade
```

Available since v0.30.0+

#### help - Display Command Information

```bash
dprint help
dprint help fmt
dprint help check
```

### Configuration Options

Apply globally to most commands:

- **`--config <path|url>` or `-c`**: Specify custom config file
- **`--config-discovery <mode>`**: Set discovery behavior
  - `default` (default)
  - `ignore-descendants`
  - `global`
  - `false`
- **`--includes-override`**: Override config include patterns
- **`--excludes-override`**: Override config exclude patterns

Example:
```bash
dprint fmt --config /path/to/custom.json --includes-override "**/*.{ts,js}"
```

### Diagnostic Commands

Display internal information for debugging:

```bash
# Display resolved file paths that would be formatted
dprint output-file-paths

# Show internal plugin configuration
dprint output-resolved-config

# List formatting duration per file
dprint output-format-times

# Remove internal cache
dprint clear-cache
```

### Output Control

- **`--log-level <level>`**: Set verbosity
  - `silent` - No output
  - `error` - Only errors
  - `warn` - Warnings and errors
  - `info` (default) - General information
  - `debug` - Detailed debugging information

- **`--allow-no-files`**: Suppress error when no files found (v0.43+)

Example:
```bash
dprint fmt --log-level debug
dprint check --log-level silent
```

### Exit Codes

Exit codes indicate result status:

- `0` - Success
- `1-10` - Configuration or setup errors
- `11-19` - Plugin-related issues
- `20` - Files need formatting (from `check` command)

## Plugins

dprint supports a comprehensive collection of code formatting plugins, enabling support for virtually any programming language or file type.

### WebAssembly Plugins (Sandboxed)

These compile to `.wasm` files and run in a secure sandbox environment:

#### Language-Specific Formatters

- **TypeScript** - TypeScript/JavaScript formatting
- **JavaScript** - JavaScript code formatting
- **JSON** - JSON file formatting with configurable indentation
- **Markdown** - Markdown document formatting
- **TOML** - TOML configuration file formatting
- **Python (Ruff)** - Python code formatting via Ruff
- **PHP (Mago)** - PHP code formatting
- **Rust** - Rust code formatting (via Rustfmt)

#### Stylesheet Formatters

- **Malva** - CSS, SCSS, Sass, and Less stylesheets

#### Markup Formatters

- **Markup_fmt** - HTML, Vue, Svelte, Astro, Angular, Jinja, Twig, Nunjucks, and Vento templates

#### Data Format Formatters

- **Pretty GraphQL** - GraphQL query language
- **Pretty YAML** - YAML configuration files
- **Dockerfile** - Docker container files
- **Jupyter** - Jupyter notebook support

#### Multi-Language Formatters

- **Biome** - Handles JavaScript/TypeScript/JSON files
- **Oxc** - JavaScript and TypeScript support

### Process Plugins (Non-Sandboxed)

These run as separate executables and require checksums for security:

- **Prettier** - Popular JavaScript formatter (requires Prettier installed)
- **Roslyn** - C# and Visual Basic formatting (requires .NET SDK)
- **Exec** - Integration wrapper for any system-installed formatting CLI

### Plugin Usage

Add plugins to your `dprint.json`:

```json
{
  "plugins": [
    "https://plugins.dprint.dev/typescript-0.91.2.wasm",
    "https://plugins.dprint.dev/json-0.19.3.wasm",
    "https://plugins.dprint.dev/markdown-0.17.3.wasm",
    "https://plugins.dprint.dev/toml-0.9.3.wasm"
  ]
}
```

Or use a configuration shorthand:

```json
{
  "plugins": ["typescript", "json", "markdown", "toml"]
}
```

### Plugin Configuration

Override global settings per-plugin:

```json
{
  "typescript": {
    "indentWidth": 4,
    "lineWidth": 80,
    "semiColons": "prefer"
  },
  "json": {
    "indentWidth": 2
  }
}
```

### Browser Compatibility

WebAssembly plugins can be utilized in:
- Browser environments
- Deno runtime
- Node.js environment

Access via the dedicated JavaScript formatter library.

## Editor Integration

### Language Server Protocol (LSP)

dprint provides a Language Server Protocol interface for editor integration:

```bash
dprint lsp
```

This command starts an LSP server for code formatting support in compatible editors.

### VS Code

Install the official dprint extension from the Visual Studio Code marketplace. The extension integrates with dprint for format on save functionality.

### IntelliJ IDEs

IntelliJ IDEA, PhpStorm, WebStorm, and other JetBrains IDEs have dprint integration available through the IDE's plugin marketplace.

### Neovim

Configure dprint as an LSP client in your Neovim configuration:

```lua
-- Example Neovim setup
require('lspconfig').dprint.setup {}
```

### Other Editors

For editors supporting LSP, configure dprint as an LSP server:

```
dprint lsp
```

Refer to your editor's LSP configuration documentation.

## Advanced Usage

### Staged Files Formatting

Format only git staged files (requires git):

```bash
dprint fmt --staged
```

This is useful for pre-commit hooks:

```bash
#!/bin/bash
dprint fmt --staged
git add -u
```

### Custom Plugin Executables

Use the Exec plugin to integrate custom CLIs:

```json
{
  "plugins": [
    "https://plugins.dprint.dev/exec-0.4.0.wasm"
  ],
  "exec": {
    "commands": [
      {
        "id": "custom-formatter",
        "command": "custom-formatter",
        "args": ["--format"]
      }
    ]
  }
}
```

### Incremental Formatting

By default, dprint tracks which files have been modified and only reformats those files. For a clean run:

```bash
dprint fmt --incremental=false
```

### Cache Management

dprint stores cached information in the system user's cache directory. Clear the cache with:

```bash
dprint clear-cache
```

### Performance Optimization

Control parallelism using the environment variable:

```bash
DPRINT_MAX_THREADS=4 dprint fmt
```

This limits CPU core usage for systems with resource constraints.

### stdin/stdout Processing

Process code via stdin and stdout:

```bash
cat file.js | dprint fmt --stdin file.js > formatted.js
```

Specify the file extension or path:

```bash
echo 'const x=1;' | dprint fmt --stdin test.js
```

### Output File Paths

View all files that would be formatted:

```bash
dprint output-file-paths
```

### Formatting Performance Analysis

Analyze formatting times per file:

```bash
dprint output-format-times
```

Useful for identifying slow formatting operations.

### Configuration Inspection

View the resolved configuration used:

```bash
dprint output-resolved-config
```

Helpful for debugging configuration issues.

## Integration Examples

### GitHub Actions

```yaml
name: Format Check

on: [push, pull_request]

jobs:
  format:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm install -g dprint
      - run: dprint check
```

### Pre-commit Hook

```bash
#!/bin/bash
dprint fmt --staged
if [ $? -ne 0 ]; then
  echo "dprint formatting failed"
  exit 1
fi
git add -u
```

### npm Scripts

```json
{
  "scripts": {
    "format": "dprint fmt",
    "format:check": "dprint check",
    "format:stdin": "dprint fmt --stdin"
  }
}
```

## Troubleshooting

### No Files Found

Ensure your `includes` and `excludes` patterns are correct:

```bash
dprint output-file-paths
```

### Plugin Download Issues

Check network connectivity and proxy settings:

```bash
HTTPS_PROXY=http://proxy:port dprint fmt
```

### Cache Issues

Clear the cache if experiencing unexpected behavior:

```bash
dprint clear-cache
```

### Performance Issues

Limit thread usage for slower systems:

```bash
DPRINT_MAX_THREADS=2 dprint fmt
```

## Related Resources

- **GitHub Repository**: https://github.com/dprint/dprint
- **Official Website**: https://dprint.dev/
- **Plugin Registry**: https://plugins.dprint.dev/
- **Community Plugins**: Available at plugin registry
- **Discord Community**: Community support and discussions
