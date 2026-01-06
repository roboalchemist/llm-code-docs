# thrift-ls Quick Start Guide

# Source: https://github.com/ocfbnj/thrift-ls

## What is thrift-ls?

**thrift-ls** is a Language Server that provides IDE features for Apache Thrift IDL (Interface Definition Language) development. It brings syntax highlighting, code completion, error checking, and navigation features to your editor.

## Installation in 5 Minutes

### Option 1: VS Code (Easiest)

1. Open VS Code
2. Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac)
3. Search for **"thrift-language-server"**
4. Click **Install**
5. Done! You're ready to code

### Option 2: Build from Source (All Editors)

**Requirements:**
- Rust (install from [rustup.rs](https://rustup.rs/))
- Git

**Steps:**
```bash
git clone https://github.com/ocfbnj/thrift-ls.git
cd thrift-ls
cargo build --release

# Binary is ready at: ./target/release/thrift-ls
```

## First Steps

### VS Code
1. Create a new file with `.thrift` extension
2. Start typing - syntax highlighting appears automatically
3. Type `ser` and press `Ctrl+Space` - see autocompletion suggestions
4. Hover over any word for documentation
5. Right-click and select "Go to Definition" to navigate

### Vim/Neovim
1. Install an LSP client plugin (e.g., `nvim-lspconfig`)
2. Configure it to use thrift-ls for `.thrift` files
3. Open a `.thrift` file
4. Use editor commands: `gd` for goto definition, `K` for hover docs

### Other Editors
1. Install an LSP client package/extension for your editor
2. Point it to the thrift-ls binary
3. Open a `.thrift` file and start editing

## Common Commands

### VS Code / General Editor

| Action | Shortcut |
|--------|----------|
| Go to Definition | Click on symbol + Ctrl/Cmd, or F12 |
| Peek Definition | Ctrl+Shift+F12 (Windows/Linux), Cmd+Shift+F12 (Mac) |
| Find References | Ctrl+Shift+H or right-click → Find All References |
| Autocomplete | Ctrl+Space |
| Show Errors | Ctrl+Shift+M |

### Example Thrift File

Create `hello.thrift`:

```thrift
// Define a service
service HelloService {
  // Method definition
  string sayHello(1: string name),

  // Another method
  list<string> listUsers()
}

// Define a data structure
struct User {
  1: required i32 id,
  2: required string name,
  3: optional string email
}

// Define a constant
const string DEFAULT_NAME = "World"

// Define an enumeration
enum UserRole {
  ADMIN = 1,
  USER = 2,
  GUEST = 3
}
```

## Editor Configuration

### VS Code
- **Zero configuration needed** - just install the extension

### Neovim (init.lua)

```lua
require('lspconfig').thrift_ls.setup {}
```

### Vim (init.vim)

```vim
if executable('thrift-ls')
  au User lsp_setup call lsp#register_server({
    \   'name': 'thrift-ls',
    \   'cmd': {server_info->['thrift-ls']},
    \   'whitelist': ['thrift'],
    \ })
endif
```

## What thrift-ls Can Do

✓ **Syntax Highlighting** - Color-coded Thrift syntax
✓ **Error Detection** - Real-time error reporting
✓ **Autocompletion** - Intelligent code suggestions
✓ **Go to Definition** - Jump to type/service definitions
✓ **Find References** - See all uses of a symbol

## Common Issues & Solutions

### "Language server not found"
```bash
# Ensure the binary is built
cargo build --release

# Provide full path to configuration
# Point to: /path/to/thrift-ls/target/release/thrift-ls
```

### No syntax highlighting
- Check that file has `.thrift` extension
- In Vim: `:set filetype=thrift`
- In VS Code: Reload window (Cmd+R)

### Completions not working
- Make sure file is saved (`.thrift` extension)
- Try `Ctrl+Space` to manually trigger
- Check editor's Language Server output for errors

## Learn More

- **Full Documentation**: See `index.md` in this directory
- **Thrift IDL Docs**: https://thrift.apache.org/docs/idl
- **Report Issues**: https://github.com/ocfbnj/thrift-ls/issues

## Next Steps

1. Install thrift-ls for your editor
2. Create a `.thrift` file
3. Start defining services and data types
4. Explore the IDE features (go to definition, completions, etc.)
5. Check the full documentation for advanced features

---

**Ready to code Thrift?** Start with the example above!
