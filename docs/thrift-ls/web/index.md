# thrift-ls - Apache Thrift Language Server

# Source: https://github.com/ocfbnj/thrift-ls

**thrift-ls** is a Language Server Protocol (LSP) implementation for Apache Thrift, providing IDE features and development tools across multiple editors and platforms.

## Overview

thrift-ls brings comprehensive IDE support to Thrift Interface Definition Language (IDL) development. It implements the Language Server Protocol standard, making it compatible with any editor that supports LSP, including Visual Studio Code, Vim/Neovim, Lapce, and others.

## Core Features

### 1. **Semantic Syntax Highlighting**
Provides context-aware syntax highlighting for `.thrift` files, improving code readability and error visibility.

### 2. **Go to Definition**
Navigate directly to the definition of types, services, structs, and other elements within your Thrift projects.

### 3. **Diagnostics**
Real-time error checking and reporting for syntax errors, type issues, and other problems in Thrift IDL files.

### 4. **Code Completion**
Intelligent autocompletion for:
- Keywords and language constructs
- Type names and struct fields
- Service methods and functions
- Constants and enumerations

## Supported Editors

### VS Code
- **Extension Name**: thrift-language-server (multiple implementations available)
- **Installation**: Available from VS Code Marketplace
- **Features**: Full IDE support with all LSP capabilities
- **Extensions**:
  - jiangpengfei.thrift-language-server
  - ocfbnj.thrift-ls

### Vim/Neovim
- **Setup**: Configure as an LSP provider through your Neovim/Vim LSP client
- **Command**: Use the thrift-ls binary from the command line
- **Configuration**: Requires LSP client plugin (e.g., nvim-lspconfig)

### Lapce
- **Plugin**: Available from Lapce plugin marketplace
- **Installation**: Plugin ID: `joyme123/thrift-ls`
- **Features**: Native integration with Lapce's LSP support

### Other Editors
Any editor supporting the Language Server Protocol can integrate thrift-ls:
- Emacs (with lsp-mode)
- Sublime Text (with LSP package)
- Atom (with atom-languageclient)
- And other LSP-compatible editors

## Installation

### Build from Source

