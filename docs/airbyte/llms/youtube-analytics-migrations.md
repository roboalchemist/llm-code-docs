# Source: https://docs.airbyte.com/integrations/sources/youtube-analytics-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-youtube-analytics/latest/icon.svg)

# YouTube Analytics Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.2.3](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-youtube-analytics)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-youtube-analytics)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `afa734e4-3571-11ec-991a-1e0031268139`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

Version 1.0.0 updates the connector to use the latest versions of YouTube's Bulk Reports API in response to YouTube's Shorts view-counting change. YouTube announced the change on March 26, 2025, Shorts view counting changed on March 31, 2025, and the Bulk Reports API was updated on June 30, 2025. See the YouTube API revision history for details.

### What changed[​](#what-changed "Direct link to What changed")

YouTube updated how views are counted for Shorts:

* **For Shorts**: Views now count the number of times a Short starts to play or replay, with no minimum watch time requirement.
* **For videos**: No change to how views are counted.
* **New metric**: A new `engaged_views` column has been added to reports, which reflects the previous view-counting methodology.

As a result of this change, each affected report's version has incremented by one (for example, version a2 to version a3 for channel reports, and a1 to a2 for playlist reports). See the [YouTube API revision history](https://developers.google.com/youtube/reporting/revision_history) for complete details.

**Important**: previous report versions were deprecated on October 31, 2025. You must upgrade to version 1.0.0 to continue syncing YouTube Analytics data.

## New stream names[​](#new-stream-names "Direct link to New stream names")

| Old Stream                       | New Stream                       |
| -------------------------------- | -------------------------------- |
| channel\_basic\_a2               | channel\_basic\_a3               |
| channel\_combined\_a2            | channel\_combined\_a3            |
| channel\_device\_os\_a2          | channel\_device\_os\_a3          |
| channel\_playback\_location\_a2  | channel\_playback\_location\_a3  |
| channel\_province\_a2            | channel\_province\_a3            |
| channel\_subtitles\_a2           | channel\_subtitles\_a3           |
| channel\_traffic\_source\_a2     | channel\_traffic\_source\_a3     |
| playlist\_basic\_a1              | playlist\_basic\_a2              |
| playlist\_combined\_a1           | playlist\_combined\_a2           |
| playlist\_device\_os\_a1         | playlist\_device\_os\_a2         |
| playlist\_playback\_location\_a1 | playlist\_playback\_location\_a2 |
| playlist\_province\_a1           | playlist\_province\_a2           |
| playlist\_traffic\_source\_a1    | playlist\_traffic\_source\_a2    |

## Migration Steps[​](#migration-steps "Direct link to Migration Steps")

### Refresh source schemas and clear data[​](#refresh-source-schemas-and-clear-data "Direct link to Refresh source schemas and clear data")

Clearing your data is required for the affected streams to continue syncing successfully. To clear your data for the affected streams, follow the steps below:

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
