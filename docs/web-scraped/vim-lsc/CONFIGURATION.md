# vim-lsc Configuration Guide

## Quick Start Configuration

### Minimal Setup

```vim
" Enable the plugin
Plug 'natebosch/vim-lsc'

" Configure language servers
let g:lsc_server_commands = {
  \ 'python': 'pylsp',
  \ 'go': 'gopls',
  \ 'rust': 'rust-analyzer',
  \ 'javascript': 'typescript-language-server --stdio',
  \ }

" Enable auto-map for default keybindings
let g:lsc_auto_map = v:true
```

### Full-Featured Setup

```vim
Plug 'natebosch/vim-lsc'
Plug 'liuchengxu/vista.vim'

let g:lsc_server_commands = {
  \ 'python': 'pylsp',
  \ 'go': 'gopls',
  \ 'rust': 'rust-analyzer',
  \ 'javascript': 'typescript-language-server --stdio',
  \ }

let g:lsc_auto_map = v:true
let g:lsc_enable_autocomplete = v:true
let g:lsc_enable_diagnostics = v:true
let g:lsc_diagnostic_highlights = v:true
let g:lsc_hover_popup = v:true
let g:lsc_reference_highlights = v:true
```

---

## Core Configuration Options

### Server Commands

**`g:lsc_server_commands`** (Dictionary, required)

Maps filetypes to language server commands.

**Simple form (command string):**
```vim
let g:lsc_server_commands = {
  \ 'python': 'pylsp',
  \ 'go': 'gopls',
  \ 'rust': 'rust-analyzer',
  \ 'dart': 'dart_language_server',
  \ }
```

**Extended form (command with arguments):**
```vim
let g:lsc_server_commands = {
  \ 'javascript': 'node_modules/.bin/eslint-language-server --stdio',
  \ 'typescript': 'node_modules/.bin/typescript-language-server --stdio',
  \ }
```

**Host:port form (remote server):**
```vim
let g:lsc_server_commands = {
  \ 'python': 'localhost:8080',
  \ }
```

---

### Autocompletion Settings

**`g:lsc_enable_autocomplete`** (Boolean, default: v:true)

Enable or disable automatic completion triggering.

```vim
" Enable autocompletion
let g:lsc_enable_autocomplete = v:true

" Disable autocompletion (use manual completion with Ctrl-X Ctrl-O)
let g:lsc_enable_autocomplete = v:false
```

**`g:lsc_autocomplete_length`** (Number, default: 3)

Number of characters typed before autocompletion triggers.

```vim
" Trigger after 3 characters (default)
let g:lsc_autocomplete_length = 3

" Trigger after 1 character
let g:lsc_autocomplete_length = 1

" Require more characters for trigger
let g:lsc_autocomplete_length = 5
```

**`g:lsc_complete_timeout`** (Number, default: 5)

Number of seconds to wait for completion results.

```vim
" Default 5 second timeout
let g:lsc_complete_timeout = 5

" Shorter timeout
let g:lsc_complete_timeout = 2

" Longer timeout
let g:lsc_complete_timeout = 10
```

**`g:lsc_block_complete_triggers`** (List, default: [])

Characters that should NOT trigger completion.

```vim
" Don't trigger completion after these characters
let g:lsc_block_complete_triggers = ['/', '-', ':']
```

**`g:lsc_enable_snippet_support`** (Boolean, default: v:false)

Enable snippet expansion during completion.

```vim
" Enable snippet support (requires vim-vsnip or similar)
let g:lsc_enable_snippet_support = v:true
```

---

### Diagnostics Settings

**`g:lsc_enable_diagnostics`** (Boolean, default: v:true)

Enable or disable all diagnostic features.

```vim
" Enable diagnostics
let g:lsc_enable_diagnostics = v:true

" Disable diagnostics
let g:lsc_enable_diagnostics = v:false
```

**`g:lsc_diagnostic_highlights`** (Boolean, default: v:true)

Enable highlighting of diagnostics in the buffer.

```vim
" Enable diagnostic highlighting and messages
let g:lsc_diagnostic_highlights = v:true

" Disable but keep diagnostics in lists
let g:lsc_diagnostic_highlights = v:false
```

**`g:lsc_change_debounce_time`** (Number, default: 500)

Milliseconds to wait before sending document changes to server.

```vim
" Default 500ms debounce
let g:lsc_change_debounce_time = 500

" Faster (200ms)
let g:lsc_change_debounce_time = 200

" Slower (1000ms)
let g:lsc_change_debounce_time = 1000
```

---

### Hover and Display Settings

**`g:lsc_hover_popup`** (Boolean, default: v:true in Neovim, v:false in Vim)

Use floating window for hover information (Neovim only).

```vim
" Use floating window (Neovim)
let g:lsc_hover_popup = v:true

" Use preview window (fallback for Vim 8)
let g:lsc_hover_popup = v:false
```

