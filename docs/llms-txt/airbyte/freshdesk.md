# Source: https://docs.airbyte.com/integrations/sources/freshdesk.md

# Source: https://docs.airbyte.com/ai-agents/connectors/freshdesk.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-freshdesk/latest/icon.svg)

# Freshdesk

Copy Page

The Freshdesk agent connector is a Python package that equips AI agents to interact with Freshdesk through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the Freshdesk customer support platform API (v2). Provides read access to helpdesk data including tickets, contacts, agents, groups, companies, roles, satisfaction ratings, surveys, time entries, and ticket fields. Freshdesk is a cloud-based customer support solution that enables companies to manage customer conversations across email, phone, chat, and social media.

## Example questions[​](#example-questions "Direct link to Example questions")

The Freshdesk connector is optimized to handle prompts like these.

* List all open tickets in Freshdesk
* Show me all agents in the support team
* List all groups configured in Freshdesk
* Get the details of ticket #26
* Show me all companies in Freshdesk
* List all roles defined in the helpdesk
* Show me the ticket fields and their options
* List time entries for tickets
* What are the high priority tickets from last week?
* Which tickets have breached their SLA due date?
* Show me tickets assigned to agent {agent\_name}
* Find all tickets from company {company\_name}
* How many tickets were created this month by status?
* What are the satisfaction ratings for resolved tickets?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Freshdesk connector isn't currently able to handle prompts like these.

* Create a new ticket in Freshdesk
* Update the status of ticket #{ticket\_id}
* Delete a contact from Freshdesk
* Assign a ticket to a different agent

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-freshdesk
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_freshdesk import FreshdeskConnector
from airbyte_agent_freshdesk.models import FreshdeskAuthConfig

connector = FreshdeskConnector(
    auth_config=FreshdeskAuthConfig(
        api_key="<Your Freshdesk API key (found in Profile Settings)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@FreshdeskConnector.tool_utils
async def freshdesk_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/freshdesk/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_freshdesk import FreshdeskConnector, AirbyteAuthConfig

connector = FreshdeskConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@FreshdeskConnector.tool_utils
async def freshdesk_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/freshdesk/REFERENCE.md).

| Entity               | Actions                                                                                                                                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tickets              | [List](/ai-agents/connectors/freshdesk/REFERENCE.md#tickets-list), [Get](/ai-agents/connectors/freshdesk/REFERENCE.md#tickets-get), [Search](/ai-agents/connectors/freshdesk/REFERENCE.md#tickets-search) |
| Contacts             | [List](/ai-agents/connectors/freshdesk/REFERENCE.md#contacts-list), [Get](/ai-agents/connectors/freshdesk/REFERENCE.md#contacts-get)                                                                      |
| Agents               | [List](/ai-agents/connectors/freshdesk/REFERENCE.md#agents-list), [Get](/ai-agents/connectors/freshdesk/REFERENCE.md#agents-get), [Search](/ai-agents/connectors/freshdesk/REFERENCE.md#agents-search)    |
| Groups               | [List](/ai-agents/connectors/freshdesk/REFERENCE.md#groups-list), [Get](/ai-agents/connectors/freshdesk/REFERENCE.md#groups-get), [Search](/ai-agents/connectors/freshdesk/REFERENCE.md#groups-search)    |
| Companies            | [List](/ai-agents/connectors/freshdesk/REFERENCE.md#companies-list), [Get](/ai-agents/connectors/freshdesk/REFERENCE.md#companies-get)                                                                    |
| Roles                | [List](/ai-agents/connectors/freshdesk/REFERENCE.md#roles-list), [Get](/ai-agents/connectors/freshdesk/REFERENCE.md#roles-get)                                                                            |
| Satisfaction Ratings | [List](/ai-agents/connectors/freshdesk/REFERENCE.md#satisfaction-ratings-list)                                                                                                                            |
| Surveys              | [List](/ai-agents/connectors/freshdesk/REFERENCE.md#surveys-list)                                                                                                                                         |
| Time Entries         | [List](/ai-agents/connectors/freshdesk/REFERENCE.md#time-entries-list)                                                                                                                                    |
| Ticket Fields        | [List](/ai-agents/connectors/freshdesk/REFERENCE.md#ticket-fields-list)                                                                                                                                   |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/freshdesk/AUTH.md).

### Freshdesk API docs[​](#freshdesk-api-docs "Direct link to Freshdesk API docs")

See the official [Freshdesk API reference](https://developers.freshdesk.com/api/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.13
* **Connector version:** 1.0.2
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/freshdesk/CHANGELOG.md)
