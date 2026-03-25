# Source: https://docs.airbyte.com/integrations/sources/linear.md

# Source: https://docs.airbyte.com/ai-agents/connectors/linear.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-linear/latest/icon.svg)

# Linear

Copy Page

The Linear agent connector is a Python package that equips AI agents to interact with Linear through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Linear is a modern issue tracking and project management tool built for software development teams. This connector provides access to issues, projects, and teams for sprint planning, backlog management, and development workflow analysis.

## Example questions[​](#example-questions "Direct link to Example questions")

The Linear connector is optimized to handle prompts like these.

* Show me the open issues assigned to my team this week
* List out all projects I'm currently involved in
* List all users in my Linear workspace
* Who is assigned to the most recently updated issue?
* Create a new issue titled 'Fix login bug'
* Update the priority of a recent issue to urgent
* Change the title of a recent issue to 'Updated feature request'
* Add a comment to a recent issue saying 'This is ready for review'
* Update my most recent comment to say 'Revised feedback after testing'
* Create a high priority issue about API performance
* Assign a recent issue to a teammate
* Unassign the current assignee from a recent issue
* Reassign a recent issue from one teammate to another
* Analyze the workload distribution across my development team
* What are the top priority issues in our current sprint?
* Identify the most active projects in our organization right now
* Summarize the recent issues for {team\_member} in the last two weeks
* Compare the issue complexity across different teams
* Which projects have the most unresolved issues?
* Give me an overview of my team's current project backlog

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Linear connector isn't currently able to handle prompts like these.

* Delete an outdated project from our workspace
* Schedule a sprint planning meeting
* Delete this issue
* Remove a comment from an issue

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-linear
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_linear import LinearConnector
from airbyte_agent_linear.models import LinearAuthConfig

connector = LinearConnector(
    auth_config=LinearAuthConfig(
        api_key="<Your Linear API key from Settings > API > Personal API keys>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@LinearConnector.tool_utils
async def linear_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/linear/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_linear import LinearConnector, AirbyteAuthConfig

connector = LinearConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@LinearConnector.tool_utils
async def linear_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/linear/REFERENCE.md).

| Entity   | Actions                                                                                                                                                                                                                                                                                                                                       |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Issues   | [List](/ai-agents/connectors/linear/REFERENCE.md#issues-list), [Get](/ai-agents/connectors/linear/REFERENCE.md#issues-get), [Create](/ai-agents/connectors/linear/REFERENCE.md#issues-create), [Update](/ai-agents/connectors/linear/REFERENCE.md#issues-update), [Search](/ai-agents/connectors/linear/REFERENCE.md#issues-search)           |
| Projects | [List](/ai-agents/connectors/linear/REFERENCE.md#projects-list), [Get](/ai-agents/connectors/linear/REFERENCE.md#projects-get), [Search](/ai-agents/connectors/linear/REFERENCE.md#projects-search)                                                                                                                                           |
| Teams    | [List](/ai-agents/connectors/linear/REFERENCE.md#teams-list), [Get](/ai-agents/connectors/linear/REFERENCE.md#teams-get), [Search](/ai-agents/connectors/linear/REFERENCE.md#teams-search)                                                                                                                                                    |
| Users    | [List](/ai-agents/connectors/linear/REFERENCE.md#users-list), [Get](/ai-agents/connectors/linear/REFERENCE.md#users-get), [Search](/ai-agents/connectors/linear/REFERENCE.md#users-search)                                                                                                                                                    |
| Comments | [List](/ai-agents/connectors/linear/REFERENCE.md#comments-list), [Get](/ai-agents/connectors/linear/REFERENCE.md#comments-get), [Create](/ai-agents/connectors/linear/REFERENCE.md#comments-create), [Update](/ai-agents/connectors/linear/REFERENCE.md#comments-update), [Search](/ai-agents/connectors/linear/REFERENCE.md#comments-search) |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/linear/AUTH.md).

### Linear API docs[​](#linear-api-docs "Direct link to Linear API docs")

See the official [Linear API reference](https://linear.app/developers/graphql).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.19.113
* **Connector version:** 0.1.11
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/linear/CHANGELOG.md)
