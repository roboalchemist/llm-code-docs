# Source: https://docs.airbyte.com/integrations/sources/tmdb-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-tmdb/latest/icon.svg)

# TMDb Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.41](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-tmdb)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-tmdb)(last updated 23 days ago)

* Definition ID

  `6240848f-f795-45eb-8f5e-c7542822fc03`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

Version 1.0.0 has a schema change.

The search\_people schema has been changed it's 'type' in schema\['properties']\['results']\['items']\['properties']\['known\_for']\['items']\['properties']\['poster\_path'] to be optionally empty The search\_tv\_shows schema has been changed it's pattern in schema\['properties']\['results']\['items']\['properties']\['overview'] to contain both strings and spaces.
