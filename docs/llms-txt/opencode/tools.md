# OpenCode Tools

## Overview

Tools let the LLM perform actions in your codebase. All tools enabled by default without permission requirements.

Configure via:
- Global: `tools` option
- Per-agent: Agent-specific overrides
- Permissions: `permission` option

## Built-in Tools

### bash
Execute shell commands.

```json
{
  "tools": {
    "bash": true
  }
}
```

Runs terminal commands like `npm install`, `git status`, etc.

### edit
Modify files via exact string replacements.

```json
{
  "tools": {
    "edit": true
  }
}
```

Primary way LLM modifies code. Performs precise edits by replacing exact text.

### write
Create new files or overwrite existing.

```json
{
  "tools": {
    "write": true
  }
}
```

Allows file creation. Overwrites if file exists.

### read
Read file contents.

```json
{
  "tools": {
    "read": true
  }
}
```

Returns file contents. Supports line ranges for large files.

### grep
Search file contents with regex.

```json
{
  "tools": {
    "grep": true
  }
}
```

Fast codebase search. Full regex syntax, file pattern filtering.

### glob
Find files by pattern.

```json
{
  "tools": {
    "glob": true
  }
}
```

Search using glob patterns (`**/*.js`, `src/**/*.ts`). Results sorted by modification time.

### list
List directory contents.

```json
{
  "tools": {
    "list": true
  }
}
```

Lists files/directories. Accepts glob patterns for filtering.

### lsp (experimental)
Code intelligence via LSP servers.

Requires `OPENCODE_EXPERIMENTAL_LSP_TOOL=true` or `OPENCODE_EXPERIMENTAL=true`.

```json
{
  "tools": {
    "lsp": true
  }
}
```

Operations:
- `goToDefinition`
- `findReferences`
- `hover`
- `documentSymbol`
- `workspaceSymbol`
- `goToImplementation`
- `prepareCallHierarchy`
- `incomingCalls`
- `outgoingCalls`

Configure LSP servers: [LSP Servers docs](/docs/lsp).

### patch
Apply patch files.

```json
{
  "tools": {
    "patch": true
  }
}
```

Applies diffs and patches to codebase.

### skill
Load skill definitions.

```json
{
  "tools": {
    "skill": true
  }
}
```

Loads `SKILL.md` files. Control with `permission.skill`. See [Skills docs](/docs/skills).

### todowrite
Manage todo lists.

```json
{
  "tools": {
    "todowrite": true
  }
}
```

Creates/updates task lists for complex operations. Disabled for subagents by default.

### todoread
Read todo lists.

```json
{
  "tools": {
    "todoread": true
  }
}
```

Reads current todo state. Disabled for subagents by default.

### webfetch
Fetch web content.

```json
{
  "tools": {
    "webfetch": true
  }
}
```

Allows reading web pages. Useful for docs and research.

## Global Configuration

### Disable Tools

```json
{
  "tools": {
    "write": false,
    "bash": false
  }
}
```

### Wildcard Patterns

```json
{
  "tools": {
    "mymcp_*": false  // Disable all MCP tools matching pattern
  }
}
```

## Per-Agent Configuration

Override global settings for specific agents:

```json
{
  "tools": {
    "write": true,
    "bash": true
  },
  "agent": {
    "plan": {
      "tools": {
        "write": false,
        "bash": false
      }
    }
  }
}
```

In markdown:

```markdown
---
description: Read-only analysis
mode: subagent
tools:
  write: false
  edit: false
  bash: false
---

Analyze code without modifications.
```

## MCP Tools

MCP servers provide additional tools. Manage like built-in tools:

```json
{
  "mcp": {
    "my-mcp": {
      "type": "local",
      "command": ["npx", "my-mcp-server"]
    }
  },
  "tools": {
    "my-mcp*": false  // Disable all tools from this MCP
  }
}
```

See [MCP Servers docs](/docs/mcp-servers).

## Custom Tools

Define your own tools in config. See [Custom Tools docs](/docs/custom-tools).

## Internals

### Ignore Patterns

Tools like `grep`, `glob`, `list` use [ripgrep](https://github.com/BurntSushi/ripgrep). Respects `.gitignore` by default.

To include ignored files, create `.ignore` file:

```
!node_modules/
!dist/
!build/
```

This allows searching within normally ignored directories.

## Tool Permissions

Control execution permissions separately from availability:

```json
{
  "permission": {
    "edit": "ask",     // Ask before editing
    "bash": "allow",   // Allow without asking
    "webfetch": "deny" // Deny completely
  }
}
```

Permission levels:
- `"allow"`: Execute without asking
- `"ask"`: Prompt for approval
- `"deny"`: Disable tool

### Per-Command Bash Permissions

```json
{
  "permission": {
    "bash": {
      "git push": "ask",
      "git *": "ask",
      "*": "allow"
    }
  }
}
```

### Per-Agent Permissions

```json
{
  "agent": {
    "plan": {
      "permission": {
        "edit": "deny",
        "bash": "deny"
      }
    }
  }
}
```

See [Permissions docs](/docs/permissions).

## Common Patterns

### Read-Only Agent

```json
{
  "agent": {
    "readonly": {
      "tools": {
        "write": false,
        "edit": false,
        "bash": false
      }
    }
  }
}
```

### Analysis Agent

```json
{
  "agent": {
    "analyze": {
      "tools": {
        "write": false,
        "edit": false,
        "bash": true,  // Allow for running checks
        "read": true,
        "grep": true,
        "glob": true
      }
    }
  }
}
```

### Documentation Agent

```json
{
  "agent": {
    "docs": {
      "tools": {
        "bash": false,
        "write": true,
        "edit": true,
        "webfetch": true  // For research
      }
    }
  }
}
```

## Best Practices

1. **Be selective**: Disable unused tools to reduce context
2. **Use permissions**: Control risky operations (bash, edit)
3. **Per-agent config**: Different tools for different agents
4. **MCP wildcards**: Disable entire MCP servers when not needed
5. **Test carefully**: Verify tool access matches intent
