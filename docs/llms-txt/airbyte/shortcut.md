# Source: https://docs.airbyte.com/integrations/sources/shortcut.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-shortcut/latest/icon.svg)

# Shortcut

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.43](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-shortcut)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-shortcut)(last updated 23 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `72b4b6ad-bf46-4113-a97e-c8e2666f7230`

This page contains the setup guide and reference information for the [Shortcut](https://app.shortcut.com/) source connector.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

To set up the shortcut source connector with Airbyte, you'll need to create your API tokens from theie settings page. Please visit `https://app.shortcut.com/janfab/settings/account/api-tokens` for getting your api\_key.

## Documentation reference:[​](#documentation-reference "Direct link to Documentation reference:")

Visit `https://developer.shortcut.com/api/rest/v3#Introduction` for API documentation

## Authentication setup[​](#authentication-setup "Direct link to Authentication setup")

Refer `https://developer.shortcut.com/api/rest/v3#Authentication` for more details.

## Configuration[​](#configuration "Direct link to Configuration")

| Input        | Type     | Description                                                                                                                                      | Default Value                        |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| `api_key_2`  | `string` | API Key.                                                                                                                                         |                                      |
| `start_date` | `string` | Start date.                                                                                                                                      |                                      |
| `query`      | `string` | Query. Query for searching as defined in `https://help.shortcut.com/hc/en-us/articles/360000046646-Searching-in-Shortcut-Using-Search-Operators` | title<!-- -->:Our<!-- --> first Epic |

## Streams[​](#streams "Direct link to Streams")

| Stream Name            | Primary Key | Pagination       | Supports Full Sync | Supports Incremental |
| ---------------------- | ----------- | ---------------- | ------------------ | -------------------- |
| search\_epics          | id          | DefaultPaginator | ✅                 | ✅                   |
| categories             | id          | No pagination    | ✅                 | ✅                   |
| categories\_milestones | id          | No pagination    | ✅                 | ✅                   |
| categories\_objectives | id          | No pagination    | ✅                 | ✅                   |
| custom-fields          | id          | No pagination    | ✅                 | ✅                   |
| epic-workflow          | id          | No pagination    | ✅                 | ✅                   |
| epics                  | id          | No pagination    | ✅                 | ✅                   |
| epics\_comments        | id          | No pagination    | ✅                 | ✅                   |
| epics\_stories         | id          | No pagination    | ✅                 | ✅                   |
| files                  | id          | No pagination    | ✅                 | ✅                   |
| groups                 | id          | No pagination    | ✅                 | ❌                   |
| groups\_stories        | id          | No pagination    | ✅                 | ✅                   |
| iterations             | id          | No pagination    | ✅                 | ✅                   |
| iterations\_stories    | id          | No pagination    | ✅                 | ✅                   |
| labels                 | id          | No pagination    | ✅                 | ✅                   |
| member                 | id          | No pagination    | ✅                 | ❌                   |
| members                | id          | No pagination    | ✅                 | ✅                   |
| milestones             | id          | No pagination    | ✅                 | ✅                   |
| milestones\_epics      | id          | No pagination    | ✅                 | ✅                   |
| objectives             | id          | No pagination    | ✅                 | ✅                   |
| objectives\_epics      | id          | No pagination    | ✅                 | ✅                   |
| workflows              | id          | No pagination    | ✅                 | ✅                   |
| stories\_comments      | id          | No pagination    | ✅                 | ✅                   |
| story\_history         | id          | No pagination    | ✅                 | ✅                   |

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

API Key

required

string

api\_key\_2

›

Start date

required

string

start\_date

›

Query

string

query

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                                                                                                                |
| ------- | ---------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.0.44  | 2026-03-03 | [74231](https://github.com/airbytehq/airbyte/pull/74231) | Update dependencies                                                                                                                                                    |
| 0.0.43  | 2026-02-17 | [72725](https://github.com/airbytehq/airbyte/pull/72725) | Update dependencies                                                                                                                                                    |
| 0.0.42  | 2026-01-20 | [71658](https://github.com/airbytehq/airbyte/pull/71658) | Update dependencies                                                                                                                                                    |
| 0.0.41  | 2025-12-18 | [70703](https://github.com/airbytehq/airbyte/pull/70703) | Update dependencies                                                                                                                                                    |
| 0.0.40  | 2025-11-25 | [70108](https://github.com/airbytehq/airbyte/pull/70108) | Update dependencies                                                                                                                                                    |
| 0.0.39  | 2025-11-18 | [69486](https://github.com/airbytehq/airbyte/pull/69486) | Update dependencies                                                                                                                                                    |
| 0.0.38  | 2025-10-29 | [68807](https://github.com/airbytehq/airbyte/pull/68807) | Update dependencies                                                                                                                                                    |
| 0.0.37  | 2025-10-21 | [68232](https://github.com/airbytehq/airbyte/pull/68232) | Update dependencies                                                                                                                                                    |
| 0.0.36  | 2025-10-14 | [67743](https://github.com/airbytehq/airbyte/pull/67743) | Update dependencies                                                                                                                                                    |
| 0.0.35  | 2025-10-07 | [67439](https://github.com/airbytehq/airbyte/pull/67439) | Update dependencies                                                                                                                                                    |
| 0.0.34  | 2025-09-30 | [66907](https://github.com/airbytehq/airbyte/pull/66907) | Update dependencies                                                                                                                                                    |
| 0.0.33  | 2025-09-24 | [66258](https://github.com/airbytehq/airbyte/pull/66258) | Update dependencies                                                                                                                                                    |
| 0.0.32  | 2025-09-09 | [65699](https://github.com/airbytehq/airbyte/pull/65699) | Update dependencies                                                                                                                                                    |
| 0.0.31  | 2025-08-24 | [65392](https://github.com/airbytehq/airbyte/pull/65392) | Update dependencies                                                                                                                                                    |
| 0.0.30  | 2025-08-16 | [64992](https://github.com/airbytehq/airbyte/pull/64992) | Update dependencies                                                                                                                                                    |
| 0.0.29  | 2025-08-03 | [64471](https://github.com/airbytehq/airbyte/pull/64471) | Update dependencies                                                                                                                                                    |
| 0.0.28  | 2025-06-28 | [62293](https://github.com/airbytehq/airbyte/pull/62293) | Update dependencies                                                                                                                                                    |
| 0.0.27  | 2025-06-21 | [61821](https://github.com/airbytehq/airbyte/pull/61821) | Update dependencies                                                                                                                                                    |
| 0.0.26  | 2025-06-14 | [61307](https://github.com/airbytehq/airbyte/pull/61307) | Update dependencies                                                                                                                                                    |
| 0.0.25  | 2025-05-25 | [60582](https://github.com/airbytehq/airbyte/pull/60582) | Update dependencies                                                                                                                                                    |
| 0.0.24  | 2025-05-10 | [60060](https://github.com/airbytehq/airbyte/pull/60060) | Update dependencies                                                                                                                                                    |
| 0.0.23  | 2025-05-04 | [59632](https://github.com/airbytehq/airbyte/pull/59632) | Update dependencies                                                                                                                                                    |
| 0.0.22  | 2025-04-27 | [58994](https://github.com/airbytehq/airbyte/pull/58994) | Update dependencies                                                                                                                                                    |
| 0.0.21  | 2025-04-19 | [58444](https://github.com/airbytehq/airbyte/pull/58444) | Update dependencies                                                                                                                                                    |
| 0.0.20  | 2025-04-12 | [58008](https://github.com/airbytehq/airbyte/pull/58008) | Update dependencies                                                                                                                                                    |
| 0.0.19  | 2025-04-05 | [57413](https://github.com/airbytehq/airbyte/pull/57413) | Update dependencies                                                                                                                                                    |
| 0.0.18  | 2025-03-29 | [56896](https://github.com/airbytehq/airbyte/pull/56896) | Update dependencies                                                                                                                                                    |
| 0.0.17  | 2025-03-22 | [56248](https://github.com/airbytehq/airbyte/pull/56248) | Update dependencies                                                                                                                                                    |
| 0.0.16  | 2025-03-08 | [55632](https://github.com/airbytehq/airbyte/pull/55632) | Update dependencies                                                                                                                                                    |
| 0.0.15  | 2025-03-01 | [55079](https://github.com/airbytehq/airbyte/pull/55079) | Update dependencies                                                                                                                                                    |
| 0.0.14  | 2025-02-22 | [54524](https://github.com/airbytehq/airbyte/pull/54524) | Update dependencies                                                                                                                                                    |
| 0.0.13  | 2025-02-15 | [54072](https://github.com/airbytehq/airbyte/pull/54072) | Update dependencies                                                                                                                                                    |
| 0.0.12  | 2025-02-08 | [53585](https://github.com/airbytehq/airbyte/pull/53585) | Update dependencies                                                                                                                                                    |
| 0.0.11  | 2025-02-01 | [53110](https://github.com/airbytehq/airbyte/pull/53110) | Update dependencies                                                                                                                                                    |
| 0.0.10  | 2025-01-25 | [52393](https://github.com/airbytehq/airbyte/pull/52393) | Update dependencies                                                                                                                                                    |
| 0.0.9   | 2025-01-18 | [51998](https://github.com/airbytehq/airbyte/pull/51998) | Update dependencies                                                                                                                                                    |
| 0.0.8   | 2025-01-11 | [51451](https://github.com/airbytehq/airbyte/pull/51451) | Update dependencies                                                                                                                                                    |
| 0.0.7   | 2024-12-28 | [50759](https://github.com/airbytehq/airbyte/pull/50759) | Update dependencies                                                                                                                                                    |
| 0.0.6   | 2024-12-21 | [50353](https://github.com/airbytehq/airbyte/pull/50353) | Update dependencies                                                                                                                                                    |
| 0.0.5   | 2024-12-14 | [49788](https://github.com/airbytehq/airbyte/pull/49788) | Update dependencies                                                                                                                                                    |
| 0.0.4   | 2024-12-12 | [49440](https://github.com/airbytehq/airbyte/pull/49440) | Update dependencies                                                                                                                                                    |
| 0.0.3   | 2024-12-11 | [49120](https://github.com/airbytehq/airbyte/pull/49120) | Starting with this version, the Docker image is now rootless. Please note that this and future versions will not be compatible with Airbyte versions earlier than 0.64 |
| 0.0.2   | 2024-11-04 | [47658](https://github.com/airbytehq/airbyte/pull/47658) | Update dependencies                                                                                                                                                    |
| 0.0.1   | 2024-09-05 | [45176](https://github.com/airbytehq/airbyte/pull/45176) | Initial release by [@btkcodedev](https://github.com/btkcodedev) via Connector Builder                                                                                  |
