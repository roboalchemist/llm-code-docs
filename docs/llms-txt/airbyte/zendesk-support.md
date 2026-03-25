# Source: https://docs.airbyte.com/integrations/sources/zendesk-support.md

# Source: https://docs.airbyte.com/ai-agents/connectors/zendesk-support.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-zendesk-support/latest/icon.svg)

# Zendesk-Support

Copy Page

The Zendesk-Support agent connector is a Python package that equips AI agents to interact with Zendesk-Support through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Zendesk Support is a customer service platform that helps businesses manage support tickets, customer interactions, and help center content. This connector provides access to tickets, users, organizations, groups, comments, attachments, automations, triggers, macros, views, satisfaction ratings, SLA policies, and help center articles for customer support analytics and service performance insights.

## Example questions[​](#example-questions "Direct link to Example questions")

The Zendesk-Support connector is optimized to handle prompts like these.

* Show me the tickets assigned to me last week
* List all unresolved tickets
* Show me the details of recent tickets
* What are the top 5 support issues our organization has faced this month?
* Analyze the satisfaction ratings for our support team in the last 30 days
* Compare ticket resolution times across different support groups
* Identify the most common ticket fields used in our support workflow
* Summarize the performance of our SLA policies this quarter

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Zendesk-Support connector isn't currently able to handle prompts like these.

* Create a new support ticket for {customer}
* Update the priority of this ticket
* Assign this ticket to {team\_member}
* Delete these old support tickets
* Send an automatic response to {customer}

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-zendesk-support
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_zendesk_support import ZendeskSupportConnector
from airbyte_agent_zendesk_support.models import ZendeskSupportApiTokenAuthConfig

connector = ZendeskSupportConnector(
    auth_config=ZendeskSupportApiTokenAuthConfig(
        email="<Your Zendesk account email address>",
        api_token="<Your Zendesk API token from Admin Center>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZendeskSupportConnector.tool_utils
async def zendesk_support_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/zendesk-support/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_zendesk_support import ZendeskSupportConnector, AirbyteAuthConfig

connector = ZendeskSupportConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZendeskSupportConnector.tool_utils
async def zendesk_support_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/zendesk-support/REFERENCE.md).

| Entity                   | Actions                                                                                                                                                                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tickets                  | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#tickets-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#tickets-get), [Search](/ai-agents/connectors/zendesk-support/REFERENCE.md#tickets-search)                                         |
| Users                    | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#users-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#users-get), [Search](/ai-agents/connectors/zendesk-support/REFERENCE.md#users-search)                                               |
| Organizations            | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#organizations-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#organizations-get), [Search](/ai-agents/connectors/zendesk-support/REFERENCE.md#organizations-search)                       |
| Groups                   | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#groups-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#groups-get), [Search](/ai-agents/connectors/zendesk-support/REFERENCE.md#groups-search)                                            |
| Ticket Comments          | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-comments-list), [Search](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-comments-search)                                                                                                |
| Attachments              | [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#attachments-get), [Download](/ai-agents/connectors/zendesk-support/REFERENCE.md#attachments-download)                                                                                                      |
| Ticket Audits            | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-audits-list), [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-audits-list), [Search](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-audits-search)                     |
| Ticket Metrics           | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-metrics-list), [Search](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-metrics-search)                                                                                                  |
| Ticket Fields            | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-fields-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-fields-get), [Search](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-fields-search)                       |
| Brands                   | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#brands-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#brands-get), [Search](/ai-agents/connectors/zendesk-support/REFERENCE.md#brands-search)                                            |
| Views                    | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#views-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#views-get)                                                                                                                          |
| Macros                   | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#macros-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#macros-get)                                                                                                                        |
| Triggers                 | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#triggers-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#triggers-get)                                                                                                                    |
| Automations              | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#automations-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#automations-get)                                                                                                              |
| Tags                     | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#tags-list), [Search](/ai-agents/connectors/zendesk-support/REFERENCE.md#tags-search)                                                                                                                      |
| Satisfaction Ratings     | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#satisfaction-ratings-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#satisfaction-ratings-get), [Search](/ai-agents/connectors/zendesk-support/REFERENCE.md#satisfaction-ratings-search)  |
| Group Memberships        | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#group-memberships-list)                                                                                                                                                                                   |
| Organization Memberships | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#organization-memberships-list)                                                                                                                                                                            |
| Sla Policies             | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#sla-policies-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#sla-policies-get)                                                                                                            |
| Ticket Forms             | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-forms-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-forms-get), [Search](/ai-agents/connectors/zendesk-support/REFERENCE.md#ticket-forms-search)                          |
| Articles                 | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#articles-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#articles-get)                                                                                                                    |
| Article Attachments      | [List](/ai-agents/connectors/zendesk-support/REFERENCE.md#article-attachments-list), [Get](/ai-agents/connectors/zendesk-support/REFERENCE.md#article-attachments-get), [Download](/ai-agents/connectors/zendesk-support/REFERENCE.md#article-attachments-download) |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/zendesk-support/AUTH.md).

### Zendesk-Support API docs[​](#zendesk-support-api-docs "Direct link to Zendesk-Support API docs")

See the official [Zendesk-Support API reference](https://developer.zendesk.com/api-reference/ticketing/introduction/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.18.119
* **Connector version:** 0.1.16
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/zendesk-support/CHANGELOG.md)
