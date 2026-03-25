# Source: https://docs.airbyte.com/integrations/sources/outlook.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-outlook/latest/icon.svg)

# Outlook

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.14](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-outlook)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-outlook)(last updated 2 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `886bdbfe-7935-4d96-b097-e3c1db73b951`

Outlook is the email service provided by Microsoft. This connector enables you to sync emails, mailboxes, and conversations from Microsoft Outlook/Exchange Online using Microsoft Graph API with delegated permissions for multi-tenant support.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

To use this connector, you need:

* A Microsoft Entra ID (formerly Azure AD) tenant
* An account with at least the Cloud Application Administrator role
* An Azure App Registration with the required API permissions

## Setup Guide[​](#setup-guide "Direct link to Setup Guide")

### Step 1: Register an Application in Azure[​](#step-1-register-an-application-in-azure "Direct link to Step 1: Register an Application in Azure")

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com)

2. Navigate to **Identity** > **Applications** > **App registrations**

3. Select **New registration**

4. Enter a display name for your application (for example, "Airbyte Outlook Connector")

5. Under **Supported account types**, select the appropriate option:

   <!-- -->

   * **Accounts in this organizational directory only**: Single-tenant (your organization only)
   * **Accounts in any organizational directory**: Multi-tenant (any Microsoft Entra organization)
   * **Accounts in any organizational directory and personal Microsoft accounts**: Multi-tenant with personal accounts

