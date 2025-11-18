# Augment Code Documentation

Source: https://docs.augmentcode.com/llms-full.txt

---

# ACP Mode
Source: https://docs.augmentcode.com/cli/acp/agent

Auggie is a fully compatible Agent Client Protocol (ACP) agent enabling you to bring the power of Augment to any compatible client.

## About ACP Mode

[Agent Client Protocol](https://agentclientprotocol.com/overview/introduction) (ACP) is an open protocol that provides a standardized way to connect AI agents to different text editors, IDEs, and other tools. ACP mode uses JSON-RPC over standard input and output to communicate between the agent and the client. You can see a [overview of the protocol](https://agentclientprotocol.com/protocol/overview) to learn more.

## Using ACP Mode

To use Auggie in ACP mode, you need to pass the `--acp` flag when starting Auggie. You can pass additional [command-line arguments](/cli/reference) to set the model, authentication, and other options.

```sh  theme={null}
auggie --acp
```

To use Auggie in a ACP-compatible client, you need to configure the client to launch Auggie with the `--acp` flag and follow the client-specific instructions. See the [ACP Clients](/cli/acp/clients) page for more details.

## Compatibility

ACP is an emerging protocol and is in active development. Not all features available in interactive mode are supported in ACP mode. We are looking forward to working with the community to add support for more features in the future.


# ACP Clients
Source: https://docs.augmentcode.com/cli/acp/clients

Configure Auggie to run in any Agent Client Protocol (ACP) compatible client like Zed, Neovim, or Emacs.

## About ACP Clients

[Agent Client Protocol](https://agentclientprotocol.com/overview/introduction) (ACP) is an open protocol that provides a standardized way to connect AI agents to different text editors, IDEs, and other tools. Auggie is a fully ACP compatible agent enabling you to bring the power of Augment to editors like Zed, Neovim, or Emacs. See a [full list of supported clients](https://agentclientprotocol.com/overview/clients) in the ACP docs.

## Prerequisites

* Auggie CLI [installed and configured](/cli/setup-auggie/install-auggie-cli)
* Login to Augment with `auggie login`
* A compatible ACP client

## Client configuration

If you have an ACP client that you would like to have listed here, please [open an issue](https://github.com/augmentcode/auggie/issues/new) and we'll be happy to add it.

### Zed

<Note>
  We recommend installing and configuring Auggie in [Zed](https://zed.dev/) using the [Auggie extension](https://zed.dev/extensions/auggie).
</Note>

If you want to configure Auggie manually through Zed's settings, you can use the following configuration. You can pass additional [command-line arguments](/cli/reference) to Auggie by adding them to the `args` array or use alternative [authentication methods](/cli/setup-auggie/authentication) by passing environment variables in the `env` object.

```
{
  "agent_servers": {
    "Auggie CLI": {
      "command": "auggie",
      "args": ["--acp"],
      "env": {}
    }
  }
}
```

### Neovim

To use Auggie with neovim, you can use one of the following plugins:

* [CodeCompanion](https://github.com/olimorris/codecompanion.nvim)
* [Avante](https://github.com/yetone/avante.nvim?tab=readme-ov-file#enabling-acp)

### Emacs

To use Auggie with emacs, you can use one of the following plugins:

* [agent-shell.el](https://github.com/xenodium/agent-shell)


# Using Auggie with Automation
Source: https://docs.augmentcode.com/cli/automation/overview

Auggie was designed to not just be a powerful agent to write code, but to automate all the tasks that are needed to build software at scale.

## About automation

Auggie was purpose built to integrate into your software development stack. From using Auggie in your local development workflows to automatically running Auggie in your CI/CD pipelines, Auggie can help you build better software faster.

### Example use cases

* **Code reviews**: Review code changes and provide feedback.
* **Issue triage**: Triage incoming issues and route them to the appropriate team or individual.
* **Automate on-call**: Respond to incoming alerts and create an assessment plan.
* **Exception management**: Analyze incoming exceptions and create tickets.

## Integrating with your workflows

In order to use Auggie in your systems, like a CI/CD pipeline, you'll need to install Auggie CLI, provide a session token, and write an instruction that will be used alongside any data from your system you want to include.

### Installation

Auggie can be [installed](/cli/setup-auggie/install-auggie-cli) directly from npm anywhere you can run Node 22 or later including VMs, serverless functions, and containers. You will also need to install any dependencies for defined MCP servers in those environments.

```sh  theme={null}
npm install -g @augmentcode/auggie
```

### Authentication

Session tokens are associated with the user that created it, and Auggie will run with integration configurations from that user. See [Authentication](/cli/setup-auggie/authentication) for full details. You can override the user's GitHub configuration by passing `--github-api-token <token>`.

```sh  theme={null}
# First, login to Augment with the CLI
auggie login

# Next, output your token
auggie tokens print

# Then, pass your token to auggie
AUGMENT_SESSION_AUTH='<token>' auggie --print "Summarize the build failure"
```

### Scripts and pipes

Auggie runs as a subprocess, so it can be used in any shell script. It can be used just like any command-line tool that follows the Unix philosophy. You can pipe data into Auggie and then pipe the response to another command. Data passed into Auggie through stdin will be used as context in addition to the instruction.

```sh  theme={null}
# Pipe data through stdin
cat build.log | auggie --print "Summarize the failure and open a Linear ticket"

# Provide input from a file
auggie --compact --instruction /path/to/instruction.md < build.log
```

## GitHub Actions

GitHub Actions makes it easy to connect Auggie to other parts of your software development pipeline, from linting, testing, build, and deploy. We've built a [simple wrapper for Auggie](https://github.com/augmentcode/augment-agent) that enables you to  integrate with GitHub Action workflows and build custom tooling around Auggie.

Follow the instructions to [configure Augment Agent](https://github.com/augmentcode/augment-agent/blob/main/README.md) in GitHub Actions and explore the [example-workflows](https://github.com/augmentcode/augment-agent/tree/main/example-workflows) directory to get started.

### Ready to use workflows

Get started using Auggie in GitHub Actions immediately by following the instructions for setup and deploy in one of the following workflows, or use the `/github-workflow` wizard in Auggie to have the workflows generated for you.

* [PR Description](https://github.com/augmentcode/describe-pr): This action automatically analyzes your PR changes and generates comprehensive, informative descriptions.
* [PR Review](https://github.com/augmentcode/review-pr): This action automatically analyzes your PR changes and generates comprehensive, informative reviews

Need even more help building GitHub Actions? May we suggest asking Auggie.

```sh  theme={null}
auggie "Help me build a GitHub Action to..."
```


# Service Accounts
Source: https://docs.augmentcode.com/cli/automation/service-accounts



## About

Service Accounts provide non-human identities for automation use cases to make API requests to the Augment backend through Auggie CLI. They decouple automation tasks from using individual user accounts and enable per-automation task token lifecycle management.

## Managing Service Accounts

Service Accounts can be managed by navigating to [app.augmentcode.com/settings/service-accounts](https://app.augmentcode.com/settings/service-accounts) and logging in. Service accounts are only available to [Enterprise plan](https://augmentcode.com/pricing) customers. Service accounts can only be managed by the Administrator of the Enterprise Plan.

### Creating a Service Account

To create a new service account, click the "New Service Account" button. You will be prompted to enter a name and an optional description for the service account. The account name must be unique within your organization.

### Creating API tokens

Once you've created a service account, you can create API tokens for it by clicking the "Add API token" button next to the service account name in the list of service accounts. You will be prompted to enter a name for the API token which must be unique amongst the tokens for this service account. Once you've created a token, you will be given a one time opportunity to retrieve the token value by either:

* Copying the token value directly or using the "Copy token" button **OR**
* Downloading a `session.json` file that is ready to use with Auggie CLI.

API tokens for service accounts don't have an expiration date and need to be manually revoked if they are no longer needed.

### Deleting Service Accounts and API tokens

API tokens can be revoked by selecting "Revoke" from the triple dot menu next to the token name in the service account list. Note that revoking a token is a permanent action and cannot be undone. Any existing Auggie CLI automation sessions using the token will be disrupted.

Service accounts can be deleted by clicking "Manage" next to the service account name in the service account list, and then clicking "Delete Account" from the dialog that appears. Note that deleting a service account will also delete all the associated API tokens.

## Using API tokens with Auggie CLI

In order to use a service account API token with Auggie CLI, you need to edit the `session.json` file stored under `~/.augment`. If you've downloaded a `session.json` file after creating the API token, you can simply replace the existing `session.json` file with the new one. If you've only copied the token value, you need to edit the `session.json` file with the following content and replace the `accessToken` value with the new token value.

```
{
  "accessToken": "<TOKEN VALUE>",
  "tenantURL": "<TENANT URL>",
  "scopes": [
    "read",
    "write"
  ]
}
```

The correct `tenantURL` value for your organization is displayed on top of the service account list in the management UI.

## Best Practices

* Use a separate service account per automation task. This will allow you to manage token lifecycle and monitor credit usage per automation task.
* Use the ability to create multiple tokens under a service account to rotate tokens when needed. Create a new API token, update the automation tasks to use the new token, and revoke the old token once all automation tasks have been updated.


# Automatic Updates
Source: https://docs.augmentcode.com/cli/autoupgrade

Learn how to manage and troubleshoot Auggie CLI's automatic update feature.

## How Automatic Updates Work

Auggie CLI automatically updates itself when running in interactive mode to ensure you always have the latest features and bug fixes.

### Interactive Mode (TUI)

* Automatically checks npm for newer versions when you start Auggie
* Performs upgrades without prompting to minimize interruption
* Shows a brief notification when an update is applied
* Best-effort approach - continues running even if update fails

### Non-interactive Mode (Print/Text Mode)

* Auto-update is completely disabled
* Respects version pinning in automation scripts

## Disabling Automatic Updates

Set the `AUGMENT_DISABLE_AUTO_UPDATE` environment variable to `1` to disable automatic updates.

### Environment Variable (Recommended for Scripts)

```bash  theme={null}
# Disable for current session
export AUGMENT_DISABLE_AUTO_UPDATE=1

# Disable for single command
AUGMENT_DISABLE_AUTO_UPDATE=1 auggie --print "Your instruction here"
```

## Manual Updates

You can manually update Auggie CLI by running the following command.

```bash  theme={null}
auggie upgrade
```


# Custom Slash Commands
Source: https://docs.augmentcode.com/cli/custom-commands

Create and manage custom slash commands for frequently-used prompts and workflows.

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


# Custom Slash Commands Examples
Source: https://docs.augmentcode.com/cli/custom-commands-examples

Ready-to-use examples of custom slash commands for common development workflows.

## Example Commands

Here are some practical examples of custom slash commands you can use in your projects:

<AccordionGroup>
  <Accordion title="Code Review Command">
    ```markdown  theme={null}
    ---
    description: Perform a comprehensive code review
    argument-hint: [file-path]
    ---

    Please perform a comprehensive code review of the specified file or current changes, focusing on:

    1. **Code Quality**: Check for readability, maintainability, and adherence to best practices
    2. **Security**: Look for potential security vulnerabilities
    3. **Performance**: Identify potential performance issues
    4. **Testing**: Suggest areas that need test coverage
    5. **Documentation**: Check if code is properly documented

    $ARGUMENTS
    ```
  </Accordion>

  <Accordion title="Bug Fix Template">
    ```markdown  theme={null}
    ---
    description: Generate a structured bug fix approach
    argument-hint: [bug-description]
    ---

    Help me fix this bug: $ARGUMENTS

    Please provide:
    1. Root cause analysis
    2. Step-by-step fix approach
    3. Testing strategy
    4. Prevention measures for similar issues
    ```
  </Accordion>

  <Accordion title="Feature Implementation Guide">
    ```markdown  theme={null}
    ---
    description: Create implementation plan for new features
    argument-hint: [feature-description]
    ---

    Create a detailed implementation plan for: $ARGUMENTS

    Include:
    - Technical requirements
    - Architecture considerations
    - Implementation steps
    - Testing approach
    - Documentation needs
    ```
  </Accordion>

  <Accordion title="Security Review Command">
    ```markdown  theme={null}
    ---
    description: Perform security analysis on code
    argument-hint: [file-path]
    ---

    Perform a security review of: $ARGUMENTS

    Focus on:
    1. **Input validation** and sanitization
    2. **Authentication** and authorization checks
    3. **Data exposure** and privacy concerns
    4. **Injection vulnerabilities** (SQL, XSS, etc.)
    5. **Cryptographic** implementations
    6. **Dependencies** with known vulnerabilities

    Provide specific recommendations for any issues found.
    ```
  </Accordion>

  <Accordion title="Performance Optimization">
    ```markdown  theme={null}
    ---
    description: Analyze and optimize code performance
    argument-hint: [file-path]
    ---

    Analyze the performance of: $ARGUMENTS

    Please examine:
    1. **Algorithm complexity** and efficiency
    2. **Memory usage** patterns
    3. **Database queries** and optimization opportunities
    4. **Caching** strategies
    5. **Network requests** and bundling
    6. **Rendering performance** (for frontend code)

    Suggest specific optimizations with expected impact.
    ```
  </Accordion>

  <Accordion title="Documentation Generator">
    ```markdown  theme={null}
    ---
    description: Generate comprehensive documentation
    argument-hint: [file-path]
    ---

    Generate documentation for: $ARGUMENTS

    Include:
    1. **Overview** and purpose
    2. **API reference** with parameters and return values
    3. **Usage examples** with code snippets
    4. **Configuration options** if applicable
    5. **Error handling** and troubleshooting
    6. **Dependencies** and requirements

    Format as clear, structured markdown.
    ```
  </Accordion>

  <Accordion title="Test Generation Command">
    ```markdown  theme={null}
    ---
    description: Generate comprehensive test cases
    argument-hint: [file-path]
    ---

    Generate test cases for: $ARGUMENTS

    Create tests covering:
    1. **Happy path** scenarios
    2. **Edge cases** and boundary conditions
    3. **Error handling** and exceptions
    4. **Integration points** with other components
    5. **Performance** considerations
    6. **Security** edge cases

    Use appropriate testing framework conventions and include setup/teardown as needed.
    ```
  </Accordion>
</AccordionGroup>

## How to Add Commands to Your Project

To use these custom slash commands in your project, you need to save them in the `.augment/commands/` directory:

### Step 1: Create the Commands Directory

First, create the `.augment/commands/` directory in your project root if it doesn't exist:

```bash  theme={null}
mkdir -p .augment/commands
```

### Step 2: Save Command Files

Save each command as a separate `.md` file in the `.augment/commands/` directory. For example:

```bash  theme={null}
# Save the code review command
cat > .augment/commands/code-review.md << 'EOF'
---
description: Perform a comprehensive code review
argument-hint: [file-path]
---

Please perform a comprehensive code review of the specified file or current changes, focusing on:

1. **Code Quality**: Check for readability, maintainability, and adherence to best practices
2. **Security**: Look for potential security vulnerabilities
3. **Performance**: Identify potential performance issues
4. **Testing**: Suggest areas that need test coverage
5. **Documentation**: Check if code is properly documented

$ARGUMENTS
EOF
```

### Step 3: Use Your Commands

Once saved, your custom commands become available as slash commands in Augment:

```
/code-review src/components/Button.tsx
/bug-fix "Login form validation not working"
/security-review auth/middleware.js
```

### Directory Structure

Your project structure should look like this:

```
your-project/
├── .augment/
│   └── commands/
│       ├── code-review.md
│       ├── bug-fix.md
│       ├── security-review.md
│       └── performance-optimization.md
├── src/
└── package.json
```

## Usage Tips

* **Save these templates** in your `.augment/commands/` directory
* **Customize the prompts** to match your team's coding standards and practices
* **Add project-specific context** to make the commands more effective
* **Combine commands** by referencing outputs from one command in another
* **Use meaningful filenames** like `code-review.md`, `bug-fix.md`, etc.
* **Version control your commands** by committing the `.augment/commands/` directory to your repository

## Creating Your Own Examples

When creating custom commands, consider these patterns:

1. **Start with a clear description** in the frontmatter
2. **Use argument hints** to guide users on expected inputs
3. **Structure your prompts** with numbered lists or bullet points
4. **Include specific instructions** for the type of analysis or output you want
5. **Reference the `$ARGUMENTS` variable** where user input should be inserted

## See Also

* [Custom Slash Commands](/cli/custom-commands) - Learn how to create and manage custom commands
* [CLI Reference for Custom Commands](/cli/reference#custom-commands) - Complete command-line reference for custom commands


# Integrations and MCP
Source: https://docs.augmentcode.com/cli/integrations

Expand Augment's capabilities with external tools and data sources through native integrations and Model Context Protocol (MCP) servers.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

<Note>Auggie runs commands and tools automatically. Only use integrations and MCP servers from trusted sources, and be aware of the risks of combining multiple tools with external data sources or production systems.</Note>

## About Integrations and MCP

Auggie can utilize external integrations through native integrations like GitHub, Linear, and Notion and Model Context Protocol (MCP) to access external systems for information and integrate tools to take actions. MCP is an open protocol that provides a standardized way to connect AI models to different data sources and tools.

## Native Integrations

You'll need to configure the integration in Augment for VS Code or JetBrains IDEs. Once configured, the integration will be available for use with Auggie automatically. See a full list and examples for [native agent integrations](/setup-augment/agent-integrations).

### 1. Setup in Augment extension

* **Visual Studio Code**: Click the settings icon in the top right of Augment's chat window or press <Keyboard shortcut="Cmd/Ctrl Shift P" /> and select <Command text="Show Settings Panel" />
* **JetBrains IDEs**: Click the Augment icon in the bottom right of your JetBrains IDE and select <Command text="Tool Settings" />

### 2. Connect the integration

Click "Connect" for the integration you want to set up

<img className="block rounded-xl" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=8e1cb7e476ff72baf79853e1a396061a" alt="Set up integrations in the settings page" data-og-width="1096" width="1096" data-og-height="598" height="598" data-path="images/integration-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6b58b42005ec712d925971f18e71f0df 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b0347aaa6924edd4a61a6ed59e70f84c 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=50b67616fb88ab7b1620628cf09c5c40 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=66664659b4ca1d32c356fbf0e72b2778 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ccfd90b3fe548564b1c3482f5d4d0e95 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f78ecdd094cea06ca826da1580683efc 2500w" />

You'll be redirected to authorize the integration with the appropriate service. After authorization, the integration will be available for use with Augment Agent.

## MCP Integrations

In addition to native integrations, Auggie can also access external systems through Model Context Protocol (MCP) servers. MCP servers enable Auggie to interact with external tools and services through a standardized protocol, such as accessing databases, running browser automation, sending messages to Slack, or integrating with APIs.

### Configure MCP via settings.json

You can persist MCP servers in the Augment settings file `~/.augment/settings.json`, which will initialize on startup and can be checked with `/mcp-status`.

```json  theme={null}
{
  "mcpServers": {
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY"
      }
    },
    "weather": {
      "type": "sse",
      "url": "https://weather-mcp.example.com/v1",
      "headers": {
        "X-API-Key": "your_weather_api_key",
        "Content-Type": "application/json"
      }
    },
    "renderMCP": {
      "type": "http",
      "url": "https://mcp.render.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_API_KEY>"
      }
    },
    "local-tool": {
      "command": "/usr/local/bin/custom-mcp",
      "args": ["--serve", "--port", "3000"],
      "env": { "DEBUG": "true" }
    }
  }
}
```

#### HTTP Transport with Headers

MCP servers using HTTP transport can include a `headers` object for authentication or custom headers:

```json  theme={null}
{
  "mcpServers": {
    "renderMCP": {
      "type": "http",
      "url": "https://mcp.render.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_API_KEY>",
        "X-Custom-Header": "custom-value"
      }
    }
  }
}
```

The `headers` field accepts any valid HTTP headers as key-value pairs.

**Common uses**

* **Authentication** - `Authorization` headers with bearer tokens or API keys
* **Custom parameters** - Server-specific information that doesn't fit into standard request parameters
* **Session management** - `Mcp-Session-Id` header for managing sessions in Streamable HTTP transport

**Considerations**

* **Transport type** - Headers are relevant for HTTP and SSE transports only. Stdio transport uses standard input/output and does not use HTTP headers
* **Server requirements** - Required headers depend on the MCP server implementation
* **Security** - Avoid including sensitive information like API keys directly in configuration files. Consider secure credential management methods

### Manage MCP servers with the Auggie CLI

You can add and inspect MCP servers is via Auggie subcommands, which will persist the configuration to your `~/.augment/settings.json` file:

#### Usage

**Add MCP server:**

```bash  theme={null}
auggie mcp add <name> [options]
```

Writes the server entry to your settings.json with interactive prompts for overwriting existing configurations.

Options:

* `--command <path>` - Executable path (for stdio transport)
* `--args <args>` - Arguments string for command
* `-e, --env <KEY=VAL>` - Environment variable (repeatable)
* `-t, --transport <transport>` - stdio|sse|http (default: "stdio")
* `-u, --url <url>` - URL (required for --transport sse or http)
* `-h, --header <KEY:VAL>` - HTTP header (repeatable, for http transport)
* `-r, --replace` - Overwrite existing entry without prompt
* `--json` - Output JSON

**Add MCP server from JSON:**

```bash  theme={null}
auggie mcp add-json <name> <json>
```

Import an MCP server configuration directly from a JSON string. This is useful when you have a complete server configuration in JSON format and want to add it quickly without specifying individual options.

The JSON string should match the structure used in `settings.json` for MCP server configurations. This command uses the same mechanism as `--mcp-config` but provides a convenient way to add servers directly from the command line.

**List MCP servers:**

```bash  theme={null}
auggie mcp list [options]
```

Lists configured MCP servers (from settings and any active overrides).

Options:

* `--json` - Output JSON format

**Remove MCP server:**

```bash  theme={null}
auggie mcp remove <name> [options]
```

Cleanly removes the named server configuration from settings.json.

Examples:

```bash  theme={null}
# Add a stdio-based MCP server (executable with args and environment)
auggie mcp add context7 \
  --command npx \
  --args "-y @upstash/context7-mcp@latest" \
  --env CONTEXT7_API_KEY=your_key

# Compressed syntax 
auggie mcp add context7 -- npx -y @upstash/context7-mcp

# Add an SSE-based MCP server (Server-Sent Events with URL)
auggie mcp add weather-api \
  --transport sse \
  --url https://weather-mcp.example.com/sse

# Compressed syntax
auggie mcp add weather-api --transport sse https://weather-mcp.example.com/sse

# Add an HTTP-based MCP server with authentication headers
auggie mcp add renderMCP \
  --transport http \
  --url https://mcp.render.com/mcp \
  --header "Authorization:Bearer YOUR_API_TOKEN"

# Add HTTP server with multiple headers
auggie mcp add api-service \
  --transport http \
  --url https://api.example.com/mcp \
  --header "Authorization:Bearer YOUR_TOKEN" \
  --header "X-Custom-Header:custom-value"

# List all configured servers (tabular display with status)
auggie mcp list

# List servers in JSON format for programmatic access
auggie mcp list --json

# Remove a server configuration
auggie mcp remove context7

# Replace existing server without interactive prompt
auggie mcp add context7 --command npx --args "..." --replace

# Add MCP server from JSON configuration (stdio transport)
auggie mcp add-json weather-api '{"type":"stdio","command":"/path/to/weather-cli","args":["--api-key","abc123"],"env":{"CACHE_DIR":"/tmp"}}'

# Add MCP server from JSON configuration (SSE transport)
auggie mcp add-json remote-api '{"type":"sse","url":"https://api.example.com/sse"}'

# Add MCP server from JSON configuration (HTTP transport with headers)
auggie mcp add-json renderMCP '{"type":"http","url":"https://mcp.render.com/mcp","headers":{"Authorization":"Bearer ABC_XYZ_123"}}'
```

### MCP overrides

You can define servers by passing ad‑hoc overrides with `--mcp-config`. The structure is the same as `settings.json`:

```json  theme={null}
// After npm install gitlab-mr-mcp
{
  "mcpServers": {
    "gitlab-mr-mcp": {
      "command": "node",
      "args": ["/path/to/gitlab-mr-mcp/index.js"],
      "env": {
        "MR_MCP_GITLAB_TOKEN": "your_gitlab_token",
        "MR_MCP_GITLAB_HOST": "your_gitlab_host"
      }
    }
  }
}
```


# Interactive mode
Source: https://docs.augmentcode.com/cli/interactive

Use a rich interactive terminal experience to explore your codebase, build new features, debug issues, and integrate your tools.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

<Note>Auggie is currently in beta and does not support all features available in the Augment plugins for Visual Studio Code or JetBrains IDEs.</Note>

## About interactive mode

Auggie is an agentic terminal-based code assistant that has deep codebase knowledge powered by Augment's context engine. Auggie can help you understand a new codebase, fix bugs quickly, and build new features faster. Auggie has access to your connected integrations and MCP servers and can pull in additional context or run tools to get your tasks done.

## Using interactive mode

Run `auggie` without any mode flags to get the full-screen terminal user interface with rich interactive features, real-time streaming of responses, and visual progress indicators. This mode shows all tool calls, results, and allows ongoing conversation through an intuitive interface.

```sh  theme={null}
# Start Auggie in interactive mode
auggie

# Provide an initial instruction
auggie "Look at my open issues and prioritize the highest impact ones for me"
```

### Multi-line input

Entering a new line in the input box depends on your terminal configuration and platform. You can use `Ctrl + J` to enter a new line in any terminal. See below for instructions to configure your terminal to use `Option + Enter` to enter a new line.

| Terminal application       | New line shortcut |
| :------------------------- | :---------------- |
| All terminals              | `Ctrl + J`        |
| MacOS Terminal (see below) | `Option + Enter`  |
| iTerm2 (see below)         | `Option + Enter`  |
| VS Code Terminal           | `Option + Enter`  |
| Ghostty                    | `Shift + Enter`   |

**MacOS Terminal**

1. Go to <Command text="Terminal > Settings... > Profiles > Keyboard" />
2. Check <Command text="Use option key as meta key" />

**iTerm2**

1. Go to <Command text="iTerm2 > Settings... > Profiles > Keys" />
2. Check <Command text="Left or Right option key acts as Esc+" />

## Reference

### Shortcuts

| Command             | Description                                                 |
| :------------------ | :---------------------------------------------------------- |
| `Ctrl + P`          | Enhance your prompt with codebase context                   |
| `Escape`            | Interrupt the active agent                                  |
| `Ctrl + C`          | Interrupt the active agent                                  |
| `Escape` + `Escape` | Clear the input box                                         |
| `Ctrl + C`          | Press twice to exit                                         |
| `Ctrl + D`          | Press twice to exit                                         |
| `Up Arrow`          | Cycle through previous messages                             |
| `Down Arrow`        | Cycle through previous messages                             |
| `Ctrl + O`          | Open current input in external editor, inserts text on exit |

### Slash Commands

| Command            | Description                                                 |
| :----------------- | :---------------------------------------------------------- |
| `/account`         | Show account information                                    |
| `/clear`           | Clear the input box                                         |
| `/editor`          | Open current input in external editor, inserts text on exit |
| `/exit`            | Exit Auggie                                                 |
| `/feedback`        | Provide feedback to the Augment team                        |
| `/github-workflow` | Generate a GitHub Action workflow                           |
| `/help`            | Show help                                                   |
| `/logout`          | Logout of Augment                                           |
| `/mcp-status`      | View the status of all configured MCP servers               |
| `/model`           | Select the model for this session                           |
| `/new`             | Start a new conversation with no message history            |
| `/permissions`     | View and manage tool permissions                            |
| `/request-id`      | Show the request ID for the current conversation            |
| `/task`            | Open task manager to add, edit, and manage tasks            |
| `/verbose`         | Toggle verbose output for tools                             |
| `/vim`             | Toggle Vim mode for advanced text editing                   |

For more information about slash commands, including how to create custom commands, see [Custom Slash Commands](/cli/custom-commands).


# Prompt Enhancer
Source: https://docs.augmentcode.com/cli/interactive/prompt-enhancer

Use Ctrl+P to enhance your prompts with relevant context, structure, and conventions from your codebase.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## About the Prompt Enhancer

The Auggie CLI prompt enhancer is a powerful feature that helps you craft better prompts by automatically adding relevant context, structure, and conventions from your codebase. Instead of writing detailed prompts from scratch, you can start with a simple idea and let the prompt enhancer transform it into a comprehensive, well-structured prompt.

## Activating the Prompt Enhancer

To use the prompt enhancer in Auggie's interactive mode:

1. **Start typing your prompt** in the input box
2. **Press <Keyboard shortcut="Ctrl + P" />** to activate the prompt enhancer
3. **Wait for enhancement** - Auggie will process your prompt and replace it with an enhanced version
4. **Review and edit** the enhanced prompt if needed
5. **Submit your enhanced prompt** by pressing Enter

<Note>The prompt enhancer is only available when you have text entered at the command prompt. The <Keyboard shortcut="Ctrl + P" /> shortcut will only work in interactive mode.</Note>

## How It Works

When you press <Keyboard shortcut="Ctrl + P" />, the prompt enhancer:

1. **Captures your current input** and saves it to history
2. **Switches to Enhancement mode** - you'll see the mode indicator change and input will be temporarily disabled
3. **Sends your prompt** to the enhancement service using your current workspace context
4. **Processes the response** and extracts the enhanced prompt
5. **Replaces your input** with the enhanced version and returns to Normal mode

During enhancement, you'll see:

* The mode indicator shows "Enhancing your prompt, press Esc to cancel"
* Input is disabled to prevent conflicts
* A visual indication that processing is in progress

## Enhancement Process

The prompt enhancer uses your workspace context to improve your prompts by:

* **Adding relevant file references** from your current project
* **Including coding conventions** and patterns from your codebase
* **Structuring the prompt** for better clarity and specificity
* **Adding context** about your project's architecture and dependencies
* **Suggesting specific examples** based on existing code patterns

## Canceling Enhancement

You can cancel the prompt enhancement process at any time:

* **Press <Keyboard shortcut="Esc" />** to cancel enhancement and restore your original input
* **Press <Keyboard shortcut="Ctrl + C" />** to cancel enhancement and restore your original input

When canceled, you'll see a brief notification and your original prompt will be restored.

## Error Handling

If the prompt enhancement fails:

* Your original input will be restored
* An error notification will appear briefly (\~3 seconds)
* You can try enhancing again or proceed with your original prompt

Common reasons for enhancement failure:

* Network connectivity issues
* Service temporarily unavailable
* Input too short or unclear for enhancement

## Examples

### Before Enhancement

```
fix the login bug
```

### After Enhancement (Example)

```
Fix the authentication bug in the login flow. Please:

1. Review the current login implementation in `src/auth/login.ts`
2. Check for issues with token validation and session management
3. Examine error handling in the authentication middleware
4. Look at recent changes to the user authentication flow
5. Test the fix with both valid and invalid credentials
6. Ensure the fix follows our existing error handling patterns

Context: This appears to be related to the recent changes in the authentication system. Please maintain consistency with our existing auth patterns and ensure proper error messages are returned to the user.
```

## Integration with Other Features

The prompt enhancer works seamlessly with other Auggie CLI features:

* **History Navigation**: Enhanced prompts are added to your command history
* **Multi-line Input**: Works with both single-line and multi-line prompts
* **Conversation Context**: Uses your current conversation history for better enhancement
* **Workspace Awareness**: Leverages your current workspace and file context

## Tips for Best Results

1. **Start with clear intent** - Even simple prompts like "add tests" or "refactor this" work well
2. **Be specific about scope** - Mention specific files or components when relevant
3. **Use domain language** - Technical terms related to your project help the enhancer understand context
4. **Review enhanced prompts** - The enhancer provides a starting point; feel free to edit further
5. **Iterate if needed** - You can enhance the same prompt multiple times for different approaches

## Troubleshooting

**Ctrl+P doesn't work:**

* Ensure you have text in the input box
* Make sure you're in Normal mode (not in a menu or other mode)
* Check that you're using the correct key combination for your terminal

**Enhancement takes too long:**

* Press Esc to cancel and try again
* Check your network connection
* Try with a shorter or simpler prompt

**Enhanced prompt isn't helpful:**

* Edit the enhanced prompt manually
* Try starting with a more specific initial prompt
* Consider the context - the enhancer works best with workspace-relevant requests

## Related Features

* [Task Management](/cli/interactive/task-management) - Break down enhanced prompts into manageable tasks
* [Keyboard Shortcuts](/cli/interactive#shortcuts) - Learn other useful CLI shortcuts
* [Slash Commands](/cli/interactive#slash-commands) - Discover other interactive commands


# Using Task Manager
Source: https://docs.augmentcode.com/cli/interactive/task-management

Use /task to break down complex problems into manageable steps.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## About the Task Manager

The Auggie CLI task manager allows you to break down complex problems into discrete, manageable actions and track your progress through each step. It's particularly useful for automation workflows and keeping the agent focused on multi-step tasks.

The task manager maintains state per session and stores tasks under `~/.augment` for persistence across CLI sessions.

## Activating the Task Manager

Start Auggie in interactive mode and use the `/task` slash command:

```bash  theme={null}
# Start Auggie in interactive mode
auggie

# Then type the slash command
/task
```

This opens the task manager interface, which takes over the main panel and provides a focused environment for task management.

### Alternative Access

You can also ask the agent to create a task list for you:

```bash  theme={null}
auggie "Start a task list to implement user authentication"
```

The agent will automatically create and populate a task list when it encounters complex, multi-step problems.

## Task Manager Interface

The task manager provides a scrollable interface with comprehensive theming and visual feedback. When active, it replaces the main chat interface to provide a focused task management experience.

### Navigation and Interaction

Use your keyboard to interact with the Task Manager:

| Key        | Action                                                                                     |
| :--------- | :----------------------------------------------------------------------------------------- |
| `↑` / `↓`  | Navigate between tasks. The active task is highlighted with • next to the \[ ] Task Title. |
| `J` / `K`  | Alternative vim-style navigation (up/down)                                                 |
| `A`        | Add a new task                                                                             |
| `E`        | Edit the active task's title and description                                               |
| `D`        | Delete the active task                                                                     |
| `Spacebar` | Toggle task status                                                                         |
| `Esc`      | Dismiss the Task Manager                                                                   |

## Task Status Indicators

Tasks have three distinct states with corresponding visual status indicators:

* **\[ ] Not Started** - Empty checkbox, task has not been started
* **\[✓] Done** - Checkmark, task has been completed
* **\[-] Cancelled** - Dash, task has been cancelled or is no longer needed

## Working with Tasks

### Creating Tasks

**Manual Creation:**

1. Press `A` to add a new task
2. Enter the task title when prompted
3. Optionally add a description for more detailed context

**Agent-Generated Tasks:**
The agent automatically creates tasks inside the Task Manager when it encounters complex problems. You can also explicitly request task creation:

```bash  theme={null}
"Create a task list to refactor the authentication system"
```

### Editing Tasks

1. Navigate to the desired task using arrow keys or J/K
2. Press `E` to edit
3. Modify the title first, then the description
4. The task manager provides inline editing with clear visual feedback

### Task Execution

**Manual Execution:**

* Use the task list as a checklist, manually updating status as you complete work
* Toggle status with `Spacebar` to track progress

**Agent Execution:**
You can ask the agent to work on specific tasks from the task manager:

```bash  theme={null}
"Work on the first incomplete task in my task list"
"Complete the database migration task"
```

The agent will access your task list and update task status as it works.

## Advanced Features

### Task Hierarchy and Subtasks

The task manager supports nested task structures:

* Main tasks can have subtasks for complex workflows
* Subtasks are automatically indented and organized hierarchically
* Navigate through nested structures using standard navigation keys

### Persistence and Sessions

* Tasks are automatically saved per session under `~/.augment`
* Task lists persist across CLI restarts within the same session
* Each conversation session maintains its own task list

### Integration with Agent Workflow

The task manager is designed to work seamlessly with agent automation:

* **Keeps agents focused**: Provides clear structure for multi-step workflows
* **Progress tracking**: Agent can update task status as it completes work
* **Context preservation**: Tasks maintain context across long conversations
* **Automation-friendly**: Particularly useful for non-interactive automation workflows

## Use Cases and Examples

### Development Workflow

```bash  theme={null}
auggie "Create a task list to implement user registration feature"
# Agent creates tasks like:
# [ ] Design user registration API endpoints
# [ ] Create user model and database schema
# [ ] Implement registration validation
# [ ] Add password hashing and security
# [ ] Write unit tests for registration
# [ ] Update API documentation
```

### Code Refactoring

```bash  theme={null}
auggie "Break down refactoring the payment system into tasks"
# Agent creates structured tasks for complex refactoring
```

### Bug Investigation

```bash  theme={null}
auggie "Create tasks to investigate and fix the login timeout issue"
# Agent creates systematic debugging tasks
```

## Tips for Effective Task Management

1. **Be Specific**: Create clear, actionable task descriptions
2. **Break Down Complex Work**: Use subtasks for multi-step processes
3. **Regular Updates**: Keep task status current for accurate progress tracking
4. **Agent Collaboration**: Let the agent help create and organize task structures
5. **Session Organization**: Use task lists to maintain focus across long sessions

## Troubleshooting

**Task Manager Won't Open:**

* Ensure you're in interactive mode (`auggie` without `-p` flag)
* Try typing `/task` exactly as shown
* Check that you're not in the middle of another operation

**Tasks Not Persisting:**

* Tasks are saved per session - starting a new session creates a new task list
* Check that `~/.augment` directory has proper write permissions

**Navigation Issues:**

* Use either arrow keys (↑/↓) or vim keys (J/K) for navigation
* Ensure the task manager has focus (not in edit mode)

## Related Features

* [Prompt Enhancer](/cli/interactive/prompt-enhancer) - Enhance task descriptions with context
* [Keyboard Shortcuts](/cli/interactive#shortcuts) - Learn other useful CLI shortcuts
* [Slash Commands](/cli/interactive#slash-commands) - Discover other interactive commands


# Introducing Auggie CLI
Source: https://docs.augmentcode.com/cli/overview

Auggie in the terminal gives you powerful agentic capabilities to analyze code, make changes, and execute tools in an interactive terminal and in your automated workflows.

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

<Availability tags={["beta"]} />

## Introduction

<CardGroup cols={2}>
  <Card title="GitHub Repository" icon="github" href="https://github.com/augmentcode/auggie">
    Report issues, leave feature requests and view custom workflows for Auggie CLI
  </Card>

  <Card title="NPM Package" icon="npm" href="https://www.npmjs.com/package/@augmentcode/auggie">
    Install Auggie CLI from npm
  </Card>
</CardGroup>

Auggie CLI takes the power of Augment's agent and context engine and puts it in your terminal, allowing you to use Augment anywhere your code goes. You can use Auggie in a standalone interactive terminal session alongside your favorite editor or in any part of your software development stack.

* Build features and debug issues with a standalone interactive agent.
* Get instant feedback, insight, and suggestions for your PRs and builds.
* Triage customer issues and alerts from your observability stack.

## Getting started

To use Auggie CLI in interactive mode or in your automations, you'll need:

* Node 22 or later installed
* A compatible shell like zsh, bash, fish

<Steps>
  <Step title="Install Auggie with npm">
    ```sh  theme={null}
    npm install -g @augmentcode/auggie
    ```

    You can install Auggie CLI directly from npm anywhere you can run Node 22 or later. Auggie is currently in beta and may not run on all environments and terminal configurations.
  </Step>

  <Step title="Go to your project directory">
    ```sh  theme={null}
    cd /path/to/your/project
    ```

    Your project will be indexed automatically when you run Auggie in your project directory. Augment's powerful context engine provides the best results when it has access to your project's codebase and any related repositories.
  </Step>

  <Step title="Login or sign up to Augment">
    ```sh  theme={null}
    auggie login
    ```

    After installing, you'll have to log in to your Augment account. Run auggie login and follow the prompts.
  </Step>

  <Step title="Start using Auggie">
    ```sh  theme={null}
    auggie "optional initial prompt"
    ```

    Just run `auggie` to start the interactive terminal. You can also pass a prompt as an argument and use `--print` to print the response to stdout instead of the interactive terminal–perfect for automation workflows.
  </Step>
</Steps>

## Using Auggie in interactive mode

Run `auggie` without any mode flags to get the full-screen terminal user interface with rich interactive features, real-time streaming of responses, and visual progress indicators. This mode shows all tool calls, results, and allows ongoing conversation through an intuitive interface.

Best for manual development work, exploration, and interactive problem-solving sessions where you want the full visual experience and plan to have back-and-forth conversations with the agent.

## Using Auggie in your automations

**Print Mode**: Add the `--print` flag (e.g., `auggie --print "your instruction"`) to execute the instruction once without the UI. This mode exits immediately without prompting for additional input. Perfect for automation, CI/CD pipelines, and background tasks where you want the agent to act without follow-up from a person.

**Quiet Mode**: `--quiet` flag (e.g., `auggie --print --quiet "your instruction"`) to tell the agent to only reply back with a final output. Ideal when you need to use the agent to provide structured data back without all the steps it took to get there. Provides a simple, clean response.


# Tool Permissions
Source: https://docs.augmentcode.com/cli/permissions

Control what tools Auggie CLI can execute with granular permission settings for security and compliance. Tool permissions configured will only work inside the CLI and not in the Augment code extension.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## About Tool Permissions

Auggie CLIs tool permission system provides fine-grained control over what actions the agent can perform in your environment. This security layer ensures that Auggie only executes approved operations, protecting your codebase and system from unintended changes.

Tool permissions are especially important when:

* Running Auggie in production environments
* Working with sensitive codebases
* Enforcing organizational security policies
* Using Auggie in automated workflows

## How Permissions Work

When Auggie attempts to use a tool, the permission system:

1. **Checks for matching rules** in your configuration
2. **Applies the first matching rule** based on tool name and optional patterns
3. **Rules are evaluated top-down** - first match wins
4. **Prompts for approval** when set to ask-user mode (interactive only)

### Permission Flow

```
Tool Request → Check Rules → Apply Permission → Execute/Deny → Log Decision
```

### Notes on Unmatched Tools

* Rules are evaluated in order from top to bottom
* The first matching rule determines the permission
* If no rules match, the CLI follows its implicit runtime behavior
* Configure explicit rules for all tools you want to control

## Configuration Files

Tool permissions are configured through `settings.json` files with clear precedence:

### File Locations

1. **User settings**: `~/.augment/settings.json`
   * Personal preferences that apply to all your projects
   * Ideal for your default security stance

2. **Project settings**: `<workspace>/.augment/settings.json`
   * Repository-specific rules shared with your team
   * Perfect for project-specific security requirements

<Note>Settings are merged with later files taking precedence. Project settings override user settings.</Note>

## Basic Configuration

### Creating Rules

Rules define permissions for specific tools. Each rule can specify:

* **Tool name** - The specific tool to control
* **Permission type** - `allow`, `deny`, or `ask-user`
* **Optional patterns** - For shell commands, use regex matching

### Basic Rule Structure

```json  theme={null}
{
  "tool-permissions": [
    { "toolName": "launch-process", "permission": { "type": "deny" } },
    { "toolName": "view", "permission": { "type": "allow" } }
  ]
}
```

### Allow List Configuration

Create an explicit allow list by only allowing specific tools:

```json  theme={null}
{
  "tool-permissions": [
    { "toolName": "view", "permission": { "type": "allow" } },
    { "toolName": "codebase-retrieval", "permission": { "type": "allow" } },
    { "toolName": "grep-search", "permission": { "type": "allow" } },
    { "toolName": "github-api", "permission": { "type": "allow" } }
  ]
}
```

<Note>This configuration explicitly allows only the listed tools. Tools not in this list will follow the CLI's implicit behavior.</Note>

### Block List Configuration

Create a block list by explicitly denying specific dangerous tools:

```json  theme={null}
{
  "tool-permissions": [
    { "toolName": "remove-files", "permission": { "type": "deny" } },
    { "toolName": "kill-process", "permission": { "type": "deny" } },
    { "toolName": "launch-process", "shellInputRegex": "^(rm|sudo|shutdown|reboot)", "permission": { "type": "deny" } }
  ]
}
```

<Note>This configuration blocks specific dangerous operations. Tools not explicitly denied will follow the CLI's implicit behavior.</Note>

### Mix and Match Configuration

Combine allow, deny, and ask-user rules for fine-grained control:

```json  theme={null}
{
  "tool-permissions": [
    { "toolName": "view", "permission": { "type": "allow" } },
    { "toolName": "codebase-retrieval", "permission": { "type": "allow" } },
    { "toolName": "grep-search", "permission": { "type": "allow" } },

    { "toolName": "str-replace-editor", "permission": { "type": "ask-user" } },
    { "toolName": "save-file", "permission": { "type": "ask-user" } },

    { "toolName": "launch-process", "shellInputRegex": "^(npm test|npm run lint|git status|git diff)", "permission": { "type": "allow" } },
    { "toolName": "launch-process", "shellInputRegex": "^(rm -rf|sudo|chmod 777)", "permission": { "type": "deny" } },
    { "toolName": "launch-process", "permission": { "type": "ask-user" } },

    { "toolName": "remove-files", "permission": { "type": "deny" } }
  ]
}
```

This configuration provides fine-grained control with different permission levels based on tool risk and usage patterns.

## Available Tools

### Process Management

| Tool             | Description                        |
| :--------------- | :--------------------------------- |
| `launch-process` | Execute shell commands and scripts |
| `read-process`   | Read output from running processes |
| `write-process`  | Send input to running processes    |
| `list-processes` | List all active processes          |
| `kill-process`   | Terminate running processes        |

### File Operations

| Tool                 | Description                         |
| :------------------- | :---------------------------------- |
| `view`               | Read file contents                  |
| `str-replace-editor` | Edit files with find/replace        |
| `save-file`          | Create or overwrite files           |
| `remove-files`       | Delete files from the filesystem    |
| `codebase-retrieval` | Search codebase with context engine |
| `grep-search`        | Search files with regex patterns    |

### External Services

| Tool         | Description                  |
| :----------- | :--------------------------- |
| `github-api` | GitHub API operations        |
| `linear`     | Linear issue tracking        |
| `notion`     | Notion workspace access      |
| `supabase`   | Supabase database operations |
| `web-search` | Web search queries           |
| `web-fetch`  | Fetch web page content       |

### MCP Server Tools

MCP tools follow the pattern `{tool-name}_{server-name}`:

* Example: `query_database-mcp`
* Truncated to 64 characters if longer
* Treated like any other tool for permissions

## Advanced Rules

### Shell Command Filtering

Control which shell commands can be executed using regex patterns:

```json  theme={null}
{
  "tool-permissions": [
    { "toolName": "launch-process", "shellInputRegex": "^(ls|pwd|echo|cat|grep)\\s", "permission": { "type": "allow" } },
    { "toolName": "launch-process", "permission": { "type": "deny" } }
  ]
}
```

This configuration:

1. Allows only safe commands (ls, pwd, echo, cat, grep)
2. Denies all other shell commands
3. Rules are evaluated in order - first match wins

### Event-Based Permissions

Control when permission checks occur:

```json  theme={null}
{
  "tool-permissions": [
    { "toolName": "github-api", "eventType": "tool-response", "permission": { "type": "allow" } }
  ]
}
```

**Event types:**

* **`tool-call`** (default) - Check before tool execution
* **`tool-response`** - Check after execution but before returning results to agent

## Interactive Approval

When using `ask-user` mode in interactive sessions, Auggie displays approval prompts:

```
🔒 Tool Approval Required
─────────────────────────
Tool: launch-process
Command: npm install express

[A]llow once  [D]eny  [Always allow]  [Never allow]
```

### Keyboard Shortcuts

| Key   | Action                      |
| :---- | :-------------------------- |
| `A`   | Allow this specific request |
| `D`   | Deny this specific request  |
| `Y`   | Always allow this tool      |
| `N`   | Never allow this tool       |
| `Esc` | Cancel and deny request     |

<Note>In non-interactive mode (--print), ask-user permissions default to deny for security.</Note>

## Common Configurations

### Read-Only Mode

Allow only read operations, perfect for code review and analysis:

```json  theme={null}
{
  "tool-permissions": [
    { "toolName": "view", "permission": { "type": "allow" } },
    { "toolName": "codebase-retrieval", "permission": { "type": "allow" } },
    { "toolName": "grep-search", "permission": { "type": "allow" } },
    { "toolName": "web-search", "permission": { "type": "allow" } },
    { "toolName": "web-fetch", "permission": { "type": "allow" } },
    { "toolName": "str-replace-editor", "permission": { "type": "deny" } },
    { "toolName": "save-file", "permission": { "type": "deny" } },
    { "toolName": "remove-files", "permission": { "type": "deny" } },
    { "toolName": "launch-process", "permission": { "type": "deny" } }
  ]
}
```

### Development Mode

Add safety guards for potentially dangerous operations:

```json  theme={null}
{
  "tool-permissions": [
    { "toolName": "remove-files", "permission": { "type": "ask-user" } },
    {
      "toolName": "launch-process",
      "shellInputRegex": "^(rm|sudo|chmod)\\s",
      "permission": { "type": "ask-user" }
    }
  ]
}
```

### CI/CD Pipeline

Restrictive settings for automated workflows:

```json  theme={null}
{
  "tool-permissions": [
    { "toolName": "view", "permission": { "type": "allow" } },
    { "toolName": "str-replace-editor", "permission": { "type": "allow" } },
    { "toolName": "save-file", "permission": { "type": "allow" } },
    {
      "toolName": "launch-process",
      "shellInputRegex": "^(npm test|npm run lint|jest)\\s",
      "permission": { "type": "allow" }
    },
    { "toolName": "remove-files", "permission": { "type": "deny" } },
    { "toolName": "launch-process", "permission": { "type": "deny" } }
  ]
}
```

## Custom Policies

### Webhook Validation

Use external services to validate tool requests:

```json  theme={null}
{
  "tool-permissions": [
    { "toolName": "github-api", "permission": { "type": "webhook-policy", "webhookUrl": "https://api.company.com/validate-tool" } }
  ]
}
```

The webhook receives:

```json  theme={null}
{
  "toolName": "github-api",
  "eventType": "tool-call",
  "details": { /* tool-specific data */ },
  "timestamp": "2025-01-01T02:41:40.580Z"
}
```

Expected response:

```json  theme={null}
{
  "allow": true,
  "output": "Optional message to include in agent response"
}
```

### Script Validation

Use local scripts for complex validation logic:

```json  theme={null}
{
  "tool-permissions": [
    { "toolName": "launch-process", "permission": { "type": "script-policy", "script": "/path/to/validate-command.sh" } }
  ]
}
```

## Best Practices

1. **Be Explicit**: Define clear rules for all tools you want to control
2. **Layer Settings**: Use user settings for defaults, project settings for team rules
3. **Test Configurations**: Verify permissions work as expected before automation
4. **Log Decisions**: Monitor which tools are being allowed/denied for audit trails
5. **Regular Reviews**: Periodically review and update permission rules
6. **Order Matters**: Remember that rules are evaluated top-down, first match wins

## Troubleshooting

**Ask-User Mode in Automation:**

* Ask-user permissions automatically deny in non-interactive mode
* Use explicit allow/deny rules for automation scenarios
* Consider webhook or script policies for dynamic decisions

**MCP Tools Not Recognized:**

* Ensure MCP server name follows `{tool}_{server}` pattern
* Check for 64-character truncation on long names
* Verify MCP server is properly configured and running

## Security Considerations

* **Never commit sensitive webhook URLs** to version control
* **Use `.augment/settings.local.json`** for personal security overrides
* **Regularly audit** tool usage in production environments
* **Implement defense in depth** with multiple permission layers
* **Test permission changes** in isolated environments first

## Related Features

* [Authentication](/cli/setup-auggie/authentication) - Secure access to Auggie
* [Custom Rules](/cli/rules) - Project-specific guidelines
* [MCP Integrations](/cli/integrations) - External tool configuration
* [Automation](/cli/automation) - Using permissions in CI/CD


# CLI Flags and Options
Source: https://docs.augmentcode.com/cli/reference

A comprehensive reference for all command-line flags available in the Auggie CLI.

## CLI flags

| Command                          | Description                                                                                                                                                          |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auggie`                         | Start Auggie in interactive mode                                                                                                                                     |
| `auggie --print` (`-p`)          | Output simple text for one instruction and exit                                                                                                                      |
| `auggie --quiet`                 | Output only the final response for one instruction and exit                                                                                                          |
| `auggie --compact`               | Output tool calls, results, and final response as one line each and exit                                                                                             |
| `auggie -p --output-format json` | Output the response in structured JSON format. Must be used with `--print` (`-p`) mode. Useful for parsing Auggie's output programmatically in automation workflows. |

### Input

| Command                                            | Description                                        |
| :------------------------------------------------- | :------------------------------------------------- |
| `auggie "Fix the typescript errors"`               | Provide an initial instruction in interactive mode |
| `auggie --print "Summarize the staged changes"`    | Provide an instruction and exit                    |
| `cat file \| auggie --print "Summarize this data"` | Pipe content through stdin                         |
| `auggie --print "Summarize this data" < file.txt`  | Provide input from a file                          |
| `auggie --instruction "Fix the errors"`            | Provide an initial instruction in interactive mode |
| `auggie --instruction-file /path/to/file.txt`      | Provide an instruction by file in interactive mode |

### Custom Commands

| Command                         | Description                                                                  |
| :------------------------------ | :--------------------------------------------------------------------------- |
| `auggie command <command-name>` | Execute a custom command from `.augment/commands/` or `~/.augment/commands/` |

Custom commands are reusable instructions stored as markdown files. They can be placed in:

* `~/.augment/commands/<name>.md` - Global commands (user-wide)
* `./.augment/commands/<name>.md` - Project commands (workspace-specific)
* `~/.claude/commands/<name>.md` - Claude Code user commands
* `./.claude/commands/<name>.md` - Claude Code workspace commands

Commands are resolved in order of precedence, with Auggie-specific locations taking priority over Claude Code locations.

**Examples:**

```sh  theme={null}
# Execute a custom deployment command
auggie command deploy-staging

# Execute a code review command
auggie command security-review

# List available commands (shown in help output)
auggie command help
```

See [Custom Commands](/cli/custom-commands) for detailed information on creating and managing custom commands.

### Sessions

| Command                          | Description                                       |
| :------------------------------- | :------------------------------------------------ |
| `auggie --continue` `(-c)`       | Resumes the previous conversation                 |
| `auggie --dont-save-session`     | Do not save the conversation to the local history |
| `auggie --delete-saved-sessions` | Delete all saved sessions from disk               |

### Configuration

| Command                                    | Description                                                               |
| :----------------------------------------- | :------------------------------------------------------------------------ |
| `auggie --workspace-root /path/to/project` | Specify the root of the workspace                                         |
| `auggie --rules /path/to/rules.md`         | Additional rules to append to workspace guidelines                        |
| `auggie --model "name"`                    | Select the model to use (accepts long or short names from the model list) |

### Models

List out available models and their short names to be passed into the `--model` flag

| Command                | Description                   |
| :--------------------- | :---------------------------- |
| `auggie --list-models` | List available models         |
| `auggie -lm`           | Shorthand for `--list-models` |

<Note>Tool permissions can be configured in settings.json files. See [Permissions](/cli/permissions) for detailed configuration.</Note>

### MCP and integrations

| Command                             | Description                                       |
| :---------------------------------- | :------------------------------------------------ |
| `auggie mcp add [options] <name>`   | Create or update a named MCP server configuration |
| `auggie mcp add-json <name> <json>` | Add an MCP server from JSON configuration         |
| `auggie mcp list`                   | Display all configured MCP servers                |
| `auggie mcp remove <name>`          | Remove a named MCP server configuration           |

| Command                                 | Description                        |
| :-------------------------------------- | :--------------------------------- |
| `auggie --mcp-config {key: value}`      | MCP configuration as a JSON string |
| `auggie --mcp-config /path/to/mcp.json` | MCP configuration from a JSON file |

<Note>You can define MCP servers persistently in the settings files: `~/.augment/settings.json`. Any `--mcp-config` flags are applied last and override settings.</Note>

For detailed usage examples, options, settings.json format, and precedence rules, see [Integrations and MCP](/cli/integrations#manage-mcp-servers-with-the-auggie-cli).

### Authentication

| Command               | Description                                  |
| :-------------------- | :------------------------------------------- |
| `auggie login`        | Login to Augment and store the token locally |
| `auggie logout`       | Remove the locally stored token              |
| `auggie tokens print` | Print the locally stored token               |

### Additional commands

| Command            | Description  |
| :----------------- | :----------- |
| `auggie --help`    | Show help    |
| `auggie --version` | Show version |

## Environment Variables

| Variable                      | Description                   |
| ----------------------------- | ----------------------------- |
| `AUGMENT_SESSION_AUTH`        | Authentication JSON.          |
| `AUGMENT_API_URL`             | Backend API endpoint          |
| `AUGMENT_API_TOKEN`           | Authentication token          |
| `GITHUB_API_TOKEN`            | GitHub API token              |
| `AUGMENT_DISABLE_AUTO_UPDATE` | Disable automatic CLI updates |

## See Also

* [Custom Rules and Guidelines](/cli/rules) - Configure custom rules for project-specific guidance
* [Custom Commands](/cli/custom-commands) - Create reusable command templates
* [Permissions](/cli/permissions) - Configure tool permissions and security
* [Integrations](/cli/integrations) - Connect external tools and services


# Rules & Guidelines
Source: https://docs.augmentcode.com/cli/rules

Configure custom rules and guidelines to provide context-aware assistance in Auggie CLI.

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


# Login and authentication
Source: https://docs.augmentcode.com/cli/setup-auggie/authentication

You will need an active account and valid session token to use Auggie CLI which you can get by following the instructions below.

## About authentication

Before you can use Auggie, you will need to login to create a session token that can be used by Auggie in both interactive and automation modes.

<Note>Augment authentication tokens are secrets and should be protected with the same level of security you'd use for any sensitive credential. Tokens are tied to the user who logged in, not to your team or enterprise account, so each user has a unique augment token.</Note>

## Logging in

You can login by running the following command and following the prompts.

```sh  theme={null}
auggie login
```

## Logging out

You can logout by running the following command. This will remove the local token from your machine and you will need to login again to use Auggie.

```sh  theme={null}
auggie logout
```

## Getting your token

For automation, you will need to provide your token each time you run Auggie. After you have logged in above, you can get your token by running the following command.

```sh  theme={null}
auggie tokens print
```

## Using your token

After you have your token, you can pass it to Auggie through a number of methods depending on your use case and environment.

### Environment variables

You can set the `AUGMENT_SESSION_AUTH` environment variable to your token before running Auggie. Pass it before you run the command, add it to your environment, or add it to your shell's rc file to persist it.

```sh  theme={null}
AUGMENT_SESSION_AUTH='<token>'
```

### Token file

You can store the token as plaintext in a file and then use the `--augment-token-file` flag to pass it to Auggie. We do not recommend checking your token into version control.

```sh  theme={null}
auggie --augment-token-file /path/to/token
```

## Revoking your tokens

You can expire all the tokens for the current logged in user by running the following command. Using `--logout` will only remove the local token from your machine.

```sh  theme={null}
auggie tokens revoke 
```


# Install Auggie CLI
Source: https://docs.augmentcode.com/cli/setup-auggie/install-auggie-cli

Install Auggie to get agentic coding capabilities in your terminal, on your server, or anywhere your code runs.

```sh  theme={null}
npm install -g @augmentcode/auggie
```

# About installing Auggie

Installing Auggie CLI is easy and will take you less than a minute. You can install Auggie CLI directly from npm anywhere you can run Node 22 or later. Many systems do not ship with the latest version of Node.js, so you may need to upgrade Node to use Auggie.

Auggie is currently in beta and may not run on all environments and terminal configurations.

## Automatic Updates

Auggie CLI automatically updates itself when running in interactive mode to ensure you always have the latest features and bug fixes. This feature is enabled by default and works seamlessly in the background. You can [disable automatic updates](/cli/reference#environment-variables).

## System requirements

* [**Node.js 22+**](https://nodejs.org/en/download/)
* **Platforms**: MacOS, Windows WSL, Linux
* **Shells**: zsh, bash, fish

### Interactive mode

Using Auggie in interactive mode requires a terminal that supports ANSI escape codes. We recommend using Ghostty, iTerm2, MacOS Terminal, Windows Terminal, Alacritty, Kitty, and other modern terminals.

If you are connecting to your shell over SSH or through tmux you may need to adjust your terminal settings or configuration to enable proper color support, font rendering, and interactivity.


# Workspace context
Source: https://docs.augmentcode.com/cli/setup-auggie/workspace-context

Auggie will automatically index the current working directory or directory you specify to give Augment a full view of your system.

## About Workspace Context

Augment is powered by its deep understanding of your code. Your codebase will be automatically indexed when you run `auggie` from a git directory or you can specify a directory to index. If you run Auggie from a non-git directory, a temporary workspace will be created for you.

## Specifying a directory to index

To specify a directory other than the current working directory pass the target directory to the `--workspace-root` flag.

```sh  theme={null}
auggie --workspace-root /path/to/your/project
```

To learn more about what files are indexed and how to ignore files, see [Workspace indexing](/cli/setup-auggie/workspace-indexing).


# Index your workspace
Source: https://docs.augmentcode.com/cli/setup-auggie/workspace-indexing

When your workspace is indexed, Augment can provide tailored code suggestions and answers based on your unique codebase, best practices, coding patterns, and preferences. You can always control what files are indexed.

## Security and privacy

Augment stores your code securely and privately to enable our powerful context engine. We ensure code privacy through a proof-of-possession API and maintain strict internal data minimization principles. [Read more about our security](https://www.augmentcode.com/security).

## What gets indexed

Augment will index all the files in your workspace, except for the files that match patterns in your `.gitignore` file and the `.augmentignore` file. [Read more about Workspace Context](/cli/setup-auggie/workspace-context).

## Ignoring files with .augmentignore

The `.augmentignore` file is a list of file patterns that Augment will ignore when indexing your workspace. Create an `.augmentignore` file in the root of your workspace. You can use any glob pattern that is supported by the [gitignore](https://git-scm.com/docs/gitignore) file.

## Including files that are .gitignored

If you have a file or directory in your `.gitignore` that you want to be indexed, you can add it to your `.augmentignore` file using the `!` prefix.

For example, you may want your `node_modules` indexed to provide Augment with context about the dependencies in their project, but it is typically included in their `.gitignore`. Add `!node_modules` to your `.augmentignore` file.

<CodeGroup>
  ```bash .augmentignore theme={null}
  # Include .gitignore excluded files with ! prefix
  !node_modules

  # Exclude other files with .gitignore syntax
  data/test.json
  ```

  ```bash .gitignore theme={null}
  # Exclude dependencies
  node_modules

  # Exclude secrets
  .env

  # Exclude build artifacts
  out
  build
  ```
</CodeGroup>


# Subagents
Source: https://docs.augmentcode.com/cli/subagents

Configure custom agents for specific tasks to automate your workflow and share them with your team.

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


# Augment Code Review
Source: https://docs.augmentcode.com/codereview/admin-guide

Use Augment Code Review to automatically review PRs faster while catching more critical bugs.

export const GitHubLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M7.49933 0.25C3.49635 0.25 0.25 3.49593 0.25 7.50024C0.25 10.703 2.32715 13.4206 5.2081 14.3797C5.57084 14.446 5.70302 14.2222 5.70302 14.0299C5.70302 13.8576 5.69679 13.4019 5.69323 12.797C3.67661 13.235 3.25112 11.825 3.25112 11.825C2.92132 10.9874 2.44599 10.7644 2.44599 10.7644C1.78773 10.3149 2.49584 10.3238 2.49584 10.3238C3.22353 10.375 3.60629 11.0711 3.60629 11.0711C4.25298 12.1788 5.30335 11.8588 5.71638 11.6732C5.78225 11.205 5.96962 10.8854 6.17658 10.7043C4.56675 10.5209 2.87415 9.89918 2.87415 7.12104C2.87415 6.32925 3.15677 5.68257 3.62053 5.17563C3.54576 4.99226 3.29697 4.25521 3.69174 3.25691C3.69174 3.25691 4.30015 3.06196 5.68522 3.99973C6.26337 3.83906 6.8838 3.75895 7.50022 3.75583C8.1162 3.75895 8.73619 3.83906 9.31523 3.99973C10.6994 3.06196 11.3069 3.25691 11.3069 3.25691C11.7026 4.25521 11.4538 4.99226 11.3795 5.17563C11.8441 5.68257 12.1245 6.32925 12.1245 7.12104C12.1245 9.9063 10.4292 10.5192 8.81452 10.6985C9.07444 10.9224 9.30633 11.3648 9.30633 12.0413C9.30633 13.0102 9.29742 13.7922 9.29742 14.0299C9.29742 14.2239 9.42828 14.4496 9.79591 14.3788C12.6746 13.4179 14.75 10.7025 14.75 7.50024C14.75 3.49593 11.5036 0.25 7.49933 0.25Z" fill="currentColor" />
  </svg>;

## About Augment Code Review

Augment Code Review helps professional software teams complete code-reviews faster inside GitHub while also catching more critical bugs before they hit production. Backed by Augment's industry-leading Context Engine, the agent understands your codebase at a deep level, providing reviews that are more meaningful and account for codebase-wide effects. Augment prioritizes high signal-to-noise ratio by focusing on high-impact issues like bugs, security concerns, correctness, and cross-system problems while avoiding low-value style nags.

<Note>
  Augment Code Review relies on the Augment GitHub App which is only compatible with GitHub Enterprise Cloud and github.com. GitHub Enterprise Server is not currently supported.
</Note>

## Getting Started

Visit [app.augmentcode.com/settings/code-review](https://app.augmentcode.com/settings/code-review) and log in. Augment Code Review is only available as an add-on to [Enterprise plan](https://augmentcode.com/pricing) customers. Settings are accessible to all members of the Enterprise plan, but only configurable for Administrators of the Enterprise plan. If you aren't sure if you are an Administrator, please contact your solutions team.

### Configure Repo Access inside of the Augment GitHub App

Before you can configure repositories, click on "Install" to install the Augment GitHub App. This will redirect you to GitHub to provide permissions for all the repos you grant Augment Code Review to engage.

<img src="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=fc3c7ac1bde5635d1cfef9cd96a88529" alt="Code Review Settings install button" className="rounded-xl" data-og-width="1307" width="1307" data-og-height="672" height="672" data-path="images/code-review-settings-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?w=280&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=31d46773f0cb7183c9ce124d29f560a7 280w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?w=560&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=bc0122ce8f4db9239dd4b3852a9c24e7 560w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?w=840&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=402c05c90721f936a6eb7799a09dc0f5 840w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?w=1100&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=cb2b4114383e36a3857effe12f8eec58 1100w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?w=1650&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=1e8419133d036a6b6a05fb41d1a141da 1650w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?w=2500&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=d8af4c4cb27c4d36a0b437f62f345e2c 2500w" />

If your firewall configuration, allowlist or network policy requires a static IP for this integration, please refer to our [static IP address](https://docs.augmentcode.com/setup-augment/static-ip-support#allow-augment-traffic-from-static-ips) documentation.

<AccordionGroup>
  <Accordion title="Who can install the Augment GitHub App?">
    To install the Augment GitHub App, you will need to be an Administrator of your GitHub organization. To find who the Administrators are, visit your GitHub organization settings page and click on "People." Administrators are listed under "Owners."

    <img src="https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=0f6779df0d8a446bacbb4df0575c7cd0" alt="GitHub Admins" className="rounded-xl" data-og-width="2010" width="2010" data-og-height="1284" height="1284" data-path="images/code-review-owners.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=280&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=2654775b944c43922376d86b98e22175 280w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=560&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=63d0c59812fb1d4f0e747d67e65efa46 560w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=840&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=ae3ce426fada48f9464c54981e1a93e7 840w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=1100&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=cc6ca0802f7d540c107b4e414b8f96a3 1100w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=1650&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=96124ffa1c0c7689a4b2b485189ac871 1650w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=2500&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=1f74e1e9fb88262a6a1399af1db2e06c 2500w" />
  </Accordion>
</AccordionGroup>

Once you finish installing the GitHub app, you should see a green checkmark with the text "All set!". Then, back in the Augment Code Review Settings, the "Install" button should now show a green "Installed" badge. If you do not see either of these, you may need to uninstall the app through GitHub and reinstall it. See [Troubleshooting](/codereview/admin-guide#stuck-on-install-button) for more help.

<img src="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=f4a0990fb97f3348aa6479f7227ea882" alt="GitHub App Installed" className="rounded-xl" data-og-width="813" width="813" data-og-height="627" height="627" data-path="images/code-review-github-integration-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=280&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=099cafaf756d8b53438815d57695a266 280w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=560&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=67f73fe4016247bb8f4c331cf77a1b81 560w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=840&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=83b3050a8120ec5ed27f63bc48dd311f 840w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=1100&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=873defdc8762e23920704f7c618ee1e6 1100w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=1650&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=c296b2b5bbfae6af4caf0e8f6c71323b 1650w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=2500&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=7cccceea467427c5b923c4730f406b4e 2500w" />

### Permissions requested by the Augment GitHub App:

* Contents, read-only: Clone repositories

* Pull Requests, read and write: Read pull requests and post comments to pull requests

* Issues, read-only: Read top-level PRs / Issues

* Organization Members, read-only: Read members of an organization, to distinguish internal and external users and their access levels to Augment features

Organization owners and repository admins can install the app directly; others will need owner approval. See [GitHub documentation](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party) for details. If your organization uses [Augment for Slack,](https://docs.augmentcode.com/setup-augment/install-slack-app) the same selections will apply to both Augment for Slack and Augment Code Review.

<img className="block rounded-xl" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5e4084c99c0295b0f64244970b63b7c1" alt="Installing the GitHub app on a single repository" data-og-width="1372" width="1372" data-og-height="1387" height="1387" data-path="images/install-github-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=74db4d5e2ebb869baec7fa8a5542fe1e 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=124a9fff587698addbf6521b889b5c28 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3141ed13276ff2da9a123ad94d1d98b9 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=aa841e9121554b8c1a75c35097e0d84b 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7abe3b886150b097a11ae90b41cae3f1 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=333c129e393ab4b32f04c3940492cf1c 2500w" />

You can modify repository access anytime in the Augment GitHub App settings.

### Configuring Triggers Per Repository

As the Administrator, you control when Augment Code Review triggers via [Settings](https://app.augmentcode.com/settings/code-review):

* **Automatic**: Augment Code Review will automatically review and post a comment as soon as the PR is opened for review in GitHub. Use it when your teams want immediate feedback on all pull requests.

* **Manual Command**: Augment Code Review is only triggered when someone comments on the PR with any of the following:  `auggie review`, `augment review`, or `augmentcode review` on GitHub. Use it when you want full control over when a review happens.

* **Disabled**: Augment Code Review will not run on the repository.

<img src="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=96c0f0dfc2186287a71bba713f7c31a6" alt="Trigger Types" className="rounded-xl" data-og-width="685" width="685" data-og-height="403" height="403" data-path="images/code-review-settings-triggers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=280&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=ec552a7eb0b39e85a412d191bf3c9c19 280w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=560&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=1cf11f2ee10f617961a22c17f36a6366 560w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=840&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=61f0470d5754359fa3a4375cc3112b46 840w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=1100&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=b2199c1921299daf014149220d31c120 1100w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=1650&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=fc80b5456761c3cf534b3db831fb52af 1650w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=2500&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=83c4d15d7a40b8253a01803de97354b8 2500w" />

If the repo is set to "Automatic" or "Manual Command", to run additional rounds of reviews on a subsequent commit of any PR, you can use the same manual trigger keywords (`auggie review`, `augment review`, or `augmentcode review`).

On public repositories, reviews are only triggered for PRs whose authors are members of the GitHub organization, outside collaborators to the organization or repository, or contributors to that repository.

## Change the GitHub Organization using Augment Code Review

Today, Code Review is limited to one GitHub organization per Enterprise account. Augment will address this limitation in an upcoming release. You can change the organization by reinstalling the Augment GitHub App.

* To get started you need to review the GitHub Apps installed on an organization:
  * In the top right corner of GitHub, click your profile picture, then click Your organizations.
  * Next to your organization name, click Settings.
  * In the side bar, under "Third-party Access," click GitHub Apps. A list of the GitHub Apps installed on your organization will be displayed.
  * Next to the GitHub App you want to review or modify, click Configure.
* To uninstall the Augment GitHub App, click Uninstall.
* To reinstall, visit: [https://github.com/apps/augmentcode/installations/new](https://github.com/apps/augmentcode/installations/new). Select your organization.

## Providing feedback

You can provide in product feedback directly in GitHub by reacting with a thumbs up or thumbs down emoji to the inline comment left by Augment Code Review.

<img src="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=4b5230f9a1ea82235d8275689aec130f" alt="Code Review Feedback using GitHub Reactions" className="rounded-xl place-self-center" data-og-width="524" width="524" data-og-height="163" height="163" data-path="images/code-review-github-feedback.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?w=280&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=462ec74def0372cb32ecc0d952a67878 280w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?w=560&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=8073845e10e05f4099306c21b441628f 560w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?w=840&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=27dbf7cfebe0d0d5745741af62cf8c58 840w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?w=1100&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=bf7c7d0b8fe09bc130c976ae43b3ba88 1100w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?w=1650&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=5c24ee5cbd38d0b1a8143bc6acf0479c 1650w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?w=2500&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=dd387ce425da7df2d6a42667b683e03e 2500w" />

## Tell Augment Code Review to check specific areas with guidelines

Domain knowledge that isn't always evident in the code. Tell Augment Code Review to check specific areas like security vulnerabilities or inside particular directories when relevant. Augment Code Review allows you to outline these special guidelines per repository. Describe any areas of focus using a yaml file entitled code\_review\_guidelines.yaml inside the .augment folder at the repository root:

`<repo-root>/.augment/code_review_guidelines.yaml`

Scope guidelines to the appropriate sub-directories and focus on objective issues that can cause bugs, expose vulnerabilities, etc. and less on stylistic or subjective things.

### Example Augment Code Review Guidelines

```yaml  theme={null}
# Guidelines exclusive to augmentcode/auggie

areas:
  databases:
    description: "Data and Database related rules"
    globs:
      - "**"
    rules:
      - id: "no_pii_in_bigquery"
        description: "Never store PII data in BigQuery tables."
        severity: "high"
      - id: "no_guid_keys"
        description: "GUID foreign keys can slow lookups"
        severity: "medium"

  memory_safety:
    description: "Ensure Memory Safety"
    globs:
      - "kernel/**"
    rules:
      - id: "avoid_unsafe_rust"
        description: "Avoid unsafe Rust operations."
        severity: "high"
```

### Explanation of the Guideline Format

**Areas:** Focus domain. Example: focus is “databases”

**Area Name**: Double quoted string written in snake case (ex: memory\_safety)

* **Description:** Double quoted message summarizing intent of the area
* **Globs** (short for global): Double quoted pattern-matching notation. Used to specify sets of filenames or paths using wildcard characters

<Note>
  Common **globs** or pattern matching syntax:

  * `**` - Matches any number of directories (recursive wildcard)
    * Example: `**/test.py` matches `test.py`, `src/test.py`, `src/utils/test.py`, etc.
  * `*` - Matches any sequence of characters within a single directory level
    * Example: `*.py` matches `file.py`, `main.py` but not `src/main.py`
  * `?` - Matches exactly one character
    * Example: `test?.py` matches `test1.py`, `testA.py` but not `test10.py`
</Note>

* **Rules:** Areas can contain more than one rule. Each rule contains:
  * **ID**: Double quoted title written in snake case (ex: avoid\_unsafe\_rust)
  * **Description**: Double quoted message summarizing intent of the rule
  * **Severity**: Expects double quoted “high”, “medium” or “low”. Sets the priority of review by Augment Code Review

## User Access

Administrators can specify a list of GitHub users who can trigger Augment Code Review by turning on **Allowlist Mode**.

When Allowlist Mode is active, only users in the allowlist will be able to trigger Augment Code Review. Automatic and manual reviews will be disabled for all other users. This is useful for organizations that want to limit access to the feature to a select group of users.

To manage permissions, visit [User Access for Code Review](https://app.augmentcode.com/settings/code-review/user-access).

## Model Context Protocol (MCP)

Administrators can connect Augment Code Review to external context sources through Model Context Protocol (MCP). Augment Code Review supports both local and remote MCP servers.

* Remote MCP servers run remotely and are hosted by providers. Once you add a remote MCP server, you may need to complete an OAuth flow to sign in to the server before it can be used by the code review agent.
* Local MCP servers run in their own environment within the code review agent's workspace. You can specify environment variables for local servers by clicking + MCP and then clicking + Environment Variable. Once set,
  environment variables are write-only and can only be overwritten or removed (not viewed) after the server has been added.

To configure MCP servers, visit [MCP for Code Review](https://app.augmentcode.com/settings/code-review/mcp).

## Code Review Analytics

Use the Code Review Analytics dashboard to track the review load automated by Augment, along with the comments made by Code Review that developers ultimately addressed.

1. **Navigate to Code Review** - In your browser, visit [Code Review Analytics](https://app.augmentcode.com/code-review/analytics).
2. **Filter by Date** - Refine your Analytics using the tabs for Last 7 Days, Last 30 Days, or Last 60 Days.

### Metric Definitions

* **Total PRs Reviewed**: The number of PRs that have been reviewed by Augment Code Review.
* **Total Reviews Performed**: The number of reviews that have been run by Augment Code Review. One PR can have multiple reviews if people manually trigger more reviews.
* **Total Comments**: The total number of inline comments left by Augment Code Review.
* **Percentage of Comments Addressed**: A comment is addressed if the developer resolved the concerns raised by the Augment Code Review comment. The percentage is calculated by dividing the number of addressed comments by the total number of comments left by Augment Code Review.
* **Percentage of Thumbs Up Reactions**: A thumbs up reaction is counted if a user reacts with the Thumbs Up emoji on GitHub on an inline comment left by Augment Code Review. The percentage is calculated by dividing the number of thumbs up reactions by the total number of thumbs up and thumbs down emoji reactions.
* **Estimated Dev Hours Saved**: Number of PRs multiplied by 10 minutes

### Reading the Charts

* **Addressed Comments**: A chart detailing total number of comments per day broken down by unaddressed (gray) vs addressed (green). You can interpret the green bar to mean Augment Code Review caught issues that developers fixed and may not have without the comment.
* **Reviewed PRs**: A chart detailing the total number of reviewed PRs per day (blue).

## Troubleshooting

### Stuck on Install button

If you still see the “Install” button on the Augment Code Review Settings page, then the Augment GitHub App installation failed. You will need to uninstall the Augment GitHub App from your organization and then reinstall it. Make sure the person installing the GitHub app has an Augment account and they see the "All set!" text after installing the app.

<Steps>
  <Step title="Navigate to the Augment GitHub App settings page on GitHub">
    Follow the steps on [GitHub Docs](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify) to modify the Augment GitHub App installation.
  </Step>

  <Step title="Uninstall the Augment GitHub App from your organization">
    In the Danger zone section, click on "Uninstall"
  </Step>

  <Step title="Reinstall the Augment GitHub App">
    Follow the steps in [Getting Started](/codereview/admin-guide#getting-started) again to install the app
  </Step>
</Steps>


# Using Augment Code Review
Source: https://docs.augmentcode.com/codereview/overview

Use Augment Code Review to catch critical issues, comment on PRs, and collaborate on fixes.

export const GitHubLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M7.49933 0.25C3.49635 0.25 0.25 3.49593 0.25 7.50024C0.25 10.703 2.32715 13.4206 5.2081 14.3797C5.57084 14.446 5.70302 14.2222 5.70302 14.0299C5.70302 13.8576 5.69679 13.4019 5.69323 12.797C3.67661 13.235 3.25112 11.825 3.25112 11.825C2.92132 10.9874 2.44599 10.7644 2.44599 10.7644C1.78773 10.3149 2.49584 10.3238 2.49584 10.3238C3.22353 10.375 3.60629 11.0711 3.60629 11.0711C4.25298 12.1788 5.30335 11.8588 5.71638 11.6732C5.78225 11.205 5.96962 10.8854 6.17658 10.7043C4.56675 10.5209 2.87415 9.89918 2.87415 7.12104C2.87415 6.32925 3.15677 5.68257 3.62053 5.17563C3.54576 4.99226 3.29697 4.25521 3.69174 3.25691C3.69174 3.25691 4.30015 3.06196 5.68522 3.99973C6.26337 3.83906 6.8838 3.75895 7.50022 3.75583C8.1162 3.75895 8.73619 3.83906 9.31523 3.99973C10.6994 3.06196 11.3069 3.25691 11.3069 3.25691C11.7026 4.25521 11.4538 4.99226 11.3795 5.17563C11.8441 5.68257 12.1245 6.32925 12.1245 7.12104C12.1245 9.9063 10.4292 10.5192 8.81452 10.6985C9.07444 10.9224 9.30633 11.3648 9.30633 12.0413C9.30633 13.0102 9.29742 13.7922 9.29742 14.0299C9.29742 14.2239 9.42828 14.4496 9.79591 14.3788C12.6746 13.4179 14.75 10.7025 14.75 7.50024C14.75 3.49593 11.5036 0.25 7.49933 0.25Z" fill="currentColor" />
  </svg>;

## Introduction

Augment Code Review provides a native GitHub experience for reviewing pull requests. With [Augment Code's extension](https://docs.augmentcode.com/quickstart#1-install-the-augment-extension) and [Auggie CLI](https://docs.augmentcode.com/cli/overview),
writing code is no longer the bottleneck—reviewing is. Code Review helps developers complete reviews faster while reducing bugs that reach production.

<CardGroup cols={1}>
  <Card title="Code Review Admin Guide" href="/codereview/admin-guide" icon="gear">
    Ask your plan Administrator to configure Augment Code Review and grant repository access on GitHub.
  </Card>
</CardGroup>

## Getting Started

Your plan Enterprise Administrator can [configure](https://app.augmentcode.com/settings/code-review) Augment Code Review to review automatically, or you can request a review by commenting on your PR.

* **Automatic Review on PR Opened:** Augment Code Review will automatically review and post a comment as soon as the PR is opened in GitHub. Use it when your teams want immediate feedback on all pull requests.
* **Request Review by Manual command:** Trigger a review by commenting on the PR with any of the following: `auggie review`, `augment review`, or `augmentcode review`. Augment Code Review will add 👀 to the comment so you know it is reviewing the PR. If Code Review finds an issue, it will leave a comment. If no issues are found, you'll see a comment saying "Review completed. No suggestions at this time."
* **Disabled:** Turn off Augment Code Review for a specific repository.

***

## How Augment Code Review Gathers Context

Code Review provides high-quality reviews by gathering context from multiple sources:

**PR Contents**: The agent analyzes the complete code diff to understand what changed and why.

**Entire Repository**: Through Augment's Context Engine, the agent has access to your full codebase, enabling it to identify cross-system impacts and maintain consistency with existing patterns.

**PR Title and Description**: More detailed PR descriptions help the agent provide better, more targeted reviews. Include information about:

* What the PR accomplishes
* Why the changes were made
* Any special considerations or context

**Custom Guidelines**: Repository-specific review guidelines defined in `.augment/code_review_guidelines.yaml` help the agent focus on what matters most to your team. See the [Admin Guide](/codereview/admin-guide#tell-augment-code-review-to-check-specific-areas-with-guidelines) for details on configuring guidelines.

**MCP Tools**: Integration with Model Context Protocol tools will provide additional context sources and capabilities.

***

## Review Quality and Focus

Augment Code Review prioritizes high signal-to-noise ratio by focusing on high-impact issues:

* **Bugs**: Logic errors, edge cases, and potential runtime issues
* **Security concerns**: Vulnerabilities, unsafe operations, and data exposure risks
* **Correctness**: Null handling and error management
* **Cross-system problems**: Breaking changes, API compatibility, and integration issues

The agent avoids low-value style nags and focuses on objective issues that can cause real problems in production.

***

## Best Practices

**Write detailed PR descriptions**: The more context you provide in your PR title and description, the better the agent can understand your intent and provide relevant feedback.

**Use custom guidelines**: Define repository-specific review guidelines to help the agent focus on your team's priorities and domain-specific concerns.

**Provide feedback**: Give feedback on comments using the thumbs up emoji to indicate whether the comment is useful or thumbs down if the comment was not helpful.

**Ask for a follow-up review**: If you make significant changes to the PR and want another review, then ask for a follow-up review by commenting on your PR with the same comments as a manual request: `auggie review`, `augment review`, or `augmentcode review`. The agent will add 👀 to the comment so you know it is reviewing the PR.


# Introduction
Source: https://docs.augmentcode.com/introduction

Augment is the developer AI platform that helps you understand code, debug issues, and ship faster because it understands your codebase. Use Agent, Next Edit, and Code Completions to get more done.

export const NextEditIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
        <g fill="none" fill-rule="evenodd">
            <path fill="#868686" d="M11.007 7c.126 0 .225-.091.246-.232.288-1.812.611-2.241 2.522-2.515.14-.021.225-.12.225-.253 0-.126-.084-.225-.225-.246-1.918-.274-2.157-.681-2.522-2.536-.028-.127-.12-.218-.246-.218-.133 0-.232.091-.253.225-.288 1.848-.604 2.255-2.515 2.53-.14.027-.232.119-.232.245 0 .133.091.232.232.253 1.918.274 2.164.674 2.515 2.522.028.14.127.225.253.225Z" />
            <path fill="#A7A7A7" d="M14.006 8.8c.075 0 .135-.055.147-.14.173-1.087.367-1.344 1.514-1.508.084-.013.134-.072.134-.152 0-.076-.05-.135-.134-.148-1.151-.164-1.295-.408-1.514-1.521-.017-.076-.072-.131-.147-.131-.08 0-.14.055-.152.135-.173 1.109-.363 1.353-1.51 1.517-.084.017-.138.072-.138.148 0 .08.054.14.139.152 1.15.164 1.298.404 1.509 1.513.017.084.076.135.152.135Z" opacity=".6" />
            <g fill="#5f6368">
            <path fill-rule="nonzero" d="m5.983 4.612 4.22 4.22c.433.434.78.945 1.022 1.507l1.323 3.069a.908.908 0 0 1-1.192 1.192l-3.07-1.323a4.84 4.84 0 0 1-1.505-1.022L2.56 8.035l3.423-3.423Zm-.001 1.711L4.271 8.034l3.365 3.365c.27.271.582.497.922.67l.208.097 2.37 1.022-1.022-2.37a3.63 3.63 0 0 0-.61-.963l-.157-.167-3.365-3.365Zm-.706-2.417L1.854 7.327l-.096-.104a2.42 2.42 0 0 1 3.518-3.317Z" />
            <path d="m11.678 11.388.87 2.02a.908.908 0 0 1-1.192 1.192l-2.02-.87 2.342-2.342ZM5.303 3.933l4.9 4.9c.084.083.164.17.242.26L7.04 12.497a4.84 4.84 0 0 1-.26-.242l-4.9-4.9a2.42 2.42 0 0 1 3.422-3.422Z" />
            </g>
        </g>
    </svg>;

export const CodeIcon = () => <svg xmlns="http://www.w3.org/2000/svg" height="28px" viewBox="0 -960 960 960" width="28px" fill="#5f6368">
    <path d="M336-240 96-480l240-240 51 51-189 189 189 189-51 51Zm288 0-51-51 189-189-189-189 51-51 240 240-240 240Z" />
  </svg>;

export const AgentIcon = () => <svg xmlns="http://www.w3.org/2000/svg" fill="#5f6368" width="28px" height="28px" viewBox="0 0 24 24">
    <path d="M13.5 2c0 .444-.193.843-.5 1.118V5h5a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3V8a3 3 0 0 1 3-3h5V3.118A1.5 1.5 0 1 1 13.5 2M6 7a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8a1 1 0 0 0-1-1H6m-4 3H0v6h2zm20 0h2v6h-2zM9 14.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3m6 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3" />
  </svg>;

<img className="block rounded-xl" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-hero-sm.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=722e4d813b50af9ef62afe26ae8bc692" alt="Augment Code" data-og-width="800" width="800" data-og-height="467" height="467" data-path="images/augment-hero-sm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-hero-sm.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a7f3fce08052d5f9cbf8cd2daf5975d3 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-hero-sm.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=57bfcadfe99cec702c1887f8bb04588e 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-hero-sm.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=824609d7459789a8ba19d0d9fe92e652 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-hero-sm.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b9fb39b5ffe6b5434bb283c8b7b66d6f 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-hero-sm.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a159a7925ec305e88beffb0d92a11fab 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-hero-sm.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c4550439f717627f0dfc854b93bb7444 2500w" />

## Get started in minutes

Augment works with your favorite IDE and your favorite programming language. Download the extension, sign in, and get coding.

<CardGroup cols={3}>
  <Card href="/setup-augment/install-visual-studio-code">
    <img className="w-12 h-12" src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1743e6c5d410f0c71016833690fa837e" alt="Visual Studio Code" data-og-width="64" width="64" data-og-height="64" height="64" data-path="images/vscode-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=6cc12e25432edf2e06f49d14373ac02d 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ed9401ed757b8de4c9d22f5293519da2 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ae9c1a6c3d5a2c7ac3a8530141d306d6 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b1a41a3a74fa9479caecca707cdc5325 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=7ae0cb9f27f612e21a7d60dc0fd6e817 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1cc411059b25f0fde0a0406eb9a0fc42 2500w" />

    <h2 className="pt-4 font-semibold text-base text-gray-800 dark:text-white">
      Visual Studio Code
    </h2>

    <p>
      Get completions, chat, and instructions in your favorite open source
      editor.
    </p>
  </Card>

  <Card className="bg-red" href="/setup-augment/install-jetbrains-ides">
    <img className="w-12 h-12" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c66ced5a9325498d8bfd13c09f308737" alt="JetBrains IDEs" data-og-width="64" width="64" data-og-height="64" height="64" data-path="images/jetbrains-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=19dbd0eee0903c4754190f5c5e14f204 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=256d16be8c5cee0ad668722591312714 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=47717f8a5dc2f992e7cd40bceea7dc7a 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6de74610603515a436cdd6ebbe50758c 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=81875705a8d31362022665f5edcd7385 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5cc81b977488e24b7a9ad9c2f305d084 2500w" />

    <h2 className="pt-4 font-semibold text-base text-gray-800 dark:text-white">
      JetBrains IDEs
    </h2>

    <p>
      Completions are available for all JetBrains IDEs, like WebStorm, PyCharm,
      and IntelliJ.
    </p>
  </Card>

  <Card className="bg-red" href="/cli/overview">
    <img className="w-12 h-12" src="https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=296dbf9e9899ad6582c82bc3c7a44057" alt="Auggie CLI" data-og-width="230" width="230" data-og-height="230" height="230" data-path="images/cli.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=280&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=3821a862d7ae772e4b8f5c94763b938e 280w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=560&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=f466ec96e10fad60ee1efda5cbd9ca1d 560w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=840&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=e001eadbaa9a022e8eafac2c83f80157 840w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=1100&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=d2601529bf4c2f49fd28ef7b52d16d51 1100w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=1650&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=06faa3a54ba7278fedd6a85b208b1434 1650w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=2500&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=224824a6b754861089245e04a1a80cf0 2500w" />

    <h2 className="pt-4 font-semibold text-base text-gray-800 dark:text-white">
      Auggie CLI
    </h2>

    <p>
      All the power of Augment's agent, context engine, and tools in your terminal.
    </p>
  </Card>
</CardGroup>

## Learn more

Get up to speed, stay in the flow, and get more done. Chat, Next Edit, and Code Completions will change the way you build software.

<CardGroup cols={3}>
  <Card title="Agent" icon={<AgentIcon />} href="/using-augment/agent">
    Autonomous coding with Augment's context engine and tools can tackle tasks big and small
  </Card>

  <Card title="Next Edit" icon={<NextEditIcon />} href="/using-augment/next-edit">
    Keep moving through your tasks by guiding you step-by-step through complex or repetitive changes.
  </Card>

  <Card title="Code Completions" icon={<CodeIcon />} href="/using-augment/completions">
    Intelligent code suggestions that knows your codebase right at your
    fingertips.
  </Card>
</CardGroup>


# Agent Integrations
Source: https://docs.augmentcode.com/jetbrains/setup-augment/agent-integrations

Configure integrations for Augment Agent to access external services like GitHub, Linear, Jira, Confluence, and Notion.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const GleanLogo = () => <svg width="24" height="24" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M8.95113 2.67649L10.2775 1L11.887 2.24179L10.5704 3.906C11.25 4.70862 11.6591 5.74239 11.6591 6.87053C11.6591 9.42425 9.56277 11.4945 6.9768 11.4945C4.39084 11.4945 2.29451 9.42425 2.29451 6.87053C2.29451 4.31677 4.39084 2.24655 6.9768 2.24655C7.68222 2.24655 8.35119 2.4006 8.95113 2.67649ZM6.9768 9.50853C5.50146 9.50853 4.30546 8.32747 4.30546 6.87053C4.30546 5.41358 5.50146 4.23245 6.9768 4.23245C8.45215 4.23245 9.64814 5.41358 9.64814 6.87053C9.64814 8.32747 8.45215 9.50853 6.9768 9.50853ZM11.7135 10.8261C11.5975 10.9618 11.4753 11.0913 11.3477 11.2173C11.2202 11.3424 11.0873 11.4622 10.949 11.5758C10.8116 11.6894 10.6689 11.7969 10.5208 11.8982C10.3736 11.9995 10.2211 12.0955 10.065 12.1837C9.90978 12.2726 9.75012 12.3537 9.58684 12.4286C9.42448 12.5034 9.25856 12.5712 9.08906 12.6311C8.92046 12.6919 8.74919 12.7448 8.57434 12.7898C8.40217 12.8365 8.22645 12.8743 8.04892 12.9043C7.87319 12.9351 7.69478 12.958 7.51459 12.973C7.33706 12.988 7.15776 12.9959 6.97667 12.9959C6.79558 12.9959 6.61628 12.988 6.43876 12.973C6.25856 12.958 6.08016 12.9351 5.90441 12.9043C5.7269 12.8743 5.55116 12.8365 5.379 12.7898L4.85357 14.726C5.08194 14.7868 5.31565 14.838 5.55206 14.8784C5.78488 14.919 6.02217 14.9498 6.26213 14.9692C6.49763 14.9895 6.73582 15 6.97667 15C7.21753 15 7.4557 14.9895 7.69121 14.9692C7.93117 14.9498 8.16756 14.919 8.40129 14.8784C8.63768 14.838 8.87051 14.7868 9.09977 14.726C9.33171 14.6662 9.56007 14.5957 9.7831 14.5147C10.0088 14.4345 10.2291 14.3446 10.445 14.2451C10.6617 14.1455 10.8741 14.0372 11.0802 13.92C11.2871 13.802 11.4887 13.6751 11.684 13.5394C11.8803 13.4047 12.0704 13.2619 12.2532 13.1104C12.437 12.9589 12.6136 12.8003 12.7822 12.6338C12.9517 12.4673 13.1131 12.2946 13.2675 12.1141C13.4218 11.9343 13.5681 11.7467 13.7055 11.5538L12.0435 10.4041C11.9401 10.5495 11.8295 10.6905 11.7135 10.8261Z" fill="currentColor" />
</svg>;

export const ConfluenceLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M2.43703 10.7785C2.30998 10.978 2.16478 11.2137 2.05588 11.3951C1.94698 11.5764 2.00143 11.8121 2.18293 11.921L4.66948 13.4442C4.85098 13.553 5.08695 13.4986 5.19585 13.3173C5.2866 13.1541 5.41365 12.9365 5.55885 12.7007C6.53895 11.0868 7.5372 11.2681 9.3159 12.1204L11.7843 13.281C11.9839 13.3717 12.2017 13.281 12.2925 13.0997L13.4722 10.4339C13.563 10.2526 13.4722 10.0169 13.2907 9.92619C12.7644 9.69044 11.7298 9.20084 10.8223 8.74749C7.44645 7.13354 4.59689 7.24234 2.43703 10.7785Z" fill="currentColor" />
  <path d="M13.563 4.72157C13.69 4.52209 13.8352 4.28635 13.9441 4.105C14.053 3.92366 13.9985 3.68791 13.817 3.57911L11.3305 2.05583C11.149 1.94702 10.913 2.00143 10.8041 2.18277C10.7134 2.34598 10.5863 2.56359 10.4411 2.79934C9.461 4.41329 8.46275 4.23194 6.68405 3.37963L4.21563 2.21904C4.01598 2.12837 3.79818 2.21904 3.70743 2.40038L2.52767 5.0661C2.43692 5.24745 2.52767 5.4832 2.70917 5.5739C3.23552 5.80965 4.27007 6.29925 5.1776 6.7526C8.53535 8.34845 11.3849 8.25775 13.563 4.72157Z" fill="currentColor" />
</svg>;

export const JiraLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.5028 2H7.7257C7.7257 3.44 8.8914 4.60571 10.3314 4.60571H11.3942V5.6343C11.3942 7.0743 12.5599 8.24 14 8.24V2.49714C14 2.22285 13.7771 2 13.5028 2ZM10.6399 4.88H4.86279C4.86279 6.32 6.0285 7.4857 7.4685 7.4857H8.53135V8.5143C8.53135 9.9543 9.69705 11.12 11.137 11.12V5.37715C11.137 5.10285 10.9142 4.88 10.6399 4.88ZM2 7.75995H7.7771C8.0514 7.75995 8.27425 7.9828 8.27425 8.2571V13.9999C6.83425 13.9999 5.66855 12.8342 5.66855 11.3942V10.3656H4.6057C3.16571 10.3656 2 9.19995 2 7.75995Z" fill="currentColor" />
</svg>;

export const NotionLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M3.47498 3.32462C3.92288 3.68848 4.0909 3.66071 4.93192 3.60461L12.8609 3.12851C13.029 3.12851 12.8892 2.96075 12.8332 2.93286L11.5163 1.98091C11.264 1.78502 10.9278 1.56068 10.2835 1.6168L2.60594 2.17678C2.32595 2.20454 2.27001 2.34453 2.38153 2.45676L3.47498 3.32462ZM3.95103 5.17244V13.5151C3.95103 13.9634 4.17508 14.1312 4.67938 14.1035L13.3933 13.5992C13.8978 13.5715 13.954 13.263 13.954 12.8989V4.61222C13.954 4.24858 13.8142 4.05248 13.5053 4.08047L4.39915 4.61222C4.06311 4.64046 3.95103 4.80855 3.95103 5.17244ZM12.5534 5.61996C12.6093 5.87218 12.5534 6.12417 12.3007 6.15251L11.8808 6.23616V12.3952C11.5163 12.5911 11.1801 12.7031 10.9 12.7031C10.4516 12.7031 10.3392 12.5631 10.0033 12.1433L7.257 7.83198V12.0034L8.12602 12.1995C8.12602 12.1995 8.12602 12.7031 7.4249 12.7031L5.49203 12.8152C5.43588 12.7031 5.49203 12.4235 5.68808 12.3673L6.19248 12.2276V6.71226L5.49215 6.65615C5.43599 6.40392 5.57587 6.04029 5.96841 6.01205L8.04196 5.87229L10.9 10.2398V6.37615L10.1713 6.29251C10.1154 5.98418 10.3392 5.76029 10.6195 5.73252L12.5534 5.61996ZM1.96131 1.42092L9.94726 0.832827C10.928 0.748715 11.1803 0.805058 11.7967 1.25281L14.3458 3.04451C14.7665 3.35262 14.9067 3.4365 14.9067 3.77237V13.5992C14.9067 14.215 14.6823 14.5793 13.8979 14.635L4.6239 15.1951C4.03509 15.2231 3.75485 15.1392 3.4465 14.747L1.56922 12.3113C1.23284 11.863 1.09296 11.5276 1.09296 11.1351V2.40043C1.09296 1.89679 1.31736 1.47669 1.96131 1.42092Z" fill="currentColor" />
  </svg>;

export const LinearLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M1.17156 9.61319C1.14041 9.4804 1.2986 9.39676 1.39505 9.49321L6.50679 14.6049C6.60323 14.7014 6.5196 14.8596 6.38681 14.8284C3.80721 14.2233 1.77669 12.1928 1.17156 9.61319ZM1.00026 7.56447C0.997795 7.60413 1.01271 7.64286 1.0408 7.67096L8.32904 14.9592C8.35714 14.9873 8.39586 15.0022 8.43553 14.9997C8.76721 14.9791 9.09266 14.9353 9.41026 14.8701C9.51729 14.8481 9.55448 14.7166 9.47721 14.6394L1.36063 6.52279C1.28337 6.44552 1.15187 6.48271 1.12989 6.58974C1.06466 6.90734 1.02092 7.23278 1.00026 7.56447ZM1.58953 5.15875C1.56622 5.21109 1.57809 5.27224 1.6186 5.31275L10.6872 14.3814C10.7278 14.4219 10.7889 14.4338 10.8412 14.4105C11.0913 14.2991 11.3336 14.1735 11.5672 14.0347C11.6445 13.9888 11.6564 13.8826 11.5929 13.819L2.18099 4.40714C2.11742 4.34356 2.01121 4.35549 1.96529 4.43278C1.8265 4.66636 1.70091 4.9087 1.58953 5.15875ZM2.77222 3.53036C2.7204 3.47854 2.7172 3.39544 2.76602 3.34079C4.04913 1.9043 5.9156 1 7.99327 1C11.863 1 15 4.13702 15 8.00673C15 10.0844 14.0957 11.9509 12.6592 13.234C12.6046 13.2828 12.5215 13.2796 12.4696 13.2278L2.77222 3.53036Z" fill="currentColor" />
  </svg>;

export const GitHubLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M7.49933 0.25C3.49635 0.25 0.25 3.49593 0.25 7.50024C0.25 10.703 2.32715 13.4206 5.2081 14.3797C5.57084 14.446 5.70302 14.2222 5.70302 14.0299C5.70302 13.8576 5.69679 13.4019 5.69323 12.797C3.67661 13.235 3.25112 11.825 3.25112 11.825C2.92132 10.9874 2.44599 10.7644 2.44599 10.7644C1.78773 10.3149 2.49584 10.3238 2.49584 10.3238C3.22353 10.375 3.60629 11.0711 3.60629 11.0711C4.25298 12.1788 5.30335 11.8588 5.71638 11.6732C5.78225 11.205 5.96962 10.8854 6.17658 10.7043C4.56675 10.5209 2.87415 9.89918 2.87415 7.12104C2.87415 6.32925 3.15677 5.68257 3.62053 5.17563C3.54576 4.99226 3.29697 4.25521 3.69174 3.25691C3.69174 3.25691 4.30015 3.06196 5.68522 3.99973C6.26337 3.83906 6.8838 3.75895 7.50022 3.75583C8.1162 3.75895 8.73619 3.83906 9.31523 3.99973C10.6994 3.06196 11.3069 3.25691 11.3069 3.25691C11.7026 4.25521 11.4538 4.99226 11.3795 5.17563C11.8441 5.68257 12.1245 6.32925 12.1245 7.12104C12.1245 9.9063 10.4292 10.5192 8.81452 10.6985C9.07444 10.9224 9.30633 11.3648 9.30633 12.0413C9.30633 13.0102 9.29742 13.7922 9.29742 14.0299C9.29742 14.2239 9.42828 14.4496 9.79591 14.3788C12.6746 13.4179 14.75 10.7025 14.75 7.50024C14.75 3.49593 11.5036 0.25 7.49933 0.25Z" fill="currentColor" />
  </svg>;

## About Agent Integrations

Augment Agent can access external services through integrations to add additional context to your requests and take actions on your behalf. These integrations allow Augment Agent to seamlessly work with your development tools without leaving your editor.

Once set up, Augment Agent will automatically use the appropriate integration based on your request context. Or, you can always mention the service in your request to use the integration.

## Setting Up Integrations

To set up integrations with Augment Agent in JetBrains IDEs, follow these steps:

1. Click the Augment icon in the bottom right of your IDE and select <Command text="Tools Settings" />
2. Click "Connect" for the integration you want to set up

<img className="block rounded-xl" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=8e1cb7e476ff72baf79853e1a396061a" alt="Set up integrations in the settings page" data-og-width="1096" width="1096" data-og-height="598" height="598" data-path="images/integration-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6b58b42005ec712d925971f18e71f0df 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b0347aaa6924edd4a61a6ed59e70f84c 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=50b67616fb88ab7b1620628cf09c5c40 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=66664659b4ca1d32c356fbf0e72b2778 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ccfd90b3fe548564b1c3482f5d4d0e95 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f78ecdd094cea06ca826da1580683efc 2500w" />

You'll be redirected to authorize the integration with the appropriate service. After authorization, the integration will be available for use with Augment Agent.

## Easy MCP Integrations

> **New:** Easy MCP launched ONLY July 30, 2025, providing one-click access to popular developer tools.

Easy MCP transforms complex MCP server setup into a single click. Available integrations include:

* **CircleCI** - Build logs, test insights, and flaky-test detection
* **MongoDB** - Data exploration, database management, and context-aware code generation
* **Redis** - Keyspace introspection, TTL audits, and migration helpers

For detailed setup instructions and examples, see [Configure MCP servers](/jetbrains/setup-augment/mcp).

## Native Integrations

## <div className="flex items-center gap-2"><div className="w-6 h-6"><GitHubLogo /></div> GitHub Integration</div>

Add additional context to your requests and take actions. Pull in information from a GitHub Issue, make the changes to your code (or have Agent do it for you), and open a Pull Request all without leaving your editor.

### Examples

* "Implement Issue #123 and open up a pull request"
* "Find all issues assigned to me"
* "Check the CI status of my latest commit"

For authorization details, see [GitHub documentation](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party).

## <div className="flex items-center gap-2"><div className="w-6 h-6"><LinearLogo /></div> Linear Integration</div>

Read, update, comment on, and resolve your Linear issues within your IDE.

### Examples

* "Fix TES-1"
* "Create Linear tickets for these TODOs"
* "Help me triage these new bug reports"

For authorization details, see [Linear documentation](https://linear.app/docs/third-party-application-approvals).

## <div className="flex items-center gap-2"><div className="w-6 h-6"><JiraLogo /></div> Jira Integration</div>

Work on your Jira issues, create new tickets, and update existing ones.

### Examples

* "Show me all my assigned Jira tickets"
* "Create a Jira ticket for this bug"
* "Create a PR to fix SOF-123"
* "Update the status of PROJ-123 to 'In Progress'"

For authorization details, see [Jira documentation](https://support.atlassian.com/jira-software-cloud/docs/allow-oauth-access/).

## <div className="flex items-center gap-2"><div className="w-6 h-6"><ConfluenceLogo /></div> Confluence Integration</div>

Query existing documentation or update pages directly from your IDE. Ensure your team's knowledge base stays current without any context switching.

### Examples

* "Summarize our Confluence page on microservice architecture"
* "Find information about our release process in Confluence"
* "Update our onboarding docs to explain how we use Bazel"

For authorization details, see [Confluence documentation](https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/).

## <div className="flex items-center gap-2"><div className="w-6 h-6"><NotionLogo /></div> Notion Integration</div>

Search and retrieve information from your team's knowledge base - access documentation, meeting notes, and project specifications. This integration is currently READ-ONLY.

### Examples

* "Find Notion pages about our API documentation"
* "Show me the technical specs for the payment system"
* "What outstanding tasks are left from yesterday's team meeting?"

For authorization details, see [Notion documentation](https://www.notion.so/help/add-and-manage-connections-with-the-api#install-from-a-developer).

## <div className="flex items-center gap-2"><div className="w-6 h-6"><GleanLogo /></div> Glean Integration</div>

> **Note:** The Glean integration is in early access and thus is a little different from other integrations.
>
> * It is currently only available to enterprise customers.
> * It does not appear in the list of integrations in the settings panel.

The Glean integration lets the agent retrieve information from your team's internal data sources leveraging Glean's powerful search engine.

**To Enable the Glean Integration:** You'll need to be have administrator access to Augment and Glean. Follow the instructions on [https://app.augmentcode.com/gleanConfig](https://app.augmentcode.com/gleanConfig) and your agent will be ready to use Glean!

### Examples

* "Search Glean for past related incidents and how they were resolved"
* "Search Glean for why we're migrating to a new payment processor"

## Next Steps

* [Configure additional tools with Easy MCP or advanced MCP setup](/jetbrains/setup-augment/mcp)
* Explore one-click integrations for CircleCI, MongoDB, and Redis through Easy MCP


# Install Augment for JetBrains IDEs
Source: https://docs.augmentcode.com/jetbrains/setup-augment/install-jetbrains-ides

Are you ready for your new superpowers? Augment in JetBrains IDEs gives you powerful code completions integrated into your favorite text editor.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const ExternalLink = ({text, href}) => <a href={href} rel="noopener noreferrer">
    {text}
  </a>;

export const JetbrainsLogo = () => <svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 64 64">
    <defs>
      <linearGradient id="linear-gradient" x1=".8" y1="3.3" x2="62.6" y2="64.2" gradientTransform="translate(0 66) scale(1 -1)" gradientUnits="userSpaceOnUse">
        <stop offset="0" stop-color="#ff9419" />
        <stop offset=".4" stop-color="#ff021d" />
        <stop offset="1" stop-color="#e600ff" />
      </linearGradient>
    </defs>
    <path fill="url(#linear-gradient)" d="M20.3,3.7L3.7,20.3c-2.3,2.3-3.7,5.5-3.7,8.8v29.8c0,2.8,2.2,5,5,5h29.8c3.3,0,6.5-1.3,8.8-3.7l16.7-16.7c2.3-2.3,3.7-5.5,3.7-8.8V5c0-2.8-2.2-5-5-5h-29.8c-3.3,0-6.5,1.3-8.8,3.7Z" />
    <path fill="#000" d="M48,16H8v40h40V16Z" />
    <path fill="#fff" d="M30,47H13v4h17v-4Z" />
  </svg>;

<Info>
  Augment requires version `2024.3` or above for all JetBrains IDEs. [See
  JetBrains documentation](https://www.jetbrains.com/help/) on how to update
  your IDE.
</Info>

<CardGroup cols={1}>
  <Card title="Get the Augment Plugin" href="https://plugins.jetbrains.com/plugin/24072-augment" icon={<JetbrainsLogo />} horizontal>
    Install Augment for JetBrains IDEs
  </Card>
</CardGroup>

## About Installation

Installing <ExternalLink text="Augment for JetBrains IDEs" href="https://plugins.jetbrains.com/plugin/24072-augment" /> is easy and will take you less than a minute. Augment is compatible with all JetBrains IDEs, including WebStorm, PyCharm, and IntelliJ. You can find the Augment plugin in the JetBrains Marketplace and install it following the instructions below.

<img className="block rounded-xl" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-plugin.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=fb1192b9ebe85582db42bf74930e5db7" alt="Augment plugin in JetBrains Marketplace" data-og-width="1652" width="1652" data-og-height="614" height="614" data-path="images/jetbrains-plugin.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-plugin.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7cf23a610416c92a090102197f118329 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-plugin.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=228154ff41eac23a3a2b2fd504477e00 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-plugin.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c9ae50fc32ff2be92f6909372b67e941 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-plugin.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d844406a7c5173c4dc63281ade8d0990 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-plugin.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=97762b433cae13d097f40b1120803374 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-plugin.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=9039fe18ab88f1df9ddb047a7da9518c 2500w" />

## Installing Augment for JetBrains IDEs

<Note>
  For these instructions we'll use *JetBrains IntelliJ* as an example, anywhere
  you see *IntelliJ* replace the name of the JetBrains IDE you're using.

  In the case of Android Studio, which is based on IntelliJ, please ensure that your installation
  uses a runtime with JCEF. Go to <Command text="Help > Find Action" />, type <Command text="Choose Boot Java Runtime for the IDE" />
  and press <Keyboard shortcut="Enter" />. Ensure the current runtime ends with `-jcef`; if not, select one **with JCEF** from the options
  below.
</Note>

<Steps>
  <Step title="Make sure you have the latest version of your IDE installed">
    You can download the latest version of JetBrains IDEs from the <ExternalLink text="JetBrains" href="https://www.jetbrains.com/ides/#choose-your-ide" />
    website. If you already have IntelliJ installed, you can update to the
    latest version by going to{" "}
    <Command text="IntelliJ IDEA > Check for Updates..." />.
  </Step>

  <Step title="Open the Plugins settings in your IDE">
    From the menu bar, go to <Command text="IntelliJ IDEA > Settings..." />, or
    use the keyboard shortcut <Keyboard shortcut="Cmd/Ctrl ," /> to open the
    Settings window. Select <Command text="Plugins" /> from the sidebar.
  </Step>

  <Step title="Search for Augment in the marketplace">
    Using the search bar in the Plugins panel, search for{" "}
    <Command text="Augment" />.
  </Step>

  <Step title="Install the extension">
    Click <Command text="Install" /> to install the extension. Then click{" "}
    <Command text="OK" /> to close the Settings window.
  </Step>

  <Step title="Sign into Augment and get coding">
    Sign in to by clicking <Command text="Sign in to Augment" /> in the Augment
    panel. If you do not see the Augment panel, use the shortcut{" "}
    <Keyboard shortcut="Cmd/Ctrl L" /> or click the Augment icon{" "}
    <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a659f6a8cc305adb98f17ffe362de081" className="inline h-3 p-0 m-0" data-og-width="18" width="18" data-og-height="12" height="12" data-path="images/augment-icon-simple.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4a291cdc6d1243c7730017b000deec5b 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5d30f5b2920cba98990963c02c18a39a 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d4ba43987e110d9065c707ef4c6f09d7 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f6ec12c894c73d1c344b5cce54ff19d3 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=af28ff3eeed5be9bbb6c8156e0d94bce 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=549509ac3a1fbdeb2700fb4b9f8f03ad 2500w" /> in the side bar of your IDE. See more details in [Sign
    In](/setup-augment/sign-in).
  </Step>
</Steps>

## Installing Beta versions of Augment for JetBrains IDEs

In order to get a specific bug fix or feature, sometimes you may need to *temporarily* install a beta version of Augment for JetBrains IDEs.
To do this, follow the steps below:

<Steps>
  <Step title="Download an archive of the beta version">
    You can download the latest beta version of Augment from <ExternalLink text="JetBrains Marketplace" href="https://plugins.jetbrains.com/plugin/24072-augment/versions/beta?noRedirect=true" />
    website. Please click <Command text="Download" /> on the latest version and save the archive to disk.
  </Step>

  <Step title="Open the Plugins settings in your IDE">
    From the menu bar, go to <Command text="IntelliJ IDEA > Settings..." />, or
    use the keyboard shortcut <Keyboard shortcut="Cmd/Ctrl ," /> to open the
    Settings window. Select <Command text="Plugins" /> from the sidebar.
  </Step>

  <Step title="Install Augment from the downloaded archive">
    Click on the gear icon next to <Command text="Installed" /> tab and click <Command text="Install plugin from disk..." />.
    Select the archive you downloaded in the previous step and click <Command text="OK" />.
  </Step>
</Steps>


# Keyboard Shortcuts for JetBrains IDEs
Source: https://docs.augmentcode.com/jetbrains/setup-augment/jetbrains-keyboard-shortcuts

Augment integrates with your IDE to provide keyboard shortcuts for common actions. Use these shortcuts to quickly accept suggestions, write code, and navigate your codebase.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About keyboard shortcuts

Augment is deeply integrated into your IDE and utilizes many of the standard keyboard shortcuts you are already familiar with. These shortcuts allow you to quickly accept suggestions, write code, and navigate your codebase. We also suggest updating a few keyboard shortcuts to make working with code suggestions even easier.

<Tabs>
  <Tab title="MacOS">
    To update keyboard shortcuts, use one of the following:

    | Method   | Action                                                         |
    | :------- | :------------------------------------------------------------- |
    | Keyboard | <Keyboard shortcut="Cmd ," /> select <Command text="Keymap" /> |
    | Menu bar | <Command text="IntelliJ IDEA > Settings > Keymap" />           |

    ## General

    | Action             | Default shortcut                     |
    | :----------------- | :----------------------------------- |
    | Open Augment panel | <Keyboard shortcut="Cmd Option I" /> |

    ## Chat

    | Action                   | Default shortcut                     |
    | :----------------------- | :----------------------------------- |
    | Focus or open Chat panel | <Keyboard shortcut="Cmd Option I" /> |

    ## Completions

    | Action                       | Default shortcut                     |
    | :--------------------------- | :----------------------------------- |
    | Accept entire suggestion     | <Keyboard shortcut="Tab" />          |
    | Accept word-by-word          | <Keyboard shortcut="Option Right" /> |
    | Reject suggestion            | <Keyboard shortcut="Esc" />          |
    | Toggle automatic completions | <Keyboard shortcut="Cmd Option 9" /> |
  </Tab>

  <Tab title="Windows/Linux">
    To update keyboard shortcuts, use one of the following:

    | Method   | Action                                                               |
    | :------- | :------------------------------------------------------------------- |
    | Keyboard | <Keyboard shortcut="Ctrl ," /> then select <Command text="Keymap" /> |
    | Menu bar | <Command text="File > Settings > Keymap" />                          |

    ## General

    | Action             | Default shortcut                   |
    | :----------------- | :--------------------------------- |
    | Open Augment panel | <Keyboard shortcut="Ctrl Alt I" /> |

    ## Chat

    | Action                   | Default shortcut                   |
    | :----------------------- | :--------------------------------- |
    | Focus or open Chat panel | <Keyboard shortcut="Ctrl Alt I" /> |

    ## Completions

    | Action                       | Default shortcut                   |
    | :--------------------------- | :--------------------------------- |
    | Accept entire suggestion     | <Keyboard shortcut="Tab" />        |
    | Accept word-by-word          | <Keyboard shortcut="Ctrl Right" /> |
    | Reject suggestion            | <Keyboard shortcut="Esc" />        |
    | Toggle automatic completions | <Keyboard shortcut="Ctrl Alt 9" /> |
  </Tab>
</Tabs>


# Setup Model Context Protocol servers
Source: https://docs.augmentcode.com/jetbrains/setup-augment/mcp

Use Model Context Protocol (MCP) servers with Augment to expand Augment's capabilities with external tools and data sources.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## About Model Context Protocol servers

Augment Agent can utilize external integrations through Model Context Protocol (MCP) to access external systems for information and integrate tools to take actions. MCP is an open protocol that provides a standardized way to connect AI models to different data sources and tools. MCP servers can be used to access local or remote databases, run automated browser testing, send messages to Slack or even play music on Spotify.

## Easy MCP: One-Click Integrations

> **New:** Easy MCP launched on July 30, 2025, making it easier than ever to connect popular developer tools to Augment Code.

Easy MCP is a new feature in the Augment Code extension that transforms complex MCP server setup into a single click. Instead of manually configuring servers, hunting for GitHub repos, or editing JSON files, you can now connect popular developer tools with just an API token or OAuth approval.

### Available Easy MCP Integrations

Easy MCP provides one-click access to these popular developer tools:

#### CircleCI

* **Context:** Build logs, test insights, flaky-test detection
* **Sample prompt:** "Find the latest failed pipeline on my branch and surface the failing tests."
* **Setup:** Click "+", paste your CircleCI API token, and you're connected.

#### MongoDB

* **Context:** Data exploration, database management, and context-aware code generation
* **Sample prompt:** "Analyze my user collection schema and suggest optimizations for our new search feature."
* **Setup:** One-click OAuth connection to your MongoDB instance.

#### Redis

* **Context:** Keyspace introspection, TTL audits, and migration helpers
* **Sample prompt:** "Generate a migration script to move expiring session keys to the new namespace."
* **Setup:** Connect with your Redis credentials in seconds.

### Getting Started with Easy MCP

1. Open the Augment Code extension in your JetBrains IDE
2. Navigate to the Easy MCP pane in the settings
3. Click the "+" button next to your desired integration
4. Paste an API token or approve OAuth
5. Start using the integration immediately in your Agent conversations

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c02010664a36e319631e3f5367f5f00e" className="rounded-xl" data-og-width="1078" width="1078" data-og-height="646" height="646" data-path="images/EasyMCP.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b26a28d983527d327bc35e249eabf1a8 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7e06026e10eefc855da6579dac1dea47 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3c6df59927adaa82ba7427ad8f0defa2 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=849c567deb9a052d933a4aa31f492dec 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3e66c48df372bb4e699350f8073ff0c6 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cda0cb53a2619c7cb2adffe3a12c3c38 2500w" />

From that moment on, Augment Code streams your tool's live context into every suggestion and autonomous Agent run.

## Advanced Configuration: Settings Panel

For developers who need custom MCP server configurations or want to use servers not available through Easy MCP, you can configure MCP servers manually using the Augment Settings Panel.

To access the settings panel, select the gear icon in the upper right of the Augment panel. Once the settings panel is open, you will see a section for MCP servers.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=f34e3682127f6e6ba2dfc5a4ae7fd8a5" className="rounded-xl" data-og-width="1296" width="1296" data-og-height="556" height="556" data-path="images/settings-panel-mcp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a6dff18658e5c7454fa009cc484467db 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=dbc7a07976708c4fc72a662b98c06c60 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e382a538a495053c3ca1a3c01d5e85ba 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=2efdfd04627b5a659795e5b74e672b4d 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=d0f3ce6ce06c668a2f3160a35c0586e5 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e4b1e413786735c373fb6ec386cd676e 2500w" />

Fill in the `name` and `command` fields. The `name` field must be a unique name for the server. The `command` field is the command to run the server. Environment variables have their own section and no longer need to be specified in the command.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=20d9ffa2c683194ec1d66afe390f6f9d" className="rounded-xl" data-og-width="1090" width="1090" data-og-height="586" height="586" data-path="images/mcp-env.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e9c87679180a6db78e05d7cce22845ff 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e7e5805c874eb5e006c27ee3f52360fa 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=8930b7ececcdd06705dcc9d9ed86ef12 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=8e9b4f557196621ab4d45dd52defbda7 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bd0ff7868ab46ea8325a6b9ed1856294 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4cba9d7e59969d4a48aa630ab14932a7 2500w" />

To add additional servers, click the `+` button next to the `MCP` header.
To edit a configuration or to delete a server, click the `...` button next to the server name.

### Add a Remote MCP server

If your MCP server runs remotely (for example, a hosted service), click the "+ Add remote MCP" button in the MCP section. Remote MCP connections support both HTTP and SSE (Server‑Sent Events).

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=21086d1c640c6e20975aa7207532be78" className="rounded-xl" data-og-width="1036" width="1036" data-og-height="676" height="676" data-path="images/settings-panel-mcp-remote.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3ac00d4975d2791c378a0e24b7fd1457 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4d92460a09146279b73693c6af5be240 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=2a9dfd961063e277d0dee794b71b0b47 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=cdbad5fac2856fe1fb9bc272cb22622d 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=d99df8defa992c69589501c7db0e0204 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=7f5c7e96f585a368523586154bfd696e 2500w" />

* Connection Type: choose HTTP or SSE
* Name: a unique display name for the server
* URL: the base URL to your MCP server (e.g., [https://api.example.com](https://api.example.com))

Remote MCP servers appear alongside your local MCP servers in the list. You can edit or remove them using the "..." menu next to the server name.

## Server compatibility

Not all MCP servers are compatible with Augment's models. The MCP standard, implementation of specific servers, and Augment's MCP support are frequently being updated, so check compatibility frequently.


# Index your workspace
Source: https://docs.augmentcode.com/jetbrains/setup-augment/workspace-indexing

When your workspace is indexed, Augment can provide tailored code suggestions and answers based on your unique codebase, best practices, coding patterns, and preferences. You can always control what files are indexed.

## About indexing your workspace

When you open a workspace with Augment enabled, your codebase will be automatically uploaded to Augment's secure cloud. You can control what files get indexed using `.gitignore` and `.augmentignore` files. Indexing usually takes less than a minute but can take longer depending on the size of your codebase.

## Security and privacy

Augment stores your code securely and privately to enable our powerful context engine. We ensure code privacy through a proof-of-possession API and maintain strict internal data minimization principles. [Read more about our security](https://www.augmentcode.com/security).

## What gets indexed

Augment will index all the files in your workspace, except for the files that match patterns in your `.gitignore` file and the `.augmentignore` file.

## Ignoring files with .augmentignore

The `.augmentignore` file is a list of file patterns that Augment will ignore when indexing your workspace. Create an `.augmentignore` file in the root of your workspace. You can use any glob pattern that is supported by the [gitignore](https://git-scm.com/docs/gitignore) file.

## Including files that are .gitignored

If you have a file or directory in your `.gitignore` that you want to indexed, you can add it to your `.augmentignore` file using the `!` prefix.

For example, you may want your `node_modules` indexed to provide Augment with context about the dependencies in their project, but it is typically included in their `.gitignore`. Add `!node_modules` to your `.augmentignore` file.

<CodeGroup>
  ```bash .augmentignore theme={null}
  # Include .gitignore excluded files with ! prefix
  !node_modules

  # Exclude other files with .gitignore syntax
  data/test.json
  ```

  ```bash .gitignore theme={null}
  # Exclude dependencies
  node_modules

  # Exclude secrets
  .env

  # Exclude build artifacts
  out
  build
  ```
</CodeGroup>


# Using Agent
Source: https://docs.augmentcode.com/jetbrains/using-augment/agent

Use Agent to complete simple and complex tasks across your workflow–implementing a feature, upgrade a dependency, or writing a pull request.

export const type_0 = "changes"

export const AtIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M480.39-96q-79.52 0-149.45-30Q261-156 208.5-208.5T126-330.96q-30-69.96-30-149.5t30-149.04q30-69.5 82.5-122T330.96-834q69.96-30 149.5-30t149.04 30q69.5 30 122 82.5t82.5 122Q864-560 864-480v60q0 54.85-38.5 93.42Q787-288 732-288q-34 0-62.5-17t-48.66-45Q593-321 556.5-304.5T480-288q-79.68 0-135.84-56.23-56.16-56.22-56.16-136Q288-560 344.23-616q56.22-56 136-56Q560-672 616-615.84q56 56.16 56 135.84v60q0 25.16 17.5 42.58Q707-360 732-360t42.5-17.42Q792-394.84 792-420v-60q0-130-91-221t-221-91q-130 0-221 91t-91 221q0 130 91 221t221 91h192v72H480.39ZM480-360q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35Z" />
    </svg>
  </div>;

## About Agent

Augment Agent is a powerful tool that can help you complete software development tasks end-to-end. From quick edits to complete feature implementation, Agent breaks down your requests into a functional plan and implements each step all while keeping you informed about what actions and changes are happening. Powered by Augment's Context Engine and powerful LLM architecture, Agent can write, document, and test like an experienced member of your team.

## Accessing Agent

To access Agent, simply open the Augment panel and select one of the Agent modes from the drop down in the input box.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector-jetbrains.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a67bcc5b41dca6b0a5e7d2f7eec8a2fa" alt="Augment Agent" className="rounded-xl" data-og-width="1265" width="1265" data-og-height="351" height="351" data-path="images/agent-selector-jetbrains.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector-jetbrains.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=292af64bd0d9f280f47d9465f5f14ef4 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector-jetbrains.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=887394c5adf11d8d4d7a3100a995e063 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector-jetbrains.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c4d1ccb48dd19a760f91f68a9e231983 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector-jetbrains.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e471a11b94b43e141ebe207eea5e6ee7 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector-jetbrains.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=21afcead2edeb31b785143cedd7e5103 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector-jetbrains.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ba4dc039488f3c0a3a5ff299bd5694c2 2500w" />

### Choosing a model

Use the model dropdown in the Augment panel to switch between Claude Sonnet 4 and GPT-5. Your selection applies only to Agent for the current workspace and can be changed at any time. See [Available Models](/models/available-models) for details.

## Using Agent

To use Agent, simply type your request into the input box using natural language and click the submit button. You will see the default context including current workspace, current file, and Agent memories. You can add additional context by clicking <AtIcon />and selecting files or folder, or add an image as context by clicking the paperclip. Agent can create, edit, or delete code across your workspace and can use tools like the terminal and external integrations through MCP to complete your request.

### Enhancing your prompt

You can improve the quality of your {type_0} by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

### Reviewing changes

You can review every change Agent makes by clicking on the action to expand the view. Review diffs for file changes, see complete terminal commands and output, and the results of external integration calls.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-expand-jetbrains.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b31d72511c15bceaa95ed2d6b42f6815" alt="Augment Agent" className="rounded-xl" data-og-width="1190" width="1190" data-og-height="509" height="509" data-path="images/agent-expand-jetbrains.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-expand-jetbrains.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=dd2b11f0aa9bf02ab9fcf035a4441ab6 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-expand-jetbrains.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=aa75a6cb63c3267ed0a04319446357f9 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-expand-jetbrains.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=04cfcd4d342d2c0bfac71759885abfe6 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-expand-jetbrains.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3e96ead41fad793ed9b0478ab3e1f8dc 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-expand-jetbrains.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7ef49f9de42a74672159a886d6eb34b3 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-expand-jetbrains.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=344f87684aa38da595509b25a5139f24 2500w" />

### Checkpoints

Checkpoints are automatically saved snapshots of your workspace as Agent implements the plan allowing you to easily revert back to a previous step. This enables Agent to continue working while you review code changes and commands results. To revert to a previous checkpoint, click the reverse arrow to restore your code.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint-jetbrains.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f3eb8fca517586641c2ca2c14137ca7a" alt="Augment Agent" className="rounded-xl" data-og-width="1215" width="1215" data-og-height="469" height="469" data-path="images/agent-checkpoint-jetbrains.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint-jetbrains.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cd56de4ade08a75e4049815b63d4cead 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint-jetbrains.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=0e659f42bec828809463c1b6f24747b8 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint-jetbrains.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=672150d22ae7f3aa79f577734347e79d 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint-jetbrains.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e5d3cea0c09c9b467a2be00a71247b7d 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint-jetbrains.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=084c617ca235cc0cc0da70e113cb5495 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint-jetbrains.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=36aa8bbceaba92de053998e158696428 2500w" />

### Agent vs Agent Auto

By default, Agent will pause work when it needs to execute a terminal command or access external integrations. After reviewing the suggested action, click the blue play button to have Agent execute the command and continue working. You tell Agent to skip a specific action by clicking on the three dots and then Skip.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5c528efde3b96da6711dcecdda312294" alt="Augment Agent" className="rounded-xl" data-og-width="1212" width="1212" data-og-height="373" height="373" data-path="images/agent-approval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6c5d2c65451676c4ab78e6835ec64451 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=74f3b29a19c5d3dedb4d9cf7cd4c15e8 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7099350faa1efcc52f0d17534e747438 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ec6fe85dcb06538d1b4b2817e95c977c 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e2d66bbcf048da6d3783c5b247164002 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=68093b6342af74a4aa90d521b1cd2a3a 2500w" />

In Agent Auto, Agent will act more independently. It will edit files, execute terminal commands, and access tools like MCP servers automatically.

### Stop or guide the Agent

You can interrupt the Agent at any time by clicking Stop. This will pause the action to allow you to correct something you see the agent doing incorrectly. While Agent is working, you can also prompt the Agent to try a different approach which will automatically stop the agent and prompt it to correct its course.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3c195714aa08f74acb9d63a354acdc99" alt="Stopping the agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="551" height="551" data-path="images/agent-stop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ee1b6bd049826fbd882ce234e91b8d76 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=0bb16c7d3efaf8e03e971c6ee7b8a470 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cd99b327ca87dd7e5df6671dab20594e 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4ab045596b20e4d325ba655179e98338 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ea995fe1122a55d05ea67bd99b4b51d5 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=280d36fadf5a41fa8d777be4ac1e4a96 2500w" />

### Quick Ask Mode

Quick Ask Mode is a toggle button in the agent chat interface that restricts the AI to read-only tools only. When activated, it adds a visual badge to the message and focuses the AI on information gathering without making any changes to your codebase.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/ask-mode.gif?s=c2c554fd010bb15d8267de15ad4f9dc5" alt="Quick Ask Mode toggle and usage" className="rounded-xl" data-og-width="800" width="800" data-og-height="450" height="450" data-path="images/ask-mode.gif" data-optimize="true" data-opv="3" />

### Comparison to Chat

Agent takes Chat to the next level by allowing Augment to do things for you-that is create and make modifications directly to your codebase. Chat can explain code, create plans, and suggest changes which you can smartly apply one-by-one, but Agent takes it a step further by automatically implementing the entire plan and all code changes for you.

| What are you trying to do?                       | Chat | Agent |
| :----------------------------------------------- | :--: | :---: |
| Ask questions about your code                    |  ☑️  |   ✅   |
| Get advice on how to refactor code               |  ☑️  |   ✅   |
| Add new features to selected lines of code       |  ☑️  |   ✅   |
| Add new feature spanning multiple files          |      |   ✅   |
| Document new features                            |      |   ✅   |
| Queue up tests for you in the terminal           |      |   ✅   |
| Open Linear tickets or start a pull request      |      |   ✅   |
| Start a new branch in GitHub from recent commits |      |   ✅   |
| Automatically perform tasks on your behalf       |      |   ✅   |

### Use cases

Use Agent to handle various aspects of your software development workflow, from simple configuration changes to complex feature implementations. Agent supports your daily engineering tasks like:

* **Make quick edits** - Create a pull request to adjust configuration values like feature flags from FALSE to TRUE
* **Perform refactoring** - Move functions between files while maintaining coding conventions and ensuring bug-free operation
* **Start a first draft for new features** - Start a pull request (PR) with implementing entirely new functionality straight from a GitHub Issue or Linear Ticket
* **Branch from GitHub** - Open a PR from GitHub based on recent commits that creates a new branch
* **Query Supabase tables directly** - Ask Agent to view the contents of a table
* **Start tickets in Linear or Jira** - Open tickets and ask Agent to suggest a plan to address the ticket
* **Add Pull Request descriptions** - Merge your PR into a branch then tell the agent to explain what the changes are and why they were made
* **Create test coverage** - Generate unit tests for your newly developed features
* **Generate documentation** - Produce comprehensive documentation for your libraries and features
* **Start a README** - Write a README for a new feature or updated function that you just wrote
* **Track development progress** - Review and summarize your recent Git commits for better visibility with the GitHub integration

## Next steps

* [Configure Agent Integrations](/jetbrains/setup-augment/agent-integrations)


# Using Chat
Source: https://docs.augmentcode.com/jetbrains/using-augment/chat

Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

export const type_0 = "chats"

export const DeleteIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm400-600H280v520h400v-520ZM360-280h80v-360h-80v360Zm160 0h80v-360h-80v360ZM280-720v520-520Z" />
    </svg>
  </div>;

export const ChevronRightIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z" />
    </svg>
  </div>;

export const NewChatIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M120-160v-600q0-33 23.5-56.5T200-840h480q33 0 56.5 23.5T760-760v203q-10-2-20-2.5t-20-.5q-10 0-20 .5t-20 2.5v-203H200v400h283q-2 10-2.5 20t-.5 20q0 10 .5 20t2.5 20H240L120-160Zm160-440h320v-80H280v80Zm0 160h200v-80H280v80Zm400 280v-120H560v-80h120v-120h80v120h120v80H760v120h-80ZM200-360v-400 400Z" />
    </svg>
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Chat

Chat is a new way to work with your codebase using natural language. Chat will automatically use the current workspace as context and you can [provide focus](/using-augment/chat-context) for Augment by selecting specific code blocks, files, folders, or external documentation. Details from your current chat, including the additional context, are used to provide more relevant code suggestions as well.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d375d6ded40f6ed3353e002a9d9fa7a0" alt="Augment Chat" className="rounded-xl" data-og-width="1120" width="1120" data-og-height="1209" height="1209" data-path="images/chat-explain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=72a74689a8d1160c2ec3831e752cb266 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=559d3b76f96a2df576305440cf5c241e 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=48570a3aa134abe6d23ec6c8cfa5e314 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d175cf3cfaa04e1e9de9d2894d91ecc3 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7cfebd57e867659d7e847fbd25d3b207 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a197d0a8fe4e010828796d78d172d43e 2500w" />

## Accessing Chat

Access the Chat sidebar by clicking the Augment icon <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5a70e197b4ab16c79e9612aac74015cf" className="inline h-4 p-0 m-0" data-og-width="676" width="676" data-og-height="592" height="592" data-path="images/augment-icon-chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2a32c9463cef1c6647f0dd08dd827cd2 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4cba744eb472e888403e462429f3c10a 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c8393d6a3463c6e6a99eca871d66ae67 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=573abbe9afb002028f79741b4fa4bad4 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=998af121c45992d4121b3fb97ee42007 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=aa776a96f49e4d86cb0a0d7cef78cc67 2500w" /> in the sidebar or the status bar. You can also open Chat by using one of the keyboard shortcuts below.

**Keyboard Shortcuts**

| Platform      | Shortcut                       |
| :------------ | :----------------------------- |
| MacOS         | <Keyboard shortcut="Cmd L" />  |
| Windows/Linux | <Keyboard shortcut="Ctrl L" /> |

## Using Chat

To use Chat, simply type your question or command into the input field at the bottom of the Chat panel. You will see the currently included context which includes the workspace and current file by default. Use Chat to explain your code, investigate a bug, or use a new library. See [Example Prompts for Chat](/using-augment/chat-prompts) for more ideas on using Chat.

### Enhancing your prompt

You can improve the quality of your {type_0} by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

### Conversations about code

To get the best possible results, you can go beyond asking simple questions or commands, and instead have a back and forth conversation with Chat about your code. For example, you can ask Chat to explain a specific function and then ask follow-up questions about possible refactoring options. Chat can act as a pair programmer, helping you work through a technical problem or understand unfamiliar code.

### Starting a new chat

You should start a new Chat when you want to change the topic of the conversation since the current conversation is used as part of the context for your next question. To start a new chat, open the Augment panel and click the new chat icon <NewChatIcon /> at the top-right of the Chat panel.

### Previous chats

You can continue a chat by clicking the chevron icon<ChevronRightIcon />at the top-left of the Chat panel. Your previous chats will be listed in reverse chronological order, and you can continue your conversation where you left off.

### Deleting a chat

You can delete a previous chat by clicking the chevron icon<ChevronRightIcon />at the top-left of the Chat panel to show the list of previous chats. Click the delete icon <DeleteIcon /> next to the chat you want to delete. You will be asked to confirm that you want to delete the chat.


# Using Actions in Chat
Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-actions

Actions let you take common actions on code blocks without leaving Chat. Explain, improve, or find everything you need to know about your codebase.

export const ArrowUpIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M444-192v-438L243-429l-51-51 288-288 288 288-51 51-201-201v438h-72Z" />
    </svg>
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=db5e93308abefb7782a8684ad79e2a50" alt="Augment Chat Actions" className="rounded-xl" data-og-width="1233" width="1233" data-og-height="630" height="630" data-path="images/chat-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=24ffba8783720d584f76090090aff0fe 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=63f4c3aa42421df5ae79d40be85abfa8 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c9bfcc586feef6caa23ea46efa8fd1aa 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4fa3cd4a775a3865f92d954c842706cc 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ecc12c1fedeee7734b9e3a1bef2b434c 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7e28137d1682a5b7c5d6376870b92a59 2500w" />

## Using actions in Chat

To use a quick action, you an use a <Keyboard shortcut="/" /> command or click the up arrow icon<ArrowUpIcon />to show the available actions. For explain, fix, and test actions, first highlight the code in the editor and then use the command.

| Action                           | Usage                                                                    |
| :------------------------------- | :----------------------------------------------------------------------- |
| <Keyboard shortcut="/find" />    | Use natural language to find code or functionality                       |
| <Keyboard shortcut="/explain" /> | Augment will explain the hightlighted code                               |
| <Keyboard shortcut="/fix" />     | Augment will suggest improvements or find errors in the highlighted code |
| <Keyboard shortcut="/test" />    | Augment will suggest tests for the highlighted code                      |

Augment will typically include code blocks in the response to the action. See [Applying code blocks from Chat](/using-augment/chat-apply) for more details.


# Applying code blocks from Chat
Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-apply

Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

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

export const MoreVertIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M479.79-192Q450-192 429-213.21t-21-51Q408-294 429.21-315t51-21Q510-336 531-314.79t21 51Q552-234 530.79-213t-51 21Zm0-216Q450-408 429-429.21t-21-51Q408-510 429.21-531t51-21Q510-552 531-530.79t21 51Q552-450 530.79-429t-51 21Zm0-216Q450-624 429-645.21t-21-51Q408-726 429.21-747t51-21Q510-768 531-746.79t21 51Q552-666 530.79-645t-51 21Z" />
    </svg>
  </div>;

export const CheckIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M389-267 195-460l51-52 143 143 325-324 51 51-376 375Z" />
    </svg>
  </div>;

export const FileNewIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h360v80H200v560h560v-360h80v360q0 33-23.5 56.5T760-120H200Zm120-160v-80h320v80H320Zm0-120v-80h320v80H320Zm0-120v-80h320v80H320Zm360-80v-80h-80v-80h80v-80h80v80h80v80h-80v80h-80Z" />
    </svg>
  </div>;

export const FileCopyIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M760-200H320q-33 0-56.5-23.5T240-280v-560q0-33 23.5-56.5T320-920h280l240 240v400q0 33-23.5 
      56.5T760-200ZM560-640v-200H320v560h440v-360H560ZM160-40q-33 0-56.5-23.5T80-120v-560h80v560h440v80H
      160Zm160-800v200-200 560-560Z" />
    </svg>
  </div>;

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b461dba46612cb6cc46db000bebb7566" alt="Augment Chat Apply" className="rounded-xl" data-og-width="1291" width="1291" data-og-height="375" height="375" data-path="images/chat-apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=dd3f5cea028042ba31b68a12f009acbc 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a1aca8f5dbff77303d4568677444eafa 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b4d3137bba658cecc13434bf193ea9a7 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=011d9dfafca386660985500a6d4c7ab6 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d9cc3f973615bbc1727876d11e0f4c7e 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2e3a50fd918339cb519553c06bc5a242 2500w" />

## Using code blocks from within Chat

Whenever Chat responds with code, you will have the option to add the code to your codebase. The most common option will be shown as a button and you can access the other options by clicking the overflow menu icon<MoreVertIcon />at the top-right of the code block. You can use the following options to apply the code:

* <FileCopyIcon />**Copy**
  the code from the block to your clipboard
* <FileNewIcon />**Create**
  a new file with the code from the block
* <CheckIcon />**Apply**
  the code from the block intelligently to your file


# Focusing Context in Chat
Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-context

You can specify context from files, folders, and external documentation in your conversation to focus your chat responses.

export const AtIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M480.39-96q-79.52 0-149.45-30Q261-156 208.5-208.5T126-330.96q-30-69.96-30-149.5t30-149.04q30-69.5 82.5-122T330.96-834q69.96-30 149.5-30t149.04 30q69.5 30 122 82.5t82.5 122Q864-560 864-480v60q0 54.85-38.5 93.42Q787-288 732-288q-34 0-62.5-17t-48.66-45Q593-321 556.5-304.5T480-288q-79.68 0-135.84-56.23-56.16-56.22-56.16-136Q288-560 344.23-616q56.22-56 136-56Q560-672 616-615.84q56 56.16 56 135.84v60q0 25.16 17.5 42.58Q707-360 732-360t42.5-17.42Q792-394.84 792-420v-60q0-130-91-221t-221-91q-130 0-221 91t-91 221q0 130 91 221t221 91h192v72H480.39ZM480-360q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35Z" />
    </svg>
  </div>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Chat Context

Augment intelligently includes context from your entire workspace based on the ongoing conversation–even if you don't have the relevant files open in your editor–but sometimes you want Augment to prioritize specific details for more relevant responses.

<video src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-context.mp4?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cbdd137e0c8b3c0048cfab708bbb56eb" loop muted controls className="rounded-xl" data-path="images/chat-context.mp4" />

### Focusing context for your conversation

You can specify context by clicking the <AtIcon /> icon at the top-left of the Chat panel or by <Command text="@-mentioning" /> in the input field. You can use fuzzy search to filter the list of context options quickly. There are a number of different types of additional context you can add to your conversation:

1. Highlighted code blocks
2. Specific files or folders within your workspace
3. 3rd party documentation, like Next.js documentation

#### Mentioning files and folders

Include specific files or folders in your context by typing `@` followed by the file or folder name. For example, `@routes.tsx` will include the `routes.tsx` file in your context. You can include multiple files or folders.

#### Mentioning 3rd party documentation

You can also mention 3rd party documentation in your context by typing `@` followed by the name of the documentation. For example, `@Next.js` will include Next.js documentation in your context. Augment provides nearly 300 documentation sets spanning across a wide range of domains such as programming languages, packages, software tools, and frameworks.


# Example Prompts for Chat
Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-prompts

Using natural language to interact with your codebase unlocks a whole new way of working. Learn how to get the most out of Chat with the following example prompts.

export const type_0 = "chats"

## About chatting with your codebase

Augment's Chat has deep understanding about your codebase, dependencies, and best practices. You can use Chat to ask questions about your code, but it also can help you with general software engineering questions, think through technical decisions, explore new libraries, and more.

## Enhancing your prompt

You can improve the quality of your {type_0} by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

## Example Prompts

### Explain code

* Explain this codebase to me
* How do I use the Twilio API to send a text message?
* Explain how generics work in TypeScript and give me a simple example

### Finding code

* Where are all the useEffect hooks that depend on the 'currentUser' variable?
* Find the decorators that implement retry logic across our microservices
* Find coroutines that handle database transactions without a timeout parameter

### Generate code

* Write a function to check if a string is a valid email address
* Generate a middleware function that rate-limits API requests using a sliding window algorithm
* Create a SQL query to find the top 5 customers who spent the most money last month

### Write tests

* Write integration tests for this API endpoint
* What edge cases have I not included in this test?
* Generate mock data for testing this customer order processing function

### Refactor and improve code

* This function is running slowly with large collections - how can I optimize it?
* Refactor this callback-based code to use async/await instead
* Rewrite this function in Rust

### Find and fix errors

* This endpoint sometimes returns a 500 error. Here's the error log - what's wrong?
* I'm getting 'TypeError: Cannot read property 'length' of undefined' in this component.
* Getting CORS errors when my frontend tries to fetch from the API


# Completions
Source: https://docs.augmentcode.com/jetbrains/using-augment/completions

Use code completions to get more done. Augment's radical context awareness means more relevant suggestions, fewer hallucinations, and less time hunting down documentation.

export const MoreVertIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M479.79-192Q450-192 429-213.21t-21-51Q408-294 429.21-315t51-21Q510-336 531-314.79t21 51Q552-234 530.79-213t-51 21Zm0-216Q450-408 429-429.21t-21-51Q408-510 429.21-531t51-21Q510-552 531-530.79t21 51Q552-450 530.79-429t-51 21Zm0-216Q450-624 429-645.21t-21-51Q408-726 429.21-747t51-21Q510-768 531-746.79t21 51Q552-666 530.79-645t-51 21Z" />
    </svg>
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Code Completions

Augment's Code Completions integrates with your IDE's native completions system to give you autocomplete-like suggestions as you type. You can accept all of a suggestion, accept partial suggestions a word or a line at a time, or just keep typing to ignore the suggestion.

## Using Code Completions

To use code completions, simply start typing in your IDE. Augment will provide suggestions based on the context of your code. You can accept a suggestion by pressing <Keyboard shortcut="Tab" />, or ignore it by continuing to type.

For example, add the following function to a TypeScript file:

```typescript  theme={null}
function getUser(): Promise<User>;
```

As you type `getUser`, Augment will suggest the function signature. Press <Keyboard shortcut="Tab" /> to accept the suggestion. Augment will continue to offer suggestions until the function is complete, at which point you will have a function similar to:

```typescript  theme={null}
function getUser(): Promise<User> {
  return fetch("/api/user/1")
    .then((response) => response.json())
    .then((json) => {
      return json as User;
    });
}
```

### Accepting Completions

<Tabs>
  <Tab title="MacOS">
    <Tip>
      We recommend configuring a custom keybinding to accept a word or line, see
      [Keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts) for more
      details.
    </Tip>

    | Action                         | Default keyboard shortcut                       |
    | :----------------------------- | :---------------------------------------------- |
    | Accept inline suggestion       | <Keyboard shortcut="Tab" />                     |
    | Accept next word of suggestion | <Keyboard shortcut="Cmd →" />                   |
    | Accept next line of suggestion | None (see above)                                |
    | Reject suggestion              | <Keyboard shortcut="Esc" />                     |
    | Ignore suggestion              | Continue typing through the suggestion          |
    | Toggle automatic completions   | VSCode: <Keyboard shortcut="Cmd Option A" />    |
    |                                | JetBrains: <Keyboard shortcut="Cmd Option 9" /> |
  </Tab>

  <Tab title="Windows/Linux">
    <Tip>
      We recommend configuring a custom keybinding to accept a word or line, see
      [Keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts) for more
      details.
    </Tip>

    | Action                         | Default keyboard shortcut                     |
    | :----------------------------- | :-------------------------------------------- |
    | Accept inline suggestion       | <Keyboard shortcut="Tab" />                   |
    | Accept next word of suggestion | <Keyboard shortcut="Ctrl →" />                |
    | Accept next line of suggestion | None (see above)                              |
    | Reject suggestion              | <Keyboard shortcut="Esc" />                   |
    | Ignore suggestion              | Continue typing through the suggestion        |
    | Toggle automatic completions   | VSCode: <Keyboard shortcut="Ctrl Alt A" />    |
    |                                | JetBrains: <Keyboard shortcut="Ctrl Alt 9" /> |
  </Tab>
</Tabs>

### Disabling Completions

<Tabs>
  <Tab title="Visual Studio Code">
    You can disable automatic code completions by clicking the overflow menu icon<MoreVertIcon />at the top-right of the Augment panel, then selecting <Command text="Turn Automatic Completions Off" />.
  </Tab>

  <Tab title="JetBrains IDEs">
    You can disable automatic code completions by clicking the Augment icon <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7564ed27ae27d8e8e8d37fc0c5390710" className="inline h-3 p-0 m-0" data-og-width="18" width="18" data-og-height="12" height="12" data-path="images/augment-icon-smile.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e768e602ba7fbca6dee54bd80707a65f 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2bff5c6e247ef06ee8c8aaf10b729fdb 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f137c3896e95e4ae83d7374bde6fce21 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=30c491bbedc2350eeac401d6bdb88a1d 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2b87100b107e7236c3c415c046fd988b 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a39dac81c0ae990b2c8143421f4144c5 2500w" /> in the status bar at the bottom right corner of your IDE, then selecting <Command text="Disable Completions" />.
  </Tab>
</Tabs>

### Enable Completions

<Tabs>
  <Tab title="Visual Studio Code">
    If you've temporarily disabled completions, you can re-enable them by clicking the overflow menu icon<MoreVertIcon />at the top-right of the Augment panel, then selecting <Command text="Turn Automatic Completions On" />.
  </Tab>

  <Tab title="JetBrains IDEs">
    If you've temporarily disabled completions, you can re-enable them by clicking the Augment icon <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7564ed27ae27d8e8e8d37fc0c5390710" className="inline h-3 p-0 m-0" data-og-width="18" width="18" data-og-height="12" height="12" data-path="images/augment-icon-smile.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e768e602ba7fbca6dee54bd80707a65f 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2bff5c6e247ef06ee8c8aaf10b729fdb 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f137c3896e95e4ae83d7374bde6fce21 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=30c491bbedc2350eeac401d6bdb88a1d 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2b87100b107e7236c3c415c046fd988b 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a39dac81c0ae990b2c8143421f4144c5 2500w" /> in the status bar at the bottom right corner of your IDE, then selecting <Command text="Enable Completions" />.
  </Tab>
</Tabs>


# Using Tasklist
Source: https://docs.augmentcode.com/jetbrains/using-augment/tasklist

Use Tasklist to break down complex problems into manageable steps, track progress, and collaborate with Agent on multi-step tasks.

## What is the Tasklist?

Augment's Tasklist helps the Agent create and refine a step-by-step plan for you to review. The Tasklist provides a structured interface for collaboration between you and the Agent, allowing you to break down complex problems into manageable, sequential steps.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=7b57f10306d17d7a01769a36f1f08888" alt="Tasklist Overview" className="rounded-xl" data-og-width="473" width="473" data-og-height="208" height="208" data-path="images/tasklist-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=cfe6643999d0f51858bdc307a405e706 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=707d717d48b17655f8de15a57e17efb2 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=28a71d28a31963133145d84dd4c6dc6e 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=2d8afe47cdba513cacd3b1510212c099 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=fb50e40cef51f5c43b392b283ac52626 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=2b21a1b7e583664dc6eac0559d0129ac 2500w" />

## Why Tasklist?

Tasklist improves agent effectiveness on long or complex tasks by:

* **Maintaining context** across different conversations by moving your Tasklist to a new chat
* **Breaking down complex problems** into manageable, sequential steps
* **Gathering progress** across threads
* **Exploring alternative solutions** to completed tasks if you need to pivot
* **Streamlining your approach** to nebulous problems by deleting irrelevant steps once the path forward is clear

Tasklist provides a structured interface for collaboration and opens up possibilities for agent-to-agent collaboration. We hypothesize that an interface such as Tasklist could be a preferred way to interact with coding agents in the future.

## Tasklist in Action

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-demo.gif?s=c230baeaa51a97a59401b85417a71686" alt="Tasklist demonstration" className="rounded-xl" data-og-width="800" width="800" data-og-height="542" height="542" data-path="images/tasklist-demo.gif" data-optimize="true" data-opv="3" />

## Creating a New Task

### Automatic Creation

The Agent will usually create a Tasklist when it encounters a complex, multi-step problem. You can also ask the Agent to make a Tasklist for you by simply prompting "Start a Tasklist to..." then add the problem you are trying to tackle.

### Manual Creation

You can also manually create a Tasklist:

1. Switch to Tasklist using the checklist button next to Changes
2. Click the plus to add your first task
3. Alternatively, you can create a new task by typing in the gray prompt box at the bottom of the extension. Click **Add Task** from the dropdown arrow next to Send

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a2603f672d47c74e7582cb6da58cad04" alt="Creating a new task" className="rounded-xl" data-og-width="473" width="473" data-og-height="85" height="85" data-path="images/tasklist-create-task.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=273857c88137440b4ce932962d5842d8 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b53633da83f18abacd816c4a4fbb2fe2 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=03e5417ccbd446b8ee6b10fc6b00f2f4 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=2e13079c3e2eabfdde93bb4ed73c3a87 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=34bf7e951951489686422f7cc5ea3b3d 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=bc3db1e1b3dd7c092b91dcdbd38a2561 2500w" />

## Running Tasks

To run a task, click the grey triangle (play button) next to the task. The Agent will begin executing the task and update its status as it progresses.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=58d05e0c445e9b4fb449c6ade5a298bd" alt="Running a task" className="rounded-xl" data-og-width="824" width="824" data-og-height="778" height="778" data-path="images/tasklist-run-task.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4819f31c0860ebcc5827693ea0c0baad 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=27aa131b8c5fd591162d6fccfe35ec50 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=8b90fc209a811b5f2f59f9747edce1df 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=c05369faa15a20ad17622d875ac2f601 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=6c3c3c9250484b0982d023bbd1400693 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3de97385af039261f008cfb0e801116d 2500w" />

## Task Status Indicators

Task statuses are indicated by different colors and icons:

* **Empty circle** - Task has not yet started
* **Blue half circle** - Task is currently in progress
* **Green checkbox** - Task has been completed and is ready for review

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=989d263506a6346c0033d5fe0ea51475" alt="Task status indicators" className="rounded-xl" data-og-width="473" width="473" data-og-height="214" height="214" data-path="images/tasklist-status-indicators.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=cd926a7cbeb7ec67d4bb51cead1485c6 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=6b2651040fdbad62384eee3cfdbfe716 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=856571460250f49bcabd817161b0f270 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=24e4ac9d6f6290731463213cfad02657 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a1148d6927825479fc4e92dd5da17469 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=92da7588be36eeb5b471593b51dcc1c0 2500w" />

## Subtasks

Augment Code automatically generates subtasks when needed. The Agent will automatically add and nest required subtasks under your initial tasks. You can edit and expand these subtasks just like any other task in the list. Likewise, you can remove subtasks you deem unnecessary.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=06a66a68939509b93969d6ee352363a7" alt="Subtasks example" className="rounded-xl" data-og-width="233" width="233" data-og-height="32" height="32" data-path="images/tasklist-subtasks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=64ab84c553e9c00a188211b706e2fac0 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=754a79480312c19f6d2cdfb6f0da568a 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ed5c411199b3c1c08d194dca0996ba7a 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=c85b03a98902b4200034ffbe772f86aa 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a66ffd3ef9f68064fa3d215b59b8e444 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=f40745bd17de1648e51d5304d312b67b 2500w" />

## Managing Running Tasks

### Stopping a Task

You can treat any in-progress task like any prompt you might send the Agent. To stop what the Agent is doing and offer a corrective action, click the red square (stop button) and tell the Agent what you want it to do instead.

### Running All Tasks

The Agent can complete all the tasks sequentially by clicking the triangle (play button) at the top of the Tasklist.

## Reviewing Changes

You can review the changes made by the Agent after a task is completed by toggling between the Tasks and Changes view to see the diffs (differences) of the work done by the agent for each task.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=35ce060276c5dc8fec9f1f9b473c9599" alt="Reviewing changes in Tasks and Changes view" className="rounded-xl" data-og-width="818" width="818" data-og-height="364" height="364" data-path="images/tasklist-changes-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=7c4571f3c0ead8a670ca3aa604176d0c 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4479c4f468883c3a59feed2560c9a81c 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a649dcd4a9164c2eeb3d5928ba4b5e40 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e85d1a4989fd58ab60e561f1a38fb8d3 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b563421017b53c86cb7704e7f5369ab2 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=364274422e2215186f8b207441307ec9 2500w" />

## Integration with Task Management Tools

### Jira and Linear Integration

The Tasklist is a perfect pairing with existing task management tools like Jira or Linear:

* Ask the Agent to create a Tasklist based on tickets inside Jira or Linear
* Further break down complex tickets into manageable steps
* Once your Tasklist is completed, you can ask the Agent to resolve the issue inside Jira or Linear and append the steps taken as a comment

### Standalone Usage

Don't use an issue tracker? No problem - use Tasklist to track issues you need to tackle across Threads.

## Best Practices

* **Be specific** when creating tasks to help the Agent understand exactly what needs to be done
* **Review and edit** the automatically generated subtasks to ensure they align with your goals
* **Use the stop function** to provide course corrections when the Agent is heading in the wrong direction
* **Leverage the Changes view** to review all modifications made during task execution
* **Move Tasklists** between conversations to maintain context across different chat sessions

## Next Steps

* [Learn more about Agent](/jetbrains/using-augment/agent)
* [Configure Agent Integrations](/jetbrains/setup-augment/agent-integrations)


# Available Models
Source: https://docs.augmentcode.com/models/available-models

The LLMs currently available in Augment and how we use them.

## Current models

Augment uses world-class large language models together with our Context Engine. We currently support the following models:

* Claude Haiku 4.5 by Anthropic
* Claude Sonnet 4 by Anthropic
* Claude Sonnet 4.5 by Anthropic
* GPT-5 by OpenAI

## Choosing a model

You can select the model directly using the Model Picker in the Augment.

* In VS Code and JetBrains, open the Augment panel and use the model dropdown near the input box to switch models.
* In Auggie CLI, use the `/model` slash command or pass the `--model` flag with the desired model.
* Your selection applies only to Agent in that workspace and can be changed at any time.

If you don't pick a model, Augment will use your last selection or the default set by your organization.

## Feature compatibility

Both models support the core Augment Agent features:

* Deep code understanding with Augment's Context Engine
* Tool use (integrations and MCP), file edits, and multi-step planning

Some behaviors (e.g., wording or style) may vary slightly between models. We'll continue to refine prompts and guardrails to provide a consistent developer experience.

## Notes and transparency

* We may roll out model updates gradually. If you're part of a staged rollout, different workspaces or teammates may see updates at different times.
* For troubleshooting, you can share the request ID with our support team; they can confirm which model handled a specific request.

If you have questions about model availability or want to participate in early access programs, please reach out via Support.


# Quickstart
Source: https://docs.augmentcode.com/quickstart

Augment is the developer AI for teams that deeply understands your codebase and how you build software. Your code, your dependencies, and your best practices are all at your fingertips.

export const Next = ({children}) => <div className="border-t border-b pb-8 border-gray dark:border-white/10">
    <h3>Next steps</h3>
    {children}
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

### 1. Install the Augment extension

<CardGroup cols={3}>
  <Card href="https://marketplace.visualstudio.com/items?itemName=augment.vscode-augment">
    <img className="w-12 h-12" src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1743e6c5d410f0c71016833690fa837e" alt="Visual Studio Code" data-og-width="64" width="64" data-og-height="64" height="64" data-path="images/vscode-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=6cc12e25432edf2e06f49d14373ac02d 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ed9401ed757b8de4c9d22f5293519da2 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ae9c1a6c3d5a2c7ac3a8530141d306d6 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b1a41a3a74fa9479caecca707cdc5325 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=7ae0cb9f27f612e21a7d60dc0fd6e817 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1cc411059b25f0fde0a0406eb9a0fc42 2500w" />

    <h2 className="pt-4 font-semibold text-base text-gray-800 dark:text-white">
      Visual Studio Code
    </h2>

    <p>Install Augment for Visual Studio Code</p>
  </Card>

  <Card className="bg-red" href="https://plugins.jetbrains.com/plugin/24072-augment">
    <img className="w-12 h-12" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c66ced5a9325498d8bfd13c09f308737" alt="JetBrains IDEs" data-og-width="64" width="64" data-og-height="64" height="64" data-path="images/jetbrains-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=19dbd0eee0903c4754190f5c5e14f204 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=256d16be8c5cee0ad668722591312714 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=47717f8a5dc2f992e7cd40bceea7dc7a 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6de74610603515a436cdd6ebbe50758c 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=81875705a8d31362022665f5edcd7385 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5cc81b977488e24b7a9ad9c2f305d084 2500w" />

    <h2 className="pt-4 font-semibold text-base text-gray-800 dark:text-white">
      JetBrains IDEs
    </h2>

    <p>Install Augment for JetBrains IDEs, including WebStorm, PyCharm, and IntelliJ</p>
  </Card>

  <Card className="bg-red" href="/cli/setup-auggie/install-auggie-cli">
    <img className="w-12 h-12" src="https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=296dbf9e9899ad6582c82bc3c7a44057" alt="Auggie CLI" data-og-width="230" width="230" data-og-height="230" height="230" data-path="images/cli.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=280&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=3821a862d7ae772e4b8f5c94763b938e 280w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=560&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=f466ec96e10fad60ee1efda5cbd9ca1d 560w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=840&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=e001eadbaa9a022e8eafac2c83f80157 840w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=1100&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=d2601529bf4c2f49fd28ef7b52d16d51 1100w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=1650&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=06faa3a54ba7278fedd6a85b208b1434 1650w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=2500&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=224824a6b754861089245e04a1a80cf0 2500w" />

    <h2 className="pt-4 font-semibold text-base text-gray-800 dark:text-white">
      Auggie CLI
    </h2>

    <p>
      All the power of Augment's agent, context engine, and tools in your terminal.
    </p>
  </Card>
</CardGroup>

### 2. Sign-in and sync your repository

For VS Code and JetBrains IDEs, follow the prompts in the Augment panel to [sign in](/setup-augment/sign-in) and [index your workspace](/setup-augment/workspace-indexing). If you don't see the Augment panel, press <Keyboard shortcut="Cmd/Ctrl L" /> or click the Augment icon in the side panel of your IDE.

For Auggie CLI, use the command `auggie login` to sign in.

### 3. Start coding with Augment

<Steps>
  <Step title="Using Agent">
    Augment agent enables you to complete tasks using natural language. Ask Agent to explain your codebase, debugging an
    issue, or writing entire functions, tests, or features. See [Using
    Agent](/using-augment/agent) for more details.
  </Step>

  <Step title="Using Next Edit">
    Augment Next Edit keeps you moving through your tasks by guiding you step-by-step through complex or repetitive changes. Jump to the next suggestion–in the same file or across your codebase–by pressing <Keyboard shortcut="Cmd/Ctrl ;" />. See
    [Using Next Edit](/using-augment/next-edit) for more details.
  </Step>

  <Step title="Using instructions">
    Start using an Instruction by hitting <Keyboard shortcut="Cmd/Ctrl I" /> and quickly write tests, refactor code, or craft any prompt in natural language to transform your code. See [Using
    Instructions](/using-augment/instructions) for more details.
  </Step>

  <Step title="Using completions">
    Augment provides inline code suggestions as you type. To accept the full
    suggestions, press <Keyboard shortcut="Tab" />, or accept the suggestion one
    word at a time with <Keyboard shortcut="Cmd/Ctrl →" />. See [Using
    Completions](/using-augment/completions) for more details.
  </Step>
</Steps>

<Next>
  * [Disable other code assistants](/troubleshooting/disable-copilot)
  * [Use keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts)
  * [Configure indexing](/setup-augment/workspace-indexing)
</Next>


# Agent Integrations
Source: https://docs.augmentcode.com/setup-augment/agent-integrations

Configure integrations for Augment Agent to access external services like GitHub, Linear, Jira, Confluence, Notion, Sentry, and Stripe.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const StripeLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M13.976 9.15c-2.172-.806-3.356-1.426-3.356-2.409 0-.831.683-1.305 1.901-1.305 2.227 0 4.515.858 6.09 1.631l.89-5.494C18.252.274 15.697 0 12.165 0 9.667 0 7.589.654 6.104 1.872 4.56 3.147 3.757 4.992 3.757 7.218c0 4.039 2.467 5.76 6.476 7.219 2.585.92 3.445 1.574 3.445 2.583 0 .98-.84 1.545-2.354 1.545-1.875 0-4.965-.921-6.99-2.109l-.9 5.555C5.175 22.99 8.385 24 11.714 24c2.641 0 4.843-.624 6.328-1.813 1.664-1.305 2.525-3.236 2.525-5.732 0-4.128-2.524-5.851-6.591-7.305z" fill="currentColor" />
  </svg>;

export const SentryLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z" fill="currentColor" />
    <path d="M12 6c-3.31 0-6 2.69-6 6h2c0-2.21 1.79-4 4-4s4 1.79 4 4-1.79 4-4 4v2c3.31 0 6-2.69 6-6s-2.69-6-6-6z" fill="currentColor" />
    <circle cx="12" cy="12" r="2" fill="currentColor" />
  </svg>;

export const GleanLogo = () => <svg width="24" height="24" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M8.95113 2.67649L10.2775 1L11.887 2.24179L10.5704 3.906C11.25 4.70862 11.6591 5.74239 11.6591 6.87053C11.6591 9.42425 9.56277 11.4945 6.9768 11.4945C4.39084 11.4945 2.29451 9.42425 2.29451 6.87053C2.29451 4.31677 4.39084 2.24655 6.9768 2.24655C7.68222 2.24655 8.35119 2.4006 8.95113 2.67649ZM6.9768 9.50853C5.50146 9.50853 4.30546 8.32747 4.30546 6.87053C4.30546 5.41358 5.50146 4.23245 6.9768 4.23245C8.45215 4.23245 9.64814 5.41358 9.64814 6.87053C9.64814 8.32747 8.45215 9.50853 6.9768 9.50853ZM11.7135 10.8261C11.5975 10.9618 11.4753 11.0913 11.3477 11.2173C11.2202 11.3424 11.0873 11.4622 10.949 11.5758C10.8116 11.6894 10.6689 11.7969 10.5208 11.8982C10.3736 11.9995 10.2211 12.0955 10.065 12.1837C9.90978 12.2726 9.75012 12.3537 9.58684 12.4286C9.42448 12.5034 9.25856 12.5712 9.08906 12.6311C8.92046 12.6919 8.74919 12.7448 8.57434 12.7898C8.40217 12.8365 8.22645 12.8743 8.04892 12.9043C7.87319 12.9351 7.69478 12.958 7.51459 12.973C7.33706 12.988 7.15776 12.9959 6.97667 12.9959C6.79558 12.9959 6.61628 12.988 6.43876 12.973C6.25856 12.958 6.08016 12.9351 5.90441 12.9043C5.7269 12.8743 5.55116 12.8365 5.379 12.7898L4.85357 14.726C5.08194 14.7868 5.31565 14.838 5.55206 14.8784C5.78488 14.919 6.02217 14.9498 6.26213 14.9692C6.49763 14.9895 6.73582 15 6.97667 15C7.21753 15 7.4557 14.9895 7.69121 14.9692C7.93117 14.9498 8.16756 14.919 8.40129 14.8784C8.63768 14.838 8.87051 14.7868 9.09977 14.726C9.33171 14.6662 9.56007 14.5957 9.7831 14.5147C10.0088 14.4345 10.2291 14.3446 10.445 14.2451C10.6617 14.1455 10.8741 14.0372 11.0802 13.92C11.2871 13.802 11.4887 13.6751 11.684 13.5394C11.8803 13.4047 12.0704 13.2619 12.2532 13.1104C12.437 12.9589 12.6136 12.8003 12.7822 12.6338C12.9517 12.4673 13.1131 12.2946 13.2675 12.1141C13.4218 11.9343 13.5681 11.7467 13.7055 11.5538L12.0435 10.4041C11.9401 10.5495 11.8295 10.6905 11.7135 10.8261Z" fill="currentColor" />
</svg>;

export const ConfluenceLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M2.43703 10.7785C2.30998 10.978 2.16478 11.2137 2.05588 11.3951C1.94698 11.5764 2.00143 11.8121 2.18293 11.921L4.66948 13.4442C4.85098 13.553 5.08695 13.4986 5.19585 13.3173C5.2866 13.1541 5.41365 12.9365 5.55885 12.7007C6.53895 11.0868 7.5372 11.2681 9.3159 12.1204L11.7843 13.281C11.9839 13.3717 12.2017 13.281 12.2925 13.0997L13.4722 10.4339C13.563 10.2526 13.4722 10.0169 13.2907 9.92619C12.7644 9.69044 11.7298 9.20084 10.8223 8.74749C7.44645 7.13354 4.59689 7.24234 2.43703 10.7785Z" fill="currentColor" />
  <path d="M13.563 4.72157C13.69 4.52209 13.8352 4.28635 13.9441 4.105C14.053 3.92366 13.9985 3.68791 13.817 3.57911L11.3305 2.05583C11.149 1.94702 10.913 2.00143 10.8041 2.18277C10.7134 2.34598 10.5863 2.56359 10.4411 2.79934C9.461 4.41329 8.46275 4.23194 6.68405 3.37963L4.21563 2.21904C4.01598 2.12837 3.79818 2.21904 3.70743 2.40038L2.52767 5.0661C2.43692 5.24745 2.52767 5.4832 2.70917 5.5739C3.23552 5.80965 4.27007 6.29925 5.1776 6.7526C8.53535 8.34845 11.3849 8.25775 13.563 4.72157Z" fill="currentColor" />
</svg>;

export const JiraLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.5028 2H7.7257C7.7257 3.44 8.8914 4.60571 10.3314 4.60571H11.3942V5.6343C11.3942 7.0743 12.5599 8.24 14 8.24V2.49714C14 2.22285 13.7771 2 13.5028 2ZM10.6399 4.88H4.86279C4.86279 6.32 6.0285 7.4857 7.4685 7.4857H8.53135V8.5143C8.53135 9.9543 9.69705 11.12 11.137 11.12V5.37715C11.137 5.10285 10.9142 4.88 10.6399 4.88ZM2 7.75995H7.7771C8.0514 7.75995 8.27425 7.9828 8.27425 8.2571V13.9999C6.83425 13.9999 5.66855 12.8342 5.66855 11.3942V10.3656H4.6057C3.16571 10.3656 2 9.19995 2 7.75995Z" fill="currentColor" />
</svg>;

export const NotionLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M3.47498 3.32462C3.92288 3.68848 4.0909 3.66071 4.93192 3.60461L12.8609 3.12851C13.029 3.12851 12.8892 2.96075 12.8332 2.93286L11.5163 1.98091C11.264 1.78502 10.9278 1.56068 10.2835 1.6168L2.60594 2.17678C2.32595 2.20454 2.27001 2.34453 2.38153 2.45676L3.47498 3.32462ZM3.95103 5.17244V13.5151C3.95103 13.9634 4.17508 14.1312 4.67938 14.1035L13.3933 13.5992C13.8978 13.5715 13.954 13.263 13.954 12.8989V4.61222C13.954 4.24858 13.8142 4.05248 13.5053 4.08047L4.39915 4.61222C4.06311 4.64046 3.95103 4.80855 3.95103 5.17244ZM12.5534 5.61996C12.6093 5.87218 12.5534 6.12417 12.3007 6.15251L11.8808 6.23616V12.3952C11.5163 12.5911 11.1801 12.7031 10.9 12.7031C10.4516 12.7031 10.3392 12.5631 10.0033 12.1433L7.257 7.83198V12.0034L8.12602 12.1995C8.12602 12.1995 8.12602 12.7031 7.4249 12.7031L5.49203 12.8152C5.43588 12.7031 5.49203 12.4235 5.68808 12.3673L6.19248 12.2276V6.71226L5.49215 6.65615C5.43599 6.40392 5.57587 6.04029 5.96841 6.01205L8.04196 5.87229L10.9 10.2398V6.37615L10.1713 6.29251C10.1154 5.98418 10.3392 5.76029 10.6195 5.73252L12.5534 5.61996ZM1.96131 1.42092L9.94726 0.832827C10.928 0.748715 11.1803 0.805058 11.7967 1.25281L14.3458 3.04451C14.7665 3.35262 14.9067 3.4365 14.9067 3.77237V13.5992C14.9067 14.215 14.6823 14.5793 13.8979 14.635L4.6239 15.1951C4.03509 15.2231 3.75485 15.1392 3.4465 14.747L1.56922 12.3113C1.23284 11.863 1.09296 11.5276 1.09296 11.1351V2.40043C1.09296 1.89679 1.31736 1.47669 1.96131 1.42092Z" fill="currentColor" />
  </svg>;

export const LinearLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M1.17156 9.61319C1.14041 9.4804 1.2986 9.39676 1.39505 9.49321L6.50679 14.6049C6.60323 14.7014 6.5196 14.8596 6.38681 14.8284C3.80721 14.2233 1.77669 12.1928 1.17156 9.61319ZM1.00026 7.56447C0.997795 7.60413 1.01271 7.64286 1.0408 7.67096L8.32904 14.9592C8.35714 14.9873 8.39586 15.0022 8.43553 14.9997C8.76721 14.9791 9.09266 14.9353 9.41026 14.8701C9.51729 14.8481 9.55448 14.7166 9.47721 14.6394L1.36063 6.52279C1.28337 6.44552 1.15187 6.48271 1.12989 6.58974C1.06466 6.90734 1.02092 7.23278 1.00026 7.56447ZM1.58953 5.15875C1.56622 5.21109 1.57809 5.27224 1.6186 5.31275L10.6872 14.3814C10.7278 14.4219 10.7889 14.4338 10.8412 14.4105C11.0913 14.2991 11.3336 14.1735 11.5672 14.0347C11.6445 13.9888 11.6564 13.8826 11.5929 13.819L2.18099 4.40714C2.11742 4.34356 2.01121 4.35549 1.96529 4.43278C1.8265 4.66636 1.70091 4.9087 1.58953 5.15875ZM2.77222 3.53036C2.7204 3.47854 2.7172 3.39544 2.76602 3.34079C4.04913 1.9043 5.9156 1 7.99327 1C11.863 1 15 4.13702 15 8.00673C15 10.0844 14.0957 11.9509 12.6592 13.234C12.6046 13.2828 12.5215 13.2796 12.4696 13.2278L2.77222 3.53036Z" fill="currentColor" />
  </svg>;

export const GitHubLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M7.49933 0.25C3.49635 0.25 0.25 3.49593 0.25 7.50024C0.25 10.703 2.32715 13.4206 5.2081 14.3797C5.57084 14.446 5.70302 14.2222 5.70302 14.0299C5.70302 13.8576 5.69679 13.4019 5.69323 12.797C3.67661 13.235 3.25112 11.825 3.25112 11.825C2.92132 10.9874 2.44599 10.7644 2.44599 10.7644C1.78773 10.3149 2.49584 10.3238 2.49584 10.3238C3.22353 10.375 3.60629 11.0711 3.60629 11.0711C4.25298 12.1788 5.30335 11.8588 5.71638 11.6732C5.78225 11.205 5.96962 10.8854 6.17658 10.7043C4.56675 10.5209 2.87415 9.89918 2.87415 7.12104C2.87415 6.32925 3.15677 5.68257 3.62053 5.17563C3.54576 4.99226 3.29697 4.25521 3.69174 3.25691C3.69174 3.25691 4.30015 3.06196 5.68522 3.99973C6.26337 3.83906 6.8838 3.75895 7.50022 3.75583C8.1162 3.75895 8.73619 3.83906 9.31523 3.99973C10.6994 3.06196 11.3069 3.25691 11.3069 3.25691C11.7026 4.25521 11.4538 4.99226 11.3795 5.17563C11.8441 5.68257 12.1245 6.32925 12.1245 7.12104C12.1245 9.9063 10.4292 10.5192 8.81452 10.6985C9.07444 10.9224 9.30633 11.3648 9.30633 12.0413C9.30633 13.0102 9.29742 13.7922 9.29742 14.0299C9.29742 14.2239 9.42828 14.4496 9.79591 14.3788C12.6746 13.4179 14.75 10.7025 14.75 7.50024C14.75 3.49593 11.5036 0.25 7.49933 0.25Z" fill="currentColor" />
  </svg>;

## About Agent Integrations

Augment Agent can access external services through integrations to add additional context to your requests and take actions on your behalf. These integrations allow Augment Agent to seamlessly work with your development tools without leaving your editor.

Once set up, Augment Agent will automatically use the appropriate integration based on your request context. Or, you can always mention the service in your request to use the integration.

## Setting Up Integrations

To set up integrations with Augment Agent in VS Code, follow these steps:

1. Click the settings icon in the top right of Augment's chat window or press <Keyboard shortcut="Cmd/Ctrl Shift P" /> and select <Command text="Show Settings Panel" />
2. Click "Connect" for the integration you want to set up

<img className="block rounded-xl" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=8e1cb7e476ff72baf79853e1a396061a" alt="Set up integrations in the settings page" data-og-width="1096" width="1096" data-og-height="598" height="598" data-path="images/integration-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6b58b42005ec712d925971f18e71f0df 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b0347aaa6924edd4a61a6ed59e70f84c 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=50b67616fb88ab7b1620628cf09c5c40 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=66664659b4ca1d32c356fbf0e72b2778 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ccfd90b3fe548564b1c3482f5d4d0e95 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/integration-settings.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f78ecdd094cea06ca826da1580683efc 2500w" />

You'll be redirected to authorize the integration with the appropriate service. After authorization, the integration will be available for use with Augment Agent.

## Native Integrations

## <div className="flex items-center gap-2"><div className="w-6 h-6"><GitHubLogo /></div> GitHub Integration</div>

Add additional context to your requests and take actions. Pull in information from a GitHub Issue, make the changes to your code (or have Agent do it for you), and open a Pull Request all without leaving your editor.

### Examples

* "Implement Issue #123 and open up a pull request"
* "Find all issues assigned to me"
* "Check the CI status of my latest commit"

For authorization details, see [GitHub documentation](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps).

## <div className="flex items-center gap-2"><div className="w-6 h-6"><LinearLogo /></div> Linear Integration</div>

Read, update, comment on, and resolve your Linear issues within your IDE.

### Examples

* "Fix TES-1"
* "Create Linear tickets for these TODOs"
* "Help me triage these new bug reports"

For authorization details, see [Linear documentation](https://linear.app/docs/third-party-application-approvals).

## <div className="flex items-center gap-2"><div className="w-6 h-6"><JiraLogo /></div> Jira Integration</div>

Work on your Jira issues, create new tickets, and update existing ones.

### Examples

* "Show me all my assigned Jira tickets"
* "Create a Jira ticket for this bug"
* "Create a PR to fix SOF-123"
* "Update the status of PROJ-123 to 'In Progress'"

For authorization details, see [Jira documentation](https://support.atlassian.com/jira-software-cloud/docs/allow-oauth-access/).

## <div className="flex items-center gap-2"><div className="w-6 h-6"><ConfluenceLogo /></div> Confluence Integration</div>

Query existing documentation or update pages directly from your IDE. Ensure your team's knowledge base stays current without any context switching.

### Examples

* "Summarize our Confluence page on microservice architecture"
* "Find information about our release process in Confluence"
* "Update our onboarding docs to explain how we use Bazel"

For authorization details, see [Confluence documentation](https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/).

## <div className="flex items-center gap-2"><div className="w-6 h-6"><NotionLogo /></div> Notion Integration</div>

Search and retrieve information from your team's knowledge base - access documentation, meeting notes, and project specifications. This integration is currently READ-ONLY.

### Examples

* "Find Notion pages about our API documentation"
* "Show me the technical specs for the payment system"
* "What outstanding tasks are left from yesterday's team meeting?"

For authorization details, see [Notion documentation](https://www.notion.so/help/add-and-manage-connections-with-the-api#install-from-a-developer).

## <div className="flex items-center gap-2"><div className="w-6 h-6"><GleanLogo /></div> Glean Integration</div>

> **Note:** The Glean integration is in early access and thus is a little different from other integrations.
>
> * It is currently only available to enterprise customers.
> * It does not appear in the list of integrations in the settings panel.

The Glean integration lets the agent retrieve information from your team's internal data sources leveraging Glean's powerful search engine.

**To Enable the Glean Integration:** You'll need to be have administrator access to Augment and Glean. Follow the instructions on [https://app.augmentcode.com/gleanConfig](https://app.augmentcode.com/gleanConfig) and your agent will be ready to use Glean!

### Examples

* "Search Glean for past related incidents and how they were resolved"
* "Search Glean for why we're migrating to a new payment processor"

## Enhanced Native Integrations

> **New:** Enhanced native integrations for Sentry and Stripe launched on July 30, 2025, providing deeper, more seamless access to your error tracking and payment data.

### <div className="flex items-center gap-2"><div className="w-6 h-6"><SentryLogo /></div> Sentry Integration</div>

Search issues, errors, traces, logs, and releases. Create RCAs and AI-Generated fixes with Seer integration for comprehensive error tracking and resolution.

#### Examples

* "Diagnose the top unresolved crashes in my React Native app and propose fixes"
* "Show me all errors from the latest release and their impact"
* "Create a root cause analysis for the payment processing errors"
* "Find similar issues that were resolved and suggest fixes"

### <div className="flex items-center gap-2"><div className="w-6 h-6"><StripeLogo /></div> Stripe Integration</div>

Real-time payment events, refund status, subscription metrics, and secure tokenization. Available via both remote and local MCP servers with OAuth MCP support in public preview.

#### Examples

* "Create a dashboard showing failed payment intents in the last 24 hours and suggest retry logic"
* "Analyze subscription churn patterns and recommend retention strategies"
* "Show me all refunds processed this week and their reasons"
* "Generate a report on payment method performance"

## Next Steps

* [Configure additional tools with Easy MCP or advanced MCP setup](/setup-augment/mcp)
* Explore one-click integrations for CircleCI, MongoDB, and Redis through Easy MCP


# Rules & Guidelines for Agent and Chat
Source: https://docs.augmentcode.com/setup-augment/guidelines

You can provide custom rules and guidelines written in natural language to improve Agent and Chat with your preferences, best practices, styles, and technology stack.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

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

<Availability tags={["vscode", "jetbrains"]} />

## What are Rules & Guidelines?

Agent and Chat rules and guidelines are natural language instructions that can help Augment reply with more accurate and relevant responses. Rules and guidelines are perfect for telling Augment to take into consideration specific preferences, package versions, styles, and other implementation details that can’t be managed with a linter or compiler. You can create guidelines for a specific workspace or globally for all chats in your IDE; guidelines do not currently apply to Completions, Instructions, or Next Edit.

User Guidelines are defined under Settings and stored within your IDE to be used to guide preferences inside of the Agent and Chat. Workspace Guidelines and Rules are stored directly in your repository.

## Working with User Guidelines

<Info>
  User Guidelines are stored locally in your IDE and will be applied to all future chats in that IDE. Guidelines defined in VSCode will not propagate to JetBrains IDEs and vice versa.
</Info>

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ea8daf68e19c31f2784d2de6765dc627" alt="Adding user guidelines" className="rounded-xl" data-og-width="1248" width="1248" data-og-height="603" height="603" data-path="images/user-guidelines.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=44a75f2ea891c74955080112b31425d7 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ad02067cd61b08f0b695db3c8cf91700 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=81690b18ca6b28ed1a140bb4663a8208 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=44503cc6949ec0dc58c04e73c3ea17be 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=5bc2aa6fc7e5b4a4289fb8b88cd7ef0f 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=5f09033c7ae02a579cdafffcbf329bd0 2500w" />

You can add user guidelines by clicking Context menu (@), starting an @-mention inside Chat, or clicking Settings > Rules and User Guidelines.

### Navigating from the Context menu (@) User Guidelines

1. @ mention and select `User Guidelines`
2. Enter your guidelines (see below for tips)
3. Press Escape to save or wait for autosave

### Navigating from Settings > User Guidelines and Rules

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/open-rules.gif?s=07fce1fa6c1e2bdf6f78642658f804be" alt="Open rules and guidelines" className="rounded-xl" data-og-width="800" width="800" data-og-height="393" height="393" data-path="images/open-rules.gif" data-optimize="true" data-opv="3" />

1. In the top right corner, select the hamburger menu (⋯)
2. Select Settings
3. From the left menu in Augment Settings, select User Guidelines and Rules

## Working with Rules

You can craft Rules to guide Augment towards specific documentation, frameworks, workflows or workstyles.

Rules are files that live in the `.augment/rules` directory. Currently, we support 3 types of rules:

* **Always**: contents will be included in every user prompt
* **Manual**: needs to be tagged through @ attaching the Rules file manually
* **Auto**: Agent will automatically detect and attach rules based on a description field

### Importing Rules

**Augment** will automatically import rules if they are detected in the current workspace. Augment will look for markdown files, e.g., files ending with `*.md` or `*.mdx`. You can also manually import rules inside of Settings > Import rules.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=1a01f8bde915b4d3049d7b39f17eddba" alt="Import rules" className="rounded-xl" data-og-width="1600" width="1600" data-og-height="839" height="839" data-path="images/import-rules.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=0eb8b03ecb20cc3ef865dd35bd692b0c 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a16b6f051ca12bd4f523c818cbf1096c 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=98b8e52dbc26d79d38117c71c7303379 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f26d41383781b07faba4af8e7d93d7b5 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f558643818e7433474a1d0ea80c55602 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=68e307de359234378d23d0613e747e89 2500w" />

### Importing Augment Memories into Rules or User Guidelines

Augment Memories are automatically created by the Agent. If you’ve ever modified the Memories or prompted the Agent to remember something you can import these preferences as Rules or User Guidelines.

1. From the prompt box, click on Augment Memories
2. Select the item you'd like to import and then click User Guidelines at the top of Augment Memories from inside the editor.
3. To add the memory as a Rule, you'll first need to add at least one rule using +Create new rule file. Now, you can select any information inside the Augment Memories and save it as a Rule.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=45a38f467945005fe2ac2779108ef06f" alt="Move memories" className="rounded-xl" data-og-width="1816" width="1816" data-og-height="426" height="426" data-path="images/move-memories.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e62394563486d878453a223c426cf6be 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=04d51becdd41bbfd3f443be4028bb959 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=177121e2215c3364219ca1b6d85bcd22 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=84a7f76d24c1a4ead9755a2bb53945ff 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7a96b7c249d5fd4318c1e167eddc4fa8 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f756375a0d1e054fe1820b2913453161 2500w" />

## Working with Workspace Guidelines `.augment-guidelines` (legacy)

You can add an `.augment-guidelines` file to the root of a repository to specify a set of guidelines that Augment will follow for all Agent and Chat sessions on the codebase. The `.augment-guidelines` file should be added to your version control system so that everyone working on the codebase has the same guidelines.

### Tips for good rules and guidelines

* Provide guidelines as a list
* Use simple, clear, and concise language for your guidelines
* Asking for shorter or code-only answers may hurt response quality

### Examples

<AccordionGroup>
  <Accordion title="User Guideline Examples">
    * Ask for additional explanation e.g. `For Typescript code, explain what the code is doing in more detail`

    * Set a preferred language e.g. `Respond to questions in Spanish`
  </Accordion>

  <Accordion title="Rule Examples">
    * Add links to Google Docs, Notion or Confluence files that define goals, product requirements, or project objectives

    * Point to specific documentation e.g. `Python 3.13.5` for the dependencies inside your project

    * Outline templates or example code commonly used in your project

    * Establish consistent frameworks, coding styles, and architectural patterns across your codebase

    * Provide examples on codebase style. For example:
      * Information that ONLY applies to the specific files, functions, or code snippets
      * Vague or obvious preferences that aren't actionable
      * General statements about good programming practices that any user would want
  </Accordion>

  <Accordion title="Workspace Guideline Examples">
    * Identifying preferred libraries e.g. `pytest vs unittest`
    * Identifying specific patterns e.g. `For NextJS, use the App Router and server components`
    * Rejecting specific anti-patterns e.g. `a deprecated internal module`
    * Defining naming conventions e.g. `functions start with verbs`
  </Accordion>
</AccordionGroup>

## FAQs

<AccordionGroup>
  <Accordion title="How are Rules different from Guidelines?">
    Guidelines and Rules differ in how they are stored and their scope of influence.

    * **User Guidelines** are stored in the user’s local IDE storage that will persist across Chat & Agent sessions; however, they do not persist across workspaces.
    * **Rules** will also be stored within the repository under the `.augment/rules` root that will allow you to split up previous Guidelines into multiple files to more precisely define your preferences.
    * **Workspace Guidelines** (legacy) stored within the repository under the `.augment-guidelines` file are a legacy set of rules that can be edited by editing the `.augment-guidelines` in your repository. Augment will automatically import Workspace Guidelines as Rules which you can access under Settings > User Guidelines and Rules.
  </Accordion>

  <Accordion title="What are the current limitations?">
    * User Guidelines are currently limited to a maximum of 24,576 characters.
    * Workspace Guidelines + Rules are limited to a maximum of 49,512 characters. If we exceed these limits, the user will be notified in app and be applied in order of (manual rules, always + auto rules, .augment-guidelines)
    * For VSCode, Guidelines are available in plugin version 0.492.0 and above
    * For JetBrains IDEs, Guidelines are available in plugin version 0.197.0 and above
    * Rules are not yet available in JetBrains IDEs
  </Accordion>
</AccordionGroup>

## See Also

* [Custom Rules and Guidelines (CLI)](/cli/rules) - Configure rules for Auggie CLI
* [Workspace Context](/setup-augment/workspace-context-vscode) - Understanding workspace configuration in VSCode
* [Chat Context](/using-augment/chat-context) - Learn about context in Chat


# Install Augment for Slack
Source: https://docs.augmentcode.com/setup-augment/install-slack-app

Ask Augment questions about your codebase right in Slack.

export const Next = ({children}) => <div className="border-t border-b pb-8 border-gray dark:border-white/10">
    <h3>Next steps</h3>
    {children}
  </div>;

export const SlackLogo = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 127 127">
    <path fill="#E01E5A" d="M27.2 80c0 7.3-5.9 13.2-13.2 13.2C6.7 93.2.8 87.3.8 80c0-7.3 5.9-13.2 13.2-13.2h13.2V80zm6.6 0c0-7.3 5.9-13.2 13.2-13.2 7.3 0 13.2 5.9 13.2 13.2v33c0 7.3-5.9 13.2-13.2 13.2-7.3 0-13.2-5.9-13.2-13.2V80z" />
    <path fill="#36C5F0" d="M47 27c-7.3 0-13.2-5.9-13.2-13.2C33.8 6.5 39.7.6 47 .6c7.3 0 13.2 5.9 13.2 13.2V27H47zm0 6.7c7.3 0 13.2 5.9 13.2 13.2 0 7.3-5.9 13.2-13.2 13.2H13.9C6.6 60.1.7 54.2.7 46.9c0-7.3 5.9-13.2 13.2-13.2H47z" />
    <path fill="#2EB67D" d="M99.9 46.9c0-7.3 5.9-13.2 13.2-13.2 7.3 0 13.2 5.9 13.2 13.2 0 7.3-5.9 13.2-13.2 13.2H99.9V46.9zm-6.6 0c0 7.3-5.9 13.2-13.2 13.2-7.3 0-13.2-5.9-13.2-13.2V13.8C66.9 6.5 72.8.6 80.1.6c7.3 0 13.2 5.9 13.2 13.2v33.1z" />
    <path fill="#ECB22E" d="M80.1 99.8c7.3 0 13.2 5.9 13.2 13.2 0 7.3-5.9 13.2-13.2 13.2-7.3 0-13.2-5.9-13.2-13.2V99.8h13.2zm0-6.6c-7.3 0-13.2-5.9-13.2-13.2 0-7.3 5.9-13.2 13.2-13.2h33.1c7.3 0 13.2 5.9 13.2 13.2 0 7.3-5.9 13.2-13.2 13.2H80.1z" />
  </svg>;

export const GitHubLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M7.49933 0.25C3.49635 0.25 0.25 3.49593 0.25 7.50024C0.25 10.703 2.32715 13.4206 5.2081 14.3797C5.57084 14.446 5.70302 14.2222 5.70302 14.0299C5.70302 13.8576 5.69679 13.4019 5.69323 12.797C3.67661 13.235 3.25112 11.825 3.25112 11.825C2.92132 10.9874 2.44599 10.7644 2.44599 10.7644C1.78773 10.3149 2.49584 10.3238 2.49584 10.3238C3.22353 10.375 3.60629 11.0711 3.60629 11.0711C4.25298 12.1788 5.30335 11.8588 5.71638 11.6732C5.78225 11.205 5.96962 10.8854 6.17658 10.7043C4.56675 10.5209 2.87415 9.89918 2.87415 7.12104C2.87415 6.32925 3.15677 5.68257 3.62053 5.17563C3.54576 4.99226 3.29697 4.25521 3.69174 3.25691C3.69174 3.25691 4.30015 3.06196 5.68522 3.99973C6.26337 3.83906 6.8838 3.75895 7.50022 3.75583C8.1162 3.75895 8.73619 3.83906 9.31523 3.99973C10.6994 3.06196 11.3069 3.25691 11.3069 3.25691C11.7026 4.25521 11.4538 4.99226 11.3795 5.17563C11.8441 5.68257 12.1245 6.32925 12.1245 7.12104C12.1245 9.9063 10.4292 10.5192 8.81452 10.6985C9.07444 10.9224 9.30633 11.3648 9.30633 12.0413C9.30633 13.0102 9.29742 13.7922 9.29742 14.0299C9.29742 14.2239 9.42828 14.4496 9.79591 14.3788C12.6746 13.4179 14.75 10.7025 14.75 7.50024C14.75 3.49593 11.5036 0.25 7.49933 0.25Z" fill="currentColor" />
  </svg>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

<Note>
  The Augment GitHub App is compatible with GitHub.com and GitHub Enterprise Cloud. GitHub Enterprise Server is not currently supported.
</Note>

## About Augment for Slack

Augment for Slack brings the power of Augment Chat to your team's Slack workspace. Mention <Command text="@Augment" /> in any channel or start a DM with Augment to have deep codebase-aware conversations with your team.

*To protect your confidential information, Augment will not include repository context in responses when used in shared channels with external members.*

## Installing Augment for Slack

### 1. Install GitHub App

<CardGroup cols={1}>
  <Card title="Install Augment GitHub App" href="https://github.com/apps/augmentcode/installations/new" icon={<GitHubLogo />} horizontal>
    GitHub App for Augment Chat in Slack
  </Card>
</CardGroup>

To enable Augment's rich codebase-awareness, install the Augment GitHub App and grant access to your desired repositories. Organization owners and repository admins can install the app directly; others will need owner approval. See [GitHub documentation](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party) for details.

We recommend authorizing only the few active repositories you want accessible to Augment Slack users. You can modify repository access anytime in the GitHub App settings.

<img className="block rounded-xl" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5e4084c99c0295b0f64244970b63b7c1" alt="Installing the GitHub app on a single repository" data-og-width="1372" width="1372" data-og-height="1387" height="1387" data-path="images/install-github-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=74db4d5e2ebb869baec7fa8a5542fe1e 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=124a9fff587698addbf6521b889b5c28 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3141ed13276ff2da9a123ad94d1d98b9 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=aa841e9121554b8c1a75c35097e0d84b 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7abe3b886150b097a11ae90b41cae3f1 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=333c129e393ab4b32f04c3940492cf1c 2500w" />

### 2. Install Slack App

<CardGroup cols={1}>
  <Card title="Install Augment for Slack" href="https://slack.com/oauth/v2/authorize?client_id=3751018318864.7878669571030&scope=app_mentions:read,channels:history,channels:read,chat:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,mpim:read,mpim:write,reactions:read,reactions:write,users.profile:read,users:read,users:read.email,groups:write,commands,assistant:write&user_scope=identity.basic" icon={<SlackLogo />} horizontal>
    Slack App for Augment Code
  </Card>
</CardGroup>

Once you have the GitHub App installed, install the Augment Slack App. You'll need an Augment account and correct permissions to install Slack apps for your workspace.

Any workspace member can use the Slack app once installed. Contact us if you need to restrict access to specific channels or users.

### 3. Add Augment to the Slack Navigation Bar

Make Augment easily accessible by adding it to Slack's assistant-view navigation bar:

1. Click your profile picture → **Preferences** → **Navigation**
2. Under **App agents & assistants**, select **Augment**

*Note: Each user can customize this setting in their preferences.*

<Next>
  [Using Augment for Slack](/using-augment/slack)
</Next>


# Install Augment for Visual Studio Code
Source: https://docs.augmentcode.com/setup-augment/install-visual-studio-code

Augment in Visual Studio Code gives you powerful code completions, transformations, and chat capabilities integrated into your favorite code editor.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const VscodeLogo = () => <svg xmlns="http://www.w3.org/2000/svg" xmlnsXlink="http://www.w3.org/1999/xlink" version="1.1" viewBox="0 0 64 64">
    <defs>
      <mask id="mask" x=".5" y=".7" width="63.5" height="63.1" maskUnits="userSpaceOnUse">
        <g id="mask0">
          <path fill="#fff" d="M45.5,63.5c1,.4,2.1.4,3.1-.1l13.1-6.3c1.4-.7,2.2-2,2.2-3.6V10.9c0-1.5-.9-2.9-2.2-3.6l-13.1-6.3c-1.3-.6-2.9-.5-4,.4-.2.1-.3.3-.5.4l-25,22.8-10.9-8.3c-1-.8-2.4-.7-3.4.2l-3.5,3.2c-1.2,1-1.2,2.9,0,3.9l9.4,8.6L1.4,40.9c-1.2,1-1.1,2.9,0,3.9l3.5,3.2c.9.9,2.4.9,3.4.1l10.9-8.3,25,22.8c.4.4.9.7,1.4.9ZM48.1,17.9l-19,14.4,19,14.4v-28.8Z" />
        </g>
      </mask>
      <linearGradient id="linear-gradient" x1="32.2" y1="65.3" x2="32.2" y2="2.2" gradientTransform="translate(0 66) scale(1 -1)" gradientUnits="userSpaceOnUse">
        <stop offset="0" stopColor="#fff" />
        <stop offset="1" stopColor="#fff" stopOpacity="0" />
      </linearGradient>
    </defs>
    <g style={{
  isolation: "isolate"
}}>
      <g mask="url(#mask)">
        <path fill="#0065a9" d="M61.8,7.4l-13.1-6.3c-1.5-.7-3.3-.4-4.5.8L1.4,40.9c-1.2,1-1.1,2.9,0,3.9l3.5,3.2c.9.9,2.4.9,3.4.2L59.8,9c1.7-1.3,4.2,0,4.2,2.1v-.2c0-1.5-.9-2.9-2.2-3.6Z" />
        <path fill="#007acc" d="M61.8,57.1l-13.1,6.3c-1.5.7-3.3.4-4.5-.8L1.4,23.6c-1.2-1-1.1-2.9,0-3.9l3.5-3.2c.9-.9,2.4-.9,3.4-.2l51.5,39.1c1.7,1.3,4.2,0,4.2-2.1v.2c0,1.5-.9,2.9-2.2,3.6Z" />
        <path fill="#1f9cf0" d="M48.7,63.4c-1.5.7-3.3.4-4.5-.8,1.5,1.5,4,.4,4-1.6V3.5c0-2.1-2.5-3.1-4-1.6,1.2-1.2,3-1.5,4.5-.8l13.1,6.3c1.4.7,2.2,2,2.2,3.6v42.6c0,1.5-.9,2.9-2.2,3.6l-13.1,6.3Z" />
        <g style={{
  mixBlendMode: "overlay",
  opacity: 0.2
}}>
          <path fill="url(#linear-gradient)" fillRule="evenodd" d="M45.5,63.5c1,.4,2.1.4,3.1-.1l13.1-6.3c1.4-.7,2.2-2,2.2-3.6V10.9c0-1.5-.9-2.9-2.2-3.6l-13.1-6.3c-1.3-.6-2.9-.5-4,.4-.2.1-.3.3-.5.4l-25,22.8-10.9-8.3c-1-.8-2.4-.7-3.4.1l-3.5,3.2c-1.2,1-1.2,2.9,0,3.9l9.4,8.6L1.4,40.9c-1.2,1-1.1,2.9,0,3.9l3.5,3.2c.9.9,2.4.9,3.4.2l10.9-8.3,25,22.8c.4.4.9.7,1.4.9ZM48.1,17.9l-19,14.4,19,14.4v-28.8Z" />
        </g>
      </g>
    </g>
  </svg>;

export const ExternalLink = ({text, href}) => <a href={href} rel="noopener noreferrer">
    {text}
  </a>;

<CardGroup cols={1}>
  <Card title="Get the Augment Extension" href="https://marketplace.visualstudio.com/items?itemName=augment.vscode-augment" icon={<VscodeLogo />} horizontal>
    Install Augment for Visual Studio Code
  </Card>
</CardGroup>

## About Installation

Installing <ExternalLink text="Augment for Visual Studio Code" href="https://marketplace.visualstudio.com/items?itemName=augment.vscode-augment" /> is easy and will take you less than a minute. You can install the extension directly from the Visual Studio Code Marketplace or follow the instructions below.

<img className="block rounded-xl" src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-extension.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=495c9d08aa8330138f600a6d66431386" alt="Augment extension in Visual Studio Code Marketplace" data-og-width="1691" width="1691" data-og-height="807" height="807" data-path="images/vscode-extension.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-extension.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a8cd7fac7b09d39472a3bc4eb120e08b 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-extension.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e92a38f8f4afae66e3309a2ed2cca250 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-extension.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=500675b6520eb9f8f3099474cb50e3a8 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-extension.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=cfe11d6315f7bdf9c430d0458cbc64b2 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-extension.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=0082875d639bd21238e7d8d376259361 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-extension.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=12f768ba87c8887c995c615956d86e29 2500w" />

## Installing Augment for Visual Studio Code

<Steps>
  <Step title="Make sure you have the latest version of Visual Studio Code installed">
    You can download the latest version of Visual Studio Code from the <ExternalLink text="Visual Studio Code website" href="https://code.visualstudio.com/" />. If you already have Visual Studio Code installed, you can update to the latest version by going to <Command text="Code > Check for Updates..." />.
  </Step>

  <Step title="Open the Extensions panel in Visual Studio Code">
    Click the Extensions icon in the sidebar to show
    the Extensions panel.
  </Step>

  <Step title="Search for Augment in the marketplace">
    Using the search bar in the Extensions panel, search for{" "}
    <Command text="Augment" />.
  </Step>

  <Step title="Install the extension">
    Click <Command text="Install" /> to install the extension.
  </Step>

  <Step title="Sign into Augment and get coding">
    Sign in to by clicking <Command text="Sign in to Augment" /> in the Augment
    panel. If you do not see the Augment panel, use the shortcut{" "}
    <Keyboard shortcut="Cmd/Ctrl L" /> or click the Augment icon{" "}
    <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a659f6a8cc305adb98f17ffe362de081" className="inline h-3 p-0 m-0" data-og-width="18" width="18" data-og-height="12" height="12" data-path="images/augment-icon-simple.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4a291cdc6d1243c7730017b000deec5b 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5d30f5b2920cba98990963c02c18a39a 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d4ba43987e110d9065c707ef4c6f09d7 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f6ec12c894c73d1c344b5cce54ff19d3 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=af28ff3eeed5be9bbb6c8156e0d94bce 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-simple.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=549509ac3a1fbdeb2700fb4b9f8f03ad 2500w" /> in the side bar of your IDE. See more details in [Sign
    In](/setup-augment/sign-in).
  </Step>
</Steps>

## About pre-release versions

We regularly publish pre-release versions of the Augment extension. To use the pre-release version, go to the Augment extension in the Extensions panel and click <Command text="Switch to Pre-Release Version" /> and then <Command text="Restart extensions" />.

Pre-release versions may sometimes contain bugs or otherwise be unstable. As with the released version, please report any problems by sending us [feedback](/troubleshooting/feedback).


# Setup Model Context Protocol servers
Source: https://docs.augmentcode.com/setup-augment/mcp

Use Model Context Protocol (MCP) servers with Augment to expand Augment's capabilities with external tools and data sources.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## About Model Context Protocol servers

Augment Agent can utilize external integrations through Model Context Protocol (MCP) to access external systems for information and integrate tools to take actions. MCP is an open protocol that provides a standardized way to connect AI models to different data sources and tools. MCP servers can be used to access local or remote databases, run automated browser testing, send messages to Slack, or even play music on Spotify.

## Easy MCP: One-Click Integrations

> **New:** Easy MCP launched on July 30, 2025, making it easier than ever to connect popular developer tools to Augment Code.

Easy MCP is a new feature in the Augment Code extension that transforms complex MCP server setup into a single click. Instead of manually configuring servers, hunting for GitHub repos, or editing JSON files, you can now connect popular developer tools with just an API token or OAuth approval.

### Available Easy MCP Integrations

Easy MCP provides one-click access to these popular developer tools:

#### CircleCI

* **Context:** Build logs, test insights, flaky-test detection
* **Sample prompt:** "Find the latest failed pipeline on my branch and surface the failing tests."
* **Setup:** Click "+", paste your CircleCI API token, and you're connected.

#### MongoDB

* **Context:** Data exploration, database management, and context-aware code generation
* **Sample prompt:** "Analyze my user collection schema and suggest optimizations for our new search feature."
* **Setup:** One-click OAuth connection to your MongoDB instance.

#### Redis

* **Context:** Keyspace introspection, TTL audits, and migration helpers
* **Sample prompt:** "Generate a migration script to move expiring session keys to the new namespace."
* **Setup:** Connect with your Redis credentials in seconds.

### Getting Started with Easy MCP

1. Open the Augment Code extension in VS Code
2. Navigate to the Easy MCP pane in the settings
3. Click the "+" button next to your desired integration
4. Paste an API token or approve OAuth
5. Start using the integration immediately in your Agent conversations

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c02010664a36e319631e3f5367f5f00e" className="rounded-xl" data-og-width="1078" width="1078" data-og-height="646" height="646" data-path="images/EasyMCP.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b26a28d983527d327bc35e249eabf1a8 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7e06026e10eefc855da6579dac1dea47 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3c6df59927adaa82ba7427ad8f0defa2 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=849c567deb9a052d933a4aa31f492dec 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3e66c48df372bb4e699350f8073ff0c6 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/EasyMCP.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cda0cb53a2619c7cb2adffe3a12c3c38 2500w" />

From that moment on, Augment Code streams your tool's live context into every suggestion and autonomous Agent run.

## Advanced MCP Configuration

For developers who need custom MCP server configurations or want to use servers not available through Easy MCP, you can still configure MCP servers manually.

There are three ways to configure MCP servers in Augment:

1. **Easy MCP** (recommended) - One-click integrations for popular tools
2. **Augment Settings Panel** - Manual configuration with a GUI
3. **Import from JSON** - Paste a JSON config to quickly add servers

MCP servers configured through the Settings Panel or Import from JSON are managed in the same place. After importing, you can edit or remove servers in the Settings Panel.

## Configure in the Augment Settings Panel

The easiest way to configure MCP servers is to use the Augment Settings Panel.
To access the settings panel, open the options menu in the upper right of the Augment panel and click the Settings option. Once the settings panel is open, you will see a section for MCP servers.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=f34e3682127f6e6ba2dfc5a4ae7fd8a5" className="rounded-xl" data-og-width="1296" width="1296" data-og-height="556" height="556" data-path="images/settings-panel-mcp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a6dff18658e5c7454fa009cc484467db 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=dbc7a07976708c4fc72a662b98c06c60 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e382a538a495053c3ca1a3c01d5e85ba 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=2efdfd04627b5a659795e5b74e672b4d 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=d0f3ce6ce06c668a2f3160a35c0586e5 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e4b1e413786735c373fb6ec386cd676e 2500w" />

Fill in the `name` and `command` fields. The `name` field must be a unique name for the server. The `command` field is the command to run the server. Environment variables have their own section and no longer need to be specified in the command.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=20d9ffa2c683194ec1d66afe390f6f9d" className="rounded-xl" data-og-width="1090" width="1090" data-og-height="586" height="586" data-path="images/mcp-env.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e9c87679180a6db78e05d7cce22845ff 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e7e5805c874eb5e006c27ee3f52360fa 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=8930b7ececcdd06705dcc9d9ed86ef12 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=8e9b4f557196621ab4d45dd52defbda7 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bd0ff7868ab46ea8325a6b9ed1856294 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/mcp-env.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4cba9d7e59969d4a48aa630ab14932a7 2500w" />

To add additional servers, click the `+` button next to the `MCP` header.
To edit a configuration, or to delete a server, click the `...` button next to the server name.

### Add a Remote MCP server

If your MCP server runs remotely (for example, a hosted service), click the "+ Add remote MCP" button in the MCP section. Remote MCP connections support both HTTP and SSE (Server‑Sent Events).

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=21086d1c640c6e20975aa7207532be78" className="rounded-xl" data-og-width="1036" width="1036" data-og-height="676" height="676" data-path="images/settings-panel-mcp-remote.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3ac00d4975d2791c378a0e24b7fd1457 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4d92460a09146279b73693c6af5be240 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=2a9dfd961063e277d0dee794b71b0b47 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=cdbad5fac2856fe1fb9bc272cb22622d 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=d99df8defa992c69589501c7db0e0204 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-remote.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=7f5c7e96f585a368523586154bfd696e 2500w" />

* Connection Type: choose HTTP or SSE
* Name: a unique display name for the server
* URL: the base URL to your MCP server (e.g., [https://api.example.com](https://api.example.com))

Remote MCP servers appear alongside your local MCP servers in the list. You can edit or remove them using the "..." menu next to the server name.

## Import from JSON

You can quickly add MCP servers by importing a JSON configuration from the Augment Settings Panel:

1. Open the Settings Panel (gear icon in the Augment panel)
2. In the MCP section, click <strong>Import from JSON</strong>
3. Paste a configuration like the following and click Save

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-json.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=63f0f66b4c03a744d066509d2bd7d107" className="rounded-xl" data-og-width="1018" width="1018" data-og-height="512" height="512" data-path="images/settings-panel-mcp-json.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-json.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=c92854a977210732f7ce88365f420f13 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-json.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=13f3d3e3bd2ddd45511b24418908e37f 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-json.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=d26b8bcf4f9e592bf2b539a469de1dbe 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-json.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=39eed3e27ae9dfeeb394146153648b2a 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-json.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=734fdddd4287a85ee69e6455b1af98b1 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/settings-panel-mcp-json.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=bf906af74ac296b11558e48a07e99caf 2500w" />

**Example: Local command (Context7 via npx)**

```json  theme={null}
{
  "mcpServers": {
    "Context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

**Example: Remote SSE endpoint**

```json  theme={null}
{
  "mcpServers": {
    "test": {
      "url": "http://localhost:3001/sse",
      "type": "sse"
    }
  }
}
```

After importing, servers appear in the list where you can edit, test, or remove them. Ensure any required dependencies for the server are installed on your machine.

## Server compatibility

Not all MCP servers are compatible with Augment's models. The MCP standard, implementation of specific servers, and Augment's MCP support are frequently being updated, so check compatibility frequently.


# Sign in and out
Source: https://docs.augmentcode.com/setup-augment/sign-in

After you have installed the Augment extension, you will need to sign in to your account.

export const MoreVertIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M479.79-192Q450-192 429-213.21t-21-51Q408-294 429.21-315t51-21Q510-336 531-314.79t21 51Q552-234 530.79-213t-51 21Zm0-216Q450-408 429-429.21t-21-51Q408-510 429.21-531t51-21Q510-552 531-530.79t21 51Q552-450 530.79-429t-51 21Zm0-216Q450-624 429-645.21t-21-51Q408-726 429.21-747t51-21Q510-768 531-746.79t21 51Q552-666 530.79-645t-51 21Z" />
    </svg>
  </div>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## About Authentication

You can sign in to Augment using one of the supported identity providers–Google or Microsoft–or sign in using your email address and a single-use code we send to you. During the process, you will be redirected to your browser to sign in to your account.

## Sign in

<Steps>
  <Step title="Sign in to Augment">
    Click the <Command text="Sign in to Augment" /> button in the Augment panel. If you do not see the Augment panel press <Keyboard shortcut="Cmd/Ctrl L" />. If you are using Visual Studio Code, you be asked to confirm going to Augment's authentication portal.
  </Step>

  <Step title="Sign in with your email">
    In your browser, you may sign in with Google, Microsoft, or by receiving a single-use code in your email.
  </Step>

  <Step title="Accept the terms and conditions">
    If this is the first time you've signed in to Augment, you will be asked to accept the terms and conditions.
  </Step>

  <Step title="Return to your IDE">
    You will be automically redirected back to your IDE and you will see the Augment icon
    change to{" "}
    <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7564ed27ae27d8e8e8d37fc0c5390710" className="inline h-3 p-0 m-0" data-og-width="18" width="18" data-og-height="12" height="12" data-path="images/augment-icon-smile.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e768e602ba7fbca6dee54bd80707a65f 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2bff5c6e247ef06ee8c8aaf10b729fdb 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f137c3896e95e4ae83d7374bde6fce21 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=30c491bbedc2350eeac401d6bdb88a1d 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2b87100b107e7236c3c415c046fd988b 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a39dac81c0ae990b2c8143421f4144c5 2500w" /> in the status bar.
  </Step>

  <Step title="Sync your workspace">
    If this is your first time using Augment, or you are working on a new workspace, you will see the <Command text="Sync modal" /> in the Augment panel. Click the <Command text="Sync" /> button in the Augment panel to enable Augment's rich codebase awareness. See [Syncing your workspace](/setup-augment/workspace-indexing) to customize syncing behavior and learn more.
  </Step>
</Steps>

## Sign out

<Steps>
  <Step title="Show the Augment command menu">
    Press <Keyboard shortcut="Cmd/Ctrl Shift A" /> to show the Augment command menu.
  </Step>

  <Step title="Click Sign Out">Click <Command text="Sign Out" /> from the bottom of the commands menu.</Step>

  <Step title="You are now signed out of Augment">
    You will see the status bar icon change to orange and you will be signed out of Augment in all of your active workspaces.
  </Step>
</Steps>


# Allow Augment traffic from static IPs
Source: https://docs.augmentcode.com/setup-augment/static-ip-support

Locate Augment static IP addresses and configure firewalls, allowlists, and network policies for Augment Agent and its integrations.

Augment routes all outbound integration and remote-agent traffic through region specific static IP addresses. Add these IPs to your firewalls and allowlists when you need predictable source addresses for compliance or access control.

## When static IP support helps

**You likely need static IPs when**

* Your GitHub organization enforces IP allowlists.
* Internal APIs, artifact registries, or databases sit behind IP restricted networks.
* Corporate firewalls require a known source IP before allowing outbound agent traffic.
* You are connecting Augment remote agents to private cloud or on-prem systems.
* Compliance policies mandate tracking specific egress addresses.

**You probably do not need static IPs when**

* Integrated services such as GitHub, Linear, Slack, and others are accessible without IP restrictions.
* You only use Augment with SaaS tools that do not enforce IP allowlists.
* Your network does not block traffic based on source IP.

## Get the IP addresses for your region

<Callout type="info">
  Always perform the lookup from a network that mirrors the environment enforcing the allowlist so you can detect DNS filtering or caching differences.
</Callout>

### US region

```bash  theme={null}
dig +short us-static.augmentcode.com
```

### EU region

```bash  theme={null}
dig +short eu-static.augmentcode.com
```

The DNS record returns the exact set of IP addresses Augment uses for outbound traffic in that region. Addresses are stable, and repeated lookups should return the same list. Rerun the lookup periodically or set up monitoring so you are alerted if Augment adds new addresses.

## Add the IPs to common services

### GitHub Enterprise with IP restrictions

1. Run the lookup for your region.
2. In GitHub, open **Settings** -> **Security** -> **IP allow list**.
3. Add each Augment IP address with a clear description such as `Augment Agent`.

### Private artifact registries

Add the IP addresses to the allowlist for the registry host. For example, with a private npm registry include the addresses in the service configuration before agents pull packages.

### Corporate firewalls

1. Allow inbound traffic to your services from the Augment IP addresses.
2. Note the rules in your change management system for auditing.
3. Monitor firewall logs for denied connections from Augment IPs.

### API gateways

```yaml  theme={null}
apiVersion: networking.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-augment
spec:
  rules:
  - from:
    - source:
        ipBlocks:
        - "203.0.113.10/32"  # Replace with the Augment IPs you looked up
        - "203.0.113.11/32"
```

### Databases with IP allowlists

```sql  theme={null}
-- PostgreSQL pg_hba.conf example
host    all    augment_user    203.0.113.10/32    md5
host    all    augment_user    203.0.113.11/32    md5
```

## Implementation checklist

* Use the DNS entry for the region where your Augment deployment runs (`us-static` or `eu-static`).
* Document which services rely on Augment IPs and who owns the configuration.
* Limit access to only the systems Augment needs, following least privilege.
* Review and confirm allowlist entries during regular security audits.
* Configure alerts for DNS changes or repeated blocked traffic from Augment IPs.

## Troubleshooting

**If integrations stop working**

1. Rerun `dig +short <region>-static.augmentcode.com` and confirm the addresses match your allowlists.
2. Review firewall or service logs for blocked requests from Augment IPs.
3. Update the allowlist if any addresses changed or were missed.

**If DNS queries fail**

```bash  theme={null}
nslookup us-static.augmentcode.com
dig us-static.augmentcode.com A
dig us-static.augmentcode.com +noall +answer
```

Ensure local DNS resolvers can reach the Augment records and that caching layers are not serving stale results.

## Need help?

Contact Augment Support with your region, the affected integrations, and relevant firewall or allowlist details so the team can help you validate the configuration.


# Secrets Manager
Source: https://docs.augmentcode.com/setup-augment/user-secrets

Securely store and manage secrets for your development environment, including API keys, tokens, and credentials.

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

<Availability tags={["vscode"]} />

The Secrets Manager allows you to securely store and manage user-defined secrets that can be used in your development environment. It supports two types of secrets: **Environment Variables** and **Mounted Files**.

## Overview

The Secrets Manager provides a secure way to store sensitive information like API keys, database credentials, and configuration secrets. All secrets are encrypted and stored securely, with automatic redaction in logs to prevent accidental exposure.

## Accessing the Secrets Manager

Open the Settings Panel (gear icon in the Augment panel) and navigate to the **Secrets** section to manage your secrets.

## Secret Types

### Environment Variables

Environment variables are injected into your development environment and accessible via standard environment variable access patterns.

**Use cases:**

* API keys (GitHub tokens, OpenAI keys)
* Database connection strings
* Service endpoints
* Configuration flags

**How they work:**

* Secrets are made available as environment variables in your workspace
* Generated profile script at `/etc/profile.d/15-augment-secrets.sh`
* Automatically loaded in shell sessions

### Mounted Files

Mounted files are stored as actual files in your workspace filesystem at specified paths.

**Use cases:**

* SSH private keys
* Certificate files
* Configuration files
* Large secret content

**How they work:**

* Files are mounted to `/run/augment_secrets/` by default
* You specify the mount path when creating the secret
* Files are accessible via standard filesystem operations

## Security Features

* Secret values are never displayed by default
* All secret values are redacted in logs
* Each user can only access their own secrets

## Limits and Quotas

| Limit                | Default Value  |
| -------------------- | -------------- |
| Max secrets per user | 100            |
| Max secret size      | 4KB            |
| Max name length      | 255 characters |
| Max tags per secret  | 50             |

## Security Best Practices

1. **Use descriptive names**: Make secret purposes clear without exposing sensitive info
2. **Regular cleanup**: Remove unused secrets to minimize exposure
3. **Avoid logging values**: The system automatically redacts secrets in logs
4. **Use appropriate type**: Choose environment variables for simple values, mounted files for complex content


# Keyboard Shortcuts for Visual Studio Code
Source: https://docs.augmentcode.com/setup-augment/vscode-keyboard-shortcuts

Augment integrates with your IDE to provide keyboard shortcuts for common actions. Use these shortcuts to quickly accept suggestions, write code, and navigate your codebase.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## About keyboard shortcuts

Augment is deeply integrated into your IDE and utilizes many of the standard keyboard shortcuts you are already familiar with. These shortcuts allow you to quickly accept suggestions, write code, and navigate your codebase. We also suggest updating a few keyboard shortcuts to make working with code suggestions even easier.

<Tabs>
  <Tab title="MacOS">
    To update keyboard shortcuts, use one of the following:

    | Method          | Action                                                                                                  |   |
    | :-------------- | :------------------------------------------------------------------------------------------------------ | - |
    | Keyboard        | <Keyboard shortcut="Cmd K" /> then <Keyboard shortcut="Cmd S" />                                        |   |
    | Menu bar        | <Command text="Code > Settings... > Keyboard Shortcuts" />                                              |   |
    | Command palette | <Keyboard shortcut="Cmd Shift P" /> then search <Command text="Preferences: Open Keyboard Shortcuts" /> |   |

    ## General

    | Action                | Recommended shortcut                |
    | :-------------------- | :---------------------------------- |
    | Open Augment panel    | <Keyboard shortcut="Cmd L" />       |
    | Show Augment commands | <Keyboard shortcut="Cmd Shift A" /> |

    ## Chat

    | Action                   | Default shortcut              |
    | :----------------------- | :---------------------------- |
    | Focus or open Chat panel | <Keyboard shortcut="Cmd L" /> |

    ## Next Edit

    | Action            | Default shortcut                    |
    | :---------------- | :---------------------------------- |
    | Go to next        | <Keyboard shortcut="Cmd ;" />       |
    | Go to previous    | <Keyboard shortcut="Cmd Shift ;" /> |
    | Accept suggestion | <Keyboard shortcut="Enter" />       |
    | Reject suggestion | <Keyboard shortcut="Backspace" />   |

    ## Instructions

    | Action            | Default shortcut               |
    | :---------------- | :----------------------------- |
    | Start instruction | <Keyboard shortcut="Cmd I" />  |
    | Accept            | <Keyboard shortcut="Return" /> |
    | Reject            | <Keyboard shortcut="Esc" />    |

    ## Completions

    | Action                         | Default keyboard shortcut              |
    | :----------------------------- | :------------------------------------- |
    | Accept inline suggestion       | <Keyboard shortcut="Tab" />            |
    | Accept next word of suggestion | <Keyboard shortcut="Cmd →" />          |
    | Accept next line of suggestion | None (see below)                       |
    | Reject suggestion              | <Keyboard shortcut="Esc" />            |
    | Ignore suggestion              | Continue typing through the suggestion |
    | Toggle automatic completions   | <Keyboard shortcut="Cmd Option A" />   |

    **Recommended shortcuts**

    We recommend updating your keybindings to include the following shortcuts to
    make working with code suggestions even easier. These changes update the
    default behavior of Visual Studio Code.

    | Action                         | Recommended shortcut               |
    | :----------------------------- | :--------------------------------- |
    | Accept next line of suggestion | <Keyboard shortcut="Cmd Ctrl →" /> |
  </Tab>

  <Tab title="Windows/Linux">
    To update keyboard shortcuts, use one of the following:

    | Method          | Action                                                                                                   |
    | :-------------- | :------------------------------------------------------------------------------------------------------- |
    | Keyboard        | <Keyboard shortcut="Ctrl K" /> then <Keyboard shortcut="Ctrl S" />                                       |
    | Menu bar        | <Command text="File > Settings... > Keyboard Shortcuts" />                                               |
    | Command palette | <Keyboard shortcut="Ctrl Shift P" /> then search <Command text="Preferences: Open Keyboard Shortcuts" /> |

    ## General

    | Action                | Recommended shortcut                 |
    | :-------------------- | :----------------------------------- |
    | Open Augment panel    | <Keyboard shortcut="Ctrl L" />       |
    | Show Augment commands | <Keyboard shortcut="Ctrl Shift A" /> |

    ## Chat

    | Action                   | Default shortcut               |
    | :----------------------- | :----------------------------- |
    | Focus or open Chat panel | <Keyboard shortcut="Ctrl L" /> |

    ## Next Edit

    | Action            | Default shortcut                     |
    | :---------------- | :----------------------------------- |
    | Go to next        | <Keyboard shortcut="Ctrl ;" />       |
    | Go to previous    | <Keyboard shortcut="Ctrl Shift ;" /> |
    | Accept suggestion | <Keyboard shortcut="Enter" />        |
    | Reject suggestion | <Keyboard shortcut="Backspace" />    |

    ## Instructions

    | Action            | Default shortcut               |
    | :---------------- | :----------------------------- |
    | Start instruction | <Keyboard shortcut="Ctrl I" /> |
    | Accept            | <Keyboard shortcut="Return" /> |
    | Reject            | <Keyboard shortcut="Esc" />    |

    ## Completions

    | Action                         | Default keyboard shortcut              |
    | :----------------------------- | :------------------------------------- |
    | Accept inline suggestion       | <Keyboard shortcut="Tab" />            |
    | Accept next word of suggestion | <Keyboard shortcut="Ctrl →" />         |
    | Accept next line of suggestion | None (see below)                       |
    | Reject suggestion              | <Keyboard shortcut="Esc" />            |
    | Ignore suggestion              | Continue typing through the suggestion |
    | Toggle automatic completions   | <Keyboard shortcut="Ctrl Alt A" />     |

    **Recommended shortcuts**

    We recommend updating your keybindings to include the following shortcuts to
    make working with code suggestions even easier. These changes update default
    behavior of Visual Studio Code.

    | Action                         | Recommended shortcut               |
    | :----------------------------- | :--------------------------------- |
    | Accept next line of suggestion | <Keyboard shortcut="Ctrl Alt →" /> |
  </Tab>
</Tabs>


# Add context to your workspace
Source: https://docs.augmentcode.com/setup-augment/workspace-context-vscode

You can add additional context to your workspace–such as additional repositories and folders–to give Augment a full view of your system.

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

export const Command = ({text}) => <span className="font-bold">{text}</span>;

<Availability tags={["vscode",]} />

## About Workspace Context

Augment is powered by its deep understanding of your code. Sometimes important parts of your system exist outside of the current workspace you have open in your IDE. For example, you may have seperate frontend and backend repositories or have many services across multiple repositories. Adding additional context to your workspace will improve the code suggestions and chat responses from Augment.

## View Workspace Context

To view your Workspace Context, click the folder icon <Icon icon="folder-open" iconType="light" /> in the top right corner of the Augment sidebar panel.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=50de98aea1e300bb9386bf282cbe4581" alt="Workspace Context" className="rounded-xl" data-og-width="1156" width="1156" data-og-height="1009" height="1009" data-path="images/workspace-context.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3c66cf05f83956fad54a4d810fafb6b1 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=addf63bc42ae43d1747e74fd2d5c9fae 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=bc898ce5c72a8b07eb4ad378e312143b 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3566538a797b7b20fe288ea712ce3d48 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=01ef280a41d8cec96c771921b56dce17 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/workspace-context.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=16e11c1644cf33c6c255cac488c0eebe 2500w" />

## Add context to your workspace

To add context to your workspace, click <Command text="+ Add more..." /> at the bottom of the Source Folders section of the context manager. From the file browser select the folders you want to add to your workspace context and click <Command text="Add Source Folder" />.

## View sync status

When viewing Workspace Context, each file and folder will have an icon that indicates whether its sync status. The following icons indicate the sync status of each file in your workspace:

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Indicator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Status                                  |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------- |
|                                         <img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=83948590ef25800a8cf40c747c28b133" className="inline h-4 p-0 m-0" data-og-width="12" width="12" data-og-height="12" height="12" data-path="images/wsc-included.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=9978e5ee6258d59409574de8a746c855 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b245408a2887e5bf6844291c823ca78f 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=8076411a27ab25d56766bcce44ecda61 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a37b507ac4b71643cf77243b614a617e 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=8f9084eacaa10f33d5661907bcbcbf53 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-included.svg?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=d1dd1a289906e0bc0552624154dfede1 2500w" />                                         | Synced, or sync in progress             |
|                                         <img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e5a93c810f94d3d3db90b8984239699b" className="inline h-4 p-0 m-0" data-og-width="12" width="12" data-og-height="12" height="12" data-path="images/wsc-excluded.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=77728337572736aa0ac1c435428fcbb2 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=f875fd61db9c659377ac1b9ee9619e58 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=cd429e91f5b30345ca00d86b08b3b567 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=decd20244fdee2f81f1a7b6312081593 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1b09eebbc378320277e85fe780526f98 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-excluded.svg?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a811d1132ea0a90e117a9b85823ef9f6 2500w" />                                         | Not synced                              |
| <img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=892115c2ab50b9d2f8261f78abf89283" className="inline h-4 p-0 m-0" data-og-width="12" width="12" data-og-height="12" height="12" data-path="images/wsc-partially-included.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ad70bb3c5d05b9098387e29e1e45080f 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=911e14ce3e65aa57b175edff60b29a5b 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=6d5fa527bbaa111002ac3e8b864793c3 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=d3c65bea8eb987dfced8d8d06ea6aa7a 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=9f8e5409a71df31ee126394fbed5ddd7 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/wsc-partially-included.svg?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b311b9ab4b2c686f5ed292c9423c2744 2500w" /> | Some files within the folder are synced |


# Index your workspace
Source: https://docs.augmentcode.com/setup-augment/workspace-indexing

When your workspace is indexed, Augment can provide tailored code suggestions and answers based on your unique codebase, best practices, coding patterns, and preferences. You can always control what files are indexed.

## About indexing your workspace

When you open a workspace with Augment enabled, your codebase will be automatically uploaded to Augment's secure cloud. You can control what files get indexed using `.gitignore` and `.augmentignore` files. Indexing usually takes less than a minute but can take longer depending on the size of your codebase. In Visual Studio Code, you can use Workspace Context to [view what files are indexed](/setup-augment/workspace-context-vscode#view-index-status-in-visual-studio-code) and [add additional context](/setup-augment/workspace-context-vscode#add-context-to-your-workspace).

## Security and privacy

Augment stores your code securely and privately to enable our powerful context engine. We ensure code privacy through a proof-of-possession API and maintain strict internal data minimization principles. [Read more about our security](https://www.augmentcode.com/security).

## What gets indexed

Augment will index all the files in your workspace, except for the files that match patterns in your `.gitignore` file and the `.augmentignore` file. You can [view what files are indexed](/setup-augment/workspace-context-vscode#view-sync-status-in-visual-studio-code) in Workspace Context.

## Ignoring files with .augmentignore

The `.augmentignore` file is a list of file patterns that Augment will ignore when indexing your workspace. Create an `.augmentignore` file in the root of your workspace. You can use any glob pattern that is supported by the [gitignore](https://git-scm.com/docs/gitignore) file.

## Including files that are .gitignored

If you have a file or directory in your `.gitignore` that you want to indexed, you can add it to your `.augmentignore` file using the `!` prefix.

For example, you may want your `node_modules` indexed to provide Augment with context about the dependencies in their project, but it is typically included in their `.gitignore`. Add `!node_modules` to your `.augmentignore` file.

<CodeGroup>
  ```bash .augmentignore theme={null}
  # Include .gitignore excluded files with ! prefix
  !node_modules

  # Exclude other files with .gitignore syntax
  data/test.json
  ```

  ```bash .gitignore theme={null}
  # Exclude dependencies
  node_modules

  # Exclude secrets
  .env

  # Exclude build artifacts
  out
  build
  ```
</CodeGroup>


# Using Teams
Source: https://docs.augmentcode.com/teams/teams-admin-guide

Use Teams to collect individual Augment Code accounts (either Indie or Developer) into a Team. Once established you can bundle billing for your organization.

## About Teams

If multiple people from your organization use Augment Code through our [Indie or Developer plan](https://augmentcode.com/pricing), Teams gathers accounts together for better collaboration. Teams simplify account management, offer better access control and centralize billing. Team administrators have special privileges to invite members, manage seats, change plans, and control team settings. Teams are not available for Enterprise plans since this plan by defaults groups the entire organization.

<Note>
  Team settings and billing management are only accessible to accounts assigned as the administrator. Individual team members can view team information but cannot modify settings or manage subscriptions. To change which account is set as the administrator, contact [Augment Code Support](https://portal.usepylon.com/augment-code/forms/augment-support)
</Note>

## Team Roles and Permissions

### Administrator Role

* Can invite new team members or cancel pending invitations
* Can remove team members
* Can manage team seats (increase/decrease)
* Can change team plans
* Can view and manage billing information

### Member Role

* Can view team information
* Can leave the team (remove themselves)
* Cannot invite or remove other members
* Cannot manage billing or change plans

## Adding Team Members

To add team members, you must be an administrator with available seats on your plan.

1. **Navigate to Team from Account** - Go to your [Account](https://app.augmentcode.com/account/), and then select the "Team" tab

2. **Initiate Invitation** - Click "Add team member," enter the email address, and click "Send invitation"

3. **Invitation Status** - The invitation appears as "Pending" in your team members list and counts toward your seat allocation

4. **Acceptance** - The invitee receives an email with instructions to join. Once they authenticate with their Augment account (or create one), they become an active team member

<Note>
  Invitations expire after 7 days. Pending invitations can be cancelled before acceptance. If your team is at capacity, add more seats before inviting new members. You can send multiple invitations simultaneously using comma-separated emails.
</Note>

## Removing Team Members

To remove team members, you must be an administrator. Members can also remove themselves from a team.

1. **Navigate to Team from Account** - Go to your [Account](https://app.augmentcode.com/account/), select the "Team" tab, and find the member you want to remove

2. **Remove Member** - Click the three-dot menu (⋮) next to the member's name, select "Remove Member," and confirm the removal

3. **After Removal** - The member immediately loses access to team resources and their account reverts to individual status. For paid plans, the seat becomes available at the next billing cycle.

<Note>
  Leaving? [Ask Augment Code Support](https://support.augmentcode.com/) to grant administrator access to another account before removing yourself if you're the only administrator.
</Note>

### Cancelling Pending Invitations

To cancel a pending invitation, navigate to the team members list, filter by "Pending" status, click the three-dot menu next to the pending invitation, and select "Cancel Invitation."

## Managing Team Plans and Subscriptions

Augment offers flexible plans to meet your team's needs. Visit [augmentcode.com/pricing](https://augmentcode.com/pricing) for current plan options and pricing.

### Changing Plans

To change your team's plan, you must be a team administrator with a valid payment method for paid plans.

1. **Access Plan Selection** - Go to [Account](https://app.augmentcode.com/account/) then select Subscription and click "Change Plan" or "Upgrade"

2. **Select New Plan** - Review available plans, pricing, and included features for your team size

3. **Configure Details** - Set the number of seats needed and review pricing calculations

4. **Confirm** - Add or update your payment method if needed, review prorated charges or credits, and confirm the plan change

<Note>
  Plan changes may be immediate (upgrades, free to paid, trial to paid) or take effect at the end of your billing cycle (downgrades). Prorated charges and credits are calculated automatically for mid-cycle changes.
</Note>

### Managing Seats

**Adding Seats**

1. **Navigate to Team Settings** - Go to [Account](https://app.augmentcode.com/account/) then the Team tab and click "Manage Seats"

2. **Increase Seat Count** - Use the number control to increase seats and review the new monthly cost

3. **Save Changes** - Click "Save changes" to confirm. Additional seats are billed immediately (prorated) and the new monthly rate takes effect immediately

**Removing Seats**

1. **Check Current Usage** - Ensure you have unused seats. You cannot reduce seats below your active members plus pending invitations

2. **Decrease Seat Count** - Navigate to "Manage Seats," reduce the number using the control, and save changes

3. **Billing Impact** - Removed seats remain active until the next billing cycle. Credits are applied at the next billing period

## Troubleshooting

**Cannot add members - no seats available**

* Purchase additional seats or remove inactive members
* Cancel pending invitations to free up seat allocation

**Payment method required**

* Add a valid credit card in Account > Billing
* Ensure your payment method is not expired
* Contact support for payment issues

**Cannot remove last admin**

* Promote another member to admin first before removing yourself

**Invitation expired**

* Resend the invitation from the Team tab
* Verify the correct email address was used
* Check spam folders for the invitation email

For additional help, contact [Support](https://portal.usepylon.com/augment-code/forms/augment-support) or visit [docs.augmentcode.com](https://docs.augmentcode.com).

## Best Practices

**Regular Audits** - Review team membership monthly, remove inactive members promptly, and monitor seat utilization to optimize costs.

**Invitation Management** - Verify email addresses before sending invitations and follow up with invitees directly. Cancel unaccepted invitations after 48 hours to free up seats.

**Billing Optimization** - Right-size your seat count and plan seat changes for billing cycle boundaries to avoid prorated charges.

**Security** - Remove members immediately upon departure, regularly review admin permissions, and use company email addresses for all team members.


# Feedback
Source: https://docs.augmentcode.com/troubleshooting/feedback

We love feedback, and want to hear from you. We want to make the best AI-powered code assistant so you can get more done.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

Feedback helps us improve, and we encourage you to share your feedback on every aspect of using Augment—from suggestion and chat response quality, to user experience nusances, and even how we can improve getting your feedback.

### Reporting a bug

To report a bug, please [contact support](https://support.augmentcode.com/). Include as much detail to reproduce the problem as possible; screenshots and videos are very helpful.

### Feedback on completions

We are always balancing the needs for speed and accuracy. We want to know when you get a poor suggestion, hallucination, or a completion that actually doesn't work. The History panel has a log of all of your completions; we encourage you to use it to send us feedback on the completions you've received.

<Note>
  Providing feedback directly in your IDE through the History panel is currently
  only available in Visual Studio Code.
</Note>

<Steps>
  <Step title="Open the History panel">
    Open the History panel by pressing <Keyboard shortcut="Cmd/Ctrl Shift P" />
    and then searching for `Augment: Show History` in the command menu.
  </Step>

  <Step title="Find the completion you want to report">
    Recent completions are listed in reverse chronological order. Locate the
    completion you want to report and add complete the feedback form.
  </Step>

  <Step title="Submit your feedback">
    After completing the form, click either the red button for bad completions
    or the green button for good completions.
  </Step>
</Steps>

### Feedback on chat

After each Chat interaction, you have the opportunity to provide feedback on the quality of the response. At the bottom of the response click either the thumbs up <Icon icon="thumbs-up" iconType="light" /> or thumbs down <Icon icon="thumbs-down" iconType="light" /> icon. Add additional information in the feedback field, and click `Send Feedback`.


# Jetbrains UI issues
Source: https://docs.augmentcode.com/troubleshooting/jetbrains-rendering-issues

Fix issues where the Augment panel is white, blank or not showing anything in JetBrains IDEs.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About UI issues in JetBrains IDEs

Some users on newer versions of JetBrains IDEs (2025.1 and above) have reported that the Augment panel is white, blank or not
displaying anything at all. These issues stem from a change to the way JetBrains renders webviews, which is now
done in an out-of-process manner. Disabling out-of-process rendering has resolved a number of problems for users.

This is a known issue that impacts multiple plugins in the Jetbrains ecosystem. JetBrains is tracking the issue in IJPL-186252.

**Note**: If you are using a **JetBrains IDE 2025.2.3 on Windows**, we do not recommend disabling out-of-process rendering due
to a bug where the WebViews will render JS and CSS in plain text making it difficult to use Augment and any other WebViews. There
is a workaround for this issue <a href="https://youtrack.jetbrains.com/issue/JBR-9462/Markdown-rendering-broken-with-ide.browser.jcef.out-of-process.enabledfalse-after-upgrading-to-PyCharm-2025.2.3#focus=Comments-27-12792022.0-0">described here</a>.

If you experience issues after following the steps below, please [contact support](https://support.augmentcode.com/)
for further assistance.

### Disable out-of-process rendering

<Steps>
  <Step title="Open the Custom Properties editor">
    From the menu bar, go to <Command text="Help > Edit Custom Properties..." />. If the `idea.properties` file doesn't exist yet, you'll be prompted to create it.
  </Step>

  <Step title="Add the out-of-process rendering property">
    Add the following line to the properties file:

    ```
    ide.browser.jcef.out-of-process.enabled=false
    ```
  </Step>

  <Step title="Save and restart your IDE">
    Save the file and restart your JetBrains IDE for the changes to take effect.
  </Step>
</Steps>

After restarting, the Augment panel should render more consistently.


# Jetbrains panel steals focus
Source: https://docs.augmentcode.com/troubleshooting/jetbrains-stealing-focus

Fix issue where the Augment panel takes focus while typing in JetBrains IDEs.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About focus issues in JetBrains IDEs

Some users on Linux systems have reported that the Augment Chat window steals focus from the editor while typing. This can interrupt your workflow and make it difficult to use the IDE effectively. This issue can be resolved by enabling off-screen rendering in your JetBrains IDE.

### Enable off-screen rendering

<Steps>
  <Step title="Open the Custom Properties editor">
    From the menu bar, go to <Command text="Help > Edit Custom Properties..." />. If the `idea.properties` file doesn't exist yet, you'll be prompted to create it.
  </Step>

  <Step title="Add the off-screen rendering property">
    Add the following line to the properties file:

    ```
    augment.off.screen.rendering=true
    ```
  </Step>

  <Step title="Save and restart your IDE">
    Save the file and restart your JetBrains IDE for the changes to take effect.
  </Step>
</Steps>

After restarting, the Augment panel should no longer steal focus from the editor while you're typing.


# Request IDs
Source: https://docs.augmentcode.com/troubleshooting/request-id

Request IDs are generated with every code suggestion and chat interaction. Our team may ask you to provide the request ID when you report a bug or issue.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## Finding a Request ID for Chat

<Steps>
  <Step title="Open the Chat panel">
    Open the Chat panel by clicking the Augment icon{" "}

    <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5a70e197b4ab16c79e9612aac74015cf" className="inline h-4 p-0 m-0" data-og-width="676" width="676" data-og-height="592" height="592" data-path="images/augment-icon-chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2a32c9463cef1c6647f0dd08dd827cd2 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4cba744eb472e888403e462429f3c10a 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c8393d6a3463c6e6a99eca871d66ae67 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=573abbe9afb002028f79741b4fa4bad4 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=998af121c45992d4121b3fb97ee42007 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=aa776a96f49e4d86cb0a0d7cef78cc67 2500w" />

    {" "}

    in the action bar on the left side of your editor.
  </Step>

  <Step title="Open the chat thread">
    If the chat reply you are interested is in a previous chat thread, find the
    chat thread by clicking the <Icon icon="chevron-right" /> at the top of the
    chat panel and clicking the relevant chat thread.
  </Step>

  <Step title="Find the request ID">
    Find the reply in question and click the <Icon icon="link-simple" /> icon
    above the reply to copy the request ID to your clipboard.
  </Step>
</Steps>

## Finding a Request ID for Completions

<Steps>
  <Step title="Open the History panel">
    Open the History panel by pressing <Keyboard shortcut="Cmd/Ctrl Shift P" />
    and then searching for `Augment: Show History` in the command menu.
  </Step>

  <Step title="Find the request ID">
    Recent requests are listed in reverse chronological order. Locate the
    request you are interested in and copy the request ID by clicking on the
    request ID, for example:
    <br /> `-- Request ID: 7f67c0dd-4c80-4167-9383-8013b18836cb`
  </Step>
</Steps>


# Using Agent
Source: https://docs.augmentcode.com/using-augment/agent

Use Agent to complete simple and complex tasks across your workflow–implementing a feature, upgrade a dependency, or writing a pull request.

export const type_0 = "changes"

export const AtIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M480.39-96q-79.52 0-149.45-30Q261-156 208.5-208.5T126-330.96q-30-69.96-30-149.5t30-149.04q30-69.5 82.5-122T330.96-834q69.96-30 149.5-30t149.04 30q69.5 30 122 82.5t82.5 122Q864-560 864-480v60q0 54.85-38.5 93.42Q787-288 732-288q-34 0-62.5-17t-48.66-45Q593-321 556.5-304.5T480-288q-79.68 0-135.84-56.23-56.16-56.22-56.16-136Q288-560 344.23-616q56.22-56 136-56Q560-672 616-615.84q56 56.16 56 135.84v60q0 25.16 17.5 42.58Q707-360 732-360t42.5-17.42Q792-394.84 792-420v-60q0-130-91-221t-221-91q-130 0-221 91t-91 221q0 130 91 221t221 91h192v72H480.39ZM480-360q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35Z" />
    </svg>
  </div>;

## About Agent

Augment Agent is a powerful tool that can help you complete software development tasks end-to-end. From quick edits to complete feature implementation, Agent breaks down your requests into a functional plan and implements each step all while keeping you informed about what actions and changes are happening. Powered by Augment's Context Engine and powerful LLM architecture, Agent can write, document, and test like an experienced member of your team.

## Accessing Agent

To access Agent, simply open the Augment panel and select one of the Agent modes from the drop down in the input box.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=51d70e49f675669435e22fa95a1451bc" alt="Augment Agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="434" height="434" data-path="images/agent-selector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bf58d45da80eb95ddc3aa478add24e5c 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a44992db36a19f1f6a853691c1fd5967 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=509265e75111915c1c542fa32a22471b 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=925e22b37cb18461397e64cdcb040cc2 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=94acc730b73f331885b659dbe623d6f7 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a8bcace31c370f0fcef0946d06b96efd 2500w" />

### Choosing a model

Use the model dropdown in the Augment panel to switch between models. Your selection applies only to Agent for the current workspace and can be changed at any time. See [Available Models](/models/available-models) for details.

## Using Agent

To use Agent, simply type your request into the input box using natural language and click the submit button. You will see the default context including current workspace, current file, and Agent memories. You can add additional context by clicking <AtIcon />and selecting files or folder, or add an image as context by clicking the paperclip. Agent can create, edit, or delete code across your workspace and can use tools like the terminal and external integrations through MCP to complete your request.

### Enhancing your prompt

You can improve the quality of your {type_0} by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

### Reviewing changes

You can review every change Agent makes by clicking on the action to expand the view. Review diffs for file changes, see complete terminal commands and output, and the results of external integration calls.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bab5fc7aed7f83ae499c9b5d72dfd03a" alt="Augment Agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="543" height="543" data-path="images/agent-edit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d0ba25bfbf7579dc11e03c5c610f5f9b 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=24afe8b62ccaf04b7b8a38541c94eb7b 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cc170722a8152fada50217b03c08c013 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=71ebbaa901d3740c0be592f243a47931 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a7befc70fed705adaa44a9af3b178134 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b847e3015c2963f15a77f3e2b648086b 2500w" />

### Checkpoints

Checkpoints are automatically saved snapshots of your workspace as Agent implements the plan allowing you to easily revert back to a previous step. This enables Agent to continue working while you review code changes and commands results. To revert to a previous checkpoint, click the reverse arrow icon to restore your code.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b74e713d55dd365ea383f4b16dc88205" alt="Augment Agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="286" height="286" data-path="images/agent-checkpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=0def9b44ce305366ba2f7abb482016a0 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=15298f09b3179ef13437e8db0ff91174 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2cbde4f2c5522158a42c118c7dac95e5 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=1fbac8a7522674beab6176e0f04ac9c4 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=25b1363f04cd1d2e3f006db4fdd2f7a5 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=0d6b3f3786360d920c167c9c8147e34d 2500w" />

### Agent memories

Memories help the Agent remember important details about your workspace and your preferences for working in it. Memories are stored locally and are applied to all Agent requests. Memories can be added automatically by Agent, by clicking the remember button under a message, asking Agent to remember something, or by editing the Memories files directly.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6c97e0962bf72ab46c4a121a6d60496c" alt="Stopping the agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="377" height="377" data-path="images/agent-memories.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f6c7fe852e448fe202b7e537f7687048 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e77d425d2cd9218c11b6e7f8be78e074 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4709bd2e26af695ff79e5751acc37e61 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e9ccb06085be6101caa2690c3180ea01 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ad9abafab8116ecee267db387a9c3c0a 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7306c0ea821e5129728993a0eb20b76a 2500w" />

### Agent vs Agent Auto

By default, Agent will pause work when it needs to execute a terminal command or access external integrations. After reviewing the suggested action, click the blue play button to have Agent execute the command and continue working. You tell Agent to skip a specific action by clicking on the three dots and then Skip.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5c528efde3b96da6711dcecdda312294" alt="Augment Agent" className="rounded-xl" data-og-width="1212" width="1212" data-og-height="373" height="373" data-path="images/agent-approval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6c5d2c65451676c4ab78e6835ec64451 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=74f3b29a19c5d3dedb4d9cf7cd4c15e8 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7099350faa1efcc52f0d17534e747438 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ec6fe85dcb06538d1b4b2817e95c977c 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e2d66bbcf048da6d3783c5b247164002 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=68093b6342af74a4aa90d521b1cd2a3a 2500w" />

In Agent Auto, Agent will act more independently. It will edit files, execute terminal commands, and access tools like MCP servers automatically.

### Stop or guide the Agent

You can interrupt the Agent at any time by clicking Stop. This will pause the action to allow you to correct something you see the agent doing incorrectly. While Agent is working, you can also prompt the Agent to try a different approach which will automatically stop the agent and prompt it to correct its course.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3c195714aa08f74acb9d63a354acdc99" alt="Stopping the agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="551" height="551" data-path="images/agent-stop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ee1b6bd049826fbd882ce234e91b8d76 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=0bb16c7d3efaf8e03e971c6ee7b8a470 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cd99b327ca87dd7e5df6671dab20594e 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4ab045596b20e4d325ba655179e98338 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ea995fe1122a55d05ea67bd99b4b51d5 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=280d36fadf5a41fa8d777be4ac1e4a96 2500w" />

### Quick Ask Mode

Quick Ask Mode is a toggle button in the agent chat interface that restricts the AI to read-only tools only. When activated, it adds a visual badge to the message and focuses the AI on information gathering without making any changes to your codebase.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/ask-mode.gif?s=c2c554fd010bb15d8267de15ad4f9dc5" alt="Quick Ask Mode toggle and usage" className="rounded-xl" data-og-width="800" width="800" data-og-height="450" height="450" data-path="images/ask-mode.gif" data-optimize="true" data-opv="3" />

### Comparison to Chat

Agent takes Chat to the next level by allowing Augment to do things for you-that is create and make modifications directly to your codebase. Chat can explain code, create plans, and suggest changes which you can smartly apply one-by-one, but Agent takes it a step further by automatically implementing the entire plan and all code changes for you.

| What are you trying to do?                       | Chat | Agent |
| :----------------------------------------------- | :--: | :---: |
| Ask questions about your code                    |  ☑️  |   ✅   |
| Get advice on how to refactor code               |  ☑️  |   ✅   |
| Add new features to selected lines of code       |  ☑️  |   ✅   |
| Add new feature spanning multiple files          |      |   ✅   |
| Document new features                            |      |   ✅   |
| Queue up tests for you in the terminal           |      |   ✅   |
| Open Linear tickets or start a pull request      |      |   ✅   |
| Start a new branch in GitHub from recent commits |      |   ✅   |
| Automatically perform tasks on your behalf       |      |   ✅   |

### Use cases

Use Agent to handle various aspects of your software development workflow, from simple configuration changes to complex feature implementations. Agent supports your daily engineering tasks like:

* **Make quick edits** - Create a pull request to adjust configuration values like feature flags from FALSE to TRUE
* **Perform refactoring** - Move functions between files while maintaining coding conventions and ensuring bug-free operation
* **Start a first draft for new features** - Start a pull request (PR) with implementing entirely new functionality straight from a GitHub Issue or Linear Ticket
* **Branch from GitHub** - Open a PR from GitHub based on recent commits that creates a new branch
* **Query Supabase tables directly** - Ask Agent to view the contents of a table
* **Start tickets in Linear or Jira** - Open tickets and ask Agent to suggest a plan to address the ticket
* **Add Pull Request descriptions** - Merge your PR into a branch then tell the agent to explain what the changes are and why they were made
* **Create test coverage** - Generate unit tests for your newly developed features
* **Generate documentation** - Produce comprehensive documentation for your libraries and features
* **Start a README** - Write a README for a new feature or updated function that you just wrote
* **Track development progress** - Review and summarize your recent Git commits for better visibility with the GitHub integration

## Next steps

* [Configure Agent Integrations](/setup-augment/agent-integrations)
* [Configure other tools with MCP](/setup-augment/mcp)


# Using Chat
Source: https://docs.augmentcode.com/using-augment/chat

Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

export const type_0 = "chats"

export const DeleteIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm400-600H280v520h400v-520ZM360-280h80v-360h-80v360Zm160 0h80v-360h-80v360ZM280-720v520-520Z" />
    </svg>
  </div>;

export const ChevronRightIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z" />
    </svg>
  </div>;

export const NewChatIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M120-160v-600q0-33 23.5-56.5T200-840h480q33 0 56.5 23.5T760-760v203q-10-2-20-2.5t-20-.5q-10 0-20 .5t-20 2.5v-203H200v400h283q-2 10-2.5 20t-.5 20q0 10 .5 20t2.5 20H240L120-160Zm160-440h320v-80H280v80Zm0 160h200v-80H280v80Zm400 280v-120H560v-80h120v-120h80v120h120v80H760v120h-80ZM200-360v-400 400Z" />
    </svg>
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Chat

Chat is a new way to work with your codebase using natural language. Chat will automatically use the current workspace as context and you can [provide focus](/using-augment/chat-context) for Augment by selecting specific code blocks, files, folders, or external documentation. Details from your current chat, including the additional context, are used to provide more relevant code suggestions as well.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d375d6ded40f6ed3353e002a9d9fa7a0" alt="Augment Chat" className="rounded-xl" data-og-width="1120" width="1120" data-og-height="1209" height="1209" data-path="images/chat-explain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=72a74689a8d1160c2ec3831e752cb266 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=559d3b76f96a2df576305440cf5c241e 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=48570a3aa134abe6d23ec6c8cfa5e314 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d175cf3cfaa04e1e9de9d2894d91ecc3 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7cfebd57e867659d7e847fbd25d3b207 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a197d0a8fe4e010828796d78d172d43e 2500w" />

## Accessing Chat

Access the Chat sidebar by clicking the Augment icon <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5a70e197b4ab16c79e9612aac74015cf" className="inline h-4 p-0 m-0" data-og-width="676" width="676" data-og-height="592" height="592" data-path="images/augment-icon-chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2a32c9463cef1c6647f0dd08dd827cd2 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4cba744eb472e888403e462429f3c10a 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c8393d6a3463c6e6a99eca871d66ae67 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=573abbe9afb002028f79741b4fa4bad4 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=998af121c45992d4121b3fb97ee42007 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=aa776a96f49e4d86cb0a0d7cef78cc67 2500w" /> in the sidebar or the status bar. You can also open Chat by using one of the keyboard shortcuts below.

**Keyboard Shortcuts**

| Platform      | Shortcut                       |
| :------------ | :----------------------------- |
| MacOS         | <Keyboard shortcut="Cmd L" />  |
| Windows/Linux | <Keyboard shortcut="Ctrl L" /> |

## Using Chat

To use Chat, simply type your question or command into the input field at the bottom of the Chat panel. You will see the currently included context which includes the workspace and current file by default. Use Chat to explain your code, investigate a bug, or use a new library. See [Example Prompts for Chat](/using-augment/chat-prompts) for more ideas on using Chat.

### Conversations about code

To get the best possible results, you can go beyond asking simple questions or commands, and instead have a back and forth conversation with Chat about your code. For example, you can ask Chat to explain a specific function and then ask follow-up questions about possible refactoring options. Chat can act as a pair programmer, helping you work through a technical problem or understand unfamiliar code.

### Enhancing your prompt

You can improve the quality of your {type_0} by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

### Starting a new chat

You should start a new Chat when you want to change the topic of the conversation since the current conversation is used as part of the context for your next question. To start a new chat, open the Augment panel and click the new chat icon <NewChatIcon /> at the top-right of the Chat panel.

### Previous chats

You can continue a chat by clicking the chevron icon<ChevronRightIcon />at the top-left of the Chat panel. Your previous chats will be listed in reverse chronological order, and you can continue your conversation where you left off.

### Deleting a chat

You can delete a previous chat by clicking the chevron icon<ChevronRightIcon />at the top-left of the Chat panel to show the list of previous chats. Click the delete icon <DeleteIcon /> next to the chat you want to delete. You will be asked to confirm that you want to delete the chat.


# Using Actions in Chat
Source: https://docs.augmentcode.com/using-augment/chat-actions

Actions let you take common actions on code blocks without leaving Chat. Explain, improve, or find everything you need to know about your codebase.

export const ArrowUpIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M444-192v-438L243-429l-51-51 288-288 288 288-51 51-201-201v438h-72Z" />
    </svg>
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=db5e93308abefb7782a8684ad79e2a50" alt="Augment Chat Actions" className="rounded-xl" data-og-width="1233" width="1233" data-og-height="630" height="630" data-path="images/chat-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=24ffba8783720d584f76090090aff0fe 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=63f4c3aa42421df5ae79d40be85abfa8 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c9bfcc586feef6caa23ea46efa8fd1aa 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4fa3cd4a775a3865f92d954c842706cc 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ecc12c1fedeee7734b9e3a1bef2b434c 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7e28137d1682a5b7c5d6376870b92a59 2500w" />

## Using actions in Chat

To use a quick action, you an use a <Keyboard shortcut="/" /> command or click the up arrow icon<ArrowUpIcon />to show the available actions. For explain, fix, and test actions, first highlight the code in the editor and then use the command.

| Action                           | Usage                                                                    |
| :------------------------------- | :----------------------------------------------------------------------- |
| <Keyboard shortcut="/find" />    | Use natural language to find code or functionality                       |
| <Keyboard shortcut="/explain" /> | Augment will explain the hightlighted code                               |
| <Keyboard shortcut="/fix" />     | Augment will suggest improvements or find errors in the highlighted code |
| <Keyboard shortcut="/test" />    | Augment will suggest tests for the highlighted code                      |

Augment will typically include code blocks in the response to the action. See [Applying code blocks from Chat](/using-augment/chat-apply) for more details.


# Applying code blocks from Chat
Source: https://docs.augmentcode.com/using-augment/chat-apply

Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

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

export const MoreVertIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M479.79-192Q450-192 429-213.21t-21-51Q408-294 429.21-315t51-21Q510-336 531-314.79t21 51Q552-234 530.79-213t-51 21Zm0-216Q450-408 429-429.21t-21-51Q408-510 429.21-531t51-21Q510-552 531-530.79t21 51Q552-450 530.79-429t-51 21Zm0-216Q450-624 429-645.21t-21-51Q408-726 429.21-747t51-21Q510-768 531-746.79t21 51Q552-666 530.79-645t-51 21Z" />
    </svg>
  </div>;

export const CheckIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M389-267 195-460l51-52 143 143 325-324 51 51-376 375Z" />
    </svg>
  </div>;

export const FileNewIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h360v80H200v560h560v-360h80v360q0 33-23.5 56.5T760-120H200Zm120-160v-80h320v80H320Zm0-120v-80h320v80H320Zm0-120v-80h320v80H320Zm360-80v-80h-80v-80h80v-80h80v80h80v80h-80v80h-80Z" />
    </svg>
  </div>;

export const FileCopyIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M760-200H320q-33 0-56.5-23.5T240-280v-560q0-33 23.5-56.5T320-920h280l240 240v400q0 33-23.5 
      56.5T760-200ZM560-640v-200H320v560h440v-360H560ZM160-40q-33 0-56.5-23.5T80-120v-560h80v560h440v80H
      160Zm160-800v200-200 560-560Z" />
    </svg>
  </div>;

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b461dba46612cb6cc46db000bebb7566" alt="Augment Chat Apply" className="rounded-xl" data-og-width="1291" width="1291" data-og-height="375" height="375" data-path="images/chat-apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=dd3f5cea028042ba31b68a12f009acbc 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a1aca8f5dbff77303d4568677444eafa 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b4d3137bba658cecc13434bf193ea9a7 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=011d9dfafca386660985500a6d4c7ab6 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d9cc3f973615bbc1727876d11e0f4c7e 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-apply.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2e3a50fd918339cb519553c06bc5a242 2500w" />

## Using code blocks from within Chat

Whenever Chat responds with code, you will have the option to add the code to your codebase. The most common option will be shown as a button and you can access the other options by clicking the overflow menu icon<MoreVertIcon />at the top-right of the code block. You can use the following options to apply the code:

* <FileCopyIcon />**Copy**
  the code from the block to your clipboard
* <FileNewIcon />**Create**
  a new file with the code from the block
* <CheckIcon />**Apply**
  the code from the block intelligently to your file


# Focusing Context in Chat
Source: https://docs.augmentcode.com/using-augment/chat-context

You can specify context from files, folders, and external documentation in your conversation to focus your chat responses.

export const AtIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M480.39-96q-79.52 0-149.45-30Q261-156 208.5-208.5T126-330.96q-30-69.96-30-149.5t30-149.04q30-69.5 82.5-122T330.96-834q69.96-30 149.5-30t149.04 30q69.5 30 122 82.5t82.5 122Q864-560 864-480v60q0 54.85-38.5 93.42Q787-288 732-288q-34 0-62.5-17t-48.66-45Q593-321 556.5-304.5T480-288q-79.68 0-135.84-56.23-56.16-56.22-56.16-136Q288-560 344.23-616q56.22-56 136-56Q560-672 616-615.84q56 56.16 56 135.84v60q0 25.16 17.5 42.58Q707-360 732-360t42.5-17.42Q792-394.84 792-420v-60q0-130-91-221t-221-91q-130 0-221 91t-91 221q0 130 91 221t221 91h192v72H480.39ZM480-360q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35Z" />
    </svg>
  </div>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Chat Context

Augment intelligently includes context from your entire workspace based on the ongoing conversation–even if you don't have the relevant files open in your editor–but sometimes you want Augment to prioritize specific details for more relevant responses.

<video src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-context.mp4?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cbdd137e0c8b3c0048cfab708bbb56eb" loop muted controls className="rounded-xl" data-path="images/chat-context.mp4" />

### Focusing context for your conversation

You can specify context by clicking the <AtIcon /> icon at the top-left of the Chat panel or by <Command text="@-mentioning" /> in the input field. You can use fuzzy search to filter the list of context options quickly. There are a number of different types of additional context you can add to your conversation:

1. Highlighted code blocks
2. Specific files or folders within your workspace
3. 3rd party documentation, like Next.js documentation

#### Mentioning files and folders

Include specific files or folders in your context by typing `@` followed by the file or folder name. For example, `@routes.tsx` will include the `routes.tsx` file in your context. You can include multiple files or folders.

#### Mentioning 3rd party documentation

You can also mention 3rd party documentation in your context by typing `@` followed by the name of the documentation. For example, `@Next.js` will include Next.js documentation in your context. Augment provides nearly 300 documentation sets spanning across a wide range of domains such as programming languages, packages, software tools, and frameworks.


# Example Prompts for Chat
Source: https://docs.augmentcode.com/using-augment/chat-prompts

Using natural language to interact with your codebase unlocks a whole new way of working. Learn how to get the most out of Chat with the following example prompts.

export const type_0 = "chats"

## About chatting with your codebase

Augment's Chat has deep understanding about your codebase, dependencies, and best practices. You can use Chat to ask questions about your code, but it also can help you with general software engineering questions, think through technical decisions, explore new libraries, and more.

## Enhancing your prompt

You can improve the quality of your {type_0} by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

## Example Prompts

### Explain code

* Explain this codebase to me
* How do I use the Twilio API to send a text message?
* Explain how generics work in TypeScript and give me a simple example

### Finding code

* Where are all the useEffect hooks that depend on the 'currentUser' variable?
* Find the decorators that implement retry logic across our microservices
* Find coroutines that handle database transactions without a timeout parameter

### Generate code

* Write a function to check if a string is a valid email address
* Generate a middleware function that rate-limits API requests using a sliding window algorithm
* Create a SQL query to find the top 5 customers who spent the most money last month

### Write tests

* Write integration tests for this API endpoint
* What edge cases have I not included in this test?
* Generate mock data for testing this customer order processing function

### Refactor and improve code

* This function is running slowly with large collections - how can I optimize it?
* Refactor this callback-based code to use async/await instead
* Rewrite this function in Rust

### Find and fix errors

* This endpoint sometimes returns a 500 error. Here's the error log - what's wrong?
* I'm getting 'TypeError: Cannot read property 'length' of undefined' in this component.
* Getting CORS errors when my frontend tries to fetch from the API


# Completions
Source: https://docs.augmentcode.com/using-augment/completions

Use code completions to get more done. Augment's radical context awareness means more relevant suggestions, fewer hallucinations, and less time hunting down documentation.

export const MoreVertIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M479.79-192Q450-192 429-213.21t-21-51Q408-294 429.21-315t51-21Q510-336 531-314.79t21 51Q552-234 530.79-213t-51 21Zm0-216Q450-408 429-429.21t-21-51Q408-510 429.21-531t51-21Q510-552 531-530.79t21 51Q552-450 530.79-429t-51 21Zm0-216Q450-624 429-645.21t-21-51Q408-726 429.21-747t51-21Q510-768 531-746.79t21 51Q552-666 530.79-645t-51 21Z" />
    </svg>
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Code Completions

Augment's Code Completions integrates with your IDE's native completions system to give you autocomplete-like suggestions as you type. You can accept all of a suggestion, accept partial suggestions a word or a line at a time, or just keep typing to ignore the suggestion.

## Using Code Completions

To use code completions, simply start typing in your IDE. Augment will provide suggestions based on the context of your code. You can accept a suggestion by pressing <Keyboard shortcut="Cmd/Ctrl →" />, or ignore it by continuing to type.

For example, add the following function to a TypeScript file:

```typescript  theme={null}
function getUser(): Promise<User>;
```

As you type `getUser`, Augment will suggest the function signature. Press <Keyboard shortcut="Tab" /> to accept the suggestion. Augment will continue to offer suggestions until the function is complete, at which point you will have a function similar to:

```typescript  theme={null}
function getUser(): Promise<User> {
  return fetch("/api/user/1")
    .then((response) => response.json())
    .then((json) => {
      return json as User;
    });
}
```

### Accepting Completions

<Tabs>
  <Tab title="MacOS">
    <Tip>
      We recommend configuring a custom keybinding to accept a word or line, see
      [Keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts) for more
      details.
    </Tip>

    | Action                         | Default keyboard shortcut                       |
    | :----------------------------- | :---------------------------------------------- |
    | Accept inline suggestion       | <Keyboard shortcut="Tab" />                     |
    | Accept next word of suggestion | <Keyboard shortcut="Cmd →" />                   |
    | Accept next line of suggestion | None (see above)                                |
    | Reject suggestion              | <Keyboard shortcut="Esc" />                     |
    | Ignore suggestion              | Continue typing through the suggestion          |
    | Toggle automatic completions   | VSCode: <Keyboard shortcut="Cmd Option A" />    |
    |                                | JetBrains: <Keyboard shortcut="Cmd Option 9" /> |
  </Tab>

  <Tab title="Windows/Linux">
    <Tip>
      We recommend configuring a custom keybinding to accept a word or line, see
      [Keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts) for more
      details.
    </Tip>

    | Action                         | Default keyboard shortcut                     |
    | :----------------------------- | :-------------------------------------------- |
    | Accept inline suggestion       | <Keyboard shortcut="Tab" />                   |
    | Accept next word of suggestion | <Keyboard shortcut="Ctrl →" />                |
    | Accept next line of suggestion | None (see above)                              |
    | Reject suggestion              | <Keyboard shortcut="Esc" />                   |
    | Ignore suggestion              | Continue typing through the suggestion        |
    | Toggle automatic completions   | VSCode: <Keyboard shortcut="Ctrl Alt A" />    |
    |                                | JetBrains: <Keyboard shortcut="Ctrl Alt 9" /> |
  </Tab>
</Tabs>

### Disabling Completions

<Tabs>
  <Tab title="Visual Studio Code">
    You can disable automatic code completions by clicking the overflow menu icon<MoreVertIcon />at the top-right of the Augment panel, then selecting <Command text="Turn Automatic Completions Off" />.
  </Tab>

  <Tab title="JetBrains IDEs">
    You can disable automatic code completions by clicking the Augment icon <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7564ed27ae27d8e8e8d37fc0c5390710" className="inline h-3 p-0 m-0" data-og-width="18" width="18" data-og-height="12" height="12" data-path="images/augment-icon-smile.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e768e602ba7fbca6dee54bd80707a65f 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2bff5c6e247ef06ee8c8aaf10b729fdb 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f137c3896e95e4ae83d7374bde6fce21 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=30c491bbedc2350eeac401d6bdb88a1d 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2b87100b107e7236c3c415c046fd988b 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a39dac81c0ae990b2c8143421f4144c5 2500w" /> in the status bar at the bottom right corner of your IDE, then selecting <Command text="Disable Completions" />.
  </Tab>
</Tabs>

### Enable Completions

<Tabs>
  <Tab title="Visual Studio Code">
    If you've temporarily disabled completions, you can re-enable them by clicking the overflow menu icon<MoreVertIcon />at the top-right of the Augment panel, then selecting <Command text="Turn Automatic Completions On" />.
  </Tab>

  <Tab title="JetBrains IDEs">
    If you've temporarily disabled completions, you can re-enable them by clicking the Augment icon <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7564ed27ae27d8e8e8d37fc0c5390710" className="inline h-3 p-0 m-0" data-og-width="18" width="18" data-og-height="12" height="12" data-path="images/augment-icon-smile.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e768e602ba7fbca6dee54bd80707a65f 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2bff5c6e247ef06ee8c8aaf10b729fdb 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f137c3896e95e4ae83d7374bde6fce21 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=30c491bbedc2350eeac401d6bdb88a1d 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2b87100b107e7236c3c415c046fd988b 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a39dac81c0ae990b2c8143421f4144c5 2500w" /> in the status bar at the bottom right corner of your IDE, then selecting <Command text="Enable Completions" />.
  </Tab>
</Tabs>


# Instructions
Source: https://docs.augmentcode.com/using-augment/instructions

Use Instructions to write or modify blocks of code using natural language. Refactor a function, write unit tests, or craft any prompt to transform your code.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

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

<Availability tags={["vscode",]} />

## About Instructions

Augment's Instructions let you use natural language prompts to insert new code or modify your existing code. Instructions can be initiated by hitting <Keyboard shortcut="Cmd/Ctrl I" /> and entering an instruction inside the input box that appears in the diff view. The change will be applied as a diff to be reviewed before accepting.

## Using Instructions

To start a new Instruction, there are two options. You can select & highlight the code you want to change or place your cursor where you want new code to be added, then press <Keyboard shortcut="Cmd/Ctrl I" />. You'll be taken to a diff view where you can enter your prompt and see the results.

For example, you can generate new functions based on existing code:

```
> Add a getUser function that takes userId as a parameter
```

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bb67b9d0048e2a7c1ed23b9c3cccc8eb" className="rounded-xl" alt="Augment Instructions Diff" data-og-width="1310" width="1310" data-og-height="695" height="695" data-path="images/instructions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=238e917a8ba8599ec9b42f937b57096b 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=27e6a8088a09230d96fb467c41b9b12c 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bc05e6b31dad514fa287b2701a2356ec 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6e73c226d5591861cd9280a042bbfc16 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f7829b5be828f8e8da1442653986f84f 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/instructions.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=30ae9550ad8b82d4b84ee39aeeee2e76 2500w" />

Your change will be made as a diff, so you can review the suggested updates before modifying your code. Use the following shortcuts or click the options in the UI to accept or reject the changes.

<Tabs>
  <Tab title="MacOS">
    | Action            | Shortcut                       |
    | :---------------- | :----------------------------- |
    | Start instruction | <Keyboard shortcut="Cmd I" />  |
    | Accept            | <Keyboard shortcut="Return" /> |
    | Reject            | <Keyboard shortcut="Esc" />    |
  </Tab>

  <Tab title="Windows/Linux">
    | Action            | Shortcut                       |
    | :---------------- | :----------------------------- |
    | Start instruction | <Keyboard shortcut="Ctrl I" /> |
    | Accept            | <Keyboard shortcut="Return" /> |
    | Reject            | <Keyboard shortcut="Esc" />    |
  </Tab>
</Tabs>


# Next Edit
Source: https://docs.augmentcode.com/using-augment/next-edit

Use Next Edit to flow through complex changes across your codebase. Cut down the time you spend on repetitive work like refactors, library upgrades, and schema changes.


export const NextEditSettingsIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg width="16" height="16" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="currentColor">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M19.85 8.75l4.15.83v4.84l-4.15.83 2.35 3.52-3.43 3.43-3.52-2.35-.83 4.15H9.58l-.83-4.15-3.52 2.35-3.43-3.43 2.35-3.52L0 14.42V9.58l4.15-.83L1.8 5.23 5.23 1.8l3.52 2.35L9.58 0h4.84l.83 4.15 3.52-2.35 3.43 3.43-2.35 3.52zm-1.57 5.07l4-.81v-2l-4-.81-.54-1.3 2.29-3.43-1.43-1.43-3.43 2.29-1.3-.54-.81-4h-2l-.81 4-1.3.54-3.43-2.29-1.43 1.43L6.38 8.9l-.54 1.3-4 .81v2l4 .81.54 1.3-2.29 3.43 1.43 1.43 3.43-2.29 1.3.54.81 4h2l.81-4 1.3-.54 3.43 2.29 1.43-1.43-2.29-3.43.54-1.3zm-8.186-4.672A3.43 3.43 0 0 1 12 8.57 3.44 3.44 0 0 1 15.43 12a3.43 3.43 0 1 1-5.336-2.852zm.956 4.274c.281.188.612.288.95.288A1.7 1.7 0 0 0 13.71 12a1.71 1.71 0 1 0-2.66 1.422z" />
    </svg>
  </div>;

export const NextEditDiffIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M10.7099 1.28902L13.7099 4.28902L13.9999 4.99902V13.999L12.9999 14.999H3.99994L2.99994 13.999V1.99902L3.99994 0.999023H9.99994L10.7099 1.28902ZM3.99994 13.999H12.9999V4.99902L9.99994 1.99902H3.99994V13.999ZM8 5.99902H6V6.99902H8V8.99902H9V6.99902H11V5.99902H9V3.99902H8V5.99902ZM6 10.999H11V11.999H6V10.999Z" />
    </svg>
  </div>;

export const NextEditPencil = () => <div className="inline-block w-4 h-4 mr-2">
    <svg width="16px" height="16px" viewBox="0 0 16 16" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <title>nextedit_available_dark</title>
    <g id="nextedit_available_dark" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <path d="M11.0070258,7 C11.1334895,7 11.2318501,6.90866511 11.2529274,6.76814988 C11.5409836,4.95550351 11.8641686,4.52693208 13.7751756,4.2529274 C13.9156909,4.23185012 14,4.13348946 14,4 C14,3.8735363 13.9156909,3.77517564 13.7751756,3.75409836 C11.8571429,3.48009368 11.618267,3.07259953 11.2529274,1.21779859 C11.2248244,1.09133489 11.1334895,1 11.0070258,1 C10.8735363,1 10.7751756,1.09133489 10.7540984,1.22482436 C10.4660422,3.07259953 10.1498829,3.48009368 8.23887588,3.75409836 C8.09836066,3.78220141 8.00702576,3.8735363 8.00702576,4 C8.00702576,4.13348946 8.09836066,4.23185012 8.23887588,4.2529274 C10.1569087,4.52693208 10.4028103,4.92740047 10.7540984,6.77517564 C10.7822014,6.91569087 10.8805621,7 11.0070258,7 Z" id="Path" fill="#BF5AF2"></path>
        <path d="M14.0056206,8.8 C14.0814988,8.8 14.1405152,8.74519906 14.1531616,8.66088993 C14.3259953,7.57330211 14.5199063,7.31615925 15.6665105,7.15175644 C15.7508197,7.13911007 15.8014052,7.08009368 15.8014052,7 C15.8014052,6.92412178 15.7508197,6.86510539 15.6665105,6.85245902 C14.5156909,6.68805621 14.3723653,6.44355972 14.1531616,5.33067916 C14.1362998,5.25480094 14.0814988,5.2 14.0056206,5.2 C13.9255269,5.2 13.8665105,5.25480094 13.8538642,5.33489461 C13.6810304,6.44355972 13.4913349,6.68805621 12.3447307,6.85245902 C12.2604215,6.86932084 12.2056206,6.92412178 12.2056206,7 C12.2056206,7.08009368 12.2604215,7.13911007 12.3447307,7.15175644 C13.4955504,7.31615925 13.6430913,7.55644028 13.8538642,8.66510539 C13.870726,8.74941452 13.9297424,8.8 14.0056206,8.8 Z" id="Path-Copy" fill="#BF5AF2" opacity="0.600000024"></path>
        <g id="Pencil_Base" fill="#168AFF">
            <path d="M3.07557525,3.27946831 C3.10738379,3.27258798 3.13664209,3.26682472 3.16597818,3.26160513 C3.19407786,3.25661079 3.22181021,3.25217747 3.24959807,3.24822758 C3.3431507,3.23490837 3.43787348,3.22705558 3.53270619,3.22474499 C3.54619312,3.22441336 3.56021661,3.22418981 3.57424082,3.22408741 L3.59202055,3.22402251 C3.61600759,3.22402251 3.63999463,3.22437692 3.66397314,3.22508575 C3.69176119,3.22590043 3.72012236,3.22722855 3.74845755,3.22905289 C3.77692744,3.23089046 3.80498198,3.23319023 3.83299719,3.23597733 C3.86236278,3.23889105 3.89230728,3.24242516 3.92218997,3.24651769 C3.95842477,3.25149198 3.99379267,3.25714552 4.02904516,3.2635852 C4.04457753,3.26641925 4.06056799,3.26950351 4.07653203,3.27274998 C4.1217801,3.28195855 4.16647313,3.29238022 4.21089814,3.30408537 C4.22093231,3.3067264 4.23153789,3.30959531 4.24212737,3.31253756 C4.27196202,3.32083528 4.30106886,3.32952376 4.33003598,3.33877116 C4.35855924,3.347869 4.38751122,3.35771229 4.41630528,3.3681193 C4.42116985,3.36987869 4.42551008,3.37146263 4.42984665,3.3730594 C4.4761162,3.39008583 4.52241276,3.4087674 4.56821184,3.42893807 C4.59406406,3.44033198 4.61917606,3.45191971 4.64412424,3.46396063 C4.67111495,3.47697976 4.69839649,3.4907848 4.72546291,3.50513959 C4.75890801,3.52288219 4.79178851,3.54132453 4.82431475,3.56059431 C4.8374698,3.56838641 4.85073285,3.5764165 4.86393439,3.58458539 C4.89491851,3.60376145 4.92539479,3.6235868 4.95550936,3.64416832 C4.9772823,3.65904443 4.99913454,3.67451232 5.02078256,3.69038541 C5.03998798,3.70447076 5.05881967,3.71870909 5.07748715,3.73325923 C5.10440445,3.75423289 5.13126725,3.7760983 5.15775949,3.79862613 C5.1821715,3.81939236 5.20595148,3.84042939 5.22940861,3.86201411 C5.24512436,3.87647694 5.26059993,3.89109333 5.27592752,3.90595256 C5.28442786,3.91418351 5.29385225,3.92345739 5.30321896,3.9328241 L10.2031018,8.83270693 C10.255475,8.88508012 10.3065885,8.93859789 10.3564099,8.99321224 L10.2031018,8.83270693 C10.2748395,8.90444467 10.344214,8.97832987 10.4111413,9.05423915 C10.4223877,9.06699478 10.4335715,9.07981507 10.4446856,9.092692 C10.7663645,9.46539004 11.0297601,9.88553066 11.2252237,10.3388957 L11.6780206,11.3880225 L12.548286,13.4076516 C12.7467158,13.8678966 12.5344727,14.4018581 12.0742277,14.6002879 C11.9977866,14.6332447 11.9179446,14.6552159 11.836969,14.6662015 L11.7149387,14.6744406 C11.592625,14.6744406 11.4703113,14.6497231 11.3556497,14.6002879 L11.2340206,14.5480225 L9.33602055,13.7300225 L8.28689372,13.2772256 C7.83352871,13.081762 7.41338809,12.8183665 7.04069004,12.4966876 L7.0022372,12.4631433 C6.98177889,12.4451057 6.9614676,12.4268903 6.94130575,12.4084989 L7.04069004,12.4966876 C6.95122931,12.4194733 6.86450207,12.3389008 6.78070498,12.2551038 L1.88082214,7.35522092 C0.935753358,6.41015213 0.935753358,4.87789288 1.88082214,3.9328241 L1.90902055,3.90502251 L2.01192506,3.8109306 C2.19120357,3.65606766 2.38780913,3.5318516 2.59488381,3.4382824 C2.62872186,3.42311621 2.65522016,3.41182111 2.68187195,3.40102033 C2.76025666,3.36925866 2.83986347,3.34180278 2.92043821,3.31861145 L3.07557525,3.27946831 Z M9.58610551,9.95149698 L7.89951995,11.6381324 C8.10279642,11.805046 8.32371441,11.9494547 8.55841217,12.068738 L8.76594574,12.166096 L10.2570206,12.8090225 L10.7570206,12.3090225 L10.114094,10.8179477 C9.97930356,10.5053101 9.80144069,10.2137385 9.58610551,9.95149698 Z" id="Combined-Shape" fill-rule="nonzero"></path>
            <rect id="Rectangle" opacity="0.005" x="0" y="0" width="16" height="16" rx="2"></rect>
        </g>
    </g>
    </svg>
  </div>;

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

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

<Availability tags={["vscode"]} />

## About Next Edit

<iframe class="w-full aspect-video rounded-md" src="https://www.youtube.com/embed/GPQgQpXbunc?si=opEGaxWlnWWtDimK" title="Feature Intro: Augment Next Edit" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

Next Edit helps you complete your train of thought by suggesting changes based on
your recent work and other context. You can jump to the next edit and quickly accept or
reject the suggested change with a single keystroke.

## Using Next Edit

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=15d2c45a86087dbf50527e6fd6f2fcbf" className="rounded-xl" data-og-width="800" width="800" data-og-height="269" height="269" data-path="images/next-edit-example.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f5012d087f9b3d75b1ffbe6f3e9377b9 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bc7568485ba1b35dc4a8e2328d44be52 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=9efd8d51d0a8454f4dcc67b1bcc7e6f1 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=133205b0f221da141c170291e6a712c7 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b1a1323ffd4c70f32c314563c3415865 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7991b04dd64d5e34638c3ec2e055f638 2500w" />

When Next Edit has a suggestion available, you will see a gutter icon and a summary
of the change in gray at the end of the line.
To jump to the next suggestion, press <Keyboard shortcut="Cmd/Ctrl ;" /> and
after reviewing the change, press <Keyboard shortcut="Enter" /> to accept
or <Keyboard shortcut="Backspace" /> to reject. If there are multiple
changes, press <Keyboard shortcut="Cmd/Ctrl ;" /> to accept and go to the
next suggestion.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2da1f3c529ce412004a7ed76ed9f7f6b" className="rounded-xl" data-og-width="1462" width="1462" data-og-height="447" height="447" data-path="images/next-edit-before.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=0eb68374ca0a2c27fdad7a7b03f83607 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a8814149922d202be7f35bcdca312c51 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=45a4363821b32aecef32a97c0eb61afd 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=1f9b79e4de971adac4dada7b8d82d796 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e8aec093ceccb9149bcd11a4093fdc24 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d77a87e90ab11569419ab6ddfd62952f 2500w" />

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4a4da9a295d213befb4787f8f32db0c3" className="rounded-xl" data-og-width="1462" width="1462" data-og-height="447" height="447" data-path="images/next-edit-after.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e4cc486dd570c612801d2cf45a8b5c2d 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4225a043bd285ccb80727b2414049819 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d515db036c6c0a2e74542fbab2b01e40 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2fee9ca15c32226d7122c870d2cee767 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=83ad3d37fa57e5c619b2b7c4e51bfdbf 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=dd22baa4f4973628ef4b6c310a225de2 2500w" />

By default, Next Edit will briefly highlight which parts of the existing code will
change before applying the change and highlighting the new code. Use Undo
(<Keyboard shortcut="Cmd/Ctrl Z" />) and Redo
(<Keyboard shortcut="Cmd Shift Z/Ctrl Y" />) to manually review the change.
You can configure this behavior in your Augment extension settings.

### Keyboard Shortcuts

<Tabs>
  <Tab title="MacOS">
    | Action            | Default shortcut                    |
    | :---------------- | :---------------------------------- |
    | Go to next        | <Keyboard shortcut="Cmd ;" />       |
    | Go to previous    | <Keyboard shortcut="Cmd Shift ;" /> |
    | Accept suggestion | <Keyboard shortcut="Enter" />       |
    | Reject suggestion | <Keyboard shortcut="Backspace" />   |
  </Tab>

  <Tab title="Windows/Linux">
    | Action            | Default shortcut                     |
    | :---------------- | :----------------------------------- |
    | Go to next        | <Keyboard shortcut="Ctrl ;" />       |
    | Go to previous    | <Keyboard shortcut="Ctrl Shift ;" /> |
    | Accept suggestion | <Keyboard shortcut="Enter" />        |
    | Reject suggestion | <Keyboard shortcut="Backspace" />    |
  </Tab>
</Tabs>

### Next Edit Indicators And Actions

There are several indicators to let you know Next Edits are available:

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d430e246380007353fb051329d5fe5c0" className="rounded-xl" data-og-width="1321" width="1321" data-og-height="493" height="493" data-path="images/next-edit-indicators-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7891da274cf6c865d15111e74b6ef820 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=91ce4241983c21e7292035b0200e3c2f 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c60a652018795ef075189345dd70a6df 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4571970e9457d34f15a446aba7cc2d94 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=53c7de6e5e691db931866dd603d61a03 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b9f5440a70f7dc5d40a3bd4fc403f8da 2500w" />

1. **Editor Title Icon** (Top Right): Changes colors when next edits are available.
   Click on the <NextEditPencil /> icon to open the next edit menu for
   additional actions like enabling/disabling the feature or accessing settings.
2. **Gutter Icon** (Left) - Indicates which lines will be changed by the suggestion
   and whether it will insert, delete or change code.
3. **Grey Text** (Right) -  appears on the line with the suggestion on screen with a
   brief summary of the change and the keybinding to press (typically
   <Keyboard shortcut="Cmd/Ctrl ;" />).

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=461d6b6607c9676e5ec7e691bd1d466d" className="rounded-xl" data-og-width="1322" width="1322" data-og-height="136" height="136" data-path="images/next-edit-indicators-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=fab3666721b4f18842ee57ae232c7c98 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=543b6460fdb6a499ed1b4a3914a787a8 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c201443209c6b06bd5f2e9e61e21b3dd 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3bd7d2ecacc875128a22079b5dffad2d 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=52ade466db783f9248a3c3650e482892 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c949c4bc61b0570c0495ff9fffc0e58e 2500w" />

4. **Hint Box** (Bottom Left) - appears when the next suggestion is off screen with
   brief summary of the change and the keybinding to press (typically
   <Keyboard shortcut="Cmd/Ctrl ;" />).

The tooltip also presents a few actions as icons:

* <NextEditDiffIcon /> Toggles showing diffs for suggestions in the tooltip.
* <NextEditSettingsIcon /> Opens Next Edit settings.

### Next Edit Settings

You can configure Next Edit settings in your Augment extension settings.
To open Augment extension settings, either navigate to the option through the pencil
menu, or open the Augment Commands panel by pressing
<Keyboard shortcut="Cmd/Ctrl Shift A" /> and select <Command text="⚙ Edit Settings" />.

Here are some notable settings:

* <Command text="Augment > Next Edit: Enable Background Suggestions" />: Use to enable or
  disable the feature.
* <Command text="Augment > Next Edit: Enable Global Background Suggestions" />: When enabled, Next
  Edits will suggest changes in other files via the hint box.
* <Command text="Augment > Next Edit: Enable Auto Apply" />: When enabled, Next
  Edits will automatically apply changes when you jump to them.
* <Command text="Augment > Next Edit: Show Diff in Hover" />: When enabled,
  Next Edits will show a diff of the suggested change in the hover.
* <Command text="Augment > Next Edit: Highlight Suggestions in The Editor" />: When enabled,
  Next Edits will highlight all lines with a suggestion in addition to showing gutter
  icons and grey text.


# Using Remote Agent
Source: https://docs.augmentcode.com/using-augment/remote-agent

Use Remote Agent to complete tasks across your workflow–implementing a feature, upgrade a dependency, or writing a pull request–all from the cloud and with the full power of Visual Studio Code when you need it.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Remote Agent

Augment Remote Agent is a powerful tool that can help you complete software development tasks end-to-end that runs in a secure, cloud environment. You can run multiple agents in parallel on independent tasks, and you'll monitor and manage their progress from within Visual Studio Code. Remote Agents can run in normal or auto mode, just like IDE-based agents, and will notify you when they need attention.

### How is Remote Agent different from Agent?

Remote Agent is a cloud version of the IDE-bound Agent. Each Remote Agent runs on its own secure environment, with its own workspace-all of which is managed for you. Each Remote Agent works independently and on its own branch, so you can have multiple agents working on the same repository at the same time.

## Accessing Remote Agent

To start a new Remote Agent, simply open the Augment panel and select Remote Agent from the drop down in the input box.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b915365cbd1ba0b0b272899cb0aa32f7" alt="Augment Remote Agent" className="rounded-xl" data-og-width="1400" width="1400" data-og-height="738" height="738" data-path="images/remote-agent-selector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=23b52dee17b6abdb8006622c37e2f080 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=dc85ccfab2d3058d17bfba609d343328 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ad0eea50ca4866a38f8a4d1d33b57db5 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1494fd89713449c5444bce132d68b447 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=da8ddb5bc00d9760c37f2cf871f2a3cb 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a433a1a6db69a74b535b1f93c5f6ac4f 2500w" />

### Agent dashboard

You can view all of your remote agents in the Remote Agent dashboard by clicking the <Command text="Expand dashboard" /> icon in the top of the Augment panel. From the dashboard you are able to see the status of all of your agents, connect to them through SSH, or delete them when they are no longer needed.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a973fa14491d8c99a348880e3ee73043" alt="Augment Agent" className="rounded-xl" data-og-width="1134" width="1134" data-og-height="640" height="640" data-path="images/remote-agent-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=445b4523e55e972d73394aa7950eea4e 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=87bc074b950ea95ac85a53430c974d77 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b871b9516084db79bf35a1bd0f00f537 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ff93117d5b3cf69073587289588d0bf6 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=0995d1b19016a912cae022d48c3c4d6b 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=cf0fc2b471ef2c12fa027ba68f49366d 2500w" />

## Using Remote Agent

Remote Agents function nearly identically to IDE-bound agents as you work through your tasks and projects. Because they run asynchronously in the cloud, you can access and manage them while working on other projects in your editor. Access your Remote Agents from the threads menu at the top of the Augment panel or through the Remote Agent dashboard.

You can create and manage a Remote Agent for any repository you have access to through GitHub regardless of which project you are currently working on in your editor.

### Create a remote agent

<Note>
  Before you can use Remote Agent, you will need to connect your GitHub account to enable the agent to clone your repository, create branches, and open pull requests. See [Agent Integrations](/setup-augment/agent-integrations) for setup instructions.
</Note>

1. **Select the repository** you want the agent to work on
2. **Select the branch** or let the agent create a new branch for you
3. **Select an environment** or [create a new one](/using-augment/remote-agent-environment) for the agent to run in
4. Enter your prompt into the input box using natural language and click **Create agent**

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1677b4b0e978f84ca87753d69617e5d9" alt="Create a Remote Agent" className="rounded-xl" data-og-width="962" width="962" data-og-height="950" height="950" data-path="images/remote-agent-new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=9a324c04f5bf4d155197bc0efa9d2236 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3f8caa0995808766fb0ad94af3db2d31 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=40caf3a505518828f41e233c2fec39e2 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=666583055ada1ba387c7ac9eabf9bded 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b831ffe39c9ce1945d1b1daaff60be79 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=5fed4b0725c25eb6c4aa937439399182 2500w" />

#### Agent environment

Each Remote Agent runs in an secure, independent environment in the cloud. This enables each agent to have its own workspace, copy of the repository, and virtualized operating system to run other tools and commands. You can use the [base environment](/using-augment/remote-agent-environment#base-environment), or setup a custom environment using a bash script to configure the tools the agent will need to complete the task.

See [Remote Agent Environment](/using-augment/remote-agent-environment) for more details on customizing the agent environment.

### Agent notifications

By default, you will receive a notification in VS Code when the agent has completed a task or needs your attention. You can disable notifications for a remote agent by clicking the bell icon in the theads list of the Augment panel.

### Iterating with an agent

Once an agent has completed the task, you can continue to iterate with the agent by sending additional messages. The agent will continue to work on the task, using its past conversations as context. If you need to switch to editing files directly, you can connect to the agent environment over SSH. See [Connecting to a Remote Agent](#connecting-to-a-remote-agent-environment) for more details.

### Reviewing changes

You can review every change Agent makes by clicking on the action to expand the view. Review diffs for file changes, see complete terminal commands and output, and the results of external integration calls.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bab5fc7aed7f83ae499c9b5d72dfd03a" alt="Augment Agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="543" height="543" data-path="images/agent-edit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d0ba25bfbf7579dc11e03c5c610f5f9b 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=24afe8b62ccaf04b7b8a38541c94eb7b 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cc170722a8152fada50217b03c08c013 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=71ebbaa901d3740c0be592f243a47931 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a7befc70fed705adaa44a9af3b178134 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b847e3015c2963f15a77f3e2b648086b 2500w" />

### Stop or guide the Agent

You can interrupt the Agent at any time by clicking Stop. This will pause the action to allow you to correct something you see the agent doing incorrectly. While Agent is working, you can also prompt the Agent to try a different approach which will automatically stop the agent and prompt it to correct its course.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1d3cbc704431241980fe8deca0118841" alt="Stopping the agent" className="rounded-xl" data-og-width="1290" width="1290" data-og-height="574" height="574" data-path="images/remote-agent-stop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=f148b2d42f38a9127c4fd78f4abae33c 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b9298bd27a06e0c3f34bf0e1c9f6e8c8 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=45885224a221e2463f9aeb249e7aab90 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=209dfa6202425a57063678e2815b7e40 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3415dfda919fa793cc8291a8e35f6fde 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3ea17b3dcb19e4b44da54c62582a50cb 2500w" />

### Connecting to a Remote Agent environment

<Note>
  You will need to have the [Remote-SSH extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) installed in Visual Studio Code to connect to a remote agent. If you do not have it installed, you will be prompted to install it automatically.
</Note>

From time to time you may need to connect to a remote agent to view or edit files directly, in that case you can connect to the agent environment over SSH. From the Remote Agent dashboard, click the <Command text="SSH to agent" /> button in the agent card you with to connect to.

This will open a Visual Studio Code window connected to the agent's environment. If this is your first time opening the connection, you will be prompted by VS Code to trust the files in the remote folder. Click <Command text="Yes, I trust the authors" /> to continue.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=182e98219b6387fed988fad50c4759cb" alt="Augment Agent" className="rounded-xl" data-og-width="1362" width="1362" data-og-height="816" height="816" data-path="images/remote-agent-trust.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=8380e170bf1d3d87b4dc254f3c4bb709 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e262b7c1c6516a8e7c10d698e1b49c71 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=77342a498afbe40fa86f5bc81c37d786 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=055371af3b44656a2338e8f703a9d225 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=86544b81a1cc9794e8e191bb21fd0fbb 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4e2da851750f33d8d1762bf13ebc5d67 2500w" />

You can use the new VS Code window to view and edit files, run commands in the terminal, and generally interact with the agent just like you would a local IDE-bound agent.

### Opening a Pull Request

When the agent has completed the work, you can open a pull request to have your changes opened for review and merging into the main branch. Select the agent from the threads list and click <Command text="Create a PR" />. The agent will create a branch, commit the changes, and open a pull request for you. This will count against your credits quota.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=92e70ec38eb113bb6850dd2ec582b00b" alt="Augment Agent Pull Request" className="rounded-xl" data-og-width="1290" width="1290" data-og-height="962" height="962" data-path="images/remote-agent-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ec3b729b160ae86958b1ff565970e56c 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=238d74d2e0ee38d2f312b92a893a70cb 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=307a9f2bd706cd48cc9c9ca5f3d59c4c 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=589cf5049fe23ea64a955d58821d263d 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=146faadaedd646fe0f34f9194258532f 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=8ecd151ccfbe83eaa6c6e9737f921e07 2500w" />

### Resuming a Remote Agent

Remote Agents automatically pause after completing a request or remaining idle for a period of time. To resume a paused Remote Agent, either click <Command text="Open a remote workspace" /> or send a new message to the agent. Both actions will count against your credits quota.

## Comparison chart

Agent takes Chat to the next level by allowing Augment to do things for you-that is create and make modifications directly to your codebase. Chat can explain code, create plans, and suggest changes which you can smartly apply one-by-one, but Agent takes it a step further by automatically implementing the entire plan and all code changes for you.

| What are you trying to do?                       | Chat | Agent | Remote Agent |
| :----------------------------------------------- | :--: | :---: | :----------: |
| Ask questions about your code                    |  ☑️  |   ✅   |       ✅      |
| Get advice on how to refactor code               |  ☑️  |   ✅   |       ✅      |
| Add new features to selected lines of code       |  ☑️  |   ✅   |       ✅      |
| Add new feature spanning multiple files          |      |   ✅   |       ✅      |
| Document new features                            |      |   ✅   |       ✅      |
| Open Linear tickets or start a pull request      |      |   ✅   |       ✅      |
| Start a new branch in GitHub from recent commits |      |   ✅   |       ✅      |
| Automatically perform tasks on your behalf       |      |   ✅   |       ✅      |
| Work on multiple tasks in the same repository    |      |       |       ✅      |
| Continue working after closing VS Code           |      |       |       ✅      |

## Use cases

Use Remote Agent to handle various aspects of your software development workflow, from simple configuration changes to feature implementations. Remote Agent is best for discreet tasks that can be completed in isolation from other work. Remote Agent supports your daily engineering tasks like:

* **Make quick edits** - Create a pull request to adjust configuration values like feature flags from FALSE to TRUE
* **Fix papercuts** - Fix small bugs or issues in the codebase that never make it to the top of your TODO list
* **Perform refactoring** - Move functions between files while maintaining coding conventions and ensuring bug-free operation
* **Explore alternatives** - Run multiple remote agents to create alternative solutions to a problem
* **Start a first draft for new features** - Start a pull request (PR) with implementing entirely new functionality straight from a GitHub Issue or Linear Ticket
* **Start tickets in Linear or Jira** - Open tickets and ask Agent to suggest a plan to address the ticket
* **Create test coverage** - Generate unit tests for your newly developed features
* **Generate documentation** - Produce comprehensive documentation for your libraries and features

## Remote Agent Clean-up

Remote Agents automatically pause after completing a request or remaining idle for a period of time. Agents that remain idle for 30 days are automatically cleaned up by the system. This cleanup process removes all files in the Remote Workspace, conversation history, and any pending diffs.

## Next steps

* [Configure Agent Integrations](/setup-augment/agent-integrations)
* [Configure other tools with MCP](/setup-augment/mcp)


# Using Augment for Slack
Source: https://docs.augmentcode.com/using-augment/slack

Chat with Augment directly in Slack to explore your codebase, get instant help, and collaborate with your team on technical problems.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Augment for Slack

Augment for Slack brings the power of Augment Chat to your team's Slack workspace. Mention <Command text="@Augment" /> in any channel or start a DM with Augment to have deep codebase-aware conversations with your team. Before you can use Augment for Slack, you will need to [install the Augment Slack App](/setup-augment/install-slack-app).

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=6f5619de7d03d015c25ce2f514a56fd5" alt="Augment for Slack" className="rounded-xl" data-og-width="1544" width="1544" data-og-height="866" height="866" data-path="images/slack-chat-reply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=636f110e793cb75bf701d78e0147210e 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4d4433371e614333995402bd9c502be4 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=f2e551a655626021bb180c0494e84e5b 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=af85a5400a3db50da8b71456e47b51e8 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=80a7ddc46d881dcc81a51e3aa6f2d92e 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4e240bc18073e63e661404f2d3cc00fe 2500w" />

## Adding Augment to Channels

Mention <Command text="@Augment" /> to add it to any public or private channel.

*Note: To protect your code, Augment excludes repository context in channels with external members.*

## Starting Conversations in Channels

Mention <Command text="@Augment" /> anywhere in your message or thread to start a conversation. Augment will consider the entire thread's context when responding. Remove messages by adding a ❌ reaction.

## Direct Messages

While group discussions help share knowledge, you can also have private conversations with Augment. Access it by:

* Clicking the Augment logo in the top right of your Slack workspace
* Finding it under <Command text="Apps" /> in the Slack sidebar
* Pressing <Keyboard shortcut="Cmd/Ctrl T" /> and searching for <Command text="@Augment" />

If you don't see the Augment logo, add it to your [navigation bar](/setup-augment/install-slack-app#3-add-augment-to-the-slack-navigation-bar). *If you don't see this option, contact your workspace admin to [re-install the App](/setup-augment/install-slack-app#2-install-slack-app).*

You do not need to mention Augment in direct messages - it will respond to every message!

## Restricting where Augment can be used

Augment already avoids responding with codebase context in external channels, to protect your codebase from Slack users outside of your organization. Beyond this, you can also further restrict what channels Augment can be used in, with an allowlist. If configured, Augment will only respond in channels or DMs that are in the allowlist. To use this feature, contact us.

## Repository Context

Augment uses the default branch (typically `main`) of your linked repositories. Currently, other branches aren't accessible.

If you have multiple repositories installed, use <Command text="/augment repo-select" /> to choose which repository Augment should use for the current conversation. This selection applies to the specific channel or DM where you run the command, allowing you to work with different repositories in different conversations.

## Feedback

Help us improve by reacting with 👍 or 👎 to Augment's responses, or use the `Send feedback` message shortcut. We love hearing from you!


# Using Tasklist
Source: https://docs.augmentcode.com/using-augment/tasklist

Use Tasklist to break down complex problems into manageable steps, track progress, and collaborate with Agent on multi-step tasks.

## About the Tasklist?

Augment's Tasklist helps the Agent in the IDE create and refine a step-by-step plan for you to review. The Tasklist provides a structured interface for collaboration between you and the Agent, allowing you to break down complex problems into manageable, sequential steps.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=7b57f10306d17d7a01769a36f1f08888" alt="Tasklist Overview" className="rounded-xl" data-og-width="473" width="473" data-og-height="208" height="208" data-path="images/tasklist-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=cfe6643999d0f51858bdc307a405e706 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=707d717d48b17655f8de15a57e17efb2 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=28a71d28a31963133145d84dd4c6dc6e 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=2d8afe47cdba513cacd3b1510212c099 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=fb50e40cef51f5c43b392b283ac52626 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-overview.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=2b21a1b7e583664dc6eac0559d0129ac 2500w" />

## Getting started with Tasklist?

Tasklist improves agent effectiveness on long or complex tasks by:

* **Maintaining context** across different conversations by moving your Tasklist to a new chat
* **Breaking down complex problems** into manageable, sequential steps
* **Gathering progress** across threads
* **Exploring alternative solutions** to completed tasks if you need to pivot
* **Streamlining your approach** to nebulous problems by deleting irrelevant steps once the path forward is clear

Tasklist provides a structured interface for collaboration and opens up possibilities for agent-to-agent collaboration. We hypothesize that an interface such as Tasklist could be a preferred way to interact with coding agents in the future.

## Creating a New Task

### Automatic Creation

The Agent will usually create a Tasklist when it encounters a complex, multi-step problem. You can also ask the Agent to make a Tasklist for you by simply prompting "Start a Tasklist to..." then add the problem you are trying to tackle.

### Manual Creation

You can also manually create a Tasklist:

1. Switch to Tasklist using the checklist button next to Changes
2. Click the plus to add your first task
3. Alternatively, you can create a new task by typing in the gray prompt box at the bottom of the extension. Click **Add Task** from the dropdown arrow next to Send

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a2603f672d47c74e7582cb6da58cad04" alt="Creating a new task" className="rounded-xl" data-og-width="473" width="473" data-og-height="85" height="85" data-path="images/tasklist-create-task.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=273857c88137440b4ce932962d5842d8 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b53633da83f18abacd816c4a4fbb2fe2 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=03e5417ccbd446b8ee6b10fc6b00f2f4 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=2e13079c3e2eabfdde93bb4ed73c3a87 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=34bf7e951951489686422f7cc5ea3b3d 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-create-task.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=bc3db1e1b3dd7c092b91dcdbd38a2561 2500w" />

## Running Tasks

To run a task, click the grey triangle (play button) next to the task. The Agent will begin executing the task and update its status as it progresses.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=58d05e0c445e9b4fb449c6ade5a298bd" alt="Running a task" className="rounded-xl" data-og-width="824" width="824" data-og-height="778" height="778" data-path="images/tasklist-run-task.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4819f31c0860ebcc5827693ea0c0baad 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=27aa131b8c5fd591162d6fccfe35ec50 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=8b90fc209a811b5f2f59f9747edce1df 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=c05369faa15a20ad17622d875ac2f601 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=6c3c3c9250484b0982d023bbd1400693 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-run-task.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3de97385af039261f008cfb0e801116d 2500w" />

## Task Status Indicators

Task statuses are indicated by different colors and icons:

* **Empty circle** - Task has not yet started
* **Blue half circle** - Task is currently in progress
* **Green checkbox** - Task has been completed and is ready for review

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=989d263506a6346c0033d5fe0ea51475" alt="Task status indicators" className="rounded-xl" data-og-width="473" width="473" data-og-height="214" height="214" data-path="images/tasklist-status-indicators.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=cd926a7cbeb7ec67d4bb51cead1485c6 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=6b2651040fdbad62384eee3cfdbfe716 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=856571460250f49bcabd817161b0f270 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=24e4ac9d6f6290731463213cfad02657 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a1148d6927825479fc4e92dd5da17469 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-status-indicators.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=92da7588be36eeb5b471593b51dcc1c0 2500w" />

## Subtasks

Augment Code automatically generates subtasks when needed. The Agent will automatically add and nest required subtasks under your initial tasks. You can edit and expand these subtasks just like any other task in the list. Likewise, you can remove subtasks you deem unnecessary.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=06a66a68939509b93969d6ee352363a7" alt="Subtasks example" className="rounded-xl" data-og-width="233" width="233" data-og-height="32" height="32" data-path="images/tasklist-subtasks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=64ab84c553e9c00a188211b706e2fac0 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=754a79480312c19f6d2cdfb6f0da568a 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ed5c411199b3c1c08d194dca0996ba7a 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=c85b03a98902b4200034ffbe772f86aa 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a66ffd3ef9f68064fa3d215b59b8e444 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-subtasks.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=f40745bd17de1648e51d5304d312b67b 2500w" />

## Managing Running Tasks

### Stopping a Task

You can treat any in-progress task like any prompt you might send the Agent. To stop what the Agent is doing and offer a corrective action, click the red square (stop button) and tell the Agent what you want it to do instead.

### Running All Tasks

The Agent can complete all the tasks sequentially by clicking the triangle (play button) at the top of the Tasklist.

## Reviewing Changes

You can review the changes made by the Agent after a task is completed by toggling between the Tasks and Changes view to see the diffs (differences) of the work done by the agent for each task.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=35ce060276c5dc8fec9f1f9b473c9599" alt="Reviewing changes in Tasks and Changes view" className="rounded-xl" data-og-width="818" width="818" data-og-height="364" height="364" data-path="images/tasklist-changes-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=7c4571f3c0ead8a670ca3aa604176d0c 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4479c4f468883c3a59feed2560c9a81c 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a649dcd4a9164c2eeb3d5928ba4b5e40 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e85d1a4989fd58ab60e561f1a38fb8d3 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b563421017b53c86cb7704e7f5369ab2 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/tasklist-changes-view.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=364274422e2215186f8b207441307ec9 2500w" />

## Integration with Task Management Tools

### Jira and Linear Integration

The Tasklist is a perfect pairing with existing task management tools like Jira or Linear:

* Ask the Agent to create a Tasklist based on tickets inside Jira or Linear
* Further break down complex tickets into manageable steps
* Once your Tasklist is completed, you can ask the Agent to resolve the issue inside Jira or Linear and append the steps taken as a comment

### Standalone Usage

Don't use an issue tracker? No problem - use Tasklist to track issues you need to tackle across Threads.

## Best Practices

* **Be specific** when creating tasks to help the Agent understand exactly what needs to be done
* **Review and edit** the automatically generated subtasks to ensure they align with your goals
* **Use the stop function** to provide course corrections when the Agent is heading in the wrong direction
* **Leverage the Changes view** to review all modifications made during task execution
* **Move Tasklists** between conversations to maintain context across different chat sessions

## Next Steps

* [Learn more about Agent](/using-augment/agent)
* [Configure Agent Integrations](/setup-augment/agent-integrations)


# Install Augment for Vim and Neovim
Source: https://docs.augmentcode.com/vim/setup-augment/install-vim-neovim

Augment for Vim and Neovim gives you powerful code completions and chat capabilities integrated into your favorite code editor.

export const Next = ({children}) => <div className="border-t border-b pb-8 border-gray dark:border-white/10">
    <h3>Next steps</h3>
    {children}
  </div>;

export const NeoVimLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_1012_311)">
<path fill-rule="evenodd" clip-rule="evenodd" d="M2.11719 5.0407L7.2509 -0.14502V23.9669L2.11719 18.841V5.0407Z" fill="url(#paint0_linear_1012_311)" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M21.9551 5.08747L16.7572 -0.14502L16.8625 23.9669L21.9902 18.8404L21.9551 5.08747Z" fill="url(#paint1_linear_1012_311)" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M7.25 -0.111816L20.5981 20.2637L16.8629 24.0001L3.50781 3.66964L7.25 -0.111816Z" fill="url(#paint2_linear_1012_311)" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M7.24955 9.28895L7.24248 10.0894L3.14258 4.01872L3.52221 3.63086L7.24955 9.28895Z" fill="black" fill-opacity="0.13" />
</g>
<defs>
<linearGradient id="paint0_linear_1012_311" x1="258.803" y1="-0.14502" x2="258.803" y2="2411.04" gradientUnits="userSpaceOnUse">
<stop stop-color="#16B0ED" stop-opacity="0.800236" />
<stop offset="1" stop-color="#0F59B2" stop-opacity="0.837" />
</linearGradient>
<linearGradient id="paint1_linear_1012_311" x1="-239.663" y1="-0.14502" x2="-239.663" y2="2411.04" gradientUnits="userSpaceOnUse">
<stop stop-color="#7DB643" />
<stop offset="1" stop-color="#367533" />
</linearGradient>
<linearGradient id="paint2_linear_1012_311" x1="858.022" y1="-0.111816" x2="858.022" y2="2411.08" gradientUnits="userSpaceOnUse">
<stop stop-color="#88C649" stop-opacity="0.8" />
<stop offset="1" stop-color="#439240" stop-opacity="0.84" />
</linearGradient>
<clipPath id="clip0_1012_311">
<rect width="24" height="24" fill="white" />
</clipPath>
</defs>
</svg>;

export const ExternalLink = ({text, href}) => <a href={href} rel="noopener noreferrer">
    {text}
  </a>;

<CardGroup cols={1}>
  <Card title="Get the Augment Extension" href="https://github.com/augmentcode/augment.vim" icon={<NeoVimLogo />} horizontal>
    View Augment for Vim and Neovim on GitHub
  </Card>
</CardGroup>

## About Installation

Installing <ExternalLink text="Augment for Vim and Neovim" href="https://github.com/augmentcode/augment.vim" /> is easy and will take you less than a minute. You can install the extension manually or you can use your favorite plugin manager.

## Prerequisites

Augment for Vim and Neovim requires a compatible version of Vim or Neovim, and Node.js:

| Dependency                                                                                     | Minimum version |
| :--------------------------------------------------------------------------------------------- | :-------------- |
| [Vim](https://github.com/vim/vim?tab=readme-ov-file#installation)                              | 9.1.0           |
| [Neovim](https://github.com/neovim/neovim/tree/master?tab=readme-ov-file#install-from-package) | 0.10.0          |
| [Node.js](https://nodejs.org/en/download/package-manager/all)                                  | 22.0.0          |

## 1. Install the extension

<Tabs>
  <Tab title="Neovim">
    ### Manual Installation

    ```sh  theme={null}
    git clone https://github.com/augmentcode/augment.vim.git ~/.config/nvim/pack/augment/start/augment.vim
    ```

    ### Using Lazy.nvim

    Add the following to your `init.lua` file, then run `:Lazy sync` in Neovim. See more details about using [Lazy.nvim on GitHub](https://github.com/folke/lazy.nvim).

    ```lua  theme={null}
    require('lazy').setup({
      -- Your other plugins here
      'augmentcode/augment.vim',
    })
    ```
  </Tab>

  <Tab title="Vim">
    ### Manual Installation

    ```sh  theme={null}
    git clone https://github.com/augmentcode/augment.vim.git ~/.vim/pack/augment/start/augment.vim
    ```

    ### Using Vim Plug

    Add the following to your `.vimrc` file, then run `:PlugInstall` in Vim. See more details about using [Vim Plug on GitHub](https://github.com/junegunn/vim-plug).

    ```vim  theme={null}
    call plug#begin()

    " Your other plugins here
    Plug 'augmentcode/augment.vim'

    call plug#end()
    ```
  </Tab>
</Tabs>

## 2. Configure your workspace context

Add your project root to your workspace context by setting `g:augment_workspace_folders` in your `.vimrc` or `init.lua` file before the plugin is loaded. For example:

```vim  theme={null}
" Add to your .vimrc
let g:augment_workspace_folders = ['/path/to/project']

" Add to your init.lua
vim.g.augment_workspace_folders = {'/path/to/project'}
```

Augment's Context Engine provides the best suggestions when it has access to your project's codebase and any related repositories. See more details in
[Configure additional workspace context](/vim/setup-augment/workspace-context-vim).

## 3. Sign-in to Augment

Open Vim or Neovim and sign-in to Augment with the following command:

```vim  theme={null}
:Augment signin
```

<Next>
  * [Using Chat with Vim and Neovim](/vim/using-augment/vim-chat)
  * [Using Completions with Vim and Neovim](/vim/using-augment/vim-completions)
  * [Configure keyboard shortcuts](/vim/setup-augment/vim-keyboard-shortcuts)
</Next>


# Commands and shortcuts for Vim and Neovim
Source: https://docs.augmentcode.com/vim/setup-augment/vim-keyboard-shortcuts

Augment flexibly integrates with your editor to provide keyboard shortcuts for common actions. Customize your keymappings to quickly accept suggestions and chat with Augment.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## All available commands

| Command                                         | Action                                      |
| :---------------------------------------------- | :------------------------------------------ |
| <Keyboard shortcut=":Augment enable" />         | Globally enable suggestions (on by default) |
| <Keyboard shortcut=":Augment disable" />        | Globally disable suggestions                |
| <Keyboard shortcut=":Augment chat <message>" /> | Send a chat message to Augment              |
| <Keyboard shortcut=":Augment chat-new" />       | Start a new chat conversation               |
| <Keyboard shortcut=":Augment chat-toggle" />    | Toggle the chat panel visibility            |
| <Keyboard shortcut=":Augment signin" />         | Start the sign in flow                      |
| <Keyboard shortcut=":Augment signout" />        | Sign out of Augment                         |
| <Keyboard shortcut=":Augment status" />         | View the current status of the plugin       |
| <Keyboard shortcut=":Augment log" />            | View the plugin log                         |

## Creating custom shortcuts

You can create custom shortcuts for any of the above commands by adding mappings to your `.vimrc` or `init.lua` file. For example, to create a shortcut for the :Augment chat\* commands, you can add the following mappings:

```vim  theme={null}
" Send a chat message in normal and visual mode
nnoremap <leader>ac :Augment chat<CR>
vnoremap <leader>ac :Augment chat<CR>

" Start a new chat conversation
nnoremap <leader>an :Augment chat-new<CR>

" Toggle the chat panel visibility
nnoremap <leader>at :Augment chat-toggle<CR>
```

## Customizing accepting a completion suggestion

By default <Keyboard shortcut="Tab" /> is used to accept a suggestion. If you want to use a key other than <Keyboard shortcut="Tab" /> to accept a suggestion, create a mapping that calls `augment#Accept()`. The function takes an optional arugment used to specify the fallback text to insert if no suggestion is available.

```vim  theme={null}
" Use Ctrl-Y to accept a suggestion
inoremap <c-y> <cmd>call augment#Accept()<cr>

" Use enter to accept a suggestion, falling back to a newline if no suggestion
" is available
inoremap <cr> <cmd>call augment#Accept("\n")<cr>
```

You can disable the default <Keyboard shortcut="Tab" /> mapping by setting `g:augment_disable_tab_mapping = v:true` before the plugin is loaded.


# Add context to your workspace
Source: https://docs.augmentcode.com/vim/setup-augment/workspace-context-vim

You can add additional context to your workspace–such as additional repositories and folders–to give Augment a full view of your system.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

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

<Availability tags={["vim","neovim"]} />

## About Workspace Context

Augment is powered by its deep understanding of your code. You'll need to configure your project's source in your workspace context to get full codebase understanding in your chats and suggestions.

Sometimes important parts of your system exist outside of the current project. For example, you may have seperate frontend and backend repositories or have many services across multiple repositories. Adding additional codebases to your workspace context will improve the code suggestions and chat responses from Augment.

## Add context to your workspace

<Note>
  Be sure to set `g:augment_workspace_folders` before the Augment plugin is loaded.
</Note>

To add context to your workspace, in your `.vimrc` set `g:augment_workspace_folders` to a list of paths to the folders you want to add to your workspace context. For example:

```vim  theme={null}
let g:augment_workspace_folders = ['/path/to/folder', '~/path/to/another/folder']
```

You may want to ignore specific folders, like `node_modules`, see [Ignoring files with .augmentignore](/setup-augment/workspace-indexing#ignoring-files-with-augmentignore) for more details.

After adding a workspace folder and restarting Vim, the output of the <Keyboard shortcut=":Augment status" /> command will include the syncing progress for the added folder.


# Index your workspace
Source: https://docs.augmentcode.com/vim/setup-augment/workspace-indexing

When your workspace is indexed, Augment can provide tailored code suggestions and answers based on your unique codebase, best practices, coding patterns, and preferences. You can always control what files are indexed.

## About indexing your workspace

When you open a workspace with Augment enabled, your codebase will be automatically uploaded to Augment's secure cloud. You can control what files get indexed using `.gitignore` and `.augmentignore` files. Indexing usually takes less than a minute but can take longer depending on the size of your codebase.

## Security and privacy

Augment stores your code securely and privately to enable our powerful context engine. We ensure code privacy through a proof-of-possession API and maintain strict internal data minimization principles. [Read more about our security](https://www.augmentcode.com/security).

## What gets indexed

Augment will index all the files in your workspace, except for the files that match patterns in your `.gitignore` file and the `.augmentignore` file.

## Ignoring files with .augmentignore

The `.augmentignore` file is a list of file patterns that Augment will ignore when indexing your workspace. Create an `.augmentignore` file in the root of your workspace. You can use any glob pattern that is supported by the [gitignore](https://git-scm.com/docs/gitignore) file.

## Including files that are .gitignored

If you have a file or directory in your `.gitignore` that you want to indexed, you can add it to your `.augmentignore` file using the `!` prefix.

For example, you may want your `node_modules` indexed to provide Augment with context about the dependencies in their project, but it is typically included in their `.gitignore`. Add `!node_modules` to your `.augmentignore` file.

<CodeGroup>
  ```bash .augmentignore theme={null}
  # Include .gitignore excluded files with ! prefix
  !node_modules

  # Exclude other files with .gitignore syntax
  data/test.json
  ```

  ```bash .gitignore theme={null}
  # Exclude dependencies
  node_modules

  # Exclude secrets
  .env

  # Exclude build artifacts
  out
  build
  ```
</CodeGroup>


# Chat
Source: https://docs.augmentcode.com/vim/using-augment/vim-chat

Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

export const Next = ({children}) => <div className="border-t border-b pb-8 border-gray dark:border-white/10">
    <h3>Next steps</h3>
    {children}
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## Using chat

Chat is a new way to work with your codebase using natural language. Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

| Command                                         | Action                           |
| :---------------------------------------------- | :------------------------------- |
| <Keyboard shortcut=":Augment chat <message>" /> | Send a chat message to Augment   |
| <Keyboard shortcut=":Augment chat-new" />       | Start a new chat conversation    |
| <Keyboard shortcut=":Augment chat-toggle" />    | Toggle the chat panel visibility |

### Sending a message

You can send a message to Chat using the <Keyboard shortcut=":Augment chat" /> command. You can send your message as an optional argument to the command or enter it into the command-line when prompted. Each new message will continue the current conversation which will be used as context for your next message.

**Focusing on selected text**

If you have text selected in `visual mode`, Augment will automatically include it in your message. This is useful for asking questions about specific code or requesting changes to the selected code.

### Starting a new conversation

You can start a new conversation by using the <Keyboard shortcut=":Augment chat-new" /> command.

<Next>
  * [Using Completions](/vim/using-augment/vim-completions)
  * [Configure keyboard shortcuts](/vim/setup-augment/vim-keyboard-shortcuts)
</Next>


# Completions
Source: https://docs.augmentcode.com/vim/using-augment/vim-completions

Use code completions to get more done. Augment’s radical context awareness means more relevant suggestions, fewer hallucinations, and less time hunting down documentation.

export const Next = ({children}) => <div className="border-t border-b pb-8 border-gray dark:border-white/10">
    <h3>Next steps</h3>
    {children}
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## Using completions

Augment’s code completions integrates with Vim and Neovim to give you autocomplete-like suggestions as you type. Completions are enable by default and you can use <Keyboard shortcut="Tab" /> to accept a suggestion.

| Command                                  | Action                                      |
| :--------------------------------------- | :------------------------------------------ |
| <Keyboard shortcut="Tab" />              | Accept the current suggestion               |
| <Keyboard shortcut=":Augment enable" />  | Globally enable suggestions (on by default) |
| <Keyboard shortcut=":Augment disable" /> | Globally disable suggestions                |

### Customizing accepting a suggestion

If you want to use a key other than <Keyboard shortcut="Tab" /> to accept a suggestion, create a mapping that calls `augment#Accept()`. The function takes an optional arugment used to specify the fallback text to insert if no suggestion is available.

```vim  theme={null}
" Use Ctrl-Y to accept a suggestion
inoremap <c-y> <cmd>call augment#Accept()<cr>

" Use enter to accept a suggestion, falling back to a newline if no suggestion
" is available
inoremap <cr> <cmd>call augment#Accept("\n")<cr>
```

You can disable the default <Keyboard shortcut="Tab" /> mapping by setting `g:augment_disable_tab_mapping = v:true` before the plugin is loaded.

<Next>
  * [Using Chat](/vim/using-augment/vim-chat)
  * [Configure keyboard shortcuts](/vim/setup-augment/vim-keyboard-shortcuts)
</Next>


