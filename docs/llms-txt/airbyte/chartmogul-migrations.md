# Source: https://docs.airbyte.com/integrations/sources/chartmogul-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-chartmogul/latest/icon.svg)

# Chartmogul Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.44](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-chartmogul)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-chartmogul)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `b6604cbd-1b12-4c08-8767-e140d0fb0877`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

Version 1.0.0 refactors and separates the `customer_count` stream into multiple streams (daily, weekly, monthly, quarterly).

Users that have this stream enabled will need to refresh the schema and run a reset to use the new streams in affected connections to continue syncing.
