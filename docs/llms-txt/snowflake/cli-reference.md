# Source: https://docs.snowflake.com/en/user-guide/cortex-code/cli-reference.md

# Cortex Code CLI reference

Command line reference for Cortex Code CLI.

## Starting Cortex Code

| Command | Description |
| --- | --- |
| `cortex` | Start in current directory |
| `cortex -c production` | Start with specific connection |
| `cortex -w /path/to/project` | Start in specific directory |
| `cortex -w /new/project -c myconn` | Combine workdir and connection |
| `cortex --continue` | Continue last session |
| `cortex --resume <session_id>` | Resume specific session |

## CLI options

| Option | Description |
| --- | --- |
| `-c, --connection <name>` | Use specific Snowflake connection |
| `-w, --workdir <path>` | Set working directory for file operations |
| `-m, --model <model_name>` | Specify AI model to use |
| `--plan` | Plan mode: require approval before all actions |
| `--bypass` | Automatically approve all planned actions |
| `--dangerously-allow-all-tool-calls` | Disable tool call permission prompts (caution) |
| `--continue` | Resume most recent conversation |
| `-r, --resume <session_id>` | Resume specific session by ID, or `last` for last session |
| `-p, --print  "<prompt>"` | Pass specified prompt, print response, and exit |
| `-f, --file <file>` | Read prompt from file, execute, and exit |
| `--output-format stream-json` | JSON output (for scripting) |
| `-V, --version` | Show installed version |
| `--help` | Show CLI help |

Connections must be defined in `~/.snowflake/connections.toml`. See [Cortex Code CLI](cortex-code-cli.md) for connection setup. Session IDs are shown at startup, at exit, and stored in `~/.snowflake/cortex/conversations/`.

### Examples

Start with working directory:

```bash
cortex -w /path/to/project
```

Resume last session with specific connection:

```bash
cortex --continue -c production
```

One-off prompt (JSON output):

```bash
cortex -p "List all Python files" --output-format stream-json
```

## Commands

### `update`

| Command | Description |
| --- | --- |
| `cortex update` | Update to latest version |
| `cortex --version` | Verify after update |

### `mcp`

| Command | Description |
| --- | --- |
| `cortex mcp list` | List configured servers |
| `cortex mcp add` | Add new server (interactive) |
| `cortex mcp remove <server_name>` | Remove server |

See [Model Context Protocol (MCP)](extensibility.md) for details.

## Interactive mode

### Keyboard shortcuts

| Shortcut | Action |
| --- | --- |
| `Ctrl+C` | Cancel current operation |
| `Ctrl+C Ctrl+C` | Exit Cortex Code CLI |
| `Ctrl+L` | Clear terminal screen (keeps conversation) |
| `Up/Down arrows` | Navigate command history |
| `Tab` | Command completion |

### Slash commands

#### Session management

| Command | Description |
| --- | --- |
| `/help` | Show interactive help |
| `/plan` | Enable planning mode |
| `/plan_off` | Disable planning mode |
| `/clear`, `/cls` | Clear the screen |
| `/new` | Start a new session |
| `/rename <title>` | Rename current session |
| `/exit`, `/quit` | Exit Cortex Code CLI |
| `/resume`, `/r`, `/sessions` | List and resume sessions |
| `/rewind` | Go back *n* steps in conversation or pick interactively |
| `/skill list` | List available skills |
| `/mcp-status` | Show MCP server status |
| `/fork` | Fork current session into a new session |

#### Model and mode

| Command | Description |
| --- | --- |
| `/model` | Show/select AI model |
| `/plan` | Enable plan mode |
| `/plan-off` | Disable plan mode |
| `/bypass` | Enable bypass mode (auto-approve all including tool calls) |
| `/bypass-off` | Disable bypass mode |
| `/status` | Show current configuration |

#### Snowflake and data

