# Source: https://docs.airbyte.com/integrations/sources/wasabi-stats-api.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-wasabi-stats-api/latest/icon.svg)

# Wasabi

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.1](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-wasabi-stats-api)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-wasabi-stats-api)(last updated 4 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `6b0d43cb-8d31-4f9f-9832-6e577aa80db4`

Connector for <https://www.wasabi.com> stats API. API docs: <https://docs.wasabi.com/docs/wasabi-stats-api>

info

This connector ingest stats information from Wasabi server. It **does not** ingest content from files stored in Wasabi.

## Configuration[​](#configuration "Direct link to Configuration")

| Input        | Type     | Description                                          | Default Value |
| ------------ | -------- | ---------------------------------------------------- | ------------- |
| `api_key`    | `string` | API Key. The API key format is `AccessKey:SecretKey` |               |
| `start_date` | `string` | Start date.                                          |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name                    | Primary Key | Pagination       | Supports Full Sync | Supports Incremental |
| ------------------------------ | ----------- | ---------------- | ------------------ | -------------------- |
| Standalone Utilizations        |             | DefaultPaginator | ✅                 | ✅                   |
| Standalone Bucket Utilizations |             | DefaultPaginator | ✅                 | ✅                   |

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

| Version | Date       | Subject                                                                             |
| ------- | ---------- | ----------------------------------------------------------------------------------- |
| 0.0.1   | 2024-10-25 | Initial release by [@dainiussa](https://github.com/dainiussa) via Connector Builder |
