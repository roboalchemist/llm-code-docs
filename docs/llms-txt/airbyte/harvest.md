# Source: https://docs.airbyte.com/integrations/sources/harvest.md

# Source: https://docs.airbyte.com/ai-agents/connectors/harvest.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-harvest/latest/icon.svg)

# Harvest

Copy Page

The Harvest agent connector is a Python package that equips AI agents to interact with Harvest through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the Harvest time-tracking and invoicing API (v2). Provides read access to time tracking data including users, clients, projects, tasks, time entries, invoices, estimates, expenses, and more. Harvest is a cloud-based time tracking and invoicing solution that helps teams track time, manage projects, and streamline invoicing.

## Example questions[​](#example-questions "Direct link to Example questions")

The Harvest connector is optimized to handle prompts like these.

* List all users in Harvest
* Show me all active projects
* List all clients
* Show me recent time entries
* List all invoices
* Show me all tasks
* List all expense categories
* Get company information
* How many hours were logged last week?
* Which projects have the most time entries?
* Show me all unbilled time entries
* What are the active projects for a specific client?
* List all overdue invoices
* Which users logged the most hours this month?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Harvest connector isn't currently able to handle prompts like these.

* Create a new time entry in Harvest
* Update a project budget
* Delete an invoice
* Start a timer for a task

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-harvest
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_harvest import HarvestConnector
from airbyte_agent_harvest.models import HarvestPersonalAccessTokenAuthConfig

connector = HarvestConnector(
    auth_config=HarvestPersonalAccessTokenAuthConfig(
        token="<Your Harvest personal access token>",
        account_id="<Your Harvest account ID>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@HarvestConnector.tool_utils
async def harvest_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/harvest/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_harvest import HarvestConnector, AirbyteAuthConfig

connector = HarvestConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@HarvestConnector.tool_utils
async def harvest_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/harvest/REFERENCE.md).

| Entity                   | Actions                                                                                                                                                                                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Users                    | [List](/ai-agents/connectors/harvest/REFERENCE.md#users-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#users-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#users-search)                                                          |
| Clients                  | [List](/ai-agents/connectors/harvest/REFERENCE.md#clients-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#clients-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#clients-search)                                                    |
| Contacts                 | [List](/ai-agents/connectors/harvest/REFERENCE.md#contacts-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#contacts-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#contacts-search)                                                 |
| Company                  | [Get](/ai-agents/connectors/harvest/REFERENCE.md#company-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#company-search)                                                                                                                     |
| Projects                 | [List](/ai-agents/connectors/harvest/REFERENCE.md#projects-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#projects-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#projects-search)                                                 |
| Tasks                    | [List](/ai-agents/connectors/harvest/REFERENCE.md#tasks-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#tasks-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#tasks-search)                                                          |
| Time Entries             | [List](/ai-agents/connectors/harvest/REFERENCE.md#time-entries-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#time-entries-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#time-entries-search)                                     |
| Invoices                 | [List](/ai-agents/connectors/harvest/REFERENCE.md#invoices-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#invoices-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#invoices-search)                                                 |
| Invoice Item Categories  | [List](/ai-agents/connectors/harvest/REFERENCE.md#invoice-item-categories-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#invoice-item-categories-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#invoice-item-categories-search)    |
| Estimates                | [List](/ai-agents/connectors/harvest/REFERENCE.md#estimates-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#estimates-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#estimates-search)                                              |
| Estimate Item Categories | [List](/ai-agents/connectors/harvest/REFERENCE.md#estimate-item-categories-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#estimate-item-categories-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#estimate-item-categories-search) |
| Expenses                 | [List](/ai-agents/connectors/harvest/REFERENCE.md#expenses-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#expenses-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#expenses-search)                                                 |
| Expense Categories       | [List](/ai-agents/connectors/harvest/REFERENCE.md#expense-categories-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#expense-categories-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#expense-categories-search)                   |
| Roles                    | [List](/ai-agents/connectors/harvest/REFERENCE.md#roles-list), [Get](/ai-agents/connectors/harvest/REFERENCE.md#roles-get), [Search](/ai-agents/connectors/harvest/REFERENCE.md#roles-search)                                                          |
| User Assignments         | [List](/ai-agents/connectors/harvest/REFERENCE.md#user-assignments-list), [Search](/ai-agents/connectors/harvest/REFERENCE.md#user-assignments-search)                                                                                                 |
| Task Assignments         | [List](/ai-agents/connectors/harvest/REFERENCE.md#task-assignments-list), [Search](/ai-agents/connectors/harvest/REFERENCE.md#task-assignments-search)                                                                                                 |
| Time Projects            | [List](/ai-agents/connectors/harvest/REFERENCE.md#time-projects-list), [Search](/ai-agents/connectors/harvest/REFERENCE.md#time-projects-search)                                                                                                       |
| Time Tasks               | [List](/ai-agents/connectors/harvest/REFERENCE.md#time-tasks-list), [Search](/ai-agents/connectors/harvest/REFERENCE.md#time-tasks-search)                                                                                                             |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/harvest/AUTH.md).

### Harvest API docs[​](#harvest-api-docs "Direct link to Harvest API docs")

See the official [Harvest API reference](https://help.getharvest.com/api-v2/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.2
* **Connector version:** 1.0.2
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/harvest/CHANGELOG.md)
