# OpenCode Documentation

OpenCode is an open-source AI coding agent providing terminal-based interface, desktop app, and IDE extension capabilities for developers. Built with TypeScript, MIT licensed, and supporting 75+ LLM providers.

## Installation

### Installation Methods

```bash
# Install script (recommended)
curl -fsSL https://opencode.ai/install | bash

# npm
npm install -g opencode-ai

# Homebrew (macOS/Linux)
brew install opencode

# Chocolatey (Windows)
choco install opencode

# Docker
docker run -it --rm ghcr.io/sst/opencode

# Arch Linux (paru)
paru -S opencode

# Or use any Node package manager
pnpm add -g opencode-ai
bun add -g opencode-ai
yarn global add opencode-ai
```

## Quick Start

```bash
# Navigate to your project
cd /path/to/project

# Start OpenCode
opencode

# Configure a provider
/connect

# Initialize project analysis
/init
```

## Core Concepts

### Primary Agents
- **Build** (default): Full development capabilities with all tools enabled
- **Plan**: Analysis-only mode - generates implementation strategies without modifying code

Switch between primary agents with Tab key.

### Subagents
Invoke specialized agents via `@mention`:
- **General**: Research and multi-step task execution
- **Explore**: Fast codebase exploration

### Built-in Tools
- `bash` - Execute shell commands
- `edit` - Modify files via exact string replacements
- `write` - Create new files
- `read` - Read file contents (supports line ranges)
- `grep` - Search file contents with regex
- `glob` - Find files by pattern
- `list` - List directory contents
- `patch` - Apply patch files
- `skill` - Load reusable skills
- `webfetch` - Fetch web content

### Configuration Locations (Merged, Later Overrides)
1. Global: `~/.config/opencode/opencode.json`
2. Project: `./opencode.json`
3. Environment: `OPENCODE_CONFIG` variable

### Basic Configuration Example

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
Use `@` syntax to reference files in prompts:
```
How is auth handled in @src/auth.ts?
```

### Built-in Commands
- `/connect` - Add or configure providers
- `/models` - Select which model to use
- `/init` - Create AGENTS.md project analysis
- `/undo` - Revert last changes (including files)
- `/redo` - Restore changes
- `/share` - Share conversation with others
- `/help` - Display help information

### Image Support
Drag and drop images or use `![image](path)` for design references in prompts.

## Common Workflows

### Add a Feature (Plan-First Approach)

```
# Switch to Plan mode
<Tab>

# Describe feature
When a user deletes a note, flag as deleted in the database.
Create a screen showing deleted notes with undelete/permanent delete options.

# Review plan
Sounds good! Make the changes.

# Switch back to Build mode
<Tab>
```

### Make Targeted Changes

```
Add authentication to /settings route.
Use the same pattern as @packages/functions/src/notes.ts
```

### Undo/Redo Operations

```
# Undo last change (reverts all modifications)
/undo

# Restore changes
/redo
```

## Permissions & Safety

### Control Tool Access

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

Permission levels:
- `"allow"` - Allow without asking
- `"ask"` - Prompt for confirmation
- `"deny"` - Block completely

## Providers

OpenCode supports 75+ LLM providers including:

**Major Providers:**
- Anthropic Claude
- OpenAI
- Google Gemini
- DeepSeek
- Together AI
- OpenRouter
- Z.AI
- OpenCode Zen (curated, tested models)

**Cloud Platforms:**
- Amazon Bedrock
- Google Vertex AI
- Azure OpenAI

**Local Models:**
- Ollama
- LM Studio

Configure providers with `/connect` command or environment variables.

## Advanced Features

### Custom Agents

Define specialized agents in JSON or Markdown:

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

### Custom Commands

Create reusable commands:

**JSON:**
```json
{
  "command": {
    "test": {
      "template": "Run full test suite with coverage",
      "description": "Run tests",
      "agent": "build"
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

### MCP Servers

Integrate external tools via Model Context Protocol:

**Local Server:**
```json
{
  "mcp": {
    "my-mcp": {
      "type": "local",
      "command": ["npx", "-y", "package-name"],
      "environment": {
        "API_KEY": "{env:MY_API_KEY}"
      }
    }
  }
}
```

**Remote Server:**
```json
{
  "mcp": {
    "my-remote": {
      "type": "remote",
      "url": "https://mcp.example.com"
    }
  }
}
```

## Best Practices

1. **Use Plan mode** for reviewing changes before implementation
2. **Reference files** with `@` for proper context
3. **Enable only needed MCPs** to conserve context tokens
4. **Configure permissions** for risky operations
5. **Create custom agents** for specific task types
6. **Use skills** for reusable workflows
7. **Set up formatters** for code consistency
8. **Commit AGENTS.md** to version control for team sharing

## Links

- **Website:** https://opencode.ai
- **Documentation:** https://opencode.ai/docs
- **GitHub:** https://github.com/sst/opencode
- **Discord:** https://opencode.ai/discord
- **Models:** https://models.dev
