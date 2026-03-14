# Source: https://docs.airbyte.com/integrations/sources/snapchat-marketing.md

# Source: https://docs.airbyte.com/ai-agents/connectors/snapchat-marketing.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-snapchat-marketing/latest/icon.svg)

# Snapchat-Marketing

Copy Page

The Snapchat-Marketing agent connector is a Python package that equips AI agents to interact with Snapchat-Marketing through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Connector for the Snapchat Marketing API (Ads API). Provides access to Snapchat advertising entities including organizations, ad accounts, campaigns, ad squads, ads, creatives, media, and audience segments. Supports OAuth2 authentication with automatic token refresh.

## Example questions[​](#example-questions "Direct link to Example questions")

The Snapchat-Marketing connector is optimized to handle prompts like these.

* List all organizations I belong to
* Show me all ad accounts for my organization
* List all campaigns in my ad account
* Show me the ad squads for my ad account
* List all ads in my ad account
* Show me the creatives for my ad account
* List all media files in my ad account
* Show me the audience segments in my ad account
* Which campaigns are currently active?
* What ad squads have the highest daily budget?
* Show me ads that are pending review
* Find campaigns created in the last month

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Snapchat-Marketing connector isn't currently able to handle prompts like these.

* Create a new campaign
* Update an ad's status
* Delete a creative
* Show me ad performance statistics

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-snapchat-marketing
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_snapchat_marketing import SnapchatMarketingConnector
from airbyte_agent_snapchat_marketing.models import SnapchatMarketingAuthConfig

connector = SnapchatMarketingConnector(
    auth_config=SnapchatMarketingAuthConfig(
        client_id="<The Client ID of your Snapchat developer application>",
        client_secret="<The Client Secret of your Snapchat developer application>",
        refresh_token="<Refresh Token to renew the expired Access Token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SnapchatMarketingConnector.tool_utils
async def snapchat_marketing_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/snapchat-marketing/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_snapchat_marketing import SnapchatMarketingConnector, AirbyteAuthConfig

connector = SnapchatMarketingConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SnapchatMarketingConnector.tool_utils
async def snapchat_marketing_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/snapchat-marketing/REFERENCE.md).

| Entity        | Actions                                                                                                                                                                                                                                                |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Organizations | [List](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#organizations-list), [Get](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#organizations-get), [Search](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#organizations-search) |
| Adaccounts    | [List](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#adaccounts-list), [Get](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#adaccounts-get), [Search](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#adaccounts-search)          |
| Campaigns     | [List](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#campaigns-list), [Get](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#campaigns-get), [Search](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#campaigns-search)             |
| Adsquads      | [List](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#adsquads-list), [Get](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#adsquads-get), [Search](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#adsquads-search)                |
| Ads           | [List](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#ads-list), [Get](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#ads-get), [Search](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#ads-search)                               |
| Creatives     | [List](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#creatives-list), [Get](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#creatives-get), [Search](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#creatives-search)             |
| Media         | [List](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#media-list), [Get](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#media-get), [Search](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#media-search)                         |
| Segments      | [List](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#segments-list), [Get](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#segments-get), [Search](/ai-agents/connectors/snapchat-marketing/REFERENCE.md#segments-search)                |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/snapchat-marketing/AUTH.md).

### Snapchat-Marketing API docs[​](#snapchat-marketing-api-docs "Direct link to Snapchat-Marketing API docs")

See the official [Snapchat-Marketing API reference](https://developers.snap.com/api/marketing-api/Ads-API/introduction).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.1
* **Connector version:** 1.0.1
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/snapchat-marketing/CHANGELOG.md)
