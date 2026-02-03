# Source: https://docs.augmentcode.com/cli/skills.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent Skills

> Extend Auggie's capabilities with specialized domain knowledge using the agentskills.io specification.

## Overview

Skills provide a standardized way to give Auggie specialized domain knowledge and capabilities. Following the [agentskills.io](https://agentskills.io) specification, skills are modular packages of guidance, resources, and context that help the agent understand specific domains or workflows.

## What are Skills?

Skills are self-contained packages that provide:

* **Specialized knowledge**: Domain-specific guidance and best practices
* **Contextual resources**: Links to documentation, APIs, or tools
* **Workflow patterns**: Step-by-step procedures for common tasks
* **Tool usage guidance**: How to use specific tools or frameworks

Unlike rules (which provide general guidelines), skills are designed to be:

* **Discoverable**: The agent can see what skills are available through their metadata
* **Modular**: Each skill is independent and can be added or removed easily
* **Standardized**: Following the agentskills.io spec ensures compatibility across AI tools

## Skill File Structure

Skills are defined in `SKILL.md` files located in the `.augment/skills/` or `.claude/skills/` directories (in either your workspace or home directory). Each skill must be in its own subdirectory:

```
.augment/skills/
  ├── python-testing/
  │   └── SKILL.md
  ├── api-design/
  │   └── SKILL.md
  └── database-migrations/
      └── SKILL.md
```

### SKILL.md Format

Each `SKILL.md` file must include YAML frontmatter with required metadata:

**Example SKILL.md file:**

```markdown  theme={null}
---
name: python-testing
description: Best practices for writing and running Python tests with pytest
---

# Python Testing Skill

This skill provides guidance on writing effective Python tests.
```

The file content after the frontmatter can include:

* Markdown headings and text
* Code examples (using code blocks)
* Lists and other markdown formatting

### Required Frontmatter Fields

| Field         | Description                            | Requirements                                                                        |
| :------------ | :------------------------------------- | :---------------------------------------------------------------------------------- |
| `name`        | Skill identifier                       | 1-64 characters, lowercase alphanumeric and hyphens only, must match directory name |
| `description` | What the skill does and when to use it | 1-1024 characters, helps the agent understand when to apply the skill               |

### Skill Name Requirements

Per the agentskills.io specification, skill names must:

* Be 1-64 characters long
* Use only lowercase letters, numbers, and hyphens
* Not start or end with a hyphen
* Not contain consecutive hyphens
* Match the directory name containing the SKILL.md file

**Valid names**: `python-testing`, `api-design`, `database-migrations`\
**Invalid names**: `Python-Testing`, `api_design`, `-database`, `my--skill`

## Skill Locations

Skills are discovered from multiple locations, similar to rules:

| Location                       | Source    | Description                                                |
| :----------------------------- | :-------- | :--------------------------------------------------------- |
| `~/.augment/skills/`           | User      | Available in all workspaces, stored in your home directory |
| `<workspace>/.augment/skills/` | Workspace | Project-specific skills, can be version controlled         |
| `~/.claude/skills/`            | User      | Compatible with Claude Code, stored in home directory      |
| `<workspace>/.claude/skills/`  | Workspace | Compatible with Claude Code, in workspace                  |

Skills from all locations are loaded and made available to the agent. The **Source** column in the `/skills` popover shows whether each skill came from your home directory (User) or the current workspace (Workspace).

## Viewing Skills

Use the `/skills` slash command to view all loaded skills and their details:

```
/skills
```

This opens a popover showing:

* **Name**: The skill identifier
* **Source**: Where the skill was loaded from (Workspace or User)
* **Description**: What the skill does
* **Tokens**: Estimated token count based on the SKILL.md file size

### Skills Popover Navigation

| Key                    | Action                                 |
| :--------------------- | :------------------------------------- |
| `↑` / `↓` or `j` / `k` | Navigate between skills                |
| `Enter`                | Open the selected skill in your editor |
| `Esc`                  | Close the popover                      |

The token count helps you understand the context window cost of each skill. Skills with larger instructions will consume more tokens when activated.

## Creating Your First Skill

<Steps>
  <Step title="Create the skills directory">
    ```bash  theme={null}
    mkdir -p .augment/skills/my-skill
    ```
  </Step>

  <Step title="Create the SKILL.md file">
    Create a file at `.augment/skills/my-skill/SKILL.md` with the following content:

    ```markdown  theme={null}
    ---
    name: my-skill
    description: Custom skill for my project's specific workflow
    ---

    # My Custom Skill

    Add your skill content here with guidance, examples, and resources.
    ```
  </Step>

  <Step title="Verify the skill is loaded">
    Start Auggie and use the `/skills` command to confirm your skill appears in the list.
  </Step>
</Steps>

## Skills vs Rules

While both skills and rules provide guidance to the agent, they serve different purposes:

| Feature       | Skills                              | Rules                              |
| :------------ | :---------------------------------- | :--------------------------------- |
| **Purpose**   | Specialized domain knowledge        | General coding guidelines          |
| **Format**    | agentskills.io specification        | Markdown with optional frontmatter |
| **Discovery** | Metadata-based (name + description) | Content-based or always-applied    |
| **Scope**     | Specific domains/workflows          | Project-wide conventions           |
| **Standard**  | Cross-platform (agentskills.io)     | Augment-specific                   |

Use **skills** for:

* Framework-specific knowledge (e.g., React patterns, Django best practices)
* Tool usage guides (e.g., Docker workflows, CI/CD procedures)
* Domain expertise (e.g., security practices, performance optimization)

Use **rules** for:

* Code style preferences
* Project architecture guidelines
* Team conventions

## Best Practices

1. **Be Specific**: Focus each skill on a single domain or workflow
2. **Include Examples**: Provide concrete code examples and commands
3. **Keep Updated**: Review and update skills as tools and practices evolve
4. **Use Clear Descriptions**: Help the agent understand when to use each skill
5. **Version Control**: Commit workspace skills to share with your team

## See Also

* [agentskills.io Specification](https://agentskills.io/specification) - Official skill format specification
* [Example Skills](https://github.com/anthropics/skills) - Collection of example skills from Anthropic
* [Rules & Guidelines](/cli/rules) - Configure general project guidelines
* [CLI Reference](/cli/reference) - Complete command-line reference
