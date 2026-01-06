# vim-lsc: Vim Language Server Client

Source: https://github.com/natebosch/vim-lsc

## Overview

vim-lsc is a Language Server Protocol (LSP) client for Vim that integrates IDE-like features directly into the editor. It enables intelligent code editing through language servers, providing autocomplete, diagnostics, navigation, and refactoring capabilities for multiple programming languages.

The plugin is compatible with:
- Vim 8+
- Neovim
- Common plugin managers (vim-plug, vundle, etc.)

## Installation

### Basic Installation

Install via your preferred plugin manager:

**vim-plug:**
```vim
Plug 'natebosch/vim-lsc'
```

**Vundle:**
```vim
Plugin 'natebosch/vim-lsc'
```

**Native Vim 8:**
```bash
git clone https://github.com/natebosch/vim-lsc.git ~/.vim/pack/plugins/start/vim-lsc
```

### Important Setup Notes

**For Neovim users:** Add the following to your configuration to prevent error message suppression:
```vim
set shortmess-=F
```

**Language Server Installation:** You must install the appropriate language server for each filetype you want to use. Language servers must be available in your `$PATH`.

## Configuration

### Basic Server Setup

Configure language servers by mapping filetypes to their executable names in your `.vimrc` or `init.vim`:

```vim
let g:lsc_server_commands = {
  \ 'dart': 'dart_language_server',
  \ 'python': 'pylsp',
  \ 'rust': 'rls',
  \ 'go': 'gopls',
  \ 'javascript': 'node_modules/.bin/eslint-language-server --stdio',
  \ }
```

### Server Command Format

Each server can be specified as:
1. **Simple string:** Executable name or absolute path
   ```vim
   'dart': 'dart_language_server'
   ```

2. **Host:port pair:** For server/client architecture
   ```vim
   'python': 'localhost:8080'
   ```

3. **Dictionary:** Advanced configuration (see Advanced Configuration below)

### Essential Configuration Options

**Enable/Disable Autocompletion:**
```vim
let g:lsc_enable_autocomplete = v:false  " Disable if desired (default: v:true)
```

**Autocomplete Trigger Length:**
```vim
let g:lsc_autocomplete_length = 3  " Characters before autocompletion triggers
```

**Auto-map Default Keybindings:**
```vim
let g:lsc_auto_map = v:true  " Enable all default keybindings
```

**Enable/Disable Diagnostics:**
```vim
let g:lsc_enable_diagnostics = v:true  " Show errors and warnings
```

**Server Trace/Logging Level:**
```vim
let g:lsc_trace_level = 'off'  " Options: 'off', 'messages', 'verbose'
```

### Hover Display Options

**Use Floating Window (Neovim):**
```vim
let g:lsc_hover_popup = v:true  " Use floating window for hover
```

**Hover Window Direction:**
```vim
let g:lsc_preview_split_direction = 'above'  " or 'below'
```

### Snippet Support

Enable snippet expansion during autocompletion:
```vim
let g:lsc_enable_snippet_support = v:true
```

## Key Mappings

When `g:lsc_auto_map = v:true`, the following default keybindings are enabled:

| Keybinding | Command | Description |
|------------|---------|-------------|
| `<C-]>` | GoToDefinition | Jump to symbol definition |
| `<C-W>]` | GoToDefinitionSplit | Open definition in horizontal split |
| `<C-W><C-]>` | GoToDefinitionSplit | Open definition in split (alternative) |
| `gr` | FindReferences | Find all references to symbol |
| `<C-n>` | NextReference | Navigate to next reference |
| `<C-p>` | PreviousReference | Navigate to previous reference |
| `gI` | FindImplementations | Find implementations |
| `go` | DocumentSymbol | Show symbols in current document |
| `gS` | WorkspaceSymbol | Search workspace symbols |
| `ga` | FindCodeActions | Show available code actions |
| `gR` | Rename | Rename symbol under cursor |
| `gm` | SignatureHelp | Show function signature help |
| `K` | ShowHover | Display hover information |

### Custom Keybindings

Override default mappings by setting them to empty strings or custom bindings:

