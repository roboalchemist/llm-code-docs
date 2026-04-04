# Source: https://docs.port.io/ai-interfaces/port-mcp-server/available-tools.md

# Available tools

The Port MCP Server exposes different sets of tools based on your role and use case. The tools you see will depend on your permissions in Port.

* Developer
* Builder

**Developers** are typically users who consume and interact with the developer portal - querying services, running actions, and analyzing data. These tools help you get information and execute approved workflows.

`list_blueprints`

List blueprints in your organization. Without identifiers, returns a summary list. With identifiers, returns full blueprint details including property definitions, schemas, and enum values.

<!-- -->

[API Reference](/api-reference/get-all-blueprints.md)

`list_entities`

Query entities from a blueprint with filtering, sorting, and pagination. Supports identifiers for specific entities, groupBy for value distribution, and countOnly for counting without retrieving data.

<!-- -->

[API Reference](/api-reference/get-all-entities-of-a-blueprint.md)

`list_scorecards`

List scorecards in your organization. Without identifiers, returns a summary list. With identifiers, returns full scorecard details including complete rule configurations.

<!-- -->

[API Reference](/api-reference/get-all-scorecards.md)

`list_actions`

List actions in your organization. Without identifiers, returns a summary list. With identifiers, returns full action details including complete input schemas.

`track_action_run`

Track action execution status.

`run_action`Dynamic

Execute any action you have permission to run in Port. Provide the action identifier and inputs to run the action. This unified tool handles all actions in your organization, reducing the total number of tools available.

<!-- -->

[API Reference](/api-reference/execute-a-self-service-action.md)

`get_action_permissions`

Get permissions/approval config for actions.

`search_port_knowledge_sources`

Search the official Port documentation and return the most relevant sections from it for a user query. Each returned section includes the url and its actual content in markdown. Use this tool for all queries that require Port knowledge.

`describe_user_details`

Describe the user, which organization he is connected to and what teams he is a member of and more information regarding the user. Can be useful for questions that relate to the user or when looking up for related entities to the user

<!-- -->

[API Reference](/api-reference/get-organization-details.md)

`load_skill`

Load specialized guidance for a domain-specific task. Skills provide step-by-step instructions for common workflows like troubleshooting integrations. Load a skill before starting a specialized task to ensure consistent, thorough handling.

**Builders** are platform engineers or admins who design and configure the developer portal - creating blueprints, setting up scorecards, and managing the overall structure. These tools help you build and maintain the portal.

Builders have access to all the tools available to Developers, plus additional management tools for creating and configuring the portal.

`list_blueprints`

List blueprints in your organization. Without identifiers, returns a summary list. With identifiers, returns full blueprint details including property definitions, schemas, and enum values.

<!-- -->

[API Reference](/api-reference/get-all-blueprints.md)

`upsert_blueprint`

Create or update a blueprint. Updates if the blueprint exists, creates if it does not.

<!-- -->

[API Reference](/api-reference/create-a-blueprint.md)

`delete_blueprint`

Delete blueprint and all its entities.

<!-- -->

[API Reference](/api-reference/delete-a-blueprint.md)

`list_entities`

Query entities from a blueprint with filtering, sorting, and pagination. Supports identifiers for specific entities, groupBy for value distribution, and countOnly for counting without retrieving data.

<!-- -->

[API Reference](/api-reference/get-all-entities-of-a-blueprint.md)

`upsert_entity`

Create or update an entity. Updates if the entity exists, creates if it does not. Uses merge by default to preserve existing fields.

<!-- -->

[API Reference](/api-reference/create-an-entity.md)

`delete_entity`

Delete entity with optional dependents.

<!-- -->

[API Reference](/api-reference/delete-an-entity.md)

`list_scorecards`

List scorecards in your organization. Without identifiers, returns a summary list. With identifiers, returns full scorecard details including complete rule configurations.

<!-- -->

[API Reference](/api-reference/get-all-scorecards.md)

`upsert_scorecard`

Create or update a scorecard. Updates if the scorecard exists, creates if it does not.

<!-- -->

[API Reference](/api-reference/create-a-scorecard.md)

`delete_scorecard`

Delete scorecard by identifiers.

<!-- -->

[API Reference](/api-reference/delete-a-scorecard.md)

`list_actions`

List actions in your organization. Without identifiers, returns a summary list. With identifiers, returns full action details including complete input schemas.

`upsert_action`

Create or update an action. Updates if the action exists, creates if it does not.

`delete_action`

Delete action by identifier.

`track_action_run`

Track action execution status.

`run_action`Dynamic

Execute any action you have permission to run in Port. Provide the action identifier and inputs to run the action. This unified tool handles all actions in your organization, reducing the total number of tools available.

<!-- -->

