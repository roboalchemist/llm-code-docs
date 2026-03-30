# Source: https://docs.airbyte.com/integrations/sources/orb-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-orb/latest/icon.svg)

# Orb Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [2.1.22](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-orb)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-orb)(last updated 4 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `7f0455fb-4518-4ec0-b7a3-d808bf8081cc`

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

This version migrates the Orb connector to our low-code framework for greater maintainability.

As part of this release, we've also updated data types across streams to match the correct return types from the upstream API. You will need to run a reset on connections using this connector after upgrading to continue syncing. The data type of the `credit_block_per_unit_cost_basis` field (primary key) in the `credits_ledger_entries` stream has been changed from `string` to `number`