```vim
" Disable a specific mapping
let g:lsc_map_keys = {
  \ 'goToDefinition': '<C-]>',
  \ 'findReferences': 'gr',
  \ 'findImplementations': 'gI',
  \ 'findCodeActions': 'ga',
  \ 'rename': 'gR',
  \ 'showHover': 'K',
  \ 'documentSymbol': 'go',
  \ 'workspaceSymbol': 'gS',
  \ 'signatureHelp': 'gm',
  \ }
```

## Core Commands

### Navigation

**`:LSClientGoToDefinition`**
- Jump to the definition of the symbol under the cursor
- Equivalent to pressing `<C-]>` with auto-map enabled

**`:LSClientGoToDefinitionSplit`**
- Open the definition in a split window
- Equivalent to `<C-W>]` or `<C-W><C-]>` with auto-map enabled

### Reference Handling

**`:LSClientFindReferences`**
- Populate the quickfix list with all references to the symbol under cursor
- Highlights all instances in the buffer when server supports reference highlighting

**`:LSClientNextReference`**
- Navigate to the next highlighted reference (when reference highlighting is enabled)

**`:LSClientPreviousReference`**
- Navigate to the previous highlighted reference

### Symbol Navigation

**`:LSClientFindImplementations`**
- Jump to implementation(s) of the symbol under cursor
- Useful for finding interface implementations or overridden methods

**`:LSClientDocumentSymbol`**
- Display all symbols (functions, classes, variables) in the current document
- Results shown in a location list for easy navigation

**`:LSClientWorkspaceSymbol`**
- Search for symbols across the entire workspace
- Prompts for search term and populates quickfix list with results

### Information & Hover

**`:LSClientShowHover`**
- Display documentation and type information for the symbol under cursor
- Shows in a floating window (Neovim) or preview window (Vim)
- Equivalent to pressing `K` with auto-map enabled

### Code Actions & Refactoring

**`:LSClientFindCodeActions`**
- Show available code actions at the current cursor position
- Code actions may include quick-fixes, refactorings, or linter suggestions
- Select and apply an action directly from the menu

**`:LSClientRename`**
- Rename the symbol under cursor throughout the document/workspace
- Equivalent to pressing `gR` with auto-map enabled

### Diagnostics Management

**`:LSClientAllDiagnostics`**
- Populate the quickfix list with all diagnostics in all open buffers
- Useful for reviewing all errors and warnings

**`:LSClientWindowDiagnostics`**
- Show diagnostics for the current window in the location list
- Allows per-window diagnostic viewing

**`:LSClientLineDiagnostics`**
- Display diagnostics for the current line in the message area
- Shows detailed error/warning information

**`:LSClientEnableDiagnosticHighlights`**
- Enable highlighting of diagnostic locations in the buffer
- Shows errors, warnings, and hints with appropriate highlighting

**`:LSClientDisableDiagnosticHighlights`**
- Disable diagnostic highlighting

### Server Management

**`:LSClientRestartServer`**
- Restart the language server for the current buffer's filetype
- Useful when the server becomes unresponsive

**`:LSClientDisable`**
- Temporarily disable the language server
- Server stops processing but can be re-enabled

**`:LSClientEnable`**
- Re-enable a previously disabled language server

## Core Features

### Diagnostics

The plugin automatically receives and displays errors, warnings, and hints from the language server:

- **In-buffer highlighting:** Errors and warnings are highlighted at their locations
- **Message display:** When the cursor rests on a diagnostic line, the message is echoed
- **Quickfix integration:** All diagnostics can be viewed in the quickfix list
- **Location list integration:** Window-specific diagnostics in the location list

Diagnostic behavior is controlled by:
- `g:lsc_enable_diagnostics` - Enable/disable diagnostics entirely
- `g:lsc_diagnostic_highlights` - Enable/disable highlighting and echoing
- `g:lsc_change_debounce_time` - Delay before sending document changes (default: 500ms)

### Autocompletion

Provides intelligent code completion based on language server capabilities:

- **Automatic triggering:** Activates after typing 3+ word characters (configurable)
- **Trigger characters:** Special characters can trigger completion (language-specific)
- **Completion menu:** Native Vim completion menu with LSP suggestions
- **Type information:** Shows types and descriptions for completions
- **Snippet support:** Can expand snippets if `g:lsc_enable_snippet_support = v:true`

