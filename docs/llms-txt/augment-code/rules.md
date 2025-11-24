# Source: https://docs.augmentcode.com/cli/rules.md

# Rules & Guidelines

> Configure custom rules and guidelines to provide context-aware assistance in Auggie CLI.

## Overview

Auggie automatically loads custom rules and guidelines from several file locations to provide context-aware assistance. These files help Auggie understand your project's conventions, coding standards, and preferences.

<Note>The Auggie CLI uses the same rules system as the VSCode and JetBrains IDE extensions. For more information on IDE specific features like user guidelines, see [Rules & Guidelines for Agent and Chat](/setup-augment/guidelines).</Note>

## Supported Rules Files

Auggie looks for rules files in the following order of precedence:

1. **Custom rules file** (via `--rules` flag): `/path/to/custom-rules.md`
2. **CLAUDE.md**: Compatible with Claude Code and other AI tools
3. **AGENTS.md**: Compatible with Cursor and other AI development tools
4. **Workspace guidelines**: `<workspace_root>/.augment/guidelines.md` (legacy format)
5. **Augment rules folder**: `<workspace_root>/.augment/rules/` - Recursively searches .md files in the directory in the workspace root

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

Rules files in the `.augment/rules/` directory support frontmatter to configure their behavior. Use YAML frontmatter at the beginning of your rule file to specify how the rule should be applied:

| Frontmatter Field | Purpose                                                                       | Options                           | Default        |
| :---------------- | :---------------------------------------------------------------------------- | :-------------------------------- | :------------- |
| `type`            | Controls when the rule is applied                                             | `always_apply`, `agent_requested` | `always_apply` |
| `description`     | Brief description of the rule's purpose (required for `agent_requested` type) | Any text                          | None           |

**Rule Types:**

* **`always_apply`**: Rule contents are automatically included in every user prompt
* **`agent_requested`**: Rule is automatically detected and attached based on the description field when relevant

<Note>Manual rules are not yet supported in the CLI. In the CLI, all rules in `.augment/rules/` are currently treated as `always_apply` rules and automatically included. The `manual` type only works in the IDE extensions where you can use @ mentions to selectively attach rules.</Note>

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

* [Rules & Guidelines for Agent and Chat](/setup-augment/guidelines) - Configure rules in VSCode and JetBrains IDEs
* [CLI Reference](/cli/reference) - Complete command-line reference
* [Workspace Context](/cli/setup-auggie/workspace-context) - Understanding workspace configuration
* [Custom Commands](/cli/custom-commands) - Create reusable command templates
