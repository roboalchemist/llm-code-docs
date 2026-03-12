# Source: https://docs.airbyte.com/integrations/sources/criteo-marketing.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-criteo-marketing/latest/icon.svg)

# Criteo Marketing

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.1](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-criteo-marketing)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-criteo-marketing)(last updated 14 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `9a5346ac-42ee-485d-a791-d079f92ccdfc`

API documentation:

<https://developers.criteo.com/marketing-solutions/reference/getadsetreport>

## Configuration[​](#configuration "Direct link to Configuration")

| Input           | Type     | Description                                 | Default Value |
| --------------- | -------- | ------------------------------------------- | ------------- |
| `currency`      | `string` | Currency. Currency to be used on the report |               |
| `end_date`      | `string` | EndDate. End date of the report             |               |
| `client_id`     | `string` | OAuth Client ID.                            |               |
| `start_date`    | `string` | StartDate. Start date of the report         |               |
| `client_secret` | `string` | OAuth Client Secret.                        |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name      | Primary Key                 | Pagination    | Supports Full Sync | Supports Incremental |
| ---------------- | --------------------------- | ------------- | ------------------ | -------------------- |
| ad\_spend\_daily | AdvertiserId.CampaignId.Day | No pagination | ✅                 | ✅                   |
| adsets           | Id                          | No pagination | ✅                 | ❌                   |

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

OAuth Client ID

required

string

client\_id

OAuth Client Secret

required

string

client\_secret

›

Currency

required

string

currency

›

StartDate

required

string

start\_date

›

EndDate

string

end\_date

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                   |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------- |
| 0.0.2   | 2026-03-03 | [74165](https://github.com/airbytehq/airbyte/pull/74165) | Update dependencies                                                       |
| 0.0.1   | 2026-02-04 |                                                          | Initial release by [@mvfc](https://github.com/mvfc) via Connector Builder |
