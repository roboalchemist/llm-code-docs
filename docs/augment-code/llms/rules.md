# Source: https://docs.augmentcode.com/cli/rules.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rules & Guidelines

> Configure custom rules and guidelines to provide context-aware assistance in Auggie CLI.

## Overview

Auggie automatically loads custom rules and guidelines from several file locations to provide context-aware assistance. These files help Auggie understand your project's conventions, coding standards, and preferences.

<Note>The Auggie CLI uses the same rules system as the VSCode and JetBrains IDE extensions. For more information on IDE specific features like user guidelines, see [Rules & Guidelines for Agent and Chat](/setup-augment/guidelines).</Note>

<Note>Looking for specialized domain knowledge? Check out [Skills](/cli/skills) - a standardized way to provide framework-specific guidance, tool usage patterns, and workflow procedures following the agentskills.io specification.</Note>

## Supported Rules Files

Auggie looks for rules files in the following order of precedence:

1. **Custom rules file** (via `--rules` flag): `/path/to/custom-rules.md`
2. **CLAUDE.md**: Compatible with Claude Code and other AI tools
3. **AGENTS.md**: Compatible with Cursor and other AI development tools
4. **Workspace guidelines**: `<workspace_root>/.augment/guidelines.md` (legacy format)
5. **Workspace rules folder**: `<workspace_root>/.augment/rules/` - Recursively searches .md files in the workspace
6. **User rules folder**: `~/.augment/rules/` - Recursively searches .md files for user-wide rules

### User Rules vs Workspace Rules

Rules can be defined at two levels:

| Scope     | Location                           | Availability                        |
| :-------- | :--------------------------------- | :---------------------------------- |
| User      | `~/.augment/rules/`                | Available in all workspaces         |
| Workspace | `<workspace_root>/.augment/rules/` | Available in current workspace only |

**User rules** are stored in your home directory and apply to all projects. Use these for personal preferences, coding style guidelines, or conventions you want to follow across all your work. User rules are always treated as `always_apply` type and are automatically included in every prompt regardless of any frontmatter configuration.

**Workspace rules** are stored in the project repository and apply only to that specific project. Use these for project-specific guidelines that should be shared with your team via version control.

## Rules File Format

Rules files should be written in Markdown format with natural language instructions. Here's the recommended structure:

```markdown  theme={null}
# Project Guidelines

## Code Style
- Use TypeScript for all new JavaScript files
- Follow the existing naming conventions in the codebase
- Add JSDoc comments for all public functions and classes

## Architecture
- Follow the MVC pattern established in the codebase
- Place business logic in service classes
- Keep controllers thin and focused on request/response handling

## Testing
- Write unit tests for all new functions
- Maintain test coverage above 80%
- Use Jest for testing framework

## Dependencies
- Prefer built-in Node.js modules when possible
- Use npm for package management
- Pin exact versions in package.json for production dependencies
```

## Frontmatter Configuration for Rules

Rules files in the `<workspace_root>/.augment/rules/` (workspace) directory support frontmatter to configure their behavior. Use YAML frontmatter at the beginning of your rule file to specify how the rule should be applied:

<Note>User rules in `~/.augment/rules/` are always treated as `always_apply` and do not support other frontmatter types. Frontmatter configuration only affects workspace rules.</Note>

| Frontmatter Field | Purpose                                                                       | Options                           | Default        |
| :---------------- | :---------------------------------------------------------------------------- | :-------------------------------- | :------------- |
| `type`            | Controls when the rule is applied                                             | `always_apply`, `agent_requested` | `always_apply` |
| `description`     | Brief description of the rule's purpose (required for `agent_requested` type) | Any text                          | None           |

**Rule Types:**

* **`always_apply`**: Rule contents are automatically included in every user prompt
* **`agent_requested`**: Rule is automatically detected and attached based on the description field when relevant