#### Prerequisites
- **Rust toolchain**: Available from [rustup.rs](https://rustup.rs/)
- **Cargo**: Included with Rust installation
- **Node.js** (optional): Only needed for building the VS Code extension

#### Building the Language Server Binary

```bash
# Clone the repository
git clone https://github.com/ocfbnj/thrift-ls.git
cd thrift-ls

# Build the release binary
cargo build --release

# The executable will be at: ./target/release/thrift-ls
```

#### Building the VS Code Extension

```bash
# Install required tools
cargo install wasm-pack
cargo install wasm-bindgen-cli
npm install -g vsce

# Navigate to the VS Code extension directory
cd editors/code

# Install dependencies
npm install

# Package the extension
vsce package

# The .vsix file will be generated in the project root
# Install in VS Code: code --install-extension thrift-ls-*.vsix
```

### Installing the VS Code Extension

**From Marketplace:**
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
3. Search for "thrift-language-server" or "thrift-ls"
4. Click Install

**From .vsix File:**
```bash
code --install-extension thrift-ls-[version].vsix
```

## Configuration

### Language Server Command

When configuring thrift-ls in your editor's LSP settings, point to the binary:

```
/path/to/thrift-ls
```

Or if installed via package manager:
```
thrift-ls
```

### Editor-Specific Configuration

#### Neovim (nvim-lspconfig)

```lua
require('lspconfig').thrift_ls.setup {
  cmd = { 'thrift-ls' },
  filetypes = { 'thrift' },
  root_dir = require('lspconfig').util.root_pattern('*.thrift'),
}
```

#### VS Code

No additional configuration needed after extension installation. The extension handles all LSP setup automatically.

#### Vim 8+

Using vim-lsp:

```vim
augroup lsp
  autocmd!
  autocmd User lsp_setup call lsp#register_server({
    \ 'name': 'thrift-ls',
    \ 'cmd': {server_info -> ['thrift-ls']},
    \ 'whitelist': ['thrift'],
    \ })
augroup END
```

## Usage

### File Association

Ensure your editor recognizes `.thrift` files and associates them with the language server:

**VS Code**: Automatic after extension installation

**Vim/Neovim**: Configure filetype:
```vim
autocmd BufRead,BufNewFile *.thrift setfiletype thrift
```

### Common Workflows

#### Navigating Code
- **Go to Definition**: Hover over a type/service name and use your editor's "Go to Definition" command (usually Ctrl+Click or F12)
- **Peek Definition**: Use "Peek Definition" for inline viewing without navigating
- **Find References**: Right-click and select "Find All References" to see all usages

#### Writing Code
- **Autocomplete**: Start typing and press Ctrl+Space to trigger completions
- **Syntax Check**: Errors appear automatically in the editor's problems panel
- **Quick Fixes**: Some errors offer quick fix suggestions (if implemented in your extension)

#### Debugging Issues
- Check the Language Server output in your editor's output panel
- VS Code: View > Output, then select "thrift-ls" from the dropdown
- Look for error messages that indicate configuration issues

## Architecture

### Components

1. **Rust Language Server** (`src/` directory)
   - Core LSP implementation
   - Thrift IDL parser and analyzer
   - Diagnostics engine
   - Symbol resolution and navigation

2. **WASM Module** (`lib/` directory)
   - WebAssembly compilation of core functionality
   - Used by the VS Code extension for client-side processing
   - Enables consistent behavior across platforms

3. **VS Code Extension** (`editors/code/` directory)
   - Extension manifest and packaging
   - UI/UX integration
   - LSP client implementation for VS Code

### Thrift Language Support

thrift-ls supports the full Apache Thrift IDL syntax:

**Data Types:**
- Primitive types: i32, i64, double, string, bool, byte, etc.
- Collections: list<T>, set<T>, map<K,V>
- Structs, Exceptions, Unions
- Typedefs and Enumerations

**Service Definitions:**
- Service declaration with methods
- Method parameters and return types
- Exceptions and oneway calls

**Constants and Includes:**
- Constant definitions
- Include directives for modular IDL

## Development

### Understanding the Codebase

The project follows a standard Rust project structure:
- `src/main.rs` - Language server entry point
- `src/lib.rs` - Core library implementation
- `Cargo.toml` - Rust project manifest
- `editors/code/` - VS Code extension source

### Running in Development Mode

```bash
# Build in debug mode
cargo build

# Run the language server directly
./target/debug/thrift-ls

# The server listens for LSP requests on stdin/stdout
```

### Testing

While the repository doesn't include formal test files, you can test functionality by:

1. Building a test `.thrift` file with various constructs
2. Launching the server in a test editor environment
3. Verifying syntax highlighting, completions, and error detection

Example test file:

```thrift
// test.thrift
namespace java com.example
namespace py example
namespace js example

service GreetingService {
  string greet(1: string name),
  list<string> getNames()
}

struct Person {
  1: required i32 id,
  2: required string name,
  3: optional i32 age
}
```

## Troubleshooting

### Language Server Not Found

**Problem**: Editor says "language server not found" or "command not found"

**Solution**:
- Ensure the binary is built: `cargo build --release`
- Provide absolute path to the binary in editor configuration
- Verify the binary is executable: `chmod +x ./target/release/thrift-ls`

### No Syntax Highlighting

**Problem**: `.thrift` files appear as plain text

**Solution**:
- Install or activate the VS Code extension
- Set filetype in Vim: `:set filetype=thrift`
- Verify the editor's LSP client is properly configured

### Completions Not Working

**Problem**: Autocompletion doesn't appear when typing

**Solution**:
- Ensure the file is saved and recognized as `.thrift`
- Try triggering completion manually (Ctrl+Space in most editors)
- Check the Language Server output for errors
- Verify your editor's LSP configuration includes `thrift` in the filetypes list

### Diagnostics Not Appearing

**Problem**: Syntax errors aren't highlighted

**Solution**:
- Check that the Thrift file has valid syntax
- Ensure the file is saved (some servers only analyze saved files)
- Look in the editor's "Problems" panel for error messages
- Verify the LSP server started successfully in the editor's output panel

## References

### Official Documentation
- [Apache Thrift IDL Documentation](https://thrift.apache.org/docs/idl)
- [Language Server Protocol Specification](https://microsoft.github.io/language-server-protocol/)

### Related Projects
- **Alternative Implementation**: [joyme123/thrift-ls](https://github.com/joyme123/thrift-ls)
- **Thrift Compiler**: [Apache Thrift GitHub Repository](https://github.com/apache/thrift)
- **LSP Implementations**: [LSP Implementations](https://microsoft.github.io/language-server-protocol/implementations/servers/)

### Editor Resources
- **VS Code Extension API**: https://code.visualstudio.com/api
- **Neovim LSP**: https://neovim.io/doc/user/lsp.html
- **Vim LSP**: https://github.com/prabirshrestha/vim-lsp

## Community and Support

- **GitHub Issues**: Report bugs or request features at https://github.com/ocfbnj/thrift-ls/issues
- **Discussions**: Engage with the community on GitHub Discussions (if enabled)
- **Apache Thrift Community**: Get Thrift-specific help at https://thrift.apache.org/

## License

Apache License 2.0 (per MIT license in repository)

## Related Tools

### Apache Thrift
The Thrift software framework provides code generation and serialization across multiple programming languages. thrift-ls provides IDE support for writing Thrift IDL files.

### Language Server Protocol
LSP is a standardized protocol for language tools to communicate with editors. thrift-ls implements LSP to provide consistent IDE support across multiple editors.

## Version Information

- **Project**: thrift-ls
- **Repository**: https://github.com/ocfbnj/thrift-ls
- **Implementation**: Rust
- **Latest**: Main branch (no version tags in initial implementation)
- **License**: MIT

---

**Last Updated**: 2026-01-06
**Source Repository**: https://github.com/ocfbnj/thrift-ls
