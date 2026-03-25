# Source: https://docs.airbyte.com/integrations/sources/weatherstack-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-weatherstack/latest/icon.svg)

# Weatherstack Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.14](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-weatherstack)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-weatherstack)(last updated 4 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `5db8292c-5f5a-11ed-9b6a-0242ac120002`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

Version 1.0.0 introduces changes to the connection configuration. The `is_paid_account` config input is removed and streams unavailable to unpaid accounts will simply be empty when read.

Due to this upgrade, no synced streams were affected. However, for unpaid accounts, the following streams which were initially hidden will now appear but with empty records since the API only makes them available for paid accounts.

1. historical
2. location\_lookup

## Migration Steps[​](#migration-steps "Direct link to Migration Steps")

### Refresh source schemas and reset data[​](#refresh-source-schemas-and-reset-data "Direct link to Refresh source schemas and reset data")

1. Select **Connections** in the main nav bar.
   <!-- -->
   1. Select the connection(s) affected by the update.

2. Select the **Replication** tab.

   <!-- -->

   1. Select **Refresh source schema**.

   2. Select **OK**.

      <!-- -->

      > \[!NOTE]<br /><!-- -->Any detected schema changes will be listed for your review.

3. Select **Save changes** at the bottom of the page.

   <!-- -->

   1. Ensure the **Reset affected streams** option is checked.

      <!-- -->

      > \[!NOTE]<br /><!-- -->Depending on destination type you may not be prompted to reset your data.

4. Select **Save connection**.

   <!-- -->

   > \[!NOTE]<br /><!-- -->This will reset the data in your destination and initiate a fresh sync.

For more information on resetting your data in Airbyte, see [this page](https://docs.airbyte.com/operator-guides/reset).
