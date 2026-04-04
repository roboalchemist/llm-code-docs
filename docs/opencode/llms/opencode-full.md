# OpenCode - Complete Documentation

OpenCode is an open source AI coding agent. Terminal-based interface, desktop app, and IDE extension.

## Installation

```bash
# Recommended
curl -fsSL https://opencode.ai/install | bash

# npm
npm install -g opencode-ai

# Homebrew
brew install opencode

# Chocolatey (Windows)
choco install opencode

# Docker
docker run -it --rm ghcr.io/sst/opencode
```

## Quick Start

```bash
cd /path/to/project
opencode
/connect          # Configure provider
/init            # Initialize project
```

## Core Concepts

### Agents
**Primary** (Tab to switch):
- **Build**: Full development, all tools
- **Plan**: Analysis only, no code changes

**Subagents** (@ mention):
- **General**: Research, multi-step tasks
- **Explore**: Fast codebase exploration

### File References
```
How is auth handled in @src/auth.ts?
```

### Bash Commands
```
!ls -la
```

### Commands
- `/connect` - Add providers
- `/models` - Select model
- `/init` - Create AGENTS.md
- `/undo` - Revert changes
- `/redo` - Restore changes
- `/share` - Share conversation
- `/help` - Show help

## Configuration

**Locations** (merged, later overrides):
1. Global: `~/.config/opencode/opencode.json`
2. Project: `./opencode.json`
3. Custom: `OPENCODE_CONFIG` env var

**Basic config:**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-5",
  "theme": "opencode",
  "autoupdate": true
}
```

## Agents

### Define Custom Agent

**JSON:**
```json
{
  "agent": {
    "code-reviewer": {
      "description": "Reviews code for issues",
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-5",
      "temperature": 0.1,
      "tools": {
        "write": false,
        "edit": false
      }
    }
  }
}
```

**Markdown** (`.opencode/agent/review.md`):
```markdown
---
description: Code review agent
mode: subagent
tools:
  write: false
  edit: false
---

Review code for quality and best practices.
```

### Agent Options
- `description` (required): Purpose
- `mode`: "primary", "subagent", "all"
- `model`: Override default
- `prompt`: Custom prompt or `{file:path}`
- `temperature`: 0.0-1.0
- `maxSteps`: Max iterations
- `tools`: Tool overrides
- `permission`: Permission overrides

### Usage
```bash
# Switch primary agents
<Tab>

# Invoke subagent
@general help me find this function

