# Source: https://docs.tabnine.com/main/getting-started/tabnine-agent/guidelines.md

# Guidelines

## Guidelines Overview

Guidelines are a powerful feature of Tabnine Agents that allow you to define custom behaviors, workflow rules, and system prompts through simple Markdown files. Think of guidelines as custom instructions that shape how your agent behaves and operates within your specific development environment.

### What are Guidelines?

Guidelines are Markdown files stored in your project’s `/.tabnine/guidelines/` directory that act as:

* **Custom System Prompts**: Define how the agent should behave
* **Workflow Rules**: Specify procedures and processes to follow
* **Tool Instructions**: Control how and when tools should be used
* **Team Standards**: Encode your team’s coding practices and conventions

### Creating Guidelines

To add custom guidelines for use by Tabnine Agent, create a new directory called `.tabnine`.

This directory will either reside either 1) in your home directory or 2) on a per-project basis within your project directory.

After that, create a `/guidelines/` folder in the `/tabnine/` directory either in your Terminal or manually.

Once in the `.tabnine/guidelines/` directory, save a markdown file (`.md`) with written instructions in natural language. Tabnine Agent will interpret the text.

There is no *real* structural requirement, but it is still a best practice to list the various guidelines in a *hierarchical structure* for easy interpretation, both by Agents and other users.

Your location will resemble `$PROJECT_FOLDER/.tabnine/guidelines/appguidelines.md`.

As noted above, you can save multiple guideline files.

{% hint style="info" %}
Think of these in a similar fashion to the `agents.md` file that other agentic tools use.
{% endhint %}

Here is a common example of a `guidelines.md` file with hierarchical structure:

```markdown
# Team Coding Standards
## Overview
This guideline defines our team's coding standards and practices for consistent code quality.
## Instructions
### Code Style- Use meaningful variable and function names
- Follow language-specific naming conventions (camelCase for JavaScript, snake_case for Python)
- Keep functions small and focused (max 20-30 lines)
- Add comments for complex business logic
### Error Handling- Always handle errors gracefully
- Use try-catch blocks for operations that might fail
- Log errors with appropriate context
- Provide user-friendly error messages
### Testing- Write unit tests for all new functions
- Maintain minimum 80% code coverage
- Include integration tests for API endpoints
- Use descriptive test names that explain the scenario
## Examples
Good variable naming:
userAuthenticationToken = generateToken(user);
const isValidEmail = validateEmailAddress(email);
Bad variable naming:
const t = generateToken(user);  // Too generic
const flag = validateEmailAddress(email);  // Unclear purpose
```

{% hint style="info" %}
It is recommended to keep your `guidelines.md` file to 500 lines or less.
{% endhint %}

### Governance for Agentic Guidelines

(Released [5.26.0](https://docs.tabnine.com/main/administering-tabnine/release-notes#v5.26.0))

In the Admin UI, navigate over to Agent Guidelines on the left-hand side of the page.

Beneath the **General Guideline** title, you can add your natural language guideline description.  They will also be applicable to all your organization’s users and projects.

Guidelines that are input here will have the same effect as guidelines listed in your `guidelines.md` file, but they will take precedence over personal guidelines that exist in the `guidelines.md` file.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2F63yT6enSDFZNhb1gftq6%2Funknown.png?alt=media&#x26;token=6b18232a-e717-452a-b761-4c30fdb762c5" alt=""><figcaption></figcaption></figure>

<br>
