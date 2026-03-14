# Source: https://docs.airbyte.com/integrations/sources/tavus.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-tavus/latest/icon.svg)

# Tavus

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.29](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-tavus)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-tavus)(last updated 2 days ago)

* Definition ID

  `f2889d35-753f-4106-bce5-8a865bc339a6`

Website: <https://platform.tavus.io/> API Reference: <https://docs.tavus.io/api-reference/phoenix-replica-model/get-replicas>

## Configuration[​](#configuration "Direct link to Configuration")

| Input        | Type     | Description                                                                                     | Default Value |
| ------------ | -------- | ----------------------------------------------------------------------------------------------- | ------------- |
| `api_key`    | `string` | API Key. Your Tavus API key. You can find this in your Tavus account settings or API dashboard. |               |
| `start_date` | `string` | Start date.                                                                                     |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name   | Primary Key      | Pagination       | Supports Full Sync | Supports Incremental |
| ------------- | ---------------- | ---------------- | ------------------ | -------------------- |
| replicas      | replica\_id      | DefaultPaginator | ✅                 | ✅                   |
| videos        | video\_id        | DefaultPaginator | ✅                 | ❌                   |
| conversations | conversation\_id | DefaultPaginator | ✅                 | ✅                   |
| personas      | persona\_id      | DefaultPaginator | ✅                 | ✅                   |
| speeches      | speech\_id       | DefaultPaginator | ✅                 | ✅                   |

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

Start date

required

string

start\_date

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                              | Subject                                                                               |
| ------- | ---------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 0.0.29  | 2026-03-10 | [74581](https://github.com/airbytehq/airbyte/pull/74581)  | Update dependencies                                                                   |
| 0.0.28  | 2026-02-24 | [73834](https://github.com/airbytehq/airbyte/pull/73834)  | Update dependencies                                                                   |
| 0.0.27  | 2026-02-10 | [73126](https://github.com/airbytehq/airbyte/pull/73126)  | Update dependencies                                                                   |
| 0.0.26  | 2026-01-20 | [72107](https://github.com/airbytehq/airbyte/pull/72107)  | Update dependencies                                                                   |
| 0.0.25  | 2026-01-14 | [71577](https://github.com/airbytehq/airbyte/pull/71577)  | Update dependencies                                                                   |
| 0.0.24  | 2025-12-18 | [70603](https://github.com/airbytehq/airbyte/pull/70603)  | Update dependencies                                                                   |
| 0.0.23  | 2025-11-25 | [70044](https://github.com/airbytehq/airbyte/pull/70044)  | Update dependencies                                                                   |
| 0.0.22  | 2025-11-18 | [69555](https://github.com/airbytehq/airbyte/pull/69555)  | Update dependencies                                                                   |
| 0.0.21  | 2025-10-29 | [69013](https://github.com/airbytehq/airbyte/pull/69013)  | Update dependencies                                                                   |
| 0.0.20  | 2025-10-21 | [68540](https://github.com/airbytehq/airbyte/pull/68540)  | Update dependencies                                                                   |
| 0.0.19  | 2025-10-14 | [67875](https://github.com/airbytehq/airbyte/pull/67875)  | Update dependencies                                                                   |
| 0.0.18  | 2025-10-07 | [67457](https://github.com/airbytehq/airbyte/pull/67457)  | Update dependencies                                                                   |
| 0.0.17  | 2025-09-30 | [66878](https://github.com/airbytehq/airbyte/pull/66878)  | Update dependencies                                                                   |
| 0.0.16  | 2025-09-23 | [66358](https://github.com/airbytehq/airbyte/pull/66358)  | Update dependencies                                                                   |
| 0.0.15  | 2025-09-09 | [65677](https://github.com/airbytehq/airbyte/pull/65677)  | Update dependencies                                                                   |
| 0.0.14  | 2025-08-24 | [65433](https://github.com/airbytehq/airbyte/pull/65433)  | Update dependencies                                                                   |
| 0.0.13  | 2025-08-10 | [64810](https://github.com/airbytehq/airbyte/pull/64810)  | Update dependencies                                                                   |
| 0.0.12  | 2025-07-26 | [63970](https://github.com/airbytehq/airbyte/pull/63970)  | Update dependencies                                                                   |
| 0.0.11  | 2025-07-19 | [63649](https://github.com/airbytehq/airbyte/pull/63649)  | Update dependencies                                                                   |
| 0.0.10  | 2025-07-12 | [63071](https://github.com/airbytehq/airbyte/pull/63071)  | Update dependencies                                                                   |
| 0.0.9   | 2025-07-05 | [62728](https://github.com/airbytehq/airbyte/pull/62728)  | Update dependencies                                                                   |
| 0.0.8   | 2025-06-28 | [62209](https://github.com/airbytehq/airbyte/pull/62209)  | Update dependencies                                                                   |
| 0.0.7   | 2025-06-14 | [60446](https://github.com/airbytehq/airbyte/pull/60446)  | Update dependencies                                                                   |
| 0.0.6   | 2025-05-10 | [60137](https://github.com/airbytehq/airbyte/pull/60137)  | Update dependencies                                                                   |
| 0.0.5   | 2025-05-04 | [59607](https://github.com/airbytehq/airbyte/pull/59607)  | Update dependencies                                                                   |
| 0.0.4   | 2025-04-27 | [59000](https://github.com/airbytehq/airbyte/pull/59000)  | Update dependencies                                                                   |
| 0.0.3   | 2025-04-19 | [58383](https://github.com/airbytehq/airbyte/pull/58383)  | Update dependencies                                                                   |
| 0.0.2   | 2025-04-12 | [57929](https://github.com/airbytehq/airbyte/pull/57929)  | Update dependencies                                                                   |
| 0.0.1   | 2025-04-05 | [#57022](https://github.com/airbytehq/airbyte/pull/57022) | Initial release by [@btkcodedev](https://github.com/btkcodedev) via Connector Builder |
