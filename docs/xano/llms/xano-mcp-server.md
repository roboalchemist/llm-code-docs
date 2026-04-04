# Source: https://docs.xano.com/ai-tools/xano-mcp-server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Xano MCP Server

> Manage your Xano data using your favorite MCP client

## Connect your client

View the [instructions on connecting clients](/ai-tools/mcp-builder/connecting-clients)

## Available Tools

### User Authentication

* **getLoggedInUser** - Validates the provided Access Token and returns the associated account details.

### Workspace Management

* **listWorkspaces** - Lists all workspaces accessible by the authenticated user.

* **getWorkspace** - Retrieves detailed information about a specific workspace.

* **getWorkspaceBranches** - Lists all branches (e.g., development, production) within the specified workspace.

* **workspaceGetDataSources** - Lists all external data sources connected to the specified workspace.

* **workspaceRealtimeDetails** - Retrieves [Realtime](/realtime/realtime-in-xano) information for the specified workspace.

### Table Management

* **addTable** - Creates a new table within the specified workspace.

* **getTables** - Lists all tables within a specific workspace.

* **getTable** - Retrieves the details of a specific table within the workspace.

* **deleteTable** - Deletes a specific table and all data it contains from the workspace.

* **updateTableMeta** - Modifies the metadata (e.g., schema, field definitions, descriptions) of the specified table.

* **updateTableSecurity** - Updates the security rules for the specified table.

### Table Content Management

* **getTableContent** - Retrieves a list of records from the specified table.

* **getTableContentItem** - Retrieves a single, specific record from the table using its ID.

* **updateTableContentItem** - Updates an existing record in the table using its ID.

* **deleteTableContentItem** - Deletes a single, specific record from the table using its ID.

* **searchTableContent** - Searches for records within the table using complex filter criteria and sorting options.

* **patchTableContentBySearch** - Updates fields of all records in the table that match the specified search criteria.

* **deleteTableContentBySearch** - Deletes all records from the table that match the specified search criteria.

* **addTableContentBulk** - Adds multiple new records to the table in a single operation.

* **patchTableContentBulk** - Updates multiple existing records in the table in a single bulk operation.

* **deleteTableContentBulk** - Deletes multiple records from the table in bulk, based on a list of record IDs.

### API Management

* **listAPIGroups** - Lists all API groups within the specified workspace.

* **getApiGroup** - Retrieves details for a specific API group within the workspace.

* **listAPIs** - Lists all individual API endpoints defined within a specific API group.

* **getApiGroupSwagger** - Returns the JSON version of the [Swagger (OpenAPI Documentation)](/the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation) for a specific API group

* **getApiSwagger** - Returns the JSON version of the [Swagger (OpenAPI Documentation)](/the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation) for a specific API

### Request Management

* **getRequestHistory** - Lists the history of API requests made to the specified workspace.

* **searchRequestHistory** - Performs an advanced search of the workspace's API request history using filters and sorting.


Built with [Mintlify](https://mintlify.com).