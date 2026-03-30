# Source: https://docs.airbyte.com/integrations/sources/coin-api.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-coin-api/latest/icon.svg)

# CoinAPI

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.3.22](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-coin-api)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-coin-api)(last updated 4 months ago)

* Definition ID

  `919984ef-53a2-479b-8ffe-9c1ddb9fc3f3`

## Sync overview[​](#sync-overview "Direct link to Sync overview")

This source can sync OHLCV and trades historical data for a single coin listed on [CoinAPI](https://www.coinapi.io/). It currently only supports Full Refresh syncs.

### Output schema[​](#output-schema "Direct link to Output schema")

This source is capable of syncing the following streams:

* `ohlcv_historical_data`
* `trades_historical_data`

### Features[​](#features "Direct link to Features")

| Feature           | Supported? (Yes/No) | Notes                                                   |
| ----------------- | ------------------- | ------------------------------------------------------- |
| Full Refresh Sync | Yes                 |                                                         |
| Incremental Sync  | No                  |                                                         |
| API Environments  | Yes                 | Both sandbox and production environments are supported. |

### Performance considerations[​](#performance-considerations "Direct link to Performance considerations")

CoinAPI allows only 100 daily requests on the free plan. Use of this connector may require a paid plan.

## Getting started[​](#getting-started "Direct link to Getting started")

### Requirements[​](#requirements "Direct link to Requirements")

1. Obtain an API key from [CoinAPI](https://www.coinapi.io/).
2. Choose a symbol to pull data for. You can find a list of symbols [here](https://docs.coinapi.io/#list-all-symbols-get).
3. Choose a time interval to pull data for. You can find a list of intervals [here](https://docs.coinapi.io/#list-all-periods-get).

### Setup guide[​](#setup-guide "Direct link to Setup guide")

The following fields are required fields for the connector to work:

* `api_key`: Your CoinAPI API key.
* `environment`: The environment to use. Can be either `sandbox` or `production`.
* `symbol_id`: The symbol to pull data for.
* `period`: The time interval to pull data for.
* `start_date`: The start date to pull `history` data from.
* (optional) `end_date`: The end date to pull `history` data until.
* (optional) `limit`: The maximum number of records to pull per request. Defaults to 100.

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

api\_key

required

string

api\_key

›

environment

required

string

environment

›

period

required

string

period

›

start\_date

required

string

start\_date

›

symbol\_id

required

string

symbol\_id

›

end\_date

string

end\_date

›

limit

integer

limit

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                              | Subject                                                                                     |
| ------- | ---------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 0.3.22  | 2025-05-24 | [60417](https://github.com/airbytehq/airbyte/pull/60417)  | Update dependencies                                                                         |
| 0.3.21  | 2025-05-10 | [60004](https://github.com/airbytehq/airbyte/pull/60004)  | Update dependencies                                                                         |
| 0.3.20  | 2025-05-03 | [59429](https://github.com/airbytehq/airbyte/pull/59429)  | Update dependencies                                                                         |
| 0.3.19  | 2025-04-26 | [58903](https://github.com/airbytehq/airbyte/pull/58903)  | Update dependencies                                                                         |
| 0.3.18  | 2025-04-19 | [58299](https://github.com/airbytehq/airbyte/pull/58299)  | Update dependencies                                                                         |
| 0.3.17  | 2025-04-12 | [57838](https://github.com/airbytehq/airbyte/pull/57838)  | Update dependencies                                                                         |
| 0.3.16  | 2025-04-05 | [57255](https://github.com/airbytehq/airbyte/pull/57255)  | Update dependencies                                                                         |
| 0.3.15  | 2025-03-29 | [56496](https://github.com/airbytehq/airbyte/pull/56496)  | Update dependencies                                                                         |
| 0.3.14  | 2025-03-22 | [55949](https://github.com/airbytehq/airbyte/pull/55949)  | Update dependencies                                                                         |
| 0.3.13  | 2025-03-08 | [55308](https://github.com/airbytehq/airbyte/pull/55308)  | Update dependencies                                                                         |
| 0.3.12  | 2025-03-01 | [54453](https://github.com/airbytehq/airbyte/pull/54453)  | Update dependencies                                                                         |
| 0.3.11  | 2025-02-15 | [53722](https://github.com/airbytehq/airbyte/pull/53722)  | Update dependencies                                                                         |
| 0.3.10  | 2025-02-08 | [53324](https://github.com/airbytehq/airbyte/pull/53324)  | Update dependencies                                                                         |
| 0.3.9   | 2025-02-01 | [52867](https://github.com/airbytehq/airbyte/pull/52867)  | Update dependencies                                                                         |
| 0.3.8   | 2025-01-25 | [52357](https://github.com/airbytehq/airbyte/pull/52357)  | Update dependencies                                                                         |
| 0.3.7   | 2025-01-18 | [51654](https://github.com/airbytehq/airbyte/pull/51654)  | Update dependencies                                                                         |
| 0.3.6   | 2025-01-11 | [51125](https://github.com/airbytehq/airbyte/pull/51125)  | Update dependencies                                                                         |
| 0.3.5   | 2024-12-28 | [50027](https://github.com/airbytehq/airbyte/pull/50027)  | Update dependencies                                                                         |
| 0.3.4   | 2024-12-14 | [49503](https://github.com/airbytehq/airbyte/pull/49503)  | Update dependencies                                                                         |
| 0.3.3   | 2024-12-12 | [49150](https://github.com/airbytehq/airbyte/pull/49150)  | Update dependencies                                                                         |
| 0.3.2   | 2024-10-29 | [47739](https://github.com/airbytehq/airbyte/pull/47739)  | Update dependencies                                                                         |
| 0.3.1   | 2024-08-16 | [44196](https://github.com/airbytehq/airbyte/pull/44196)  | Bump source-declarative-manifest version                                                    |
| 0.3.0   | 2024-08-15 | [44164](https://github.com/airbytehq/airbyte/pull/44164)  | Refactor connector to manifest-only format                                                  |
| 0.2.16  | 2024-08-10 | [43507](https://github.com/airbytehq/airbyte/pull/43507)  | Update dependencies                                                                         |
| 0.2.15  | 2024-08-03 | [43091](https://github.com/airbytehq/airbyte/pull/43091)  | Update dependencies                                                                         |
| 0.2.14  | 2024-07-27 | [42599](https://github.com/airbytehq/airbyte/pull/42599)  | Update dependencies                                                                         |
| 0.2.13  | 2024-07-20 | [42238](https://github.com/airbytehq/airbyte/pull/42238)  | Update dependencies                                                                         |
| 0.2.12  | 2024-07-13 | [41763](https://github.com/airbytehq/airbyte/pull/41763)  | Update dependencies                                                                         |
| 0.2.11  | 2024-07-10 | [41488](https://github.com/airbytehq/airbyte/pull/41488)  | Update dependencies                                                                         |
| 0.2.10  | 2024-07-09 | [41206](https://github.com/airbytehq/airbyte/pull/41206)  | Update dependencies                                                                         |
| 0.2.9   | 2024-07-06 | [40976](https://github.com/airbytehq/airbyte/pull/40976)  | Update dependencies                                                                         |
| 0.2.8   | 2024-06-26 | [40315](https://github.com/airbytehq/airbyte/pull/40315)  | Update dependencies                                                                         |
| 0.2.7   | 2024-06-22 | [40062](https://github.com/airbytehq/airbyte/pull/40062)  | Update dependencies                                                                         |
| 0.2.6   | 2024-06-06 | [39257](https://github.com/airbytehq/airbyte/pull/39257)  | \[autopull] Upgrade base image to v1.2.2                                                    |
| 0.2.5   | 2024-05-21 | [38139](https://github.com/airbytehq/airbyte/pull/38139)  | Make connector compatable with builder \`                                                   |
| 0.2.4   | 2024-04-19 | [37138](https://github.com/airbytehq/airbyte/pull/37138)  | Updating to 0.80.0 CDK                                                                      |
| 0.2.3   | 2024-04-18 | [37138](https://github.com/airbytehq/airbyte/pull/37138)  | Manage dependencies with Poetry.                                                            |
| 0.2.2   | 2024-04-15 | [37138](https://github.com/airbytehq/airbyte/pull/37138)  | Base image migration: remove Dockerfile and use the python-connector-base image             |
| 0.2.1   | 2024-04-12 | [37138](https://github.com/airbytehq/airbyte/pull/37138)  | schema descriptions                                                                         |
| 0.2.0   | 2024-02-05 | [#34826](https://github.com/airbytehq/airbyte/pull/34826) | Fix catalog types for fields `bid_price` and `bid_size` in stream `quotes_historical_data`. |
| 0.1.1   | 2022-12-19 | [#20600](https://github.com/airbytehq/airbyte/pull/20600) | Add quotes historical data stream                                                           |
| 0.1.0   | 2022-10-21 | [#18302](https://github.com/airbytehq/airbyte/pull/18302) | New source                                                                                  |
