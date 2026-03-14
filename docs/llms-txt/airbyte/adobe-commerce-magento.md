# Source: https://docs.airbyte.com/integrations/sources/adobe-commerce-magento.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-adobe-commerce-magento/latest/icon.svg)

# Adobe Commerce (Magento)

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.9](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-adobe-commerce-magento)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-adobe-commerce-magento)(last updated a month ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `2a97bcea-a59e-4fe1-89e0-1663f11ec646`

Integrate Adobe Commerce store data to your destination

## Configuration[​](#configuration "Direct link to Configuration")

| Input         | Type     | Description                     | Default Value |
| ------------- | -------- | ------------------------------- | ------------- |
| `api_key`     | `string` | Integration Access Token.       |               |
| `start_date`  | `string` | Start Date.                     |               |
| `store_host`  | `string` | Store Host. magento.mystore.com |               |
| `api_version` | `string` | API Version. V1                 | V1            |

## Streams[​](#streams "Direct link to Streams")

| Stream Name              | Primary Key          | Pagination       | Supports Full Sync | Supports Incremental |
| ------------------------ | -------------------- | ---------------- | ------------------ | -------------------- |
| carts                    | id                   | DefaultPaginator | ✅                 | ✅                   |
| coupons                  | coupon\_id           | DefaultPaginator | ✅                 | ✅                   |
| creditmemos              | entity\_id           | DefaultPaginator | ✅                 | ✅                   |
| customers                | id                   | DefaultPaginator | ✅                 | ✅                   |
| customer\_groups         | id.code              | DefaultPaginator | ✅                 | ❌                   |
| directory\_countries     | id                   | DefaultPaginator | ✅                 | ❌                   |
| directory\_currency      | base\_currency\_code | DefaultPaginator | ✅                 | ❌                   |
| inventory\_stocks        | stock\_id            | DefaultPaginator | ✅                 | ❌                   |
| inventory\_sources       | source\_code         | DefaultPaginator | ✅                 | ❌                   |
| inventory\_source\_items | sku                  | DefaultPaginator | ✅                 | ❌                   |
| invoices                 | entity\_id           | DefaultPaginator | ✅                 | ✅                   |
| orders                   | entity\_id           | DefaultPaginator | ✅                 | ✅                   |
| products                 | id                   | DefaultPaginator | ✅                 | ✅                   |
| sales\_rules             | rule\_id             | DefaultPaginator | ✅                 | ✅                   |
| shipments                | entity\_id           | DefaultPaginator | ✅                 | ✅                   |
| store\_websites          | id.code              | DefaultPaginator | ✅                 | ❌                   |
| store\_views             | id.code              | DefaultPaginator | ✅                 | ❌                   |
| store\_groups            | id.code              | DefaultPaginator | ✅                 | ❌                   |
| tax\_rates               | id                   | DefaultPaginator | ✅                 | ❌                   |
| tax\_classes             | class\_id            | DefaultPaginator | ✅                 | ❌                   |
| transactions             | transaction\_id      | DefaultPaginator | ✅                 | ✅                   |

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

Integration Access Token

required

string

api\_key

›

Start Date

required

string

start\_date

›

Store Host

required

string

store\_host

›

API Version

string

api\_version

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                               |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 0.0.10  | 2026-03-10 | [74535](https://github.com/airbytehq/airbyte/pull/74535) | Update dependencies                                                                   |
| 0.0.9   | 2026-02-10 | [73003](https://github.com/airbytehq/airbyte/pull/73003) | Update dependencies                                                                   |
| 0.0.8   | 2026-01-20 | [71997](https://github.com/airbytehq/airbyte/pull/71997) | Update dependencies                                                                   |
| 0.0.7   | 2026-01-14 | [71508](https://github.com/airbytehq/airbyte/pull/71508) | Update dependencies                                                                   |
| 0.0.6   | 2025-12-18 | [70559](https://github.com/airbytehq/airbyte/pull/70559) | Update dependencies                                                                   |
| 0.0.5   | 2025-11-25 | [69909](https://github.com/airbytehq/airbyte/pull/69909) | Update dependencies                                                                   |
| 0.0.4   | 2025-10-29 | [69058](https://github.com/airbytehq/airbyte/pull/69058) | Update dependencies                                                                   |
| 0.0.3   | 2025-09-30 | [65651](https://github.com/airbytehq/airbyte/pull/65651) | Update dependencies                                                                   |
| 0.0.2   | 2025-08-23 | [65323](https://github.com/airbytehq/airbyte/pull/65323) | Update dependencies                                                                   |
| 0.0.1   | 2025-07-26 |                                                          | Initial release by [@joacoc2020](https://github.com/joacoc2020) via Connector Builder |
