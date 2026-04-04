# Source: https://docs.airbyte.com/integrations/sources/snapchat-marketing-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-snapchat-marketing/latest/icon.svg)

# Snapchat Marketing Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [1.5.29](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-snapchat-marketing)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-snapchat-marketing)(last updated 15 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `200330b2-ea62-4d11-ac6d-cfe3e3f8ab2b`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

We're continuously striving to enhance the quality and reliability of our connectors at Airbyte. As part of our commitment to delivering exceptional service, we are transitioning Snapchat Marketing source from the Python Connector Development Kit (CDK) to our innovative low-code framework. This is part of a strategic move to streamline many processes across connectors, bolstering maintainability and freeing us to focus more of our efforts on improving the performance and features of our evolving platform and growing catalog. However, due to differences between the Python and low-code CDKs, this migration constitutes a breaking change.

To gracefully handle these changes for your existing connections, we highly recommend resetting your data before resuming your data syncs with the new version.

### Migration Steps[​](#migration-steps "Direct link to Migration Steps")

1. Select **Connections** in the main navbar.
   <!-- -->
   1. Select the connection(s) affected by the update.
2. Select the **Schema** tab.
3. Uncheck all streams except the affected ones.
4. Select **Save changes** at the bottom of the page.
5. Select the **Settings** tab.
6. Press the **Clear your data** button.
7. Return to the **Schema** tab.
8. Check all your streams.
9. Select **Sync now** to sync your data

For more information on resetting your data in Airbyte, see [this page](/platform/operator-guides/clear.md).
