# Source: https://docs.augmentcode.com/cli/custom-commands.md

# Custom Slash Commands

> Create and manage custom slash commands for frequently-used prompts and workflows.

## About Custom Slash Commands

Custom slash commands let you create reusable prompts stored as Markdown files that Auggie can run. You can organize commands by scope (workspace or user) and use directory structures for namespacing.

### Syntax

```
/<command-name> [arguments]
```

### Parameters

| Parameter        | Description                              |
| :--------------- | :--------------------------------------- |
| `<command-name>` | Name derived from the Markdown filename  |
| `[arguments]`    | Optional arguments passed to the command |

## Command Types and Locations

Custom commands are stored in markdown files and can be placed in multiple locations with a specific order of precedence:

### Command Locations (in order of precedence)

1. **User Commands**: `~/.augment/commands/<name>.md` (user)
2. **Workspace Commands**: `./.augment/commands/<name>.md` (workspace)
3. **Claude Code Commands**: `./.claude/commands/<name>.md` (.claude)

### User Commands

Commands available across all your projects. These are user-wide and persist across different workspaces.

**Location**: `~/.augment/commands/`

```sh  theme={null}
# Create a global command
mkdir -p ~/.augment/commands
echo "Review this code for security vulnerabilities:" > ~/.augment/commands/security-review.md
```

### Workspace Commands

Commands stored in your repository and shared with your team. These are workspace-specific and can be committed to version control.

**Location**: `./.augment/commands/`

```sh  theme={null}
# Create a workspace command
mkdir -p .augment/commands
echo "Analyze this code for performance issues and suggest optimizations:" > .augment/commands/optimize.md
```

### Claude Code Compatibility

Auggie automatically detects and supports commands from `./.claude/commands/` for compatibility with existing Claude Code setups. This allows teams already using Claude Code to continue using their existing command libraries without modification.

**Location**: `./.claude/commands/` and `~/.claude/commands/`

**Migration**: While `./.claude/commands/` is supported for compatibility, we recommend migrating to `./.augment/commands/` for new projects to maintain consistency with Auggie's naming conventions.

## Features

### Namespacing

Organize commands in subdirectories. Commands from nested directories can be accessed using the `namespace:command` syntax, where the namespace corresponds to the subdirectory name.

For example, a file at `.augment/commands/frontend/component.md` creates the command `/frontend:component`.

Conflicts between user and workspace level commands are not supported and will be defined in order of precedence above.

### Arguments

Pass dynamic values to commands.

```markdown  theme={null}
# Command definition
echo 'Fix issue following our coding standards' > .augment/commands/fix-issue.md

# Usage
> /fix-issue 123
```

### Frontmatter

Command files support frontmatter for metadata:

| Frontmatter     | Purpose                                                                    | Default                             |
| :-------------- | :------------------------------------------------------------------------- | :---------------------------------- |
| `description`   | Brief description of the command                                           | Uses the first line from the prompt |
| `argument-hint` | Expected arguments format that will be displayed after typing in a command | None                                |
| `model`         | Specify the model to run this command with (overrides the CLI default)     | Uses the CLI default model          |

**File**: `~/.augment/commands/deploy-staging.md`

```markdown  theme={null}
---
description: Deploy the application to staging with health checks
argument-hint: [branch-name]
model: gpt-4o
---

Deploy the application to the staging environment:

1. Run all tests to ensure code quality
2. Build the application for production
3. Deploy to staging server
4. Run health checks to verify deployment
5. Send notification to team channel
```

## Command Line Execution

We also provide the ability to execute custom commands from the command line using the `auggie command <your_command>` or list them with `auggie command list`. For complete command-line reference, see [CLI Reference for Custom Commands](/cli/reference#custom-commands).

```sh  theme={null}
# Execute a custom command
auggie command deploy-staging

# List all available commands (including custom ones)
auggie command list
```

Custom commands appear in the help output with their descriptions:

```
Available custom commands:
  auggie command deploy-staging    # Deploy the application to staging
  auggie command security-review   # Review code for security vulnerabilities
```

## Example Commands

For ready-to-use examples of custom slash commands, including code review templates, bug fix guides, and feature implementation plans, see:

**[Custom Commands Examples](/cli/custom-commands-examples)**

## Best Practices

1. **Use kebab-case naming** for command names (e.g., `deploy-staging`, `run-tests`)
2. **Keep names descriptive** but concise, avoiding spaces and special characters
3. **Use meaningful prefixes** for related commands (e.g., `deploy-staging`, `deploy-production`)
4. **Include clear descriptions** in frontmatter for better discoverability
5. **Break complex workflows** into numbered steps for clarity
6. **Use user commands** (`~/.augment/commands/`) for personal workflows across all projects
7. **Use workspace commands** (`./.augment/commands/`) for team-shared, project-specific tasks
8. **Organize with subdirectories** for related command groups using namespacing
9. **Document command purpose** and expected outcomes clearly
10. **Version your commands** when making significant changes

## See Also

* [Custom Commands Examples](/cli/custom-commands-examples) - Ready-to-use command templates and examples
* [Interactive Mode Slash Commands](/cli/interactive#slash-commands) - Learn about Auggie's interactive terminal features
* [CLI Reference for Custom Commands](/cli/reference#custom-commands) - Complete reference for command-line flags
