# Source: https://docs.airbyte.com/integrations/sources/rss-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-rss/latest/icon.svg)

# Rss Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.0.31](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-rss)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-rss)(last updated a year ago)

* CDK Version

  [0.88.1](https://pypi.org/project/airbyte-cdk/0.88.1/)

* Sync Success Rate

* Usage Rate

* Definition ID

  `0efee448-6948-49e2-b786-17db50647908`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

We're continuously striving to enhance the quality and reliability of our connectors at Airbyte.

As part of our commitment to delivering exceptional service, we are transitioning our RSS source from the Python Connector Development Kit (CDK) to our new low-code framework improving maintainability and reliability of the connector. Due to differences between the Python and low-code CDKs, this migration constitutes a breaking change.

## Migration Steps[​](#migration-steps "Direct link to Migration Steps")

Clearing your data is required for the affected streams in order to continue syncing successfully. To clear your data for the affected streams, follow the steps below:

1. Select **Connections** in the main navbar and select the connection(s) affected by the update.

2. Select the **Schema** tab.

   <!-- -->

   1. Select **Refresh source schema** to bring in any schema changes. Any detected schema changes will be listed for your review.
   2. Select **OK** to approve changes.

3. Select **Save changes** at the bottom of the page.
   <!-- -->
   1. Ensure the **Clear affected streams** option is checked to ensure your streams continue syncing successfully with the new schema.

4. Select **Save connection**.

This will clear the data in your destination for the subset of streams with schema changes. After the clear succeeds, trigger a sync by clicking **Sync Now**. For more information on clearing your data in Airbyte, see [this page](/platform/operator-guides/clear.md).
