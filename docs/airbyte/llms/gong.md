# Source: https://docs.airbyte.com/integrations/sources/gong.md

# Source: https://docs.airbyte.com/ai-agents/connectors/gong.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-gong/latest/icon.svg)

# Gong

Copy Page

The Gong agent connector is a Python package that equips AI agents to interact with Gong through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Gong is a revenue intelligence platform that captures and analyzes customer interactions across calls, emails, and web conferences. This connector provides access to users, recorded calls with transcripts, activity statistics, scorecards, trackers, workspaces, coaching metrics, and library content for sales performance analysis and revenue insights.

## Example questions[​](#example-questions "Direct link to Example questions")

The Gong connector is optimized to handle prompts like these.

* List all users in my Gong account
* Show me calls from last week
* Get the transcript for a recent call
* List all workspaces in Gong
* Show me the scorecard configurations
* What trackers are set up in my account?
* Get coaching metrics for a manager
* What are the activity stats for our sales team?
* Find calls mentioning {keyword} this month
* Show me calls for rep {user\_id} in the last 30 days
* Which calls had the longest duration last week?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Gong connector isn't currently able to handle prompts like these.

* Create a new user in Gong
* Delete a call recording
* Update scorecard questions
* Schedule a new meeting
* Send feedback to a team member
* Modify tracker keywords

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-gong
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_gong import GongConnector
from airbyte_agent_gong.models import GongAccessKeyAuthenticationAuthConfig

connector = GongConnector(
    auth_config=GongAccessKeyAuthenticationAuthConfig(
        access_key="<Your Gong API Access Key>",
        access_key_secret="<Your Gong API Access Key Secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GongConnector.tool_utils
async def gong_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/gong/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_gong import GongConnector, AirbyteAuthConfig

connector = GongConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GongConnector.tool_utils
async def gong_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/gong/REFERENCE.md).

| Entity                    | Actions                                                                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Users                     | [List](/ai-agents/connectors/gong/REFERENCE.md#users-list), [Get](/ai-agents/connectors/gong/REFERENCE.md#users-get), [Search](/ai-agents/connectors/gong/REFERENCE.md#users-search) |
| Calls                     | [List](/ai-agents/connectors/gong/REFERENCE.md#calls-list), [Get](/ai-agents/connectors/gong/REFERENCE.md#calls-get), [Search](/ai-agents/connectors/gong/REFERENCE.md#calls-search) |
| Calls Extensive           | [List](/ai-agents/connectors/gong/REFERENCE.md#calls-extensive-list), [Search](/ai-agents/connectors/gong/REFERENCE.md#calls-extensive-search)                                       |
| Call Audio                | [Download](/ai-agents/connectors/gong/REFERENCE.md#call-audio-download)                                                                                                              |
| Call Video                | [Download](/ai-agents/connectors/gong/REFERENCE.md#call-video-download)                                                                                                              |
| Workspaces                | [List](/ai-agents/connectors/gong/REFERENCE.md#workspaces-list)                                                                                                                      |
| Call Transcripts          | [List](/ai-agents/connectors/gong/REFERENCE.md#call-transcripts-list)                                                                                                                |
| Stats Activity Aggregate  | [List](/ai-agents/connectors/gong/REFERENCE.md#stats-activity-aggregate-list)                                                                                                        |
| Stats Activity Day By Day | [List](/ai-agents/connectors/gong/REFERENCE.md#stats-activity-day-by-day-list)                                                                                                       |
| Stats Interaction         | [List](/ai-agents/connectors/gong/REFERENCE.md#stats-interaction-list)                                                                                                               |
| Settings Scorecards       | [List](/ai-agents/connectors/gong/REFERENCE.md#settings-scorecards-list), [Search](/ai-agents/connectors/gong/REFERENCE.md#settings-scorecards-search)                               |
| Settings Trackers         | [List](/ai-agents/connectors/gong/REFERENCE.md#settings-trackers-list)                                                                                                               |
| Library Folders           | [List](/ai-agents/connectors/gong/REFERENCE.md#library-folders-list)                                                                                                                 |
| Library Folder Content    | [List](/ai-agents/connectors/gong/REFERENCE.md#library-folder-content-list)                                                                                                          |
| Coaching                  | [List](/ai-agents/connectors/gong/REFERENCE.md#coaching-list)                                                                                                                        |
| Stats Activity Scorecards | [List](/ai-agents/connectors/gong/REFERENCE.md#stats-activity-scorecards-list), [Search](/ai-agents/connectors/gong/REFERENCE.md#stats-activity-scorecards-search)                   |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/gong/AUTH.md).

### Gong API docs[​](#gong-api-docs "Direct link to Gong API docs")

See the official [Gong API reference](https://gong.app.gong.io/settings/api/documentation).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.19.122
* **Connector version:** 0.1.19
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/gong/CHANGELOG.md)
