# Source: https://docs.airbyte.com/integrations/sources/facebook-marketing.md

# Source: https://docs.airbyte.com/ai-agents/connectors/facebook-marketing.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-facebook-marketing/latest/icon.svg)

# Facebook-Marketing

Copy Page

The Facebook-Marketing agent connector is a Python package that equips AI agents to interact with Facebook-Marketing through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Facebook Marketing API connector for managing ad campaigns, ad sets, ads, creatives, and accessing performance insights, pixel configuration, and event quality data. This connector provides read access to Facebook Ads Manager data for analytics and reporting purposes.

## Example questions[​](#example-questions "Direct link to Example questions")

The Facebook-Marketing connector is optimized to handle prompts like these.

* List all active campaigns in my ad account
* What ads are currently running in a recent campaign?
* List all ad creatives in my account
* What is the status of my campaigns?
* List all custom conversion events in my account
* Show me all ad images in my account
* What videos are available in my ad account?
* Create a new campaign called 'Summer Sale 2026' with traffic objective
* Pause my most recent campaign
* Create a new ad set with a $50 daily budget in my latest campaign
* Update the daily budget of my top performing ad set to $100
* Rename my most recent ad set to 'Holiday Promo'
* Create a new ad in my latest ad set
* Pause all ads in my most recent ad set
* List all pixels in my ad account
* Show me the event stats for my pixel
* What events is my Facebook pixel tracking?
* Search the Ad Library for political ads in the US
* Find ads about climate change in the Ad Library
* Show me Ad Library ads from a specific Facebook page
* Show me the ad sets with the highest daily budget
* Show me the performance insights for the last 7 days
* Which campaigns have the most spend this month?
* Show me ads with the highest click-through rate

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Facebook-Marketing connector isn't currently able to handle prompts like these.

* Delete this ad creative
* Delete this campaign
* Delete this ad set
* Delete this ad

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-facebook-marketing
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_facebook_marketing import FacebookMarketingConnector
from airbyte_agent_facebook_marketing.models import FacebookMarketingServiceAccountKeyAuthenticationAuthConfig

connector = FacebookMarketingConnector(
    auth_config=FacebookMarketingServiceAccountKeyAuthenticationAuthConfig(
        account_key="<Facebook long-lived access token for Service Account authentication>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@FacebookMarketingConnector.tool_utils
async def facebook_marketing_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/facebook-marketing/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_facebook_marketing import FacebookMarketingConnector, AirbyteAuthConfig

connector = FacebookMarketingConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@FacebookMarketingConnector.tool_utils
async def facebook_marketing_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/facebook-marketing/REFERENCE.md).

| Entity             | Actions                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Current User       | [Get](/ai-agents/connectors/facebook-marketing/REFERENCE.md#current-user-get)                                                                                                                                                                                                                                                                                                                                  |
| Ad Accounts        | [List](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ad-accounts-list), [Search](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ad-accounts-search)                                                                                                                                                                                                                                             |
| Campaigns          | [List](/ai-agents/connectors/facebook-marketing/REFERENCE.md#campaigns-list), [Create](/ai-agents/connectors/facebook-marketing/REFERENCE.md#campaigns-create), [Get](/ai-agents/connectors/facebook-marketing/REFERENCE.md#campaigns-get), [Update](/ai-agents/connectors/facebook-marketing/REFERENCE.md#campaigns-update), [Search](/ai-agents/connectors/facebook-marketing/REFERENCE.md#campaigns-search) |
| Ad Sets            | [List](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ad-sets-list), [Create](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ad-sets-create), [Get](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ad-sets-get), [Update](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ad-sets-update), [Search](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ad-sets-search)           |
| Ads                | [List](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ads-list), [Create](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ads-create), [Get](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ads-get), [Update](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ads-update), [Search](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ads-search)                               |
| Ad Creatives       | [List](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ad-creatives-list), [Search](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ad-creatives-search)                                                                                                                                                                                                                                           |
| Ads Insights       | [List](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ads-insights-list), [Search](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ads-insights-search)                                                                                                                                                                                                                                           |
| Ad Account         | [Get](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ad-account-get), [Search](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ad-account-search)                                                                                                                                                                                                                                                 |
| Custom Conversions | [List](/ai-agents/connectors/facebook-marketing/REFERENCE.md#custom-conversions-list), [Search](/ai-agents/connectors/facebook-marketing/REFERENCE.md#custom-conversions-search)                                                                                                                                                                                                                               |
| Images             | [List](/ai-agents/connectors/facebook-marketing/REFERENCE.md#images-list), [Search](/ai-agents/connectors/facebook-marketing/REFERENCE.md#images-search)                                                                                                                                                                                                                                                       |
| Videos             | [List](/ai-agents/connectors/facebook-marketing/REFERENCE.md#videos-list), [Search](/ai-agents/connectors/facebook-marketing/REFERENCE.md#videos-search)                                                                                                                                                                                                                                                       |
| Pixels             | [List](/ai-agents/connectors/facebook-marketing/REFERENCE.md#pixels-list), [Get](/ai-agents/connectors/facebook-marketing/REFERENCE.md#pixels-get)                                                                                                                                                                                                                                                             |
| Pixel Stats        | [List](/ai-agents/connectors/facebook-marketing/REFERENCE.md#pixel-stats-list)                                                                                                                                                                                                                                                                                                                                 |
| Ad Library         | [List](/ai-agents/connectors/facebook-marketing/REFERENCE.md#ad-library-list)                                                                                                                                                                                                                                                                                                                                  |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/facebook-marketing/AUTH.md).

### Facebook-Marketing API docs[​](#facebook-marketing-api-docs "Direct link to Facebook-Marketing API docs")

See the official [Facebook-Marketing API reference](https://developers.facebook.com/docs/marketing-api/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.53
* **Connector version:** 1.0.19
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/facebook-marketing/CHANGELOG.md)
