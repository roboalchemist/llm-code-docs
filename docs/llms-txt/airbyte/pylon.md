# Source: https://docs.airbyte.com/integrations/sources/pylon.md

# Source: https://docs.airbyte.com/ai-agents/connectors/pylon.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-pylon/latest/icon.svg)

# Pylon

Copy Page

The Pylon agent connector is a Python package that equips AI agents to interact with Pylon through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Pylon is a customer support platform that helps B2B companies manage customer interactions across Slack, email, chat widgets, and other channels. This connector provides access to issues, accounts, contacts, teams, tags, users, custom fields, ticket forms, and user roles for customer support analytics and account intelligence insights.

## Example questions[​](#example-questions "Direct link to Example questions")

The Pylon connector is optimized to handle prompts like these.

* List all open issues in Pylon
* Show me all accounts in Pylon
* List all contacts in Pylon
* What teams are configured in my Pylon workspace?
* Show me all tags used in Pylon
* List all users in my Pylon account
* Show me the custom fields configured for issues
* List all ticket forms in Pylon
* What user roles are available in Pylon?
* Show me details for a specific issue
* Get details for a specific account
* Show me details for a specific contact
* What are the most common issue sources this month?
* Show me issues assigned to a specific team
* Which accounts have the most open issues?
* Analyze issue resolution times over the last 30 days
* List contacts associated with a specific account

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Pylon connector isn't currently able to handle prompts like these.

* Delete an issue
* Delete an account
* Send a message to a customer
* Schedule a meeting with a contact

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-pylon
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_pylon import PylonConnector
from airbyte_agent_pylon.models import PylonAuthConfig

connector = PylonConnector(
    auth_config=PylonAuthConfig(
        api_token="<Your Pylon API token. Only admin users can create API tokens.>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@PylonConnector.tool_utils
async def pylon_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/pylon/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_pylon import PylonConnector, AirbyteAuthConfig

connector = PylonConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@PylonConnector.tool_utils
async def pylon_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/pylon/REFERENCE.md).

| Entity        | Actions                                                                                                                                                                                                                                                              |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Issues        | [List](/ai-agents/connectors/pylon/REFERENCE.md#issues-list), [Create](/ai-agents/connectors/pylon/REFERENCE.md#issues-create), [Get](/ai-agents/connectors/pylon/REFERENCE.md#issues-get), [Update](/ai-agents/connectors/pylon/REFERENCE.md#issues-update)         |
| Messages      | [List](/ai-agents/connectors/pylon/REFERENCE.md#messages-list)                                                                                                                                                                                                       |
| Issue Notes   | [Create](/ai-agents/connectors/pylon/REFERENCE.md#issue-notes-create)                                                                                                                                                                                                |
| Issue Threads | [Create](/ai-agents/connectors/pylon/REFERENCE.md#issue-threads-create)                                                                                                                                                                                              |
| Accounts      | [List](/ai-agents/connectors/pylon/REFERENCE.md#accounts-list), [Create](/ai-agents/connectors/pylon/REFERENCE.md#accounts-create), [Get](/ai-agents/connectors/pylon/REFERENCE.md#accounts-get), [Update](/ai-agents/connectors/pylon/REFERENCE.md#accounts-update) |
| Contacts      | [List](/ai-agents/connectors/pylon/REFERENCE.md#contacts-list), [Create](/ai-agents/connectors/pylon/REFERENCE.md#contacts-create), [Get](/ai-agents/connectors/pylon/REFERENCE.md#contacts-get), [Update](/ai-agents/connectors/pylon/REFERENCE.md#contacts-update) |
| Teams         | [List](/ai-agents/connectors/pylon/REFERENCE.md#teams-list), [Create](/ai-agents/connectors/pylon/REFERENCE.md#teams-create), [Get](/ai-agents/connectors/pylon/REFERENCE.md#teams-get), [Update](/ai-agents/connectors/pylon/REFERENCE.md#teams-update)             |
| Tags          | [List](/ai-agents/connectors/pylon/REFERENCE.md#tags-list), [Create](/ai-agents/connectors/pylon/REFERENCE.md#tags-create), [Get](/ai-agents/connectors/pylon/REFERENCE.md#tags-get), [Update](/ai-agents/connectors/pylon/REFERENCE.md#tags-update)                 |
| Users         | [List](/ai-agents/connectors/pylon/REFERENCE.md#users-list), [Get](/ai-agents/connectors/pylon/REFERENCE.md#users-get)                                                                                                                                               |
| Custom Fields | [List](/ai-agents/connectors/pylon/REFERENCE.md#custom-fields-list), [Get](/ai-agents/connectors/pylon/REFERENCE.md#custom-fields-get)                                                                                                                               |
| Ticket Forms  | [List](/ai-agents/connectors/pylon/REFERENCE.md#ticket-forms-list)                                                                                                                                                                                                   |
| User Roles    | [List](/ai-agents/connectors/pylon/REFERENCE.md#user-roles-list)                                                                                                                                                                                                     |
| Tasks         | [Create](/ai-agents/connectors/pylon/REFERENCE.md#tasks-create), [Update](/ai-agents/connectors/pylon/REFERENCE.md#tasks-update)                                                                                                                                     |
| Projects      | [Create](/ai-agents/connectors/pylon/REFERENCE.md#projects-create), [Update](/ai-agents/connectors/pylon/REFERENCE.md#projects-update)                                                                                                                               |
| Milestones    | [Create](/ai-agents/connectors/pylon/REFERENCE.md#milestones-create), [Update](/ai-agents/connectors/pylon/REFERENCE.md#milestones-update)                                                                                                                           |
| Articles      | [Create](/ai-agents/connectors/pylon/REFERENCE.md#articles-create), [Update](/ai-agents/connectors/pylon/REFERENCE.md#articles-update)                                                                                                                               |
| Collections   | [Create](/ai-agents/connectors/pylon/REFERENCE.md#collections-create)                                                                                                                                                                                                |
| Me            | [Get](/ai-agents/connectors/pylon/REFERENCE.md#me-get)                                                                                                                                                                                                               |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/pylon/AUTH.md).

### Pylon API docs[​](#pylon-api-docs "Direct link to Pylon API docs")

See the official [Pylon API reference](https://docs.usepylon.com/pylon-docs/developer/api/api-reference).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.12
* **Connector version:** 0.1.4
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/pylon/CHANGELOG.md)
