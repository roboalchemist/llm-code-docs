# Source: https://docs.airbyte.com/integrations/sources/ezofficeinventory.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-ezofficeinventory/latest/icon.svg)

# EZOfficeInventory

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.48](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-ezofficeinventory)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-ezofficeinventory)(last updated 2 days ago)

* Definition ID

  `7b6be0f6-4139-42f8-a89e-2ca25560979a`

A manifest only source for EZOfficeInventory. <https://ezo.io/ezofficeinventory/>

## Configuration[​](#configuration "Direct link to Configuration")

| Input        | Type     | Description                                                                                                                                                                                        | Default Value |
| ------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `api_key`    | `string` | API Key. Your EZOfficeInventory Access Token. API Access is disabled by default. Enable API Access in Settings > Integrations > API Integration and click on Update to generate a new access token |               |
| `subdomain`  | `string` | Subdomain. The company name used in signup, also visible in the URL when logged in.                                                                                                                |               |
| `start_date` | `string` | Start date. Earliest date you want to sync historical streams (inventory\_histories, asset\_histories, asset\_stock\_histories) from                                                               |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name             | Primary Key | Pagination       | Supports Full Sync | Supports Incremental |
| ----------------------- | ----------- | ---------------- | ------------------ | -------------------- |
| inventories             | identifier  | DefaultPaginator | ✅                 | ❌                   |
| assets                  | identifier  | DefaultPaginator | ✅                 | ❌                   |
| checked\_out\_assets    | identifier  | DefaultPaginator | ✅                 | ❌                   |
| asset\_stocks           | identifier  | DefaultPaginator | ✅                 | ❌                   |
| members                 | id          | DefaultPaginator | ✅                 | ❌                   |
| locations               | id          | DefaultPaginator | ✅                 | ❌                   |
| groups                  | id          | DefaultPaginator | ✅                 | ❌                   |
| subgroups               | id          | DefaultPaginator | ✅                 | ❌                   |
| vendors                 | id          | DefaultPaginator | ✅                 | ❌                   |
| labels                  | id          | DefaultPaginator | ✅                 | ❌                   |
| custom\_fields          | id          | DefaultPaginator | ✅                 | ❌                   |
| purchase\_orders        | id          | DefaultPaginator | ✅                 | ❌                   |
| bundles                 |             | DefaultPaginator | ✅                 | ❌                   |
| carts                   |             | DefaultPaginator | ✅                 | ❌                   |
| inventory\_histories    |             | DefaultPaginator | ✅                 | ✅                   |
| asset\_histories        |             | DefaultPaginator | ✅                 | ✅                   |
| asset\_stock\_histories |             | DefaultPaginator | ✅                 | ✅                   |

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

›

Subdomain

required

string

