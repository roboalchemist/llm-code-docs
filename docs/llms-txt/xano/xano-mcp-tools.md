# Source: https://docs.xano.com/building/build-with-ai/xano-mcp-tools.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Xano MCP Tools

> A list of all the tools available in the Xano MCP Server

The Xano MCP Tools are a collection of tools that you can use to build your entire backend with AI.

## Authentication

* `getLoggedInUser` — Identifies account details for the current Access Token.
* `documentation` — This utility provides a comprehensive overview of the MCP Server's operation and includes detailed documentation for the XanoScript syntax. To begin, use the type `"start"` to view all available commands.

## Addons

* `updateAddonSecurity` — Updates security settings for a workspace addon.
* `deleteAddon` — Deletes a workspace addon permanently.
* `getAddon` — Gets a specific addon by ID from a workspace.
* `updateAddon` — Updates a workspace addon using XanoScript.
* `listAddons` — Lists addons within a workspace.
* `createAddon` — Adds a new addon to a workspace using XanoScript.

## Agent Triggers

* `updateAgentTriggerSecurity` — Update agent trigger security configuration and access controls.
* `deleteAgentTrigger` — Delete an agent trigger permanently. This action cannot be undone.
* `getAgentTrigger` — Retrieve an agent trigger by ID.
* `updateAgentTrigger` — Update agent trigger using XanoScript.
* `listAgentTriggers` — Lists agent triggers.
* `createAgentTrigger` — Create a new agent trigger using XanoScript.

## Agents

* `deleteAgent` — Delete an agent permanently. This action cannot be undone.
* `getAgent` — Retrieve a specific agent by ID.
* `updateAgent` — Update agent details using XanoScript.
* `listAgents` — Lists agents within a workspace.
* `createAgent` — Create a new agent using XanoScript.

## APIs

* `getApiSwagger` — Returns the JSON output of the OpenAPI (Swagger) specification for a given API's REST endpoint.
* `updateAPISecurity` — Updates an API endpoint's security configuration and access controls.
* `deleteAPI` — Deletes an API endpoint permanently.
* `getAPI` — Retrieves a specific API endpoint by ID.
* `updateAPI` — Updates an API endpoint's code, settings, and authentication rules.
* `listAPIs` — Lists API endpoints within a specific API group.
* `createAPI` — Creates a new API endpoint using XanoScript.

## API Groups

* `getApiGroupSwagger` — Returns the JSON output of the OpenAPI (Swagger) specification for a given API group's REST endpoints.
* `updateApiGroupSecurity` — Updates security settings for an API group.
* `deleteApiGroup` — Deletes an API group and all its endpoints.
* `getApiGroup` — Retrieves details for a specific API group.
* `updateApiGroup` — Updates an existing API group.
* `listAPIGroups` — Lists API groups in a Xano workspace.
* `createApiGroup` — Creates a new API group in a workspace.

## Workspace Management

* `deleteWorkspaceBranch` — Deletes a branch within a workspace.
* `getWorkspaceBranches` — Lists branches within a workspace.
* `getWorkspaceContext` — Generates the full context for a workspace.

## Data Sources

* `deleteDataSource` — Deletes a data source permanently.
* `updateDataSource` — Updates an existing data source's label and color.
* `listDataSources` — Lists data sources within a workspace.
* `createDataSource` — Creates a new external data source.

## Files

* `deleteFiles` — Deletes multiple files permanently.
* `deleteFile` — Deletes a file permanently.
* `listFiles` — Retrieves workspace files with optional search, filtering, and pagination.
* `uploadFile` — Uploads a file to a workspace.

## Functions

* `updateFunctionSecurity` — Update function security configuration and access controls.
* `deleteFunction` — Delete a function permanently. This action cannot be undone.
* `getFunction` — Retrieve a specific function by ID.
* `updateFunction` — Update function code, metadata, and caching settings.
* `searchFunctionRequestHistory` — Searches API function request history within a specified Xano workspace. Allows for complex filtering (e.g., by status, verb) and sorting of function logs.
* `getFunctionRequestHistory` — Lists API function request history for a specified Xano workspace. Supports pagination and basic filtering by branch, API ID, or query ID.
* `listFunctions` — Lists functions within a workspace.
* `createFunction` — Create a new function using XanoScript.

## MCP Server Triggers

