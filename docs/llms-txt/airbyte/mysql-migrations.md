# Source: https://docs.airbyte.com/integrations/sources/mysql-migrations.md

# Source: https://docs.airbyte.com/integrations/destinations/mysql-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/destination-mysql/latest/icon.svg)

# MySQL Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.1](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-mysql)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-mysql)(last updated 4 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `ca81ee7c-3163-4246-af40-094cc31e5e42`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

This version introduces [Destinations V2](/release_notes/upgrading_to_destinations_v2.md#what-is-destinations-v2), which provides better error handling and improved final table structures. To review the breaking changes, and how to upgrade, see [here](/release_notes/upgrading_to_destinations_v2.md#quick-start-to-upgrading). These changes will likely require updates to downstream dbt / SQL models, which we walk through [here](/release_notes/upgrading_to_destinations_v2.md#updating-downstream-transformations). Selecting `Upgrade` will upgrade **all** connections using this destination at their next sync. You can manually sync existing connections prior to the next scheduled sync to start the upgrade early.

Worthy of specific mention, this version includes:

* Per-record error handling
* Clearer table structure
* Removal of sub-tables for nested properties
* Removal of SCD tables

Learn more about what's new in Destinations V2 [here](/platform/using-airbyte/core-concepts/typing-deduping.md).
