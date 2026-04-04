# OpenCode Configuration

## Config Locations

Configuration files are merged in this order (later overrides earlier):
1. Global: `~/.config/opencode/opencode.json`
2. Project: `./opencode.json` (or nearest Git directory)
3. Custom: Set via `OPENCODE_CONFIG` environment variable
4. Custom directory: Set via `OPENCODE_CONFIG_DIR`

## Format

Supports JSON and JSONC (JSON with Comments):

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  // Your configuration
  "theme": "opencode",
  "model": "anthropic/claude-sonnet-4-5"
}
```

## Core Settings

### Models

```json
{
  "provider": {},
  "model": "anthropic/claude-sonnet-4-5",
  "small_model": "anthropic/claude-haiku-4-5"
}
```

- `model`: Main model for tasks
- `small_model`: Cheaper model for lightweight tasks (title generation, etc)

### TUI Settings

```json
{
  "tui": {
    "scroll_speed": 3,
    "scroll_acceleration": {
      "enabled": true
    }
  }
}
```

- `scroll_acceleration.enabled`: macOS-style scroll acceleration (overrides scroll_speed)
- `scroll_speed`: Multiplier for scroll speed (default: 1, min: 1)

### Theme

```json
{
  "theme": "opencode"
}
```

### Autoupdate

```json
{
  "autoupdate": true  // or false, or "notify"
}
```

## Tools Configuration

### Global Tools

```json
{
  "tools": {
    "write": true,
    "bash": true,
    "edit": false
  }
}
```

### Wildcard Patterns

```json
{
  "tools": {
    "mymcp_*": false  // Disable all tools from mymcp server
  }
}
```

## Agents

### Define Agents

```jsonc
{
  "agent": {
    "code-reviewer": {
      "description": "Reviews code for best practices",
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-5",
      "prompt": "You are a code reviewer...",
      "tools": {
        "write": false,
        "edit": false
      },
      "temperature": 0.1
    }
  }
}
```

### Agent Options

- `description` (required): What the agent does
- `mode`: "primary", "subagent", or "all"
- `model`: Override default model
- `prompt`: Custom system prompt or `{file:./path.txt}`
- `tools`: Tool availability overrides
- `temperature`: 0.0-1.0 (lower = more focused)
- `maxSteps`: Max iterations before stopping
- `permission`: Permission overrides

### Default Agent

```json
{
  "default_agent": "plan"  // Must be a primary agent
}
```

## Commands

### JSON Configuration

```json
{
  "command": {
    "test": {
      "template": "Run the full test suite with coverage",
      "description": "Run tests with coverage",
      "agent": "build",
      "model": "anthropic/claude-haiku-4-5"
    }
  }
}
```

### Command Options

- `template` (required): Prompt template
- `description`: Description shown in TUI
- `agent`: Which agent executes the command
- `subtask`: Force subagent invocation (boolean)
- `model`: Override default model

### Template Variables

- `$ARGUMENTS`: All arguments as single string
- `$1`, `$2`, `$3...`: Individual arguments
- `!`command``: Shell command output
- `@filename`: File contents

## Permissions

```json
{
  "permission": {
    "edit": "ask",     // "allow", "ask", "deny"
    "bash": {
      "git push": "ask",
      "git *": "ask",
      "*": "allow"
    },
    "webfetch": "deny"
  }
}
```

Per-agent permissions:

```json
{
  "agent": {
    "build": {
      "permission": {
        "bash": {
          "git push": "ask"
        }
      }
    }
  }
}
```

## Formatters

```json
{
  "formatter": {
    "prettier": {
      "disabled": true
    },
    "custom-prettier": {
      "command": ["npx", "prettier", "--write", "$FILE"],
      "environment": {
        "NODE_ENV": "development"
      },
      "extensions": [".js", ".ts", ".jsx", ".tsx"]
    }
  }
}
```

## MCP Servers

### Local MCP

```json
{
  "mcp": {
    "my-mcp": {
      "type": "local",
      "command": ["npx", "-y", "package-name"],
      "enabled": true,
      "environment": {
        "API_KEY": "{env:MY_API_KEY}"
      },
      "timeout": 5000
    }
  }
}
```

### Remote MCP

```json
{
  "mcp": {
    "my-remote": {
      "type": "remote",
      "url": "https://mcp.example.com",
      "enabled": true,
      "headers": {
        "Authorization": "Bearer {env:API_KEY}"
      },
      "oauth": {
        "clientId": "{env:CLIENT_ID}",
        "clientSecret": "{env:CLIENT_SECRET}",
        "scope": "tools:read"
      }
    }
  }
}
```

## Sharing

```json
{
  "share": "manual"  // "auto", "manual", or "disabled"
}
```

## Instructions

```json
{
  "instructions": [
    "CONTRIBUTING.md",
    "docs/guidelines.md",
    ".cursor/rules/*.md"
  ]
}
```

## Provider Management

### Disable Providers

```json
{
  "disabled_providers": ["openai", "gemini"]
}
```

### Enable Only Specific Providers

```json
{
  "enabled_providers": ["anthropic", "openai"]
}
```

Note: `disabled_providers` takes priority over `enabled_providers`.

## Variable Substitution

### Environment Variables

```json
{
  "model": "{env:OPENCODE_MODEL}",
  "provider": {
    "anthropic": {
      "options": {
        "apiKey": "{env:ANTHROPIC_API_KEY}"
      }
    }
  }
}
```

### File Contents

```json
{
  "instructions": ["./custom-instructions.md"],
  "provider": {
    "openai": {
      "options": {
        "apiKey": "{file:~/.secrets/openai-key}"
      }
    }
  }
}
```

## Keybinds

```json
{
  "keybinds": {
    "leader": "ctrl+x",
    "switch_agent": "tab",
    "new_session": "ctrl+x n",
    "undo": "ctrl+x u"
  }
}
```

## Environment Variables

Common environment variables:

- `OPENCODE_CONFIG`: Path to config file
- `OPENCODE_CONFIG_DIR`: Path to config directory
- `OPENCODE_CONFIG_CONTENT`: Inline JSON config
- `OPENCODE_DISABLE_AUTOUPDATE`: Disable auto-updates
- `OPENCODE_PERMISSION`: Inline permissions JSON
- `OPENCODE_CLIENT`: Client identifier (default: "cli")

## Schema Validation

Config uses schema from https://opencode.ai/config.json for editor autocomplete and validation.
