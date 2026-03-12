# Source: https://docs.airbyte.com/integrations/sources/faker-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-faker/latest/icon.svg)

# Sample Data Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [6.2.24](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-faker)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-faker)(last updated 4 months ago)

* CDK Version

  [2.4.0](https://pypi.org/project/airbyte-cdk/2.4.0/)

* Sync Success Rate

* Usage Rate

* Definition ID

  `dfd88b22-b603-4c3d-aad7-3701784586b1`

## Upgrading to 7.0.0[​](#upgrading-to-700 "Direct link to Upgrading to 7.0.0")

This is a test breaking change to validate breaking change infrastructure. No actual schema or functionality changes were made. No user action is required.

## Upgrading to 6.0.0[​](#upgrading-to-600 "Direct link to Upgrading to 6.0.0")

All streams (`users`, `products`, and `purchases`) now properly declare `id` as their respective primary keys. Existing sync jobs should still work as expected but you may need to reset your sync and/or update write mode after upgrading to the latest connector version.

## Upgrading to 5.0.0[​](#upgrading-to-500 "Direct link to Upgrading to 5.0.0")

Some columns are narrowing from `number` to `integer`. You may need to force normalization to rebuild your destination tables by manually dropping the SCD and final tables, refreshing the connection schema (skipping the reset), and running a sync. Alternatively, you can just run a reset.

## Upgrading to 4.0.0[​](#upgrading-to-400 "Direct link to Upgrading to 4.0.0")

Nothing to do here - this was a test breaking change.
