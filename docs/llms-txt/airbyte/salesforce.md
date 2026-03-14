# Source: https://docs.airbyte.com/integrations/sources/salesforce.md

# Source: https://docs.airbyte.com/ai-agents/connectors/salesforce.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-salesforce/latest/icon.svg)

# Salesforce

Copy Page

The Salesforce agent connector is a Python package that equips AI agents to interact with Salesforce through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Salesforce is a cloud-based CRM platform that helps businesses manage customer relationships, sales pipelines, and business operations. This connector provides access to accounts, contacts, leads, opportunities, tasks, events, campaigns, cases, notes, and attachments for sales analytics and customer relationship management.

## Example questions[​](#example-questions "Direct link to Example questions")

The Salesforce connector is optimized to handle prompts like these.

* List recent contacts in my Salesforce account
* List open cases in my Salesforce account
* Show me the notes and attachments for a recent account
* Show me my top 5 opportunities this month
* List all contacts from {company} in the last quarter
* Search for leads in the technology sector with revenue over $10M
* What trends can you identify in my recent sales pipeline?
* Summarize the open cases for my key accounts
* Find upcoming events related to my most important opportunities
* Analyze the performance of my recent marketing campaigns
* Identify the highest value opportunities I'm currently tracking

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Salesforce connector isn't currently able to handle prompts like these.

* Create a new lead for {person}
* Update the status of my sales opportunity
* Schedule a follow-up meeting with {customer}
* Delete this old contact record
* Send an email to all contacts in this campaign

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-salesforce
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_salesforce import SalesforceConnector
from airbyte_agent_salesforce.models import SalesforceAuthConfig

connector = SalesforceConnector(
    auth_config=SalesforceAuthConfig(
        refresh_token="<OAuth refresh token for automatic token renewal>",
        client_id="<Connected App Consumer Key>",
        client_secret="<Connected App Consumer Secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SalesforceConnector.tool_utils
async def salesforce_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/salesforce/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_salesforce import SalesforceConnector, AirbyteAuthConfig

connector = SalesforceConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SalesforceConnector.tool_utils
async def salesforce_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/salesforce/REFERENCE.md).

| Entity           | Actions                                                                                                                                                                                                                                                                                                              |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sobjects         | [List](/ai-agents/connectors/salesforce/REFERENCE.md#sobjects-list)                                                                                                                                                                                                                                                  |
| Accounts         | [List](/ai-agents/connectors/salesforce/REFERENCE.md#accounts-list), [Get](/ai-agents/connectors/salesforce/REFERENCE.md#accounts-get), [API Search](/ai-agents/connectors/salesforce/REFERENCE.md#accounts-api_search), [Search](/ai-agents/connectors/salesforce/REFERENCE.md#accounts-search)                     |
| Contacts         | [List](/ai-agents/connectors/salesforce/REFERENCE.md#contacts-list), [Get](/ai-agents/connectors/salesforce/REFERENCE.md#contacts-get), [API Search](/ai-agents/connectors/salesforce/REFERENCE.md#contacts-api_search), [Search](/ai-agents/connectors/salesforce/REFERENCE.md#contacts-search)                     |
| Leads            | [List](/ai-agents/connectors/salesforce/REFERENCE.md#leads-list), [Get](/ai-agents/connectors/salesforce/REFERENCE.md#leads-get), [API Search](/ai-agents/connectors/salesforce/REFERENCE.md#leads-api_search), [Search](/ai-agents/connectors/salesforce/REFERENCE.md#leads-search)                                 |
| Opportunities    | [List](/ai-agents/connectors/salesforce/REFERENCE.md#opportunities-list), [Get](/ai-agents/connectors/salesforce/REFERENCE.md#opportunities-get), [API Search](/ai-agents/connectors/salesforce/REFERENCE.md#opportunities-api_search), [Search](/ai-agents/connectors/salesforce/REFERENCE.md#opportunities-search) |
| Tasks            | [List](/ai-agents/connectors/salesforce/REFERENCE.md#tasks-list), [Get](/ai-agents/connectors/salesforce/REFERENCE.md#tasks-get), [API Search](/ai-agents/connectors/salesforce/REFERENCE.md#tasks-api_search), [Search](/ai-agents/connectors/salesforce/REFERENCE.md#tasks-search)                                 |
| Events           | [List](/ai-agents/connectors/salesforce/REFERENCE.md#events-list), [Get](/ai-agents/connectors/salesforce/REFERENCE.md#events-get), [API Search](/ai-agents/connectors/salesforce/REFERENCE.md#events-api_search)                                                                                                    |
| Campaigns        | [List](/ai-agents/connectors/salesforce/REFERENCE.md#campaigns-list), [Get](/ai-agents/connectors/salesforce/REFERENCE.md#campaigns-get), [API Search](/ai-agents/connectors/salesforce/REFERENCE.md#campaigns-api_search)                                                                                           |
| Cases            | [List](/ai-agents/connectors/salesforce/REFERENCE.md#cases-list), [Get](/ai-agents/connectors/salesforce/REFERENCE.md#cases-get), [API Search](/ai-agents/connectors/salesforce/REFERENCE.md#cases-api_search)                                                                                                       |
| Notes            | [List](/ai-agents/connectors/salesforce/REFERENCE.md#notes-list), [Get](/ai-agents/connectors/salesforce/REFERENCE.md#notes-get), [API Search](/ai-agents/connectors/salesforce/REFERENCE.md#notes-api_search)                                                                                                       |
| Content Versions | [List](/ai-agents/connectors/salesforce/REFERENCE.md#content-versions-list), [Get](/ai-agents/connectors/salesforce/REFERENCE.md#content-versions-get), [Download](/ai-agents/connectors/salesforce/REFERENCE.md#content-versions-download)                                                                          |
| Attachments      | [List](/ai-agents/connectors/salesforce/REFERENCE.md#attachments-list), [Get](/ai-agents/connectors/salesforce/REFERENCE.md#attachments-get), [Download](/ai-agents/connectors/salesforce/REFERENCE.md#attachments-download)                                                                                         |
| Query            | [List](/ai-agents/connectors/salesforce/REFERENCE.md#query-list)                                                                                                                                                                                                                                                     |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/salesforce/AUTH.md).

### Salesforce API docs[​](#salesforce-api-docs "Direct link to Salesforce API docs")

See the official [Salesforce API reference](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.109
* **Connector version:** 1.0.14
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/salesforce/CHANGELOG.md)