[API Reference](/api-reference/execute-a-self-service-action.md)

`get_action_permissions`

Get permissions/approval config for actions.

`update_action_permissions`

Update action permissions configuration.

`list_integrations`

List integrations in your organization. Without identifiers, returns a summary list. With identifiers, returns full integration details including complete config with mapping configuration.

<!-- -->

[API Reference](/api-reference/get-all-integrations.md)

`test_integration_mapping`

Test an integration mapping against raw data examples. Validates the mapping, checks for errors, and returns the mapped results or error messages.

`get_integration_sync_metrics`

Fetch sync metrics for an integration. Returns detailed metrics including status, number of items handled in each phase of the integration pipeline (extract, transform, load, delete), and per-kind statistics.

<!-- -->

[API Reference](/api-reference/get-an-integrations-metrics-and-sync-status.md)

`get_integration_event_logs`

Fetch event logs for an integration. Supports pagination to read logs page by page. You can paginate by using the timestamp and log\_id from the previous response.

<!-- -->

[API Reference](/api-reference/get-an-integrations-audit-logs)

`get_integration_kinds_with_examples`

Fetch all kinds (data types) that an integration ingests, along with raw data examples for each kind. For example, a GitHub integration might have kinds like "pull\_request", "issue", and "repo".

`search_port_knowledge_sources`

Search the official Port documentation and return the most relevant sections from it for a user query. Each returned section includes the url and its actual content in markdown. Use this tool for all queries that require Port knowledge.

`describe_user_details`

Describe the user, which organization he is connected to and what teams he is a member of and more information regarding the user. Can be useful for questions that relate to the user or when looking up for related entities to the user

<!-- -->

[API Reference](/api-reference/get-organization-details.md)

`load_skill`

Load specialized guidance for a domain-specific task. Skills provide step-by-step instructions for common workflows like troubleshooting integrations. Load a skill before starting a specialized task to ensure consistent, thorough handling.

Client Support

Tool support in external MCP clients depends on whether the client implements the tools feature according to the [MCP specification](https://modelcontextprotocol.info/docs/clients/). Most MCP clients support tools. Check the [MCP client documentation](https://modelcontextprotocol.info/docs/clients/) to see which features your client supports.

## Select which tools to use[â](#select-which-tools-to-use "Direct link to Select which tools to use")

By default, when you open a chat with Port MCP, all available tools (based on your permissions) are loaded and ready to use. However, you can customize which tools are available if you want to focus on specific workflows.

For example, if you only want to query data from Port without building or modifying anything, you can limit the tools to just the read-only ones. This helps reduce complexity and ensures you don't accidentally make changes.

### Using headers to control tool availability[â](#using-headers-to-control-tool-availability "Direct link to Using headers to control tool availability")

You can use headers when configuring your MCP server connection to control which tools are available:

**Read-only mode** - The `x-read-only-mode` header controls whether write tools are available. Set it to `1` to restrict the MCP server to only expose read-only tools, completely hiding write tools from the available tools list. Set it to `0` (default) to allow all tools based on your permissions.

**Control actions** - The `x-allowed-actions-to-run` header controls which actions are available through the `run_action` tool. This header accepts a comma-separated list of action identifiers. Only the specified actions will be available. If the header is not specified, all actions you have permission to run will be available. If set to an empty string, no actions will be allowed to run.

Examples:

* `x-allowed-actions-to-run: "create_github_issue,create_incident"` - Allows only the specified GitHub and incident actions.
* `x-allowed-actions-to-run: "create_service,deploy_to_production"` - Allows only the specified deployment actions.
* `x-allowed-actions-to-run: ""` - No actions will be allowed to run.

See the [token-based authentication guide](/ai-interfaces/port-mcp-server/token-based-authentication.md) for examples of how to configure these headers.

### Using client UI to select tools[â](#using-client-ui-to-select-tools "Direct link to Using client UI to select tools")

* Cursor
* VSCode
* Claude

In Cursor, you can customize which tools are available through the UI after connecting to Port MCP. Once connected, you can select specific tools as shown below.

![Enabling specific tools in Cursor](/assets/images/MCPCursorEnableTools-3c7bcb8970cfc1e209dde52318ba2197.png)

In VSCode, you can choose the tools through the UI after connecting to Port MCP.

![Enabling specific tools in VSCode](/assets/images/MCPVSCodeEnableTools-2a4ce11acae848bf33b52e138e21845e.png)

When creating a custom connector in Claude, you can specify exactly which tools to expose instead of enabling everything.

![Enabling specific tools in Claude](/assets/images/MCPClaudeEnableTools-488b41f87c50aad0004f5d2839a4fe46.png)

Refer to the [Claude custom connector documentation](https://support.anthropic.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp) for detailed instructions.
