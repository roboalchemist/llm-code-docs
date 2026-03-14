# Source: https://docs.airbyte.com/integrations/sources/trello-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-trello/latest/icon.svg)

# Trello Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.3.10](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-trello)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-trello)(last updated 4 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `8da67652-004c-11ec-9a03-0242ac130003`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

This version upgrades the connector to the low-code framework for better maintainability. This migration includes a breaking change to the state format of the `actions` stream.

Any connection using the `actions` stream in `incremental` mode will need to be reset after the upgrade to avoid sync failures.
