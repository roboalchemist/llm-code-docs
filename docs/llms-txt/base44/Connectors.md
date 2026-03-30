# Source: https://docs.base44.com/developers/references/sdk/docs/interfaces/connectors.md

# Source: https://docs.base44.com/developers/backend/resources/connectors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OAuth Connectors

> OAuth integrations for connecting your app to third-party services

<div className="dev-docs-banner">
  <div className="dev-docs-banner-content">
    <div className="dev-docs-banner-title">
      You're viewing developer documentation
    </div>

    <div className="dev-docs-banner-text">
      This documentation is for developers working with the Base44 developer platform. For information about connectors in the app editor, see <a href="/Integrations/Connectors">Using Connectors</a>.
    </div>
  </div>
</div>

Connectors are OAuth integrations that let your app connect to [third-party services](#supported-services). Use connectors to authenticate with external APIs and make calls with your app's credentials.

To get started:

1. [**Configure**](#configure) a JSONC file for each service you need
2. [**Deploy and authorize**](#deploy-and-authorize) via the CLI
3. [**Use in backend functions**](#use-in-backend-functions) by calling [`getConnection()`](/developers/references/sdk/docs/interfaces/connectors#getconnection) to retrieve OAuth tokens

## Configure

Each connector is a JSONC file in your project's connectors directory. The file defines the integration type and the OAuth scopes your app needs. By default the directory is `base44/connectors/`, but you can customize the path in your [project configuration](/developers/backend/overview/project-structure#config-jsonc).

<Tree>
  <Tree.Folder name="connectors" defaultOpen>
    <Tree.File name="googlecalendar.jsonc" />

    <Tree.File name="slack.jsonc" />

    <Tree.File name="slackbot.jsonc" />

    <Tree.File name="notion.jsonc" />
  </Tree.Folder>
</Tree>

### Example

This example configures a Google Calendar connector with read and event management scopes:

```jsonc  theme={null}
{
  "type": "googlecalendar",
  "scopes": [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/calendar.events",
  ],
}
```

### Field reference

<ResponseField name="type" type="string" required>
  The integration type identifier. Must be one of: `discord`, `github`, `gmail`, `googlebigquery`, `googlecalendar`, `googledocs`, `googledrive`, `googlesheets`, `googleslides`, `hubspot`, `linkedin`, `notion`, `salesforce`, `slack`, `slackbot`, or `tiktok`.

  Each connector type can only be defined once in your project.
</ResponseField>

<ResponseField name="scopes" type="array" required>
  Array of OAuth scopes required for your integration. The specific scopes
  depend on the external service and what operations your app needs to perform.
  See the [connector permissions and
  scopes](/Integrations/Connectors#connector-permissions) documentation for
  available scopes for each service.
</ResponseField>

## Deploy and authorize

Deploy connectors with [`connectors push`](/developers/references/cli/commands/connectors-push) or [`deploy`](/developers/references/cli/commands/deploy). To download existing connectors from Base44, use [`connectors pull`](/developers/references/cli/commands/connectors-pull).

When you push, the CLI prompts you to authorize each connector one by one. It suggests opening your browser automatically, and if you accept, it iterates through each integration's authorization page sequentially. After authorization completes, your OAuth tokens are stored securely and you can retrieve them using the SDK.

Authorization requires a browser-based OAuth flow and cannot be done programmatically from a backend function.

## Use in backend functions

Once deployed and authorized, retrieve connection details in your [backend functions](/developers/backend/resources/functions) using [`connectors.getConnection()`](/developers/references/sdk/docs/interfaces/connectors#getconnection). The returned object contains an `accessToken` for making authenticated API calls and, for some connectors, a `connectionConfig` with additional parameters (e.g. a subdomain or account ID).

### Example

This example retrieves a Google Calendar connection and fetches upcoming events:

```typescript  theme={null}
const { accessToken } =
  await base44.asServiceRole.connectors.getConnection("googlecalendar");

const timeMin = new Date().toISOString();
const url = `https://www.googleapis.com/calendar/v3/calendars/primary/events?maxResults=10&orderBy=startTime&singleEvents=true&timeMin=${timeMin}`;

const calendarResponse = await fetch(url, {
  headers: { Authorization: `Bearer ${accessToken}` },
});

const events = await calendarResponse.json();
```

## Supported services

Pass the type identifier to [`getConnection()`](/developers/references/sdk/docs/interfaces/connectors#getconnection) to retrieve a connection for any of these services:

| Service          | Type identifier    |
| ---------------- | ------------------ |
| Box              | `box`              |
| ClickUp          | `clickup`          |
| Discord          | `discord`          |
| GitHub           | `github`           |
| Gmail            | `gmail`            |
| Google Analytics | `google_analytics` |
| Google BigQuery  | `googlebigquery`   |
| Google Calendar  | `googlecalendar`   |
| Google Docs      | `googledocs`       |
| Google Drive     | `googledrive`      |
| Google Sheets    | `googlesheets`     |
| Google Slides    | `googleslides`     |
| HubSpot          | `hubspot`          |
| LinkedIn         | `linkedin`         |
| Notion           | `notion`           |
| Salesforce       | `salesforce`       |
| Slack User       | `slack`            |
| Slack Bot        | `slackbot`         |
| TikTok           | `tiktok`           |
| Wrike            | `wrike`            |

See the integration guides for more details:

* **Scopes and permissions**: [Gmail](/Integrations/gmail-connector#gmail-scopes-and-permissions), [LinkedIn](/Integrations/linkedin-connector#linkedin-scopes-and-permissions), [Slack](/Integrations/slack-connector#slack-scopes-and-permissions)
* **Slack connector types**: [About the Slack connectors](/Integrations/slack-connector#about-the-slack-connectors) explains the difference between `slack` and `slackbot`

## See also

* [connectors pull](/developers/references/cli/commands/connectors-pull)
* [connectors push](/developers/references/cli/commands/connectors-push)
* [deploy](/developers/references/cli/commands/deploy)
* [Backend Functions](/developers/backend/resources/functions)


Built with [Mintlify](https://mintlify.com).