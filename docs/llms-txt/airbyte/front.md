# Source: https://docs.airbyte.com/integrations/sources/front.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-front/latest/icon.svg)

# Front

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.39](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-front)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-front)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `ae390de9-bdd5-4bfa-9d14-34010b44ca50`

This page contains the setup guide and reference information for the [Front](https://app.frontapp.com) source connector.

## Documentation reference:[​](#documentation-reference "Direct link to Documentation reference:")

Visit `https://dev.frontapp.com/reference/introduction` for API documentation

## Authentication setup[​](#authentication-setup "Direct link to Authentication setup")

`Source-front` uses bearer token authentication, Visit `https://dev.frontapp.com/docs/create-and-revoke-api-tokens` for getting your API token.

## Configuration[​](#configuration "Direct link to Configuration")

| Input        | Type     | Description                              | Default Value |
| ------------ | -------- | ---------------------------------------- | ------------- |
| `api_key`    | `string` | API Key.                                 |               |
| `start_date` | `string` | Start date.                              |               |
| `page_limit` | `string` | Page limit. Page limit for the responses | 50            |

## Streams[​](#streams "Direct link to Streams")

| Stream Name                   | Primary Key | Pagination       | Supports Full Sync | Supports Incremental |
| ----------------------------- | ----------- | ---------------- | ------------------ | -------------------- |
| events                        | id          | DefaultPaginator | ✅                 | ✅                   |
| inboxes                       | id          | DefaultPaginator | ✅                 | ❌                   |
| inboxes\_channels             | id          | DefaultPaginator | ✅                 | ❌                   |
| inboxes\_conversations        | id          | DefaultPaginator | ✅                 | ✅                   |
| inboxes\_teammates            | id          | DefaultPaginator | ✅                 | ❌                   |
| conversations                 | id          | DefaultPaginator | ✅                 | ✅                   |
| conversations\_events         | id          | DefaultPaginator | ✅                 | ✅                   |
| conversations\_followers      | id          | DefaultPaginator | ✅                 | ❌                   |
| conversations\_inboxes        |             | DefaultPaginator | ✅                 | ❌                   |
| conversations\_messages       | id          | DefaultPaginator | ✅                 | ✅                   |
| links                         | id          | DefaultPaginator | ✅                 | ❌                   |
| accounts                      | id          | DefaultPaginator | ✅                 | ✅                   |
| accounts\_contacts            | id          | DefaultPaginator | ✅                 | ✅                   |
| contacts                      | id          | DefaultPaginator | ✅                 | ✅                   |
| channels                      | id          | DefaultPaginator | ✅                 | ❌                   |
| company\_tags                 | id          | DefaultPaginator | ✅                 | ✅                   |
| teammates                     | id          | DefaultPaginator | ✅                 | ❌                   |
| tags                          | id          | DefaultPaginator | ✅                 | ✅                   |
| tags\_children                | id          | DefaultPaginator | ✅                 | ✅                   |
| teammates\_tags               | id          | DefaultPaginator | ✅                 | ✅                   |
| teams                         | id          | DefaultPaginator | ✅                 | ❌                   |
| teams\_tags                   | id          | DefaultPaginator | ✅                 | ✅                   |
| contact\_groups               | id          | DefaultPaginator | ✅                 | ❌                   |
| conversations\_drafts         | id          | DefaultPaginator | ✅                 | ✅                   |
| contacts\_notes               |             | DefaultPaginator | ✅                 | ✅                   |
| teammates\_contact\_groups    | id          | DefaultPaginator | ✅                 | ❌                   |
| teams\_contact\_groups        |             | DefaultPaginator | ✅                 | ❌                   |
| knowledge\_bases              | id          | DefaultPaginator | ✅                 | ✅                   |
| knowledge\_bases\_articles    |             | DefaultPaginator | ✅                 | ✅                   |
| knowledge\_bases\_categories  |             | DefaultPaginator | ✅                 | ✅                   |
| message\_template\_folders    | id          | DefaultPaginator | ✅                 | ✅                   |
| teams\_signatures             | id          | DefaultPaginator | ✅                 | ❌                   |
| message\_templates            | id          | DefaultPaginator | ✅                 | ✅                   |
| teammates\_message\_templates | id          | DefaultPaginator | ✅                 | ❌                   |
| teams\_message\_templates     | id          | DefaultPaginator | ✅                 | ✅                   |

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

›

Page limit

string

page\_limit

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                               |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 0.0.40  | 2026-03-10 | [74529](https://github.com/airbytehq/airbyte/pull/74529) | Update dependencies                                                                   |
| 0.0.39  | 2026-02-24 | [73773](https://github.com/airbytehq/airbyte/pull/73773) | Update dependencies                                                                   |
| 0.0.38  | 2026-02-10 | [73066](https://github.com/airbytehq/airbyte/pull/73066) | Update dependencies                                                                   |
| 0.0.37  | 2026-02-03 | [72591](https://github.com/airbytehq/airbyte/pull/72591) | Update dependencies                                                                   |
| 0.0.36  | 2026-01-20 | [71925](https://github.com/airbytehq/airbyte/pull/71925) | Update dependencies                                                                   |
| 0.0.35  | 2026-01-14 | [71419](https://github.com/airbytehq/airbyte/pull/71419) | Update dependencies                                                                   |
| 0.0.34  | 2025-12-18 | [70580](https://github.com/airbytehq/airbyte/pull/70580) | Update dependencies                                                                   |
| 0.0.33  | 2025-11-25 | [69499](https://github.com/airbytehq/airbyte/pull/69499) | Update dependencies                                                                   |
| 0.0.32  | 2025-10-29 | [68808](https://github.com/airbytehq/airbyte/pull/68808) | Update dependencies                                                                   |
| 0.0.31  | 2025-10-21 | [68426](https://github.com/airbytehq/airbyte/pull/68426) | Update dependencies                                                                   |
| 0.0.30  | 2025-10-14 | [68073](https://github.com/airbytehq/airbyte/pull/68073) | Update dependencies                                                                   |
| 0.0.29  | 2025-10-07 | [67298](https://github.com/airbytehq/airbyte/pull/67298) | Update dependencies                                                                   |
| 0.0.28  | 2025-09-30 | [66776](https://github.com/airbytehq/airbyte/pull/66776) | Update dependencies                                                                   |
| 0.0.27  | 2025-09-24 | [65759](https://github.com/airbytehq/airbyte/pull/65759) | Update dependencies                                                                   |
| 0.0.26  | 2025-08-23 | [65245](https://github.com/airbytehq/airbyte/pull/65245) | Update dependencies                                                                   |
| 0.0.25  | 2025-08-09 | [64779](https://github.com/airbytehq/airbyte/pull/64779) | Update dependencies                                                                   |
| 0.0.24  | 2025-07-26 | [64049](https://github.com/airbytehq/airbyte/pull/64049) | Update dependencies                                                                   |
| 0.0.23  | 2025-07-19 | [63572](https://github.com/airbytehq/airbyte/pull/63572) | Update dependencies                                                                   |
| 0.0.22  | 2025-07-12 | [62961](https://github.com/airbytehq/airbyte/pull/62961) | Update dependencies                                                                   |
| 0.0.21  | 2025-07-05 | [62780](https://github.com/airbytehq/airbyte/pull/62780) | Update dependencies                                                                   |
| 0.0.20  | 2025-06-28 | [62366](https://github.com/airbytehq/airbyte/pull/62366) | Update dependencies                                                                   |
| 0.0.19  | 2025-06-21 | [61963](https://github.com/airbytehq/airbyte/pull/61963) | Update dependencies                                                                   |
| 0.0.18  | 2025-06-14 | [61281](https://github.com/airbytehq/airbyte/pull/61281) | Update dependencies                                                                   |
| 0.0.17  | 2025-05-24 | [60416](https://github.com/airbytehq/airbyte/pull/60416) | Update dependencies                                                                   |
| 0.0.16  | 2025-05-10 | [59920](https://github.com/airbytehq/airbyte/pull/59920) | Update dependencies                                                                   |
| 0.0.15  | 2025-05-03 | [59422](https://github.com/airbytehq/airbyte/pull/59422) | Update dependencies                                                                   |
| 0.0.14  | 2025-04-26 | [58309](https://github.com/airbytehq/airbyte/pull/58309) | Update dependencies                                                                   |
| 0.0.13  | 2025-04-12 | [57819](https://github.com/airbytehq/airbyte/pull/57819) | Update dependencies                                                                   |
| 0.0.12  | 2025-04-05 | [57276](https://github.com/airbytehq/airbyte/pull/57276) | Update dependencies                                                                   |
| 0.0.11  | 2025-03-29 | [56476](https://github.com/airbytehq/airbyte/pull/56476) | Update dependencies                                                                   |
| 0.0.10  | 2025-03-22 | [55932](https://github.com/airbytehq/airbyte/pull/55932) | Update dependencies                                                                   |
| 0.0.9   | 2025-03-08 | [55298](https://github.com/airbytehq/airbyte/pull/55298) | Update dependencies                                                                   |
| 0.0.8   | 2025-03-01 | [54987](https://github.com/airbytehq/airbyte/pull/54987) | Update dependencies                                                                   |
| 0.0.7   | 2025-02-22 | [54437](https://github.com/airbytehq/airbyte/pull/54437) | Update dependencies                                                                   |
| 0.0.6   | 2025-02-15 | [50584](https://github.com/airbytehq/airbyte/pull/50584) | Update dependencies                                                                   |
| 0.0.5   | 2024-12-21 | [50005](https://github.com/airbytehq/airbyte/pull/50005) | Update dependencies                                                                   |
| 0.0.4   | 2024-12-14 | [49536](https://github.com/airbytehq/airbyte/pull/49536) | Update dependencies                                                                   |
| 0.0.3   | 2024-12-12 | [48960](https://github.com/airbytehq/airbyte/pull/48960) | Update dependencies                                                                   |
| 0.0.2   | 2024-10-29 | [47759](https://github.com/airbytehq/airbyte/pull/47759) | Update dependencies                                                                   |
| 0.0.1   | 2024-09-11 | [45387](https://github.com/airbytehq/airbyte/pull/45387) | Initial release by [@btkcodedev](https://github.com/btkcodedev) via Connector Builder |
