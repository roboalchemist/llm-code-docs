# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/commands.md

# Commands

Tabnine CLI supports built-in commands to help you manage your session, customize the interface, and control its behavior. Commands are prefixed with `/`, `@`, or `!`.

### Slash Commands (`/`)

Slash commands provide meta-level control over the CLI.

| Command                   | Description                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Core Commands**         |                                                                                                               |
| `/help` or `/?`           | Display help information about Tabnine CLI, including available commands and their usage.                     |
| `/about`                  | Show version information. Share this when filing issues.                                                      |
| `/auth`                   | Open a dialog to change the authentication method.                                                            |
| `/quit` or `/exit`        | Exit Tabnine CLI.                                                                                             |
| `/clear`                  | Clear the terminal screen and scrollback. **Shortcut**: `Ctrl+L`                                              |
| **Session Management**    |                                                                                                               |
| `/chat save <tag>`        | Save current conversation with a tag.                                                                         |
| `/chat resume <tag>`      | Resume a saved conversation.                                                                                  |
| `/chat list`              | List available saved conversations.                                                                           |
| `/chat delete <tag>`      | Delete a saved conversation.                                                                                  |
| `/chat share <file.md>`   | Export conversation to Markdown or JSON.                                                                      |
| `/resume`                 | Browse and resume previous conversation sessions interactively.                                               |
| `/restore [tool_call_id]` | Restore project files to the state before a tool was executed. Lists available checkpoints if no ID provided. |
| `/compress`               | Replace chat context with a summary to save tokens while retaining history.                                   |
| **Tools & Functionality** |                                                                                                               |
| `/mcp list` or `/mcp ls`  | List configured MCP servers and tools.                                                                        |
| `/mcp desc`               | List with descriptions.                                                                                       |
| `/mcp schema`             | List with descriptions and schemas.                                                                           |
| `/mcp auth <server>`      | Authenticate with OAuth-enabled server.                                                                       |
| `/mcp refresh`            | Restart all MCP servers.                                                                                      |
| `/tools [desc]`           | Display available tools.                                                                                      |
| **Memory Management**     |                                                                                                               |
| `/memory add <text>`      | Add text to AI's memory.                                                                                      |
| `/memory show`            | Display full memory content.                                                                                  |
| `/memory refresh`         | Reload from `TABNINE.md` files.                                                                               |
| `/memory list`            | List paths of `TABNINE.md` files.                                                                             |
| **Directory Management**  |                                                                                                               |
| `/directory add <path>`   | Add directories to workspace.                                                                                 |
| `/directory show`         | Display all workspace directories.                                                                            |
| **Configuration**         |                                                                                                               |
| `/model`                  | Open dialog to choose your AI model. See Model Selection.                                                     |
| `/settings`               | Open settings editor to view and modify Tabnine CLI settings. See Settings.                                   |
| `/theme`                  | Open dialog to change the visual theme. See Themes.                                                           |
| `/editor`                 | Open dialog for selecting supported editors.                                                                  |
| `/vim`                    | Toggle vim mode on/off.                                                                                       |
| **Utilities**             |                                                                                                               |
| `/copy`                   | Copy last output to clipboard. Requirements: Linux: `xclip` or `xsel`, macOS: `pbcopy`, Windows: `clip`.      |
| `/stats`                  | Display session statistics (token usage, cached tokens, duration).                                            |
| `/bug <description>`      | File an issue about Tabnine CLI.                                                                              |
| `/init`                   | Analyze current directory and generate a tailored `TABNINE.md` file.                                          |
| `/hooks`                  | Manage hooks (if enabled). See Hooks.                                                                         |
| `/permissions`            | Manage folder trust settings (if enabled).                                                                    |

***

### At Commands (`@`)

Include file/directory content in your prompt.

#### @

Inject file or directory content.

Examples:

```
@src/index.ts Explain this code
@docs/ Summarize these documents
What is @README.md about?
```

Features:

* Git-aware filtering (excludes `node_modules/`, `.git/`, etc.)
* Recursive directory reading
* Escape spaces: `@My\ Documents/file.txt`

Note: Uses `read_many_files` tool internally

#### @ (lone)

