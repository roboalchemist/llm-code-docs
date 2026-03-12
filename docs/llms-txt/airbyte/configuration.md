# Source: https://docs.airbyte.com/ai-agents/mcp-server/configuration.md

# Configure the MCP server

Copy Page

<!-- -->

You configure the Agent Engine MCP server with a YAML file that specifies which connector to use and how to authenticate. This page covers the configuration file format, execution modes, credential management, and aggregate configurations for running multiple connectors.

If you need help getting started with the MCP server, complete the [tutorial](/ai-agents/tutorials/quickstarts/tutorial-mcp-server.md) first.

## Configuration file format[​](#configuration-file-format "Direct link to Configuration file format")

Place the configuration file in the folder from which you run the MCP server. The file has two required sections.

| Key           | Description                                                                                                       |
| ------------- | ----------------------------------------------------------------------------------------------------------------- |
| `connector`   | Specifies the connector source. This can be a PyPI package, a git URL, a local path, or an agent connector ID.    |
| `credentials` | A key-value map of authentication fields. Values use `${env.VAR_NAME}` syntax to reference environment variables. |

This is an example of the file format.

connector-gong-package.yaml

```
connector:
  package: airbyte-agent-gong
credentials:
  access_key: ${env.GONG_ACCESS_KEY}
  access_key_secret: ${env.GONG_ACCESS_KEY_SECRET}
```

Some connectors also accept a `config` section for additional parameters like subdomains or workspace IDs. The `agent-engine connectors configure` command generates the correct structure for each connector.

