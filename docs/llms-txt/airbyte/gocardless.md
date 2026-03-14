# Source: https://docs.airbyte.com/integrations/sources/gocardless.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-gocardless/latest/icon.svg)

# GoCardless

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.2.24](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-gocardless)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-gocardless)(last updated 4 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `ba15ac82-5c6a-4fb2-bf24-925c23a1180c`

## Overview[​](#overview "Direct link to Overview")

The GoCardless source can sync data from the [GoCardless API](https://gocardless.com/)

#### Output schema[​](#output-schema "Direct link to Output schema")

This source is capable of syncing the following streams:

* Mandates
* Payments
* Payouts
* Refunds

#### Features[​](#features "Direct link to Features")

| Feature                   | Supported? |
| ------------------------- | ---------- |
| Full Refresh Sync         | Yes        |
| Incremental - Append Sync | No         |
| Namespaces                | No         |

### Requirements / Setup Guide[​](#requirements--setup-guide "Direct link to Requirements / Setup Guide")

* Access Token
* GoCardless Environment
* GoCardless Version
* Start Date

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

Access Token

required

string

access\_token

›

GoCardless API Environment

required

string

gocardless\_environment

›

GoCardless API Version

required

string

gocardless\_version

›

Start Date

required

string

start\_date

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                        |
| ------- | ---------- | -------------------------------------------------------- | ---------------------------------------------- |
| 0.2.24  | 2025-05-24 | [60712](https://github.com/airbytehq/airbyte/pull/60712) | Update dependencies                            |
| 0.2.23  | 2025-05-10 | [59846](https://github.com/airbytehq/airbyte/pull/59846) | Update dependencies                            |
| 0.2.22  | 2025-05-03 | [59227](https://github.com/airbytehq/airbyte/pull/59227) | Update dependencies                            |
| 0.2.21  | 2025-04-26 | [58800](https://github.com/airbytehq/airbyte/pull/58800) | Update dependencies                            |
| 0.2.20  | 2025-04-19 | [58171](https://github.com/airbytehq/airbyte/pull/58171) | Update dependencies                            |
| 0.2.19  | 2025-04-12 | [57743](https://github.com/airbytehq/airbyte/pull/57743) | Update dependencies                            |
| 0.2.18  | 2025-04-05 | [57277](https://github.com/airbytehq/airbyte/pull/57277) | Update dependencies                            |
| 0.2.17  | 2025-03-29 | [56523](https://github.com/airbytehq/airbyte/pull/56523) | Update dependencies                            |
| 0.2.16  | 2025-03-22 | [55929](https://github.com/airbytehq/airbyte/pull/55929) | Update dependencies                            |
| 0.2.15  | 2025-03-08 | [55296](https://github.com/airbytehq/airbyte/pull/55296) | Update dependencies                            |
| 0.2.14  | 2025-03-01 | [54950](https://github.com/airbytehq/airbyte/pull/54950) | Update dependencies                            |
| 0.2.13  | 2025-02-22 | [54452](https://github.com/airbytehq/airbyte/pull/54452) | Update dependencies                            |
| 0.2.12  | 2025-02-15 | [53347](https://github.com/airbytehq/airbyte/pull/53347) | Update dependencies                            |
| 0.2.11  | 2025-02-01 | [52820](https://github.com/airbytehq/airbyte/pull/52820) | Update dependencies                            |
| 0.2.10  | 2025-01-25 | [52374](https://github.com/airbytehq/airbyte/pull/52374) | Update dependencies                            |
| 0.2.9   | 2025-01-18 | [51640](https://github.com/airbytehq/airbyte/pull/51640) | Update dependencies                            |
| 0.2.8   | 2025-01-11 | [51127](https://github.com/airbytehq/airbyte/pull/51127) | Update dependencies                            |
| 0.2.7   | 2024-12-28 | [50514](https://github.com/airbytehq/airbyte/pull/50514) | Update dependencies                            |
| 0.2.6   | 2024-12-21 | [50023](https://github.com/airbytehq/airbyte/pull/50023) | Update dependencies                            |
| 0.2.5   | 2024-12-14 | [49505](https://github.com/airbytehq/airbyte/pull/49505) | Update dependencies                            |
| 0.2.4   | 2024-12-12 | [49169](https://github.com/airbytehq/airbyte/pull/49169) | Update dependencies                            |
| 0.2.3   | 2024-11-04 | [48295](https://github.com/airbytehq/airbyte/pull/48295) | Update dependencies                            |
| 0.2.2   | 2024-10-29 | [47772](https://github.com/airbytehq/airbyte/pull/47772) | Update dependencies                            |
| 0.2.1   | 2024-08-16 | [44196](https://github.com/airbytehq/airbyte/pull/44196) | Bump source-declarative-manifest version       |
| 0.2.0   | 2024-08-15 | [44145](https://github.com/airbytehq/airbyte/pull/44145) | Refactor connector to manifest-only format     |
| 0.1.14  | 2024-08-12 | [43840](https://github.com/airbytehq/airbyte/pull/43840) | Update dependencies                            |
| 0.1.13  | 2024-08-10 | [43706](https://github.com/airbytehq/airbyte/pull/43706) | Update dependencies                            |
| 0.1.12  | 2024-08-03 | [43230](https://github.com/airbytehq/airbyte/pull/43230) | Update dependencies                            |
| 0.1.11  | 2024-07-27 | [42810](https://github.com/airbytehq/airbyte/pull/42810) | Update dependencies                            |
| 0.1.10  | 2024-07-20 | [42223](https://github.com/airbytehq/airbyte/pull/42223) | Update dependencies                            |
| 0.1.9   | 2024-07-13 | [41826](https://github.com/airbytehq/airbyte/pull/41826) | Update dependencies                            |
| 0.1.8   | 2024-07-10 | [41559](https://github.com/airbytehq/airbyte/pull/41559) | Update dependencies                            |
| 0.1.7   | 2024-07-09 | [41291](https://github.com/airbytehq/airbyte/pull/41291) | Update dependencies                            |
| 0.1.6   | 2024-07-06 | [40846](https://github.com/airbytehq/airbyte/pull/40846) | Update dependencies                            |
| 0.1.5   | 2024-06-25 | [40370](https://github.com/airbytehq/airbyte/pull/40370) | Update dependencies                            |
| 0.1.4   | 2024-06-21 | [39946](https://github.com/airbytehq/airbyte/pull/39946) | Update dependencies                            |
| 0.1.3   | 2024-06-06 | [39207](https://github.com/airbytehq/airbyte/pull/39207) | \[autopull] Upgrade base image to v1.2.2       |
| 0.1.2   | 2024-06-05 | [38818](https://github.com/airbytehq/airbyte/pull/38818) | Make compatible with the builder               |
| 0.1.1   | 2024-05-20 | [38425](https://github.com/airbytehq/airbyte/pull/38425) | \[autopull] base image + poetry + up\_to\_date |
| 0.1.0   | 2022-10-19 | [17792](https://github.com/airbytehq/airbyte/pull/17792) | Initial release supporting the GoCardless      |
