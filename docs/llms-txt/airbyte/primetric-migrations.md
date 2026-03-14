# Source: https://docs.airbyte.com/integrations/sources/primetric-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-primetric/latest/icon.svg)

# Primetric Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.39](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-primetric)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-primetric)(last updated 3 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `f636c3c6-4077-45ac-b109-19fc62a283c1`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

The uuid field now have a string format (without 'format: uuid') for all streams, the destination should me managed according to that if needed. The Assignments stream schema property financial\_client\_currency\_exchange\_rate has changed its type to string. The Organization\_rag\_scopes stream has schema changes to include order and uuid.
