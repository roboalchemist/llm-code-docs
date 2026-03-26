# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-skills.md

# Agent Skills

## Agent Skills

Agent Skills allow you to extend Tabnine CLI with specialized expertise, procedural workflows, and task-specific resources. A "skill" is a self-contained directory that packages instructions and assets into a discoverable capability.

## Skills

#### What are skills?

A skill is a reusable capability that the Tabnine Agent or a subagent can call when solving a task.

Examples of skills include summarization, testing, validation, and prompt composition or command composition:

**Summarization:**

`Summarize this file for a code review.`

**Testing:**

`Generate unit tests for this function.`

**Validation:**

`Extract configuration values and validate them against a schema.`

**Command Composition:**

`Convert a natural language description into a CLI command.`

Skills can be combined: a subagent might chain several skills together to complete a higher-level workflow.

#### How skills are invoked

In typical usage, skills are invoked implicitly:

* You describe what you want done in natural language.
* The agent selects one or more skills that match the request.
* The skills operate on your project files, external content, or prior\
  conversation.

Extensions can register new skills, and those skills become available wherever\
the agent runs: in your terminal, inside supported IDEs, or as part of automated\
workflows.

### Overview

Unlike general context files (such as `TABNINE.md`), which provide persistent workspace-wide background, skills represent **on-demand expertise** for specific types of tasks. This lets Tabnine CLI keep a large library of specialized capabilities – like security auditing, cloud deployments, or codebase migrations – without loading all of that detail all the time.

When your request matches a skill's description, Tabnine CLI can choose to use that skill, load its instructions, and apply them to your task.

### Key Benefits

