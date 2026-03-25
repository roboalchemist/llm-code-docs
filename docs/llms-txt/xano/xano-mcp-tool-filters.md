# Source: https://docs.xano.com/building/build-with-ai/xano-mcp-tool-filters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Xano MCP Tool filters

> When connecting to the Xano MCP server, you'll need to select what categories of tools to allow. This guide explains the available tool filter options.

<Tabs>
  <Tab title="AI">
    | Tool Name                        | Type                 | Tags                              |
    | :------------------------------- | :------------------- | :-------------------------------- |
    | `listAgents`                     | `agent`              | `agent`, `ai`                     |
    | `getAgent`                       | `agent`              | `agent`, `ai`                     |
    | `deleteAgent`                    | `agent`              | `agent`, `ai`                     |
    | `createAgent`                    | `agent`              | `agent`, `ai`                     |
    | `updateAgent`                    | `agent`              | `agent`, `ai`                     |
    | `listAgentTriggers`              | `agent_trigger`      | `agent_trigger`, `ai`             |
    | `getAgentTrigger`                | `agent_trigger`      | `agent_trigger`, `ai`             |
    | `deleteAgentTrigger`             | `agent_trigger`      | `agent_trigger`, `ai`             |
    | `createAgentTrigger`             | `agent_trigger`      | `agent_trigger`, `ai`             |
    | `updateAgentTrigger`             | `agent_trigger`      | `agent_trigger`, `ai`             |
    | `updateAgentTriggerSecurity`     | `agent_trigger`      | `agent_trigger`, `ai`             |
    | `listTools`                      | `tool`               | `tool`, `ai`                      |
    | `getTool`                        | `tool`               | `tool`, `ai`                      |
    | `deleteTool`                     | `tool`               | `tool`, `ai`                      |
    | `createTool`                     | `tool`               | `tool`, `ai`                      |
    | `updateTool`                     | `tool`               | `tool`, `ai`                      |
    | `updateToolSecurity`             | `tool`               | `tool`, `ai`                      |
    | `listMCPServers`                 | `mcp_server`         | `mcp_server`, `ai`                |
    | `getMCPServer`                   | `mcp_server`         | `mcp_server`, `ai`                |
    | `deleteMCPServer`                | `mcp_server`         | `mcp_server`, `ai`                |
    | `createMCPServer`                | `mcp_server`         | `mcp_server`, `ai`                |
    | `updateMCPServer`                | `mcp_server`         | `mcp_server`, `ai`                |
    | `documentation`                  | `mcp_server`         | `mcp_server`, `ai`                |
    | `listMcpServerTriggers`          | `mcp_server_trigger` | `mcp_server_trigger`, `ai`        |
    | `getMCPServerTrigger`            | `mcp_server_trigger` | `mcp_server_trigger`, `ai`        |
    | `deleteMCPServerTrigger`         | `mcp_server_trigger` | `mcp_server_trigger`, `ai`        |
    | `createMCPServerTrigger`         | `mcp_server_trigger` | `mcp_server_trigger`, `ai`        |
    | `updateMCPServerTrigger`         | `mcp_server_trigger` | `mcp_server_trigger`, `ai`        |
    | `updateMCPServerTriggerSecurity` | `mcp_server_trigger` | `mcp_server_trigger`, `ai`        |
    | `getWorkspaceBranches`           | `workspace_branch`   | `workspace_branch`, `logic`, `ai` |
    | `deleteWorkspaceBranch`          | `workspace_branch`   | `workspace_branch`, `logic`, `ai` |
  </Tab>

  <Tab title="Logic">
    | Tool Name                        | Type                | Tags                             |
    | :------------------------------- | :------------------ | :------------------------------- |
    | `listFunctions`                  | `function`          | `function`, `logic`              |
    | `getFunction`                    | `function`          | `function`, `logic`              |
    | `deleteFunction`                 | `function`          | `function`, `logic`              |
    | `createFunction`                 | `function`          | `function`, `logic`              |
    | `updateFunction`                 | `function`          | `function`, `logic`              |
    | `updateFunctionSecurity`         | `function`          | `function`, `logic`              |
    | `listAPIGroups`                  | `api_group`         | `api_group`, `logic`             |
    | `getApiGroup`                    | `api_group`         | `api_group`, `logic`, `frontend` |
    | `getApiGroupSwagger`             | `api_group`         | `api_group`, `logic`, `frontend` |
    | `deleteApiGroup`                 | `api_group`         | `api_group`, `logic`             |
    | `createApiGroup`                 | `api_group`         | `api_group`, `logic`             |
    | `updateApiGroup`                 | `api_group`         | `api_group`, `logic`             |
    | `updateApiGroupSecurity`         | `api_group`         | `api_group`, `logic`             |
    | `listAddons`                     | `add_on`            | `add_on`, `logic`                |
    | `getAddon`                       | `add_on`            | `add_on`, `logic`                |
    | `deleteAddon`                    | `add_on`            | `add_on`, `logic`                |
    | `createAddon`                    | `add_on`            | `add_on`, `logic`                |
    | `updateAddon`                    | `add_on`            | `add_on`, `logic`                |
    | `updateAddonSecurity`            | `add_on`            | `add_on`, `logic`                |
    | `listmiddlewares`                | `middleware`        | `middleware`, `logic`            |
    | `getMiddleware`                  | `middleware`        | `middleware`, `logic`            |
    | `deleteMiddleware`               | `middleware`        | `middleware`, `logic`            |
    | `createMiddleware`               | `middleware`        | `middleware`, `logic`            |
    | `updateMiddleware`               | `middleware`        | `middleware`, `logic`            |
    | `updateMiddlewareSecurity`       | `middleware`        | `middleware`, `logic`            |
    | `listTasks`                      | `task`              | `task`, `logic`                  |
    | `getTask`                        | `task`              | `task`, `logic`                  |
    | `deleteTask`                     | `task`              | `task`, `logic`                  |
    | `createTask`                     | `task`              | `task`, `logic`                  |
    | `updateTask`                     | `task`              | `task`, `logic`                  |
    | `updateTaskSecurity`             | `task`              | `task`, `logic`                  |
    | `listWorkspaceTriggers`          | `workspace_trigger` | `workspace_trigger`, `logic`     |
    | `getWorkspaceTrigger`            | `workspace_trigger` | `workspace_trigger`, `logic`     |
    | `deleteWorkspaceTrigger`         | `workspace_trigger` | `workspace_trigger`, `logic`     |
    | `createWorkspaceTrigger`         | `workspace_trigger` | `workspace_trigger`, `logic`     |
    | `updateWorkspaceTrigger`         | `workspace_trigger` | `workspace_trigger`, `logic`     |
    | `updateWorkspaceTriggerSecurity` | `workspace_trigger` | `workspace_trigger`, `logic`     |
    | `listWorkflowTests`              | `workflow_test`     | `workflow_test`, `logic`         |
    | `getWorkflowTest`                | `workflow_test`     | `workflow_test`, `logic`         |
    | `deleteWorkflowTest`             | `workflow_test`     | `workflow_test`, `logic`         |
    | `createWorkflowTest`             | `workflow_test`     | `workflow_test`, `logic`         |
    | `updateWorkflowTest`             | `workflow_test`     | `workflow_test`, `logic`         |
    | `updateWorkflowTestSecurity`     | `workflow_test`     | `workflow_test`, `logic`         |
    | `listWorkspaceTableTriggers`     | `table_trigger`     | `table_trigger`, `logic`         |
    | `getTableTrigger`                | `table_trigger`     | `table_trigger`, `logic`         |
    | `deleteTableTrigger`             | `table_trigger`     | `table_trigger`, `logic`         |
    | `createTableTrigger`             | `table_trigger`     | `table_trigger`, `logic`         |
    | `updateTableTrigger`             | `table_trigger`     | `table_trigger`, `logic`         |
    | `updateTableTriggerSecurity`     | `table_trigger`     | `table_trigger`, `logic`         |
    | `listAPIs`                       | `api`               | `api`, `logic`                   |
    | `getAPI`                         | `api`               | `api`, `logic`                   |
    | `deleteAPI`                      | `api`               | `api`, `logic`                   |
    | `createAPI`                      | `api`               | `api`, `logic`                   |
    | `updateAPI`                      | `api`               | `api`, `logic`                   |
    | `updateAPISecurity`              | `api`               | `api`, `logic`                   |
    | `getApiSwagger`                  | `api`               | `api`, `logic`, `frontend`       |
  </Tab>

  <Tab title="Database">
    | Tool Name                    | Type                    | Tags                                |
    | :--------------------------- | :---------------------- | :---------------------------------- |
    | `getTables`                  | `table`                 | `table`, `database`                 |
    | `getTable`                   | `table`                 | `table`, `database`                 |
    | `addTable`                   | `table`                 | `table`, `database`                 |
    | `updateTable`                | `table`                 | `table`, `database`                 |
    | `updateTableMeta`            | `table`                 | `table`, `database`                 |
    | `deleteTable`                | `table`                 | `table`, `database`                 |
    | `getTableContent`            | `table_content`         | `table_content`, `database`         |
    | `getTableContentItem`        | `table_content`         | `table_content`, `database`         |
    | `searchTableContent`         | `table_content`         | `table_content`, `database`         |
    | `deleteTableContentItem`     | `table_content`         | `table_content`, `database`         |
    | `addTableContent`            | `table_content`         | `table_content`, `database`         |
    | `addTableContentBulk`        | `table_content`         | `table_content`, `database`         |
    | `patchTableContentBulk`      | `table_content`         | `table_content`, `database`         |
    | `deleteTableContentBulk`     | `table_content`         | `table_content`, `database`         |
    | `deleteTableContentBySearch` | `table_content`         | `table_content`, `database`         |
    | `patchTableContentBySearch`  | `table_content`         | `table_content`, `database`         |
    | `updateTableContentItem`     | `table_content`         | `table_content`, `database`         |
    | `truncateTable`              | `table_content`         | `table_content`, `database`         |
    | `listTableIndexes`           | `table_index`           | `table_index`, `database`           |
    | `createBtreeIndex`           | `table_index`           | `table_index`, `database`           |
    | `createSearchIndex`          | `table_index`           | `table_index`, `database`           |
    | `createUniqueIndex`          | `table_index`           | `table_index`, `database`           |
    | `createVectorIndex`          | `table_index`           | `table_index`, `database`           |
    | `createSpatialIndex`         | `table_index`           | `table_index`, `database`           |
    | `deleteTableIndex`           | `table_index`           | `table_index`, `database`           |
    | `replaceTableIndexes`        | `table_index`           | `table_index`, `database`           |
    | `getTableSchema`             | `table_schema`          | `table_schema`, `database`          |
    | `deleteTableSchemaElement`   | `table_schema`          | `table_schema`, `database`          |
    | `getTableSchemaElement`      | `table_schema`          | `table_schema`, `database`          |
    | `updateTableSchema`          | `table_schema`          | `table_schema`, `database`          |
    | `renameTableColumn`          | `table_schema`          | `table_schema`, `database`          |
    | `listFiles`                  | `files`                 | `files`, `database`                 |
    | `uploadFile`                 | `files`                 | `files`, `database`                 |
    | `deleteFiles`                | `files`                 | `files`, `database`                 |
    | `deleteFile`                 | `files`                 | `files`, `database`                 |
    | `workspaceGetDataSources`    | `workspace_datasources` | `workspace_datasources`, `database` |
    | `createDataSource`           | `workspace_datasources` | `workspace_datasources`, `database` |
    | `updateDataSource`           | `workspace_datasources` | `workspace_datasources`, `database` |
    | `deleteDataSource`           | `workspace_datasources` | `workspace_datasources`, `database` |
    | `getWorkspaceOpenApi`        | `workspace`             | `workspace`, `openapi`, `frontend`  |
    | `generateWorkspaceSdk`       | `workspace`             | `workspace`, `sdk`, `frontend`      |
  </Tab>

  <Tab title="Frontend">
    | Tool Name                     | Type          | Tags                      |
    | :---------------------------- | :------------ | :------------------------ |
    | `listStaticHosts`             | `static_host` | `static_host`, `frontend` |
    | `listStaticHostBuilds`        | `static_host` | `static_host`, `frontend` |
    | `createStaticHostBuild`       | `static_host` | `static_host`, `frontend` |
    | `updateStaticHostEnvironment` | `static_host` | `static_host`, `frontend` |
  </Tab>

  <Tab title="Audit">
    | Tool Name                        | Type                 | Tags                          |
    | :------------------------------- | :------------------- | :---------------------------- |
    | `getApiRequestHistory`           | `request_history`    | `request_history`, `audit`    |
    | `searchApiRequestHistory`        | `request_history`    | `request_history`, `audit`    |
    | `getWorkspaceAuditLogs`          | `audit_logs`         | `audit_logs`, `audit`         |
    | `getAuditLogs`                   | `audit_logs`         | `audit_logs`, `audit`         |
    | `searchWorkspaceAuditLogs`       | `audit_logs`         | `audit_logs`, `audit`         |
    | `searchAuditLogs`                | `audit_logs`         | `audit_logs`, `audit`         |
    | `getFunctionRequestHistory`      | `function_history`   | `function_history`, `audit`   |
    | `searchFunctionRequestHistory`   | `function_history`   | `function_history`, `audit`   |
    | `getTaskRequestHistory`          | `task_history`       | `task_history`, `audit`       |
    | `searchTaskRequestHistory`       | `task_history`       | `task_history`, `audit`       |
    | `getTriggerRequestHistory`       | `trigger_history`    | `trigger_history`, `audit`    |
    | `searchTriggerRequestHistory`    | `trigger_history`    | `trigger_history`, `audit`    |
    | `getMiddlewareRequestHistory`    | `middleware_history` | `middleware_history`, `audit` |
    | `searchMiddlewareRequestHistory` | `middleware_history` | `middleware_history`, `audit` |
    | `getToolRequestHistory`          | `tool_history`       | `tool_history`, `audit`       |
    | `searchToolRequestHistory`       | `tool_history`       | `tool_history`, `audit`       |
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).