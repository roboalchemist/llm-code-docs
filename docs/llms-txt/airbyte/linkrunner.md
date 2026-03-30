# Source: https://docs.airbyte.com/integrations/sources/linkrunner.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-linkrunner/latest/icon.svg)

# Linkrunner

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.1](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-linkrunner)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-linkrunner)(last updated 7 days ago)

* Definition ID

  `ec739bc6-f8a5-4cb3-9e7b-7e0f8f53ce74`

Linkrunner is a Mobile Measurement Partner (MMP) that helps track user journeys from first click to revenue generation. This connector extracts campaign data and attributed user analytics from Linkrunner's Data API, enabling comprehensive mobile attribution reporting and analysis. Supports filtering by campaign status, advertising channels (Google, Meta, TikTok), and time-based attribution data with automatic pagination and parent-child stream relationships.

## Configuration[​](#configuration "Direct link to Configuration")

| Input             | Type     | Description                                                                                             | Default Value |
| ----------------- | -------- | ------------------------------------------------------------------------------------------------------- | ------------- |
| `linkrunner-key`  | `string` | LinkRunner API Key. Your LinkRunner API key for authentication. Find this in your LinkRunner dashboard. |               |
| `filter`          | `string` | Campaign Filter. Filter campaigns by status (ALL, ACTIVE, or INACTIVE)                                  | ALL           |
| `channel`         | `string` | Channel Filter. Filter campaigns by marketing channel (leave empty for all channels)                    |               |
| `start_timestamp` | `string` | Start Date. Start date for fetching attributed users in ISO 8601 format (e.g., 2024-01-01T00:00:00Z)    |               |
| `end_timestamp`   | `string` | End Date. End date for fetching attributed users in ISO 8601 format. Leave empty for current date.      |               |
| `timezone`        | `string` | Timezone. Timezone for date filtering (default is UTC)                                                  | UTC           |

## Streams[​](#streams "Direct link to Streams")

| Stream Name       | Primary Key | Pagination       | Supports Full Sync | Supports Incremental |
| ----------------- | ----------- | ---------------- | ------------------ | -------------------- |
| campaigns         | display\_id | DefaultPaginator | ✅                 | ❌                   |
| attributed\_users |             | DefaultPaginator | ✅                 | ❌                   |

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

LinkRunner API Key

required

string

linkrunner-key

Channel Filter

string

channel

End Timestamp

string

end\_timestamp

›

Campaign Filter

string

filter

Start Timestamp

string

start\_timestamp

›

Timezone

string

timezone

## Changelog[​](#changelog "Direct link to Changelog")

The Linkrunner Airbyte Source Connector extracts campaign data and attributed user analytics from Linkrunner’s Data API, enabling end-to-end mobile attribution analysis from first click to user attribution events. It supports: Campaign-level filtering by status (ALL, ACTIVE, INACTIVE) Filtering by advertising channels (Google, Meta, TikTok) Attributed user data linked to campaigns via parent–child streams Time-based attribution windows with timezone support Automatic pagination for large datasets Reliable full-refresh syncs using Airbyte’s Declarative (low-code) framework This connector is ideal for building comprehensive mobile marketing and attribution analytics pipelines in Airbyte.

| Version | Date       | Pull Request                                             | Subject                                                                                     |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 0.0.2   | 2026-03-10 | [74423](https://github.com/airbytehq/airbyte/pull/74423) | Update dependencies                                                                         |
| 0.0.1   | 2026-02-06 |                                                          | Initial release by [@ChetanBhosale](https://github.com/ChetanBhosale) via Connector Builder |
