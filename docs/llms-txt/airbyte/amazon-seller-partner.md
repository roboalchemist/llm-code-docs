# Source: https://docs.airbyte.com/integrations/sources/amazon-seller-partner.md

# Source: https://docs.airbyte.com/ai-agents/connectors/amazon-seller-partner.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-amazon-seller-partner/latest/icon.svg)

# Amazon-Seller-Partner

Copy Page

The Amazon-Seller-Partner agent connector is a Python package that equips AI agents to interact with Amazon-Seller-Partner through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the Amazon Selling Partner API (SP-API). Provides access to seller orders and order items, financial events and event groups, catalog item search and details, and report metadata. Supports OAuth 2.0 authentication via Login with Amazon (LWA) with automatic token refresh.

## Example questions[​](#example-questions "Direct link to Example questions")

The Amazon-Seller-Partner connector is optimized to handle prompts like these.

* List all recent orders
* Show me order items for a specific order
* List financial event groups
* Show recent financial events
* Search catalog items by keyword
* List recent reports
* What are my top-selling products by order volume?
* Show orders from the last 30 days with status Shipped
* Find financial events related to refunds
* Which orders have the highest total value?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Amazon-Seller-Partner connector isn't currently able to handle prompts like these.

* Create a new order
* Cancel an order
* Submit a new report request
* Update product listings

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-amazon-seller-partner
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_amazon_seller_partner import AmazonSellerPartnerConnector
from airbyte_agent_amazon_seller_partner.models import AmazonSellerPartnerAuthConfig

connector = AmazonSellerPartnerConnector(
    auth_config=AmazonSellerPartnerAuthConfig(
        lwa_app_id="<Your Login with Amazon Client ID.>",
        lwa_client_secret="<Your Login with Amazon Client Secret.>",
        refresh_token="<The Refresh Token obtained via the OAuth authorization flow.>",
        access_token="<Access token (optional if refresh_token is provided).>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AmazonSellerPartnerConnector.tool_utils
async def amazon_seller_partner_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/amazon-seller-partner/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_amazon_seller_partner import AmazonSellerPartnerConnector, AirbyteAuthConfig

connector = AmazonSellerPartnerConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AmazonSellerPartnerConnector.tool_utils
async def amazon_seller_partner_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md).

| Entity                      | Actions                                                                                                                                                                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Orders                      | [List](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#orders-list), [Get](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#orders-get), [Search](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#orders-search) |
| Order Items                 | [List](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#order-items-list), [Search](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#order-items-search)                                                                   |
| List Financial Event Groups | [List](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#list-financial-event-groups-list), [Search](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#list-financial-event-groups-search)                                   |
| List Financial Events       | [List](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#list-financial-events-list), [Search](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#list-financial-events-search)                                               |
| Catalog Items               | [List](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#catalog-items-list), [Get](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#catalog-items-get)                                                                     |
| Reports                     | [List](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#reports-list), [Get](/ai-agents/connectors/amazon-seller-partner/REFERENCE.md#reports-get)                                                                                 |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/amazon-seller-partner/AUTH.md).

### Amazon-Seller-Partner API docs[​](#amazon-seller-partner-api-docs "Direct link to Amazon-Seller-Partner API docs")

See the official [Amazon-Seller-Partner API reference](https://developer-docs.amazon.com/sp-api/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.3
* **Connector version:** 1.0.3
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/amazon-seller-partner/CHANGELOG.md)
