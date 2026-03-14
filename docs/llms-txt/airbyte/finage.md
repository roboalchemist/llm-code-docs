# Source: https://docs.airbyte.com/integrations/sources/finage.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-finage/latest/icon.svg)

# Finage

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.47](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-finage)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-finage)(last updated 16 days ago)

* Definition ID

  `5220663f-d87b-498e-8aed-1f2d59371a61`

Real-Time Market Data Solutions for Stocks, Forex, and Crypto This connector can be used to extract data from various APIs such as symbol-list,Aggregates,Snapshot and Technical Indicators

## Configuration[​](#configuration "Direct link to Configuration")

| Input                 | Type     | Description                                                                    | Default Value |
| --------------------- | -------- | ------------------------------------------------------------------------------ | ------------- |
| `api_key`             | `string` | API Key.                                                                       |               |
| `symbols`             | `array`  | Symbols. List of symbols                                                       |               |
| `tech_indicator_type` | `string` | Technical Indicator Type. One of DEMA, EMA, SMA, WMA, RSI, TEMA, Williams, ADX | SMA           |
| `time`                | `string` | Time Interval.                                                                 | daily         |
| `period`              | `string` | Period. Time period. Default is 10                                             |               |
| `time_aggregates`     | `string` | Time aggregates. Size of the time                                              | day           |
| `time_period`         | `string` | Time Period. Time Period for cash flow stmts                                   |               |
| `start_date`          | `string` | Start date.                                                                    |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name                     | Primary Key | Pagination    | Supports Full Sync | Supports Incremental |
| ------------------------------- | ----------- | ------------- | ------------------ | -------------------- |
| market\_news                    |             | No pagination | ✅                 | ❌                   |
| most\_active\_us\_stocks        | symbol      | No pagination | ✅                 | ❌                   |
| technical\_indicators           |             | No pagination | ✅                 | ❌                   |
| economic\_calendar              |             | No pagination | ✅                 | ✅                   |
| earning\_calendar               |             | No pagination | ✅                 | ❌                   |
| delisted\_companies             | symbol      | No pagination | ✅                 | ❌                   |
| ipo\_calendar                   | symbol      | No pagination | ✅                 | ✅                   |
| historical\_stock\_split        |             | No pagination | ✅                 | ❌                   |
| historical\_dividends\_calendar |             | No pagination | ✅                 | ❌                   |
| cash\_flow\_statements          | date.symbol | No pagination | ✅                 | ❌                   |
| balance\_sheet\_statements      | date.symbol | No pagination | ✅                 | ❌                   |
| income\_statement               | date.symbol | No pagination | ✅                 | ❌                   |
| institutional\_holders          | holder      | No pagination | ✅                 | ❌                   |
| mutual\_fund\_holder            |             | No pagination | ✅                 | ❌                   |
| most\_gainers                   | symbol      | No pagination | ✅                 | ❌                   |
| most\_losers                    | symbol      | No pagination | ✅                 | ❌                   |
| sector\_performance             | sector      | No pagination | ✅                 | ❌                   |
| shares\_float                   |             | No pagination | ✅                 | ❌                   |

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

Symbols

required

array

symbols

›

Period

string

period

›

Technical Indicator Type

string

tech\_indicator\_type

›

Time Interval

string

time

›

Time aggregates

string

time\_aggregates

›

Time Period

string

