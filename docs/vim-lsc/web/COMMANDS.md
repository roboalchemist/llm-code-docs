# vim-lsc Commands Reference

## Navigation Commands

### `:LSClientGoToDefinition`
Jump to the definition of the symbol under the cursor.

**Usage:**
```vim
:LSClientGoToDefinition
```

**Keybinding:** `<C-]>` (when auto-map enabled)

---

### `:LSClientGoToDefinitionSplit`
Open the definition of the symbol under the cursor in a split window.

**Usage:**
```vim
:LSClientGoToDefinitionSplit
```

**Keybindings:**
- `<C-W>]`
- `<C-W><C-]>`

---

## Reference Handling Commands

### `:LSClientFindReferences`
Populate the quickfix list with all references to the symbol under the cursor.

**Usage:**
```vim
:LSClientFindReferences
```

**Keybinding:** `gr` (when auto-map enabled)

**Notes:**
- Results appear in the quickfix list
- Use `:copen` to view the quickfix list
- Navigate with `:cn` (next) and `:cp` (previous)

---

### `:LSClientNextReference`
Navigate to the next highlighted reference (when reference highlighting is enabled).

**Usage:**
```vim
:LSClientNextReference
```

**Keybinding:** `<C-n>` (when auto-map enabled)

---

### `:LSClientPreviousReference`
Navigate to the previous highlighted reference.

**Usage:**
```vim
:LSClientPreviousReference
```

**Keybinding:** `<C-p>` (when auto-map enabled)

---

## Symbol Navigation Commands

### `:LSClientFindImplementations`
Jump to the implementation(s) of the symbol under the cursor.

**Usage:**
```vim
:LSClientFindImplementations
```

**Keybinding:** `gI` (when auto-map enabled)

**Use Cases:**
- Find where a method is implemented
- Locate interface implementations
- Find overridden methods

---

### `:LSClientDocumentSymbol`
Display all symbols in the current document (functions, classes, variables).

**Usage:**
```vim
:LSClientDocumentSymbol
```

**Keybinding:** `go` (when auto-map enabled)

**Notes:**
- Results appear in the location list
- Use `:lopen` to view the location list
- Navigate with `:ln` (next) and `:lp` (previous)

---

### `:LSClientWorkspaceSymbol`
Search for symbols across the entire workspace.

**Usage:**
```vim
:LSClientWorkspaceSymbol
```

**Keybinding:** `gS` (when auto-map enabled)

**Behavior:**
- Prompts for search term
- Results appear in the quickfix list
- Populates quickfix with matching symbols

---

## Information Commands

### `:LSClientShowHover`
Display documentation and type information for the symbol under the cursor.

**Usage:**
```vim
:LSClientShowHover
```

**Keybinding:** `K` (when auto-map enabled)

**Display Modes:**
- Floating window (Neovim)
- Preview window (Vim 8)

**Configuration:**
```vim
let g:lsc_hover_popup = v:true  " Use floating window
let g:lsc_preview_split_direction = 'above'  " Window direction
```

---

## Code Actions and Refactoring

### `:LSClientFindCodeActions`
Show available code actions at the current cursor position.

**Usage:**
```vim
:LSClientFindCodeActions
```

**Keybinding:** `ga` (when auto-map enabled)

**Functionality:**
- Quick fixes for errors
- Refactoring suggestions
- Linter suggestions
- Custom code actions provided by language server

**Interaction:**
- Select an action from the menu
- Action is applied to the buffer

---

### `:LSClientRename`
Rename the symbol under the cursor throughout the document/workspace.

**Usage:**
```vim
:LSClientRename
```

**Keybinding:** `gR` (when auto-map enabled)

**Behavior:**
- Prompts for new name
- Renames all occurrences
- Updates workspace as needed

---

## Signature Help

### `:LSClientSignatureHelp`
Display the signature of the function being called.

**Usage:**
```vim
:LSClientSignatureHelp
```