**Configuration:**
```vim
let g:lsc_enable_autocomplete = v:true
let g:lsc_autocomplete_length = 3
let g:lsc_complete_timeout = 5  " Seconds to wait for completion
let g:lsc_block_complete_triggers = []  " Characters to exclude
```

### Reference Highlights

When a server supports reference highlighting, all occurrences of the symbol under cursor are highlighted:

- **Visual highlighting:** All references appear highlighted in the buffer
- **Navigation:** Use `<C-n>` and `<C-p>` to jump between highlighted references
- **Hover information:** Displays context information for the highlighted symbol

Control with:
```vim
let g:lsc_reference_highlights = v:true
```

### Code Navigation

Jump between related code locations:

- **Definition:** `<C-]>` to jump to definition
- **References:** `gr` to find all references
- **Implementations:** `gI` to find implementations
- **Workspace symbols:** `gS` to search workspace-wide
- **Document symbols:** `go` to list symbols in current file

### Signature Help

Displays function signatures while editing function calls:

- **Parameter information:** Shows function parameters and types
- **Automatic display:** Can trigger automatically during function calls
- **Manual trigger:** `gm` or `:LSClientSignatureHelp` command

### Hover Information

Display documentation and type information:

- **Documentation:** Shows docstrings and comments
- **Type information:** Displays inferred or declared types
- **Floating window:** Uses Neovim floating windows when available
- **Preview window:** Falls back to preview window in Vim 8

## Advanced Configuration

### Server Configuration Dictionary

For complex server setups, configure servers using a dictionary:

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
  \ 'rust': {
  \   'command': 'rls',
  \   'name': 'Rust Language Server',
  \   'log_level': 'Error',
  \ },
  \ }
```

### Dictionary Options

- **`command`** (required): Server executable, absolute path, or "host:port"
- **`name`:** Friendly identifier for the server (useful for multiple servers per language)
- **`enabled`:** Start server immediately or defer (`v:true` or `v:false`)
- **`languageId`:** Override the filetype-to-languageId mapping
- **`log_level`:** Message filtering level (Error, Warning, Info, Log)
- **`suppress_stderr`:** Hide server stderr output (`v:true` or `v:false`)
- **`message_hooks`:** Custom function to modify outgoing LSP requests
- **`response_hooks`:** Custom function to transform server responses
- **`notifications`:** Custom notification handlers
- **`workspace_config`:** Server-specific workspace configuration settings

### Message Hooks

Modify outgoing LSP requests before sending:

```vim
function! MyMessageHook(server_name, message) abort
  " Modify message as needed
  return a:message
endfunction

let g:lsc_server_commands = {
  \ 'python': {
  \   'command': 'pylsp',
  \   'message_hooks': function('MyMessageHook'),
  \ },
  \ }
```

### Response Hooks

Transform server responses:

```vim
function! MyResponseHook(server_name, response) abort
  " Process response
  return a:response
endfunction

let g:lsc_server_commands = {
  \ 'rust': {
  \   'command': 'rls',
  \   'response_hooks': function('MyResponseHook'),
  \ },
  \ }
```

### Workspace Configuration

Pass server-specific configuration:

```vim
let g:lsc_server_commands = {
  \ 'python': {
  \   'command': 'pylsp',
  \   'workspace_config': {
  \     'pylsp': {
  \       'configurationSources': ['flake8'],
  \     },
  \   },
  \ },
  \ }
