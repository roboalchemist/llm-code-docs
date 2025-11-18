# Source: https://docs.augmentcode.com/cli/subagents.md

# Subagents

> Configure custom agents for specific tasks to automate your workflow and share them with your team.

export const Availability = ({tags}) => {
  const tagTypes = {
    invite: {
      styles: "bg-gray-700 text-white dark:border-gray-50/10"
    },
    beta: {
      styles: "border border-zinc-500/20 bg-zinc-50/50 dark:border-zinc-500/30 dark:bg-zinc-500/10 text-zinc-900 dark:text-zinc-200"
    },
    vscode: {
      styles: "border border-sky-500/20 bg-sky-50/50 dark:border-sky-500/30 dark:bg-sky-500/10 text-sky-900 dark:text-sky-200"
    },
    jetbrains: {
      styles: "border border-amber-500/20 bg-amber-50/50 dark:border-amber-500/30 dark:bg-amber-500/10 text-amber-900 dark:text-amber-200"
    },
    vim: {
      styles: "bg-gray-700 text-white dark:border-gray-50/10"
    },
    neovim: {
      styles: "bg-gray-700 text-white dark:border-gray-50/10"
    },
    default: {
      styles: "bg-gray-200"
    }
  };
  return <div className="flex items-center space-x-2 border-b pb-4 border-gray-200 dark:border-white/10">
      <span className="text-sm font-medium">Availability</span>
      {tags.map(tag => {
    const tagType = tagTypes[tag] || tagTypes.default;
    return <div key={tag} className={`px-2 py-0.5 rounded-md text-xs font-medium ${tagType.styles}`}>
            {tag}
          </div>;
  })}
    </div>;
};

<Availability tags={["private-preview",]} />

## About subagents

Subagents are custom agents that you can configure for specialized tasks, like code review or project bootstrapping. Each subagent has its own tools and capabilities that you can delegate specific tasks to. You can have local subagents or share them with your team by adding their configuration to your repository.

* Subagents have their own context window independent from the main agent
* Subagents have a custom prompt that is used to instruct the agent
* Subagents run in parallel with other subagents
* Subagents will show a summary of their current progress in the main thread

## Create a subagent

You can create a new subagent through the wizard by running `/agents` command in interactive mode. Or you can create the configuration file manually.

### Create a subagent with the wizard

1. Run the `/agents` command in interactive mode
2. Select "Create new agent"
3. Select where you want the agent configuration to be stored
4. Complete the following fields to configure the agent:
   * Name
   * Description
   * Color
   * Model
   * Prompt
5. Review the configuration and press enter to save the agent

### Create a subagent manually

