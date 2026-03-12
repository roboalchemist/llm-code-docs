# Source: https://docs.airbyte.com/integrations/sources/circleci.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-circleci/latest/icon.svg)

# Circleci

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.1.0](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-circleci)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-circleci)(last updated 4 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `dd9a9d23-a64a-483c-b1ed-da1391d13f91`

This directory contains the manifest-only connector for [`source-circleci`](https://app.circleci.com/).

## Documentation reference:[​](#documentation-reference "Direct link to Documentation reference:")

* Visit `https://circleci.com/docs/api/v1/index.html` for V1 API documentation
* Visit `https://circleci.com/docs/api/v2/index.html` for V2 API documentation

## Authentication setup[​](#authentication-setup "Direct link to Authentication setup")

`CircleCI` uses api key authentication, Visit `https://app.circleci.com/settings/user/tokens` for getting your api keys.

## Configuration[​](#configuration "Direct link to Configuration")

| Input         | Type     | Description                                                                                                                                                                              | Default Value |
| ------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `api_key`     | `string` | API Key.                                                                                                                                                                                 |               |
| `org_id`      | `string` | Organization ID. The org ID found in `https://app.circleci.com/settings/organization/circleci/xxxxx/overview`                                                                            |               |
| `start_date`  | `string` | Start date.                                                                                                                                                                              |               |
| `project_id`  | `string` | Project ID found in the project settings, Visit `https://app.circleci.com/settings/project/circleci/ORG_SLUG/YYYYY`                                                                      |               |
| `workflow_id` | `array`  | Workflow ID's of project pipelines, Could be seen in the URL of pipeline build, Example `https://app.circleci.com/pipelines/circleci/55555xxxxxx/7yyyyyyyyxxxxx/2/workflows/WORKFLOW_ID` |               |
| `job_number`  | `string` | Job Number of the workflow for `jobs` stream, Auto fetches from `workflow_jobs` stream, if not configured                                                                                | `2`           |

## Streams[​](#streams "Direct link to Streams")

| Stream Name          | Primary Key   | Pagination       | Supports Full Sync | Supports Incremental |
| -------------------- | ------------- | ---------------- | ------------------ | -------------------- |
| context              | id            | DefaultPaginator | ✅                 | ✅                   |
| self\_ids            | id            | DefaultPaginator | ✅                 | ❌                   |
| self\_collaborations | id            | DefaultPaginator | ✅                 | ❌                   |
| me                   | analytics\_id | DefaultPaginator | ✅                 | ✅                   |
| projects             | vcs\_url      | DefaultPaginator | ✅                 | ❌                   |
| pipelines            | id            | DefaultPaginator | ✅                 | ✅                   |
| specific\_project    | id            | DefaultPaginator | ✅                 | ❌                   |
| jobs                 | number        | DefaultPaginator | ✅                 | ❌                   |
| workflow             | id            | DefaultPaginator | ✅                 | ✅                   |
| insights\_metrics    | project\_id   | DefaultPaginator | ✅                 | ❌                   |
| insights\_branches   | id            | DefaultPaginator | ✅                 | ❌                   |
| workflow\_jobs       | id            | DefaultPaginator | ✅                 | ✅                   |

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

Organization ID

required

string

org\_id

›

Project ID

required

string

project\_id

›

Start date

required

string

start\_date

›

Job Number

string

job\_number

›

Workflow ID

array

workflow\_id

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | PR                                                       | Subject                                                                               |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 0.1.0   | 2024-10-11 | [46729](https://github.com/airbytehq/airbyte/pull/46729) | Remove unwanted optional config parameters                                            |
| 0.0.1   | 2024-09-29 | [46249](https://github.com/airbytehq/airbyte/pull/46249) | Initial release by [@btkcodedev](https://github.com/btkcodedev) via Connector Builder |
