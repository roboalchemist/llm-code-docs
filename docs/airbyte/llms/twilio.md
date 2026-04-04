# Source: https://docs.airbyte.com/integrations/sources/twilio.md

# Source: https://docs.airbyte.com/ai-agents/connectors/twilio.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-twilio/latest/icon.svg)

# Twilio

Copy Page

The Twilio agent connector is a Python package that equips AI agents to interact with Twilio through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the Twilio REST API. Provides read access to core Twilio resources including accounts, calls, messages, recordings, conferences, incoming phone numbers, usage records, addresses, queues, transcriptions, and outgoing caller IDs. Uses HTTP Basic authentication with Account SID and Auth Token.

## Example questions[​](#example-questions "Direct link to Example questions")

The Twilio connector is optimized to handle prompts like these.

* List all calls from the last 7 days
* Show me recent inbound SMS messages
* List all active phone numbers on my account
* Show me details for a specific call
* List all recordings
* Show me conference calls
* List usage records for my account
* Show me all queues
* List outgoing caller IDs
* Show me addresses on my account
* List transcriptions
* What are my top 10 most expensive calls this month?
* How many SMS messages did I send vs receive in the last 30 days?
* Summarize my usage costs by category
* Which phone numbers have the most incoming calls?
* Show me all failed messages and their error codes
* What is the average call duration for outbound calls?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Twilio connector isn't currently able to handle prompts like these.

* Send a new SMS message
* Make a phone call
* Purchase a new phone number
* Delete a recording
* Create a new queue

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-twilio
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_twilio import TwilioConnector
from airbyte_agent_twilio.models import TwilioAuthConfig

connector = TwilioConnector(
    auth_config=TwilioAuthConfig(
        account_sid="<Your Twilio Account SID (starts with AC)>",
        auth_token="<Your Twilio Auth Token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@TwilioConnector.tool_utils
async def twilio_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/twilio/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_twilio import TwilioConnector, AirbyteAuthConfig

connector = TwilioConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@TwilioConnector.tool_utils
async def twilio_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/twilio/REFERENCE.md).

| Entity                 | Actions                                                                                                                                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accounts               | [List](/ai-agents/connectors/twilio/REFERENCE.md#accounts-list), [Get](/ai-agents/connectors/twilio/REFERENCE.md#accounts-get), [Search](/ai-agents/connectors/twilio/REFERENCE.md#accounts-search)                                           |
| Calls                  | [List](/ai-agents/connectors/twilio/REFERENCE.md#calls-list), [Get](/ai-agents/connectors/twilio/REFERENCE.md#calls-get), [Search](/ai-agents/connectors/twilio/REFERENCE.md#calls-search)                                                    |
| Messages               | [List](/ai-agents/connectors/twilio/REFERENCE.md#messages-list), [Get](/ai-agents/connectors/twilio/REFERENCE.md#messages-get), [Search](/ai-agents/connectors/twilio/REFERENCE.md#messages-search)                                           |
| Incoming Phone Numbers | [List](/ai-agents/connectors/twilio/REFERENCE.md#incoming-phone-numbers-list), [Get](/ai-agents/connectors/twilio/REFERENCE.md#incoming-phone-numbers-get), [Search](/ai-agents/connectors/twilio/REFERENCE.md#incoming-phone-numbers-search) |
| Recordings             | [List](/ai-agents/connectors/twilio/REFERENCE.md#recordings-list), [Get](/ai-agents/connectors/twilio/REFERENCE.md#recordings-get), [Search](/ai-agents/connectors/twilio/REFERENCE.md#recordings-search)                                     |
| Conferences            | [List](/ai-agents/connectors/twilio/REFERENCE.md#conferences-list), [Get](/ai-agents/connectors/twilio/REFERENCE.md#conferences-get), [Search](/ai-agents/connectors/twilio/REFERENCE.md#conferences-search)                                  |
| Usage Records          | [List](/ai-agents/connectors/twilio/REFERENCE.md#usage-records-list), [Search](/ai-agents/connectors/twilio/REFERENCE.md#usage-records-search)                                                                                                |
| Addresses              | [List](/ai-agents/connectors/twilio/REFERENCE.md#addresses-list), [Get](/ai-agents/connectors/twilio/REFERENCE.md#addresses-get), [Search](/ai-agents/connectors/twilio/REFERENCE.md#addresses-search)                                        |
| Queues                 | [List](/ai-agents/connectors/twilio/REFERENCE.md#queues-list), [Get](/ai-agents/connectors/twilio/REFERENCE.md#queues-get), [Search](/ai-agents/connectors/twilio/REFERENCE.md#queues-search)                                                 |
| Transcriptions         | [List](/ai-agents/connectors/twilio/REFERENCE.md#transcriptions-list), [Get](/ai-agents/connectors/twilio/REFERENCE.md#transcriptions-get), [Search](/ai-agents/connectors/twilio/REFERENCE.md#transcriptions-search)                         |
| Outgoing Caller Ids    | [List](/ai-agents/connectors/twilio/REFERENCE.md#outgoing-caller-ids-list), [Get](/ai-agents/connectors/twilio/REFERENCE.md#outgoing-caller-ids-get), [Search](/ai-agents/connectors/twilio/REFERENCE.md#outgoing-caller-ids-search)          |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/twilio/AUTH.md).

### Twilio API docs[​](#twilio-api-docs "Direct link to Twilio API docs")

See the official [Twilio API reference](https://www.twilio.com/docs/usage/api).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.2
* **Connector version:** 1.0.1
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/twilio/CHANGELOG.md)
