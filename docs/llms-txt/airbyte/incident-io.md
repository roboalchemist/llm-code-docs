# Source: https://docs.airbyte.com/integrations/sources/incident-io.md

# Source: https://docs.airbyte.com/ai-agents/connectors/incident-io.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-incident-io/latest/icon.svg)

# Incident-Io

Copy Page

The Incident-Io agent connector is a Python package that equips AI agents to interact with Incident-Io through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connect to the incident.io API to access incident management data including incidents, alerts, escalations, users, schedules, and more. incident.io is an on-call, status pages, and incident response platform. This connector provides read-only access to core incident management entities via the v1 and v2 APIs. Requires an API key from your incident.io dashboard (Pro plan or above).

## Example questions[​](#example-questions "Direct link to Example questions")

The Incident-Io connector is optimized to handle prompts like these.

* List all incidents
* Show all open incidents
* List all alerts
* Show all users
* List all escalations
* Show all on-call schedules
* List all severities
* Show all incident statuses
* List all custom fields
* Which incidents were created this week?
* What are the most recent high-severity incidents?
* Who is currently on-call?
* How many incidents are in triage status?
* What incidents were updated today?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Incident-Io connector isn't currently able to handle prompts like these.

* Create a new incident
* Update an incident's severity
* Delete an alert
* Assign someone to an incident role

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-incident-io
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_incident_io import IncidentIoConnector
from airbyte_agent_incident_io.models import IncidentIoAuthConfig

connector = IncidentIoConnector(
    auth_config=IncidentIoAuthConfig(
        api_key="<Your incident.io API key. Create one at https://app.incident.io/settings/api-keys>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@IncidentIoConnector.tool_utils
async def incident_io_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/incident-io/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_incident_io import IncidentIoConnector, AirbyteAuthConfig

connector = IncidentIoConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@IncidentIoConnector.tool_utils
async def incident_io_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/incident-io/REFERENCE.md).

| Entity              | Actions                                                                                                                                                                                                                                             |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Incidents           | [List](/ai-agents/connectors/incident-io/REFERENCE.md#incidents-list), [Get](/ai-agents/connectors/incident-io/REFERENCE.md#incidents-get), [Search](/ai-agents/connectors/incident-io/REFERENCE.md#incidents-search)                               |
| Alerts              | [List](/ai-agents/connectors/incident-io/REFERENCE.md#alerts-list), [Get](/ai-agents/connectors/incident-io/REFERENCE.md#alerts-get), [Search](/ai-agents/connectors/incident-io/REFERENCE.md#alerts-search)                                        |
| Escalations         | [List](/ai-agents/connectors/incident-io/REFERENCE.md#escalations-list), [Get](/ai-agents/connectors/incident-io/REFERENCE.md#escalations-get), [Search](/ai-agents/connectors/incident-io/REFERENCE.md#escalations-search)                         |
| Users               | [List](/ai-agents/connectors/incident-io/REFERENCE.md#users-list), [Get](/ai-agents/connectors/incident-io/REFERENCE.md#users-get), [Search](/ai-agents/connectors/incident-io/REFERENCE.md#users-search)                                           |
| Incident Updates    | [List](/ai-agents/connectors/incident-io/REFERENCE.md#incident-updates-list), [Search](/ai-agents/connectors/incident-io/REFERENCE.md#incident-updates-search)                                                                                      |
| Incident Roles      | [List](/ai-agents/connectors/incident-io/REFERENCE.md#incident-roles-list), [Get](/ai-agents/connectors/incident-io/REFERENCE.md#incident-roles-get), [Search](/ai-agents/connectors/incident-io/REFERENCE.md#incident-roles-search)                |
| Incident Statuses   | [List](/ai-agents/connectors/incident-io/REFERENCE.md#incident-statuses-list), [Get](/ai-agents/connectors/incident-io/REFERENCE.md#incident-statuses-get), [Search](/ai-agents/connectors/incident-io/REFERENCE.md#incident-statuses-search)       |
| Incident Timestamps | [List](/ai-agents/connectors/incident-io/REFERENCE.md#incident-timestamps-list), [Get](/ai-agents/connectors/incident-io/REFERENCE.md#incident-timestamps-get), [Search](/ai-agents/connectors/incident-io/REFERENCE.md#incident-timestamps-search) |
| Severities          | [List](/ai-agents/connectors/incident-io/REFERENCE.md#severities-list), [Get](/ai-agents/connectors/incident-io/REFERENCE.md#severities-get), [Search](/ai-agents/connectors/incident-io/REFERENCE.md#severities-search)                            |
| Custom Fields       | [List](/ai-agents/connectors/incident-io/REFERENCE.md#custom-fields-list), [Get](/ai-agents/connectors/incident-io/REFERENCE.md#custom-fields-get), [Search](/ai-agents/connectors/incident-io/REFERENCE.md#custom-fields-search)                   |
| Catalog Types       | [List](/ai-agents/connectors/incident-io/REFERENCE.md#catalog-types-list), [Get](/ai-agents/connectors/incident-io/REFERENCE.md#catalog-types-get), [Search](/ai-agents/connectors/incident-io/REFERENCE.md#catalog-types-search)                   |
| Schedules           | [List](/ai-agents/connectors/incident-io/REFERENCE.md#schedules-list), [Get](/ai-agents/connectors/incident-io/REFERENCE.md#schedules-get), [Search](/ai-agents/connectors/incident-io/REFERENCE.md#schedules-search)                               |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/incident-io/AUTH.md).

### Incident-Io API docs[​](#incident-io-api-docs "Direct link to Incident-Io API docs")

See the official [Incident-Io API reference](https://api-docs.incident.io/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.6
* **Connector version:** 1.0.3
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/incident-io/CHANGELOG.md)
