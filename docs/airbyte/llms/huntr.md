# Source: https://docs.airbyte.com/integrations/sources/huntr.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-huntr/latest/icon.svg)

# Huntr

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.1.0](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-huntr)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-huntr)(last updated a year ago)

* Definition ID

  `e1b1016c-04d5-41e6-b4ed-46f0893bb02a`

A connector for the Huntr application

## Configuration[​](#configuration "Direct link to Configuration")

| Input     | Type     | Description | Default Value |
| --------- | -------- | ----------- | ------------- |
| `api_key` | `string` | API Key.    |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name               | Primary Key | Pagination       | Supports Full Sync | Supports Incremental |
| ------------------------- | ----------- | ---------------- | ------------------ | -------------------- |
| members                   | id          | DefaultPaginator | ✅                 | ❌                   |
| organization\_invitations | id          | DefaultPaginator | ✅                 | ❌                   |
| member\_fields            | id          | DefaultPaginator | ✅                 | ❌                   |
| activities                | id          | DefaultPaginator | ✅                 | ❌                   |
| notes                     | id          | DefaultPaginator | ✅                 | ❌                   |
| actions                   | id          | DefaultPaginator | ✅                 | ❌                   |
| candidates                | id          | DefaultPaginator | ✅                 | ❌                   |

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

API Key

required

string

api\_key

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Subject                                                                         |
| ------- | ---------- | ------------------------------------------------------------------------------- |
| 0.1.0   | 2025-01-29 | Add new streams                                                                 |
| 0.0.1   | 2025-01-15 | Initial release by [@krokrob](https://github.com/krokrob) via Connector Builder |
