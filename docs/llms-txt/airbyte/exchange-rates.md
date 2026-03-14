# Source: https://docs.airbyte.com/integrations/sources/exchange-rates.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-exchange-rates/latest/icon.svg)

# Exchange Rates API

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.4.46](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-exchange-rates)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-exchange-rates)(last updated 2 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `e2b40e36-aa0e-4bed-b41b-bcea6fa348b1`

This page contains the setup guide and reference information for the [Exchange Rates API](https://exchangeratesapi.io/) source connector.

## Overview[​](#overview "Direct link to Overview")

The Exchange Rates API integration is a toy integration to demonstrate how Airbyte works with a very simple source.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Exchange Rates API account
* API Access Key

## Setup Guide[​](#setup-guide "Direct link to Setup Guide")

### Step 1: Set up Exchange Rates API[​](#step-1-set-up-exchange-rates-api "Direct link to Step 1: Set up Exchange Rates API")

1. Create an account with [Exchange Rates API](https://manage.exchangeratesapi.io/signup/).
2. Navigate to the [Exchange Rates API Dashboard](https://manage.exchangeratesapi.io/dashboard) to find your `API Access Key`.

note

If you have a `free` subscription plan, you will have two limitations to the plan:

1. Limit of 1,000 API calls per month
2. You won't be able to specify the `base` parameter, meaning that you will be only be allowed to use the default base value which is `EUR`.

### Step 2: Set up the Exchange Rates connector in Airbyte[​](#step-2-set-up-the-exchange-rates-connector-in-airbyte "Direct link to Step 2: Set up the Exchange Rates connector in Airbyte")

1. Enter a **Name** for your source.
2. Enter your **API key** as the `access_key` from the prerequisites.
3. Enter the **Start Date** in YYYY-MM-DD format. The data added on and after this date will be replicated.
4. (Optional) Enter a **base** currency. For those on the free plan, `EUR` is the only option available. If none are specified, `EUR` will be used.
5. Click **Set up source**.

## Supported sync modes[​](#supported-sync-modes "Direct link to Supported sync modes")

| Feature                   | Supported? |
| ------------------------- | ---------- |
| Full Refresh Sync         | Yes        |
| Incremental - Append Sync | Yes        |
| Namespaces                | No         |

## Supported streams[​](#supported-streams "Direct link to Supported streams")

It contains one stream: `exchange_rates`

Each record in the stream contains many fields:

* The date of the record.
* One field for every supported [currency](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) which contain the value of that currency on that date.

## Data type map[​](#data-type-map "Direct link to Data type map")

| Field    | Airbyte Type |
| -------- | ------------ |
| Currency | `number`     |
| Date     | `string`     |

## Limitations & Troubleshooting[​](#limitations--troubleshooting "Direct link to Limitations & Troubleshooting")

Expand to see details about Exchange Rates API connector limitations and troubleshooting.

### Connector limitations[​](#connector-limitations "Direct link to Connector limitations")

#### Rate limiting[​](#rate-limiting "Direct link to Rate limiting")

The Exchange Rates API has rate limits that vary per pricing plan. The free plan is subject to rate limiting of 1,000 requests per month. Review the [Exchange Rates API Pricing Plans](https://exchangeratesapi.io/#pricing_plan) for more information.

### Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

* With the free plan, you won't be able to specify the `base` parameter, meaning that you will be only be allowed to use the default base value which is `EUR`.
* Check out common troubleshooting issues for the Exchange Rates API source connector on our [Airbyte Forum](https://github.com/airbytehq/airbyte/discussions).

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

access\_key

required

string

access\_key

›

start\_date

required

string

start\_date

›

base

string

base

›

ignore\_weekends

boolean

ignore\_weekends

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                                                              |
| ------- | ---------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| 1.4.46  | 2026-03-10 | [74462](https://github.com/airbytehq/airbyte/pull/74462) | Update dependencies                                                                                                  |
| 1.4.45  | 2026-02-24 | [73899](https://github.com/airbytehq/airbyte/pull/73899) | Update dependencies                                                                                                  |
| 1.4.44  | 2026-02-17 | [73457](https://github.com/airbytehq/airbyte/pull/73457) | Update dependencies                                                                                                  |
| 1.4.43  | 2026-02-10 | [73010](https://github.com/airbytehq/airbyte/pull/73010) | Update dependencies                                                                                                  |
| 1.4.42  | 2026-01-20 | [71902](https://github.com/airbytehq/airbyte/pull/71902) | Update dependencies                                                                                                  |
| 1.4.41  | 2026-01-14 | [71608](https://github.com/airbytehq/airbyte/pull/71608) | Update dependencies                                                                                                  |
| 1.4.40  | 2025-12-18 | [70600](https://github.com/airbytehq/airbyte/pull/70600) | Update dependencies                                                                                                  |
| 1.4.39  | 2025-11-25 | [70166](https://github.com/airbytehq/airbyte/pull/70166) | Update dependencies                                                                                                  |
| 1.4.38  | 2025-11-18 | [69393](https://github.com/airbytehq/airbyte/pull/69393) | Update dependencies                                                                                                  |
| 1.4.37  | 2025-10-29 | [68716](https://github.com/airbytehq/airbyte/pull/68716) | Update dependencies                                                                                                  |
| 1.4.36  | 2025-10-21 | [68560](https://github.com/airbytehq/airbyte/pull/68560) | Update dependencies                                                                                                  |
| 1.4.35  | 2025-10-14 | [67766](https://github.com/airbytehq/airbyte/pull/67766) | Update dependencies                                                                                                  |
| 1.4.34  | 2025-10-07 | [67277](https://github.com/airbytehq/airbyte/pull/67277) | Update dependencies                                                                                                  |
| 1.4.33  | 2025-09-30 | [65808](https://github.com/airbytehq/airbyte/pull/65808) | Update dependencies                                                                                                  |
| 1.4.32  | 2025-08-23 | [65295](https://github.com/airbytehq/airbyte/pull/65295) | Update dependencies                                                                                                  |
| 1.4.31  | 2025-08-09 | [64761](https://github.com/airbytehq/airbyte/pull/64761) | Update dependencies                                                                                                  |
| 1.4.30  | 2025-08-02 | [64335](https://github.com/airbytehq/airbyte/pull/64335) | Update dependencies                                                                                                  |
| 1.4.29  | 2025-07-26 | [64014](https://github.com/airbytehq/airbyte/pull/64014) | Update dependencies                                                                                                  |
| 1.4.28  | 2025-07-19 | [63607](https://github.com/airbytehq/airbyte/pull/63607) | Update dependencies                                                                                                  |
| 1.4.27  | 2025-07-12 | [62957](https://github.com/airbytehq/airbyte/pull/62957) | Update dependencies                                                                                                  |
| 1.4.26  | 2025-07-05 | [62781](https://github.com/airbytehq/airbyte/pull/62781) | Update dependencies                                                                                                  |
| 1.4.25  | 2025-06-28 | [62431](https://github.com/airbytehq/airbyte/pull/62431) | Update dependencies                                                                                                  |
| 1.4.24  | 2025-06-21 | [61941](https://github.com/airbytehq/airbyte/pull/61941) | Update dependencies                                                                                                  |
| 1.4.23  | 2025-06-14 | [61277](https://github.com/airbytehq/airbyte/pull/61277) | Update dependencies                                                                                                  |
| 1.4.22  | 2025-05-24 | [60376](https://github.com/airbytehq/airbyte/pull/60376) | Update dependencies                                                                                                  |
| 1.4.21  | 2025-05-10 | [60018](https://github.com/airbytehq/airbyte/pull/60018) | Update dependencies                                                                                                  |
| 1.4.20  | 2025-05-03 | [58841](https://github.com/airbytehq/airbyte/pull/58841) | Update dependencies                                                                                                  |
| 1.4.19  | 2025-04-19 | [58307](https://github.com/airbytehq/airbyte/pull/58307) | Update dependencies                                                                                                  |
| 1.4.18  | 2025-04-12 | [57765](https://github.com/airbytehq/airbyte/pull/57765) | Update dependencies                                                                                                  |
| 1.4.17  | 2025-04-05 | [57201](https://github.com/airbytehq/airbyte/pull/57201) | Update dependencies                                                                                                  |
| 1.4.16  | 2025-03-29 | [56474](https://github.com/airbytehq/airbyte/pull/56474) | Update dependencies                                                                                                  |
| 1.4.15  | 2025-03-22 | [55944](https://github.com/airbytehq/airbyte/pull/55944) | Update dependencies                                                                                                  |
| 1.4.14  | 2025-03-08 | [55292](https://github.com/airbytehq/airbyte/pull/55292) | Update dependencies                                                                                                  |
| 1.4.13  | 2025-03-01 | [54926](https://github.com/airbytehq/airbyte/pull/54926) | Update dependencies                                                                                                  |
| 1.4.12  | 2025-02-22 | [54447](https://github.com/airbytehq/airbyte/pull/54447) | Update dependencies                                                                                                  |
| 1.4.11  | 2025-02-15 | [53740](https://github.com/airbytehq/airbyte/pull/53740) | Update dependencies                                                                                                  |
| 1.4.10  | 2025-02-08 | [53379](https://github.com/airbytehq/airbyte/pull/53379) | Update dependencies                                                                                                  |
| 1.4.9   | 2025-02-01 | [52798](https://github.com/airbytehq/airbyte/pull/52798) | Update dependencies                                                                                                  |
| 1.4.8   | 2025-01-25 | [51697](https://github.com/airbytehq/airbyte/pull/51697) | Update dependencies                                                                                                  |
| 1.4.7   | 2025-01-11 | [51108](https://github.com/airbytehq/airbyte/pull/51108) | Update dependencies                                                                                                  |
| 1.4.6   | 2024-12-28 | [49990](https://github.com/airbytehq/airbyte/pull/49990) | Update dependencies                                                                                                  |
| 1.4.5   | 2024-12-14 | [49478](https://github.com/airbytehq/airbyte/pull/49478) | Update dependencies                                                                                                  |
| 1.4.4   | 2024-12-12 | [49196](https://github.com/airbytehq/airbyte/pull/49196) | Update dependencies                                                                                                  |
| 1.4.3   | 2024-10-29 | [47813](https://github.com/airbytehq/airbyte/pull/47813) | Update dependencies                                                                                                  |
| 1.4.2   | 2024-10-28 | [47549](https://github.com/airbytehq/airbyte/pull/47549) | Update dependencies                                                                                                  |
| 1.4.1   | 2024-08-16 | [44196](https://github.com/airbytehq/airbyte/pull/44196) | Bump source-declarative-manifest version                                                                             |
| 1.4.0   | 2024-08-15 | [44150](https://github.com/airbytehq/airbyte/pull/44150) | Refactor connector to manifest-only format                                                                           |
| 1.3.11  | 2024-08-12 | [43761](https://github.com/airbytehq/airbyte/pull/43761) | Update dependencies                                                                                                  |
| 1.3.10  | 2024-08-10 | [43639](https://github.com/airbytehq/airbyte/pull/43639) | Update dependencies                                                                                                  |
| 1.3.9   | 2024-08-03 | [42659](https://github.com/airbytehq/airbyte/pull/42659) | Update dependencies                                                                                                  |
| 1.3.8   | 2024-07-20 | [42348](https://github.com/airbytehq/airbyte/pull/42348) | Update dependencies                                                                                                  |
| 1.3.7   | 2024-07-13 | [41157](https://github.com/airbytehq/airbyte/pull/41157) | Update dependencies                                                                                                  |
| 1.3.6   | 2024-07-06 | [40924](https://github.com/airbytehq/airbyte/pull/40924) | Update dependencies                                                                                                  |
| 1.3.5   | 2024-06-26 | [40508](https://github.com/airbytehq/airbyte/pull/40508) | Update dependencies                                                                                                  |
| 1.3.4   | 2024-06-23 | [40125](https://github.com/airbytehq/airbyte/pull/40125) | Update dependencies                                                                                                  |
| 1.3.3   | 2024-05-30 | [38543](https://github.com/airbytehq/airbyte/pull/38543) | \[autopull] base image + poetry + up\_to\_date                                                                       |
| 1.3.2   | 2024-06-06 | [39250](https://github.com/airbytehq/airbyte/pull/39250) | \[autopull] Upgrade base image to v1.2.2                                                                             |
| 1.3.1   | 2024-05-30 | [38135](https://github.com/airbytehq/airbyte/pull/38135) | Make connector compatable with the builder                                                                           |
| 1.3.0   | 2023-08-25 | [29299](https://github.com/airbytehq/airbyte/pull/29299) | Migrate to low-code                                                                                                  |
| 1.2.9   | 2023-08-15 | [23000](https://github.com/airbytehq/airbyte/pull/23000) | Fix schema and tests                                                                                                 |
| 1.2.8   | 2023-02-14 | [23000](https://github.com/airbytehq/airbyte/pull/23000) | Specified date formatting in specification                                                                           |
| 1.2.7   | 2022-10-31 | [18726](https://github.com/airbytehq/airbyte/pull/18726) | Fix handling error during check connection                                                                           |
| 1.2.6   | 2022-08-23 | [15884](https://github.com/airbytehq/airbyte/pull/15884) | Migrated to new API Layer endpoint                                                                                   |
| 0.2.6   | 2022-04-20 | [12230](https://github.com/airbytehq/airbyte/pull/12230) | Update connector to use a `spec.yaml`                                                                                |
| 0.2.5   | 2021-11-12 | [7936](https://github.com/airbytehq/airbyte/pull/7936)   | Add ignore\_weekends boolean option                                                                                  |
| 0.2.4   | 2021-11-08 | [7499](https://github.com/airbytehq/airbyte/pull/7499)   | Remove base-python dependencies                                                                                      |
| 0.2.3   | 2021-06-06 | [3973](https://github.com/airbytehq/airbyte/pull/3973)   | Add `AIRBYTE_ENTRYPOINT` for kubernetes support                                                                      |
| 0.2.2   | 2021-05-28 | [3677](https://github.com/airbytehq/airbyte/pull/3677)   | Adding clearer error message when a currency isn't supported. access\_key field in spec.json was marked as sensitive |
| 0.2.0   | 2021-05-26 | [3566](https://github.com/airbytehq/airbyte/pull/3566)   | Move from `api.ratesapi.io/` to `api.exchangeratesapi.io/`. Add required field `access_key` to `config.json`.        |
| 0.1.0   | 2021-04-19 | [2942](https://github.com/airbytehq/airbyte/pull/2942)   | Implement Exchange API using the CDK                                                                                 |
