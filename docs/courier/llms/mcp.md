# Source: https://www.courier.com/docs/tools/mcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Model Context Protocol (MCP)

> Give AI agents full access to the Courier API. Send messages, manage profiles, debug deliveries, configure lists, and more.

## Prerequisite: Create an API Key

You need a Courier API key to authenticate MCP requests. [Create one in your Courier Settings](https://app.courier.com/settings/api-keys), then replace `YOUR_COURIER_API_KEY` in the installation config below.

<Tip>
  Each MCP client passes the key differently (header, flag, or config field), but the value is the same API key you'd use with the REST API or any Courier SDK.
</Tip>

## Installation

<Tabs>
  <Tab title="Cursor">
    #### Quick install:

    <a href="https://cursor.com/en/install-mcp?name=courier&config=eyJ1cmwiOiJodHRwczovL21jcC5jb3VyaWVyLmNvbSIsImhlYWRlcnMiOnsiYXBpX2tleSI6IlhYWFgifX0%3D" target="_blank">
      <img src="https://cursor.com/deeplink/mcp-install-dark.svg" alt="Add to Cursor" height="32" style={{maxWidth: '200px'}} className="block dark:hidden" noZoom />

      <img src="https://cursor.com/deeplink/mcp-install-light.svg" alt="Add to Cursor" height="32" style={{maxWidth: '200px'}} className="hidden dark:block" noZoom />
    </a>

    #### Manual install:

    In Cursor, go to **Cursor > Cursor Settings > Tools & Integrations > MCP Tools > New MCP Server**, then add:

    ```json  theme={null}
    {
      "mcpServers": {
        "courier": {
          "url": "https://mcp.courier.com",
          "headers": {
            "api_key": "YOUR_COURIER_API_KEY"
          }
        }
      }
    }
    ```

    <Tip>
      Courier MCP works best with Agent mode enabled.
    </Tip>
  </Tab>

  <Tab title="Claude Code">
    ```bash  theme={null}
    claude mcp add --transport http courier https://mcp.courier.com --header api_key:YOUR_COURIER_API_KEY
    ```
  </Tab>

  <Tab title="Claude Desktop">
    In Claude Desktop, go to **Claude > Settings > Developer > Edit Config**, then add:

    ```json  theme={null}
    {
      "mcpServers": {
        "courier": {
          "command": "npx",
          "args": ["-y", "mcp-remote", "https://mcp.courier.com", "--header", "api_key: YOUR_COURIER_API_KEY"]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Windsurf">
    In Windsurf, go to **Windsurf > Windsurf Settings > Manage MCP Servers > View Raw Config**, then add:

    ```json  theme={null}
    {
      "mcpServers": {
        "courier": {
          "serverUrl": "https://mcp.courier.com",
          "headers": {
            "api_key": "YOUR_COURIER_API_KEY"
          },
          "disabled": false,
          "disabledTools": []
        }
      }
    }
    ```
  </Tab>

  <Tab title="VSCode">
    Create `.vscode/mcp.json` in your project and add:

    ```json  theme={null}
    {
      "inputs": [
        {
          "type": "promptString",
          "id": "courier-api-key",
          "description": "API key for Courier service",
          "password": true
        }
      ],
      "servers": {
        "courier": {
          "url": "https://mcp.courier.com",
          "type": "http",
          "headers": {
            "api_key": "${input:courier-api-key}"
          }
        }
      }
    }
    ```

    Open the chat window, click the Gear icon, then **MCP Servers**, and start the "courier" server.

    <Tip>
      VS Code works best when prefixing prompts with `#` in the chat. For example: `#get_user_profile_by_id example_user_id`.
    </Tip>
  </Tab>

  <Tab title="OpenAI API">
    OpenAI's [Responses API](https://platform.openai.com/docs/guides/tools-remote-mcp) supports MCP servers as tool providers. The `input` field is the user prompt; the model decides which tools to call based on it.

    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI();

    const response = await client.responses.create({
      model: "gpt-4o",
      input: "Look up the profile for user-123 and tell me their email",
      tools: [
        {
          type: "mcp",
          server_label: "courier",
          server_url: "https://mcp.courier.com",
          headers: { api_key: "YOUR_COURIER_API_KEY" },
          require_approval: "never",
        },
      ],
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

## Available Tools

The Courier MCP server exposes 60 tools covering the full Courier API surface: 59 default tools plus 1 diagnostic tool available in local installs. All tools are backed by the official [`@trycourier/courier`](https://www.npmjs.com/package/@trycourier/courier) Node SDK with typed error handling.

### Send

| Tool                                                                  | Description                                        |
| --------------------------------------------------------------------- | -------------------------------------------------- |
| [`send_message`](/api-reference/send/send-a-message)                  | Send a message using inline title and body content |
| [`send_message_template`](/api-reference/send/send-a-message)         | Send a message using a notification template       |
| [`send_message_to_list`](/api-reference/send/send-a-message)          | Send inline content to all subscribers of a list   |
| [`send_message_to_list_template`](/api-reference/send/send-a-message) | Send a template to all subscribers of a list       |

### Messages

| Tool                                                                      | Description                                                           |
| ------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| [`list_messages`](/api-reference/sent-messages/list-messages)             | List sent messages with filters (status, recipient, provider, tags)   |
| [`get_message`](/api-reference/sent-messages/get-message)                 | Get full details and delivery status of a message                     |
| [`get_message_content`](/api-reference/sent-messages/get-message-content) | Get the rendered HTML, text, and subject of a sent message            |
| [`get_message_history`](/api-reference/sent-messages/get-message-history) | Get the event history for a message (enqueued, sent, delivered, etc.) |
| [`cancel_message`](/api-reference/sent-messages/cancel-message)           | Cancel a message currently being delivered                            |

### Profiles

| Tool                                                                                       | Description                                     |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| [`get_user_profile_by_id`](/api-reference/user-profiles/get-a-profile)                     | Get a user profile by ID                        |
| [`create_or_merge_user`](/api-reference/user-profiles/create-a-profile)                    | Create or merge values into an existing profile |
| [`replace_profile`](/api-reference/user-profiles/replace-a-profile)                        | Fully replace a user profile (PUT)              |
| [`delete_profile`](/api-reference/user-profiles/delete-a-profile)                          | Delete a user profile                           |
| [`get_user_list_subscriptions`](/api-reference/user-profiles/get-list-subscriptions)       | Get all list subscriptions for a user           |
| [`subscribe_user_to_lists`](/api-reference/user-profiles/subscribe-to-one-or-more-lists)   | Subscribe a user to one or more lists           |
| [`delete_user_list_subscriptions`](/api-reference/user-profiles/delete-list-subscriptions) | Remove all list subscriptions for a user        |

### Lists

| Tool                                                                                        | Description                                   |
| ------------------------------------------------------------------------------------------- | --------------------------------------------- |
| [`list_lists`](/api-reference/lists/get-all-lists)                                          | Get all lists, optionally filtered by pattern |
| [`get_list`](/api-reference/lists/get-a-list)                                               | Get a list by ID                              |
| [`get_list_subscribers`](/api-reference/lists/get-the-subscriptions-for-a-list)             | Get all subscribers of a list                 |
| [`create_list`](/api-reference/lists/update-a-list)                                         | Create or update a list                       |
| [`subscribe_user_to_list`](/api-reference/lists/subscribe-users-to-a-list)                  | Subscribe a user to a list                    |
| [`unsubscribe_user_from_list`](/api-reference/lists/unsubscribe-a-user-profile-from-a-list) | Unsubscribe a user from a list                |

### Audiences

| Tool                                                                      | Description                                           |
| ------------------------------------------------------------------------- | ----------------------------------------------------- |
| [`get_audience`](/api-reference/audiences/get-an-audience)                | Get an audience by ID                                 |
| [`list_audiences`](/api-reference/audiences/list-all-audiences)           | List all audiences                                    |
| [`list_audience_members`](/api-reference/audiences/list-audience-members) | List members of an audience                           |
| [`update_audience`](/api-reference/audiences/update-an-audience)          | Create or update an audience with a filter definition |
| [`delete_audience`](/api-reference/audiences/delete-an-audience)          | Delete an audience                                    |

### Notifications

| Tool                                                                                                     | Description                                |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| [`list_notifications`](/api-reference/notification-templates/get-notifications)                          | List notification templates                |
| [`get_notification_content`](/api-reference/notification-templates/get-notifications-content)            | Get published content blocks of a template |
| [`get_notification_draft_content`](/api-reference/notification-templates/get-notifications-draftcontent) | Get draft content blocks of a template     |

### Brands

| Tool                                                       | Description        |
| ---------------------------------------------------------- | ------------------ |
| [`create_brand`](/api-reference/brands/create-a-new-brand) | Create a new brand |
| [`get_brand`](/api-reference/brands/get-a-brand)           | Get a brand by ID  |
| [`list_brands`](/api-reference/brands/list-brands)         | List all brands    |

### Auth & Tokens

| Tool                                                                                         | Description                                   |
| -------------------------------------------------------------------------------------------- | --------------------------------------------- |
| [`generate_jwt_for_user`](/api-reference/authentication/create-a-jwt)                        | Generate a JWT token for client-side SDK auth |
| [`list_user_push_tokens`](/api-reference/device-tokens/get-all-tokens)                       | List all push/device tokens for a user        |
| [`get_user_push_token`](/api-reference/device-tokens/get-single-token)                       | Get a specific push token                     |
| [`create_or_replace_user_push_token`](/api-reference/device-tokens/add-single-token-to-user) | Create or replace a push token                |

### Automations

| Tool                                                                                 | Description                                   |
| ------------------------------------------------------------------------------------ | --------------------------------------------- |
| [`invoke_automation_template`](/api-reference/automations/invoke-an-automation)      | Invoke an automation from a template          |
| [`invoke_ad_hoc_automation`](/api-reference/automations/invoke-an-ad-hoc-automation) | Invoke an ad-hoc automation with inline steps |

### Bulk

| Tool                                                       | Description                                 |
| ---------------------------------------------------------- | ------------------------------------------- |
| [`create_bulk_job`](/api-reference/bulk/create-a-bulk-job) | Create a bulk job for multi-recipient sends |
| [`add_bulk_users`](/api-reference/bulk/add-users)          | Add users to an existing bulk job           |
| [`run_bulk_job`](/api-reference/bulk/run-a-job)            | Trigger delivery for a bulk job             |
| [`get_bulk_job`](/api-reference/bulk/get-a-job)            | Get the status of a bulk job                |
| [`list_bulk_users`](/api-reference/bulk/get-users)         | List users in a bulk job                    |

### Tenants

| Tool                                                                           | Description                |
| ------------------------------------------------------------------------------ | -------------------------- |
| [`get_tenant`](/api-reference/tenants/get-a-tenant)                            | Get a tenant by ID         |
| [`create_or_update_tenant`](/api-reference/tenants/create-or-replace-a-tenant) | Create or replace a tenant |
| [`list_tenants`](/api-reference/tenants/get-a-list-of-tenants)                 | List all tenants           |
| [`delete_tenant`](/api-reference/tenants/delete-a-tenant)                      | Delete a tenant            |

### Users

| Tool                                                                                                                                  | Description                                         |
| ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [`get_user_preferences`](/api-reference/user-preferences/get-users-preferences)                                                       | Get a user's notification preferences               |
| [`update_user_preference_topic`](/api-reference/user-preferences/update-or-create-user-preferences-for-a-specific-subscription-topic) | Update a user's preference for a subscription topic |
| [`list_user_tenants`](/api-reference/user-tenants/get-tenants-associated-with-a-given-user)                                           | List all tenants a user belongs to                  |
| [`add_user_to_tenant`](/api-reference/user-tenants/add-a-user-to-a-single-tenant)                                                     | Add a user to a tenant                              |
| [`remove_user_from_tenant`](/api-reference/user-tenants/remove-user-from-a-tenant)                                                    | Remove a user from a tenant                         |

### Translations

| Tool                                                                              | Description                    |
| --------------------------------------------------------------------------------- | ------------------------------ |
| [`get_translation`](/api-reference/translations/get-a-translation)                | Get a translation for a locale |
| [`update_translation`](/api-reference/translations/update-translations-by-locale) | Create or update a translation |

### Inbound

| Tool                                                                | Description                                         |
| ------------------------------------------------------------------- | --------------------------------------------------- |
| [`track_inbound_event`](/api-reference/inbound/courier-track-event) | Track an inbound event that can trigger automations |

### Audit Events

| Tool                                                                    | Description                |
| ----------------------------------------------------------------------- | -------------------------- |
| [`get_audit_event`](/api-reference/audit-events/get-an-audit-event)     | Get a specific audit event |
| [`list_audit_events`](/api-reference/audit-events/get-all-audit-events) | List audit events          |

### Utility

| Tool                         | Description                                 |
| ---------------------------- | ------------------------------------------- |
| `courier_installation_guide` | Get SDK installation guide for any platform |

### Diagnostic (local installs only)

| Tool                     | Description                                                                 |
| ------------------------ | --------------------------------------------------------------------------- |
| `get_environment_config` | Check which API key, base URL, and package version the MCP session is using |

## Error Handling

All tools return structured error responses when something goes wrong. Errors from the Courier API include the HTTP status code and message:

```json  theme={null}
{
  "error": true,
  "status": 404,
  "message": "Profile not found"
}
```

Common error codes: `400` (bad request), `401` (invalid API key), `404` (resource not found), `429` (rate limited).

## What's Next

<CardGroup cols={2}>
  <Card title="AI Developer Tools" icon="wand-magic-sparkles" href="/tools/ai-onboarding">
    Overview of all Courier AI tools
  </Card>

  <Card title="CLI" icon="terminal" href="/tools/cli">
    Courier CLI for terminal workflows
  </Card>

  <Card title="Courier Skills" icon="brain" href="/tools/courier-skills">
    Best-practice guides for AI agents
  </Card>

  <Card title="API Reference" icon="book" href="/reference/get-started">
    Full Courier API documentation
  </Card>
</CardGroup>