* `updateMCPServerTriggerSecurity` — Update mcp\_server trigger security configuration and access controls.
* `deleteMCPServerTrigger` — Delete a mcp\_server trigger permanently. This action cannot be undone.
* `getMCPServerTrigger` — Retrieve an mcp\_server trigger by ID.
* `updateMCPServerTrigger` — Update mcp\_server trigger using XanoScript.
* `listMcpServerTriggers` — Lists mcp\_server triggers.
* `createMCPServerTrigger` — Create a new mcp\_server trigger using XanoScript.

## MCP Server

* `deleteMCPServer` — Delete a MCP server permanently. This action cannot be undone.
* `getMCPServer` — Retrieve a specific MCP server by ID.
* `updateMCPServer` — Update MCP server details using XanoScript.
* `listMCPServers` — Lists MCP servers within a workspace.
* `createMCPServer` — Create a new MCP server using XanoScript.

## Middleware

* `updateMiddlewareSecurity` — Updates middleware security configuration and access controls.
* `deleteMiddleware` — Deletes a middleware permanently.
* `getMiddleware` — Retrieves a specific middleware by ID.
* `updateMiddleware` — Updates middleware code, metadata, and caching settings.
* `searchMiddlewareRequestHistory` — Searches middleware request history within a specified Xano workspace. Allows for complex filtering (e.g., by status, verb) and sorting of middleware logs.
* `getMiddlewareRequestHistory` — Lists middleware request history for a specified Xano workspace. Supports pagination and basic filtering by branch, API ID, or query ID.
* `listmiddlewares` — Lists middlewares within a workspace.
* `createMiddleware` — Creates a new middleware using XanoScript.

## Realtime

* `getWorkspaceOpenApi` — Returns the JSON output of the OpenAPI (Swagger) specification for all API groups in a workspace.
* `listRealtimeChannels` — Lists realtime channels.
* `listRealtimeTriggers` — Lists realtime triggers.

## API Request History

* `searchApiRequestHistory` — Searches API request history within a specified Xano workspace. Allows for complex filtering (e.g., by status, verb) and sorting of request logs.
* `getApiRequestHistory` — Lists API request history for a specified Xano workspace. Supports pagination and basic filtering by branch, API ID, or query ID.
* `generateWorkspaceSdk` — Generates a downloadable SDK package for all API groups in a workspace.

## Static Hosts

* `updateStaticHostEnvironment` — Updates a static hosting environment.
* `listStaticHostBuilds` — Retrieves builds for a static host.
* `createStaticHostBuild` — Creates a static host build.
* `listStaticHosts` — Retrieves workspace static hosts.

## Table Triggers

* `updateTableTriggerSecurity` — Updates security settings for a table trigger.
* `deleteTableTrigger` — Deletes a table trigger permanently.
* `getTableTrigger` — Retrieves a specific table trigger by ID.
* `updateTableTrigger` — Updates a table trigger using XanoScript.
* `listWorkspaceTableTriggers` — Lists workspace table triggers.
* `createTableTrigger` — Creates a new table trigger using XanoScript.

## Table Content

* `deleteTableContentBulk` — Deletes multiple records from a table in bulk.
* `patchTableContentBulk` — Updates multiple records in a table in bulk.
* `addTableContentBulk` — Adds multiple records to a table in bulk.
* `deleteTableContentBySearch` — Deletes table records matching search criteria.
* `patchTableContentBySearch` — Updates table records matching search criteria.
* `searchTableContent` — Searches records in a table.
* `deleteTableContentItem` — Deletes a specific record from a table.
* `getTableContentItem` — Retrieves a specific record from a table.
* `updateTableContentItem` — Updates a record in a table. The data for the fields you wish to update should be provided as additional key-value pairs directly within the arguments object. The keys should match the names of the columns in the table, and the values should be the new values for those columns.
* `getTableContent` — Retrieves records from a table.
* `addTableContent` — Adds a new record to a table. The data for the new record should be provided as additional key-value pairs directly within the arguments object. The keys should match the names of the columns in the table, and the values should be the values for those columns.

## Table Indexes

