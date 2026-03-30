# Source: https://docs.airbyte.com/integrations/sources/shopify.md

# Source: https://docs.airbyte.com/ai-agents/connectors/shopify.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-shopify/latest/icon.svg)

# Shopify

Copy Page

The Shopify agent connector is a Python package that equips AI agents to interact with Shopify through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Shopify is an e-commerce platform that enables businesses to create online stores, manage products, process orders, and handle customer relationships. This connector provides access to Shopify Admin REST API for reading store data including customers, orders, products, inventory, and more.

## Example questions[​](#example-questions "Direct link to Example questions")

The Shopify connector is optimized to handle prompts like these.

* List all customers in my Shopify store
* Show me details for a recent customer
* What products do I have in my store?
* List all locations for my store
* Show me inventory levels for a recent location
* Show me all draft orders
* List all custom collections in my store
* Show me details for a recent order
* Show me product variants for a recent product
* Show me orders from the last 30 days
* Show me abandoned checkouts from this week
* What price rules are currently active?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Shopify connector isn't currently able to handle prompts like these.

* Create a new customer in Shopify
* Update product pricing
* Delete an order
* Process a refund
* Send shipping notification to customer
* Create a new discount code

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-shopify
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_shopify import ShopifyConnector
from airbyte_agent_shopify.models import ShopifyAuthConfig

connector = ShopifyConnector(
    auth_config=ShopifyAuthConfig(
        api_key="<Your Shopify Admin API access token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ShopifyConnector.tool_utils
async def shopify_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/shopify/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_shopify import ShopifyConnector, AirbyteAuthConfig

connector = ShopifyConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ShopifyConnector.tool_utils
async def shopify_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/shopify/REFERENCE.md).

| Entity                      | Actions                                                                                                                                              |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customers                   | [List](/ai-agents/connectors/shopify/REFERENCE.md#customers-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#customers-get)                   |
| Orders                      | [List](/ai-agents/connectors/shopify/REFERENCE.md#orders-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#orders-get)                         |
| Products                    | [List](/ai-agents/connectors/shopify/REFERENCE.md#products-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#products-get)                     |
| Product Variants            | [List](/ai-agents/connectors/shopify/REFERENCE.md#product-variants-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#product-variants-get)     |
| Product Images              | [List](/ai-agents/connectors/shopify/REFERENCE.md#product-images-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#product-images-get)         |
| Abandoned Checkouts         | [List](/ai-agents/connectors/shopify/REFERENCE.md#abandoned-checkouts-list)                                                                          |
| Locations                   | [List](/ai-agents/connectors/shopify/REFERENCE.md#locations-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#locations-get)                   |
| Inventory Levels            | [List](/ai-agents/connectors/shopify/REFERENCE.md#inventory-levels-list)                                                                             |
| Inventory Items             | [List](/ai-agents/connectors/shopify/REFERENCE.md#inventory-items-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#inventory-items-get)       |
| Shop                        | [Get](/ai-agents/connectors/shopify/REFERENCE.md#shop-get)                                                                                           |
| Price Rules                 | [List](/ai-agents/connectors/shopify/REFERENCE.md#price-rules-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#price-rules-get)               |
| Discount Codes              | [List](/ai-agents/connectors/shopify/REFERENCE.md#discount-codes-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#discount-codes-get)         |
| Custom Collections          | [List](/ai-agents/connectors/shopify/REFERENCE.md#custom-collections-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#custom-collections-get) |
| Smart Collections           | [List](/ai-agents/connectors/shopify/REFERENCE.md#smart-collections-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#smart-collections-get)   |
| Collects                    | [List](/ai-agents/connectors/shopify/REFERENCE.md#collects-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#collects-get)                     |
| Draft Orders                | [List](/ai-agents/connectors/shopify/REFERENCE.md#draft-orders-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#draft-orders-get)             |
| Fulfillments                | [List](/ai-agents/connectors/shopify/REFERENCE.md#fulfillments-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#fulfillments-get)             |
| Order Refunds               | [List](/ai-agents/connectors/shopify/REFERENCE.md#order-refunds-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#order-refunds-get)           |
| Transactions                | [List](/ai-agents/connectors/shopify/REFERENCE.md#transactions-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#transactions-get)             |
| Tender Transactions         | [List](/ai-agents/connectors/shopify/REFERENCE.md#tender-transactions-list)                                                                          |
| Countries                   | [List](/ai-agents/connectors/shopify/REFERENCE.md#countries-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#countries-get)                   |
| Metafield Shops             | [List](/ai-agents/connectors/shopify/REFERENCE.md#metafield-shops-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#metafield-shops-get)       |
| Metafield Customers         | [List](/ai-agents/connectors/shopify/REFERENCE.md#metafield-customers-list)                                                                          |
| Metafield Products          | [List](/ai-agents/connectors/shopify/REFERENCE.md#metafield-products-list)                                                                           |
| Metafield Orders            | [List](/ai-agents/connectors/shopify/REFERENCE.md#metafield-orders-list)                                                                             |
| Metafield Draft Orders      | [List](/ai-agents/connectors/shopify/REFERENCE.md#metafield-draft-orders-list)                                                                       |
| Metafield Locations         | [List](/ai-agents/connectors/shopify/REFERENCE.md#metafield-locations-list)                                                                          |
| Metafield Product Variants  | [List](/ai-agents/connectors/shopify/REFERENCE.md#metafield-product-variants-list)                                                                   |
| Metafield Smart Collections | [List](/ai-agents/connectors/shopify/REFERENCE.md#metafield-smart-collections-list)                                                                  |
| Metafield Product Images    | [List](/ai-agents/connectors/shopify/REFERENCE.md#metafield-product-images-list)                                                                     |
| Customer Address            | [List](/ai-agents/connectors/shopify/REFERENCE.md#customer-address-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#customer-address-get)     |
| Fulfillment Orders          | [List](/ai-agents/connectors/shopify/REFERENCE.md#fulfillment-orders-list), [Get](/ai-agents/connectors/shopify/REFERENCE.md#fulfillment-orders-get) |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/shopify/AUTH.md).

### Shopify API docs[​](#shopify-api-docs "Direct link to Shopify API docs")

See the official [Shopify API reference](https://shopify.dev/docs/api/admin-rest).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.67
* **Connector version:** 0.1.9
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/shopify/CHANGELOG.md)
