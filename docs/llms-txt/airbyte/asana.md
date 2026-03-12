# Source: https://docs.airbyte.com/integrations/sources/asana.md

# Source: https://docs.airbyte.com/ai-agents/connectors/asana.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-asana/latest/icon.svg)

# Asana

Copy Page

The Asana agent connector is a Python package that equips AI agents to interact with Asana through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Asana is a work management platform that helps teams organize, track, and manage projects and tasks. This connector provides access to tasks, projects, workspaces, teams, and users for project tracking, workload analysis, and productivity insights.

## Example questions[​](#example-questions "Direct link to Example questions")

The Asana connector is optimized to handle prompts like these.

* What tasks are assigned to me this week?
* List all projects in my workspace
* Show me the tasks for a recent project
* Who are the team members in one of my teams?
* Show me details of my current workspace and its users
* Summarize my team's workload and task completion rates
* Find all tasks related to {client\_name} across my workspaces
* Analyze the most active projects in my workspace last month
* Compare task completion rates between my different teams
* Identify overdue tasks across all my projects

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Asana connector isn't currently able to handle prompts like these.

* Create a new task for \[TeamMember]
* Update the priority of this task
* Delete the project \[ProjectName]
* Schedule a new team meeting
* Add a new team member to \[Workspace]
* Move this task to another project

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-asana
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_asana import AsanaConnector
from airbyte_agent_asana.models import AsanaPersonalAccessTokenAuthConfig

connector = AsanaConnector(
    auth_config=AsanaPersonalAccessTokenAuthConfig(
        token="<Your Asana Personal Access Token. Generate one at https://app.asana.com/0/my-apps>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AsanaConnector.tool_utils
async def asana_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/asana/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_asana import AsanaConnector, AirbyteAuthConfig

connector = AsanaConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AsanaConnector.tool_utils
async def asana_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/asana/REFERENCE.md).

| Entity                | Actions                                                                                                                                                                                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Tasks                 | [List](/ai-agents/connectors/asana/REFERENCE.md#tasks-list), [Get](/ai-agents/connectors/asana/REFERENCE.md#tasks-get), [Search](/ai-agents/connectors/asana/REFERENCE.md#tasks-search)                                                                                              |
| Project Tasks         | [List](/ai-agents/connectors/asana/REFERENCE.md#project-tasks-list)                                                                                                                                                                                                                  |
| Workspace Task Search | [List](/ai-agents/connectors/asana/REFERENCE.md#workspace-task-search-list)                                                                                                                                                                                                          |
| Projects              | [List](/ai-agents/connectors/asana/REFERENCE.md#projects-list), [Get](/ai-agents/connectors/asana/REFERENCE.md#projects-get), [Search](/ai-agents/connectors/asana/REFERENCE.md#projects-search)                                                                                     |
| Task Projects         | [List](/ai-agents/connectors/asana/REFERENCE.md#task-projects-list)                                                                                                                                                                                                                  |
| Team Projects         | [List](/ai-agents/connectors/asana/REFERENCE.md#team-projects-list)                                                                                                                                                                                                                  |
| Workspace Projects    | [List](/ai-agents/connectors/asana/REFERENCE.md#workspace-projects-list)                                                                                                                                                                                                             |
| Workspaces            | [List](/ai-agents/connectors/asana/REFERENCE.md#workspaces-list), [Get](/ai-agents/connectors/asana/REFERENCE.md#workspaces-get), [Search](/ai-agents/connectors/asana/REFERENCE.md#workspaces-search)                                                                               |
| Users                 | [List](/ai-agents/connectors/asana/REFERENCE.md#users-list), [Get](/ai-agents/connectors/asana/REFERENCE.md#users-get), [Search](/ai-agents/connectors/asana/REFERENCE.md#users-search)                                                                                              |
| Workspace Users       | [List](/ai-agents/connectors/asana/REFERENCE.md#workspace-users-list)                                                                                                                                                                                                                |
| Team Users            | [List](/ai-agents/connectors/asana/REFERENCE.md#team-users-list)                                                                                                                                                                                                                     |
| Teams                 | [Get](/ai-agents/connectors/asana/REFERENCE.md#teams-get), [Search](/ai-agents/connectors/asana/REFERENCE.md#teams-search)                                                                                                                                                           |
| Workspace Teams       | [List](/ai-agents/connectors/asana/REFERENCE.md#workspace-teams-list)                                                                                                                                                                                                                |
| User Teams            | [List](/ai-agents/connectors/asana/REFERENCE.md#user-teams-list)                                                                                                                                                                                                                     |
| Attachments           | [List](/ai-agents/connectors/asana/REFERENCE.md#attachments-list), [Get](/ai-agents/connectors/asana/REFERENCE.md#attachments-get), [Download](/ai-agents/connectors/asana/REFERENCE.md#attachments-download), [Search](/ai-agents/connectors/asana/REFERENCE.md#attachments-search) |
| Workspace Tags        | [List](/ai-agents/connectors/asana/REFERENCE.md#workspace-tags-list)                                                                                                                                                                                                                 |
| Tags                  | [Get](/ai-agents/connectors/asana/REFERENCE.md#tags-get), [Search](/ai-agents/connectors/asana/REFERENCE.md#tags-search)                                                                                                                                                             |
| Project Sections      | [List](/ai-agents/connectors/asana/REFERENCE.md#project-sections-list)                                                                                                                                                                                                               |
| Sections              | [Get](/ai-agents/connectors/asana/REFERENCE.md#sections-get), [Search](/ai-agents/connectors/asana/REFERENCE.md#sections-search)                                                                                                                                                     |
| Task Subtasks         | [List](/ai-agents/connectors/asana/REFERENCE.md#task-subtasks-list)                                                                                                                                                                                                                  |
| Task Dependencies     | [List](/ai-agents/connectors/asana/REFERENCE.md#task-dependencies-list)                                                                                                                                                                                                              |
| Task Dependents       | [List](/ai-agents/connectors/asana/REFERENCE.md#task-dependents-list)                                                                                                                                                                                                                |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/asana/AUTH.md).

### Asana API docs[​](#asana-api-docs "Direct link to Asana API docs")

See the official [Asana API reference](https://developers.asana.com/reference/rest-api-reference).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.19.119
* **Connector version:** 0.1.16
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/asana/CHANGELOG.md)
