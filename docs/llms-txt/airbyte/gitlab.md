# Source: https://docs.airbyte.com/integrations/sources/gitlab.md

# Source: https://docs.airbyte.com/ai-agents/connectors/gitlab.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-gitlab/latest/icon.svg)

# Gitlab

Copy Page

The Gitlab agent connector is a Python package that equips AI agents to interact with Gitlab through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the GitLab REST API (v4). Provides access to projects, issues, merge requests, commits, pipelines, groups, branches, releases, tags, members, milestones, and users. Supports both Personal Access Token and OAuth2 authentication.

## Example questions[​](#example-questions "Direct link to Example questions")

The Gitlab connector is optimized to handle prompts like these.

* List all projects I have access to
* Get the details of a specific project
* List all open issues in a project
* Show merge requests for a project
* List all groups I belong to
* Show recent commits in a project
* List pipelines for a project
* Show all branches in a project
* Find issues updated in the last week
* What are the most active projects?
* Show merge requests that are still open
* List projects with the most commits

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Gitlab connector isn't currently able to handle prompts like these.

* Create a new project
* Delete an issue
* Merge a merge request
* Trigger a pipeline

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-gitlab
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_gitlab import GitlabConnector
from airbyte_agent_gitlab.models import GitlabPersonalAccessTokenAuthConfig

connector = GitlabConnector(
    auth_config=GitlabPersonalAccessTokenAuthConfig(
        access_token="<Log into your GitLab account and generate a personal access token.>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GitlabConnector.tool_utils
async def gitlab_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/gitlab/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_gitlab import GitlabConnector, AirbyteAuthConfig

connector = GitlabConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GitlabConnector.tool_utils
async def gitlab_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/gitlab/REFERENCE.md).

| Entity             | Actions                                                                                                                                                                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Projects           | [List](/ai-agents/connectors/gitlab/REFERENCE.md#projects-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#projects-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#projects-search)                               |
| Issues             | [List](/ai-agents/connectors/gitlab/REFERENCE.md#issues-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#issues-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#issues-search)                                     |
| Merge Requests     | [List](/ai-agents/connectors/gitlab/REFERENCE.md#merge-requests-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#merge-requests-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#merge-requests-search)             |
| Users              | [List](/ai-agents/connectors/gitlab/REFERENCE.md#users-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#users-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#users-search)                                        |
| Commits            | [List](/ai-agents/connectors/gitlab/REFERENCE.md#commits-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#commits-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#commits-search)                                  |
| Groups             | [List](/ai-agents/connectors/gitlab/REFERENCE.md#groups-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#groups-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#groups-search)                                     |
| Branches           | [List](/ai-agents/connectors/gitlab/REFERENCE.md#branches-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#branches-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#branches-search)                               |
| Pipelines          | [List](/ai-agents/connectors/gitlab/REFERENCE.md#pipelines-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#pipelines-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#pipelines-search)                            |
| Group Members      | [List](/ai-agents/connectors/gitlab/REFERENCE.md#group-members-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#group-members-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#group-members-search)                |
| Project Members    | [List](/ai-agents/connectors/gitlab/REFERENCE.md#project-members-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#project-members-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#project-members-search)          |
| Releases           | [List](/ai-agents/connectors/gitlab/REFERENCE.md#releases-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#releases-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#releases-search)                               |
| Tags               | [List](/ai-agents/connectors/gitlab/REFERENCE.md#tags-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#tags-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#tags-search)                                           |
| Group Milestones   | [List](/ai-agents/connectors/gitlab/REFERENCE.md#group-milestones-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#group-milestones-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#group-milestones-search)       |
| Project Milestones | [List](/ai-agents/connectors/gitlab/REFERENCE.md#project-milestones-list), [Get](/ai-agents/connectors/gitlab/REFERENCE.md#project-milestones-get), [Search](/ai-agents/connectors/gitlab/REFERENCE.md#project-milestones-search) |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/gitlab/AUTH.md).

### Gitlab API docs[​](#gitlab-api-docs "Direct link to Gitlab API docs")

See the official [Gitlab API reference](https://docs.gitlab.com/ee/api/rest/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.2
* **Connector version:** 1.0.1
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/gitlab/CHANGELOG.md)
