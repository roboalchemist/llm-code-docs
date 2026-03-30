# Source: https://docs.airbyte.com/integrations/sources/granola.md

# Source: https://docs.airbyte.com/ai-agents/connectors/granola.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-granola/latest/icon.svg)

# Granola

Copy Page

The Granola agent connector is a Python package that equips AI agents to interact with Granola through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

The Granola API connector provides read access to meeting notes from Granola, an AI-powered meeting notes platform. This connector integrates with the Granola Enterprise API to list and retrieve notes, including summaries, transcripts, attendees, and calendar event details. Requires an Enterprise plan API key.

## Example questions[​](#example-questions "Direct link to Example questions")

The Granola connector is optimized to handle prompts like these.

* List all meeting notes from Granola
* Show me recent meeting notes
* Get the details of a specific note
* List notes created in the last week
* Find meeting notes from last month
* Which meetings had the most attendees?
* Show me notes that mention budget reviews
* What meetings happened this quarter?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Granola connector isn't currently able to handle prompts like these.

* Create a new meeting note
* Delete a meeting note
* Update an existing note
* Share a note with someone

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-granola
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_granola import GranolaConnector
from airbyte_agent_granola.models import GranolaAuthConfig

connector = GranolaConnector(
    auth_config=GranolaAuthConfig(
        api_key="<Granola Enterprise API key generated from Settings > Workspaces > API tab>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GranolaConnector.tool_utils
async def granola_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/granola/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_granola import GranolaConnector, AirbyteAuthConfig

connector = GranolaConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GranolaConnector.tool_utils
async def granola_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/granola/REFERENCE.md).

| Entity | Actions                                                                                                                                                                                       |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Notes  | [List](/ai-agents/connectors/granola/REFERENCE.md#notes-list), [Get](/ai-agents/connectors/granola/REFERENCE.md#notes-get), [Search](/ai-agents/connectors/granola/REFERENCE.md#notes-search) |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/granola/AUTH.md).

### Granola API docs[​](#granola-api-docs "Direct link to Granola API docs")

See the official [Granola API reference](https://docs.granola.ai/introduction).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.14
* **Connector version:** 1.0.3
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/granola/CHANGELOG.md)
