# Source: https://docs.airbyte.com/integrations/sources/chargebee.md

# Source: https://docs.airbyte.com/ai-agents/connectors/chargebee.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-chargebee/latest/icon.svg)

# Chargebee

Copy Page

The Chargebee agent connector is a Python package that equips AI agents to interact with Chargebee through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the Chargebee billing and subscription management API. Supports reading subscriptions, customers, invoices, credit notes, coupons, transactions, events, orders, items, item prices, and payment sources. Chargebee is a recurring billing platform that helps SaaS and subscription businesses manage the full subscription lifecycle.

## Example questions[​](#example-questions "Direct link to Example questions")

The Chargebee connector is optimized to handle prompts like these.

* List all active subscriptions
* Show me details for a specific customer
* List recent invoices
* Show me details for a specific subscription
* List all coupons
* List recent transactions
* List recent events
* Show me customers with the highest monthly recurring revenue
* Which subscriptions are set to cancel in the next 30 days?
* List all overdue invoices and their amounts
* Analyze subscription churn trends over the past quarter
* What are the most popular items by number of subscriptions?
* Show me total revenue breakdown by currency
* Identify customers with expiring payment sources
* Compare subscription plan distribution across item prices
* List all credit notes issued in the past month
* What is the average subscription lifetime for each plan?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Chargebee connector isn't currently able to handle prompts like these.

* Create a new subscription in Chargebee
* Update a customer's billing address
* Cancel a subscription
* Apply a coupon to a subscription
* Issue a refund for an invoice

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-chargebee
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_chargebee import ChargebeeConnector
from airbyte_agent_chargebee.models import ChargebeeAuthConfig

connector = ChargebeeConnector(
    auth_config=ChargebeeAuthConfig(
        api_key="<Your Chargebee API key (used as the HTTP Basic username)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ChargebeeConnector.tool_utils
async def chargebee_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/chargebee/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_chargebee import ChargebeeConnector, AirbyteAuthConfig

connector = ChargebeeConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ChargebeeConnector.tool_utils
async def chargebee_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/chargebee/REFERENCE.md).

| Entity         | Actions                                                                                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Customer       | [List](/ai-agents/connectors/chargebee/REFERENCE.md#customer-list), [Get](/ai-agents/connectors/chargebee/REFERENCE.md#customer-get), [Search](/ai-agents/connectors/chargebee/REFERENCE.md#customer-search)                   |
| Subscription   | [List](/ai-agents/connectors/chargebee/REFERENCE.md#subscription-list), [Get](/ai-agents/connectors/chargebee/REFERENCE.md#subscription-get), [Search](/ai-agents/connectors/chargebee/REFERENCE.md#subscription-search)       |
| Invoice        | [List](/ai-agents/connectors/chargebee/REFERENCE.md#invoice-list), [Get](/ai-agents/connectors/chargebee/REFERENCE.md#invoice-get), [Search](/ai-agents/connectors/chargebee/REFERENCE.md#invoice-search)                      |
| Credit Note    | [List](/ai-agents/connectors/chargebee/REFERENCE.md#credit-note-list), [Get](/ai-agents/connectors/chargebee/REFERENCE.md#credit-note-get), [Search](/ai-agents/connectors/chargebee/REFERENCE.md#credit-note-search)          |
| Coupon         | [List](/ai-agents/connectors/chargebee/REFERENCE.md#coupon-list), [Get](/ai-agents/connectors/chargebee/REFERENCE.md#coupon-get), [Search](/ai-agents/connectors/chargebee/REFERENCE.md#coupon-search)                         |
| Transaction    | [List](/ai-agents/connectors/chargebee/REFERENCE.md#transaction-list), [Get](/ai-agents/connectors/chargebee/REFERENCE.md#transaction-get), [Search](/ai-agents/connectors/chargebee/REFERENCE.md#transaction-search)          |
| Event          | [List](/ai-agents/connectors/chargebee/REFERENCE.md#event-list), [Get](/ai-agents/connectors/chargebee/REFERENCE.md#event-get), [Search](/ai-agents/connectors/chargebee/REFERENCE.md#event-search)                            |
| Order          | [List](/ai-agents/connectors/chargebee/REFERENCE.md#order-list), [Get](/ai-agents/connectors/chargebee/REFERENCE.md#order-get), [Search](/ai-agents/connectors/chargebee/REFERENCE.md#order-search)                            |
| Item           | [List](/ai-agents/connectors/chargebee/REFERENCE.md#item-list), [Get](/ai-agents/connectors/chargebee/REFERENCE.md#item-get), [Search](/ai-agents/connectors/chargebee/REFERENCE.md#item-search)                               |
| Item Price     | [List](/ai-agents/connectors/chargebee/REFERENCE.md#item-price-list), [Get](/ai-agents/connectors/chargebee/REFERENCE.md#item-price-get), [Search](/ai-agents/connectors/chargebee/REFERENCE.md#item-price-search)             |
| Payment Source | [List](/ai-agents/connectors/chargebee/REFERENCE.md#payment-source-list), [Get](/ai-agents/connectors/chargebee/REFERENCE.md#payment-source-get), [Search](/ai-agents/connectors/chargebee/REFERENCE.md#payment-source-search) |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/chargebee/AUTH.md).

### Chargebee API docs[​](#chargebee-api-docs "Direct link to Chargebee API docs")

See the official [Chargebee API reference](https://apidocs.chargebee.com/docs/api).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.2
* **Connector version:** 1.0.1
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/chargebee/CHANGELOG.md)