* `createBtreeIndex` — Creates a btree index on table columns to optimize query performance.
* `createSearchIndex` — Creates a full-text search index for table columns with language-specific optimization.
* `createSpatialIndex` — Creates a spatial index on a table for optimized geometry operations.
* `createUniqueIndex` — Creates a unique index on table fields to enforce data uniqueness and improve query performance.
* `createVectorIndex` — Creates a vector index on a table column with support for Inner Product, Cosine, L1, and L2 distance operations.
* `deleteTableIndex` — Deletes a specific table index.
* `listTableIndexes` — Retrieves all indexes for a database table.
* `replaceTableIndexes` — Replaces all indexes for a database table with a new configuration.

## Table Schema

* `updateTableMetadata` — Updates the metadata for a table.
* `renameTableColumn` — Renames a column in a table's schema.
* `deleteTableSchemaElement` — Deletes a column from a table's schema.
* `getTableSchemaElement` — Retrieves a specific column from a table's schema.
* `getTableSchema` — Retrieves the schema of a table.
* `updateTableSchema` — Replaces the entire schema of a table.
* `updateTableSecurity` — Updates security rules for a table using a GUID.
* `truncateTable` — Deletes all records from a table.
* `deleteTable` — Deletes a table and its data.
* `getTable` — Retrieves details for a specific table.
* `updateTable` — Updates a workspace table using XanoScript.
* `getTables` — Lists tables in a workspace.
* `addTable` — Creates a new database table in a workspace. Note: Xano automatically adds an `id` field (default primary key) and a `created_at` timestamp field; these do not need to be defined in the `schema` array.

## Tasks

* `updateTaskSecurity` — Updates scheduled task security configuration and access controls.
* `deleteTask` — Deletes a scheduled task permanently.
* `getTask` — Retrieves a specific scheduled task by ID.
* `updateTask` — Updates task code, schedule settings, and activation status.
* `searchTaskRequestHistory` — Searches task request history within a specified Xano workspace. Allows for complex filtering (e.g., by status, verb) and sorting of task logs.
* `getTaskRequestHistory` — Lists task request history for a specified Xano workspace. Supports pagination and basic filtering by branch, API ID, or query ID.
* `listTasks` — Lists tasks within a workspace.
* `createTask` — Creates a new scheduled task using XanoScript.

## Tools

* `updateToolSecurity` — Update tool security configuration and access controls.
* `deleteTool` — Delete a tool permanently. This action cannot be undone.
* `getTool` — Retrieve a specific tool by ID.
* `updateTool` — Update tool code, metadata, and caching settings.
* `searchToolRequestHistory` — Searches tool request history within a specified Xano workspace. Allows for complex filtering (e.g., by status, verb) and sorting of tool logs.
* `getToolRequestHistory` — Lists tool request history for a specified Xano workspace. Supports pagination and basic filtering by branch, API ID, or query ID.
* `listTools` — Lists tools within a workspace.
* `createTool` — Create a new tool using XanoScript.

## Workspace Triggers

* `updateWorkspaceTriggerSecurity` — Updates workspace trigger security configuration and access controls.
* `deleteWorkspaceTrigger` — Deletes a workspace trigger permanently.
* `getWorkspaceTrigger` — Retrieves a specific workspace trigger by ID.
* `updateWorkspaceTrigger` — Updates workspace trigger code, metadata, and caching settings.
* `searchTriggerRequestHistory` — Searches trigger request history within a specified Xano workspace. Allows for complex filtering (e.g., by status, verb) and sorting of trigger logs.
* `getTriggerRequestHistory` — Lists trigger request history for a specified Xano workspace. Supports pagination and basic filtering by branch, API ID, or query ID.
* `listWorkspaceTriggers` — Lists workspace triggers.
* `createWorkspaceTrigger` — Creates a new workspace trigger using XanoScript.

## Workflow Tests

* `updateWorkflowTestSecurity` — Updates security settings for a workspace workflow test.
* `deleteWorkflowTest` — Deletes a workspace workflow test permanently.
* `getWorkflowTest` — Gets a specific workflow test by ID from a workspace.
* `updateWorkflowTest` — Updates a workspace workflow test using XanoScript.
* `listWorkflowTests` — Lists workflow tests within a workspace.
* `createWorkflowTest` — Adds a new workflow test to a workspace using XanoScript.

## Workspaces

* `getWorkspace` — Retrieves details for a specific workspace.
* `listWorkspaces` — Lists workspaces accessible by the authenticated user.


Built with [Mintlify](https://mintlify.com).