```

## Additional Configuration Options

**Completion Timeout:**
```vim
let g:lsc_complete_timeout = 5  " Seconds to wait for completion results
```

**Change Debounce Time:**
```vim
let g:lsc_change_debounce_time = 500  " Milliseconds before sending changes
```

**Incremental Sync:**
```vim
let g:lsc_enable_incremental_sync = v:true  " Send diffs instead of full document
```

**Allow Server to Modify Buffers:**
```vim
let g:lsc_enable_apply_edit = v:true  " Allow :applyEdit requests
```

**Syntax Highlighting in Popups:**
```vim
let g:lsc_popup_syntax = v:true  " Use syntax highlighting in hover popups
```

## Server Status Function

Check the current status of a language server:

```vim
echo LSCServerStatus()
```

**Possible return values:**
- `'starting'` - Server is initializing
- `'running'` - Server is active and processing requests
- `'exiting'` - Server is shutting down
- `'restoring'` - Server is recovering from a crash
- `'exited'` - Server has exited gracefully
- `'unexpected exit'` - Server crashed unexpectedly
- `'failed'` - Server failed to start

## Autocommands

vim-lsc provides several autocommands for custom behavior:

**`LSCAutocomplete`**
- Triggered before completion is requested
- Allows custom logic before completion menu appears

**`LSCDiagnosticsChange`**
- Triggered when diagnostics are received from the server
- Useful for custom diagnostic handling or notifications

**`LSCShowPreview`**
- Triggered when the preview window is opened
- Can be used to customize preview window appearance

**`LSCOnChangesFlushed`**
- Triggered after document changes are synchronized with the server
- Useful for post-sync operations

### Using Autocommands

```vim
autocmd User LSCDiagnosticsChange call MyDiagnosticsHandler()
autocmd User LSCShowPreview call MyPreviewHandler()
```

## Plugin Integrations

vim-lsc works with several complementary plugins:

### vista.vim
Tag/symbol browser integration for better navigation:
```bash
Plug 'natebosch/vim-lsc'
Plug 'liuchengxu/vista.vim'
```

### deoplete-vim-lsc
Enhanced completion with deoplete:
```bash
Plug 'natebosch/vim-lsc'
Plug 'deoplete-plugins/deoplete-lsc'
```

### vim-vsnip
Snippet support for completions and code actions:
```bash
Plug 'natebosch/vim-lsc'
Plug 'hrsh7th/vim-vsnip'
Plug 'hrsh7th/vim-vsnip-integ'
```

## Common Language Server Examples

### Python

**Using Pylance:**
```vim
let g:lsc_server_commands = {
  \ 'python': {
  \   'command': 'pylance',
  \   'log_level': 'Warning',
  \ },
  \ }
```

**Using Pyright:**
```vim
let g:lsc_server_commands = {
  \ 'python': 'pyright-langserver --stdio',
  \ }
```

**Using pylsp:**
```vim
let g:lsc_server_commands = {
  \ 'python': 'pylsp',
  \ }
```

### Go

**Using gopls:**
```vim
let g:lsc_server_commands = {
  \ 'go': 'gopls serve',
  \ }
```

### Rust

**Using rust-analyzer:**
```vim
let g:lsc_server_commands = {
  \ 'rust': 'rust-analyzer',
  \ }
```

### JavaScript/TypeScript

**Using TypeScript Language Server:**
```vim
let g:lsc_server_commands = {
  \ 'javascript': 'typescript-language-server --stdio',
  \ 'typescript': 'typescript-language-server --stdio',
  \ }
```

## Troubleshooting

### Server Not Starting

1. **Verify executable:** Check that the server executable is in `$PATH`
   ```vim
   :echo system('which dart_language_server')
   ```

2. **Check configuration:** Ensure `g:lsc_server_commands` is set correctly
   ```vim
   :echo g:lsc_server_commands
   ```

3. **Check server logs:** Enable trace level
   ```vim
   let g:lsc_trace_level = 'verbose'
   ```

### Completion Not Working

1. **Verify autocomplete is enabled:**
   ```vim
   :echo g:lsc_enable_autocomplete
   ```

2. **Check trigger length:**
   ```vim
   :echo g:lsc_autocomplete_length
   ```

3. **Verify server is running:**
   ```vim
   :echo LSCServerStatus()
   ```

### No Diagnostics

1. **Enable diagnostics:**
   ```vim
   let g:lsc_enable_diagnostics = v:true
   let g:lsc_diagnostic_highlights = v:true
   ```

2. **Verify server language ID:**
   ```vim
   " Check that languageId matches what server expects
   ```

### Hover Information Not Showing

1. **Check hover settings:**
   ```vim
   :echo g:lsc_hover_popup
   ```

2. **Verify server supports hover:**
   - Not all language servers implement hover capability

### Neovim Error Suppression

If error messages are suppressed in Neovim, add:
```vim
set shortmess-=F
```

## See Also

- [Language Server Protocol Specification](https://microsoft.github.io/language-server-protocol/)
- [LSP Implementation List](https://microsoft.github.io/language-server-protocol/implementors/servers/)
- [vim-lsc GitHub Repository](https://github.com/natebosch/vim-lsc)

## License

vim-lsc is licensed under the BSD-3-Clause License. See the LICENSE file in the repository for details.
