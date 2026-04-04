# Source: https://docs.airbyte.com/integrations/sources/zendesk-chat.md

# Source: https://docs.airbyte.com/ai-agents/connectors/zendesk-chat.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-zendesk-chat/latest/icon.svg)

# Zendesk-Chat

Copy Page

The Zendesk-Chat agent connector is a Python package that equips AI agents to interact with Zendesk-Chat through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Zendesk Chat enables real-time customer support through live chat. This connector provides access to chat transcripts, agents, departments, shortcuts, triggers, and other chat configuration data for analytics and support insights.

## Supported Entities[​](#supported-entities "Direct link to Supported Entities")

* **accounts**: Account information and billing details
* **agents**: Chat agents with roles and department assignments
* **agent\_timeline**: Agent activity timeline (incremental export)
* **bans**: Banned visitors (IP and visitor-based)
* **chats**: Chat transcripts with full conversation history (incremental export)
* **departments**: Chat departments for routing
* **goals**: Conversion goals for tracking
* **roles**: Agent role definitions
* **routing\_settings**: Account-level routing configuration
* **shortcuts**: Canned responses for agents
* **skills**: Agent skills for skill-based routing
* **triggers**: Automated chat triggers

## Rate Limits[​](#rate-limits "Direct link to Rate Limits")

Zendesk Chat API uses the `Retry-After` header for rate limit backoff. The connector handles this automatically.

## Example questions[​](#example-questions "Direct link to Example questions")

The Zendesk-Chat connector is optimized to handle prompts like these.

* List all banned visitors
* List all departments with their settings
* Show me all chats from last week
* List all agents in the support department
* What are the most used chat shortcuts?
* Show chat volume by department
* What triggers are currently active?
* Show agent activity timeline for today

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Zendesk-Chat connector isn't currently able to handle prompts like these.

* Start a new chat session
* Send a message to a visitor
* Create a new agent
* Update department settings
* Delete a shortcut

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-zendesk-chat
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_zendesk_chat import ZendeskChatConnector
from airbyte_agent_zendesk_chat.models import ZendeskChatAuthConfig

connector = ZendeskChatConnector(
    auth_config=ZendeskChatAuthConfig(
        access_token="<Your Zendesk Chat OAuth 2.0 access token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZendeskChatConnector.tool_utils
async def zendesk_chat_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/zendesk-chat/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_zendesk_chat import ZendeskChatConnector, AirbyteAuthConfig

connector = ZendeskChatConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZendeskChatConnector.tool_utils
async def zendesk_chat_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/zendesk-chat/REFERENCE.md).

| Entity           | Actions                                                                                                                                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Accounts         | [Get](/ai-agents/connectors/zendesk-chat/REFERENCE.md#accounts-get)                                                                                                                                                            |
| Agents           | [List](/ai-agents/connectors/zendesk-chat/REFERENCE.md#agents-list), [Get](/ai-agents/connectors/zendesk-chat/REFERENCE.md#agents-get), [Search](/ai-agents/connectors/zendesk-chat/REFERENCE.md#agents-search)                |
| Agent Timeline   | [List](/ai-agents/connectors/zendesk-chat/REFERENCE.md#agent-timeline-list)                                                                                                                                                    |
| Bans             | [List](/ai-agents/connectors/zendesk-chat/REFERENCE.md#bans-list), [Get](/ai-agents/connectors/zendesk-chat/REFERENCE.md#bans-get)                                                                                             |
| Chats            | [List](/ai-agents/connectors/zendesk-chat/REFERENCE.md#chats-list), [Get](/ai-agents/connectors/zendesk-chat/REFERENCE.md#chats-get), [Search](/ai-agents/connectors/zendesk-chat/REFERENCE.md#chats-search)                   |
| Departments      | [List](/ai-agents/connectors/zendesk-chat/REFERENCE.md#departments-list), [Get](/ai-agents/connectors/zendesk-chat/REFERENCE.md#departments-get), [Search](/ai-agents/connectors/zendesk-chat/REFERENCE.md#departments-search) |
| Goals            | [List](/ai-agents/connectors/zendesk-chat/REFERENCE.md#goals-list), [Get](/ai-agents/connectors/zendesk-chat/REFERENCE.md#goals-get)                                                                                           |
| Roles            | [List](/ai-agents/connectors/zendesk-chat/REFERENCE.md#roles-list), [Get](/ai-agents/connectors/zendesk-chat/REFERENCE.md#roles-get)                                                                                           |
| Routing Settings | [Get](/ai-agents/connectors/zendesk-chat/REFERENCE.md#routing-settings-get)                                                                                                                                                    |
| Shortcuts        | [List](/ai-agents/connectors/zendesk-chat/REFERENCE.md#shortcuts-list), [Get](/ai-agents/connectors/zendesk-chat/REFERENCE.md#shortcuts-get), [Search](/ai-agents/connectors/zendesk-chat/REFERENCE.md#shortcuts-search)       |
| Skills           | [List](/ai-agents/connectors/zendesk-chat/REFERENCE.md#skills-list), [Get](/ai-agents/connectors/zendesk-chat/REFERENCE.md#skills-get)                                                                                         |
| Triggers         | [List](/ai-agents/connectors/zendesk-chat/REFERENCE.md#triggers-list), [Search](/ai-agents/connectors/zendesk-chat/REFERENCE.md#triggers-search)                                                                               |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/zendesk-chat/AUTH.md).

### Zendesk-Chat API docs[​](#zendesk-chat-api-docs "Direct link to Zendesk-Chat API docs")

See the official [Zendesk-Chat API reference](https://developer.zendesk.com/api-reference/live-chat/chat-api/introduction/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.66
* **Connector version:** 0.1.9
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/zendesk-chat/CHANGELOG.md)
