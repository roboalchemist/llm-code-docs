# Source: https://docs.airbyte.com/integrations/sources/pipedrive-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-pipedrive/latest/icon.svg)

# Pipedrive Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [2.4.0](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-pipedrive)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-pipedrive)(last updated 4 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `d8286229-c680-4063-8c59-23b9b391c700`

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

Please update your config and reset your data (to match the new format). This version has changed the config to only require an API key.

This version also removes the `pipeline_ids` field from the `deal_fields` stream.
