# Source: https://docs.airbyte.com/integrations/sources/mailchimp.md

# Source: https://docs.airbyte.com/ai-agents/connectors/mailchimp.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-mailchimp/latest/icon.svg)

# Mailchimp

Copy Page

The Mailchimp agent connector is a Python package that equips AI agents to interact with Mailchimp through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Mailchimp is an email marketing platform that enables businesses to create, send, and analyze email campaigns, manage subscriber lists, and automate marketing workflows. This connector provides read access to campaigns, lists, reports, email activity, automations, and more for marketing analytics and audience management.

## Example questions[​](#example-questions "Direct link to Example questions")

The Mailchimp connector is optimized to handle prompts like these.

* List all subscribers in my main mailing list
* List all automation workflows in my account
* Show me all segments for my primary audience
* List all interest categories for my primary audience
* Show me email activity for a recent campaign
* Show me the performance report for a recent campaign
* Show me all my email campaigns from the last month
* What are the open rates for my recent campaigns?
* Who unsubscribed from list {list\_id} this week?
* What tags are applied to my subscribers?
* How many subscribers do I have in each list?
* What are my top performing campaigns by click rate?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Mailchimp connector isn't currently able to handle prompts like these.

* Create a new email campaign
* Add a subscriber to my list
* Delete a campaign
* Update subscriber information
* Send a campaign now
* Create a new automation workflow

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-mailchimp
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_mailchimp import MailchimpConnector
from airbyte_agent_mailchimp.models import MailchimpAuthConfig

connector = MailchimpConnector(
    auth_config=MailchimpAuthConfig(
        api_key="<Your Mailchimp API key. You can find this in your Mailchimp account under Account > Extras > API keys.>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@MailchimpConnector.tool_utils
async def mailchimp_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/mailchimp/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_mailchimp import MailchimpConnector, AirbyteAuthConfig

connector = MailchimpConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@MailchimpConnector.tool_utils
async def mailchimp_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/mailchimp/REFERENCE.md).

| Entity              | Actions                                                                                                                                                                                                         |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Campaigns           | [List](/ai-agents/connectors/mailchimp/REFERENCE.md#campaigns-list), [Get](/ai-agents/connectors/mailchimp/REFERENCE.md#campaigns-get), [Search](/ai-agents/connectors/mailchimp/REFERENCE.md#campaigns-search) |
| Lists               | [List](/ai-agents/connectors/mailchimp/REFERENCE.md#lists-list), [Get](/ai-agents/connectors/mailchimp/REFERENCE.md#lists-get), [Search](/ai-agents/connectors/mailchimp/REFERENCE.md#lists-search)             |
| List Members        | [List](/ai-agents/connectors/mailchimp/REFERENCE.md#list-members-list), [Get](/ai-agents/connectors/mailchimp/REFERENCE.md#list-members-get)                                                                    |
| Reports             | [List](/ai-agents/connectors/mailchimp/REFERENCE.md#reports-list), [Get](/ai-agents/connectors/mailchimp/REFERENCE.md#reports-get), [Search](/ai-agents/connectors/mailchimp/REFERENCE.md#reports-search)       |
| Email Activity      | [List](/ai-agents/connectors/mailchimp/REFERENCE.md#email-activity-list), [Search](/ai-agents/connectors/mailchimp/REFERENCE.md#email-activity-search)                                                          |
| Automations         | [List](/ai-agents/connectors/mailchimp/REFERENCE.md#automations-list)                                                                                                                                           |
| Tags                | [List](/ai-agents/connectors/mailchimp/REFERENCE.md#tags-list)                                                                                                                                                  |
| Interest Categories | [List](/ai-agents/connectors/mailchimp/REFERENCE.md#interest-categories-list), [Get](/ai-agents/connectors/mailchimp/REFERENCE.md#interest-categories-get)                                                      |
| Interests           | [List](/ai-agents/connectors/mailchimp/REFERENCE.md#interests-list), [Get](/ai-agents/connectors/mailchimp/REFERENCE.md#interests-get)                                                                          |
| Segments            | [List](/ai-agents/connectors/mailchimp/REFERENCE.md#segments-list), [Get](/ai-agents/connectors/mailchimp/REFERENCE.md#segments-get)                                                                            |
| Segment Members     | [List](/ai-agents/connectors/mailchimp/REFERENCE.md#segment-members-list)                                                                                                                                       |
| Unsubscribes        | [List](/ai-agents/connectors/mailchimp/REFERENCE.md#unsubscribes-list)                                                                                                                                          |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/mailchimp/AUTH.md).

### Mailchimp API docs[​](#mailchimp-api-docs "Direct link to Mailchimp API docs")

See the official [Mailchimp API reference](https://mailchimp.com/developer/marketing/api/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.71
* **Connector version:** 1.0.8
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/mailchimp/CHANGELOG.md)
