# Installation and Setup Guide

Source: https://github.com/sourcegraph/javascript-typescript-langserver

## Installation Methods

### npm Global Installation

Install the language server globally to use with multiple projects:

```bash
npm install -g javascript-typescript-langserver
```

Then run:

```bash
language-server
```

### npm Project Installation

Install as a local development dependency:

```bash
npm install --save-dev javascript-typescript-langserver
```

Add to your `package.json` scripts:

```json
{
  "scripts": {
    "lsp": "node node_modules/.bin/language-server"
  }
}
```

Then run:

```bash
npm run lsp
```

### From Source

Clone and build from the GitHub repository:

```bash
git clone https://github.com/sourcegraph/javascript-typescript-langserver.git
cd javascript-typescript-langserver
npm install
npm run build
node lib/language-server
```

## Requirements

- **Node.js**: >= 6.0.0
- **npm**: any recent version
- **Disk space**: ~200MB for dependencies and build artifacts

## Build from Source

### Prerequisites

- Git
- Node.js >= 6.0.0
- npm or yarn

### Build Steps

```bash
# Clone the repository
git clone https://github.com/sourcegraph/javascript-typescript-langserver.git
cd javascript-typescript-langserver

# Install dependencies
npm install

# Compile TypeScript to JavaScript
npm run build

# Verify the build
ls -la lib/
```

### Watch Mode (for Development)

For continuous compilation during development:

```bash
npm run watch
```

This will recompile on any changes to source files.

## Running the Server

### STDIO Mode

The most common way to run the server is over standard input/output (STDIO):

```bash
language-server
```

or from source:

```bash
node lib/language-server-stdio
```

The server will:
1. Read LSP messages from stdin
2. Process requests
3. Write responses to stdout
4. Write diagnostics and notifications as JSON-RPC messages

### TCP Mode

For networking scenarios, run the server on a TCP port:

```bash
language-server --port 2089
```

or from source:

```bash
node lib/language-server --port 2089
```

The server will listen on `localhost:2089` for TCP connections from LSP clients.

### Custom Port

Specify a different port:

```bash
language-server --port 3000
```

## Configuration

### Command Line Options

```
Options:
  -h, --help            Show help information
  -V, --version         Show version number
  -s, --strict          Enable strict mode type checking
  -p, --port [port]     TCP port to use (default: 2089)
  -c, --cluster [num]   Number of concurrent worker processes
                        (default: number of CPU cores)
  -t, --trace           Print all requests and responses
  -l, --logfile [file]  Log output to file
  -j, --enable-jaeger   Enable OpenTracing with Jaeger
```

### Examples

#### Enable Strict Mode

```bash
language-server --strict
```

#### Run on Port 3000 with Logging

```bash
language-server --port 3000 --logfile lsp.log
```

#### Use 4 Worker Processes

```bash
language-server --cluster 4
```

#### Enable Jaeger Tracing and TCP on Port 4000

```bash
language-server --port 4000 --enable-jaeger
```

#### Print All Requests and Responses

```bash
language-server --trace
```

## Integration with Editors

### Visual Studio Code

Install the `vscode-javascript-typescript` extension:

```bash
code --install-extension sourcegraph.vscode-javascript-typescript
```

Or install manually from the VS Code Marketplace.

### NeoVim

Use `LanguageClient-neovim` plugin:

```vim
" Install with vim-plug
Plug 'autozimu/LanguageClient-neovim', {
    \ 'branch': 'next',
    \ 'do': 'bash install.sh',
    \ }

" Configure for this language server
let g:LanguageClient_serverCommands = {
    \ 'javascript': ['language-server'],
    \ 'typescript': ['language-server'],
    \ }
```

### Sublime Text

Install via Package Control with the `LSP` package:

1. Install `LSP` package via Package Control
2. Configure clients in LSP settings:

```json
{
  "clients": {
    "js-ts": {
      "command": ["language-server"],
      "languages": [
        {"languageId": "javascript", "scopes": ["source.js"], "syntaxes": ["Packages/JavaScript/JavaScript.sublime-syntax"]},
        {"languageId": "typescript", "scopes": ["source.ts"], "syntaxes": ["Packages/TypeScript/TypeScript.sublime-syntax"]}
      ]
    }
  }
}
```

### Vim/Neovim with coc.nvim

Install coc-tsserver or configure with a custom LSP client:

```vim
:CocConfig
```

Add to coc-settings.json:

```json
{
  "languageserver": {
    "javascript-typescript": {
      "command": "language-server",
      "filetypes": ["javascript", "typescript", "jsx", "tsx"],
      "initializationOptions": {},
      "settings": {}
    }
  }
}
```

## Troubleshooting Installation

### Command Not Found

If `language-server` is not found after global installation:

```bash
# Check npm global installation directory
npm config get prefix

# Add to PATH if needed
export PATH="$(npm config get prefix)/bin:$PATH"
```

### Permission Errors on macOS/Linux

If you get permission errors during installation:

```bash
# Use npm with sudo (not recommended)
sudo npm install -g javascript-typescript-langserver

# Or fix npm permissions (recommended)
# See https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally
```

### TypeScript Version Conflicts

The language server includes its own bundled TypeScript version. If you have conflicts with local TypeScript:

- Ensure your project's TypeScript version is compatible
- Consider using the local `node_modules` TypeScript if available
- Check for version mismatches in `package.json`

### Build Errors on Windows

If you encounter build errors on Windows:

1. Ensure you have Visual C++ build tools installed
2. Install node-gyp globally: `npm install -g node-gyp`
3. Try rebuilding: `npm rebuild`

### Memory Issues

For large projects, increase Node.js memory:

```bash
node --max-old-space-size=4096 lib/language-server
```

## Verifying Installation

After installation, verify the server works:

```bash
# Check version
language-server --version

# Start the server
language-server --port 2089 &

# Test with a simple request (requires a JSON-RPC client)
# In another terminal, you can test connectivity:
nc localhost 2089
```

## Development Setup

For contributing to the project:

```bash
# Clone the repository
git clone https://github.com/sourcegraph/javascript-typescript-langserver.git
cd javascript-typescript-langserver

# Install dependencies
npm install

# Run tests
npm test

# Run linters
npm run lint

# Watch for changes during development
npm run watch

# Build for distribution
npm run build
```

## Next Steps

- Read the [README.md](README.md) for features and API documentation
- Check [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines
- Review the Language Server Protocol specification: https://microsoft.github.io/language-server-protocol/
