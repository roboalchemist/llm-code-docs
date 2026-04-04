# Source: https://docs.airbyte.com/integrations/sources/klaviyo.md

# Source: https://docs.airbyte.com/ai-agents/connectors/klaviyo.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-klaviyo/latest/icon.svg)

# Klaviyo

Copy Page

The Klaviyo agent connector is a Python package that equips AI agents to interact with Klaviyo through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Klaviyo is a marketing automation platform that helps businesses build customer relationships through personalized email, SMS, and push notifications. This connector provides access to Klaviyo's core entities including profiles, lists, campaigns, events, metrics, flows, and email templates for marketing analytics and customer engagement insights.

## Example questions[​](#example-questions "Direct link to Example questions")

The Klaviyo connector is optimized to handle prompts like these.

* List all profiles in my Klaviyo account
* Show me details for a recent profile
* Show me all email lists
* Show me details for a recent email list
* What campaigns have been created?
* Show me details for a recent campaign
* Show me all email campaigns
* List all events for tracking customer actions
* Show me all metrics (event types)
* Show me details for a recent metric
* What automated flows are configured?
* Show me details for a recent flow
* List all email templates
* Show me details for a recent email template

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Klaviyo connector isn't currently able to handle prompts like these.

* Create a new profile
* Update a profile's email address
* Delete a list
* Send an email campaign
* Add a profile to a list

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-klaviyo
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_klaviyo import KlaviyoConnector
from airbyte_agent_klaviyo.models import KlaviyoAuthConfig

connector = KlaviyoConnector(
    auth_config=KlaviyoAuthConfig(
        api_key="<Your Klaviyo private API key>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@KlaviyoConnector.tool_utils
async def klaviyo_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/klaviyo/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_klaviyo import KlaviyoConnector, AirbyteAuthConfig

connector = KlaviyoConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@KlaviyoConnector.tool_utils
async def klaviyo_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/klaviyo/REFERENCE.md).

| Entity          | Actions                                                                                                                                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Profiles        | [List](/ai-agents/connectors/klaviyo/REFERENCE.md#profiles-list), [Get](/ai-agents/connectors/klaviyo/REFERENCE.md#profiles-get), [Search](/ai-agents/connectors/klaviyo/REFERENCE.md#profiles-search)                      |
| Lists           | [List](/ai-agents/connectors/klaviyo/REFERENCE.md#lists-list), [Get](/ai-agents/connectors/klaviyo/REFERENCE.md#lists-get), [Search](/ai-agents/connectors/klaviyo/REFERENCE.md#lists-search)                               |
| Campaigns       | [List](/ai-agents/connectors/klaviyo/REFERENCE.md#campaigns-list), [Get](/ai-agents/connectors/klaviyo/REFERENCE.md#campaigns-get), [Search](/ai-agents/connectors/klaviyo/REFERENCE.md#campaigns-search)                   |
| Events          | [List](/ai-agents/connectors/klaviyo/REFERENCE.md#events-list), [Search](/ai-agents/connectors/klaviyo/REFERENCE.md#events-search)                                                                                          |
| Metrics         | [List](/ai-agents/connectors/klaviyo/REFERENCE.md#metrics-list), [Get](/ai-agents/connectors/klaviyo/REFERENCE.md#metrics-get), [Search](/ai-agents/connectors/klaviyo/REFERENCE.md#metrics-search)                         |
| Flows           | [List](/ai-agents/connectors/klaviyo/REFERENCE.md#flows-list), [Get](/ai-agents/connectors/klaviyo/REFERENCE.md#flows-get), [Search](/ai-agents/connectors/klaviyo/REFERENCE.md#flows-search)                               |
| Email Templates | [List](/ai-agents/connectors/klaviyo/REFERENCE.md#email-templates-list), [Get](/ai-agents/connectors/klaviyo/REFERENCE.md#email-templates-get), [Search](/ai-agents/connectors/klaviyo/REFERENCE.md#email-templates-search) |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/klaviyo/AUTH.md).

### Klaviyo API docs[​](#klaviyo-api-docs "Direct link to Klaviyo API docs")

See the official [Klaviyo API reference](https://developers.klaviyo.com/en/reference/api_overview).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.42
* **Connector version:** 1.0.3
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/klaviyo/CHANGELOG.md)
