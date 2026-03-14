# Source: https://docs.airbyte.com/integrations/sources/rocket-chat.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-rocket-chat/latest/icon.svg)

# Rocket.chat API

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.2.25](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-rocket-chat)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-rocket-chat)(last updated 10 months ago)

* Definition ID

  `921d9608-3915-450b-8078-0af18801ea1b`

## Sync overview[​](#sync-overview "Direct link to Sync overview")

This source can sync data from the [Rocket.chat API](https://developer.rocket.chat/reference/api). At present this connector only supports full refresh syncs meaning that each time you use the connector it will sync all available records from scratch. Please use cautiously if you expect your API to have a lot of records.

## This Source Supports the Following Streams[​](#this-source-supports-the-following-streams "Direct link to This Source Supports the Following Streams")

* teams
* rooms
* channels
* roles
* subscriptions
* users

### Features[​](#features "Direct link to Features")

\| Feature | Supported?(Yes/No) | Notes | | :--\_ | :--\_ | :--\* | | Full Refresh Sync | Yes | | | Incremental Sync | No | |

### Performance considerations[​](#performance-considerations "Direct link to Performance considerations")

Rocket.chat APIs are under rate limits for the number of API calls allowed per API keys per second. If you reach a rate limit, API will return a 429 HTTP error code. See [here](https://developer.rocket.chat/reference/api/rest-api/endpoints/other-important-endpoints/rate-limiter-endpoints)

## Getting started[​](#getting-started "Direct link to Getting started")

### Requirements[​](#requirements "Direct link to Requirements")

You need to setup a personal access token within the Rocket.chat workspace, see [here](https://docs.rocket.chat/use-rocket.chat/user-guides/user-panel/my-account#personal-access-tokens) for step-by-step.

* token
* user\_id
* endpoint

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

Endpoint

required

string

endpoint

›

Token

required

string

token

›

User ID.

required

string

user\_id

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                              | Subject                                                                                                                                                                |
| ------- | ---------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.2.25  | 2025-05-10 | [60126](https://github.com/airbytehq/airbyte/pull/60126)  | Update dependencies                                                                                                                                                    |
| 0.2.24  | 2025-05-04 | [59590](https://github.com/airbytehq/airbyte/pull/59590)  | Update dependencies                                                                                                                                                    |
| 0.2.23  | 2025-04-27 | [59030](https://github.com/airbytehq/airbyte/pull/59030)  | Update dependencies                                                                                                                                                    |
| 0.2.22  | 2025-04-19 | [58399](https://github.com/airbytehq/airbyte/pull/58399)  | Update dependencies                                                                                                                                                    |
| 0.2.21  | 2025-04-12 | [57942](https://github.com/airbytehq/airbyte/pull/57942)  | Update dependencies                                                                                                                                                    |
| 0.2.20  | 2025-04-05 | [57284](https://github.com/airbytehq/airbyte/pull/57284)  | Update dependencies                                                                                                                                                    |
| 0.2.19  | 2025-03-29 | [56778](https://github.com/airbytehq/airbyte/pull/56778)  | Update dependencies                                                                                                                                                    |
| 0.2.18  | 2025-03-22 | [56189](https://github.com/airbytehq/airbyte/pull/56189)  | Update dependencies                                                                                                                                                    |
| 0.2.17  | 2025-03-08 | [55525](https://github.com/airbytehq/airbyte/pull/55525)  | Update dependencies                                                                                                                                                    |
| 0.2.16  | 2025-03-01 | [55013](https://github.com/airbytehq/airbyte/pull/55013)  | Update dependencies                                                                                                                                                    |
| 0.2.15  | 2025-02-23 | [54552](https://github.com/airbytehq/airbyte/pull/54552)  | Update dependencies                                                                                                                                                    |
| 0.2.14  | 2025-02-15 | [53993](https://github.com/airbytehq/airbyte/pull/53993)  | Update dependencies                                                                                                                                                    |
| 0.2.13  | 2025-02-08 | [53495](https://github.com/airbytehq/airbyte/pull/53495)  | Update dependencies                                                                                                                                                    |
| 0.2.12  | 2025-02-01 | [53002](https://github.com/airbytehq/airbyte/pull/53002)  | Update dependencies                                                                                                                                                    |
| 0.2.11  | 2025-01-25 | [52501](https://github.com/airbytehq/airbyte/pull/52501)  | Update dependencies                                                                                                                                                    |
| 0.2.10  | 2025-01-18 | [51906](https://github.com/airbytehq/airbyte/pull/51906)  | Update dependencies                                                                                                                                                    |
| 0.2.9   | 2025-01-11 | [51375](https://github.com/airbytehq/airbyte/pull/51375)  | Update dependencies                                                                                                                                                    |
| 0.2.8   | 2024-12-28 | [50717](https://github.com/airbytehq/airbyte/pull/50717)  | Update dependencies                                                                                                                                                    |
| 0.2.7   | 2024-12-21 | [50251](https://github.com/airbytehq/airbyte/pull/50251)  | Update dependencies                                                                                                                                                    |
| 0.2.6   | 2024-12-14 | [49705](https://github.com/airbytehq/airbyte/pull/49705)  | Update dependencies                                                                                                                                                    |
| 0.2.5   | 2024-12-12 | [49340](https://github.com/airbytehq/airbyte/pull/49340)  | Update dependencies                                                                                                                                                    |
| 0.2.4   | 2024-12-11 | [49095](https://github.com/airbytehq/airbyte/pull/49095)  | Starting with this version, the Docker image is now rootless. Please note that this and future versions will not be compatible with Airbyte versions earlier than 0.64 |
| 0.2.3   | 2024-10-29 | [47853](https://github.com/airbytehq/airbyte/pull/47853)  | Update dependencies                                                                                                                                                    |
| 0.2.2   | 2024-10-28 | [47639](https://github.com/airbytehq/airbyte/pull/47639)  | Update dependencies                                                                                                                                                    |
| 0.2.1   | 2024-08-16 | [44196](https://github.com/airbytehq/airbyte/pull/44196)  | Bump source-declarative-manifest version                                                                                                                               |
| 0.2.0   | 2024-08-14 | [44076](https://github.com/airbytehq/airbyte/pull/44076)  | Refactor connector to manifest-only format                                                                                                                             |
| 0.1.13  | 2024-08-12 | [43884](https://github.com/airbytehq/airbyte/pull/43884)  | Update dependencies                                                                                                                                                    |
| 0.1.12  | 2024-08-10 | [43649](https://github.com/airbytehq/airbyte/pull/43649)  | Update dependencies                                                                                                                                                    |
| 0.1.11  | 2024-08-03 | [43157](https://github.com/airbytehq/airbyte/pull/43157)  | Update dependencies                                                                                                                                                    |
| 0.1.10  | 2024-07-27 | [42641](https://github.com/airbytehq/airbyte/pull/42641)  | Update dependencies                                                                                                                                                    |
| 0.1.9   | 2024-07-20 | [42301](https://github.com/airbytehq/airbyte/pull/42301)  | Update dependencies                                                                                                                                                    |
| 0.1.8   | 2024-07-13 | [41879](https://github.com/airbytehq/airbyte/pull/41879)  | Update dependencies                                                                                                                                                    |
| 0.1.7   | 2024-07-10 | [41518](https://github.com/airbytehq/airbyte/pull/41518)  | Update dependencies                                                                                                                                                    |
| 0.1.6   | 2024-07-06 | [40952](https://github.com/airbytehq/airbyte/pull/40952)  | Update dependencies                                                                                                                                                    |
| 0.1.5   | 2024-06-25 | [40346](https://github.com/airbytehq/airbyte/pull/40346)  | Update dependencies                                                                                                                                                    |
| 0.1.4   | 2024-06-21 | [39919](https://github.com/airbytehq/airbyte/pull/39919)  | Update dependencies                                                                                                                                                    |
| 0.1.3   | 2024-06-06 | [39110](https://github.com/airbytehq/airbyte/pull/39110)  | Make compatible with builder                                                                                                                                           |
| 0.1.2   | 2024-06-04 | [38992](https://github.com/airbytehq/airbyte/pull/38992)  | \[autopull] Upgrade base image to v1.2.1                                                                                                                               |
| 0.1.1   | 2024-05-21 | [38517](https://github.com/airbytehq/airbyte/pull/38517)  | \[autopull] base image + poetry + up\_to\_date                                                                                                                         |
| 0.1.0   | 2022-10-29 | [#18635](https://github.com/airbytehq/airbyte/pull/18635) | 🎉 New Source: Rocket.chat API \[low-code CDK]                                                                                                                         |
