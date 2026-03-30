# Source: https://docs.airbyte.com/integrations/sources/outreach-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-outreach/latest/icon.svg)

# Outreach Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.25](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-outreach)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-outreach)(last updated 23 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `3490c201-5d95-4783-b600-eaf07a4c7787`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

The verison migrates the Outreach connector to the low-code framework for greater maintainability. Important update: The sequence\_steps stream schema from API has a breaking change to the creator field to an array containing integers instead of strings. Destination should adapt to this change if needed. You may need to refresh the connection schema (with the reset), and run a sync.