**Keybinding:** `gm` (when auto-map enabled)

**Display:**
- Function parameters
- Parameter types
- Return type
- Documentation

---

## Diagnostics Commands

### `:LSClientAllDiagnostics`
Populate the quickfix list with all diagnostics from all open buffers.

**Usage:**
```vim
:LSClientAllDiagnostics
```

**Notes:**
- Shows errors, warnings, and hints
- Results appear in quickfix list
- Use `:copen` to view

---

### `:LSClientWindowDiagnostics`
Show diagnostics for the current window in the location list.

**Usage:**
```vim
:LSClientWindowDiagnostics
```

**Notes:**
- Window-specific diagnostics
- Results in location list
- Use `:lopen` to view

---

### `:LSClientLineDiagnostics`
Display diagnostics for the current line.

**Usage:**
```vim
:LSClientLineDiagnostics
```

**Display:**
- Message echoed in Vim message area
- Shows all diagnostics on current line
- Includes errors, warnings, and hints

---

### `:LSClientEnableDiagnosticHighlights`
Enable highlighting of diagnostic locations in the buffer.

**Usage:**
```vim
:LSClientEnableDiagnosticHighlights
```

**Effects:**
- Errors and warnings are highlighted
- Hover shows diagnostic messages
- Integration with quickfix

---

### `:LSClientDisableDiagnosticHighlights`
Disable diagnostic highlighting.

**Usage:**
```vim
:LSClientDisableDiagnosticHighlights
```

---

## Server Management Commands

### `:LSClientRestartServer`
Restart the language server for the current buffer's filetype.

**Usage:**
```vim
:LSClientRestartServer
```

**Use Cases:**
- Server becomes unresponsive
- Configuration changes
- Server crashes

---

### `:LSClientDisable`
Temporarily disable the language server.

**Usage:**
```vim
:LSClientDisable
```

**Effects:**
- Server stops processing requests
- No completions or diagnostics
- Server can be re-enabled

---

### `:LSClientEnable`
Re-enable a previously disabled language server.

**Usage:**
```vim
:LSClientEnable
```

---

## Querying Server Status

### `LSCServerStatus()`
Get the current status of the language server.

**Usage:**
```vim
:echo LSCServerStatus()
```

**Return Values:**
- `'starting'` - Server is initializing
- `'running'` - Server is active
- `'exiting'` - Server is shutting down
- `'restoring'` - Server is recovering
- `'exited'` - Server has exited gracefully
- `'unexpected exit'` - Server crashed
- `'failed'` - Server failed to start

---

## Command Examples

### Example 1: Complete Navigation Workflow
```vim
" Jump to definition
<C-]>

" Find all references
gr

" Navigate references with <C-n> and <C-p>
<C-n>
<C-p>

" Show hover information
K

" Rename symbol
gR
```

### Example 2: Diagnostics Workflow
```vim
" Show all diagnostics
:LSClientAllDiagnostics

" Enable diagnostic highlighting
:LSClientEnableDiagnosticHighlights

" Show current line diagnostics
:LSClientLineDiagnostics

" Find code actions
ga
```

### Example 3: Code Exploration
```vim
" Show document symbols
go

" Search workspace symbols
gS

" Find implementations
gI

" Show signature help
gm
```

---

## Mapping Custom Keybindings

Override default keybindings in your configuration:

```vim
let g:lsc_map_keys = {
  \ 'goToDefinition': '<Leader>d',
  \ 'findReferences': '<Leader>r',
  \ 'findImplementations': '<Leader>i',
  \ 'findCodeActions': '<Leader>a',
  \ 'rename': '<Leader>n',
  \ 'showHover': '<Leader>h',
  \ }
```

Or disable specific mappings by setting to empty string:
```vim
let g:lsc_map_keys = {
  \ 'findCodeActions': '',  " Disable code actions mapping
  \ }
```
