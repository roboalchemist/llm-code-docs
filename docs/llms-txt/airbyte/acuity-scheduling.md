# Source: https://docs.airbyte.com/integrations/sources/acuity-scheduling.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-acuity-scheduling/latest/icon.svg)

# Acuity Scheduling

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.1](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-acuity-scheduling)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-acuity-scheduling)(last updated 6 months ago)

* Definition ID

  `bc7db25c-bdfb-4ec2-96ae-a4687cead916`

Flexible scheduling software to help you succeed With seamless client scheduling, secure payments, and workflow automation, all you have to do is show up on time.

## Configuration[​](#configuration "Direct link to Configuration")

| Input        | Type     | Description | Default Value |
| ------------ | -------- | ----------- | ------------- |
| `username`   | `string` | Username.   |               |
| `password`   | `string` | Password.   |               |
| `start_date` | `string` | Start date. |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name       | Primary Key | Pagination    | Supports Full Sync | Supports Incremental |
| ----------------- | ----------- | ------------- | ------------------ | -------------------- |
| appointments      | id          | No pagination | ✅                 | ✅                   |
| calendars         | id          | No pagination | ✅                 | ❌                   |
| clients           | email       | No pagination | ✅                 | ❌                   |
| appointment-types | id          | No pagination | ✅                 | ❌                   |
| blocks            | id          | No pagination | ✅                 | ✅                   |
| labels            | id          | No pagination | ✅                 | ❌                   |
| forms             | id          | No pagination | ✅                 | ❌                   |

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

Start date

required

string

start\_date

Username

required

string

username

Password

string

password

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request | Subject                                                                               |
| ------- | ---------- | ------------ | ------------------------------------------------------------------------------------- |
| 0.0.1   | 2025-07-02 |              | Initial release by [@chanronson](https://github.com/chanronson) via Connector Builder |
