# Source: https://docs.airbyte.com/integrations/sources/linkedin-ads.md

# Source: https://docs.airbyte.com/ai-agents/connectors/linkedin-ads.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-linkedin-ads/latest/icon.svg)

# Linkedin-Ads

Copy Page

The Linkedin-Ads agent connector is a Python package that equips AI agents to interact with Linkedin-Ads through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the LinkedIn Ads Marketing API. Provides access to ad accounts, campaigns, campaign groups, creatives, conversions, and ad analytics data. Supports OAuth 2.0 and direct access token authentication. Use this connector to retrieve advertising performance metrics, manage campaign structures, and monitor creative assets across your LinkedIn advertising accounts.

## Example questions[​](#example-questions "Direct link to Example questions")

The Linkedin-Ads connector is optimized to handle prompts like these.

* List all my LinkedIn ad accounts
* Show me all campaigns in my ad account
* List all campaign groups
* Show me the creatives for my campaigns
* List all conversions configured for my ad accounts
* Show me account users for my LinkedIn ads accounts
* Which campaigns have the highest click-through rate?
* What is the total ad spend across all campaigns this month?
* Show me campaigns with status ACTIVE
* Which creatives have the most impressions?
* Compare campaign performance by cost type

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Linkedin-Ads connector isn't currently able to handle prompts like these.

* Create a new campaign
* Update campaign budgets
* Delete an ad creative
* Pause a campaign

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-linkedin-ads
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_linkedin_ads import LinkedinAdsConnector
from airbyte_agent_linkedin_ads.models import LinkedinAdsAuthConfig

connector = LinkedinAdsConnector(
    auth_config=LinkedinAdsAuthConfig(
        refresh_token="<OAuth 2.0 refresh token for automatic renewal>",
        client_id="<OAuth 2.0 application client ID>",
        client_secret="<OAuth 2.0 application client secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@LinkedinAdsConnector.tool_utils
async def linkedin_ads_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/linkedin-ads/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_linkedin_ads import LinkedinAdsConnector, AirbyteAuthConfig

connector = LinkedinAdsConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@LinkedinAdsConnector.tool_utils
async def linkedin_ads_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/linkedin-ads/REFERENCE.md).

| Entity                | Actions                                                                                                                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Accounts              | [List](/ai-agents/connectors/linkedin-ads/REFERENCE.md#accounts-list), [Get](/ai-agents/connectors/linkedin-ads/REFERENCE.md#accounts-get), [Search](/ai-agents/connectors/linkedin-ads/REFERENCE.md#accounts-search)                      |
| Account Users         | [List](/ai-agents/connectors/linkedin-ads/REFERENCE.md#account-users-list), [Search](/ai-agents/connectors/linkedin-ads/REFERENCE.md#account-users-search)                                                                                 |
| Campaigns             | [List](/ai-agents/connectors/linkedin-ads/REFERENCE.md#campaigns-list), [Get](/ai-agents/connectors/linkedin-ads/REFERENCE.md#campaigns-get), [Search](/ai-agents/connectors/linkedin-ads/REFERENCE.md#campaigns-search)                   |
| Campaign Groups       | [List](/ai-agents/connectors/linkedin-ads/REFERENCE.md#campaign-groups-list), [Get](/ai-agents/connectors/linkedin-ads/REFERENCE.md#campaign-groups-get), [Search](/ai-agents/connectors/linkedin-ads/REFERENCE.md#campaign-groups-search) |
| Creatives             | [List](/ai-agents/connectors/linkedin-ads/REFERENCE.md#creatives-list), [Get](/ai-agents/connectors/linkedin-ads/REFERENCE.md#creatives-get), [Search](/ai-agents/connectors/linkedin-ads/REFERENCE.md#creatives-search)                   |
| Conversions           | [List](/ai-agents/connectors/linkedin-ads/REFERENCE.md#conversions-list), [Get](/ai-agents/connectors/linkedin-ads/REFERENCE.md#conversions-get), [Search](/ai-agents/connectors/linkedin-ads/REFERENCE.md#conversions-search)             |
| Ad Campaign Analytics | [List](/ai-agents/connectors/linkedin-ads/REFERENCE.md#ad-campaign-analytics-list), [Search](/ai-agents/connectors/linkedin-ads/REFERENCE.md#ad-campaign-analytics-search)                                                                 |
| Ad Creative Analytics | [List](/ai-agents/connectors/linkedin-ads/REFERENCE.md#ad-creative-analytics-list), [Search](/ai-agents/connectors/linkedin-ads/REFERENCE.md#ad-creative-analytics-search)                                                                 |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/linkedin-ads/AUTH.md).

### Linkedin-Ads API docs[​](#linkedin-ads-api-docs "Direct link to Linkedin-Ads API docs")

See the official [Linkedin-Ads API reference](https://learn.microsoft.com/en-us/linkedin/marketing/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.2
* **Connector version:** 1.0.1
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/linkedin-ads/CHANGELOG.md)
