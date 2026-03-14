# Source: https://docs.airbyte.com/integrations/sources/amazon-ads.md

# Source: https://docs.airbyte.com/ai-agents/connectors/amazon-ads.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-amazon-ads/latest/icon.svg)

# Amazon-Ads

Copy Page

The Amazon-Ads agent connector is a Python package that equips AI agents to interact with Amazon-Ads through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Amazon Ads is Amazon's advertising platform that enables sellers and vendors to promote their products across Amazon's marketplace. This connector provides access to advertising profiles for managing and analyzing advertising campaigns across different marketplaces.

## Example questions[​](#example-questions "Direct link to Example questions")

The Amazon-Ads connector is optimized to handle prompts like these.

* List all my advertising profiles across marketplaces
* Show me the profiles for my seller accounts
* What marketplaces do I have advertising profiles in?
* List all portfolios for one of my profiles
* Show me all sponsored product campaigns
* What campaigns are currently enabled?
* Find campaigns with a specific targeting type

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Amazon-Ads connector isn't currently able to handle prompts like these.

* Create a new advertising campaign
* Update my campaign budget
* Delete an ad group
* Generate a performance report

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-amazon-ads
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_amazon_ads import AmazonAdsConnector
from airbyte_agent_amazon_ads.models import AmazonAdsAuthConfig

connector = AmazonAdsConnector(
    auth_config=AmazonAdsAuthConfig(
        client_id="<The client ID of your Amazon Ads API application>",
        client_secret="<The client secret of your Amazon Ads API application>",
        refresh_token="<The refresh token obtained from the OAuth authorization flow>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AmazonAdsConnector.tool_utils
async def amazon_ads_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/amazon-ads/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_amazon_ads import AmazonAdsConnector, AirbyteAuthConfig

connector = AmazonAdsConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AmazonAdsConnector.tool_utils
async def amazon_ads_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/amazon-ads/REFERENCE.md).

| Entity                      | Actions                                                                                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Profiles                    | [List](/ai-agents/connectors/amazon-ads/REFERENCE.md#profiles-list), [Get](/ai-agents/connectors/amazon-ads/REFERENCE.md#profiles-get), [Search](/ai-agents/connectors/amazon-ads/REFERENCE.md#profiles-search) |
| Portfolios                  | [List](/ai-agents/connectors/amazon-ads/REFERENCE.md#portfolios-list), [Get](/ai-agents/connectors/amazon-ads/REFERENCE.md#portfolios-get)                                                                      |
| Sponsored Product Campaigns | [List](/ai-agents/connectors/amazon-ads/REFERENCE.md#sponsored-product-campaigns-list), [Get](/ai-agents/connectors/amazon-ads/REFERENCE.md#sponsored-product-campaigns-get)                                    |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/amazon-ads/AUTH.md).

### Amazon-Ads API docs[​](#amazon-ads-api-docs "Direct link to Amazon-Ads API docs")

See the official [Amazon-Ads API reference](https://advertising.amazon.com/API/docs/en-us).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.64
* **Connector version:** 1.0.9
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/amazon-ads/CHANGELOG.md)
