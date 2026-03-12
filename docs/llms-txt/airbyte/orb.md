# Source: https://docs.airbyte.com/integrations/sources/orb.md

# Source: https://docs.airbyte.com/ai-agents/connectors/orb.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-orb/latest/icon.svg)

# Orb

Copy Page

The Orb agent connector is a Python package that equips AI agents to interact with Orb through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Orb is a usage-based billing platform that enables businesses to implement flexible pricing models, track customer usage, and manage subscriptions. This connector provides access to customers, subscriptions, plans, and invoices for billing analytics and customer management.

## Example questions[​](#example-questions "Direct link to Example questions")

The Orb connector is optimized to handle prompts like these.

* Show me all my customers in Orb
* List all active subscriptions
* What plans are available?
* Show me recent invoices
* Show me details for a recent customer
* What is the status of a recent subscription?
* Show me the pricing details for a plan
* Confirm the Stripe ID linked to a customer
* What is the payment provider ID for a customer?
* List all invoices for a specific customer
* List all subscriptions for customer XYZ
* Show all active subscriptions for a specific customer
* What subscriptions does customer {external\_customer\_id} have?
* Pull all invoices from the last month
* Show invoices created after {date}
* List all paid invoices for customer {customer\_id}
* What invoices are in draft status?
* Show all issued invoices for subscription {subscription\_id}

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Orb connector isn't currently able to handle prompts like these.

* Create a new customer in Orb
* Update subscription details
* Delete a customer record
* Send an invoice to a customer
* Filter subscriptions by plan name (must filter client-side after listing)
* Pull customers billed for specific products (must examine invoice line\_items client-side)

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-orb
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_orb import OrbConnector
from airbyte_agent_orb.models import OrbAuthConfig

connector = OrbConnector(
    auth_config=OrbAuthConfig(
        api_key="<Your Orb API key>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@OrbConnector.tool_utils
async def orb_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/orb/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_orb import OrbConnector, AirbyteAuthConfig

connector = OrbConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@OrbConnector.tool_utils
async def orb_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/orb/REFERENCE.md).

| Entity        | Actions                                                                                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customers     | [List](/ai-agents/connectors/orb/REFERENCE.md#customers-list), [Get](/ai-agents/connectors/orb/REFERENCE.md#customers-get), [Search](/ai-agents/connectors/orb/REFERENCE.md#customers-search)             |
| Subscriptions | [List](/ai-agents/connectors/orb/REFERENCE.md#subscriptions-list), [Get](/ai-agents/connectors/orb/REFERENCE.md#subscriptions-get), [Search](/ai-agents/connectors/orb/REFERENCE.md#subscriptions-search) |
| Plans         | [List](/ai-agents/connectors/orb/REFERENCE.md#plans-list), [Get](/ai-agents/connectors/orb/REFERENCE.md#plans-get), [Search](/ai-agents/connectors/orb/REFERENCE.md#plans-search)                         |
| Invoices      | [List](/ai-agents/connectors/orb/REFERENCE.md#invoices-list), [Get](/ai-agents/connectors/orb/REFERENCE.md#invoices-get), [Search](/ai-agents/connectors/orb/REFERENCE.md#invoices-search)                |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/orb/AUTH.md).

### Orb API docs[​](#orb-api-docs "Direct link to Orb API docs")

See the official [Orb API reference](https://docs.withorb.com/api-reference).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.46
* **Connector version:** 0.1.6
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/orb/CHANGELOG.md)
