# Source: https://docs.airbyte.com/integrations/destinations/glassflow.md

![](https://connectors.airbyte.com/files/metadata/airbyte/destination-glassflow/latest/icon.svg)

# GlassFlow

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.1.6](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-glassflow)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-glassflow)(last updated 10 months ago)

* CDK Version

  [4.6.2](https://pypi.org/project/airbyte-cdk/4.6.2/)

* Definition ID

  `6af33483-3956-4fea-a38c-04d136e90fa8`

## Overview[​](#overview "Direct link to Overview")

The GlassFlow destination allows you to send/stream data to a GlassFlow pipeline. GlassFlow is a serverless, Python-centric data streaming platform that transforms data in real-time for end-to-end data pipelines.

### Sync overview[​](#sync-overview "Direct link to Sync overview")

#### Output schema[​](#output-schema "Direct link to Output schema")

Each stream will be output a GlassFlow message. The message properties will be

* `stream`: the name of stream where the data is coming from.
* `namespace`: namespace if available from the stream.
* `emitted_at`: timestamp the `AirbyteRecord` was emitted at.
* `data`: `AirbyteRecord` data.

The message will be serialized as JSON.

## Supported sync modes[​](#supported-sync-modes "Direct link to Supported sync modes")

| Sync mode                                                                                                                                     | Supported? |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [Full Refresh - Overwrite](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite)                   | No         |
| [Full Refresh - Append](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-append)                         | Yes        |
| [Full Refresh - Overwrite + Deduped](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite-deduped) | No         |
| [Incremental Sync - Append](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append)                      | Yes        |
| [Incremental Sync - Append + Deduped](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append-deduped)    | No         |

## Getting started[​](#getting-started "Direct link to Getting started")

### Requirements[​](#requirements "Direct link to Requirements")

To use the GlassFlow destination, you'll need:

* A GlassFlow pipeline\_id and pipeline\_access\_token to publish messages.

## Namespace support[​](#namespace-support "Direct link to Namespace support")

This destination supports [namespaces](https://docs.airbyte.com/platform/using-airbyte/core-concepts/namespaces).

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

Pipeline Access Token

required

string

pipeline\_access\_token

›

Pipeline ID

required

string

pipeline\_id

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date               | Pull Request                                             | Subject             |
| ------- | ------------------ | -------------------------------------------------------- | ------------------- |
| 0.1.6   | 2025-05-03         | [59349](https://github.com/airbytehq/airbyte/pull/59349) | Update dependencies |
| 0.1.5   | 2025-04-26         | [58697](https://github.com/airbytehq/airbyte/pull/58697) | Update dependencies |
| 0.1.4   | 2025-04-19         | [58260](https://github.com/airbytehq/airbyte/pull/58260) | Update dependencies |
| 0.1.3   | 2025-04-12         | [57645](https://github.com/airbytehq/airbyte/pull/57645) | Update dependencies |
| 0.1.2   | 2025-04-05         | [57127](https://github.com/airbytehq/airbyte/pull/57127) | Update dependencies |
| 0.1.1   | 2025-03-29         | [56578](https://github.com/airbytehq/airbyte/pull/56578) | Update dependencies |
| 0.1.0   | September 01, 2024 | [#7560](https://github.com/airbytehq/airbyte/pull/7560)  | Initial release     |