# Navigate sessions
<Leader>+Right  # Next child session
<Leader>+Left   # Previous child session
```

## Tools

### Built-in
- `bash` - Shell commands
- `edit` - File modifications
- `write` - Create files
- `read` - Read files
- `grep` - Search content
- `glob` - Find files
- `list` - List directories
- `patch` - Apply patches
- `skill` - Load skills
- `webfetch` - Fetch web content

### Global Config
```json
{
  "tools": {
    "write": false,
    "bash": false,
    "mymcp_*": false  // Wildcard disable
  }
}
```

### Per-Agent
```json
{
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

## Permissions

```json
{
  "permission": {
    "edit": "ask",  // "allow", "ask", "deny"
    "bash": {
      "git push": "ask",
      "git *": "ask",
      "*": "allow"
    }
  }
}
```

Per-agent:
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

## Commands

### Define Custom Command

**JSON:**
```json
{
  "command": {
    "test": {
      "template": "Run full test suite with coverage",
      "description": "Run tests",
      "agent": "build",
      "model": "anthropic/claude-haiku-4-5"
    }
  }
}
```

**Markdown** (`.opencode/command/test.md`):
```markdown
---
description: Run tests with coverage
agent: build
---

Run the full test suite and show failures.
```

### Template Variables
- `$ARGUMENTS` - All args
- `$1`, `$2`, `$3` - Individual args
- `!`command`` - Shell output
- `@filename` - File contents

### Usage
```
/test
/test MyComponent
```

## MCP Servers

### Local
```json
{
  "mcp": {
    "my-mcp": {
      "type": "local",
      "command": ["npx", "-y", "package-name"],
      "enabled": true,
      "environment": {
        "API_KEY": "{env:MY_API_KEY}"
      }
    }
  }
}
```

### Remote
```json
{
  "mcp": {
    "my-remote": {
      "type": "remote",
      "url": "https://mcp.example.com",
      "headers": {
        "Authorization": "Bearer {env:API_KEY}"
      }
    }
  }
}
```

### OAuth
```json
{
  "mcp": {
    "oauth-server": {
      "type": "remote",
      "url": "https://mcp.example.com",
      "oauth": {
        "clientId": "{env:CLIENT_ID}",
        "clientSecret": "{env:CLIENT_SECRET}"
      }
    }
  }
}
```

Authenticate:
```bash
opencode mcp auth server-name
```

### Manage MCP Tools
```json
{
  "tools": {
    "my-mcp*": false  // Disable globally
  },
  "agent": {
    "special": {
      "tools": {
        "my-mcp*": true  // Enable for specific agent
      }
    }
  }
}
```

## Skills

Create `.opencode/skill/<name>/SKILL.md`:

```markdown
---
name: git-release
description: Create consistent releases
---

## What I do
- Draft release notes from merged PRs
- Propose version bump
```

### Permissions
```json
{
  "permission": {
    "skill": {
      "pr-review": "allow",
      "internal-*": "deny",
      "*": "ask"
    }
  }
}
```

### Disable Skill Tool
```json
{
  "agent": {
    "plan": {
      "tools": {
        "skill": false
      }
    }
  }
}
```

## Providers

### Setup
```bash
/connect
# Select provider
# Enter credentials
```

### Common Providers

**Anthropic Claude:**
```bash
/connect > Anthropic > Claude Pro/Max
# Or Create API Key / Manual entry
```

**OpenAI:**
```bash
# Get key from platform.openai.com/api-keys
/connect > OpenAI
```

**GitHub Copilot:**
```bash
/connect > GitHub Copilot
# Visit github.com/login/device
```

**DeepSeek:**
```bash
# Get key from platform.deepseek.com
/connect > DeepSeek
```

### Cloud Providers

**Amazon Bedrock:**
```bash
AWS_ACCESS_KEY_ID=xxx opencode
# Or AWS_PROFILE or AWS_BEARER_TOKEN_BEDROCK
```

**Google Vertex AI:**
```bash
GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json \
GOOGLE_CLOUD_PROJECT=project-id \
VERTEX_LOCATION=global \
opencode
```

**Azure OpenAI:**
```bash
/connect > Azure
AZURE_RESOURCE_NAME=xxx opencode
```

### Local Models

**Ollama:**
```json
{
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "llama2": {"name": "Llama 2"}
      }
    }
  }
}
```

**LM Studio:**
```json
{
  "provider": {
    "lmstudio": {
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "http://127.0.0.1:1234/v1"
      },
      "models": {
        "model-id": {"name": "Model Name"}
      }
    }
  }
}
```

### Custom Provider
```bash
/connect > Other
# Enter provider ID
# Enter API key
```

```json
{
  "provider": {
    "myprovider": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "My Provider",
      "options": {
        "baseURL": "https://api.myprovider.com/v1",
        "apiKey": "{env:MY_API_KEY}"
      },
      "models": {
        "my-model": {
          "name": "My Model",
          "limit": {
            "context": 200000,
            "output": 65536
          }
        }
      }
    }
  }
}
```

## CLI Reference

### Basic
```bash
opencode                    # Start TUI
opencode /path/to/project  # TUI in specific dir
opencode -c                # Continue last session
opencode -m provider/model # Use specific model
```

### Run Mode
```bash
opencode run "Explain async/await"
opencode run -f config.json "Analyze this"
opencode run --attach http://localhost:4096 "Help"
```

### Agent
```bash
opencode agent create      # Create agent
opencode agent list        # List agents
```

### Auth
```bash
opencode auth login        # Configure provider
opencode auth list         # List providers
opencode auth logout       # Remove provider
```

### MCP
```bash
opencode mcp add           # Add server
opencode mcp list          # List servers
opencode mcp auth [name]   # Authenticate
opencode mcp logout <name> # Remove auth
opencode mcp debug <name>  # Debug issues
```

### Models
```bash
opencode models            # List all models
opencode models anthropic  # List provider models
opencode models --refresh  # Refresh cache
opencode models --verbose  # Show costs
```

### Session
```bash
opencode session list      # List sessions
opencode export [id]       # Export session
opencode import file.json  # Import session
```

### Server
```bash
opencode serve             # Start HTTP server
opencode web               # Start with web UI
```

### Stats
```bash
opencode stats             # Usage statistics
opencode stats --days 7    # Last 7 days
```

## Workflows

### Add Feature
```
<Tab>  # Switch to Plan mode
Describe feature: When user deletes note, flag as deleted...

# Review plan
Sounds good! Make the changes.

<Tab>  # Back to Build mode
```

### Make Changes
```
Add authentication to /settings route.
Use same pattern as @packages/functions/src/notes.ts
```

### Undo/Redo
```
/undo  # Revert changes (including files)
/redo  # Restore changes
```

## Environment Variables

### General
- `OPENCODE_CONFIG` - Config file path
- `OPENCODE_CONFIG_DIR` - Config directory
- `OPENCODE_DISABLE_AUTOUPDATE` - Disable updates
- `OPENCODE_PERMISSION` - Inline permissions JSON
- `OPENCODE_CLIENT` - Client identifier

### Experimental
- `OPENCODE_EXPERIMENTAL` - Enable all experimental
- `OPENCODE_EXPERIMENTAL_LSP_TOOL` - Enable LSP tool
- `OPENCODE_EXPERIMENTAL_FILEWATCHER` - Enable file watcher

## Best Practices

1. **Use Plan mode** for reviewing before changes
2. **@ reference files** for context
3. **Enable only needed MCPs** to save context
4. **Configure permissions** for risky operations
5. **Create custom agents** for specific tasks
6. **Use skills** for reusable instructions
7. **Set up formatters** for code consistency
8. **Commit AGENTS.md** to Git for team sharing

## Links

- Website: https://opencode.ai
- Docs: https://opencode.ai/docs
- GitHub: https://github.com/sst/opencode
- Discord: https://opencode.ai/discord
- Models: https://models.dev