time\_period

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                                 |
| ------- | ---------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 0.0.47  | 2026-02-24 | [73748](https://github.com/airbytehq/airbyte/pull/73748) | Update dependencies                                                                     |
| 0.0.46  | 2026-02-17 | [73373](https://github.com/airbytehq/airbyte/pull/73373) | Update dependencies                                                                     |
| 0.0.45  | 2026-02-10 | [73145](https://github.com/airbytehq/airbyte/pull/73145) | Update dependencies                                                                     |
| 0.0.44  | 2026-02-03 | [72562](https://github.com/airbytehq/airbyte/pull/72562) | Update dependencies                                                                     |
| 0.0.43  | 2026-01-20 | [71985](https://github.com/airbytehq/airbyte/pull/71985) | Update dependencies                                                                     |
| 0.0.42  | 2026-01-14 | [71645](https://github.com/airbytehq/airbyte/pull/71645) | Update dependencies                                                                     |
| 0.0.41  | 2025-12-18 | [70536](https://github.com/airbytehq/airbyte/pull/70536) | Update dependencies                                                                     |
| 0.0.40  | 2025-11-25 | [69966](https://github.com/airbytehq/airbyte/pull/69966) | Update dependencies                                                                     |
| 0.0.39  | 2025-11-18 | [69446](https://github.com/airbytehq/airbyte/pull/69446) | Update dependencies                                                                     |
| 0.0.38  | 2025-10-29 | [68834](https://github.com/airbytehq/airbyte/pull/68834) | Update dependencies                                                                     |
| 0.0.37  | 2025-10-21 | [68460](https://github.com/airbytehq/airbyte/pull/68460) | Update dependencies                                                                     |
| 0.0.36  | 2025-10-14 | [68063](https://github.com/airbytehq/airbyte/pull/68063) | Update dependencies                                                                     |
| 0.0.35  | 2025-10-07 | [67313](https://github.com/airbytehq/airbyte/pull/67313) | Update dependencies                                                                     |
| 0.0.34  | 2025-09-30 | [66765](https://github.com/airbytehq/airbyte/pull/66765) | Update dependencies                                                                     |
| 0.0.33  | 2025-09-24 | [65820](https://github.com/airbytehq/airbyte/pull/65820) | Update dependencies                                                                     |
| 0.0.32  | 2025-08-23 | [65239](https://github.com/airbytehq/airbyte/pull/65239) | Update dependencies                                                                     |
| 0.0.31  | 2025-08-09 | [64756](https://github.com/airbytehq/airbyte/pull/64756) | Update dependencies                                                                     |
| 0.0.30  | 2025-08-02 | [64354](https://github.com/airbytehq/airbyte/pull/64354) | Update dependencies                                                                     |
| 0.0.29  | 2025-07-26 | [63988](https://github.com/airbytehq/airbyte/pull/63988) | Update dependencies                                                                     |
| 0.0.28  | 2025-07-19 | [63602](https://github.com/airbytehq/airbyte/pull/63602) | Update dependencies                                                                     |
| 0.0.27  | 2025-07-12 | [62973](https://github.com/airbytehq/airbyte/pull/62973) | Update dependencies                                                                     |
| 0.0.26  | 2025-07-05 | [62767](https://github.com/airbytehq/airbyte/pull/62767) | Update dependencies                                                                     |
| 0.0.25  | 2025-06-28 | [62375](https://github.com/airbytehq/airbyte/pull/62375) | Update dependencies                                                                     |
| 0.0.24  | 2025-06-22 | [61991](https://github.com/airbytehq/airbyte/pull/61991) | Update dependencies                                                                     |
| 0.0.23  | 2025-06-14 | [61229](https://github.com/airbytehq/airbyte/pull/61229) | Update dependencies                                                                     |
| 0.0.22  | 2025-05-24 | [59963](https://github.com/airbytehq/airbyte/pull/59963) | Update dependencies                                                                     |
| 0.0.21  | 2025-05-03 | [59397](https://github.com/airbytehq/airbyte/pull/59397) | Update dependencies                                                                     |
| 0.0.20  | 2025-04-26 | [58878](https://github.com/airbytehq/airbyte/pull/58878) | Update dependencies                                                                     |
| 0.0.19  | 2025-04-19 | [58306](https://github.com/airbytehq/airbyte/pull/58306) | Update dependencies                                                                     |
| 0.0.18  | 2025-04-12 | [57805](https://github.com/airbytehq/airbyte/pull/57805) | Update dependencies                                                                     |
| 0.0.17  | 2025-04-05 | [57209](https://github.com/airbytehq/airbyte/pull/57209) | Update dependencies                                                                     |
| 0.0.16  | 2025-03-29 | [56488](https://github.com/airbytehq/airbyte/pull/56488) | Update dependencies                                                                     |
| 0.0.15  | 2025-03-22 | [55981](https://github.com/airbytehq/airbyte/pull/55981) | Update dependencies                                                                     |
| 0.0.14  | 2025-03-08 | [55327](https://github.com/airbytehq/airbyte/pull/55327) | Update dependencies                                                                     |
| 0.0.13  | 2025-03-01 | [54914](https://github.com/airbytehq/airbyte/pull/54914) | Update dependencies                                                                     |
| 0.0.12  | 2025-02-22 | [54384](https://github.com/airbytehq/airbyte/pull/54384) | Update dependencies                                                                     |
| 0.0.11  | 2025-02-15 | [53707](https://github.com/airbytehq/airbyte/pull/53707) | Update dependencies                                                                     |
| 0.0.10  | 2025-02-08 | [53343](https://github.com/airbytehq/airbyte/pull/53343) | Update dependencies                                                                     |
| 0.0.9   | 2025-02-01 | [52801](https://github.com/airbytehq/airbyte/pull/52801) | Update dependencies                                                                     |
| 0.0.8   | 2025-01-25 | [52345](https://github.com/airbytehq/airbyte/pull/52345) | Update dependencies                                                                     |
| 0.0.7   | 2025-01-18 | [51652](https://github.com/airbytehq/airbyte/pull/51652) | Update dependencies                                                                     |
| 0.0.6   | 2025-01-11 | [51134](https://github.com/airbytehq/airbyte/pull/51134) | Update dependencies                                                                     |
| 0.0.5   | 2024-12-28 | [50566](https://github.com/airbytehq/airbyte/pull/50566) | Update dependencies                                                                     |
| 0.0.4   | 2024-12-21 | [50058](https://github.com/airbytehq/airbyte/pull/50058) | Update dependencies                                                                     |
| 0.0.3   | 2024-12-14 | [49496](https://github.com/airbytehq/airbyte/pull/49496) | Update dependencies                                                                     |
| 0.0.2   | 2024-12-12 | [49202](https://github.com/airbytehq/airbyte/pull/49202) | Update dependencies                                                                     |
| 0.0.1   | 2024-11-11 |                                                          | Initial release by [@marcosmarxm](https://github.com/marcosmarxm) via Connector Builder |