You can [configure multiple connectors](#use-multiple-connectors-with-one-mcp-server) in the same MCP server.

## Open source mode[​](#open-source-mode "Direct link to Open source mode")

In open source mode, the MCP server installs a connector package and calls the third-party API directly using your credentials. This mode only supports the operations the third-party API provides. It doesn't support using the Agent Engine's search or the [context store](/ai-agents/platform/context-store.md). Search operations are only possible if the third-party has search endpoints, and are limited to the capabilities and rate limiting of those endpoints.

### PyPI packages[​](#pypi-packages "Direct link to PyPI packages")

The most common configuration. Run `uv run agent-engine connectors list-oss` to see available packages and their versions, then specify a package name from the Airbyte connector registry.

connector-gong-package.yaml

```
connector:
  package: airbyte-agent-gong
credentials:
  access_key: ${env.GONG_ACCESS_KEY}
  access_key_secret: ${env.GONG_ACCESS_KEY_SECRET}
```

To pin a specific version:

connector-gong-package.yaml

```
connector:
  package: airbyte-agent-gong
  version: 0.1.13
credentials:
  access_key: ${env.GONG_ACCESS_KEY}
  access_key_secret: ${env.GONG_ACCESS_KEY_SECRET}
```

### Git URLs[​](#git-urls "Direct link to Git URLs")

Point the connector to a git repository.

connector-gong-package.yaml

```
connector:
  git: https://github.com/org/repo.git
credentials:
  token: ${env.MY_TOKEN}
```

You can specify a branch or tag with `ref` and a subdirectory with `subdirectory`.

connector-gong-package.yaml

```
connector:
  git: https://github.com/org/repo.git
  ref: main
  subdirectory: connectors/my-connector
credentials:
  token: ${env.MY_TOKEN}
```

### Local path[​](#local-path "Direct link to Local path")

Point the connector to a local directory.

connector-gong-package.yaml

```
connector:
  path: ../integrations/my-connector/.generated
credentials:
  token: ${env.MY_TOKEN}
```

### Manage credentials[​](#manage-credentials "Direct link to Manage credentials")

Credential values use `${env.VAR_NAME}` syntax. The MCP server resolves these placeholders at startup by reading from the process environment.

```
credentials:
  access_key: ${env.GONG_ACCESS_KEY}
  access_key_secret: ${env.GONG_ACCESS_KEY_SECRET}
```

The `agent-engine` command line tool automatically loads `.env` files from the current working directory. Create a `.env` file alongside your connector configuration:

.env

```
GONG_ACCESS_KEY=your-access-key
GONG_ACCESS_KEY_SECRET=your-secret
```

warning

Never commit your `.env` file to version control. Add `.env` to your `.gitignore` file. If you commit credentials by mistake, rotate them immediately.

## Hosted mode[​](#hosted-mode "Direct link to Hosted mode")

In hosted mode, the MCP server proxies API calls through the Agent Engine. This mode supports search and filter queries because Agent Engine keeps data indexed in the [context store](/ai-agents/platform/context-store.md).

Hosted mode uses your Agent Engine credentials (client ID and secret) instead of third-party API credentials. You authenticate once, then the CLI remembers your credentials for subsequent commands.

### Before you begin[​](#before-you-begin "Direct link to Before you begin")

Before you can use a connector in hosted mode, you need to [authenticate with that connector](/ai-agents/platform/authenticate/hosted.md).

### Step 1: Log in to Agent Engine[​](#step-1-log-in-to-agent-engine "Direct link to Step 1: Log in to Agent Engine")

Run `agent-engine login` with your organization ID. This opens a link to your Airbyte authentication page where you can find your Client ID and Secret.

```
uv run agent-engine login <organization-id>
```

The command prompts for your client ID and secret, saves them to `~/.airbyte_agent_mcp/orgs/<organization-id>/.env`, and sets the organization as the default. All subsequent `agent-engine` commands automatically load these credentials.

### Step 2: Find your connector ID[​](#step-2-find-your-connector-id "Direct link to Step 2: Find your connector ID")

List the connectors configured in your organization:

```
uv run agent-engine connectors list-cloud
```

Use `--customer` to filter by customer name:

```
uv run agent-engine connectors list-cloud --customer acme
```

### Step 3: Generate a configuration[​](#step-3-generate-a-configuration "Direct link to Step 3: Generate a configuration")

Pass the connector ID from the previous step:

```
uv run agent-engine connectors configure --connector-id <your-connector-id>
```

This generates a configuration file like this:

connector-gong-cloud.yaml

```
connector:
  connector_id: <your-connector-id>
credentials:
  airbyte_client_id: ${env.AIRBYTE_CLIENT_ID}
  airbyte_client_secret: ${env.AIRBYTE_CLIENT_SECRET}
```

### Managing multiple organizations[​](#managing-multiple-organizations "Direct link to Managing multiple organizations")

If you work with multiple Agent Engine organizations, you can log into each one and switch between them.

```
uv run agent-engine orgs list                  # List logged-in organizations
uv run agent-engine orgs default <org-id>      # Set the default organization
uv run agent-engine --org <org-id> <command>   # Override for a single command
```

## Use multiple connectors with one MCP server[​](#use-multiple-connectors-with-one-mcp-server "Direct link to Use multiple connectors with one MCP server")

You don't need to create separate MCP servers for each connector. Instead, create a YAML file that references all your individual connector config files.

| Key       | Description                                                                                         |
| --------- | --------------------------------------------------------------------------------------------------- |
| `name`    | Sets the MCP server name                                                                            |
| `configs` | Lists paths to individual connector configuration files, relative to the aggregate file's directory |

connectors.yaml

```
name: airbyte-crm-suite
configs:
  - connector-gong-package.yaml
  - connector-salesforce-cloud.yaml
```

The `name` field sets the MCP server name. The `configs` field lists paths to individual connector configuration files (relative to the aggregate file's directory).

Then, register the aggregate config with your agent the same way you would a single connector.

* Claude Code
* Claude Desktop
* Cursor
* Codex

This command runs `claude mcp add` under the hood and registers the server at the user scope.

```
uv run agent-engine mcp add-to claude-code connectors.yaml
```

To register at the project scope instead, add `--scope project` to that command.

This command modifies your Claude Desktop configuration file directly.

```
uv run agent-engine mcp add-to claude-desktop connectors.yaml
```

This modifies the Cursor MCP configuration file.

```
uv run agent-engine mcp add-to cursor connectors.yaml
```

To register at the project scope instead of user scope, add a `--scope project` flag.

This command runs `codex mcp add` to register the server.

```
uv run agent-engine mcp add-to codex connectors.yaml
```

You can optionally specify a custom name for the server with `--name`:

```
uv run agent-engine mcp add-to claude-code connector-github-package.yaml --name my-server-name
```

For a full list of all `agent-engine` commands and their options, see the [CLI reference](/ai-agents/mcp-server/cli-reference.md).
