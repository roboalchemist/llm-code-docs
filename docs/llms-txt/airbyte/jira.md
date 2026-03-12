# Source: https://docs.airbyte.com/integrations/sources/jira.md

# Source: https://docs.airbyte.com/ai-agents/connectors/jira.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-jira/latest/icon.svg)

# Jira

Copy Page

The Jira agent connector is a Python package that equips AI agents to interact with Jira through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for Jira API

## Example questions[​](#example-questions "Direct link to Example questions")

The Jira connector is optimized to handle prompts like these.

* Show me all open issues in my Jira instance
* List recent issues created in the last 7 days
* List all projects in my Jira instance
* Show me details for the most recently updated issue
* List all users in my Jira instance
* Show me comments on the most recent issue
* Show me worklogs from the last 7 days
* Assign a recent issue to a teammate
* Unassign a recent issue
* Create a new task called 'Sample task' in a project
* Create a bug with high priority
* Update the summary of a recent issue to 'Updated summary'
* Change the priority of a recent issue to high
* Add a comment to a recent issue saying 'Please investigate'
* Update my most recent comment
* Delete a test issue
* Remove my most recent comment
* What issues are assigned to {team\_member} this week?
* Find all high priority bugs in our current sprint
* Show me overdue issues across all projects
* What projects have the most issues?
* Search for users named {user\_name}

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Jira connector isn't currently able to handle prompts like these.

* Log time on {issue\_key}
* Transition {issue\_key} to Done

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-jira
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_jira import JiraConnector
from airbyte_agent_jira.models import JiraAuthConfig

connector = JiraConnector(
    auth_config=JiraAuthConfig(
        username="<Your Atlassian account email address>",
        password="<Your Jira API token from https://id.atlassian.com/manage-profile/security/api-tokens>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@JiraConnector.tool_utils
async def jira_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/jira/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_jira import JiraConnector, AirbyteAuthConfig

connector = JiraConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@JiraConnector.tool_utils
async def jira_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/jira/REFERENCE.md).

| Entity          | Actions                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Issues          | [API Search](/ai-agents/connectors/jira/REFERENCE.md#issues-api_search), [Create](/ai-agents/connectors/jira/REFERENCE.md#issues-create), [Get](/ai-agents/connectors/jira/REFERENCE.md#issues-get), [Update](/ai-agents/connectors/jira/REFERENCE.md#issues-update), [Delete](/ai-agents/connectors/jira/REFERENCE.md#issues-delete), [Search](/ai-agents/connectors/jira/REFERENCE.md#issues-search)                                     |
| Projects        | [API Search](/ai-agents/connectors/jira/REFERENCE.md#projects-api_search), [Get](/ai-agents/connectors/jira/REFERENCE.md#projects-get), [Search](/ai-agents/connectors/jira/REFERENCE.md#projects-search)                                                                                                                                                                                                                                  |
| Users           | [Get](/ai-agents/connectors/jira/REFERENCE.md#users-get), [List](/ai-agents/connectors/jira/REFERENCE.md#users-list), [API Search](/ai-agents/connectors/jira/REFERENCE.md#users-api_search), [Search](/ai-agents/connectors/jira/REFERENCE.md#users-search)                                                                                                                                                                               |
| Issue Fields    | [List](/ai-agents/connectors/jira/REFERENCE.md#issue-fields-list), [API Search](/ai-agents/connectors/jira/REFERENCE.md#issue-fields-api_search), [Search](/ai-agents/connectors/jira/REFERENCE.md#issue-fields-search)                                                                                                                                                                                                                    |
| Issue Comments  | [List](/ai-agents/connectors/jira/REFERENCE.md#issue-comments-list), [Create](/ai-agents/connectors/jira/REFERENCE.md#issue-comments-create), [Get](/ai-agents/connectors/jira/REFERENCE.md#issue-comments-get), [Update](/ai-agents/connectors/jira/REFERENCE.md#issue-comments-update), [Delete](/ai-agents/connectors/jira/REFERENCE.md#issue-comments-delete), [Search](/ai-agents/connectors/jira/REFERENCE.md#issue-comments-search) |
| Issue Worklogs  | [List](/ai-agents/connectors/jira/REFERENCE.md#issue-worklogs-list), [Get](/ai-agents/connectors/jira/REFERENCE.md#issue-worklogs-get), [Search](/ai-agents/connectors/jira/REFERENCE.md#issue-worklogs-search)                                                                                                                                                                                                                            |
| Issues Assignee | [Update](/ai-agents/connectors/jira/REFERENCE.md#issues-assignee-update)                                                                                                                                                                                                                                                                                                                                                                   |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/jira/AUTH.md).

### Jira API docs[​](#jira-api-docs "Direct link to Jira API docs")

See the official [Jira API reference](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.107
* **Connector version:** 1.1.7
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/jira/CHANGELOG.md)
