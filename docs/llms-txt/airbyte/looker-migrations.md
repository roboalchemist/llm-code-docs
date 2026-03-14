# Source: https://docs.airbyte.com/integrations/sources/looker-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-looker/latest/icon.svg)

# Looker Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.0.34](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-looker)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-looker)(last updated 4 months ago)

* CDK Version

  [4.6.2](https://pypi.org/project/airbyte-cdk/4.6.2/)

* Sync Success Rate

* Usage Rate

* Definition ID

  `00405b19-9768-4e0c-b1ae-9fc2ee2b2a8c`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

Version 1.0.0 introduces changes to the connection configuration which has been upgraded to the API v4.0 from v3.1. Due to this upgrade, the following streams were affected;

1. homepages, homepage\_items and homepage\_sections streams are replaced with boards, board\_items and board\_sections streams respectively.
2. spaces and space\_ancestors streams have been removed in favour of folders and folder\_ancestors streams
3. lookml\_dashboards stream has been removed in favour of dashboards stream

In addtion to affected streams, the schemas of the streams are expected to change.

For details about the API migration, check out [here](https://cloud.google.com/looker/docs/api-3x-deprecation)

## Migration Steps[​](#migration-steps "Direct link to Migration Steps")

### Refresh affected schemas and reset data[​](#refresh-affected-schemas-and-reset-data "Direct link to Refresh affected schemas and reset data")

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
