# vim-lsc Quick Start Guide

## Installation in 5 Minutes

### Step 1: Install the Plugin

Using vim-plug:
```vim
Plug 'natebosch/vim-lsc'
```

Then run `:PlugInstall` in Vim.

### Step 2: Install a Language Server

Choose based on your language:

**Python:**
```bash
pip install python-lsp-server
```

**Go:**
```bash
go install github.com/golang/tools/gopls@latest
```

**Rust:**
```bash
rustup component add rust-analyzer
```

**JavaScript/TypeScript:**
```bash
npm install -g typescript-language-server typescript
```

### Step 3: Configure vim-lsc

Add to your `.vimrc` or `init.vim`:

```vim
Plug 'natebosch/vim-lsc'

let g:lsc_server_commands = {
  \ 'python': 'pylsp',
  \ 'go': 'gopls serve',
  \ 'rust': 'rust-analyzer',
  \ }

let g:lsc_auto_map = v:true
```

### Step 4: Reload Configuration

Restart Vim or run:
```vim
:source ~/.vimrc
```

## Basic Usage

### Jump to Definition
```
<C-]>
```

### Find References
```
gr
```

### Show Hover Information
```
K
```

### Find Code Actions
```
ga
```

### Rename Symbol
```
gR
```

### Document Symbols
```
go
```

## Autocomplete

Type and the completion menu appears automatically:

```python
import os
os.|  <- Autocomplete menu appears here
```

Press `<C-N>` and `<C-P>` to navigate, `<C-Y>` to select, `<C-E>` to cancel.

## Troubleshooting

### Server Not Starting?

Check if the language server is installed and in your PATH:

```bash
# For Python
which pylsp

# For Go
which gopls

# For Rust
which rust-analyzer
```

If not found, install it using the commands above.

### No Completions?

1. Verify `g:lsc_enable_autocomplete` is `v:true`
2. Check that you typed at least 3 characters
3. Verify the server is running: `:echo LSCServerStatus()`

### No Hover Information?

Some language servers don't support hover. Try:
1. Check server capabilities
2. Try moving cursor to different elements
3. Enable verbose logging: `let g:lsc_trace_level = 'verbose'`

## Default Keybindings

When `g:lsc_auto_map = v:true`:

| Key | Action |
|-----|--------|
| `<C-]>` | Jump to definition |
| `gr` | Find references |
| `gI` | Find implementations |
| `ga` | Show code actions |
| `gR` | Rename symbol |
| `K` | Show hover info |
| `go` | Show document symbols |
| `gS` | Search workspace symbols |
| `gm` | Show signature help |

## Next Steps

1. **Read the full README** for complete configuration options
2. **Check CONFIGURATION.md** for advanced setup
3. **Review COMMANDS.md** for all available commands
4. **Customize keybindings** to match your preferences

## Common Configurations

### Disable Autocomplete
```vim
let g:lsc_enable_autocomplete = v:false
```

### Use Different Key Bindings
```vim
let g:lsc_map_keys = {
  \ 'goToDefinition': '<Leader>d',
  \ 'findReferences': '<Leader>r',
  \ 'rename': '<Leader>n',
  \ }
```

### Disable Diagnostics
```vim
let g:lsc_enable_diagnostics = v:false
```

### Enable Snippet Support
```vim
let g:lsc_enable_snippet_support = v:true
```

## Resources

- **GitHub:** https://github.com/natebosch/vim-lsc
- **Language Servers:** https://microsoft.github.io/language-server-protocol/implementors/servers/
- **Full Documentation:** See README.md in this directory

## Getting Help

If something doesn't work:

1. Check `:messages` for error messages
2. Enable trace logging: `let g:lsc_trace_level = 'verbose'`
3. Restart the server: `:LSClientRestartServer`
4. Check the GitHub issues: https://github.com/natebosch/vim-lsc/issues
