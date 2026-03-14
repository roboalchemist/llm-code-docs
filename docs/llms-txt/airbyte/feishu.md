# Source: https://docs.airbyte.com/integrations/sources/feishu.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-feishu/latest/icon.svg)

# Feishu

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.2](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-feishu)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-feishu)(last updated 16 days ago)

* Definition ID

  `3f1aa18a-a111-4e3b-8cac-9b79a091cc13`

This page contains the setup guide and reference information for the [Feishu](https://www.feishu.cn/) (also known as [Lark](https://www.larksuite.com/)) source connector.

The Feishu source connector syncs records from a [Feishu/Lark Bitable](https://www.feishu.cn/product/bitable) (Base) table using the Feishu Open Platform API.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* A [Feishu](https://www.feishu.cn/) or [Lark](https://www.larksuite.com/) account
* A custom app created in the [Feishu Open Platform](https://open.feishu.cn/) (or [Lark Developer](https://open.larksuite.com/)) with Bitable read permissions
* The **App ID** and **App Secret** for that custom app
* A Bitable (Base) with at least one table you want to sync

## Setup guide[​](#setup-guide "Direct link to Setup guide")

### Step 1: Create a custom app in the Feishu Open Platform[​](#step-1-create-a-custom-app-in-the-feishu-open-platform "Direct link to Step 1: Create a custom app in the Feishu Open Platform")

1. Go to the [Feishu Open Platform Developer Console](https://open.feishu.cn/app) (or [Lark Developer Console](https://open.larksuite.com/app) for international accounts).
2. Click **Create Custom App** and fill in the app name and description.
3. After creation, navigate to **Credentials & Basic Info** to find your **App ID** and **App Secret**.

### Step 2: Grant Bitable permissions[​](#step-2-grant-bitable-permissions "Direct link to Step 2: Grant Bitable permissions")

1. In your custom app's settings, go to **Permissions & Scopes**.
2. Add the Bitable-related scopes required for reading records (for example, `bitable:app:readonly` or `bitable:app`).
3. Publish the app or submit it for review, depending on your organization's requirements.

### Step 3: Find your Bitable App Token and Table ID[​](#step-3-find-your-bitable-app-token-and-table-id "Direct link to Step 3: Find your Bitable App Token and Table ID")

1. Open the Bitable (Base) you want to sync in your browser.
2. The **App Token** is in the URL path: `https://your-domain.feishu.cn/base/{app_token}`.
3. The **Table ID** is in the URL query parameter: `?table={table_id}`.

### Step 4: Set up the connector in Airbyte[​](#step-4-set-up-the-connector-in-airbyte "Direct link to Step 4: Set up the connector in Airbyte")

1. In Airbyte, go to **Sources** and select **Feishu**.
2. Enter the **App ID** and **App Secret** from Step 1.
3. Enter the **App Token** and **Table ID** from Step 3.
4. If you use Lark (international), change the **Lark Host** to `https://open.larksuite.com`. The default (`https://open.feishu.cn`) is for Feishu (China mainland).
5. Optionally adjust the **Page Size** (default: 100, maximum: 500).
6. Click **Set up source**.

## Supported sync modes[​](#supported-sync-modes "Direct link to Supported sync modes")

The Feishu source connector supports the following [sync modes](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/):

* [Full Refresh - Overwrite](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite)
* [Full Refresh - Append](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-append)

## Supported streams[​](#supported-streams "Direct link to Supported streams")

| Stream  | Primary key | Pagination                  | Incremental |
| ------- | ----------- | --------------------------- | ----------- |
| records | `record_id` | Cursor-based (`page_token`) | No          |

The **records** stream returns all records from the specified Bitable table. Each record includes a `record_id`, an optional `id`, and a `fields` object containing the values for each column in the table. The structure of the `fields` object depends on the columns defined in your Bitable table.

## Limitations[​](#limitations "Direct link to Limitations")

* This connector syncs records from a single Bitable table per configured source. To sync multiple tables, create a separate source for each.
* Only full refresh sync is supported. Incremental sync is not available.

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

App Id

required

string

app\_id

›

App Secret

required

string

app\_secret

›

App Token

required

string

app\_token

›

Lark Host

required

string

lark\_host

›

Table Id

required

string

table\_id

›

Page Size

number

page\_size

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                         |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 0.0.2   | 2026-02-24 | [73777](https://github.com/airbytehq/airbyte/pull/73777) | Update dependencies                                                             |
| 0.0.1   | 2026-02-19 | [71256](https://github.com/airbytehq/airbyte/pull/71256) | Initial release by [@WYW-min](https://github.com/WYW-min) via Connector Builder |
