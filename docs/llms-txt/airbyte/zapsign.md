# Source: https://docs.airbyte.com/integrations/sources/zapsign.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-zapsign/latest/icon.svg)

# ZapSign

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.32](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-zapsign)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-zapsign)(last updated 16 days ago)

* Definition ID

  `4a1d519c-4703-4450-87db-d95816ba4f68`

Website: <https://app.zapsign.co/> API Reference: <https://docs.zapsign.com.br/>

## Configuration[​](#configuration "Direct link to Configuration")

| Input        | Type     | Description                                                                                                                                                                                                                                                                | Default Value |
| ------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `api_token`  | `string` | API Token. Your static API token for authentication. You can find it in your ZapSign account under the 'Settings' or 'API' section. For more details, refer to the [Getting Started](https://docs.zapsign.com.br/english/getting-started#how-do-i-get-my-api-token) guide. |               |
| `start_date` | `string` | Start date.                                                                                                                                                                                                                                                                |               |
| `signer_ids` | `array`  | Signer IDs. The signer ids for signer stream                                                                                                                                                                                                                               |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name | Primary Key | Pagination       | Supports Full Sync | Supports Incremental |
| ----------- | ----------- | ---------------- | ------------------ | -------------------- |
| templates   | token       | DefaultPaginator | ✅                 | ✅                   |
| documents   | token       | DefaultPaginator | ✅                 | ✅                   |
| signer      | token       | DefaultPaginator | ✅                 | ❌                   |

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

API Token

required

string

api\_token

›

Start date

required

string

start\_date

›

Signer IDs

array

signer\_ids

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                               |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 0.0.32  | 2026-02-24 | [73892](https://github.com/airbytehq/airbyte/pull/73892) | Update dependencies                                                                   |
| 0.0.31  | 2026-02-10 | [73154](https://github.com/airbytehq/airbyte/pull/73154) | Update dependencies                                                                   |
| 0.0.30  | 2026-01-20 | [72068](https://github.com/airbytehq/airbyte/pull/72068) | Update dependencies                                                                   |
| 0.0.29  | 2026-01-14 | [71675](https://github.com/airbytehq/airbyte/pull/71675) | Update dependencies                                                                   |
| 0.0.28  | 2025-12-18 | [70712](https://github.com/airbytehq/airbyte/pull/70712) | Update dependencies                                                                   |
| 0.0.27  | 2025-11-25 | [70105](https://github.com/airbytehq/airbyte/pull/70105) | Update dependencies                                                                   |
| 0.0.26  | 2025-11-18 | [69567](https://github.com/airbytehq/airbyte/pull/69567) | Update dependencies                                                                   |
| 0.0.25  | 2025-10-29 | [68971](https://github.com/airbytehq/airbyte/pull/68971) | Update dependencies                                                                   |
| 0.0.24  | 2025-10-21 | [68458](https://github.com/airbytehq/airbyte/pull/68458) | Update dependencies                                                                   |
| 0.0.23  | 2025-10-14 | [67982](https://github.com/airbytehq/airbyte/pull/67982) | Update dependencies                                                                   |
| 0.0.22  | 2025-10-07 | [67252](https://github.com/airbytehq/airbyte/pull/67252) | Update dependencies                                                                   |
| 0.0.21  | 2025-09-30 | [66841](https://github.com/airbytehq/airbyte/pull/66841) | Update dependencies                                                                   |
| 0.0.20  | 2025-09-24 | [66463](https://github.com/airbytehq/airbyte/pull/66463) | Update dependencies                                                                   |
| 0.0.19  | 2025-09-09 | [65667](https://github.com/airbytehq/airbyte/pull/65667) | Update dependencies                                                                   |
| 0.0.18  | 2025-08-24 | [65401](https://github.com/airbytehq/airbyte/pull/65401) | Update dependencies                                                                   |
| 0.0.17  | 2025-08-10 | [64856](https://github.com/airbytehq/airbyte/pull/64856) | Update dependencies                                                                   |
| 0.0.16  | 2025-08-02 | [64352](https://github.com/airbytehq/airbyte/pull/64352) | Update dependencies                                                                   |
| 0.0.15  | 2025-07-27 | [64082](https://github.com/airbytehq/airbyte/pull/64082) | Update dependencies                                                                   |
| 0.0.14  | 2025-07-20 | [63652](https://github.com/airbytehq/airbyte/pull/63652) | Update dependencies                                                                   |
| 0.0.13  | 2025-07-12 | [63172](https://github.com/airbytehq/airbyte/pull/63172) | Update dependencies                                                                   |
| 0.0.12  | 2025-07-05 | [62720](https://github.com/airbytehq/airbyte/pull/62720) | Update dependencies                                                                   |
| 0.0.11  | 2025-06-28 | [62238](https://github.com/airbytehq/airbyte/pull/62238) | Update dependencies                                                                   |
| 0.0.10  | 2025-06-21 | [61752](https://github.com/airbytehq/airbyte/pull/61752) | Update dependencies                                                                   |
| 0.0.9   | 2025-06-15 | [61228](https://github.com/airbytehq/airbyte/pull/61228) | Update dependencies                                                                   |
| 0.0.8   | 2025-05-24 | [60739](https://github.com/airbytehq/airbyte/pull/60739) | Update dependencies                                                                   |
| 0.0.7   | 2025-05-10 | [59999](https://github.com/airbytehq/airbyte/pull/59999) | Update dependencies                                                                   |
| 0.0.6   | 2025-05-04 | [59551](https://github.com/airbytehq/airbyte/pull/59551) | Update dependencies                                                                   |
| 0.0.5   | 2025-04-26 | [58947](https://github.com/airbytehq/airbyte/pull/58947) | Update dependencies                                                                   |
| 0.0.4   | 2025-04-19 | [58552](https://github.com/airbytehq/airbyte/pull/58552) | Update dependencies                                                                   |
| 0.0.3   | 2025-04-13 | [58037](https://github.com/airbytehq/airbyte/pull/58037) | Update dependencies                                                                   |
| 0.0.2   | 2025-04-05 | [57383](https://github.com/airbytehq/airbyte/pull/57383) | Update dependencies                                                                   |
| 0.0.1   | 2025-04-04 | [57008](https://github.com/airbytehq/airbyte/pull/57008) | Initial release by [@btkcodedev](https://github.com/btkcodedev) via Connector Builder |