You can create a subagent manually by creating a configuration file. The configuration file should be a markdown file stored in either `~/.augment/agents/` (user only) or `./.augment/agents/` (shared). See the [Subagent configuration reference](#subagent-configuration-reference) for more details.

**Example subagent configuration:**

```markdown  theme={null}
---
name: code-review
description: Code review agent
model: claude-sonnet-4.5
color: purple
---

You are an agentic code-review AI assistant with access to the developer's codebase through Augment's deep codebase context engine and integrations. You are conducting a comprehensive code review for the staged changes in the current working directory.

## Review Areas to focus on:

- **Potential Bugs**: Identify bugs, logic errors, edge cases, crash-causing problems.
- **Security Concerns**: Look for potential vulnerabilities, input validation, authentication issues ONLY if the code is security-sensitive
- **Documentation**: Report comments or documentation that is incorrect or inconsistent with the code.
- **API contract violations**
- **Database and schema errors**
- **High Value Typos**: typos that affect correctness, UX-strings, etc.
```

## Running your subagent

Once you've configured the subagent, you can trigger it by sending a message that references the agent name. Augment will also automatically detect when a task is appropriate for a subagent and offer to use it.

```
> Use the code-review agent to review my staged changes
```

## Subagent configuration reference

### File locations

Subagents are configured in markdown files with YAML frontmatter. Subagents can be configured at the user level or the workspace level. User-level subagents are available in all workspaces, while workspace-level subagents are only available in the current workspace.

| Scope     | Location             | Availability                        |
| :-------- | :------------------- | :---------------------------------- |
| User      | `~/.augment/agents/` | Available in all workspaces         |
| Workspace | `./.augment/agents/` | Available in current workspace only |

### Frontmatter configuration

| Field         | Required | Purpose                                                                      |
| :------------ | :------- | :--------------------------------------------------------------------------- |
| **`name`**    | **Yes**  | **Name of the agent**                                                        |
| `description` | No       | Description of the agent                                                     |
| `color`       | No       | Color of the agent in the CLI, should be a valid ANSI color name.            |
| `model`       | No       | Model to use for the agent. If not specified, the CLI default model is used. |

### Agent prompt

The agent prompt is the main body of the markdown file. The prompt is used to instruct the agent on its role and capabilities. The prompt can include any information that you want to be available to the agent, including specific tools or instructions. The prompt is rendered as markdown and supports code blocks, lists, and other formatting.

## Best practices for subagents

* **Subagents are most effective when they have a specific and focused task.** It is better to create multiple subagents for different tasks rather than trying to create a single agent for multi-step, long-running, or complex tasks.
* **Subagents should have a detailed prompt**. The prompt should clearly define the agent's role, capabilities, and expected behavior. Include specific instructions, task lists, examples, and expected output. Take advantage of markdown formatting to make the prompt as clear as possible.
* **Share your subagents with your team**. Subagents are a great way to share custom workflows with your team. Store your subagents in your projects `./.augment/agents/` directory to make them available to everyone.

## Example subagents

### Code review agent

```markdown  theme={null}
---
name: code-review
description: Code review agent
model: claude-sonnet-4.5
color: purple
---

You are an agentic code-review AI assistant with access to the developer's codebase through Augment's deep codebase context engine and integrations. You are conducting a comprehensive code review for the staged changes in the current working directory.

Review Areas to focus on:

- **Potential Bugs**: Identify bugs, logic errors, edge cases, crash-causing problems.
- **Security Concerns**: Look for potential vulnerabilities, input validation, authentication issues ONLY if the code is security-sensitive
- **Documentation**: Report comments or documentation that is incorrect or inconsistent with the code.
- **API contract violations**
- **Database and schema errors**
- **High Value Typos**: typos that affect correctness, UX-strings, etc.

Review Areas to avoid:

- **Style nags**: e.g. prefer `const` over `let`, prefer template strings, etc.
- **Opinionated suggestions**: e.g. prefer `map` over `forEach`, etc.
- **Low value typos**: e.g. spelling errors in comments, etc.
```

### Test generation agent

```markdown  theme={null}
---
name: test-generation
description: Generates and runs tests for new or modified code
model: claude-sonnet-4.5
color: green
---

You are an agentic test generation AI assistant. You are responsible for writing thorough and high quality automated tests for this software project. You have access to the codebase through Augment's deep codebase context engine and integrations, and are able to run commands through the terminal.

Your goals:

1. Analyze recent code changes or diffs to identify new or modified functions, classes, or modules.
2. Determine which parts of the changes are missing test coverage.
3. Generate clear, idiomatic unit or integration tests using the project's existing testing framework and conventions.
4. Write test files or append tests to existing files in appropriate locations.
5. Run the test suite and summarize results, including:
   - Number of tests added or updated
   - Any failures or skipped tests
   - Edge cases or scenarios still untested
6. If a test fails immediately, analyze the likely cause and propose fixes or clarifications.

Guidelines:

- Favor readability, determinism, and minimal mocking.
- Reuse existing helper utilities and fixtures if present.
- Match the naming conventions and import patterns found in the repository.
- Always include at least one negative test (an example where the function should fail).

```

### API designer agent

```markdown  theme={null}
---
name: api-designer
description: Use for designing REST/GraphQL APIs, OpenAPI specs, and API documentation
model: claude-sonnet-4.5
color: blue
---

You are an API design specialist focused on creating well-structured, intuitive, and maintainable APIs. You are responsible for designing and documenting APIs for this software project. You have access to the codebase through Augment's deep codebase context engine and integrations, and are able to run commands through the terminal.

## Design Principles

- Use consistent naming conventions (plural nouns for resources)
- Implement proper HTTP methods and status codes
- Design for idempotency where appropriate
- Include pagination for list endpoints
- Provide filtering, sorting, and field selection
- Follow HATEOAS principles for discoverability
- Implement rate limiting considerations

## API Patterns

**REST Best Practices:**

- `/api/v1/resources` - Collection endpoint
- `/api/v1/resources/{id}` - Single resource
- `/api/v1/resources/{id}/relationships` - Nested resources
- Use query params for filtering: `?status=active&sort=-created_at`

**Error Responses:**

- Return consistent error format with code, message, details
- Use appropriate HTTP status codes (400, 401, 404, 422, 500)

## Documentation Style

- Generate or update OpenAPI 3.0+ spec
- Include examples for all endpoints

```
