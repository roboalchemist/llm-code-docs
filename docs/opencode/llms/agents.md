# OpenCode Agents

## Overview

Agents are specialized AI assistants with custom prompts, models, and tool access. Two types:

1. **Primary agents**: Main assistants you interact with (cycle with Tab)
2. **Subagents**: Specialized assistants invoked by primary agents or @ mentions

## Built-in Agents

### Build (Primary)
Default agent with all tools enabled for full development work.

### Plan (Primary)
Analysis agent with restricted permissions. By default:
- File edits: Ask before making changes
- Bash commands: Ask before running

Use for planning without modifying code.

### General (Subagent)
General-purpose agent for:
- Researching complex questions
- Searching for code
- Multi-step tasks

### Explore (Subagent)
Fast codebase exploration agent for:
- Finding files by patterns
- Searching code for keywords
- Answering codebase questions

## Usage

### Primary Agents
- Switch with **Tab** key
- Or use configured `switch_agent` keybind

### Subagents
- Automatically invoked by primary agents
- Manually invoke with @ mention:
  ```
  @general help me search for this function
  ```

### Session Navigation
Navigate between parent and child sessions:
- **Leader+Right**: Cycle forward (parent → child1 → child2 → parent)
- **Leader+Left**: Cycle backward

## Configuration

### JSON Config

```json
{
  "agent": {
    "code-reviewer": {
      "description": "Reviews code for best practices and issues",
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-5",
      "prompt": "You are a code reviewer. Focus on security, performance, maintainability.",
      "temperature": 0.1,
      "tools": {
        "write": false,
        "edit": false
      },
      "permission": {
        "bash": "ask"
      }
    }
  }
}
```

### Markdown Files

Create in `~/.config/opencode/agent/` or `.opencode/agent/`:

**review.md:**
```markdown
---
description: Reviews code for quality and best practices
mode: subagent
model: anthropic/claude-sonnet-4-5
temperature: 0.1
tools:
  write: false
  edit: false
  bash: false
---

You are in code review mode. Focus on:
- Code quality and best practices
- Potential bugs and edge cases
- Performance implications
- Security considerations

Provide constructive feedback without making direct changes.
```

## Agent Options

### Required

- **description**: What the agent does and when to use it

### Optional

- **mode**: "primary", "subagent", or "all" (default: "all")
- **model**: Override default model (e.g., "anthropic/claude-haiku-4-5")
- **prompt**: Custom system prompt or `{file:./prompts/review.txt}`
- **temperature**: 0.0-1.0 (lower = focused, higher = creative)
  - 0.0-0.2: Very focused (analysis, planning)
  - 0.3-0.5: Balanced (general development)
  - 0.6-1.0: Creative (brainstorming)
- **maxSteps**: Max iterations before forced stop
- **tools**: Tool availability overrides
- **permission**: Permission overrides

### Tools Override

```json
{
  "agent": {
    "readonly": {
      "tools": {
        "write": false,
        "edit": false,
        "bash": false,
        "mymcp_*": false  // Wildcard patterns supported
      }
    }
  }
}
```

### Permissions

```json
{
  "agent": {
    "build": {
      "permission": {
        "edit": "ask",
        "bash": {
          "git status": "allow",
          "git *": "ask",
          "*": "ask"
        }
      }
    }
  }
}
```

In markdown:
```markdown
---
permission:
  edit: deny
  bash:
    "git diff": allow
    "git log*": allow
    "*": ask
  webfetch: deny
---
```

### Provider-Specific Options

Pass through to provider (e.g., OpenAI reasoning):
```json
{
  "agent": {
    "deep-thinker": {
      "model": "openai/gpt-5",
      "reasoningEffort": "high",
      "textVerbosity": "low"
    }
  }
}
```

## Default Agent

Set which agent starts by default:

```json
{
  "default_agent": "plan"  // Must be primary agent
}
```

Applies to: TUI, CLI (`opencode run`), desktop app, GitHub Action.

## Creating Agents

### Interactive Creation

```bash
opencode agent create
```

Prompts for:
1. Save location (global/project)
2. Description
3. Tool access
4. Creates markdown file

### List Agents

```bash
opencode agent list
```

## Example Agents

### Documentation Writer

**~/.config/opencode/agent/docs-writer.md:**
```markdown
---
description: Writes and maintains project documentation
mode: subagent
tools:
  bash: false
---

You are a technical writer. Create clear, comprehensive documentation.

Focus on:
- Clear explanations
- Proper structure
- Code examples
- User-friendly language
```

### Security Auditor

**~/.config/opencode/agent/security-auditor.md:**
```markdown
---
description: Performs security audits and identifies vulnerabilities
mode: subagent
tools:
  write: false
  edit: false
---

You are a security expert. Focus on identifying potential security issues.

Look for:
- Input validation vulnerabilities
- Authentication and authorization flaws
- Data exposure risks
- Dependency vulnerabilities
- Configuration security issues
```

### Debug Agent

```json
{
  "agent": {
    "debug": {
      "description": "Focused debugging with investigation tools",
      "mode": "subagent",
      "tools": {
        "write": false,
        "edit": false,
        "bash": true,
        "read": true,
        "grep": true
      }
    }
  }
}
```

## Common Use Cases

- **Build**: Full development with all tools
- **Plan**: Analysis and planning without changes
- **Review**: Code review with read-only + docs
- **Debug**: Investigation with bash and read tools
- **Docs**: Documentation with file ops, no system commands

## Model Selection

OpenCode supports provider/model format (e.g., `anthropic/claude-sonnet-4-5`, `openai/gpt-4`, `deepseek-ai/DeepSeek-V3`).

**Recommendations:**
- **General development:** Claude Sonnet 4.5, GPT-4, DeepSeek V3
- **Fast tasks:** Claude Haiku, GPT-4 Mini
- **Complex reasoning:** Claude Opus 4.5, DeepSeek R1
- **Local/cost-conscious:** Ollama, LM Studio with smaller models

## Session Navigation

Primary and subagent invocations create a session tree:

```
Primary Agent (parent)
├── Subagent 1 (child)
├── Subagent 2 (child)
└── Subagent 3 (child)
```

Navigate with:
- **Leader+Right**: Next session (parent → child1 → child2 → parent)
- **Leader+Left**: Previous session (reverse order)

## Notes

- Agent names from markdown files match filename (e.g., `review.md` → `review`)
- Global config agents override built-in if same name
- Subagents inherit primary agent's model unless overridden
- Temperature defaults: 0.1 for analysis, 0.55 for Qwen models
- Provider-specific options pass through to underlying API (e.g., `reasoningEffort`, `textVerbosity`)