<Note>Manual rules are not yet supported in the CLI. In the CLI, workspace rules in `<workspace_root>/.augment/rules/` are currently treated as `always_apply` rules and automatically included. User rules in `~/.augment/rules/` are always `always_apply`. The `manual` type only works in the IDE extensions where you can use @ mentions to selectively attach rules.</Note>

Use `agent_requested` (also called `auto` in IDE extensions) over `always_apply` if you want to optimize context usage. For these rules, the agent will determine the rule is relevant to your current task, ensuring specialized guidelines are available when needed.

**Example with frontmatter:**

```markdown  theme={null}
---
type: always_apply
---

# TypeScript Guidelines

- Use strict mode in all TypeScript files
- Define explicit return types for all functions
- Avoid using `any` type unless absolutely necessary
```

**Agent-requested example:**

```markdown  theme={null}
---
type: agent_requested
description: React component development patterns and best practices
---

# React Component Guidelines

- Use functional components with hooks
- Implement proper TypeScript interfaces for props
- Follow the established folder structure in src/components/
```

## Hierarchical Rules

In addition to workspace-level rules, the agent supports **hierarchical rules** through `AGENTS.md` and `CLAUDE.md` files placed in subdirectories. When working on files in a subdirectory, Augment automatically discovers and applies rule files from that directory and all parent directories.

### How Hierarchical Rules Work

1. When you work on a file, Augment looks for `AGENTS.md` and `CLAUDE.md` in the file's directory
2. It then walks up the directory tree, checking each parent directory for these files
3. All discovered rules are included in the context for that work session
4. The search stops at the workspace root (since workspace root rules are already loaded separately)

### Example Directory Structure

```
my-project/
  AGENTS.md                  <- Always included (workspace root)
  src/
    AGENTS.md                <- Included when working in src/ or subdirectories
    frontend/
      AGENTS.md              <- Included when working in src/frontend/
      App.tsx
    backend/
      AGENTS.md              <- Included when working in src/backend/
      server.ts
  tests/
    AGENTS.md                <- Only included when working in tests/
```

When working on `src/frontend/App.tsx`:

* `src/frontend/AGENTS.md` is loaded (current directory)
* `src/AGENTS.md` is loaded (parent directory)
* `AGENTS.md` at workspace root is loaded via standard rules
* `src/backend/AGENTS.md` and `tests/AGENTS.md` are **not** loaded (different branches)

### Use Cases for Hierarchical Rules

* **Framework-specific guidelines**: Place React-specific rules in your frontend directory and Node.js rules in your backend directory
* **Module-specific conventions**: Define API design patterns in your `api/` directory
* **Test-specific rules**: Add testing conventions that only apply when writing tests
* **Team boundaries**: Different teams can maintain their own coding standards in their directories

### Important Notes

* Only `AGENTS.md` and `CLAUDE.md` files are discovered hierarchically
* Files in `.augment/rules/` are only loaded from the workspace root, not from subdirectories
* Rules are cached per conversation session to avoid duplicate inclusion
* Hierarchical rules are combined with workspace and user rules

## Best Practices for Rules Files

1. **Be Specific**: Provide clear, actionable guidelines rather than vague suggestions
2. **Use Examples**: Include code examples when describing patterns or conventions
3. **Keep Updated**: Regularly review and update rules as your project evolves
4. **Be Concise**: Focus on the most important guidelines to avoid overwhelming the AI
5. **Test Guidelines**: Verify that Auggie follows your rules by testing with sample requests

## Command-Line Flag

You can specify a custom rules file when starting Auggie:

```bash  theme={null}
auggie --rules /path/to/custom-rules.md
```

This will append the specified rules to any workspace guidelines that are automatically loaded.

## See Also

* [Skills](/cli/skills) - Extend capabilities with specialized domain knowledge
* [Rules & Guidelines for Agent and Chat](/setup-augment/guidelines) - Configure rules in VSCode and JetBrains IDEs
* [CLI Reference](/cli/reference) - Complete command-line reference
* [Workspace Context](/cli/setup-auggie/workspace-context) - Understanding workspace configuration
* [Custom Commands](/cli/custom-commands) - Create reusable command templates
