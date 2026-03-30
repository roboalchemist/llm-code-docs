# Source: https://docs.airbyte.com/integrations/sources/woocommerce.md

# Source: https://docs.airbyte.com/ai-agents/connectors/woocommerce.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-woocommerce/latest/icon.svg)

# Woocommerce

Copy Page

The Woocommerce agent connector is a Python package that equips AI agents to interact with Woocommerce through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the WooCommerce REST API (v3). Provides read access to a WooCommerce store's customers, orders, products, coupons, product categories, tags, reviews, attributes, variations, order notes, refunds, payment gateways, shipping methods, shipping zones, tax rates, and tax classes. Requires a WooCommerce store URL and REST API consumer key / consumer secret for authentication.

## Example questions[​](#example-questions "Direct link to Example questions")

The Woocommerce connector is optimized to handle prompts like these.

* List all customers in WooCommerce
* Show me all orders
* List all products
* Show me all coupons
* List all product categories
* Show me the product reviews
* List all shipping zones
* Show me the tax rates
* List all payment gateways
* Find orders placed this month
* What are the top-selling products?
* Show me customers who have made purchases
* Find all coupons expiring this year
* What orders are still processing?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Woocommerce connector isn't currently able to handle prompts like these.

* Create a new product
* Update an order status
* Delete a customer
* Apply a coupon to an order
* Process a refund

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-woocommerce
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_woocommerce import WoocommerceConnector
from airbyte_agent_woocommerce.models import WoocommerceAuthConfig

connector = WoocommerceConnector(
    auth_config=WoocommerceAuthConfig(
        api_key="<WooCommerce REST API consumer key (starts with ck_)>",
        api_secret="<WooCommerce REST API consumer secret (starts with cs_)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@WoocommerceConnector.tool_utils
async def woocommerce_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/woocommerce/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_woocommerce import WoocommerceConnector, AirbyteAuthConfig

connector = WoocommerceConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@WoocommerceConnector.tool_utils
async def woocommerce_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/woocommerce/REFERENCE.md).

| Entity             | Actions                                                                                                                                                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Customers          | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#customers-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#customers-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#customers-search)                            |
| Orders             | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#orders-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#orders-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#orders-search)                                     |
| Products           | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#products-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#products-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#products-search)                               |
| Coupons            | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#coupons-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#coupons-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#coupons-search)                                  |
| Product Categories | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#product-categories-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#product-categories-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#product-categories-search) |
| Product Tags       | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#product-tags-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#product-tags-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#product-tags-search)                   |
| Product Reviews    | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#product-reviews-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#product-reviews-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#product-reviews-search)          |
| Product Attributes | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#product-attributes-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#product-attributes-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#product-attributes-search) |
| Product Variations | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#product-variations-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#product-variations-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#product-variations-search) |
| Order Notes        | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#order-notes-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#order-notes-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#order-notes-search)                      |
| Refunds            | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#refunds-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#refunds-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#refunds-search)                                  |
| Payment Gateways   | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#payment-gateways-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#payment-gateways-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#payment-gateways-search)       |
| Shipping Methods   | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#shipping-methods-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#shipping-methods-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#shipping-methods-search)       |
| Shipping Zones     | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#shipping-zones-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#shipping-zones-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#shipping-zones-search)             |
| Tax Rates          | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#tax-rates-list), [Get](/ai-agents/connectors/woocommerce/REFERENCE.md#tax-rates-get), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#tax-rates-search)                            |
| Tax Classes        | [List](/ai-agents/connectors/woocommerce/REFERENCE.md#tax-classes-list), [Search](/ai-agents/connectors/woocommerce/REFERENCE.md#tax-classes-search)                                                                                             |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/woocommerce/AUTH.md).

### Woocommerce API docs[​](#woocommerce-api-docs "Direct link to Woocommerce API docs")

See the official [Woocommerce API reference](https://woocommerce.github.io/woocommerce-rest-api-docs/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.2
* **Connector version:** 1.0.1
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/woocommerce/CHANGELOG.md)
