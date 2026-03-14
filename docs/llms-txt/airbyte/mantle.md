# Source: https://docs.airbyte.com/integrations/sources/mantle.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-mantle/latest/icon.svg)

# Mantle

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.17](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-mantle)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-mantle)(last updated 23 days ago)

* Definition ID

  `da48299b-4afa-46b4-bb9d-e1ade37e7169`

This connector use the Mantle API to get customers and subscriptions streams

## Configuration[​](#configuration "Direct link to Configuration")

| Input        | Type     | Description | Default Value |
| ------------ | -------- | ----------- | ------------- |
| `api_key`    | `string` | API Key.    |               |
| `start_date` | `string` | Start date. |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name   | Primary Key | Pagination       | Supports Full Sync | Supports Incremental |
| ------------- | ----------- | ---------------- | ------------------ | -------------------- |
| customers     | id          | DefaultPaginator | ✅                 | ✅                   |
| subscriptions | id          | DefaultPaginator | ✅                 | ✅                   |

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

API Key

required

string

api\_key

›

Start date

required

string

start\_date

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                       |
| ------- | ---------- | -------------------------------------------------------- | ----------------------------------------------------------------------------- |
| 0.0.17  | 2026-02-17 | [73394](https://github.com/airbytehq/airbyte/pull/73394) | Update dependencies                                                           |
| 0.0.16  | 2026-02-10 | [73189](https://github.com/airbytehq/airbyte/pull/73189) | Update dependencies                                                           |
| 0.0.15  | 2026-02-03 | [72724](https://github.com/airbytehq/airbyte/pull/72724) | Update dependencies                                                           |
| 0.0.14  | 2026-01-20 | [72009](https://github.com/airbytehq/airbyte/pull/72009) | Update dependencies                                                           |
| 0.0.13  | 2026-01-14 | [71544](https://github.com/airbytehq/airbyte/pull/71544) | Update dependencies                                                           |
| 0.0.12  | 2025-12-18 | [70750](https://github.com/airbytehq/airbyte/pull/70750) | Update dependencies                                                           |
| 0.0.11  | 2025-11-25 | [70132](https://github.com/airbytehq/airbyte/pull/70132) | Update dependencies                                                           |
| 0.0.10  | 2025-11-18 | [69545](https://github.com/airbytehq/airbyte/pull/69545) | Update dependencies                                                           |
| 0.0.9   | 2025-10-29 | [69069](https://github.com/airbytehq/airbyte/pull/69069) | Update dependencies                                                           |
| 0.0.8   | 2025-10-21 | [68445](https://github.com/airbytehq/airbyte/pull/68445) | Update dependencies                                                           |
| 0.0.7   | 2025-10-14 | [67809](https://github.com/airbytehq/airbyte/pull/67809) | Update dependencies                                                           |
| 0.0.6   | 2025-10-07 | [67377](https://github.com/airbytehq/airbyte/pull/67377) | Update dependencies                                                           |
| 0.0.5   | 2025-09-30 | [66339](https://github.com/airbytehq/airbyte/pull/66339) | Update dependencies                                                           |
| 0.0.4   | 2025-09-09 | [65746](https://github.com/airbytehq/airbyte/pull/65746) | Update dependencies                                                           |
| 0.0.3   | 2025-09-07 | [65150](https://github.com/airbytehq/airbyte/pull/65150) | Fix pagination for Subscriptions                                              |
| 0.0.2   | 2025-08-23 | [65182](https://github.com/airbytehq/airbyte/pull/65182) | Update dependencies                                                           |
| 0.0.1   | 2025-08-13 |                                                          | Initial release by [@KimPlv](https://github.com/KimPlv) via Connector Builder |
