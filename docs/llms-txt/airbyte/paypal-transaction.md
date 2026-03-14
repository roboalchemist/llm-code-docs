# Source: https://docs.airbyte.com/integrations/sources/paypal-transaction.md

# Source: https://docs.airbyte.com/ai-agents/connectors/paypal-transaction.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-paypal-transaction/latest/icon.svg)

# Paypal-Transaction

Copy Page

The Paypal-Transaction agent connector is a Python package that equips AI agents to interact with Paypal-Transaction through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the PayPal Transaction Search API. Provides access to transaction history, account balances, payments, disputes, catalog products, and invoices for a PayPal account. Uses OAuth2 client credentials for authentication.

## Example questions[​](#example-questions "Direct link to Example questions")

The Paypal-Transaction connector is optimized to handle prompts like these.

* List all balances for my PayPal account
* Show recent transactions from the last 7 days
* List all catalog products
* Show details for a specific product
* List all disputes
* Show recent payments
* What transactions had the highest amounts last month?
* Find all declined transactions
* Show disputes grouped by status
* What is the total balance across all currencies?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Paypal-Transaction connector isn't currently able to handle prompts like these.

* Create a new payment
* Refund a transaction
* Delete a dispute
* Update product details

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-paypal-transaction
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_paypal_transaction import PaypalTransactionConnector
from airbyte_agent_paypal_transaction.models import PaypalTransactionAuthConfig

connector = PaypalTransactionConnector(
    auth_config=PaypalTransactionAuthConfig(
        client_id="<The Client ID of your PayPal developer application.>",
        client_secret="<The Client Secret of your PayPal developer application.>",
        access_token="<OAuth2 access token obtained via client credentials grant. Use the PayPal token endpoint with your client_id and client_secret to obtain this.
>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@PaypalTransactionConnector.tool_utils
async def paypal_transaction_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/paypal-transaction/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_paypal_transaction import PaypalTransactionConnector, AirbyteAuthConfig

connector = PaypalTransactionConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@PaypalTransactionConnector.tool_utils
async def paypal_transaction_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/paypal-transaction/REFERENCE.md).

| Entity               | Actions                                                                                                                                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Balances             | [List](/ai-agents/connectors/paypal-transaction/REFERENCE.md#balances-list), [Search](/ai-agents/connectors/paypal-transaction/REFERENCE.md#balances-search)                       |
| Transactions         | [List](/ai-agents/connectors/paypal-transaction/REFERENCE.md#transactions-list), [Search](/ai-agents/connectors/paypal-transaction/REFERENCE.md#transactions-search)               |
| List Payments        | [List](/ai-agents/connectors/paypal-transaction/REFERENCE.md#list-payments-list), [Search](/ai-agents/connectors/paypal-transaction/REFERENCE.md#list-payments-search)             |
| List Disputes        | [List](/ai-agents/connectors/paypal-transaction/REFERENCE.md#list-disputes-list), [Search](/ai-agents/connectors/paypal-transaction/REFERENCE.md#list-disputes-search)             |
| List Products        | [List](/ai-agents/connectors/paypal-transaction/REFERENCE.md#list-products-list), [Search](/ai-agents/connectors/paypal-transaction/REFERENCE.md#list-products-search)             |
| Show Product Details | [Get](/ai-agents/connectors/paypal-transaction/REFERENCE.md#show-product-details-get), [Search](/ai-agents/connectors/paypal-transaction/REFERENCE.md#show-product-details-search) |
| Search Invoices      | [List](/ai-agents/connectors/paypal-transaction/REFERENCE.md#search-invoices-list), [Search](/ai-agents/connectors/paypal-transaction/REFERENCE.md#search-invoices-search)         |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/paypal-transaction/AUTH.md).

### Paypal-Transaction API docs[​](#paypal-transaction-api-docs "Direct link to Paypal-Transaction API docs")

See the official [Paypal-Transaction API reference](https://developer.paypal.com/docs/api/transaction-search/v1/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.1
* **Connector version:** 1.0.1
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/paypal-transaction/CHANGELOG.md)
