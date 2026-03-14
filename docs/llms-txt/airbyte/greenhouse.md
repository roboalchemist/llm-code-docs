# Source: https://docs.airbyte.com/integrations/sources/greenhouse.md

# Source: https://docs.airbyte.com/ai-agents/connectors/greenhouse.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-greenhouse/latest/icon.svg)

# Greenhouse

Copy Page

The Greenhouse agent connector is a Python package that equips AI agents to interact with Greenhouse through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Greenhouse is an applicant tracking system (ATS) that helps companies manage their hiring process. This connector provides access to candidates, applications, jobs, offers, users, departments, offices, job posts, sources, and scheduled interviews for recruiting analytics and talent acquisition insights.

## Example questions[​](#example-questions "Direct link to Example questions")

The Greenhouse connector is optimized to handle prompts like these.

* List all open jobs
* Show me upcoming interviews this week
* Show me recent job offers
* List recent applications
* Show me candidates from {company} who applied last month
* What are the top 5 sources for our job applications this quarter?
* Analyze the interview schedules for our engineering candidates this week
* Compare the number of applications across different offices
* Identify candidates who have multiple applications in our system
* Summarize the candidate pipeline for our latest job posting
* Find the most active departments in recruiting this month

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Greenhouse connector isn't currently able to handle prompts like these.

* Create a new job posting for the marketing team
* Schedule an interview for {candidate}
* Update the status of {candidate}'s application
* Delete a candidate profile
* Send an offer letter to {candidate}
* Edit the details of a job description

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-greenhouse
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_greenhouse import GreenhouseConnector
from airbyte_agent_greenhouse.models import GreenhouseAuthConfig

connector = GreenhouseConnector(
    auth_config=GreenhouseAuthConfig(
        api_key="<Your Greenhouse Harvest API Key from the Dev Center>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GreenhouseConnector.tool_utils
async def greenhouse_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/greenhouse/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_greenhouse import GreenhouseConnector, AirbyteAuthConfig

connector = GreenhouseConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GreenhouseConnector.tool_utils
async def greenhouse_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/greenhouse/REFERENCE.md).

| Entity                 | Actions                                                                                                                                                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Candidates             | [List](/ai-agents/connectors/greenhouse/REFERENCE.md#candidates-list), [Get](/ai-agents/connectors/greenhouse/REFERENCE.md#candidates-get), [Search](/ai-agents/connectors/greenhouse/REFERENCE.md#candidates-search)       |
| Applications           | [List](/ai-agents/connectors/greenhouse/REFERENCE.md#applications-list), [Get](/ai-agents/connectors/greenhouse/REFERENCE.md#applications-get), [Search](/ai-agents/connectors/greenhouse/REFERENCE.md#applications-search) |
| Jobs                   | [List](/ai-agents/connectors/greenhouse/REFERENCE.md#jobs-list), [Get](/ai-agents/connectors/greenhouse/REFERENCE.md#jobs-get), [Search](/ai-agents/connectors/greenhouse/REFERENCE.md#jobs-search)                         |
| Offers                 | [List](/ai-agents/connectors/greenhouse/REFERENCE.md#offers-list), [Get](/ai-agents/connectors/greenhouse/REFERENCE.md#offers-get), [Search](/ai-agents/connectors/greenhouse/REFERENCE.md#offers-search)                   |
| Users                  | [List](/ai-agents/connectors/greenhouse/REFERENCE.md#users-list), [Get](/ai-agents/connectors/greenhouse/REFERENCE.md#users-get), [Search](/ai-agents/connectors/greenhouse/REFERENCE.md#users-search)                      |
| Departments            | [List](/ai-agents/connectors/greenhouse/REFERENCE.md#departments-list), [Get](/ai-agents/connectors/greenhouse/REFERENCE.md#departments-get), [Search](/ai-agents/connectors/greenhouse/REFERENCE.md#departments-search)    |
| Offices                | [List](/ai-agents/connectors/greenhouse/REFERENCE.md#offices-list), [Get](/ai-agents/connectors/greenhouse/REFERENCE.md#offices-get), [Search](/ai-agents/connectors/greenhouse/REFERENCE.md#offices-search)                |
| Job Posts              | [List](/ai-agents/connectors/greenhouse/REFERENCE.md#job-posts-list), [Get](/ai-agents/connectors/greenhouse/REFERENCE.md#job-posts-get), [Search](/ai-agents/connectors/greenhouse/REFERENCE.md#job-posts-search)          |
| Sources                | [List](/ai-agents/connectors/greenhouse/REFERENCE.md#sources-list), [Search](/ai-agents/connectors/greenhouse/REFERENCE.md#sources-search)                                                                                  |
| Scheduled Interviews   | [List](/ai-agents/connectors/greenhouse/REFERENCE.md#scheduled-interviews-list), [Get](/ai-agents/connectors/greenhouse/REFERENCE.md#scheduled-interviews-get)                                                              |
| Application Attachment | [Download](/ai-agents/connectors/greenhouse/REFERENCE.md#application-attachment-download)                                                                                                                                   |
| Candidate Attachment   | [Download](/ai-agents/connectors/greenhouse/REFERENCE.md#candidate-attachment-download)                                                                                                                                     |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/greenhouse/AUTH.md).

### Greenhouse API docs[​](#greenhouse-api-docs "Direct link to Greenhouse API docs")

See the official [Greenhouse API reference](https://developers.greenhouse.io/harvest.html).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.17.111
* **Connector version:** 0.1.7
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/greenhouse/CHANGELOG.md)
