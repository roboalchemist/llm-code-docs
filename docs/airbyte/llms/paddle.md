# Source: https://docs.airbyte.com/integrations/sources/paddle.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-paddle/latest/icon.svg)

# Paddle

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.2.13](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-paddle)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-paddle)(last updated a month ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `eb34e66a-c9b5-41ca-974f-2b82c26ae71a`

Website: <https://www.paddle.com/> API Reference: <https://developer.paddle.com/api-reference/overview>

## Configuration[​](#configuration "Direct link to Configuration")

| Input         | Type     | Description                                                                                                                                                                         | Default Value |
| ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `api_key`     | `string` | API Key. Your Paddle API key. You can generate it by navigating to Paddle > Developer tools > Authentication > Generate API key. Treat this key like a password and keep it secure. |               |
| `environment` | `string` | Environment. The environment for the Paddle API, either 'sandbox' or 'live'.                                                                                                        | api           |
| `start_date`  | `string` | Start date.                                                                                                                                                                         |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name         | Primary Key | Pagination       | Supports Full Sync | Supports Incremental |
| ------------------- | ----------- | ---------------- | ------------------ | -------------------- |
| adjustments         | id          | DefaultPaginator | ✅                 | ✅                   |
| customers           | id          | DefaultPaginator | ✅                 | ✅                   |
| customer\_addresses | id          | DefaultPaginator | ✅                 | ✅                   |
| discounts           | id          | DefaultPaginator | ✅                 | ✅                   |
| prices              | id          | DefaultPaginator | ✅                 | ✅                   |
| products            | id          | DefaultPaginator | ✅                 | ✅                   |
| businesses          | id          | DefaultPaginator | ✅                 | ✅                   |
| events              | event\_id   | DefaultPaginator | ✅                 | ✅                   |
| event\_types        | uuid        | DefaultPaginator | ✅                 | ❌                   |
| reports             | id          | DefaultPaginator | ✅                 | ✅                   |
| ip\_addresses       | uuid        | DefaultPaginator | ✅                 | ❌                   |
| subscriptions       | id          | DefaultPaginator | ✅                 | ✅                   |
| transactions        | id          | DefaultPaginator | ✅                 | ✅                   |

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

Environment

required

string

environment

›

Start date

required

string

start\_date

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                               |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 0.2.14  | 2026-03-03 | [74237](https://github.com/airbytehq/airbyte/pull/74237) | Update dependencies                                                                   |
| 0.2.13  | 2026-02-10 | [73106](https://github.com/airbytehq/airbyte/pull/73106) | Update dependencies                                                                   |
| 0.2.12  | 2026-01-20 | [71651](https://github.com/airbytehq/airbyte/pull/71651) | Update dependencies                                                                   |
| 0.2.11  | 2025-12-18 | [70506](https://github.com/airbytehq/airbyte/pull/70506) | Update dependencies                                                                   |
| 0.2.10  | 2025-11-25 | [70089](https://github.com/airbytehq/airbyte/pull/70089) | Update dependencies                                                                   |
| 0.2.9   | 2025-11-18 | [69694](https://github.com/airbytehq/airbyte/pull/69694) | Update dependencies                                                                   |
| 0.2.8   | 2025-10-29 | [69016](https://github.com/airbytehq/airbyte/pull/69016) | Update dependencies                                                                   |
| 0.2.7   | 2025-10-21 | [68291](https://github.com/airbytehq/airbyte/pull/68291) | Update dependencies                                                                   |
| 0.2.6   | 2025-10-14 | [67785](https://github.com/airbytehq/airbyte/pull/67785) | Update dependencies                                                                   |
| 0.2.5   | 2025-10-07 | [67336](https://github.com/airbytehq/airbyte/pull/67336) | Update dependencies                                                                   |
| 0.2.4   | 2025-09-30 | [66390](https://github.com/airbytehq/airbyte/pull/66390) | Update dependencies                                                                   |
| 0.2.3   | 2025-09-09 | [65806](https://github.com/airbytehq/airbyte/pull/65806) | Update dependencies                                                                   |
| 0.2.2   | 2025-08-23 | [65194](https://github.com/airbytehq/airbyte/pull/65194) | Update dependencies                                                                   |
| 0.2.1   | 2025-08-09 | [64749](https://github.com/airbytehq/airbyte/pull/64749) | Update dependencies                                                                   |
| 0.2.0   | 2025-07-10 | [62891](https://github.com/airbytehq/airbyte/pull/62891) | Remove `custom_data` property constraints and add it to `customers` stream            |
| 0.1.5   | 2025-08-02 | [64300](https://github.com/airbytehq/airbyte/pull/64300) | Update dependencies                                                                   |
| 0.1.4   | 2025-07-26 | [63842](https://github.com/airbytehq/airbyte/pull/63842) | Update dependencies                                                                   |
| 0.1.3   | 2025-07-19 | [63388](https://github.com/airbytehq/airbyte/pull/63388) | Update dependencies                                                                   |
| 0.1.2   | 2025-07-12 | [63195](https://github.com/airbytehq/airbyte/pull/63195) | Update dependencies                                                                   |
| 0.1.1   | 2025-07-05 | [62566](https://github.com/airbytehq/airbyte/pull/62566) | Update dependencies                                                                   |
| 0.1.0   | 2025-07-01 | [62479](https://github.com/airbytehq/airbyte/pull/62479) | Add adjustments stream                                                                |
| 0.0.11  | 2025-07-01 | [62461](https://github.com/airbytehq/airbyte/pull/62461) | Add constant retry backoff per Paddle API Docs                                        |
| 0.0.10  | 2025-06-28 | [62318](https://github.com/airbytehq/airbyte/pull/62318) | Update dependencies                                                                   |
| 0.0.9   | 2025-06-21 | [61917](https://github.com/airbytehq/airbyte/pull/61917) | Update dependencies                                                                   |
| 0.0.8   | 2025-06-14 | [60485](https://github.com/airbytehq/airbyte/pull/60485) | Update dependencies                                                                   |
| 0.0.7   | 2025-05-10 | [60059](https://github.com/airbytehq/airbyte/pull/60059) | Update dependencies                                                                   |
| 0.0.6   | 2025-05-04 | [59518](https://github.com/airbytehq/airbyte/pull/59518) | Update dependencies                                                                   |
| 0.0.5   | 2025-04-27 | [59085](https://github.com/airbytehq/airbyte/pull/59085) | Update dependencies                                                                   |
| 0.0.4   | 2025-04-19 | [58515](https://github.com/airbytehq/airbyte/pull/58515) | Update dependencies                                                                   |
| 0.0.3   | 2025-04-12 | [57847](https://github.com/airbytehq/airbyte/pull/57847) | Update dependencies                                                                   |
| 0.0.2   | 2025-04-05 | [57338](https://github.com/airbytehq/airbyte/pull/57338) | Update dependencies                                                                   |
| 0.0.1   | 2025-04-04 | [57003](https://github.com/airbytehq/airbyte/pull/57003) | Initial release by [@btkcodedev](https://github.com/btkcodedev) via Connector Builder |