**`g:lsc_preview_split_direction`** (String, default: 'above')

Direction for preview window (when not using floating window).

```vim
" Display above the current window
let g:lsc_preview_split_direction = 'above'

" Display below the current window
let g:lsc_preview_split_direction = 'below'
```

**`g:lsc_popup_syntax`** (Boolean, default: v:true in Neovim)

Enable syntax highlighting in hover popups.

```vim
" Enable syntax highlighting
let g:lsc_popup_syntax = v:true

" Disable syntax highlighting
let g:lsc_popup_syntax = v:false
```

---

### Navigation Settings

**`g:lsc_reference_highlights`** (Boolean, default: v:true)

Enable highlighting of all references to symbol under cursor.

```vim
" Enable reference highlighting
let g:lsc_reference_highlights = v:true

" Disable reference highlighting
let g:lsc_reference_highlights = v:false
```

**`g:lsc_auto_map`** (Boolean, default: v:false)

Enable default keybindings.

```vim
" Enable all default keybindings
let g:lsc_auto_map = v:true

" Disable and use custom mappings
let g:lsc_auto_map = v:false
```

---

### Document Synchronization

**`g:lsc_enable_incremental_sync`** (Boolean, default: v:true)

Send only changed portions of document (vs. entire document).

```vim
" Send incremental changes (more efficient)
let g:lsc_enable_incremental_sync = v:true

" Send entire document each time
let g:lsc_enable_incremental_sync = v:false
```

**`g:lsc_enable_apply_edit`** (Boolean, default: v:false)

Allow language server to modify buffers via applyEdit request.

```vim
" Allow server to modify buffers (enables some refactorings)
let g:lsc_enable_apply_edit = v:true

" Prevent server from modifying buffers
let g:lsc_enable_apply_edit = v:false
```

---

### Tracing and Logging

**`g:lsc_trace_level`** (String, default: 'off')

Server-side logging level for debugging.

```vim
" No logging
let g:lsc_trace_level = 'off'

" Log messages
let g:lsc_trace_level = 'messages'

" Verbose logging (includes full messages)
let g:lsc_trace_level = 'verbose'
```

---

## Advanced Configuration: Dictionary Format

For complex setups, use dictionary format for server configuration:

```vim
let g:lsc_server_commands = {
  \ 'python': {
  \   'command': 'pylsp',
  \   'name': 'Python Language Server',
  \   'enabled': v:true,
  \   'languageId': 'python',
  \   'log_level': 'Warning',
  \   'suppress_stderr': v:false,
  \ },
  \ }
```

### Dictionary Keys

**`command`** (String, required)
- Server executable, absolute path, or "host:port"

**`name`** (String, optional)
- Friendly identifier for the server
- Useful when multiple servers serve the same language

**`enabled`** (Boolean, default: v:true)
- Start server immediately (`v:true`) or defer (`v:false`)

**`languageId`** (String, optional)
- Override the filetype-to-languageId mapping
- Defaults to the dictionary key (filetype)

**`log_level`** (String, default: 'Warning')
- Message filtering level: 'Error', 'Warning', 'Info', 'Log', 'Debug'

**`suppress_stderr`** (Boolean, default: v:false)
- Hide server stderr output

**`message_hooks`** (Function, optional)
- Custom function to modify outgoing LSP requests

**`response_hooks`** (Function, optional)
- Custom function to transform server responses

**`notifications`** (Dictionary, optional)
- Custom handlers for server notifications

**`workspace_config`** (Dictionary, optional)
- Server-specific workspace configuration

---

## Custom Keybindings

### Override Default Mappings

```vim
let g:lsc_map_keys = {
  \ 'goToDefinition': '<C-]>',
  \ 'goToDefinitionSplit': '<C-W>]',
  \ 'findReferences': 'gr',
  \ 'nextReference': '<C-n>',
  \ 'previousReference': '<C-p>',
  \ 'findImplementations': 'gI',
  \ 'findCodeActions': 'ga',
  \ 'rename': 'gR',
  \ 'showHover': 'K',
  \ 'documentSymbol': 'go',
  \ 'workspaceSymbol': 'gS',
  \ 'signatureHelp': 'gm',
  \ }
```

### Disable Specific Mappings

```vim
" Disable code actions mapping
let g:lsc_map_keys = {
  \ 'findCodeActions': '',
  \ }
```

### Use Custom Mappings Without Auto-Map

```vim
let g:lsc_auto_map = v:false

" Define your own mappings
nnoremap <Leader>d :LSClientGoToDefinition<CR>
nnoremap <Leader>r :LSClientFindReferences<CR>
nnoremap <Leader>h :LSClientShowHover<CR>
```

---

## Language-Specific Examples

### Python Setup

