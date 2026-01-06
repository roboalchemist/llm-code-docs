# Jedi Language Server Documentation

> Language Server Protocol wrapper around the Jedi static analysis library for Python

**Repository:** https://github.com/pappasam/jedi-language-server
**License:** MIT
**Python:** >= 3.9
**Latest Version:** Check PyPI for current version

## Overview

Jedi Language Server (JLS) is a Python Language Server Protocol (LSP) implementation powered by the Jedi static analysis library. It provides intelligent code completion, navigation, and analysis capabilities through LSP.

Key features:
- Fast, accurate Python code completion
- Go to definition/references support
- Hover documentation
- Symbol renaming
- Code actions (extract variable/function)
- Jupyter notebook support
- Minimal dependencies (only Jedi-based)

## Quick Start

### Installation

```bash
# Via pip
pip install -U jedi-language-server

# Via pipx (recommended - keeps dependencies isolated)
pipx install jedi-language-server
```

### Editor Integration

Jedi Language Server is automatically integrated in:
- **VS Code:** Set `python.languageServer` to `Jedi`
- **Neovim:** Supported via nvim-lspconfig
- **Vim:** Use ALE or vim-lsp
- **Emacs:** Use lsp-jedi, eglot, or lsp-bridge

## Documentation Files

- **README.md** - Complete installation, configuration, and usage guide

## Features

### Language Server Protocol Support

- `completionItem/resolve` - Resolve completion items for additional info
- `textDocument/codeAction` - Extract variable and function refactoring
- `textDocument/completion` - Code completion with detailed information
- `textDocument/definition` - Go to definition support
- `textDocument/documentHighlight` - Highlight document symbols
- `textDocument/documentSymbol` - Document-level symbol navigation
- `textDocument/hover` - Hover documentation display
- `textDocument/publishDiagnostics` - Error and warning diagnostics
- `textDocument/references` - Find all references
- `textDocument/rename` - Symbol renaming (with workspace support)
- `textDocument/signatureHelp` - Function signature assistance
- `workspace/executeCommand` - Custom command execution
- `workspace/symbol` - Workspace-level symbol search

### Code Actions

- **Extract Variable** - Refactor code by extracting expressions into variables
- **Extract Function** - Extract code blocks into separate functions
- Customizable naming patterns for extracted entities

### Customizable Configuration

Supports extensive initialization options:
- Code action naming patterns
- Completion settings (snippets, eager resolution, pattern ignoring)
- Diagnostic controls (enable per event type)
- Hover behavior customization per symbol type
- Jedi-specific settings (auto-import, case sensitivity, debug mode)
- Workspace paths and environment configuration
- Symbol search limits

## Configuration

Jedi Language Server uses LSP initialization options for configuration:

```json
{
  "initializationOptions": {
    "codeAction": {
      "nameExtractVariable": "jls_extract_var",
      "nameExtractFunction": "jls_extract_def"
    },
    "completion": {
      "disableSnippets": false,
      "resolveEagerly": false,
      "ignorePatterns": []
    },
    "diagnostics": {
      "enable": false,
      "didOpen": true,
      "didChange": true,
      "didSave": true
    },
    "hover": {
      "enable": true
    },
    "jediSettings": {
      "autoImportModules": [],
      "caseInsensitiveCompletion": true,
      "debug": false
    },
    "workspace": {
      "extraPaths": [],
      "environmentPath": "/path/to/venv/bin/python",
      "symbols": {
        "ignoreFolders": [".nox", ".tox", ".venv", "__pycache__", "venv"]
      }
    }
  }
}
```

## Philosophy

Jedi Language Server focuses on quality over breadth:
- **Single analyzer focus:** By only supporting Jedi, the project can focus on supporting all Jedi features
- **Minimal dependencies:** Avoids exposing broken third-party dependencies
- **Simplicity:** Straightforward implementation focused on core LSP features

## Community

The project is actively maintained with regular updates and community contributions.

---

**Documentation extracted:** 2026-01-06T14:25:00.649109

**Source:** https://github.com/pappasam/jedi-language-server

For the latest information, visit the official repository.