| Command | Description |
| --- | --- |
| `/sql <query>` | Execute SQL query |
| `/sql <query> --limit <n>` | Limit displayed rows |
| `/table [<file>]`, `/csv` | Open table viewer |
| `/connections`, `/conn` | Manage Snowflake connections |

#### Development tools

| Command | Description |
| --- | --- |
| `/sh`, `! <command>` | Execute shell command |
| `/diff`, `/changes`, `/review` | Review git changes |
| `/worktree` | Manage git worktrees |
| `/dbt` | dbt operations |
| `/lineage` | dbt lineage visualization |

#### Configuration

| Command | Description |
| --- | --- |
| `/settings` | View/modify settings |
| `/theme` | Select color theme |
| `/sandbox` | Manage sandbox settings |
| `/add-dir <path>` | Add working directory |

#### Extensibility

| Command | Description |
| --- | --- |
| `/skill`, `/skills` | Manage skills |
| `/mcp` | MCP server status |
| `/hooks` | View hooks configuration |
| `/commands`, `/cmds` | Manage custom commands |
| `/agents` | View subagents |

#### Utilities

| Command | Description |
| --- | --- |
| `/tasks` | Show task list |
| `/feedback` | Provide session feedback (Saved locally as a .tgz file) |
| `/update` | Update Cortex Code |

### Session storage

| Command | Description |
| --- | --- |
| `~/.snowflake/cortex/conversations/` | Session files |
| `~/.snowflake/cortex/settings.json` | General settings |
| `~/.snowflake/cortex/permissions.json` | Permission preferences |

See [Cortex Code CLI Settings](settings.md) for configuration details.

### Command details

#### `/sql`: Execute SQL examples

Basic query:

```text
/sql SELECT * FROM users
```

With row limit:

```text
/sql SELECT * FROM large_table --limit 1000
```

Multi-line (use Ctrl+J for newlines);

```text
/sql SELECT
  customer_id,
  SUM(amount) as total
FROM orders
GROUP BY customer_id
```

Results open automatically in the table viewer (Ctrl+T).

#### `/worktree`: Git worktrees

| Command | Description |
| --- | --- |
| `/worktree create feature-branch` | Create new worktree |
| `/worktree list` | List all worktrees |
| `/worktree switch feature-branch` | Switch to worktree |
| `/worktree delete feature-branch` | Delete worktree |

#### `/sandbox`: Sandbox control

| Command | Description |
| --- | --- |
| `/sandbox` | Interactive selector |
| `/sandbox on` | Enable container sandbox |
| `/sandbox off` | Disable container sandbox |
| `/sandbox status` | Show sandbox status |
| `/sandbox runtime on` | Enable OS sandbox |
| `/sandbox runtime off` | Disable OS sandbox |
| `/sandbox mode auto` | Auto-allow sandboxed commands |
| `/sandbox mode regular` | Prompt for all commands |

#### `/mcp`: MCP servers

| Command | Description |
| --- | --- |
| `/mcp` | Show status viewer |
| `/mcp list` | List all servers |
| `/mcp start <server>` | Start server |
| `/mcp get <server>` | Get server details |
| `/mcp remove <server>` | Remove server |

## Batch mode

| Command | Description |
| --- | --- |
| `cortex -p "<prompt>"` | Run single prompt and exit |
| `cortex -f request.txt` | Read prompt from file |
| `cortex --output-format stream-json -p "<prompt>"` | JSON output |
| `cortex -c prod --workdir /app -p "..."` | Control context |

## Exit codes

| Code | Description |
| --- | --- |
| `0` | Success |
| `1` | General error |
| `2` | Configuration error |
| `3` | Connection error |
| `4` | Permission denied |
| `130` | Interrupted by user (Ctrl+C) |

## Configuration and setup

### Updating Cortex Code CLI

Cortex Code CLI updates itself when a new version is available. You can also manually update to the latest version
by issuing `cortex update`. Issue `cortex update <version>` to install the specified version.

