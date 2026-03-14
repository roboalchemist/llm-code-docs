# Source: https://docs.airbyte.com/integrations/destinations/deepset.md

![](https://connectors.airbyte.com/files/metadata/airbyte/destination-deepset/latest/icon.svg)

# deepset AI Platform

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.1.8](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-deepset)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-deepset)(last updated 9 months ago)

* CDK Version

  [6.48.16](https://pypi.org/project/airbyte-cdk/6.48.16/)

* Sync Success Rate

* Usage Rate

* Definition ID

  `a6fe9a28-7377-4d2d-aa39-15bcf9578e17`

deepset AI Platform is a SaaS platform for building LLM applications and managing them across the whole lifecycle - from early prototyping to large-scale production. For details, see [deepset documentation](https://docs.cloud.deepset.ai/docs/getting-started).

## Supported sync modes[​](#supported-sync-modes "Direct link to Supported sync modes")

| Sync mode                                                                                                                                     | Supported? |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [Full Refresh - Overwrite](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite)                   | Yes        |
| [Full Refresh - Append](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-append)                         | Yes        |
| [Full Refresh - Overwrite + Deduped](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite-deduped) | Yes        |
| [Incremental Sync - Append](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append)                      | Yes        |
| [Incremental Sync - Append + Deduped](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append-deduped)    | Yes        |

## Data Integration with Airbyte[​](#data-integration-with-airbyte "Direct link to Data Integration with Airbyte")

To make it possible to synchronize data to deepset AI Platform using Airbyte, we've added an Airbyte deepset destination connector. You can use it to stream data into deepset from any Airbyte source that emits records matching the document file type. The synchronized data are available in deepset on the Files page as Markdown files.

*Note*: The deepset destination connector writes data to your deepset workspace, but does not delete any data from the workspace. If a file with the same name already exists in the destination workspace, it is overwritten.

## Syncing Data to deepset AI Platform[​](#syncing-data-to-deepset-ai-platform "Direct link to Syncing Data to deepset AI Platform")

To use the deepset destination in Airbyte:

1. Log in to deepset AI Platform.

2. Generate the deepset Cloud API key:

   * Click your initials in the top right corner and choose Connections.
   * Scroll down the Connections page to the API Keys section and click *Add new key*. If you need help, see [Generate an API Key](https://docs.cloud.deepset.ai/docs/generate-api-key).

3. Set up the destination connector in Airbyte providing the following details:

   * `Base URL`: This is the URL for the deepset environment with your account. Possible options are: `https://api.cloud.deepset.ai` (default) for EU users , `https://api.us.deepset.ai` for US users, or custom URL for on-premise deployments.
   * `API key`: Your deepset API key (generated in step 2 above).
   * `Workspace name`: The name of the deepset workspace where you want to store the data.
   * `Retry count`: The number of times to retry syncing a record before marking it as failed. Defaults to 5 times.

After you connect a source and the first stream synchronization succeeds, your records are available in deepset AI Platform on the Files page as Markdown files.

## Namespace support[​](#namespace-support "Direct link to Namespace support")

This destination supports [namespaces](https://docs.airbyte.com/platform/using-airbyte/core-concepts/namespaces).

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

Workspace Name

required

string

workspace

›

Base URL

string

base\_url

›

Retry Count

number

retries

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject             |
| ------- | ---------- | -------------------------------------------------------- | ------------------- |
| 0.1.8   | 2025-05-17 | [60635](https://github.com/airbytehq/airbyte/pull/60635) | Update dependencies |
| 0.1.7   | 2025-05-10 | [59834](https://github.com/airbytehq/airbyte/pull/59834) | Update dependencies |
| 0.1.6   | 2025-05-03 | [58717](https://github.com/airbytehq/airbyte/pull/58717) | Update dependencies |
| 0.1.5   | 2025-04-19 | [58229](https://github.com/airbytehq/airbyte/pull/58229) | Update dependencies |
| 0.1.4   | 2025-04-12 | [57619](https://github.com/airbytehq/airbyte/pull/57619) | Update dependencies |
| 0.1.3   | 2025-04-05 | [57176](https://github.com/airbytehq/airbyte/pull/57176) | Update dependencies |
| 0.1.2   | 2025-03-29 | [56599](https://github.com/airbytehq/airbyte/pull/56599) | Update dependencies |
| 0.1.1   | 2025-03-22 | [56097](https://github.com/airbytehq/airbyte/pull/56097) | Update dependencies |
| 0.1.0   | 2025-01-10 | [48875](https://github.com/airbytehq/airbyte/pull/48875) | Initial release     |
