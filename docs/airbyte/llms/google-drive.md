# Source: https://docs.airbyte.com/integrations/sources/google-drive.md

# Source: https://docs.airbyte.com/ai-agents/connectors/google-drive.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-google-drive/latest/icon.svg)

# Google-Drive

Copy Page

The Google-Drive agent connector is a Python package that equips AI agents to interact with Google-Drive through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

Google Drive is a cloud-based file storage and synchronization service that allows users to store files, share content, and collaborate on documents. This connector provides access to files, shared drives, permissions, comments, replies, revisions, and change tracking, including the ability to create, update, delete, and upload files.

## Example questions[​](#example-questions "Direct link to Example questions")

The Google-Drive connector is optimized to handle prompts like these.

* List all files in my Google Drive
* Show me details for a recent file
* Download a recent file from my Drive
* Export a recent Google Doc as PDF
* Export a recent Google Sheet as CSV
* Show me the content of a recent file
* List all shared drives I have access to
* Show me details for a shared drive I have access to
* Show permissions for a recent file
* List comments on a recent file
* Show replies to a recent comment on a file
* Show revision history for a recent file
* Get my Drive storage quota and user info
* List files in a folder I have access to
* Create a new file in Google Drive
* Upload a document to Drive
* Delete a file from Drive
* Move a file to a different folder
* Show me files modified in the last week
* What changes have been made since my last sync?

## Unsupported questions[​](#unsupported-questions "Direct link to Unsupported questions")

The Google-Drive connector isn't currently able to handle prompts like these.

* Update file permissions
* Add a comment to a file

## Installation[​](#installation "Direct link to Installation")

```
uv pip install airbyte-agent-google-drive
```

## Usage[​](#usage "Direct link to Usage")

Connectors can run in open source or hosted mode.

### Open source[​](#open-source "Direct link to Open source")

In open source mode, you provide API credentials directly to the connector.

```
from airbyte_agent_google_drive import GoogleDriveConnector
from airbyte_agent_google_drive.models import GoogleDriveAuthConfig

connector = GoogleDriveConnector(
    auth_config=GoogleDriveAuthConfig(
        access_token="<Your Google OAuth2 Access Token (optional, will be obtained via refresh)>",
        refresh_token="<Your Google OAuth2 Refresh Token>",
        client_id="<Your Google OAuth2 Client ID>",
        client_secret="<Your Google OAuth2 Client Secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GoogleDriveConnector.tool_utils
async def google_drive_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted[​](#hosted "Direct link to Hosted")

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. If your Airbyte client can access multiple organizations, also set `organization_id`.

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](/ai-agents/connectors/google-drive/AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```
from airbyte_agent_google_drive import GoogleDriveConnector, AirbyteAuthConfig

connector = GoogleDriveConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GoogleDriveConnector.tool_utils
async def google_drive_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation[​](#full-documentation "Direct link to Full documentation")

### Entities and actions[​](#entities-and-actions "Direct link to Entities and actions")

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](/ai-agents/connectors/google-drive/REFERENCE.md).

| Entity                   | Actions                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Files                    | [List](/ai-agents/connectors/google-drive/REFERENCE.md#files-list), [Get](/ai-agents/connectors/google-drive/REFERENCE.md#files-get), [Create](/ai-agents/connectors/google-drive/REFERENCE.md#files-create), [Update](/ai-agents/connectors/google-drive/REFERENCE.md#files-update), [Delete](/ai-agents/connectors/google-drive/REFERENCE.md#files-delete), [Download](/ai-agents/connectors/google-drive/REFERENCE.md#files-download) |
| Files Upload             | [Create](/ai-agents/connectors/google-drive/REFERENCE.md#files-upload-create)                                                                                                                                                                                                                                                                                                                                                            |
| Files Export             | [Download](/ai-agents/connectors/google-drive/REFERENCE.md#files-export-download)                                                                                                                                                                                                                                                                                                                                                        |
| Drives                   | [List](/ai-agents/connectors/google-drive/REFERENCE.md#drives-list), [Get](/ai-agents/connectors/google-drive/REFERENCE.md#drives-get)                                                                                                                                                                                                                                                                                                   |
| Permissions              | [List](/ai-agents/connectors/google-drive/REFERENCE.md#permissions-list), [Get](/ai-agents/connectors/google-drive/REFERENCE.md#permissions-get)                                                                                                                                                                                                                                                                                         |
| Comments                 | [List](/ai-agents/connectors/google-drive/REFERENCE.md#comments-list), [Get](/ai-agents/connectors/google-drive/REFERENCE.md#comments-get)                                                                                                                                                                                                                                                                                               |
| Replies                  | [List](/ai-agents/connectors/google-drive/REFERENCE.md#replies-list), [Get](/ai-agents/connectors/google-drive/REFERENCE.md#replies-get)                                                                                                                                                                                                                                                                                                 |
| Revisions                | [List](/ai-agents/connectors/google-drive/REFERENCE.md#revisions-list), [Get](/ai-agents/connectors/google-drive/REFERENCE.md#revisions-get)                                                                                                                                                                                                                                                                                             |
| Changes                  | [List](/ai-agents/connectors/google-drive/REFERENCE.md#changes-list)                                                                                                                                                                                                                                                                                                                                                                     |
| Changes Start Page Token | [Get](/ai-agents/connectors/google-drive/REFERENCE.md#changes-start-page-token-get)                                                                                                                                                                                                                                                                                                                                                      |
| About                    | [Get](/ai-agents/connectors/google-drive/REFERENCE.md#about-get)                                                                                                                                                                                                                                                                                                                                                                         |

### Authentication[​](#authentication "Direct link to Authentication")

For all authentication options, see the connector's [authentication documentation](/ai-agents/connectors/google-drive/AUTH.md).

### Google-Drive API docs[​](#google-drive-api-docs "Direct link to Google-Drive API docs")

See the official [Google-Drive API reference](https://developers.google.com/workspace/drive/api/reference/rest/v3).

## Version information[​](#version-information "Direct link to Version information")

* **Package version:** 0.1.87
* **Connector version:** 0.2.2
* **Generated with Connector SDK commit SHA:** 44677ecbb4b815bb4fb2a54c6e5339681bcf36a8
* **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/google-drive/CHANGELOG.md)