* **Shared Expertise:** Package complex workflows (like a specific team's PR review process) into a folder that anyone can use.
* **Repeatable Workflows:** Ensure complex multi-step tasks are performed consistently by providing a procedural framework.
* **Resource Bundling:** Include scripts, templates, or example data alongside instructions so Tabnine has everything it needs.
* **Progressive Disclosure:** Only skill metadata (name and description) is loaded initially. Detailed instructions and resources are only disclosed when Tabnine explicitly activates the skill, saving context tokens.

### Skill Discovery Tiers

Tabnine CLI discovers skills from three primary locations:

1. **Workspace Skills** -- Located in `.tabnine/skills`. Workspace skills are typically committed to version control and shared with the team.
2. **User Skills** -- Located in `~/.tabnine/skills`. These are personal skills available across all your workspaces.
3. **Extension Skills** -- Skills bundled within installed extensions.

**Precedence:** If multiple skills share the same name, higher-precedence locations override lower ones: **Workspace > User > Extension**.

### Managing Skills

#### In an Interactive Session

Use the `/skills` slash command to view and manage available expertise:

* `/skills list` (default): Shows all discovered skills and their status.
* `/skills link <path>`: Links agent skills from a local directory via symlink.
* `/skills disable <name>`: Prevents a specific skill from being used.
* `/skills enable <name>`: Re-enables a disabled skill.
* `/skills reload`: Refreshes the list of discovered skills from all tiers.

#### From the Terminal

The `tabnine skills` command provides management utilities:

```
# List all discovered skills
tabnine skills list

# Link agent skills from a local directory via symlink
# Discovers skills (SKILL.md or */SKILL.md) and creates symlinks in ~/.tabnine/skills
# (or ~/.agents/skills)
tabnine skills link /path/to/my-skills-repo

# Link to the workspace scope (.tabnine/skills or .agents/skills)
tabnine skills link /path/to/my-skills-repo --scope workspace

# Install a skill from a Git repository, local directory, or zipped skill file (.skill)
# Uses the user scope by default (~/.tabnine/skills or ~/.agents/skills)
tabnine skills install https://github.com/user/repo.git
tabnine skills install /path/to/local/skill
tabnine skills install /path/to/local/my-expertise.skill

# Install a specific skill from a monorepo or subdirectory using --path
tabnine skills install https://github.com/my-org/my-skills.git --path skills/frontend-design

# Install to the workspace scope (.tabnine/skills or .agents/skills)
tabnine skills install /path/to/skill --scope workspace

# Uninstall a skill by name
tabnine skills uninstall my-expertise --scope workspace

# Enable a skill (globally)
tabnine skills enable my-expertise

# Disable a skill. Can use --scope to specify workspace or user (defaults to workspace)
tabnine skills disable my-expertise --scope workspace
```

### Creating Skills

You can define skills either with Tabnine's help or manually, depending on how much control you want.

#### Option 1: Use a helper skill (recommended)

If your Tabnine CLI environment includes a helper skill such as `skill-creator`, you can ask Tabnine to scaffold a new skill for you:

1. Start an interactive Tabnine CLI session.
2. Describe the skill you want. For example:

   `Create a new skill called "code-reviewer" that reviews pull requests and local changes.`
3. Tabnine will:
   1. Create a new folder for the skill (for example, `code-reviewer/`).
   2. Add a `SKILL.md` file with the required metadata (`name`, `description`)\
      and starter instructions.
   3. Optionally add common subfolders like `scripts/`, `references/`, and\
      `assets/`.

You can then edit `SKILL.md` and add any supporting files you want Tabnine to\
use when this skill is active.

> If you don't have a helper skill available yet, you can still create skills\
> manually as described below.

#### Option 2: Create a skill manually

To define a skill by hand:

1. **Create a folder** for your skill, for example:

   `my-new-skill/`
2. **Add a** `SKILL.md` file inside that folder. At minimum it should include:

   `--- name: my-new-skill description: > Short description of what this skill does and when Tabnine should use it. --- # My New Skill Explain how Tabnine should approach this kind of task. Include any steps, checklists, or rules that matter.`
3. (Optional) Add subfolders for supporting resources:

   `my-new-skill/ ├── SKILL.md ├── scripts/ # shell scripts, helpers, etc. ├── references/ # docs, guides, specs └── assets/ # templates, sample files`
4. Place the skill folder in one of the discovery locations:
   * Workspace scope: `.tabnine/skills/` in your project.
   * User scope: `~/.tabnine/skills/` in your home directory.
5. Reload skills:
   * In an interactive session: `/skills reload`
   * Or from the terminal: `tabnine skills list` (which will trigger discovery)

Once discovered, the new skill will appear in `/skills list` and can be enabled or disabled like any other skill.

#### Example: `code-reviewer` skill

Here is a concrete example of a `SKILL.md` for a `code-reviewer` skill that\
works both with local changes and remote pull requests:

```md
---
name: code-reviewer
description: >
  Use this skill to perform a structured code review on either local changes
  or a remote pull request in this repository. Prefer it when the user asks
  for a code review, feedback on a PR, or an assessment of a set of changes.
---

# Code Reviewer Skill

This skill tells Tabnine how to review code in a way that is useful and
actionable for developers working in this repository.

When this skill is active, follow these guidelines.

## 1. Identify the review target

First, figure out what you should review:

- **Remote pull request**
  - If the user gives you a PR number, branch name, or URL, treat that as
    the primary review target.
  - Ask for clarification if the repository or provider (e.g., GitHub,
    GitLab, Bitbucket) is ambiguous.

- **Local changes**
  - If the user mentions “local changes”, “my current branch”, or similar,
    review the diff between the current branch and its main/base branch.
  - If the user specifies a subset of files or paths, limit the review to
    those.

Be explicit in your response about *what* you ended up reviewing.

## 2. What to look for

Prioritize:

1. Correctness and bugs.
2. Security and reliability.
3. Design and maintainability.
4. Readability and style.

For each significant issue, explain why it matters and suggest a concrete
improvement.

## 3. How to structure your review

Include:

1. A short summary.
2. High-level feedback.
3. File-by-file or topic-based comments.
4. An actionable checklist with must-fix vs. nice-to-have items.

## 4. Tone and communication

Be constructive, specific, and concise. Assume good intent from the author
and avoid restating the diff; focus on insight and guidance.

## 5. When information is missing

If you lack context, say what you’re missing, ask a small number of focused
questions, and avoid inventing files or changes you cannot see.
```
