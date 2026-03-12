# Source: https://docs.airbyte.com/integrations/sources/datadog-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-datadog/latest/icon.svg)

# Datadog Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [2.0.24](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-datadog)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-datadog)(last updated 4 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `1cfc30c7-82db-43f4-9fd7-ac1b42312cda`

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

On December 13, 2024, Datadog is removing support for the `is_read_only` attribute in the Dashboards API’s. Hence, the `is_read_only` attribute will no longer be available in the dashboards stream response. Upgrade and resync to reset the schema and update the records.

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

Starting 1.0, Datadog source will apply start and end dates to sync data incrementally. When upgrading, take a minute to set start and end date config options.
