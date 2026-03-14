# Source: https://docs.airbyte.com/integrations/sources/pinterest.md

# Source: https://docs.airbyte.com/ai-agents/connectors/pinterest.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-pinterest/latest/icon.svg)

# Pinterest

Copy Page

The Pinterest agent connector is a Python package that equips AI agents to interact with Pinterest through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the Pinterest API v5, enabling access to Pinterest advertising and content management data. Supports reading ad accounts, boards, campaigns, ad groups, ads, board sections, board pins, catalogs, catalog feeds, catalog product groups, audiences, conversion tags, customer lists, and keywords.

## Example questions[​](#example-questions "Direct link to Example questions")

The Pinterest connector is optimized to handle prompts like these.

* List all my Pinterest ad accounts
* List all my Pinterest boards
* Show me all campaigns in my ad account
* List all ads in my ad account
* Show me all ad groups in my ad account
* List all audiences for my ad account
* Show me my catalog feeds
* Which campaigns are currently active?
* What are the top boards by pin count?
* Show me ads that have been rejected
* Find campaigns with the highest daily spend cap

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Pinterest connector isn't currently able to handle prompts like these.

* Create a new Pinterest board
* Update a campaign budget
* Delete an ad group
* Post a new pin
* Show me campaign analytics or performance metrics

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-pinterest
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_pinterest import PinterestConnector
from airbyte_agent_pinterest.models import PinterestAuthConfig

connector = PinterestConnector(
    auth_config=PinterestAuthConfig(
        refresh_token="<Pinterest OAuth2 refresh token.>",
        client_id="<Pinterest OAuth2 client ID.>",
        client_secret="<Pinterest OAuth2 client secret.>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@PinterestConnector.tool_utils
async def pinterest_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/pinterest/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_pinterest import PinterestConnector, AirbyteAuthConfig

connector = PinterestConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@PinterestConnector.tool_utils
async def pinterest_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/pinterest/REFERENCE.md).

| Entity                  | Actions                                                                                                                                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ad Accounts             | [List](/ai-agents/connectors/pinterest/REFERENCE.md#ad-accounts-list), [Get](/ai-agents/connectors/pinterest/REFERENCE.md#ad-accounts-get), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#ad-accounts-search) |
| Boards                  | [List](/ai-agents/connectors/pinterest/REFERENCE.md#boards-list), [Get](/ai-agents/connectors/pinterest/REFERENCE.md#boards-get), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#boards-search)                |
| Campaigns               | [List](/ai-agents/connectors/pinterest/REFERENCE.md#campaigns-list), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#campaigns-search)                                                                          |
| Ad Groups               | [List](/ai-agents/connectors/pinterest/REFERENCE.md#ad-groups-list), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#ad-groups-search)                                                                          |
| Ads                     | [List](/ai-agents/connectors/pinterest/REFERENCE.md#ads-list), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#ads-search)                                                                                      |
| Board Sections          | [List](/ai-agents/connectors/pinterest/REFERENCE.md#board-sections-list), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#board-sections-search)                                                                |
| Board Pins              | [List](/ai-agents/connectors/pinterest/REFERENCE.md#board-pins-list), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#board-pins-search)                                                                        |
| Catalogs                | [List](/ai-agents/connectors/pinterest/REFERENCE.md#catalogs-list), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#catalogs-search)                                                                            |
| Catalogs Feeds          | [List](/ai-agents/connectors/pinterest/REFERENCE.md#catalogs-feeds-list), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#catalogs-feeds-search)                                                                |
| Catalogs Product Groups | [List](/ai-agents/connectors/pinterest/REFERENCE.md#catalogs-product-groups-list), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#catalogs-product-groups-search)                                              |
| Audiences               | [List](/ai-agents/connectors/pinterest/REFERENCE.md#audiences-list), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#audiences-search)                                                                          |
| Conversion Tags         | [List](/ai-agents/connectors/pinterest/REFERENCE.md#conversion-tags-list), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#conversion-tags-search)                                                              |
| Customer Lists          | [List](/ai-agents/connectors/pinterest/REFERENCE.md#customer-lists-list), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#customer-lists-search)                                                                |
| Keywords                | [List](/ai-agents/connectors/pinterest/REFERENCE.md#keywords-list), [Search](/ai-agents/connectors/pinterest/REFERENCE.md#keywords-search)                                                                            |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/pinterest/AUTH.md).

### Pinterest API docs[​](#pinterest-api-docs "Direct link to Pinterest API docs")

See the official [Pinterest API reference](https://developers.pinterest.com/docs/api/v5/).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.1
* **Connector version:** 0.1.1
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/pinterest/CHANGELOG.md)
