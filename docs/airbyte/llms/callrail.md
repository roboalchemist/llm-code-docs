# Source: https://docs.airbyte.com/integrations/sources/callrail.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-callrail/latest/icon.svg)

# CallRail

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.2.13](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-callrail)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-callrail)(last updated 4 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `dc98a6ad-2dd1-47b6-9529-2ec35820f9c6`

## Overview[​](#overview "Direct link to Overview")

The CailRail source supports Full Refresh and Incremental syncs.

### Output schema[​](#output-schema "Direct link to Output schema")

This Source is capable of syncing the following core Streams:

* [Calls](https://apidocs.callrail.com/#calls)
* [Companies](https://apidocs.callrail.com/#companies)
* [Text Messages](https://apidocs.callrail.com/#text-messages)
* [Users](https://apidocs.callrail.com/#users)

### Features[​](#features "Direct link to Features")

| Feature                   | Supported? |
| ------------------------- | ---------- |
| Full Refresh Sync         | Yes        |
| Incremental - Append Sync | Yes        |
| Incremental - Dedupe Sync | Yes        |
| SSL connection            | No         |
| Namespaces                | No         |

## Getting started[​](#getting-started "Direct link to Getting started")

### Requirements[​](#requirements "Direct link to Requirements")

* CallRail Account
* CallRail API Token

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

account\_id

required

string

account\_id

›

api\_key

required

string

api\_key

›

start\_date

required

string

start\_date

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                        |
| ------- | ---------- | -------------------------------------------------------- | ---------------------------------------------- |
| 0.2.13  | 2025-05-17 | [60647](https://github.com/airbytehq/airbyte/pull/60647) | Update dependencies                            |
| 0.2.12  | 2025-05-10 | [59890](https://github.com/airbytehq/airbyte/pull/59890) | Update dependencies                            |
| 0.2.11  | 2025-05-03 | [59303](https://github.com/airbytehq/airbyte/pull/59303) | Update dependencies                            |
| 0.2.10  | 2025-04-26 | [58699](https://github.com/airbytehq/airbyte/pull/58699) | Update dependencies                            |
| 0.2.9   | 2025-04-19 | [58234](https://github.com/airbytehq/airbyte/pull/58234) | Update dependencies                            |
| 0.2.8   | 2025-04-12 | [57612](https://github.com/airbytehq/airbyte/pull/57612) | Update dependencies                            |
| 0.2.7   | 2025-04-05 | [57161](https://github.com/airbytehq/airbyte/pull/57161) | Update dependencies                            |
| 0.2.6   | 2025-03-29 | [56589](https://github.com/airbytehq/airbyte/pull/56589) | Update dependencies                            |
| 0.2.5   | 2025-03-22 | [56145](https://github.com/airbytehq/airbyte/pull/56145) | Update dependencies                            |
| 0.2.4   | 2025-03-08 | [55415](https://github.com/airbytehq/airbyte/pull/55415) | Update dependencies                            |
| 0.2.3   | 2025-03-01 | [54887](https://github.com/airbytehq/airbyte/pull/54887) | Update dependencies                            |
| 0.2.2   | 2025-02-22 | [54241](https://github.com/airbytehq/airbyte/pull/54241) | Update dependencies                            |
| 0.2.1   | 2025-02-15 | [47584](https://github.com/airbytehq/airbyte/pull/47584) | Update dependencies                            |
| 0.2.0   | 2024-08-23 | [44591](https://github.com/airbytehq/airbyte/pull/44591) | Refactor connector to manifest-only format     |
| 0.1.14  | 2024-08-17 | [44240](https://github.com/airbytehq/airbyte/pull/44240) | Update dependencies                            |
| 0.1.13  | 2024-08-12 | [43796](https://github.com/airbytehq/airbyte/pull/43796) | Update dependencies                            |
| 0.1.12  | 2024-08-10 | [43705](https://github.com/airbytehq/airbyte/pull/43705) | Update dependencies                            |
| 0.1.11  | 2024-08-03 | [43173](https://github.com/airbytehq/airbyte/pull/43173) | Update dependencies                            |
| 0.1.10  | 2024-07-27 | [42619](https://github.com/airbytehq/airbyte/pull/42619) | Update dependencies                            |
| 0.1.9   | 2024-07-20 | [42229](https://github.com/airbytehq/airbyte/pull/42229) | Update dependencies                            |
| 0.1.8   | 2024-07-13 | [41788](https://github.com/airbytehq/airbyte/pull/41788) | Update dependencies                            |
| 0.1.7   | 2024-07-10 | [41551](https://github.com/airbytehq/airbyte/pull/41551) | Update dependencies                            |
| 0.1.6   | 2024-07-09 | [41129](https://github.com/airbytehq/airbyte/pull/41129) | Update dependencies                            |
| 0.1.5   | 2024-07-06 | [40833](https://github.com/airbytehq/airbyte/pull/40833) | Update dependencies                            |
| 0.1.4   | 2024-06-25 | [40335](https://github.com/airbytehq/airbyte/pull/40335) | Update dependencies                            |
| 0.1.3   | 2024-06-22 | [39949](https://github.com/airbytehq/airbyte/pull/39949) | Update dependencies                            |
| 0.1.2   | 2024-06-06 | [39281](https://github.com/airbytehq/airbyte/pull/39281) | \[autopull] Upgrade base image to v1.2.2       |
| 0.1.1   | 2024-05-21 | [38531](https://github.com/airbytehq/airbyte/pull/38531) | \[autopull] base image + poetry + up\_to\_date |
| 0.1.0   | 2022-10-31 | [18739](https://github.com/airbytehq/airbyte/pull/18739) | 🎉 New Source: CallRail                        |
