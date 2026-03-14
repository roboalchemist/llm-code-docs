# Source: https://docs.airbyte.com/integrations/sources/airtable-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-airtable/latest/icon.svg)

# Airtable Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [4.6.23](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-airtable)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-airtable)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `14c6e7ea-97ed-4f5e-a7b5-25e9a80b8212`

## Upgrading to 4.0.0[​](#upgrading-to-400 "Direct link to Upgrading to 4.0.0")

Columns with Formulas are narrowing from `array` to `string` or `number`. You may need to refresh the connection schema (with the reset), and run a sync.
