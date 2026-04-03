# The Rover init Command

Rover enables you to create a graph or MCP server with a single interactive command.

## Initializing a graph

### `rover init`

Running `rover init` starts a short wizard that helps you create a new graph.

```terminal
rover init
```

The wizard walks you through a set of questions to help you choose the best option for your use case. When you're done, you'll have:

* A new graph in GraphOS
* A set of local configuration files and boilerplate code that represent the graph
* Credentials to interact with GraphOS
  * These credentials are necessary for actions like [developing your graph locally](https://www.apollographql.com/docs/rover/commands/dev) or [publishing graph updates](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/publish).

#### Options

You can also pass options directly to `rover init` instead of answering prompts in the wizard. The wizard still asks for any information not provided via an option and will always ask for confirmation before creating any files locally.

```terminal
rover init \
  --project-type <PROJECT_TYPE> \
  --org-id <ORGANIZATION_ID> \
  --project-use-case <PROJECT_USE_CASE> \
  --project-name <PROJECT_NAME> \
  --graph-id <GRAPH_ID>
```

For `rover init --mcp` options, see the [Initializing an MCP Server](https://www.apollographql.com/docs/rover/commands/init.md#initializing-an-mcp-server) section.

##### Available options

| Option               | Description                                                                                                                                                                | Possible Values                   |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| `--project-type`     | Whether to create a new graph or add a subgraph to an existing graph.                                                                                                      | `create-new`, `add-subgraph`      |
| `--org-id`           | The ID of the [GraphOS organization](https://www.apollographql.com/docs/graphos/platform/access-management/org#view-your-organizations) where the graph should be created. | *(your organization ID)*          |
| `--project-use-case` | Helps preconfigure your graph for specific patterns.                                                                                                                       | `connectors`, `graph-ql-template` |
| `--project-name`     | The name for your new graph.                                                                                                                                               | *(your graph name)*               |
| `--graph-id`         | The ID for your graph in GraphOS. (This must be a unique identifier.)                                                                                                      | *(your graph ID)*                 |
| `--mcp`              | See the [Initializing an MCP Server](https://www.apollographql.com/docs/rover/commands/init.md#initializing-an-mcp-server) section.                                        |                                   |

#### Choosing your use case

Once you run `rover init`, the wizard prompts you to select your use case.

* **Start a graph with one or more REST APIs**
  * Select this option to integrate REST APIs into your graph using Apollo Connectors.
* **Start a graph with recommended libraries**
  * Select this option if you want to integrate data that's not accessible via a REST API. This option helps you set up a graph using the Apollo Server library.

#### Created credentials

After you've chosen your use case, the wizard prompts you for a project name. It generates the following credentials based on the name you enter:

* **Graph ID**- A unique identifier for your graph. It represents your graph across all of Apollo.
* **Graph ref**- A reference for a specific variant of your graph. It's formatted `graph-id@variant`. To start, GraphOS automatically creates a variant titled `current` for you.
* **Graph API key**- Once it's generated, store it securely—you won't be able to access it later.
  * See the [configuration docs](https://www.apollographql.com/docs/rover/configuring#with-an-environment-variable) to learn how to set your API key as an environment variable

### Next steps

Once you've completed the wizard, it provides a [`rover dev`](https://www.apollographql.com/docs/rover/commands/dev) command with prepopulated credentials. Run this command to start developing your graph.

```terminal
rover dev --supergraph-config supergraph.yaml
```

##### Powershell

```terminal
rover dev --supergraph-config supergraph.yaml
```

##### Command Prompt

```terminal
rover dev --supergraph-config supergraph.yaml
```

If you started with TypeScript, you also need to run the following commands in a separate terminal window before running `rover dev`:

```terminal
npm ci
npm start
```

These commands start a subgraph server that `rover dev` depends on. Learn more in the `GETTING_STARTED.md` generated when you run `rover init`.

#### Additional resources

* After running `rover init`, open the generated `GETTING_STARTED.md` file for next steps.
* To go further, check out the [Getting started guide](https://www.apollographql.com/docs/graphos/get-started/guides/rest) to learn what else you can do with Apollo Connectors.
* If you learn best with videos and exercises, this [interactive course](https://www.apollographql.com/tutorials/connectors-intro-rest) teaches you how to integrate a demo REST API into a graph using Apollo Connectors.

## Initializing an MCP server

### `rover init --mcp`

Rover's `init --mcp` command provides a helpful starting point for working with the [Apollo MCP Server](https://www.apollographql.com/docs/apollo-mcp-server).

```terminal
rover init --mcp
```

The `init` CLI wizard walks you through the process of configuring and creating an MCP server. When you're done, you'll have starter files for an MCP server and a graph to run locally.

The command creates the following files:

* MCP config YAML for local and staging scenarios
* Starter [MCP tools](https://www.apollographql.com/docs/apollo-mcp-server/define-tools), based on your GraphQL API operations
* `.env` files for running the GraphQL API and MCP Server
* A set of local configuration files and boilerplate code that represent the graph
* mcp.Dockerfile (optional Docker container)

##### Options

You can also pass options directly to `rover init --mcp` instead of answering prompts in the wizard. The wizard still asks for any information not provided via an option and always asks for confirmation before creating any files locally.

```terminal
rover init --mcp \
  --project-type <PROJECT_TYPE> \
  --org-id <ORGANIZATION_ID> \
  --project-name <PROJECT_NAME> \
  --graph-id <GRAPH_ID>
```

##### Available options

| Option           | Description                                                                                                                                                                | Possible Values              |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `--project-type` | Whether to create MCP tools from a new Apollo GraphOS project or an existing Apollo GraphOS project.                                                                       | `create-new`, `add-subgraph` |
| `--org-id`       | The ID of the [GraphOS organization](https://www.apollographql.com/docs/graphos/platform/access-management/org#view-your-organizations) where the graph should be created. | *(your organization ID)*     |
| `--project-name` | The name for your new graph.                                                                                                                                               | *(your graph name)*          |
| `--graph-id`     | The ID for your graph in GraphOS. (This must be a unique identifier.)                                                                                                      | *(your graph ID)*            |

### Next steps

#### Run your MCP server

When the `rover init` wizard is complete, you can use [`rover dev`](https://www.apollographql.com/docs/rover/commands/dev) to start everything together. See [Running the Apollo MCP Server](https://www.apollographql.com/docs/apollo-mcp-server/run).

#### Connect your MCP server to Claude Desktop

```bash
# Copy and provide the configuration to Claude Desktop
# macOS:
cp claude_desktop_config.json ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Windows:
copy claude_desktop_config.json "%APPDATA%\Claude\claude_desktop_config.json"

# Linux:
cp claude_desktop_config.json ~/.config/Claude/claude_desktop_config.json

# Restart Claude Desktop
```

For instructions on adding your MCP server to other AI clients, see the [MCP Quickstart guide](https://www.apollographql.com/docs/apollo-mcp-server/quickstart).
