# Source: https://docs.airbyte.com/integrations/sources/microsoft-teams-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-microsoft-teams/latest/icon.svg)

# Microsoft Teams Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.2.12](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-microsoft-teams)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-microsoft-teams)(last updated a month ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `eaf50f04-21dd-4620-913b-2a83f5635227`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

Version 1.0.0 of the Microsoft Teams source connector introduces breaking changes to the schemas of all streams. A full schema refresh is required to ensure a seamless upgrade to this version.

### Refresh schemas and reset data[​](#refresh-schemas-and-reset-data "Direct link to Refresh schemas and reset data")

1. Select **Connections** in the main navbar.
2. From the list of your existing connections, select the connection(s) affected by the update.
3. Select the **Replication** tab, then select **Refresh source schema**.

note

Any detected schema changes will be listed for your review. Select **OK** when you are ready to proceed.

4. At the bottom of the page, select **Save changes**.

caution

Depending on your destination, you may be prompted to **Reset all streams**. Although this step is not required to proceed, it is highly recommended for users who have selected `Full Refresh | Append` sync mode, as the updated schema may lead to inconsistencies in the data structure within the destination.

5. Select **Save connection**. This will reset the data in your destination (if selected) and initiate a fresh sync.

For more information on resetting your data in Airbyte, see [this page](/platform/operator-guides/clear.md).

### Changes in 1.0.0[​](#changes-in-100 "Direct link to Changes in 1.0.0")

* The naming convention for field names in previous versions used "snake\_case", which is not aligned with the "camelCase" convention used by the Microsoft Graph API. For example:

`user_id` -> `userId` `created_date` -> `createdDate`

With the update to "camelCase", fields that may have been unrecognized or omitted in earlier versions will now be properly mapped and included in the data synchronization process, enhancing the accuracy and completeness of your data.

* The `team_device_usage_report` stream contained a fatal bug that could lead to crashes during syncs. You should now be able to reliably use this stream during syncs.

* `Date` and `date-time` fields have been typed as airbyte\_type `date` and `timestamp_without_timezone`, respectively.
