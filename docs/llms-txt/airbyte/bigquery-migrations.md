# Source: https://docs.airbyte.com/integrations/destinations/bigquery-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/destination-bigquery/latest/icon.svg)

# BigQuery Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [3.0.17](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-bigquery)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-bigquery)(last updated a month ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `22f6c74f-5699-40ff-833c-4a879ea40133`

## Upgrading to 3.0.0[​](#upgrading-to-300 "Direct link to Upgrading to 3.0.0")

This version upgrades Destination BigQuery to the [Direct-Load](/platform/using-airbyte/core-concepts/direct-load-tables.md) paradigm, which improves performance and reduces warehouse spend. If you have unusual requirements around record visibility or schema evolution, read that document for more information about how direct-load differs from Typing and Deduping.

This version also adds an option to enable CDC deletions as soft-deletes.

If you do not interact with the raw tables, you can safely upgrade. There is no breakage for this usecase.

If you *only* interact with the raw tables, make sure that you have the `Disable Final Tables` option enabled before upgrading. This will automatically enable the `Legacy raw tables` option after upgrading.

If you interact with both the raw *and* final tables, this usecase will no longer be directly supported. You must create two connectors (one with `Disable Final Tables` enabled, and one with it disabled) and run two connections in parallel.

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

This version introduces [Destinations V2](/release_notes/upgrading_to_destinations_v2.md#what-is-destinations-v2), which provides better error handling, incremental delivery of data for large syncs, and improved final table structures. To review the breaking changes, and how to upgrade, see [here](/release_notes/upgrading_to_destinations_v2.md#quick-start-to-upgrading). These changes will likely require updates to downstream dbt / SQL models, which we walk through [here](/release_notes/upgrading_to_destinations_v2.md#updating-downstream-transformations). Selecting `Upgrade` will upgrade **all** connections using this destination at their next sync. You can manually sync existing connections prior to the next scheduled sync to start the upgrade early.

Worthy of specific mention, this version includes:

* Per-record error handling
* Clearer table structure
* Removal of sub-tables for nested properties
* Removal of SCD tables

Learn more about what's new in Destinations V2 [here](/platform/using-airbyte/core-concepts/typing-deduping.md).
