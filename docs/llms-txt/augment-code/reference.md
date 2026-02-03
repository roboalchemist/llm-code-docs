# Source: https://docs.augmentcode.com/cli/reference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CLI Flags and Options

> A comprehensive reference for all command-line flags available in the Auggie CLI.

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

<Note>Skills are loaded automatically from `.augment/skills/` and `.claude/skills/` directories in both your workspace and home directory. See [Skills](/cli/skills) for more information.</Note>

### Models

List out available models and their short names to be passed into the `--model` flag

| Command              | Description           |
| :------------------- | :-------------------- |
| `auggie models list` | List available models |

### Tools

Manage which tools are available to the agent. You can temporarily disable tools for a session or persistently manage them via settings.

| Command                            | Description                                                                              |
| :--------------------------------- | :--------------------------------------------------------------------------------------- |
| `auggie --remove-tool <tool-name>` | Remove a specific tool by name for the current session. Can be specified multiple times. |
| `auggie tools list`                | List all available tools and their current status                                        |
| `auggie tools remove <tool-name>`  | Persistently remove a tool by adding it to the `removedTools` list in settings.json      |
| `auggie tools add <tool-name>`     | Re-enable a previously removed tool by removing it from the `removedTools` list          |

**Examples:**

```sh  theme={null}
# Disable the web-fetch tool for this session
auggie --remove-tool web-fetch

# Disable multiple tools for this session
auggie --remove-tool web-fetch --remove-tool web-search

# Persistently disable a tool
auggie tools remove launch-process

# Re-enable a previously disabled tool
auggie tools add launch-process

# See all tools and their status
auggie tools list
```

<Note>Command-line `--remove-tool` flags take precedence over settings. For fine-grained control over tool behavior (allow, deny, ask-user), see [Permissions](/cli/permissions).</Note>

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

### MCP Server Mode

Run Auggie as an MCP server to expose the codebase-retrieval tool to external AI tools like Claude Code, Cursor, and others.

| Flag                   | Description                                                                                       |
| :--------------------- | :------------------------------------------------------------------------------------------------ |
| `--mcp`                | Run Auggie as an MCP tool server. Uses the current working directory as the workspace by default. |
| `--mcp-auto-workspace` | Enable automatic workspace discovery based on client requests (added in v0.14.0)                  |
| `-w /path/to/project`  | Specify a workspace to index                                                                      |

#### Automatic Workspace Discovery

The `--mcp-auto-workspace` flag enables dynamic workspace discovery in MCP mode. When enabled:

* The `codebase-retrieval` tool accepts a `directory_path` parameter to specify which workspace to search
* Workspaces are indexed on-demand when first accessed
* Multiple workspaces can be searched within a single MCP server session

This is useful when the MCP client (e.g., Claude Code) needs to work with multiple projects or when the workspace isn't known at startup time.

You can combine `--mcp-auto-workspace` with `-w` to pre-index a primary workspace at startup while still allowing dynamic discovery of additional workspaces. This is useful for large workspaces that take time to index, or to reduce latency on the first query to your main project.

**Examples:**

```bash  theme={null}
# MCP server with auto-discovery (recommended)
auggie --mcp --mcp-auto-workspace

# Pre-index a workspace, allow dynamic discovery of others
auggie --mcp --mcp-auto-workspace -w /path/to/primary/project

# Use only a single workspace path
auggie --mcp -w /path/to/project

# Use current working directory as the workspace
auggie --mcp
```

<Note>When using `--mcp-auto-workspace`, the first query to a new workspace may take longer as the workspace is indexed. Subsequent queries to the same workspace will be fast.</Note>

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

### Shell Environment

When Auggie executes shell commands using the `launch-process` tool, it sets the following environment variable:

| Variable        | Description                                                                                                                        |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `AUGMENT_AGENT` | Set to `1` when a command is executed by Auggie. Scripts can check for this variable to detect if they are being run by the agent. |

**Example usage in a script:**

```sh  theme={null}
if [ -n "$AUGMENT_AGENT" ]; then
  echo "Running inside Auggie"
  # Adjust behavior for agent execution
fi
```

## See Also

* [Custom Rules and Guidelines](/cli/rules) - Configure custom rules for project-specific guidance
* [Skills](/cli/skills) - Extend capabilities with specialized domain knowledge
* [Custom Commands](/cli/custom-commands) - Create reusable command templates
* [Permissions](/cli/permissions) - Configure tool permissions and security
* [Integrations](/cli/integrations) - Connect external tools and services
