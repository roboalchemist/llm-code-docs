# Source: https://docs.airbyte.com/integrations/sources/chift.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-chift/latest/icon.svg)

# Chift

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.9](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-chift)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-chift)(last updated 2 days ago)

* Definition ID

  `d03aa64c-21a9-4edc-97b9-5590600ee3d6`

Chift is a tool that allows for the integration of financial data into SaaS products.

## Configuration[​](#configuration "Direct link to Configuration")

| Input           | Type     | Description    | Default Value |
| --------------- | -------- | -------------- | ------------- |
| `client_id`     | `string` | Client Id.     |               |
| `account_id`    | `string` | Account Id.    |               |
| `client_secret` | `string` | Client Secret. |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name | Primary Key  | Pagination    | Supports Full Sync | Supports Incremental |
| ----------- | ------------ | ------------- | ------------------ | -------------------- |
| consumers   | consumerid   | No pagination | ✅                 | ❌                   |
| connections | connectionid | No pagination | ✅                 | ❌                   |
| syncs       |              | No pagination | ✅                 | ❌                   |

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

Account Id

required

string

account\_id

Client Id

required

string

client\_id

Client Secret

required

string

client\_secret

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                                       |
| ------- | ---------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| 0.0.9   | 2026-03-10 | [74454](https://github.com/airbytehq/airbyte/pull/74454) | Update dependencies                                                                           |
| 0.0.8   | 2026-02-24 | [73822](https://github.com/airbytehq/airbyte/pull/73822) | Update dependencies                                                                           |
| 0.0.7   | 2026-02-17 | [73447](https://github.com/airbytehq/airbyte/pull/73447) | Update dependencies                                                                           |
| 0.0.6   | 2026-02-10 | [73000](https://github.com/airbytehq/airbyte/pull/73000) | Update dependencies                                                                           |
| 0.0.5   | 2026-02-03 | [72704](https://github.com/airbytehq/airbyte/pull/72704) | Update dependencies                                                                           |
| 0.0.4   | 2026-01-20 | [72112](https://github.com/airbytehq/airbyte/pull/72112) | Update dependencies                                                                           |
| 0.0.3   | 2026-01-14 | [71711](https://github.com/airbytehq/airbyte/pull/71711) | Update dependencies                                                                           |
| 0.0.2   | 2025-12-19 | [70944](https://github.com/airbytehq/airbyte/pull/70944) | Update dependencies                                                                           |
| 0.0.1   | 2025-10-13 |                                                          | Initial release by [@FVidalCarneiro](https://github.com/FVidalCarneiro) via Connector Builder |
