# OpenCode MCP Servers

## Overview

MCP (Model Context Protocol) adds external tools to OpenCode. Supports local and remote servers.

**Caveat**: MCP servers add to context. Be selective - some servers (like GitHub MCP) can exceed context limits.

## Configuration

Define in `opencode.json` under `mcp`:

```jsonc
{
  "mcp": {
    "server-name": {
      "type": "local",  // or "remote"
      "enabled": true,
      // ... type-specific options
    }
  }
}
```

## Local MCP Servers

### Basic Configuration

```json
{
  "mcp": {
    "my-local-mcp": {
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

### Options

| Option | Type | Required | Description |
|--------|------|----------|-------------|
| `type` | string | Y | Must be "local" |
| `command` | array | Y | Command and args to run server |
| `enabled` | boolean | N | Enable/disable on startup |
| `environment` | object | N | Environment variables |
| `timeout` | number | N | Timeout in ms (default: 5000) |

### Example: MCP Everything

```json
{
  "mcp": {
    "mcp_everything": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-everything"]
    }
  }
}
```

Usage:
```
use the mcp_everything tool to add 3 and 4
```

## Remote MCP Servers

### Basic Configuration

```json
{
  "mcp": {
    "my-remote-mcp": {
      "type": "remote",
      "url": "https://mcp.example.com",
      "enabled": true,
      "headers": {
        "Authorization": "Bearer {env:API_KEY}"
      }
    }
  }
}
```

### Options

| Option | Type | Required | Description |
|--------|------|----------|-------------|
| `type` | string | Y | Must be "remote" |
| `url` | string | Y | MCP server URL |
| `enabled` | boolean | N | Enable/disable on startup |
| `headers` | object | N | HTTP headers |
| `oauth` | object/false | N | OAuth config or false to disable |
| `timeout` | number | N | Timeout in ms (default: 5000) |

## OAuth Authentication

### Automatic OAuth

Most servers auto-detect OAuth. No config needed:

```json
{
  "mcp": {
    "my-oauth-server": {
      "type": "remote",
      "url": "https://mcp.example.com/mcp"
    }
  }
}
```

OpenCode will:
1. Detect 401 response
2. Use Dynamic Client Registration (RFC 7591) if supported
3. Store tokens securely

### Pre-registered Credentials

If you have client credentials:

```json
{
  "mcp": {
    "my-oauth-server": {
      "type": "remote",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "clientId": "{env:MCP_CLIENT_ID}",
        "clientSecret": "{env:MCP_CLIENT_SECRET}",
        "scope": "tools:read tools:execute"
      }
    }
  }
}
```

### OAuth Options

| Option | Type | Description |
|--------|------|-------------|
| `oauth` | object/false | OAuth config or false to disable |
| `clientId` | string | OAuth client ID |
| `clientSecret` | string | OAuth client secret |
| `scope` | string | OAuth scopes |

### Manual Authentication

```bash
# Authenticate with server
opencode mcp auth my-oauth-server

# List servers and auth status
opencode mcp list

# Remove credentials
opencode mcp logout my-oauth-server
```

Tokens stored in `~/.local/share/opencode/mcp-auth.json`.

### Disable OAuth

For API key-based servers:

```json
{
  "mcp": {
    "my-api-key-server": {
      "type": "remote",
      "url": "https://mcp.example.com/mcp",
      "oauth": false,
      "headers": {
        "Authorization": "Bearer {env:MY_API_KEY}"
      }
    }
  }
}
```

### Debugging OAuth

```bash
# View auth status
opencode mcp auth list

# Debug specific server
opencode mcp debug my-oauth-server
```

## Managing MCP Tools

### Global Enable/Disable

```json
{
  "mcp": {
    "my-mcp-foo": {
      "type": "local",
      "command": ["bun", "x", "foo"]
    }
  },
  "tools": {
    "my-mcp-foo": false  // Disable globally
  }
}
```

### Wildcard Patterns

```json
{
  "tools": {
    "my-mcp*": false  // Disable all matching
  }
}
```

Glob patterns:
- `*`: Zero or more characters
- `?`: Exactly one character
- Literal match: All other characters

### Per-Agent

Disable globally, enable for specific agents:

```json
{
  "mcp": {
    "my-mcp": {
      "type": "local",
      "command": ["bun", "x", "my-mcp-command"],
      "enabled": true
    }
  },
  "tools": {
    "my-mcp*": false
  },
  "agent": {
    "my-agent": {
      "tools": {
        "my-mcp*": true
      }
    }
  }
}
```

## Example Servers

### Sentry

```json
{
  "mcp": {
    "sentry": {
      "type": "remote",
      "url": "https://mcp.sentry.dev/mcp",
      "oauth": {}
    }
  }
}
```

Authenticate:
```bash
opencode mcp auth sentry
```

Usage:
```
Show me latest unresolved issues. use sentry
```

### Context7

Free docs search:

```json
{
  "mcp": {
    "context7": {
      "type": "remote",
      "url": "https://mcp.context7.com/mcp"
    }
  }
}
```

With API key for higher limits:

```json
{
  "mcp": {
    "context7": {
      "type": "remote",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "{env:CONTEXT7_API_KEY}"
      }
    }
  }
}
```

Usage:
```
Configure Cloudflare Worker to cache JSON for 5 minutes. use context7
```

Or add to AGENTS.md:
```markdown
When you need to search docs, use `context7` tools.
```

### Grep by Vercel

Search GitHub code:

```json
{
  "mcp": {
    "gh_grep": {
      "type": "remote",
      "url": "https://mcp.grep.app"
    }
  }
}
```

Usage:
```
How to set custom domain in SST Astro? use gh_grep
```

Or add to AGENTS.md:
```markdown
If unsure how to do something, use `gh_grep` to search GitHub examples.
```

## CLI Commands

```bash
# Add MCP server
opencode mcp add

# List servers
opencode mcp list

# Authenticate
opencode mcp auth [name]

# List OAuth servers
opencode mcp auth list

# Logout
opencode mcp logout <name>

# Debug OAuth
opencode mcp debug <name>
```

## Best Practices

1. **Be selective**: MCP servers add context - only enable what you need
2. **Use per-agent**: Enable specific servers for specific agents
3. **Test connection**: Use `opencode mcp debug` to troubleshoot
4. **Document usage**: Add to AGENTS.md when server should be used
5. **Monitor context**: Watch for context limit issues with large servers

## Variable Substitution

Use environment variables in config:

```json
{
  "mcp": {
    "my-server": {
      "environment": {
        "API_KEY": "{env:MY_API_KEY}"
      },
      "headers": {
        "Authorization": "Bearer {env:AUTH_TOKEN}"
      }
    }
  }
}
```
