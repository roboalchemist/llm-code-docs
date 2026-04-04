# Source: https://docs.airbyte.com/integrations/sources/pingdom.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-pingdom/latest/icon.svg)

# Pingdom

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.1](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-pingdom)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-pingdom)(last updated a year ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `14fb7a17-a371-4ebc-a072-b339c4daa4c1`

This Source is capable of syncing the following core Streams:

* [checks](https://docs.pingdom.com/api/#tag/Checks/paths/~1checks/get)
* [performance](https://docs.pingdom.com/api/#tag/Summary.performance/paths/~1summary.performance~1%7Bcheckid%7D/get)

## Requirements[​](#requirements "Direct link to Requirements")

* **Pingdom API Key**.\[required] See the [PingDom API docs](https://docs.pingdom.com/api/#section/Authentication) for information on how to obtain the API token.
* **Start date**.\[required]. To Fetch data from. Only use for Incremental way.
* **Probes**\[optional]. Filter to only use results from a list of probes. Format is a comma separated list of probe identifiers.
* **Resolution**\[optional]. Interval Size. Should be `hour`, `day`, `week`. Default: `hour`

## Configuration[​](#configuration "Direct link to Configuration")

| Input        | Type     | Description | Default Value |
| ------------ | -------- | ----------- | ------------- |
| `probes`     | `string` | probes.     |               |
| `api_key`    | `string` | API Key.    |               |
| `resolution` | `string` | resolution. | hour          |
| `start_date` | `string` | Start date. |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name | Primary Key | Pagination       | Supports Full Sync | Supports Incremental |
| ----------- | ----------- | ---------------- | ------------------ | -------------------- |
| checks      | id          | DefaultPaginator | ✅                 | ❌                   |
| performance |             | No pagination    | ✅                 | ✅                   |

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

probes

string

probes

›

resolution

string

resolution

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Subject                                                                       |
| ------- | ---------- | ----------------------------------------------------------------------------- |
| 0.0.1   | 2024-12-03 | Initial release by [@KimPlv](https://github.com/KimPlv) via Connector Builder |
