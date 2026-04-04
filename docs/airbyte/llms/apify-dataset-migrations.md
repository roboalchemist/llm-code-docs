# Source: https://docs.airbyte.com/integrations/sources/apify-dataset-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-apify-dataset/latest/icon.svg)

# Apify Dataset Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [2.2.40](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-apify-dataset)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-apify-dataset)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `47f17145-fe20-4ef5-a548-e29b048adf84`

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

Major update: The old broken Item Collection stream has been removed and replaced with a new Item Collection (WCC) stream specific for the datasets produced by [Website Content Crawler](https://apify.com/apify/website-content-crawler) Actor. In a follow-up release 2.1.0, a generic item collection stream will be added to support all other datasets.

After upgrading, users should:

* Reconfigure dataset id and API key
* Reset all streams

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

A major update fixing the data ingestion to retrieve properly data from Apify. Please update your connector configuration setup.
