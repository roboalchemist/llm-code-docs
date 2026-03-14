# Source: https://docs.airbyte.com/integrations/sources/watchmode.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-watchmode/latest/icon.svg)

# Watchmode

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.31](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-watchmode)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-watchmode)(last updated 2 days ago)

* Definition ID

  `c10bae9d-398b-480a-a49b-5ae69cdc0759`

Website: <https://watchmode.com/> API Reference: <https://api.watchmode.com/docs>

## Configuration[​](#configuration "Direct link to Configuration")

| Input        | Type     | Description                                                                                                                                    | Default Value |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `api_key`    | `string` | API Key. Your API key for authenticating with the Watchmode API. You can request a free API key at <https://api.watchmode.com/requestApiKey/>. |               |
| `search_val` | `string` | Search Value. The name value for search stream                                                                                                 | Terminator    |
| `start_date` | `string` | Start date.                                                                                                                                    |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name          | Primary Key | Pagination       | Supports Full Sync | Supports Incremental |
| -------------------- | ----------- | ---------------- | ------------------ | -------------------- |
| sources              | id          | DefaultPaginator | ✅                 | ❌                   |
| regions              | uuid        | DefaultPaginator | ✅                 | ❌                   |
| networks             | id          | No pagination    | ✅                 | ❌                   |
| genres               | id          | DefaultPaginator | ✅                 | ❌                   |
| search               | id          | DefaultPaginator | ✅                 | ❌                   |
| autocomplete\_search | id          | DefaultPaginator | ✅                 | ❌                   |
| titles               | id          | DefaultPaginator | ✅                 | ❌                   |
| releases             | id          | DefaultPaginator | ✅                 | ✅                   |

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

API Key

required

string

api\_key

›

Search Value

required

string

search\_val

›

Start date

required

string

start\_date

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                               |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 0.0.31  | 2026-03-10 | [74508](https://github.com/airbytehq/airbyte/pull/74508) | Update dependencies                                                                   |
| 0.0.30  | 2026-02-24 | [73921](https://github.com/airbytehq/airbyte/pull/73921) | Update dependencies                                                                   |
| 0.0.29  | 2026-02-17 | [73436](https://github.com/airbytehq/airbyte/pull/73436) | Update dependencies                                                                   |
| 0.0.28  | 2026-02-03 | [72657](https://github.com/airbytehq/airbyte/pull/72657) | Update dependencies                                                                   |
| 0.0.27  | 2026-01-20 | [71493](https://github.com/airbytehq/airbyte/pull/71493) | Update dependencies                                                                   |
| 0.0.26  | 2025-12-18 | [70688](https://github.com/airbytehq/airbyte/pull/70688) | Update dependencies                                                                   |
| 0.0.25  | 2025-11-25 | [70168](https://github.com/airbytehq/airbyte/pull/70168) | Update dependencies                                                                   |
| 0.0.24  | 2025-11-18 | [69703](https://github.com/airbytehq/airbyte/pull/69703) | Update dependencies                                                                   |
| 0.0.23  | 2025-10-29 | [68934](https://github.com/airbytehq/airbyte/pull/68934) | Update dependencies                                                                   |
| 0.0.22  | 2025-10-21 | [68367](https://github.com/airbytehq/airbyte/pull/68367) | Update dependencies                                                                   |
| 0.0.21  | 2025-10-14 | [67969](https://github.com/airbytehq/airbyte/pull/67969) | Update dependencies                                                                   |
| 0.0.20  | 2025-10-07 | [67327](https://github.com/airbytehq/airbyte/pull/67327) | Update dependencies                                                                   |
| 0.0.19  | 2025-10-01 | [66449](https://github.com/airbytehq/airbyte/pull/66449) | Update dependencies                                                                   |
| 0.0.18  | 2025-09-09 | [65681](https://github.com/airbytehq/airbyte/pull/65681) | Update dependencies                                                                   |
| 0.0.17  | 2025-08-24 | [65478](https://github.com/airbytehq/airbyte/pull/65478) | Update dependencies                                                                   |
| 0.0.16  | 2025-08-10 | [64815](https://github.com/airbytehq/airbyte/pull/64815) | Update dependencies                                                                   |
| 0.0.15  | 2025-08-02 | [64380](https://github.com/airbytehq/airbyte/pull/64380) | Update dependencies                                                                   |
| 0.0.14  | 2025-07-26 | [64059](https://github.com/airbytehq/airbyte/pull/64059) | Update dependencies                                                                   |
| 0.0.13  | 2025-07-20 | [63692](https://github.com/airbytehq/airbyte/pull/63692) | Update dependencies                                                                   |
| 0.0.12  | 2025-07-12 | [63160](https://github.com/airbytehq/airbyte/pull/63160) | Update dependencies                                                                   |
| 0.0.11  | 2025-07-05 | [62752](https://github.com/airbytehq/airbyte/pull/62752) | Update dependencies                                                                   |
| 0.0.10  | 2025-06-28 | [62228](https://github.com/airbytehq/airbyte/pull/62228) | Update dependencies                                                                   |
| 0.0.9   | 2025-06-21 | [61755](https://github.com/airbytehq/airbyte/pull/61755) | Update dependencies                                                                   |
| 0.0.8   | 2025-06-15 | [61254](https://github.com/airbytehq/airbyte/pull/61254) | Update dependencies                                                                   |
| 0.0.7   | 2025-05-24 | [60740](https://github.com/airbytehq/airbyte/pull/60740) | Update dependencies                                                                   |
| 0.0.6   | 2025-05-10 | [59975](https://github.com/airbytehq/airbyte/pull/59975) | Update dependencies                                                                   |
| 0.0.5   | 2025-05-04 | [59528](https://github.com/airbytehq/airbyte/pull/59528) | Update dependencies                                                                   |
| 0.0.4   | 2025-04-26 | [58959](https://github.com/airbytehq/airbyte/pull/58959) | Update dependencies                                                                   |
| 0.0.3   | 2025-04-19 | [58562](https://github.com/airbytehq/airbyte/pull/58562) | Update dependencies                                                                   |
| 0.0.2   | 2025-04-12 | [58020](https://github.com/airbytehq/airbyte/pull/58020) | Update dependencies                                                                   |
| 0.0.1   | 2025-04-05 | [57406](https://github.com/airbytehq/airbyte/pull/57406) | Initial release by [@btkcodedev](https://github.com/btkcodedev) via Connector Builder |
