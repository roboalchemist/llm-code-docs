# Source: https://docs.airbyte.com/integrations/sources/zendesk-talk.md

# Source: https://docs.airbyte.com/ai-agents/connectors/zendesk-talk.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-zendesk-talk/latest/icon.svg)

# Zendesk-Talk

Copy Page

The Zendesk-Talk agent connector is a Python package that equips AI agents to interact with Zendesk-Talk through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the Zendesk Talk (Voice) API. Provides access to phone numbers, addresses, greetings, IVR configurations, call data, and agent/account statistics for Zendesk Talk voice support channels.

## Example questions[​](#example-questions "Direct link to Example questions")

The Zendesk-Talk connector is optimized to handle prompts like these.

* List all phone numbers in our Zendesk Talk account
* Show all addresses on file
* List all IVR configurations
* Show all greetings
* List greeting categories
* Show agent activity statistics
* Show the account overview stats
* Show current queue activity
* Which phone numbers have SMS enabled?
* Find agents who have missed the most calls today
* What is the average call duration across all calls?
* Which phone numbers are toll-free?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Zendesk-Talk connector isn't currently able to handle prompts like these.

* Create a new phone number
* Delete an IVR configuration
* Update a greeting
* Make an outbound call

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-zendesk-talk
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_zendesk_talk import ZendeskTalkConnector
from airbyte_agent_zendesk_talk.models import ZendeskTalkApiTokenAuthConfig

connector = ZendeskTalkConnector(
    auth_config=ZendeskTalkApiTokenAuthConfig(
        email="<Your Zendesk account email address>",
        api_token="<Your Zendesk API token from Admin Center>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZendeskTalkConnector.tool_utils
async def zendesk_talk_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/zendesk-talk/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_zendesk_talk import ZendeskTalkConnector, AirbyteAuthConfig

connector = ZendeskTalkConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZendeskTalkConnector.tool_utils
async def zendesk_talk_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/zendesk-talk/REFERENCE.md).

| Entity                 | Actions                                                                                                                                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Phone Numbers          | [List](/ai-agents/connectors/zendesk-talk/REFERENCE.md#phone-numbers-list), [Get](/ai-agents/connectors/zendesk-talk/REFERENCE.md#phone-numbers-get), [Search](/ai-agents/connectors/zendesk-talk/REFERENCE.md#phone-numbers-search)                   |
| Addresses              | [List](/ai-agents/connectors/zendesk-talk/REFERENCE.md#addresses-list), [Get](/ai-agents/connectors/zendesk-talk/REFERENCE.md#addresses-get), [Search](/ai-agents/connectors/zendesk-talk/REFERENCE.md#addresses-search)                               |
| Greetings              | [List](/ai-agents/connectors/zendesk-talk/REFERENCE.md#greetings-list), [Get](/ai-agents/connectors/zendesk-talk/REFERENCE.md#greetings-get), [Search](/ai-agents/connectors/zendesk-talk/REFERENCE.md#greetings-search)                               |
| Greeting Categories    | [List](/ai-agents/connectors/zendesk-talk/REFERENCE.md#greeting-categories-list), [Get](/ai-agents/connectors/zendesk-talk/REFERENCE.md#greeting-categories-get), [Search](/ai-agents/connectors/zendesk-talk/REFERENCE.md#greeting-categories-search) |
| Ivrs                   | [List](/ai-agents/connectors/zendesk-talk/REFERENCE.md#ivrs-list), [Get](/ai-agents/connectors/zendesk-talk/REFERENCE.md#ivrs-get), [Search](/ai-agents/connectors/zendesk-talk/REFERENCE.md#ivrs-search)                                              |
| Agents Activity        | [List](/ai-agents/connectors/zendesk-talk/REFERENCE.md#agents-activity-list), [Search](/ai-agents/connectors/zendesk-talk/REFERENCE.md#agents-activity-search)                                                                                         |
| Agents Overview        | [List](/ai-agents/connectors/zendesk-talk/REFERENCE.md#agents-overview-list), [Search](/ai-agents/connectors/zendesk-talk/REFERENCE.md#agents-overview-search)                                                                                         |
| Account Overview       | [List](/ai-agents/connectors/zendesk-talk/REFERENCE.md#account-overview-list), [Search](/ai-agents/connectors/zendesk-talk/REFERENCE.md#account-overview-search)                                                                                       |
| Current Queue Activity | [List](/ai-agents/connectors/zendesk-talk/REFERENCE.md#current-queue-activity-list), [Search](/ai-agents/connectors/zendesk-talk/REFERENCE.md#current-queue-activity-search)                                                                           |
| Calls                  | [List](/ai-agents/connectors/zendesk-talk/REFERENCE.md#calls-list), [Search](/ai-agents/connectors/zendesk-talk/REFERENCE.md#calls-search)                                                                                                             |
| Call Legs              | [List](/ai-agents/connectors/zendesk-talk/REFERENCE.md#call-legs-list), [Search](/ai-agents/connectors/zendesk-talk/REFERENCE.md#call-legs-search)                                                                                                     |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/zendesk-talk/AUTH.md).

### Zendesk-Talk API docs[​](#zendesk-talk-api-docs "Direct link to Zendesk-Talk API docs")

See the official [Zendesk-Talk API reference](https://developer.zendesk.com/api-reference/voice/talk-api/introduction/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.1
* **Connector version:** 1.0.0
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/zendesk-talk/CHANGELOG.md)
