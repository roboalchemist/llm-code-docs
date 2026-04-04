# Source: https://docs.airbyte.com/integrations/sources/stripe.md

# Source: https://docs.airbyte.com/ai-agents/connectors/stripe.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-stripe/latest/icon.svg)

# Stripe

Copy Page

The Stripe agent connector is a Python package that equips AI agents to interact with Stripe through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Stripe is a payment processing platform that enables businesses to accept payments, manage subscriptions, and handle financial transactions. This connector provides access to customers for payment analytics and customer management.

## Example questions[​](#example-questions "Direct link to Example questions")

The Stripe connector is optimized to handle prompts like these.

* List customers created in the last 7 days
* Show me details for a recent customer
* List recent charges
* Show me details for a recent charge
* List recent invoices
* List active subscriptions
* Show me my top 10 customers by total revenue this month
* List all customers who have spent over $5,000 in the last quarter
* Analyze payment trends for my Stripe customers
* Identify which customers have the most consistent subscription payments
* Give me insights into my customer retention rates
* Summarize the payment history for {customer}
* Compare customer spending patterns from last month to this month
* Show me details about my highest-value Stripe customers
* What are the key financial insights from my customer base?
* Break down my customers by their average transaction value

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Stripe connector isn't currently able to handle prompts like these.

* Create a new customer profile in Stripe
* Update the billing information for {customer}
* Delete a customer record
* Send a payment reminder to {customer}
* Schedule an automatic invoice for {company}

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-stripe
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_stripe import StripeConnector
from airbyte_agent_stripe.models import StripeAuthConfig

connector = StripeConnector(
    auth_config=StripeAuthConfig(
        api_key="<Your Stripe API Key (starts with sk_test_ or sk_live_)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@StripeConnector.tool_utils
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/stripe/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_stripe import StripeConnector, AirbyteAuthConfig

connector = StripeConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@StripeConnector.tool_utils
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/stripe/REFERENCE.md).

| Entity               | Actions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Customers            | [List](/ai-agents/connectors/stripe/REFERENCE.md#customers-list), [Create](/ai-agents/connectors/stripe/REFERENCE.md#customers-create), [Get](/ai-agents/connectors/stripe/REFERENCE.md#customers-get), [Update](/ai-agents/connectors/stripe/REFERENCE.md#customers-update), [Delete](/ai-agents/connectors/stripe/REFERENCE.md#customers-delete), [API Search](/ai-agents/connectors/stripe/REFERENCE.md#customers-api_search), [Search](/ai-agents/connectors/stripe/REFERENCE.md#customers-search) |
| Invoices             | [List](/ai-agents/connectors/stripe/REFERENCE.md#invoices-list), [Get](/ai-agents/connectors/stripe/REFERENCE.md#invoices-get), [API Search](/ai-agents/connectors/stripe/REFERENCE.md#invoices-api_search), [Search](/ai-agents/connectors/stripe/REFERENCE.md#invoices-search)                                                                                                                                                                                                                       |
| Charges              | [List](/ai-agents/connectors/stripe/REFERENCE.md#charges-list), [Get](/ai-agents/connectors/stripe/REFERENCE.md#charges-get), [API Search](/ai-agents/connectors/stripe/REFERENCE.md#charges-api_search), [Search](/ai-agents/connectors/stripe/REFERENCE.md#charges-search)                                                                                                                                                                                                                           |
| Subscriptions        | [List](/ai-agents/connectors/stripe/REFERENCE.md#subscriptions-list), [Get](/ai-agents/connectors/stripe/REFERENCE.md#subscriptions-get), [API Search](/ai-agents/connectors/stripe/REFERENCE.md#subscriptions-api_search), [Search](/ai-agents/connectors/stripe/REFERENCE.md#subscriptions-search)                                                                                                                                                                                                   |
| Refunds              | [List](/ai-agents/connectors/stripe/REFERENCE.md#refunds-list), [Create](/ai-agents/connectors/stripe/REFERENCE.md#refunds-create), [Get](/ai-agents/connectors/stripe/REFERENCE.md#refunds-get), [Search](/ai-agents/connectors/stripe/REFERENCE.md#refunds-search)                                                                                                                                                                                                                                   |
| Products             | [List](/ai-agents/connectors/stripe/REFERENCE.md#products-list), [Create](/ai-agents/connectors/stripe/REFERENCE.md#products-create), [Get](/ai-agents/connectors/stripe/REFERENCE.md#products-get), [Update](/ai-agents/connectors/stripe/REFERENCE.md#products-update), [Delete](/ai-agents/connectors/stripe/REFERENCE.md#products-delete), [API Search](/ai-agents/connectors/stripe/REFERENCE.md#products-api_search)                                                                             |
| Balance              | [Get](/ai-agents/connectors/stripe/REFERENCE.md#balance-get)                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Balance Transactions | [List](/ai-agents/connectors/stripe/REFERENCE.md#balance-transactions-list), [Get](/ai-agents/connectors/stripe/REFERENCE.md#balance-transactions-get)                                                                                                                                                                                                                                                                                                                                                 |
| Payment Intents      | [List](/ai-agents/connectors/stripe/REFERENCE.md#payment-intents-list), [Get](/ai-agents/connectors/stripe/REFERENCE.md#payment-intents-get), [API Search](/ai-agents/connectors/stripe/REFERENCE.md#payment-intents-api_search)                                                                                                                                                                                                                                                                       |
| Disputes             | [List](/ai-agents/connectors/stripe/REFERENCE.md#disputes-list), [Get](/ai-agents/connectors/stripe/REFERENCE.md#disputes-get)                                                                                                                                                                                                                                                                                                                                                                         |
| Payouts              | [List](/ai-agents/connectors/stripe/REFERENCE.md#payouts-list), [Get](/ai-agents/connectors/stripe/REFERENCE.md#payouts-get)                                                                                                                                                                                                                                                                                                                                                                           |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/stripe/AUTH.md).

### Stripe API docs[​](#stripe-api-docs "Direct link to Stripe API docs")

See the official [Stripe API reference](https://docs.stripe.com/api).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.5.114
* **Connector version:** 0.1.10
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/stripe/CHANGELOG.md)
