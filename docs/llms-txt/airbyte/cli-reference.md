# Source: https://docs.airbyte.com/ai-agents/mcp-server/cli-reference.md

# Command line reference

Copy Page

All commands use `uv run agent-engine <command>`. Use `--help` on any command for full options.

## Global flags[​](#global-flags "Direct link to Global flags")

| Flag                 | Description                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `--config-dir`, `-d` | Config directory (default: `~/.airbyte_agent_mcp`). Can also be set with the `AIRBYTE_CONFIG_DIR` environment variable. |
| `--org`              | Organization ID to use, overriding the default set by `agent-engine login`.                                             |

## `agent-engine connectors list-oss`[​](#agent-engine-connectors-list-oss "Direct link to agent-engine-connectors-list-oss")

List available open source connectors from the Airbyte registry.

```
uv run agent-engine connectors list-oss
uv run agent-engine connectors list-oss --pattern salesforce
```

| Flag              | Description               |
| ----------------- | ------------------------- |
| `--pattern`, `-p` | Filter connectors by name |

## `agent-engine connectors list-cloud`[​](#agent-engine-connectors-list-cloud "Direct link to agent-engine-connectors-list-cloud")

List connectors configured in your Agent Engine organization. Requires [`agent-engine login`](#agent-engine-login) first.

```
uv run agent-engine connectors list-cloud
uv run agent-engine connectors list-cloud --customer acme
```

| Flag               | Description             |
| ------------------ | ----------------------- |
| `--customer`, `-c` | Filter by customer name |
| `--customer-id`    | Filter by customer ID   |

## `agent-engine connectors configure`[​](#agent-engine-connectors-configure "Direct link to agent-engine-connectors-configure")

Generate a connector configuration file by inspecting the connector's authentication requirements.

```
uv run agent-engine connectors configure --package airbyte-agent-gong
uv run agent-engine connectors configure --connector-id <your-connector-id>
```

| Flag                   | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| `--package`            | PyPI package name, local path, or `git+https://` URL |
| `--connector-id`, `-c` | Agent Engine connector ID                            |
| `--version`, `-v`      | Package version (PyPI only)                          |
| `--filename`, `-f`     | Output file path (auto-generated if not specified)   |
| `--overwrite`, `-o`    | Overwrite the output file if it already exists       |

## `agent-engine login`[​](#agent-engine-login "Direct link to agent-engine-login")

Save Agent Engine credentials to the global config directory. Prompts for your Client ID and Secret, then stores them for subsequent commands.

```
uv run agent-engine login <organization-id>
```

| Flag                | Description                                  |
| ------------------- | -------------------------------------------- |
| `<organization-id>` | Your Agent Engine organization ID (required) |

## `agent-engine orgs`[​](#agent-engine-orgs "Direct link to agent-engine-orgs")

Manage logged-in organizations.

```
uv run agent-engine orgs list
uv run agent-engine orgs default
uv run agent-engine orgs default <org-id>
```

| Subcommand         | Description                      |
| ------------------ | -------------------------------- |
| `list`             | List all logged-in organizations |
| `default`          | Show the default organization    |
| `default <org-id>` | Set the default organization     |

## `agent-engine mcp serve`[​](#agent-engine-mcp-serve "Direct link to agent-engine-mcp-serve")

Start the MCP server with a connector configuration.

```
uv run agent-engine mcp serve connector-gong-package.yaml
uv run agent-engine mcp serve connector-gong-package.yaml --transport http --port 8080
```

| Flag                | Default     | Description                            |
| ------------------- | ----------- | -------------------------------------- |
| `--transport`, `-t` | `stdio`     | Transport protocol (`stdio` or `http`) |
| `--host`, `-h`      | `127.0.0.1` | Host to bind to (HTTP only)            |
| `--port`, `-p`      | `8000`      | Port to bind to (HTTP only)            |

## `agent-engine mcp add-to`[​](#agent-engine-mcp-add-to "Direct link to agent-engine-mcp-add-to")

Register the MCP server with an agent. Supported targets: `claude-code`, `claude-desktop`, `cursor`, `codex`.

```
uv run agent-engine mcp add-to claude-code connector-gong-package.yaml
uv run agent-engine mcp add-to cursor connector-gong-package.yaml --scope project
```

| Flag            | Default | Description                                                    |
| --------------- | ------- | -------------------------------------------------------------- |
| `--name`, `-n`  | Auto    | Name for the MCP server (default: `airbyte-<connector>`)       |
| `--scope`, `-s` | `user`  | Configuration scope: `user` or `project` (Claude Code, Cursor) |

## `agent-engine chat`[​](#agent-engine-chat "Direct link to agent-engine-chat")

Chat with connector data using natural language in the terminal. Uses Claude and requires an `ANTHROPIC_API_KEY` environment variable. Pass a prompt argument for one-shot mode, or omit it to start an interactive REPL.

```
uv run agent-engine chat connector-gong-package.yaml "show me 5 recent calls"
uv run agent-engine chat connector-gong-package.yaml
```

| Flag            | Default           | Description                                  |
| --------------- | ----------------- | -------------------------------------------- |
| `--model`, `-m` | `claude-opus-4-6` | Anthropic model to use                       |
| `--quiet`, `-q` | `false`           | Only show the final answer (hide tool calls) |
