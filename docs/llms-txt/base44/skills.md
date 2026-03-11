# Source: https://docs.base44.com/developers/backend/overview/skills.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Skills

> Reusable instructions that teach AI coding agents how to perform Base44-specific tasks

Base44 skills help external AI tools like Claude, Cursor, or other AI coding assistants work more effectively with Base44. They provide reusable instructions and context that these tools can use when helping you build and manage your Base44 apps.

## About skills

Base44 skills are self-contained instructions that teach AI agents how to perform specific tasks with Base44. They follow the open <a href="https://agentskills.io/specification" target="_blank">Agent Skills specification <Icon icon="arrow-up-right-from-square" /></a> and consist of a `SKILL.md` file containing metadata and instructions, along with any additional background information the agent may need.

Each skill includes:

* **Name and description**: Helps agents identify when to use the skill.
* **Instructions**: Step-by-step guidance for performing the task.
* **Optional resources**: Scripts, reference docs, and assets the agent can use.

If you want to use Base44 skills to create new projects, install them globally:

```bash  theme={null}
npx skills add base44/skills -g
```

Base44 skills are automatically included in projects created with the CLI. If you installed the skills globally, your AI agent will typically use the project-level Base44 skills.

Base44 skills are maintained in the [base44/skills](https://github.com/base44/skills) repository.

## Available skills

Base44 provides three skills that cover the full development workflow:

* [base44-cli](#base44-cli): Project setup, resource management, and deployment.
* [base44-sdk](#base44-sdk): Feature implementation with the JavaScript SDK.
* [base44-troubleshooter](#base44-troubleshooter): Production debugging and log analysis.

### base44-cli

The CLI skill teaches agents how to manage Base44 projects using the command-line interface. This is your agent's first stop when starting a new project or performing infrastructure tasks.

#### Capabilities

Capabilities of this skill include:

* Create and link Base44 projects from templates.
* Define [entity schemas](/developers/backend/data/entities) with proper field types, formats, and RLS rules.
* Configure [backend functions](/developers/backend/functions/overview) with automations.
* Set up [AI agents](/developers/backend/agents/overview) with tool permissions.
* Configure [OAuth connectors](/developers/references/sdk/integrations) for external services such as Google Calendar, Slack, and Notion.
* Generate TypeScript types from your project resources.
* Deploy resources to production, including site deployment to Base44 hosting.
* Authenticate with Base44 and manage CLI sessions.
* Configure project settings.

#### Example prompts

* "Create a new Base44 project for a todo app".
* "Add a User entity with email, name, and role fields".
* "Deploy all my changes to production".
* "Set up RLS so users can only see their own tasks".
* "Add a Google Calendar connector to my project".
* "Generate TypeScript types for my entities".

### base44-sdk

The SDK skill teaches agents how to build features using the Base44 JavaScript SDK. Once your project is initialized, this skill guides implementation work.

#### Capabilities

Capabilities of this skill include:

* Write frontend code that interacts with [entities](/developers/backend/data/entities).
* Implement [authentication](/developers/references/sdk/auth) and user management.
* Integrate [AI agents](/developers/backend/agents/overview) into your app.
* Call [backend functions](/developers/backend/functions/overview) from the frontend.
* Use [integrations](/developers/references/sdk/integrations) for AI, email, and file uploads.
* Implement [real-time features](/developers/references/sdk/subscriptions) with subscriptions.
* Build [backend functions](/developers/backend/functions/writing-functions) with service role access.
* Use [OAuth connectors](/developers/references/sdk/integrations) to get access tokens for external services in backend functions.
* [Invite users](/developers/references/sdk/auth) to your app.
* Track [analytics](/developers/references/sdk/analytics) and [log user activity](/developers/references/sdk/analytics) with the app logs module.

#### Example prompts

* "Add a login page with email and password".
* "Show a list of all pending tasks for the current user".
* "Create a chat interface for the support agent".
* "Send an email notification when a new order is created".
* "Use the Slack connector to post a message from a backend function".

### base44-troubleshooter

The troubleshooter skill teaches agents how to investigate production issues by fetching and analyzing backend function logs.

#### Capabilities

Capabilities of this skill include:

* Fetch backend function logs with filtering by function name, log level, and time range.
* Identify errors across all project functions.
* Drill into specific function logs for targeted debugging.
* Correlate log timestamps with user-reported issues.
* Analyze stack traces and error messages from function executions.

#### Example prompts

* "Show me all errors from the checkout function today".
* "Pull the last 100 log entries for my send-email function".
* "Check for any errors in the last hour across all functions".
* "Get warning and error logs from the process-payment function since yesterday".

## Keep skills in sync

Base44 skills work best when they match your Base44 CLI version. When you update the CLI, you should also update your Base44 skills:

```bash  theme={null}
# Update Base44 skills in current project
npx skills add base44/skills

# Update Base44 skills globally
npx skills add base44/skills -g
```

This updates existing Base44 skills and installs any newly added ones from the repository.

## See also

* [Base44 MCP server](/developers/backend/overview/mcp-server): Create and manage backend projects from AI assistants
* [Docs MCP server](/developers/backend/overview/base44-docs-mcp): Let AI assistants search Base44 documentation while you develop
* [Project structure](/developers/backend/overview/project-structure): Base44 project organization
* [CLI reference](/developers/references/cli/overview): Complete CLI documentation
* [SDK reference](/developers/references/sdk/overview): Complete SDK documentation


Built with [Mintlify](https://mintlify.com).