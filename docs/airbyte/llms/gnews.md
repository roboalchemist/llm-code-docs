# Source: https://docs.airbyte.com/integrations/sources/gnews.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-gnews/latest/icon.svg)

# GNews

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.2.23](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-gnews)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-gnews)(last updated 4 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `ce38aec4-5a77-439a-be29-9ca44fd4e811`

## Overview[​](#overview "Direct link to Overview")

The GNews source supports full refresh syncs

### Output schema[​](#output-schema "Direct link to Output schema")

Two output streams are available from this source:

\_[Search](https://gnews.io/docs/v4?shell#search-endpoint). \_[Top Headlines](https://gnews.io/docs/v4?shell#top-headlines-endpoint).

### Features[​](#features "Direct link to Features")

| Feature           | Supported? |
| ----------------- | ---------- |
| Full Refresh Sync | Yes        |
| Incremental Sync  | Yes        |

### Performance considerations[​](#performance-considerations "Direct link to Performance considerations")

Rate Limiting is based on the API Key tier subscription, get more info [here](https://gnews.io/#pricing).

## Getting started[​](#getting-started "Direct link to Getting started")

### Requirements[​](#requirements "Direct link to Requirements")

* GNews API Key.

### Connect using `API Key`:[​](#connect-using-api-key "Direct link to connect-using-api-key")

1. Generate an API Key as described [here](https://gnews.io/docs/v4?shell#authentication).
2. Use the generated `API Key` in the Airbyte connection.

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

Query

required

string

query

›

Country

string

country

›

End Date

string

end\_date

›

In

array\<string>

in

Language

string

language

›

Nullable

array\<string>

nullable

›

Sort By

string

sortby

›

Start Date

string

start\_date

›

Top Headlines Query

string

top\_headlines\_query

›

Top Headlines Topic

string

top\_headlines\_topic

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                          |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------ |
| 0.2.23  | 2025-05-24 | [60638](https://github.com/airbytehq/airbyte/pull/60638) | Update dependencies                              |
| 0.2.22  | 2025-05-10 | [59267](https://github.com/airbytehq/airbyte/pull/59267) | Update dependencies                              |
| 0.2.21  | 2025-04-26 | [58763](https://github.com/airbytehq/airbyte/pull/58763) | Update dependencies                              |
| 0.2.20  | 2025-04-19 | [58197](https://github.com/airbytehq/airbyte/pull/58197) | Update dependencies                              |
| 0.2.19  | 2025-04-12 | [57729](https://github.com/airbytehq/airbyte/pull/57729) | Update dependencies                              |
| 0.2.18  | 2025-04-05 | [57216](https://github.com/airbytehq/airbyte/pull/57216) | Update dependencies                              |
| 0.2.17  | 2025-03-29 | [56548](https://github.com/airbytehq/airbyte/pull/56548) | Update dependencies                              |
| 0.2.16  | 2025-03-22 | [55930](https://github.com/airbytehq/airbyte/pull/55930) | Update dependencies                              |
| 0.2.15  | 2025-03-08 | [55273](https://github.com/airbytehq/airbyte/pull/55273) | Update dependencies                              |
| 0.2.14  | 2025-03-01 | [54964](https://github.com/airbytehq/airbyte/pull/54964) | Update dependencies                              |
| 0.2.13  | 2025-02-22 | [54380](https://github.com/airbytehq/airbyte/pull/54380) | Update dependencies                              |
| 0.2.12  | 2025-02-15 | [53745](https://github.com/airbytehq/airbyte/pull/53745) | Update dependencies                              |
| 0.2.11  | 2025-02-08 | [53366](https://github.com/airbytehq/airbyte/pull/53366) | Update dependencies                              |
| 0.2.10  | 2025-02-01 | [52861](https://github.com/airbytehq/airbyte/pull/52861) | Update dependencies                              |
| 0.2.9   | 2025-01-25 | [52320](https://github.com/airbytehq/airbyte/pull/52320) | Update dependencies                              |
| 0.2.8   | 2025-01-18 | [51622](https://github.com/airbytehq/airbyte/pull/51622) | Update dependencies                              |
| 0.2.7   | 2025-01-11 | [51072](https://github.com/airbytehq/airbyte/pull/51072) | Update dependencies                              |
| 0.2.6   | 2024-12-28 | [50535](https://github.com/airbytehq/airbyte/pull/50535) | Update dependencies                              |
| 0.2.5   | 2024-12-21 | [50037](https://github.com/airbytehq/airbyte/pull/50037) | Update dependencies                              |
| 0.2.4   | 2024-12-14 | [49521](https://github.com/airbytehq/airbyte/pull/49521) | Update dependencies                              |
| 0.2.3   | 2024-12-12 | [48214](https://github.com/airbytehq/airbyte/pull/48214) | Update dependencies                              |
| 0.2.2   | 2024-10-29 | [47918](https://github.com/airbytehq/airbyte/pull/47918) | Update dependencies                              |
| 0.2.1   | 2024-10-28 | [47499](https://github.com/airbytehq/airbyte/pull/47499) | Update dependencies                              |
| 0.2.0   | 2024-10-17 | [46959](https://github.com/airbytehq/airbyte/pull/46959) | Refactor connector to manifest-only format       |
| 0.1.25  | 2024-10-12 | [46802](https://github.com/airbytehq/airbyte/pull/46802) | Update dependencies                              |
| 0.1.24  | 2024-10-05 | [46425](https://github.com/airbytehq/airbyte/pull/46425) | Update dependencies                              |
| 0.1.23  | 2024-09-28 | [46209](https://github.com/airbytehq/airbyte/pull/46209) | Update dependencies                              |
| 0.1.22  | 2024-09-21 | [45808](https://github.com/airbytehq/airbyte/pull/45808) | Update dependencies                              |
| 0.1.21  | 2024-09-14 | [45541](https://github.com/airbytehq/airbyte/pull/45541) | Update dependencies                              |
| 0.1.20  | 2024-09-07 | [45290](https://github.com/airbytehq/airbyte/pull/45290) | Update dependencies                              |
| 0.1.19  | 2024-08-31 | [45034](https://github.com/airbytehq/airbyte/pull/45034) | Update dependencies                              |
| 0.1.18  | 2024-08-24 | [44631](https://github.com/airbytehq/airbyte/pull/44631) | Update dependencies                              |
| 0.1.17  | 2024-08-17 | [44355](https://github.com/airbytehq/airbyte/pull/44355) | Update dependencies                              |
| 0.1.16  | 2024-08-12 | [43922](https://github.com/airbytehq/airbyte/pull/43922) | Update dependencies                              |
| 0.1.15  | 2024-08-10 | [43659](https://github.com/airbytehq/airbyte/pull/43659) | Update dependencies                              |
| 0.1.14  | 2024-08-03 | [43263](https://github.com/airbytehq/airbyte/pull/43263) | Update dependencies                              |
| 0.1.13  | 2024-07-27 | [42634](https://github.com/airbytehq/airbyte/pull/42634) | Update dependencies                              |
| 0.1.12  | 2024-07-20 | [42340](https://github.com/airbytehq/airbyte/pull/42340) | Update dependencies                              |
| 0.1.11  | 2024-07-13 | [41832](https://github.com/airbytehq/airbyte/pull/41832) | Update dependencies                              |
| 0.1.10  | 2024-07-10 | [41461](https://github.com/airbytehq/airbyte/pull/41461) | Update dependencies                              |
| 0.1.9   | 2024-07-09 | [41179](https://github.com/airbytehq/airbyte/pull/41179) | Update dependencies                              |
| 0.1.8   | 2024-07-06 | [40892](https://github.com/airbytehq/airbyte/pull/40892) | Update dependencies                              |
| 0.1.7   | 2024-06-25 | [40281](https://github.com/airbytehq/airbyte/pull/40281) | Update dependencies                              |
| 0.1.6   | 2024-06-22 | [40196](https://github.com/airbytehq/airbyte/pull/40196) | Update dependencies                              |
| 0.1.5   | 2024-06-06 | [39188](https://github.com/airbytehq/airbyte/pull/39188) | \[autopull] Upgrade base image to v1.2.2         |
| 0.1.4   | 2024-05-20 | [38394](https://github.com/airbytehq/airbyte/pull/38394) | \[autopull] base image + poetry + up\_to\_date   |
| 0.1.3   | 2022-12-16 | [21322](https://github.com/airbytehq/airbyte/pull/21322) | Reorganize manifest inline stream schemas        |
| 0.1.2   | 2022-12-16 | [20405](https://github.com/airbytehq/airbyte/pull/20405) | Update the manifest to use inline stream schemas |
| 0.1.1   | 2022-12-13 | [20460](https://github.com/airbytehq/airbyte/pull/20460) | Update source acceptance test config             |
| 0.1.0   | 2022-11-01 | [18808](https://github.com/airbytehq/airbyte/pull/18808) | 🎉 New Source: GNews                             |
