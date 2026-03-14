# Source: https://docs.airbyte.com/integrations/sources/clickup-api.md

# Source: https://docs.airbyte.com/ai-agents/connectors/clickup-api.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-clickup-api/latest/icon.svg)

# Clickup-Api

Copy Page

The Clickup-Api agent connector is a Python package that equips AI agents to interact with Clickup-Api through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

ClickUp is a productivity platform that provides project management, task tracking, docs, goals, and time tracking for teams. This connector provides access to workspaces, spaces, folders, lists, tasks (including workspace-wide search), comments, goals, views, time tracking, members, and docs.

## Example questions[​](#example-questions "Direct link to Example questions")

The Clickup-Api connector is optimized to handle prompts like these.

* List all workspaces I have access to
* Show me the spaces in my workspace
* List the folders in a space
* Show me the lists in a folder
* Get the tasks in a list
* Get details for a specific task
* Search for tasks containing 'bug' across my workspace
* Find all urgent priority tasks in my workspace
* Show me tasks assigned to a specific user
* List comments on a task
* Get threaded replies on a comment
* Create a comment on a task
* Update a comment to mark it resolved
* List all goals in my workspace
* Get details for a specific goal
* Show me all workspace-level views
* Get tasks matching a saved view
* List time entries for my workspace this week
* Get details for a specific time entry
* Show me the members assigned to a task
* List all docs in my workspace
* Get details for a specific doc
* What tasks are overdue in my workspace?
* Which tasks were updated in the last 24 hours?
* Show me all high-priority tasks across all projects
* How much time has been tracked this week?
* What are the most commented tasks?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Clickup-Api connector isn't currently able to handle prompts like these.

* Delete a task
* Delete a comment
* Delete a goal

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-clickup-api
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_clickup_api import ClickupApiConnector
from airbyte_agent_clickup_api.models import ClickupApiAuthConfig

connector = ClickupApiConnector(
    auth_config=ClickupApiAuthConfig(
        api_key="<Your ClickUp personal API token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ClickupApiConnector.tool_utils
async def clickup_api_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/clickup-api/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_clickup_api import ClickupApiConnector, AirbyteAuthConfig

connector = ClickupApiConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ClickupApiConnector.tool_utils
async def clickup_api_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/clickup-api/REFERENCE.md).

| Entity        | Actions                                                                                                                                                                                                                                                                                      |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User          | [Get](/ai-agents/connectors/clickup-api/REFERENCE.md#user-get)                                                                                                                                                                                                                               |
| Teams         | [List](/ai-agents/connectors/clickup-api/REFERENCE.md#teams-list)                                                                                                                                                                                                                            |
| Spaces        | [List](/ai-agents/connectors/clickup-api/REFERENCE.md#spaces-list), [Get](/ai-agents/connectors/clickup-api/REFERENCE.md#spaces-get)                                                                                                                                                         |
| Folders       | [List](/ai-agents/connectors/clickup-api/REFERENCE.md#folders-list), [Get](/ai-agents/connectors/clickup-api/REFERENCE.md#folders-get)                                                                                                                                                       |
| Lists         | [List](/ai-agents/connectors/clickup-api/REFERENCE.md#lists-list), [Get](/ai-agents/connectors/clickup-api/REFERENCE.md#lists-get)                                                                                                                                                           |
| Tasks         | [List](/ai-agents/connectors/clickup-api/REFERENCE.md#tasks-list), [Get](/ai-agents/connectors/clickup-api/REFERENCE.md#tasks-get), [API Search](/ai-agents/connectors/clickup-api/REFERENCE.md#tasks-api_search)                                                                            |
| Comments      | [List](/ai-agents/connectors/clickup-api/REFERENCE.md#comments-list), [Create](/ai-agents/connectors/clickup-api/REFERENCE.md#comments-create), [Get](/ai-agents/connectors/clickup-api/REFERENCE.md#comments-get), [Update](/ai-agents/connectors/clickup-api/REFERENCE.md#comments-update) |
| Goals         | [List](/ai-agents/connectors/clickup-api/REFERENCE.md#goals-list), [Get](/ai-agents/connectors/clickup-api/REFERENCE.md#goals-get)                                                                                                                                                           |
| Views         | [List](/ai-agents/connectors/clickup-api/REFERENCE.md#views-list), [Get](/ai-agents/connectors/clickup-api/REFERENCE.md#views-get)                                                                                                                                                           |
| View Tasks    | [List](/ai-agents/connectors/clickup-api/REFERENCE.md#view-tasks-list)                                                                                                                                                                                                                       |
| Time Tracking | [List](/ai-agents/connectors/clickup-api/REFERENCE.md#time-tracking-list), [Get](/ai-agents/connectors/clickup-api/REFERENCE.md#time-tracking-get)                                                                                                                                           |
| Members       | [List](/ai-agents/connectors/clickup-api/REFERENCE.md#members-list)                                                                                                                                                                                                                          |
| Docs          | [List](/ai-agents/connectors/clickup-api/REFERENCE.md#docs-list), [Get](/ai-agents/connectors/clickup-api/REFERENCE.md#docs-get)                                                                                                                                                             |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/clickup-api/AUTH.md).

### Clickup-Api API docs[​](#clickup-api-api-docs "Direct link to Clickup-Api API docs")

See the official [Clickup-Api API reference](https://developer.clickup.com/reference).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.2
* **Connector version:** 0.1.2
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/clickup-api/CHANGELOG.md)