subdomain

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                                                                                                                |
| ------- | ---------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.0.48  | 2026-03-10 | [74432](https://github.com/airbytehq/airbyte/pull/74432) | Update dependencies                                                                                                                                                    |
| 0.0.47  | 2026-02-24 | [73897](https://github.com/airbytehq/airbyte/pull/73897) | Update dependencies                                                                                                                                                    |
| 0.0.46  | 2026-02-17 | [73455](https://github.com/airbytehq/airbyte/pull/73455) | Update dependencies                                                                                                                                                    |
| 0.0.45  | 2026-02-10 | [72984](https://github.com/airbytehq/airbyte/pull/72984) | Update dependencies                                                                                                                                                    |
| 0.0.44  | 2026-02-03 | [72606](https://github.com/airbytehq/airbyte/pull/72606) | Update dependencies                                                                                                                                                    |
| 0.0.43  | 2026-01-20 | [71887](https://github.com/airbytehq/airbyte/pull/71887) | Update dependencies                                                                                                                                                    |
| 0.0.42  | 2026-01-14 | [71611](https://github.com/airbytehq/airbyte/pull/71611) | Update dependencies                                                                                                                                                    |
| 0.0.41  | 2025-12-18 | [70546](https://github.com/airbytehq/airbyte/pull/70546) | Update dependencies                                                                                                                                                    |
| 0.0.40  | 2025-11-25 | [70188](https://github.com/airbytehq/airbyte/pull/70188) | Update dependencies                                                                                                                                                    |
| 0.0.39  | 2025-11-18 | [69417](https://github.com/airbytehq/airbyte/pull/69417) | Update dependencies                                                                                                                                                    |
| 0.0.38  | 2025-10-29 | [68741](https://github.com/airbytehq/airbyte/pull/68741) | Update dependencies                                                                                                                                                    |
| 0.0.37  | 2025-10-21 | [68575](https://github.com/airbytehq/airbyte/pull/68575) | Update dependencies                                                                                                                                                    |
| 0.0.36  | 2025-10-14 | [67762](https://github.com/airbytehq/airbyte/pull/67762) | Update dependencies                                                                                                                                                    |
| 0.0.35  | 2025-10-07 | [67286](https://github.com/airbytehq/airbyte/pull/67286) | Update dependencies                                                                                                                                                    |
| 0.0.34  | 2025-09-30 | [65832](https://github.com/airbytehq/airbyte/pull/65832) | Update dependencies                                                                                                                                                    |
| 0.0.33  | 2025-08-23 | [65297](https://github.com/airbytehq/airbyte/pull/65297) | Update dependencies                                                                                                                                                    |
| 0.0.32  | 2025-08-09 | [64709](https://github.com/airbytehq/airbyte/pull/64709) | Update dependencies                                                                                                                                                    |
| 0.0.31  | 2025-08-02 | [63976](https://github.com/airbytehq/airbyte/pull/63976) | Update dependencies                                                                                                                                                    |
| 0.0.30  | 2025-07-19 | [63544](https://github.com/airbytehq/airbyte/pull/63544) | Update dependencies                                                                                                                                                    |
| 0.0.29  | 2025-07-12 | [63020](https://github.com/airbytehq/airbyte/pull/63020) | Update dependencies                                                                                                                                                    |
| 0.0.28  | 2025-07-05 | [62763](https://github.com/airbytehq/airbyte/pull/62763) | Update dependencies                                                                                                                                                    |
| 0.0.27  | 2025-06-28 | [62355](https://github.com/airbytehq/airbyte/pull/62355) | Update dependencies                                                                                                                                                    |
| 0.0.26  | 2025-06-21 | [61943](https://github.com/airbytehq/airbyte/pull/61943) | Update dependencies                                                                                                                                                    |
| 0.0.25  | 2025-06-14 | [61235](https://github.com/airbytehq/airbyte/pull/61235) | Update dependencies                                                                                                                                                    |
| 0.0.24  | 2025-05-24 | [60380](https://github.com/airbytehq/airbyte/pull/60380) | Update dependencies                                                                                                                                                    |
| 0.0.23  | 2025-05-10 | [59943](https://github.com/airbytehq/airbyte/pull/59943) | Update dependencies                                                                                                                                                    |
| 0.0.22  | 2025-05-03 | [58867](https://github.com/airbytehq/airbyte/pull/58867) | Update dependencies                                                                                                                                                    |
| 0.0.21  | 2025-04-19 | [58368](https://github.com/airbytehq/airbyte/pull/58368) | Update dependencies                                                                                                                                                    |
| 0.0.20  | 2025-04-12 | [57789](https://github.com/airbytehq/airbyte/pull/57789) | Update dependencies                                                                                                                                                    |
| 0.0.19  | 2025-04-05 | [57228](https://github.com/airbytehq/airbyte/pull/57228) | Update dependencies                                                                                                                                                    |
| 0.0.18  | 2025-03-29 | [56512](https://github.com/airbytehq/airbyte/pull/56512) | Update dependencies                                                                                                                                                    |
| 0.0.17  | 2025-03-22 | [55341](https://github.com/airbytehq/airbyte/pull/55341) | Update dependencies                                                                                                                                                    |
| 0.0.16  | 2025-03-01 | [54958](https://github.com/airbytehq/airbyte/pull/54958) | Update dependencies                                                                                                                                                    |
| 0.0.15  | 2025-02-22 | [54399](https://github.com/airbytehq/airbyte/pull/54399) | Update dependencies                                                                                                                                                    |
| 0.0.14  | 2025-02-15 | [53709](https://github.com/airbytehq/airbyte/pull/53709) | Update dependencies                                                                                                                                                    |
| 0.0.13  | 2025-02-08 | [53316](https://github.com/airbytehq/airbyte/pull/53316) | Update dependencies                                                                                                                                                    |
| 0.0.12  | 2025-02-01 | [52805](https://github.com/airbytehq/airbyte/pull/52805) | Update dependencies                                                                                                                                                    |
| 0.0.11  | 2025-01-25 | [51698](https://github.com/airbytehq/airbyte/pull/51698) | Update dependencies                                                                                                                                                    |
| 0.0.10  | 2025-01-11 | [51095](https://github.com/airbytehq/airbyte/pull/51095) | Update dependencies                                                                                                                                                    |
| 0.0.9   | 2024-12-28 | [50580](https://github.com/airbytehq/airbyte/pull/50580) | Update dependencies                                                                                                                                                    |
| 0.0.8   | 2024-12-21 | [50054](https://github.com/airbytehq/airbyte/pull/50054) | Update dependencies                                                                                                                                                    |
| 0.0.7   | 2024-12-14 | [49506](https://github.com/airbytehq/airbyte/pull/49506) | Update dependencies                                                                                                                                                    |
| 0.0.6   | 2024-12-12 | [49164](https://github.com/airbytehq/airbyte/pull/49164) | Update dependencies                                                                                                                                                    |
| 0.0.5   | 2024-12-11 | [48932](https://github.com/airbytehq/airbyte/pull/48932) | Starting with this version, the Docker image is now rootless. Please note that this and future versions will not be compatible with Airbyte versions earlier than 0.64 |
| 0.0.4   | 2024-11-04 | [48180](https://github.com/airbytehq/airbyte/pull/48180) | Update dependencies                                                                                                                                                    |
| 0.0.3   | 2024-10-29 | [47913](https://github.com/airbytehq/airbyte/pull/47913) | Update dependencies                                                                                                                                                    |
| 0.0.2   | 2024-10-28 | [47535](https://github.com/airbytehq/airbyte/pull/47535) | Update dependencies                                                                                                                                                    |
| 0.0.1   | 2024-09-15 | [45590](https://github.com/airbytehq/airbyte/pull/45590) | Initial release by [@pabloescoder](https://github.com/pabloescoder) via Connector Builder                                                                              |
