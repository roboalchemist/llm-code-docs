# Source: https://docs.airbyte.com/integrations/sources/intercom.md

# Source: https://docs.airbyte.com/ai-agents/connectors/intercom.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-intercom/latest/icon.svg)

# Intercom

Copy Page

The Intercom agent connector is a Python package that equips AI agents to interact with Intercom through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Intercom is a customer messaging platform that enables businesses to communicate with customers through chat, email, and in-app messaging. This connector provides access to core Intercom entities including contacts, conversations, companies, teams, admins, tags, and segments for customer support analytics and insights. It also supports creating and updating contacts, creating notes, creating internal articles, creating and updating companies, and creating tags.

## Example questions[​](#example-questions "Direct link to Example questions")

The Intercom connector is optimized to handle prompts like these.

* List all contacts in my Intercom workspace
* List all companies in Intercom
* What teams are configured in my workspace?
* Show me all admins in my Intercom account
* List all tags used in Intercom
* Show me all customer segments
* Show me details for a recent contact
* Show me details for a recent company
* Show me details for a recent conversation
* Create a new lead contact named 'Jane Smith' with email <jane@example.com>
* Create an internal article titled 'Onboarding Guide' with instructions for new team members
* Create a company named 'Acme Corp' with company\_id 'acme-001'
* Create a tag named 'VIP Customer'
* Update the name of contact {id} to 'John Updated'
* Add a note to contact {id} saying 'Followed up on support request'
* Show me conversations from the last week
* List conversations assigned to team {team\_id}
* Show me open conversations

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Intercom connector isn't currently able to handle prompts like these.

* Send a message to a customer
* Delete a conversation
* Delete a contact
* Delete a company
* Assign a conversation to an admin

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-intercom
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_intercom import IntercomConnector
from airbyte_agent_intercom.models import IntercomAuthConfig

connector = IntercomConnector(
    auth_config=IntercomAuthConfig(
        access_token="<Your Intercom API Access Token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@IntercomConnector.tool_utils
async def intercom_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/intercom/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_intercom import IntercomConnector, AirbyteAuthConfig

connector = IntercomConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@IntercomConnector.tool_utils
async def intercom_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/intercom/REFERENCE.md).

| Entity            | Actions                                                                                                                                                                                                                                                                                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Contacts          | [List](/ai-agents/connectors/intercom/REFERENCE.md#contacts-list), [Create](/ai-agents/connectors/intercom/REFERENCE.md#contacts-create), [Get](/ai-agents/connectors/intercom/REFERENCE.md#contacts-get), [Update](/ai-agents/connectors/intercom/REFERENCE.md#contacts-update), [Search](/ai-agents/connectors/intercom/REFERENCE.md#contacts-search)      |
| Conversations     | [List](/ai-agents/connectors/intercom/REFERENCE.md#conversations-list), [Get](/ai-agents/connectors/intercom/REFERENCE.md#conversations-get), [Search](/ai-agents/connectors/intercom/REFERENCE.md#conversations-search)                                                                                                                                     |
| Companies         | [List](/ai-agents/connectors/intercom/REFERENCE.md#companies-list), [Create](/ai-agents/connectors/intercom/REFERENCE.md#companies-create), [Get](/ai-agents/connectors/intercom/REFERENCE.md#companies-get), [Update](/ai-agents/connectors/intercom/REFERENCE.md#companies-update), [Search](/ai-agents/connectors/intercom/REFERENCE.md#companies-search) |
| Teams             | [List](/ai-agents/connectors/intercom/REFERENCE.md#teams-list), [Get](/ai-agents/connectors/intercom/REFERENCE.md#teams-get), [Search](/ai-agents/connectors/intercom/REFERENCE.md#teams-search)                                                                                                                                                             |
| Admins            | [List](/ai-agents/connectors/intercom/REFERENCE.md#admins-list), [Get](/ai-agents/connectors/intercom/REFERENCE.md#admins-get)                                                                                                                                                                                                                               |
| Tags              | [List](/ai-agents/connectors/intercom/REFERENCE.md#tags-list), [Create](/ai-agents/connectors/intercom/REFERENCE.md#tags-create), [Get](/ai-agents/connectors/intercom/REFERENCE.md#tags-get)                                                                                                                                                                |
| Notes             | [Create](/ai-agents/connectors/intercom/REFERENCE.md#notes-create)                                                                                                                                                                                                                                                                                           |
| Segments          | [List](/ai-agents/connectors/intercom/REFERENCE.md#segments-list), [Get](/ai-agents/connectors/intercom/REFERENCE.md#segments-get)                                                                                                                                                                                                                           |
| Internal Articles | [Create](/ai-agents/connectors/intercom/REFERENCE.md#internal-articles-create)                                                                                                                                                                                                                                                                               |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/intercom/AUTH.md).

### Intercom API docs[​](#intercom-api-docs "Direct link to Intercom API docs")

See the official [Intercom API reference](https://developers.intercom.com/docs/references/rest-api/api.intercom.io).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.86
* **Connector version:** 0.1.9
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/intercom/CHANGELOG.md)
