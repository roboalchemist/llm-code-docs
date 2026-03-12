# Source: https://docs.airbyte.com/integrations/sources/quickbooks-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-quickbooks/latest/icon.svg)

# QuickBooks Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [4.0.4](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-quickbooks)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-quickbooks)(last updated 4 months ago)

* CDK Version

  [4.6.2](https://pypi.org/project/airbyte-cdk/4.6.2/)

* Sync Success Rate

* Usage Rate

* Definition ID

  `cf9c4355-b171-4477-8f2d-6c5cc5fc8b7e`

## Upgrading to 4.0.0[​](#upgrading-to-400 "Direct link to Upgrading to 4.0.0")

The config no longer has a nested credentials field, while the config fields remain the same, they are now at the root level instead of being nested inside a credentials object. You will need to repopulate the config fields to make the connector work again. This is done to fix the refresh token issue where it wasn't getting updated after 24 hours.

## Upgrading to 3.0.0[​](#upgrading-to-300 "Direct link to Upgrading to 3.0.0")

Some fields in `bills`, `credit_memos`, `items`, `refund_receipts`, and `sales_receipts` streams have been changed from `integer` to `number` to fix normalization. You may need to refresh the connection schema for those streams (skipping the reset), and running a sync. Alternatively, you can just run a reset.
