# Source: https://docs.airbyte.com/integrations/sources/gmail.md

# Source: https://docs.airbyte.com/ai-agents/connectors/gmail.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-gmail/latest/icon.svg)

# Gmail

Copy Page

The Gmail agent connector is a Python package that equips AI agents to interact with Gmail through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Gmail is Google's email service that provides email sending, receiving, and organization capabilities. This connector provides access to messages, threads, labels, drafts, and user profile information. It supports read operations for listing and retrieving email data, as well as write operations including sending messages, managing drafts, modifying message labels, and creating or updating labels.

## Example questions[​](#example-questions "Direct link to Example questions")

The Gmail connector is optimized to handle prompts like these.

* List my recent emails
* Show me unread messages in my inbox
* Get the details of a specific email
* List all my Gmail labels
* Show me details for a specific label
* List my email drafts
* Get the content of a specific draft
* List my email threads
* Show me the full thread for a conversation
* Get my Gmail profile information
* Send an email to someone
* Create a new email draft
* Archive a message by removing the INBOX label
* Mark a message as read
* Mark a message as unread
* Move a message to trash
* Create a new label
* Update a label name or settings
* Delete a label
* Search for messages matching a query
* Find emails from a specific sender
* Show me emails with attachments

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Gmail connector isn't currently able to handle prompts like these.

* Attach a file to an email
* Forward an email to someone
* Create a filter or rule
* Manage Gmail settings
* Access Google Calendar events
* Manage contacts

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-gmail
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_gmail import GmailConnector
from airbyte_agent_gmail.models import GmailAuthConfig

connector = GmailConnector(
    auth_config=GmailAuthConfig(
        access_token="<Your Google OAuth2 Access Token (optional, will be obtained via refresh)>",
        refresh_token="<Your Google OAuth2 Refresh Token>",
        client_id="<Your Google OAuth2 Client ID>",
        client_secret="<Your Google OAuth2 Client Secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GmailConnector.tool_utils
async def gmail_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/gmail/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_gmail import GmailConnector, AirbyteAuthConfig

connector = GmailConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GmailConnector.tool_utils
async def gmail_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/gmail/REFERENCE.md).

| Entity           | Actions                                                                                                                                                                                                                                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Profile          | [Get](/ai-agents/connectors/gmail/REFERENCE.md#profile-get)                                                                                                                                                                                                                                                                    |
| Messages         | [List](/ai-agents/connectors/gmail/REFERENCE.md#messages-list), [Get](/ai-agents/connectors/gmail/REFERENCE.md#messages-get), [Create](/ai-agents/connectors/gmail/REFERENCE.md#messages-create), [Update](/ai-agents/connectors/gmail/REFERENCE.md#messages-update)                                                           |
| Labels           | [List](/ai-agents/connectors/gmail/REFERENCE.md#labels-list), [Create](/ai-agents/connectors/gmail/REFERENCE.md#labels-create), [Get](/ai-agents/connectors/gmail/REFERENCE.md#labels-get), [Update](/ai-agents/connectors/gmail/REFERENCE.md#labels-update), [Delete](/ai-agents/connectors/gmail/REFERENCE.md#labels-delete) |
| Drafts           | [List](/ai-agents/connectors/gmail/REFERENCE.md#drafts-list), [Create](/ai-agents/connectors/gmail/REFERENCE.md#drafts-create), [Get](/ai-agents/connectors/gmail/REFERENCE.md#drafts-get), [Update](/ai-agents/connectors/gmail/REFERENCE.md#drafts-update), [Delete](/ai-agents/connectors/gmail/REFERENCE.md#drafts-delete) |
| Drafts Send      | [Create](/ai-agents/connectors/gmail/REFERENCE.md#drafts-send-create)                                                                                                                                                                                                                                                          |
| Threads          | [List](/ai-agents/connectors/gmail/REFERENCE.md#threads-list), [Get](/ai-agents/connectors/gmail/REFERENCE.md#threads-get)                                                                                                                                                                                                     |
| Messages Trash   | [Create](/ai-agents/connectors/gmail/REFERENCE.md#messages-trash-create)                                                                                                                                                                                                                                                       |
| Messages Untrash | [Create](/ai-agents/connectors/gmail/REFERENCE.md#messages-untrash-create)                                                                                                                                                                                                                                                     |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/gmail/AUTH.md).

### Gmail API docs[​](#gmail-api-docs "Direct link to Gmail API docs")

See the official [Gmail API reference](https://developers.google.com/gmail/api/reference/rest).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.17
* **Connector version:** 0.1.3
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/gmail/CHANGELOG.md)
