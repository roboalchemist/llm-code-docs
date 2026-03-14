# Source: https://docs.airbyte.com/integrations/sources/github.md

# Source: https://docs.airbyte.com/ai-agents/connectors/github.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-github/latest/icon.svg)

# Github

Copy Page

The Github agent connector is a Python package that equips AI agents to interact with Github through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

GitHub is a platform for version control and collaborative software development using Git. This connector provides access to repositories, branches, commits, issues, pull requests, reviews, comments, releases, organizations, teams, and users for development workflow analysis and project management insights.

## Example questions[​](#example-questions "Direct link to Example questions")

The Github connector is optimized to handle prompts like these.

* Show me all open issues in my repositories this month
* List the top 5 repositories I've starred recently
* Analyze the commit trends in my main project over the last quarter
* Find all pull requests created in the past two weeks
* Search for repositories related to machine learning in my organizations
* Compare the number of contributors across my different team projects
* Identify the most active branches in my main repository
* Get details about the most recent releases in my organization
* List all milestones for our current development sprint
* Show me insights about pull request review patterns in our team

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Github connector isn't currently able to handle prompts like these.

* Create a new issue in the project repository
* Update the status of this pull request
* Delete an old branch from the repository
* Schedule a team review for this code
* Assign a new label to this issue

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-github
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

connector = GithubConnector(
    auth_config=GithubPersonalAccessTokenAuthConfig(
        token="<GitHub personal access token (fine-grained or classic)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GithubConnector.tool_utils
async def github_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/github/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_github import GithubConnector, AirbyteAuthConfig

connector = GithubConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GithubConnector.tool_utils
async def github_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/github/REFERENCE.md).

| Entity              | Actions                                                                                                                                                                                                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Repositories        | [Get](/ai-agents/connectors/github/REFERENCE.md#repositories-get), [List](/ai-agents/connectors/github/REFERENCE.md#repositories-list), [API Search](/ai-agents/connectors/github/REFERENCE.md#repositories-api_search)    |
| Org Repositories    | [List](/ai-agents/connectors/github/REFERENCE.md#org-repositories-list)                                                                                                                                                    |
| Branches            | [List](/ai-agents/connectors/github/REFERENCE.md#branches-list), [Get](/ai-agents/connectors/github/REFERENCE.md#branches-get)                                                                                             |
| Commits             | [List](/ai-agents/connectors/github/REFERENCE.md#commits-list), [Get](/ai-agents/connectors/github/REFERENCE.md#commits-get)                                                                                               |
| Releases            | [List](/ai-agents/connectors/github/REFERENCE.md#releases-list), [Get](/ai-agents/connectors/github/REFERENCE.md#releases-get)                                                                                             |
| Issues              | [List](/ai-agents/connectors/github/REFERENCE.md#issues-list), [Get](/ai-agents/connectors/github/REFERENCE.md#issues-get), [API Search](/ai-agents/connectors/github/REFERENCE.md#issues-api_search)                      |
| Pull Requests       | [List](/ai-agents/connectors/github/REFERENCE.md#pull-requests-list), [Get](/ai-agents/connectors/github/REFERENCE.md#pull-requests-get), [API Search](/ai-agents/connectors/github/REFERENCE.md#pull-requests-api_search) |
| Reviews             | [List](/ai-agents/connectors/github/REFERENCE.md#reviews-list)                                                                                                                                                             |
| Comments            | [List](/ai-agents/connectors/github/REFERENCE.md#comments-list), [Get](/ai-agents/connectors/github/REFERENCE.md#comments-get)                                                                                             |
| Pr Comments         | [List](/ai-agents/connectors/github/REFERENCE.md#pr-comments-list), [Get](/ai-agents/connectors/github/REFERENCE.md#pr-comments-get)                                                                                       |
| Labels              | [List](/ai-agents/connectors/github/REFERENCE.md#labels-list), [Get](/ai-agents/connectors/github/REFERENCE.md#labels-get)                                                                                                 |
| Milestones          | [List](/ai-agents/connectors/github/REFERENCE.md#milestones-list), [Get](/ai-agents/connectors/github/REFERENCE.md#milestones-get)                                                                                         |
| Organizations       | [Get](/ai-agents/connectors/github/REFERENCE.md#organizations-get), [List](/ai-agents/connectors/github/REFERENCE.md#organizations-list)                                                                                   |
| Users               | [Get](/ai-agents/connectors/github/REFERENCE.md#users-get), [List](/ai-agents/connectors/github/REFERENCE.md#users-list), [API Search](/ai-agents/connectors/github/REFERENCE.md#users-api_search)                         |
| Teams               | [List](/ai-agents/connectors/github/REFERENCE.md#teams-list), [Get](/ai-agents/connectors/github/REFERENCE.md#teams-get)                                                                                                   |
| Tags                | [List](/ai-agents/connectors/github/REFERENCE.md#tags-list), [Get](/ai-agents/connectors/github/REFERENCE.md#tags-get)                                                                                                     |
| Stargazers          | [List](/ai-agents/connectors/github/REFERENCE.md#stargazers-list)                                                                                                                                                          |
| Viewer              | [Get](/ai-agents/connectors/github/REFERENCE.md#viewer-get)                                                                                                                                                                |
| Viewer Repositories | [List](/ai-agents/connectors/github/REFERENCE.md#viewer-repositories-list)                                                                                                                                                 |
| Projects            | [List](/ai-agents/connectors/github/REFERENCE.md#projects-list), [Get](/ai-agents/connectors/github/REFERENCE.md#projects-get)                                                                                             |
| Project Items       | [List](/ai-agents/connectors/github/REFERENCE.md#project-items-list)                                                                                                                                                       |
| File Content        | [Get](/ai-agents/connectors/github/REFERENCE.md#file-content-get)                                                                                                                                                          |
| Directory Content   | [List](/ai-agents/connectors/github/REFERENCE.md#directory-content-list)                                                                                                                                                   |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/github/AUTH.md).

### Github API docs[​](#github-api-docs "Direct link to Github API docs")

See the official [Github API reference](https://docs.github.com/en/rest).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.18.119
* **Connector version:** 0.1.16
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/github/CHANGELOG.md)
