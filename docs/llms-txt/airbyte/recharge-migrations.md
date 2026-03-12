# Source: https://docs.airbyte.com/integrations/sources/recharge-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-recharge/latest/icon.svg)

# Recharge Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [3.0.11](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-recharge)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-recharge)(last updated 5 months ago)

* CDK Version

  [4.6.2](https://pypi.org/project/airbyte-cdk/4.6.2/)

* Sync Success Rate

* Usage Rate

* Definition ID

  `45d2e135-2ede-49e1-939f-3e3ec357a65e`

## Upgrading to 3.0.0[​](#upgrading-to-300 "Direct link to Upgrading to 3.0.0")

This is a breaking change for **Products** stream. This version introduces the `plans` stream for replacement of products stream according to the official [notice](https://docs.getrecharge.com/docs/deprecation-notice-products-v2021-01) from recharge.

To gracefully handle these changes for your existing connections, we highly recommend resetting your data before resuming your data syncs with the new version.

1. Select **Connections** in the main navbar.
   <!-- -->
   1. Select the connection(s) affected by the update.
2. Select the **Schema** tab.
3. Click **Refresh source schema**, then **Ok**.
4. Select **Save changes** at the bottom of the page.
5. Select the **Status** tab and click three dots on the right side of **Shop**.
6. Press the **Clear data** button.
7. Return to the **Schema** tab.
8. Check all your streams.
9. Select **Sync now** to sync your data

For more information on resetting your data in Airbyte, see [this page](/platform/operator-guides/clear.md).

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

This is a breaking change for **Shop** stream, which used `[shop, store]` fields as a primary key. This version introduces changing of primary key from `[shop, store]`(type: object, object) to primary key `id`(type: integer), as it makes stream compatible with destinations that do not support complex primary keys(e.g. BigQuery).

To gracefully handle these changes for your existing connections, we highly recommend resetting your data before resuming your data syncs with the new version. The **Shop** stream can be manually reset in the following way:

1. Select **Connections** in the main navbar.
   <!-- -->
   1. Select the connection(s) affected by the update.
2. Select the **Schema** tab.
3. Click **Refresh source schema**, then **Ok**.
4. Select **Save changes** at the bottom of the page.
5. Select the **Status** tab and click three dots on the right side of **Shop**.
6. Press the **Clear data** button.
7. Return to the **Schema** tab.
8. Check all your streams.
9. Select **Sync now** to sync your data

For more information on resetting your data in Airbyte, see [this page](/platform/operator-guides/clear.md).