6. Leave **Redirect URI** blank for now (you'll configure this in Step 3)

7. Click **Register**

After registration, note the **Application (client) ID** displayed on the Overview page.

### Step 2: Configure API Permissions[​](#step-2-configure-api-permissions "Direct link to Step 2: Configure API Permissions")

The connector requires the following Microsoft Graph API permissions:

1. In your app registration, navigate to **API permissions**

2. Click **Add a permission** > **Microsoft Graph** > **Delegated permissions**

3. Add the following permissions:

   <!-- -->

   * `Mail.Read`: Allows the app to read the signed-in user's mailbox. This permission is required to access email messages and their attachments.
   * `User.Read`: Allows users to sign in to the app and allows the app to read the profile of signed-in users.

4. Click **Add permissions**

**Note**: Admin consent is not required for `Mail.Read` delegated permission when used with the signed-in user's own mailbox. However, your organization's policies may require admin consent for all permissions.

For more information about these permissions, see the [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

### Step 3: Configure Redirect URI[​](#step-3-configure-redirect-uri "Direct link to Step 3: Configure Redirect URI")

1. In your app registration, navigate to **Authentication**
2. Under **Platform configurations**, click **Add a platform**
3. Select **Web**
4. Enter the redirect URI provided by Airbyte during the OAuth configuration process
5. Click **Configure**

The redirect URI is where Microsoft will send the authentication response after the user signs in. Airbyte provides this URI when you configure the connector.

### Step 4: Create a Client Secret[​](#step-4-create-a-client-secret "Direct link to Step 4: Create a Client Secret")

1. In your app registration, navigate to **Certificates & secrets**
2. Under **Client secrets**, click **New client secret**
3. Add a description (for example, "Airbyte Outlook Connector Secret")
4. Select an expiration period (Microsoft recommends less than 12 months)
5. Click **Add**
6. **Important**: Copy the secret value immediately. This value is never displayed again after you leave this page.

### Step 5: Obtain OAuth Credentials[​](#step-5-obtain-oauth-credentials "Direct link to Step 5: Obtain OAuth Credentials")

To obtain the refresh token needed for Airbyte configuration:

1. Use the OAuth 2.0 authorization flow with your Client ID and Client Secret
2. Request the following scopes: `https://graph.microsoft.com/Mail.Read https://graph.microsoft.com/User.Read offline_access`
3. After user consent, exchange the authorization code for an access token and refresh token
4. Save the refresh token for use in Airbyte configuration

For detailed instructions on the OAuth flow, see [Get access on behalf of a user](https://learn.microsoft.com/en-us/graph/auth-v2-user).

## Configuration[​](#configuration "Direct link to Configuration")

| Input           | Type     | Description                                                                                     | Default Value |
| --------------- | -------- | ----------------------------------------------------------------------------------------------- | ------------- |
| `client_id`     | `string` | OAuth Client ID. The Client ID of your Microsoft Azure application                              |               |
| `tenant_id`     | `string` | Tenant ID (Optional). Azure AD Tenant ID (optional for multi-tenant apps, defaults to 'common') | common        |
| `client_secret` | `string` | OAuth Client Secret. The Client Secret of your Microsoft Azure application                      |               |
| `refresh_token` | `string` | Refresh Token. Refresh token obtained from Microsoft OAuth flow                                 |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name       | Primary Key    | Pagination       | Supports Full Sync | Supports Incremental |
| ----------------- | -------------- | ---------------- | ------------------ | -------------------- |
| profile           |                | No pagination    | ✅                 | ❌                   |
| mailboxes         | id             | DefaultPaginator | ✅                 | ❌                   |
| messages          | id             | DefaultPaginator | ✅                 | ❌                   |
| messages\_details | id             | No pagination    | ✅                 | ❌                   |
| conversations     | conversationId | DefaultPaginator | ✅                 | ❌                   |

### Stream Details[​](#stream-details "Direct link to Stream Details")

`messages`: Retrieves all messages from the signed-in user's mailbox using the `/me/messages` endpoint. This stream fetches messages from all folders including Inbox, Sent Items, Deleted Items, and other mail folders.

`mailboxes`: Retrieves information about mail folders in the user's mailbox.

`profile`: Retrieves the signed-in user's profile information.

`conversations`: Retrieves conversation threads from the user's mailbox.

`messages_details`: Retrieves detailed information for individual messages.

## Filtering and Limitations[​](#filtering-and-limitations "Direct link to Filtering and Limitations")

This connector does not currently support filtering emails by specific criteria such as:

* Specific mailbox or folder path
* Email subject
* Sender or recipient
* Date ranges

The connector retrieves all messages from the signed-in user's mailbox via the `/me/messages` endpoint. The Microsoft Graph API does support filtering via OData query parameters (such as `$filter`), but these are not currently exposed as configuration options in this connector.

To filter messages after extraction, you can:

* Use [Airbyte Mappings](/platform/using-airbyte/mappings.md) to filter rows based on field values
* Apply filters in your data warehouse or transformation tool after sync
* Use the Microsoft Graph API directly with custom filtering parameters

For more information about Microsoft Graph Mail API capabilities, see the [Microsoft Graph Mail API documentation](https://learn.microsoft.com/en-us/graph/api/user-list-messages).

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

OAuth Client ID

required

string

client\_id

›

OAuth Client Secret

required

string

client\_secret

›

Refresh Token

required

string

refresh\_token

›

Tenant ID (Optional)

string

tenant\_id

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                                           |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 0.0.15  | 2026-03-03 | [73816](https://github.com/airbytehq/airbyte/pull/73816) | Update dependencies                                                                               |
| 0.0.14  | 2026-01-20 | [72166](https://github.com/airbytehq/airbyte/pull/72166) | Update dependencies                                                                               |
| 0.0.13  | 2026-01-14 | [71676](https://github.com/airbytehq/airbyte/pull/71676) | Update dependencies                                                                               |
| 0.0.12  | 2025-12-18 | [70526](https://github.com/airbytehq/airbyte/pull/70526) | Update dependencies                                                                               |
| 0.0.11  | 2025-11-25 | [70123](https://github.com/airbytehq/airbyte/pull/70123) | Update dependencies                                                                               |
| 0.0.10  | 2025-11-18 | [69707](https://github.com/airbytehq/airbyte/pull/69707) | Update dependencies                                                                               |
| 0.0.9   | 2025-10-29 | [69010](https://github.com/airbytehq/airbyte/pull/69010) | Update dependencies                                                                               |
| 0.0.8   | 2025-10-21 | [68311](https://github.com/airbytehq/airbyte/pull/68311) | Update dependencies                                                                               |
| 0.0.7   | 2025-10-14 | [67772](https://github.com/airbytehq/airbyte/pull/67772) | Update dependencies                                                                               |
| 0.0.6   | 2025-10-07 | [67343](https://github.com/airbytehq/airbyte/pull/67343) | Update dependencies                                                                               |
| 0.0.5   | 2025-09-30 | [66389](https://github.com/airbytehq/airbyte/pull/66389) | Update dependencies                                                                               |
| 0.0.4   | 2025-09-09 | [65826](https://github.com/airbytehq/airbyte/pull/65826) | Update dependencies                                                                               |
| 0.0.3   | 2025-08-23 | [65161](https://github.com/airbytehq/airbyte/pull/65161) | Update dependencies                                                                               |
| 0.0.2   | 2025-08-15 | [64942](https://github.com/airbytehq/airbyte/pull/64942) | Fix docker image entrypoint for platform syncs                                                    |
| 0.0.1   | 2025-08-14 |                                                          | Initial release by [@saif-qureshi-341](https://github.com/saif-qureshi-341) via Connector Builder |
