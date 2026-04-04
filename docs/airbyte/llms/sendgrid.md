# Source: https://docs.airbyte.com/integrations/sources/sendgrid.md

# Source: https://docs.airbyte.com/ai-agents/connectors/sendgrid.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-sendgrid/latest/icon.svg)

# Sendgrid

Copy Page

The Sendgrid agent connector is a Python package that equips AI agents to interact with Sendgrid through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the Twilio SendGrid v3 API. Provides read access to marketing campaigns, contacts, lists, segments, single sends, transactional templates, and suppression management (bounces, blocks, spam reports, invalid emails, global suppressions, suppression groups, and suppression group members).

## Example questions[​](#example-questions "Direct link to Example questions")

The Sendgrid connector is optimized to handle prompts like these.

* List all marketing contacts
* Get the details of a specific contact
* Show me all marketing lists
* List all transactional templates
* Show all single sends
* List all bounced emails
* Show all blocked email addresses
* List all spam reports
* Show all suppression groups
* How many contacts are in each marketing list?
* Which single sends were scheduled in the last month?
* What are the most common bounce reasons?
* Show me contacts created in the last 7 days

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Sendgrid connector isn't currently able to handle prompts like these.

* Send an email
* Create a new contact
* Delete a bounce record
* Update a marketing list

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-sendgrid
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_sendgrid import SendgridConnector
from airbyte_agent_sendgrid.models import SendgridAuthConfig

connector = SendgridConnector(
    auth_config=SendgridAuthConfig(
        api_key="<Your SendGrid API key (generated at https://app.sendgrid.com/settings/api_keys)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SendgridConnector.tool_utils
async def sendgrid_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/sendgrid/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_sendgrid import SendgridConnector, AirbyteAuthConfig

connector = SendgridConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SendgridConnector.tool_utils
async def sendgrid_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/sendgrid/REFERENCE.md).

| Entity                    | Actions                                                                                                                                                                                                                                 |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Contacts                  | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#contacts-list), [Get](/ai-agents/connectors/sendgrid/REFERENCE.md#contacts-get), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#contacts-search)                               |
| Lists                     | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#lists-list), [Get](/ai-agents/connectors/sendgrid/REFERENCE.md#lists-get), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#lists-search)                                        |
| Segments                  | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#segments-list), [Get](/ai-agents/connectors/sendgrid/REFERENCE.md#segments-get), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#segments-search)                               |
| Campaigns                 | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#campaigns-list), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#campaigns-search)                                                                                              |
| Singlesends               | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#singlesends-list), [Get](/ai-agents/connectors/sendgrid/REFERENCE.md#singlesends-get), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#singlesends-search)                      |
| Templates                 | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#templates-list), [Get](/ai-agents/connectors/sendgrid/REFERENCE.md#templates-get), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#templates-search)                            |
| Singlesend Stats          | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#singlesend-stats-list), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#singlesend-stats-search)                                                                                |
| Bounces                   | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#bounces-list), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#bounces-search)                                                                                                  |
| Blocks                    | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#blocks-list), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#blocks-search)                                                                                                    |
| Spam Reports              | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#spam-reports-list)                                                                                                                                                                   |
| Invalid Emails            | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#invalid-emails-list), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#invalid-emails-search)                                                                                    |
| Global Suppressions       | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#global-suppressions-list), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#global-suppressions-search)                                                                          |
| Suppression Groups        | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#suppression-groups-list), [Get](/ai-agents/connectors/sendgrid/REFERENCE.md#suppression-groups-get), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#suppression-groups-search) |
| Suppression Group Members | [List](/ai-agents/connectors/sendgrid/REFERENCE.md#suppression-group-members-list), [Search](/ai-agents/connectors/sendgrid/REFERENCE.md#suppression-group-members-search)                                                              |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/sendgrid/AUTH.md).

### Sendgrid API docs[​](#sendgrid-api-docs "Direct link to Sendgrid API docs")

See the official [Sendgrid API reference](https://docs.sendgrid.com/api-reference).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.9
* **Connector version:** 1.0.2
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/sendgrid/CHANGELOG.md)
