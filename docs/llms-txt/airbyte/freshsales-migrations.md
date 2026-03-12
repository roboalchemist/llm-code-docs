# Source: https://docs.airbyte.com/integrations/sources/freshsales-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-freshsales/latest/icon.svg)

# Freshsales Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.43](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-freshsales)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-freshsales)(last updated 23 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `eca08d79-7b92-4065-b7f3-79c14836ebe7`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

This version migrates the Freshsales connector to our low-code framework for greater maintainability.

As part of this release, we've also updated data types across streams to match the correct return types from the upstream API. You will need to run a reset on connections using this connector after upgrading to continue syncing.