To disable automatic updates, edit `~/.snowflake/cortex/settings.json` and add `"autoUpdate": false`.

### Manually adding a connection

To manually create or edit the `~/.snowflake/connections.toml` file to define your connection, follow the steps below:

1. Create the `~/.snowflake/connections.toml` file if it doesn’t already exist.

   ```shell
   mkdir -p ~/.snowflake
   touch ~/.snowflake/connections.toml
   ```

2. Use the `chmod` command to set its permissions so that only you can read and write it.

   ```shell
   chmod 600 ~/.snowflake/connections.toml
   ```

3. Open the file in a text editor (here, `nano`).

   ```shell
   nano ~/.snowflake/connections.toml
   ```

4. Add lines like the following to define a connection. Enter the name of the connection in place of `myaccount` and
   replace the placeholder values with your Snowflake account details. Use browser-based SSO (external browser
   authentication) or PAT (programmatic access token). You can obtain a PAT from Snowsight (see
   [Using programmatic access tokens for authentication](../programmatic-access-tokens.md)). Include only the `authenticator` value or `password` value,
   depending on the authentication method you choose.

   ```toml
   [myaccount]
   account       = "<ACCOUNT>"
   user          = "<USERNAME>"
   authenticator = "externalbrowser" # For browser-based SSO; omit for PAT
   password      = "<PAT>"           # For PAT authentication; omit for SSO
   warehouse     = "<WAREHOUSE>"
   role          = "<ROLE>"
   database      = "<DATABASE>"
   schema        = "<SCHEMA>"
   ```

5. Save and close the file.

### Setting up shell completions

To give your shell the ability to auto-complete Cortex Code CLI commands and options, follow the instructions below for your shell.

> **Tip:**
>
> If you’re not sure which shell you’re using, issue `echo $(basename $SHELL)` in your terminal. The name printed is the default
> shell for your account, and may not be accurate if you have started a different shell manually.

| Shell | Command |
| --- | --- |
| `bash` | `cortex completion bash > ~/.bash_completion.d/cortex` |
| `zsh` | `cortex completion zsh > ~/.zsh/completions/_cortex` |
| `fish` | `cortex completion fish > ~/.config/fish/completions/cortex.fish` |

After running the appropriate command above for your shell, restart your shell with `exec $SHELL`.

### Directory structure

Installing Cortex Code CLI creates the following directory structure in your home directory:

```text
~/.snowflake/cortex/
   ├── settings.json          # Main configuration
   ├── mcp.json               # MCP server configs
   ├── conversations/         # Session history
   ├── skills/                # Global skills
   ├── commands/              # Custom commands
   ├── hooks/                 # Hook scripts
   ├── profiles/              # Team profiles
   └── cache/                 # Temporary cache
```

## Troubleshooting

Following are common error messages you may encounter during installation and setup.

### Command not found

Make sure that the installation directory `~/.local/bin` is included in your `PATH` environment variable.
For example, if you are using `bash`, issue the following commands:

```shell
export PATH="~/.local/bin:$PATH"
echo 'export PATH="~/.local/bin:$PATH"' >> ~/.bashrc
```

### Permission denied

Make sure that the `cortex` executable has execute permissions. Issue the following command:

```shell
chmod +x ~/.local/bin/cortex
```

### Connection errors

Make sure that the connection file `~/.snowflake/connections.toml` exists and contains valid connection details.

```shell
cat ~/.snowflake/connections.toml
```

Try invoking the `cortex` command with a connection explicitly specified using the `-c` option. For example:

```shell
cortex -c myaccount
```

## See also

[Cortex Code CLI](cortex-code-cli.md)
:   Installation, setup, and first prompts

[Cortex Code CLI Settings](settings.md)
:   Configuration file reference

[Cortex Code CLI workflow examples](workflows.md)
:   Capabilities and workflow examples
