# Source: https://docs.airbyte.com/integrations/destinations/pubsub.md

![](https://connectors.airbyte.com/files/metadata/airbyte/destination-pubsub/latest/icon.svg)

# PubSub

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.2.3](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-pubsub)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-pubsub)(last updated 9 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `356668e2-7e34-47f3-a3b0-67a8a481b692`

## Overview[​](#overview "Direct link to Overview")

The Airbyte Google PubSub destination allows you to send/stream data into PubSub. Pub/Sub is an asynchronous messaging service provided by Google Cloud Provider.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* For Airbyte Open Source users using the [Postgres](https://docs.airbyte.com/integrations/sources/postgres) source connector, [upgrade](https://docs.airbyte.com/operator-guides/upgrading-airbyte/) your Airbyte platform to version `v0.40.0-alpha` or newer and upgrade your PubSub connector to version `0.1.6` or newer

### Sync overview[​](#sync-overview "Direct link to Sync overview")

#### Output schema[​](#output-schema "Direct link to Output schema")

Each stream will be output a PubSubMessage with attributes. The message attributes will be

* `_stream`: the name of stream where the data is coming from
* `_namespace`: namespace if available from the stream

The data will be a serialized JSON, containing the following fields

* `_airbyte_ab_id`: a uuid string assigned by Airbyte to each event that is processed.
* `_airbyte_emitted_at`: a long timestamp(ms) representing when the event was pulled from the data source.
* `_airbyte_data`: a json string representing source data.

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

To use the PubSub destination, you'll need:

* A Google Cloud Project with PubSub enabled
* A PubSub Topic to which Airbyte can stream/sync your data
* A Google Cloud Service Account with the `Pub/Sub Editor` role in your GCP project
* A Service Account Key to authenticate into your Service Account

See the setup guide for more information about how to create the required resources.

### Setup guide[​](#setup-guide "Direct link to Setup guide")

#### Google cloud project[​](#google-cloud-project "Direct link to Google cloud project")

If you have a Google Cloud Project with PubSub enabled, skip to the "Create a Topic" section.

First, follow along the Google Cloud instructions to [Create a Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin). PubSub is enabled automatically in new projects. If this is not the case for your project, find it in [Marketplace](https://console.cloud.google.com/marketplace/product/google/pubsub.googleapis.com) and enable.

#### PubSub topic for Airbyte syncs[​](#pubsub-topic-for-airbyte-syncs "Direct link to PubSub topic for Airbyte syncs")

Airbyte needs a topic in PubSub to write the data being streamed/synced from your data sources. If you already have a Topic into which Airbyte should stream/sync data, skip this section. Otherwise, follow the Google Cloud guide for [Creating a PubSub Topic](https://cloud.google.com/pubsub/docs/admin#creating_a_topic) to achieve this.

#### Service account[​](#service-account "Direct link to Service account")

In order for Airbyte to stream/sync data into PubSub, it needs credentials for a [Service Account](https://cloud.google.com/iam/docs/service-accounts) with the `Pub/Sub Editor` role, which grants permissions to publish messages into PubSub topics. We highly recommend that this Service Account is exclusive to Airbyte for ease of permissioning and auditing. However, you can use a pre-existing Service Account if you already have one with the correct permissions.

The easiest way to create a Service Account is to follow GCP's guide for [Creating a Service Account](https://cloud.google.com/iam/docs/creating-managing-service-accounts). Once you've created the Service Account, make sure to keep its ID handy as you will need to reference it when granting roles. Service Account IDs typically take the form `<account-name>@<project-name>.iam.gserviceaccount.com`

Then, add the service account as a Member in your Google Cloud Project with the `Pub/Sub Editor` role. To do this, follow the instructions for [Granting Access](https://cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console) in the Google documentation. The email address of the member you are adding is the same as the Service Account ID you just created.

At this point you should have a service account with the `Pub/Sub Editor` project-level permission.

#### Service account key[​](#service-account-key "Direct link to Service account key")

Service Account Keys are used to authenticate as Google Service Accounts. For Airbyte to leverage the permissions you granted to the Service Account in the previous step, you'll need to provide its Service Account Keys. See the [Google documentation](https://cloud.google.com/iam/docs/service-accounts#service_account_keys) for more information about Keys.

Follow the [Creating and Managing Service Account Keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) guide to create a key. Airbyte currently supports JSON Keys only, so make sure you create your key in that format. As soon as you created the key, make sure to download it, as that is the only time Google will allow you to see its contents. Once you've successfully configured BigQuery as a destination in Airbyte, delete this key from your computer.

### Setup the PubSub destination in Airbyte[​](#setup-the-pubsub-destination-in-airbyte "Direct link to Setup the PubSub destination in Airbyte")

You should now have all the requirements needed to configure PubSub as a destination in the UI. You'll need the following information to configure the PubSub destination:

* **Project ID**: GCP project id
* **Topic ID**: name of pubsub topic under the project
* **Service Account Key**: the contents of your Service Account Key JSON file

Once you've configured PubSub as a destination, delete the Service Account Key from your computer.

## Namespace support[​](#namespace-support "Direct link to Namespace support")

This destination does not support [namespaces](https://docs.airbyte.com/platform/using-airbyte/core-concepts/namespaces).

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

Message Batching Enabled

required

boolean

batching\_enabled

›

Credentials JSON

required

string

credentials\_json

›

Message Ordering Enabled

required

boolean

ordering\_enabled

›

Project ID

required

string

project\_id

›

PubSub Topic ID

required

string

topic\_id

›

Message Batching: Delay Threshold

integer

batching\_delay\_threshold

›

Message Batching: Element Count Threshold

integer

batching\_element\_count\_threshold

›

Message Batching: Request Bytes Threshold

integer

batching\_request\_bytes\_threshold

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date              | Pull Request                                             | Subject                                                           |
| ------- | ----------------- | -------------------------------------------------------- | ----------------------------------------------------------------- |
| 0.2.3   | 2025-03-24        | [56355](https://github.com/airbytehq/airbyte/pull/56355) | Upgrade to airbyte/java-connector-base:2.0.1 to be M4 compatible. |
| 0.2.2   | 2025-01-10        | [51481](https://github.com/airbytehq/airbyte/pull/51481) | Use a non root base image                                         |
| 0.2.1   | 2024-12-18        | [49878](https://github.com/airbytehq/airbyte/pull/49878) | Use a base image: airbyte/java-connector-base:1.0.0               |
| 0.2.0   | August 16, 2022   | [15705](https://github.com/airbytehq/airbyte/pull/15705) | Add configuration for Batching and Ordering                       |
| 0.1.5   | 2022-06-17        | [13864](https://github.com/airbytehq/airbyte/pull/13864) | Updated stacktrace format for any trace message errors            |
| 0.1.4   | February 21, 2022 | [#9819](https://github.com/airbytehq/airbyte/pull/9819)  | Upgrade version of google-cloud-pubsub                            |
| 0.1.3   | 2022-02-14        | [10256](https://github.com/airbytehq/airbyte/pull/10256) | (unpublished) Add `-XX:+ExitOnOutOfMemoryError` JVM option        |
| 0.1.2   | December 29, 2021 | [#9183](https://github.com/airbytehq/airbyte/pull/9183)  | Update connector fields title/description                         |
| 0.1.1   | August 13, 2021   | [#4699](https://github.com/airbytehq/airbyte/pull/4699)  | Added json config validator                                       |
| 0.1.0   | June 24, 2021     | [#4339](https://github.com/airbytehq/airbyte/pull/4339)  | Initial release                                                   |
