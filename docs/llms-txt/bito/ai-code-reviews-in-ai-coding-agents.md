# Source: https://docs.bito.ai/ai-code-reviews-in-cli/ai-code-reviews-in-ai-coding-agents.md

# AI code reviews in AI coding agents

[**AI Code Reviews in CLI**](https://docs.bito.ai/ai-code-reviews-in-cli/overview) integrates seamlessly with AI coding agents like Cursor, Claude Code, Windsurf, and others, enabling natural language code reviews and automated fixes.

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Before you begin, make sure you have:

* ✅ Installed the CLI ([Installation guide](https://docs.bito.ai/ai-code-reviews-in-cli/installation-guide))
* ✅ Configured your [Bito API key (aka Bito Access Key)](https://docs.bito.ai/help/account-and-settings/access-key)
* ✅ A Git repository with code changes (committed or uncommitted)

## Why use code review CLI with AI agents?

AI coding agents are great at writing code, but they need expert guidance to catch security vulnerabilities, performance issues, and best practices violations. The **AI Code Reviews in CLI** provides that expertise.

**The power combination:**

* **AI Code Reviews in CLI** provides specialized code analysis
* **Your AI agent (Cursor, Claude Code, Windsurf, etc.)** implements the fixes and iterates based on feedback
* **You** stay in natural conversation, never leaving your workflow

## How it works

{% stepper %}
{% step %}

### Configure your agent

Add `bitoreview` command to your agent's rules file so it knows when and how to run code reviews.
{% endstep %}

{% step %}

### Ask for code reviews in natural language

Simply tell your agent "review my changes" or "check for security issues"
{% endstep %}

{% step %}

### Agent runs code review CLI Automatically

Your agent executes the `bitoreview` command and reads the results
{% endstep %}

{% step %}

### Get fixes implemented instantly

Tell your agent which issues to fix, and it implements the changes automatically
{% endstep %}
{% endstepper %}

## Setup guide

Add the markdown content below to your agent's rules file. The exact file location depends on the AI coding agent you're using:

* **Cursor**: `.cursor/rules/bito-code-review.mdc`
* **Claude Code**:&#x20;

  * `~/.claude/CLAUDE.md`  in your home folder, which applies it to all your Claude sessions.

  OR

  * `CLAUDE.md` in the root of your repo
* **Windsurf**: `.windsurf/rules/bito-code-review.md`
* **Cline**: `.clinerules/bito-code-review.md`
* **Other agents**: Check your agent's documentation for custom rules/instructions location

```markdown
# AI Code Review Rules

## Automatic code reviews
When the user asks to "review my changes", "review code", "check for issues", or similar:
1. Run: `bitoreview review --prompt-only`
2. Parse and present the findings clearly to the user
3. Offer to fix issues automatically

## Review scope options
**Review uncommitted changes only:**
- Command: `bitoreview review --type uncommitted --prompt-only`

**Review committed changes only:**
- Command: `bitoreview review --type committed --prompt-only`

**Review all changes (committed + uncommitted):**
- Command: `bitoreview review --type all --prompt-only`

**Review against specific branch:**
- Command: `bitoreview review --base <branch> --prompt-only`

**Review against specific commit:**
- Command: `bitoreview review --base-commit <commit-hash> --prompt-only`

**Review specific files or patterns:**
- Command: `bitoreview review [files...] --prompt-only`

## Review modes
**Essential mode (HIGH severity only):**
- Command: `bitoreview review --mode essential --prompt-only`
- Use when: "quick review", "HIGH severity only"
- Shows only critical issues for rapid feedback

**Comprehensive mode (all severities):**
- Command: `bitoreview review --mode comprehensive --prompt-only`
- Use when: "thorough review", "full review", "detailed analysis"
- Shows HIGH, MEDIUM, and LOW severity issues

## Working directory override
**Review from different directory:**
- Command: `bitoreview review --cwd /path/to/project --prompt-only`

## Fix implementation workflow
When implementing fixes from review results:
1. Address HIGH severity issues first
2. Explain what you're changing before applying fixes
3. Show before/after code snippets for context
4. Ask for user confirmation on significant changes
```