Pass literal `@` symbol to model.

***

### Shell Mode (`!`)

Execute shell commands directly.

#### !

Execute a shell command and return to Tabnine CLI.

Examples:

```
!ls -la
!git status
!npm test
```

Shells:

* Linux/macOS: `bash`
* Windows: `powershell.exe -NoProfile -Command`

#### ! (toggle)

Toggle shell mode on/off. When active, all input is interpreted as shell commands.

Environment: Commands run with `TABNINE_CLI=1` environment variable set.

{% hint style="danger" %}
**Warning:** Commands executed via the Tabnine CLI will have the same system permissions as the user running the CLI.
{% endhint %}

***

### Custom Commands

Custom commands are reusable shortcuts for frequently-used prompts, enhancing efficiency and maintaining consistency.

#### Creating Custom Commands

Custom commands are stored in your settings and can be global or project-specific:

* **Global commands**: Located in `~/.tabnine/agent/commands/`
* **Project-specific commands**: Located in `<your-project-root>/.tabnine/agent/commands/`

If a project command has the same name as a global command, the project command takes precedence.

Command names are based on file paths relative to the `commands` directory. Subdirectories create namespaced commands; path separators convert to colons (`:`). For example:

* Global: `~/.tabnine/agent/commands/review.toml` becomes `/review`
* Project-specific: `<project>/.gemini/commands/code/review.toml` becomes `/code:review`

#### TOML File Format

* **Fields**:
  * `prompt` (String) - *Required*: The prompt executed by the model.
  * `description` (String) - *Optional*: A brief description shown in the `/help` menu.

**Example**

`~/.tabnine/commands/review.toml`

```toml
prompt = "Review the following code for: - Security vulnerabilities - Performance issues - Best practices - Code quality"
description = "Review code for best practices"
```

#### Using Custom Commands

Invoke commands like `/review @src/index.ts`. Templates expand with additional input.

#### Shell Injection

Integrate shell outputs using `!{...}` within the `prompt`. This gathers local context, e.g., file content or Git status. Upon shell command execution, confirmation is required for security.

#### Context Injection

* `{{args}}`: Replaced with user-typed text. When used Inside `!{...}`, arguments are shell-escaped.

#### File Content Injection

Embed file or directory content with `@{...}` syntax.

#### Custom Command Example

Explore a sample `.toml` configuration for context and file content injection in a command script.

```toml
# File: ~/.gemini/commands/review/pr.toml
# Usage: /review:pr <PR_number>

description = "Reviews a GitHub PR with full context including diff, file contents, and CI status"

prompt = """
You are an experienced code reviewer. Please review the following pull request comprehensively.

## Pull Request: {{args}}

### Current Branch Status
!{git branch --show-current}

### Changes in this PR
!{git diff main...HEAD}

### Modified Package Configuration
@{package.json}

### CI/CD Status
!{gh pr view {{args}} --json statusCheckRollup --jq '.statusCheckRollup[].conclusion'}

Please provide:
1. A summary of changes for PR #{{args}}
2. Potential bugs or issues
3. Security concerns
4. Performance implications
5. Suggestions for improvement

Focus on code quality, maintainability, and adherence to best practices.
"""

```

#### Explanation:

* **`{{args}}` - User Arguments**: Captures the PR number to customize the command for any PR.
* **`!{...}` - Live Command Execution**: Executes shell commands in real-time:
  * Retrieves the current git branch.
  * Generates the diff between `main` and `HEAD`.
  * Fetches CI/CD test results using GitHub CLI.
  * Combines with `{{args}}` for specific PR status.
* **`@{...}` - File Content Injection**: Injects `package.json` content into the prompt, providing insight into dependencies and project configurations.

This setup automates comprehensive code reviews for GitHub PRs by assembling all relevant information - PR number, code changes, test status, and files - into a single, structured prompt.

#### Best Practices

* **Focus**: One clear purpose per command.
* **Naming**: Use descriptive, brief names.
* **Descriptions**: Aid in command recall.
* **Version Control**: Commit `.tabnine/commands/` for team use.

#### Listing Custom Commands

Use `/help` to see custom commands alongside built-in options.