**Option 1: Using Pylance**
```vim
let g:lsc_server_commands = {
  \ 'python': {
  \   'command': 'pylance',
  \   'log_level': 'Warning',
  \ },
  \ }
```

**Option 2: Using Pyright**
```vim
let g:lsc_server_commands = {
  \ 'python': 'pyright-langserver --stdio',
  \ }
```

**Option 3: Using pylsp with plugins**
```vim
let g:lsc_server_commands = {
  \ 'python': {
  \   'command': 'pylsp',
  \   'workspace_config': {
  \     'pylsp': {
  \       'plugins': {
  \         'autopep8': {'enabled': v:true},
  \         'flake8': {'enabled': v:true},
  \         'mccabe': {'enabled': v:true},
  \         'pycodestyle': {'enabled': v:true},
  \       },
  \     },
  \   },
  \ },
  \ }
```

### Go Setup

```vim
let g:lsc_server_commands = {
  \ 'go': {
  \   'command': 'gopls serve',
  \   'log_level': 'Warning',
  \ },
  \ }
```

### Rust Setup

```vim
let g:lsc_server_commands = {
  \ 'rust': {
  \   'command': 'rust-analyzer',
  \   'log_level': 'Warning',
  \ },
  \ }
```

### JavaScript/TypeScript Setup

```vim
let g:lsc_server_commands = {
  \ 'javascript': 'typescript-language-server --stdio',
  \ 'typescript': 'typescript-language-server --stdio',
  \ 'typescriptreact': 'typescript-language-server --stdio',
  \ }
```

---

## Debugging Configuration

### Verify Configuration is Loaded

```vim
:echo g:lsc_server_commands
:echo g:lsc_enable_autocomplete
:echo g:lsc_enable_diagnostics
```

### Check Server Status

```vim
:echo LSCServerStatus()
```

### Enable Verbose Tracing

```vim
let g:lsc_trace_level = 'verbose'
```

### Check if Plugin is Loaded

```vim
:scriptnames | grep lsc
```

---

## Configuration Troubleshooting

### Server Not Starting

1. Check if server is installed and in PATH:
   ```vim
   :echo system('which pylsp')
   ```

2. Verify configuration syntax:
   ```vim
   :echo g:lsc_server_commands
   ```

3. Enable trace for debugging:
   ```vim
   let g:lsc_trace_level = 'verbose'
   ```

### Completion Not Working

1. Check if enabled:
   ```vim
   :echo g:lsc_enable_autocomplete
   ```

2. Verify trigger length:
   ```vim
   :echo g:lsc_autocomplete_length
   ```

3. Check server status:
   ```vim
   :echo LSCServerStatus()
   ```

### Diagnostics Not Showing

1. Check if enabled:
   ```vim
   :echo g:lsc_enable_diagnostics
   :echo g:lsc_diagnostic_highlights
   ```

2. Verify server is running and can analyze buffer

3. Check current line diagnostics:
   ```vim
   :LSClientLineDiagnostics
   ```

### Hover Not Working in Neovim

Add to configuration if errors are suppressed:
```vim
set shortmess-=F
```

---

## Complete Example Configuration

```vim
" Plugin manager setup
Plug 'natebosch/vim-lsc'
Plug 'liuchengxu/vista.vim'

" Core server configuration
let g:lsc_server_commands = {
  \ 'python': 'pylsp',
  \ 'go': 'gopls serve',
  \ 'rust': 'rust-analyzer',
  \ 'javascript': 'typescript-language-server --stdio',
  \ 'typescript': 'typescript-language-server --stdio',
  \ }

" Keybindings and behavior
let g:lsc_auto_map = v:true
let g:lsc_map_keys = {
  \ 'goToDefinition': '<C-]>',
  \ 'findReferences': 'gr',
  \ 'findImplementations': 'gI',
  \ 'findCodeActions': 'ga',
  \ 'rename': 'gR',
  \ 'showHover': 'K',
  \ }

" Completion settings
let g:lsc_enable_autocomplete = v:true
let g:lsc_autocomplete_length = 3
let g:lsc_complete_timeout = 5
let g:lsc_enable_snippet_support = v:true

" Diagnostics
let g:lsc_enable_diagnostics = v:true
let g:lsc_diagnostic_highlights = v:true
let g:lsc_change_debounce_time = 500

" Display options
let g:lsc_hover_popup = v:true
let g:lsc_popup_syntax = v:true
let g:lsc_preview_split_direction = 'above'

" Navigation
let g:lsc_reference_highlights = v:true

" Advanced options
let g:lsc_enable_incremental_sync = v:true
let g:lsc_enable_apply_edit = v:false
let g:lsc_trace_level = 'off'

" Neovim fix (if needed)
if has('nvim')
  set shortmess-=F
endif

" Example hook function
function! MyMessageHook(server_name, message) abort
  " Custom message processing
  return a:message
endfunction
```
