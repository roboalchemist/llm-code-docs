# Source: https://docs.airbyte.com/integrations/sources/amplitude.md

# Source: https://docs.airbyte.com/ai-agents/connectors/amplitude.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-amplitude/latest/icon.svg)

# Amplitude

Copy Page

The Amplitude agent connector is a Python package that equips AI agents to interact with Amplitude through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the Amplitude Analytics API. Provides access to core analytics data including event exports, cohort definitions, chart annotations, event type listings, active user counts, and average session length metrics. Authentication uses HTTP Basic with your Amplitude API key and secret key.

## Example questions[​](#example-questions "Direct link to Example questions")

The Amplitude connector is optimized to handle prompts like these.

* List all chart annotations in Amplitude
* Show me all cohorts
* List all event types
* Which cohorts have more than 1000 users?
* What are the most popular event types by total count?
* Show me annotations created in the last month

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Amplitude connector isn't currently able to handle prompts like these.

* Create a new annotation
* Delete a cohort
* Export raw event data

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-amplitude
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_amplitude import AmplitudeConnector
from airbyte_agent_amplitude.models import AmplitudeAuthConfig

connector = AmplitudeConnector(
    auth_config=AmplitudeAuthConfig(
        api_key="<Your Amplitude project API key. Find it in Settings > Projects in your Amplitude account.
>",
        secret_key="<Your Amplitude project secret key. Find it in Settings > Projects in your Amplitude account.
>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AmplitudeConnector.tool_utils
async def amplitude_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/amplitude/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_amplitude import AmplitudeConnector, AirbyteAuthConfig

connector = AmplitudeConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AmplitudeConnector.tool_utils
async def amplitude_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/amplitude/REFERENCE.md).

| Entity                 | Actions                                                                                                                                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Annotations            | [List](/ai-agents/connectors/amplitude/REFERENCE.md#annotations-list), [Get](/ai-agents/connectors/amplitude/REFERENCE.md#annotations-get), [Search](/ai-agents/connectors/amplitude/REFERENCE.md#annotations-search) |
| Cohorts                | [List](/ai-agents/connectors/amplitude/REFERENCE.md#cohorts-list), [Get](/ai-agents/connectors/amplitude/REFERENCE.md#cohorts-get), [Search](/ai-agents/connectors/amplitude/REFERENCE.md#cohorts-search)             |
| Events List            | [List](/ai-agents/connectors/amplitude/REFERENCE.md#events-list-list), [Search](/ai-agents/connectors/amplitude/REFERENCE.md#events-list-search)                                                                      |
| Active Users           | [List](/ai-agents/connectors/amplitude/REFERENCE.md#active-users-list), [Search](/ai-agents/connectors/amplitude/REFERENCE.md#active-users-search)                                                                    |
| Average Session Length | [List](/ai-agents/connectors/amplitude/REFERENCE.md#average-session-length-list), [Search](/ai-agents/connectors/amplitude/REFERENCE.md#average-session-length-search)                                                |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/amplitude/AUTH.md).

### Amplitude API docs[​](#amplitude-api-docs "Direct link to Amplitude API docs")

See the official [Amplitude API reference](https://www.docs.developers.amplitude.com/analytics/apis/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.5
* **Connector version:** 1.0.2
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/amplitude/CHANGELOG.md)
