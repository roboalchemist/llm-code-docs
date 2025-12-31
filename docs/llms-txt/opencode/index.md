# OpenCode Documentation

OpenCode is an open source AI coding agent available as a terminal-based interface, desktop app, or IDE extension.

## Quick Start

### Installation

```bash
# Install script (recommended)
curl -fsSL https://opencode.ai/install | bash

# Or using npm
npm install -g opencode-ai

# Or using Homebrew
brew install opencode
```

### First Run

```bash
# Navigate to your project
cd /path/to/project

# Start OpenCode
opencode

# Configure a provider (recommended: OpenCode Zen)
/connect

# Initialize for your project
/init
```

## Core Concepts

### Agents
- **Build** (default): Full development with all tools enabled
- **Plan**: Analysis mode - suggests changes without modifying code
- **General**: Research and multi-step task execution (subagent)
- **Explore**: Fast codebase exploration (subagent)

Switch agents with Tab key or @ mention subagents.

### Tools
Built-in tools include:
- `bash` - Execute shell commands
- `edit` - Modify files with exact replacements
- `write` - Create new files
- `read` - Read file contents
- `grep` - Search file contents
- `glob` - Find files by pattern
- `webfetch` - Fetch web content
- `skill` - Load reusable skills

### Configuration

Global config: `~/.config/opencode/opencode.json`
Project config: `./opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-5",
  "theme": "opencode",
  "autoupdate": true
}
```

## Key Features

### File References
Use `@` to reference files in prompts:
```
How is auth handled in @src/auth.ts?
```

### Commands
Built-in commands:
- `/connect` - Add providers
- `/models` - Select model
- `/init` - Create AGENTS.md
- `/undo` - Revert changes
- `/redo` - Restore changes
- `/share` - Share conversation
- `/help` - Show help

### MCP Servers
Add external tools via Model Context Protocol:
```json
{
  "mcp": {
    "server-name": {
      "type": "local",
      "command": ["npx", "-y", "package-name"]
    }
  }
}
```

### Custom Agents
Define specialized agents:
```json
{
  "agent": {
    "code-reviewer": {
      "description": "Reviews code for issues",
      "mode": "subagent",
      "tools": {
        "write": false,
        "edit": false
      }
    }
  }
}
```

## Common Workflows

### Add a Feature
```
# Switch to Plan mode
<Tab>

# Describe feature
When a user deletes a note, flag it as deleted in the database.
Create a screen showing deleted notes with undelete/permanent delete options.

# Review and approve plan
Sounds good! Go ahead and make the changes.

# Switch back to Build mode
<Tab>
```

### Make Changes
```
Add authentication to /settings route. Use the same pattern as @packages/functions/src/notes.ts
```

### Undo/Redo
```
# Undo last change
/undo

# Redo change
/redo
```

## Advanced

### Permissions
Control tool permissions:
```json
{
  "permission": {
    "edit": "ask",
    "bash": {
      "git push": "ask",
      "*": "allow"
    }
  }
}
```

### Custom Commands
Define reusable prompts:
```json
{
  "command": {
    "test": {
      "template": "Run full test suite with coverage",
      "agent": "build"
    }
  }
}
```

### Skills
Create reusable instructions in `.opencode/skill/<name>/SKILL.md`:
```markdown
---
name: git-release
description: Create consistent releases
---

## What I do
- Draft release notes from merged PRs
- Propose version bump
```

## Providers

Supports 75+ LLM providers via AI SDK and Models.dev:
- Anthropic Claude
- OpenAI
- Google Gemini
- Amazon Bedrock
- DeepSeek
- OpenRouter
- Local models (Ollama, LM Studio)
- And many more

Configure with `/connect` or environment variables.

## Links

- Website: https://opencode.ai
- GitHub: https://github.com/sst/opencode
- Discord: https://opencode.ai/discord
- Docs: https://opencode.ai/docs
