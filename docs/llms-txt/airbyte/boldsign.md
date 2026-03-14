# Source: https://docs.airbyte.com/integrations/sources/boldsign.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-boldsign/latest/icon.svg)

# BoldSign

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.23](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-boldsign)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-boldsign)(last updated 16 days ago)

* Definition ID

  `b013676a-2286-4f7a-bca4-811477207761`

Website: <https://app.boldsign.com/> API Reference: <https://developers.boldsign.com/api-overview/getting-started/?region=us>

## Configuration[​](#configuration "Direct link to Configuration")

| Input        | Type     | Description                                                                                                                                                                                            | Default Value |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| `api_key`    | `string` | API Key. Your BoldSign API key. You can generate it by navigating to the API menu in the BoldSign app, selecting 'API Key', and clicking 'Generate API Key'. Copy the generated key and paste it here. |               |
| `start_date` | `string` | Start date.                                                                                                                                                                                            |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name      | Primary Key   | Pagination       | Supports Full Sync | Supports Incremental |
| ---------------- | ------------- | ---------------- | ------------------ | -------------------- |
| documents        | documentId    | DefaultPaginator | ✅                 | ✅                   |
| brands           | brandId       | DefaultPaginator | ✅                 | ❌                   |
| senderIdentities | email         | DefaultPaginator | ✅                 | ❌                   |
| teams            | teamId        | DefaultPaginator | ✅                 | ✅                   |
| templates        | documentId    | DefaultPaginator | ✅                 | ✅                   |
| users\_list      | userId        | DefaultPaginator | ✅                 | ✅                   |
| custom\_fields   | customFieldId | DefaultPaginator | ✅                 | ❌                   |
| contacts         | id            | DefaultPaginator | ✅                 | ❌                   |

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

| Version | Date       | Pull Request                                             | Subject                                                                               |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 0.0.23  | 2026-02-24 | [73790](https://github.com/airbytehq/airbyte/pull/73790) | Update dependencies                                                                   |
| 0.0.22  | 2026-02-03 | [72062](https://github.com/airbytehq/airbyte/pull/72062) | Update dependencies                                                                   |
| 0.0.21  | 2026-01-14 | [71470](https://github.com/airbytehq/airbyte/pull/71470) | Update dependencies                                                                   |
| 0.0.20  | 2025-12-18 | [70661](https://github.com/airbytehq/airbyte/pull/70661) | Update dependencies                                                                   |
| 0.0.19  | 2025-11-25 | [69948](https://github.com/airbytehq/airbyte/pull/69948) | Update dependencies                                                                   |
| 0.0.18  | 2025-11-18 | [69463](https://github.com/airbytehq/airbyte/pull/69463) | Update dependencies                                                                   |
| 0.0.17  | 2025-10-29 | [68697](https://github.com/airbytehq/airbyte/pull/68697) | Update dependencies                                                                   |
| 0.0.16  | 2025-10-21 | [68221](https://github.com/airbytehq/airbyte/pull/68221) | Update dependencies                                                                   |
| 0.0.15  | 2025-10-14 | [67834](https://github.com/airbytehq/airbyte/pull/67834) | Update dependencies                                                                   |
| 0.0.14  | 2025-10-07 | [67211](https://github.com/airbytehq/airbyte/pull/67211) | Update dependencies                                                                   |
| 0.0.13  | 2025-09-30 | [65632](https://github.com/airbytehq/airbyte/pull/65632) | Update dependencies                                                                   |
| 0.0.12  | 2025-08-09 | [64656](https://github.com/airbytehq/airbyte/pull/64656) | Update dependencies                                                                   |
| 0.0.11  | 2025-07-12 | [63033](https://github.com/airbytehq/airbyte/pull/63033) | Update dependencies                                                                   |
| 0.0.10  | 2025-07-05 | [62531](https://github.com/airbytehq/airbyte/pull/62531) | Update dependencies                                                                   |
| 0.0.9   | 2025-06-28 | [62138](https://github.com/airbytehq/airbyte/pull/62138) | Update dependencies                                                                   |
| 0.0.8   | 2025-06-21 | [61875](https://github.com/airbytehq/airbyte/pull/61875) | Update dependencies                                                                   |
| 0.0.7   | 2025-06-15 | [59840](https://github.com/airbytehq/airbyte/pull/59840) | Update dependencies                                                                   |
| 0.0.6   | 2025-05-03 | [59345](https://github.com/airbytehq/airbyte/pull/59345) | Update dependencies                                                                   |
| 0.0.5   | 2025-04-26 | [58724](https://github.com/airbytehq/airbyte/pull/58724) | Update dependencies                                                                   |
| 0.0.4   | 2025-04-19 | [58240](https://github.com/airbytehq/airbyte/pull/58240) | Update dependencies                                                                   |
| 0.0.3   | 2025-04-12 | [57617](https://github.com/airbytehq/airbyte/pull/57617) | Update dependencies                                                                   |
| 0.0.2   | 2025-04-05 | [57159](https://github.com/airbytehq/airbyte/pull/57159) | Update dependencies                                                                   |
| 0.0.1   | 2025-04-04 | [57005](https://github.com/airbytehq/airbyte/pull/57005) | Initial release by [@btkcodedev](https://github.com/btkcodedev) via Connector Builder |
