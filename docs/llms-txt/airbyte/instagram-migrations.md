# Source: https://docs.airbyte.com/integrations/sources/instagram-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-instagram/latest/icon.svg)

# Instagram Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [4.2.18](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-instagram)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-instagram)(last updated 15 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `6acf6b55-4f1e-4fca-944e-1a3caef8aba8`

## Upgrading to 4.0.0[​](#upgrading-to-400 "Direct link to Upgrading to 4.0.0")

This release removes certain deprecated metrics. Hence, the following metrics in the following streams will become unavailable:

* `MediaInsights` Stream:

  * `clips_replays_count`
  * `ig_reels_aggregated_all_plays_count`
  * `impressions`
  * `plays`

* `UserInsights` Stream:

  * `impressions`

* `StoryInsights` Stream:

  * `impressions`

To ensure uninterrupted syncs, users should follow the instructions below to migrate to version 4.0.0:

1. Select **Connections** in the main navbar. 1.1 Select the connection(s) affected by the update.
2. Select the **Replication** tab. 2.1 Select **Refresh source schema**. `note Any detected schema changes will be listed for your review. `2.2 Select **OK**.
3. Select **Save changes** at the bottom of the page. 3.1 Ensure the **Reset affected streams** option is checked. `note Depending on destination type, you may not be prompted to reset your data.`
4. Select **Save connection**. `note This will reset the data in your destination and initiate a fresh sync.`

For more information on resetting your data in Airbyte, see [this page](/platform/operator-guides/clear.md).

## Upgrading to 3.0.0[​](#upgrading-to-300 "Direct link to Upgrading to 3.0.0")

The Instagram connector has been upgrade to API v18 (following the deprecation of v11). Connector will be upgraded to API v18. Affected Streams and their corresponding changes are listed below:

* `Media Insights`

  Old metric will be replaced with the new ones, refer to the [IG Media Insights](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights#metrics) for more info.

  | Old metric                    | New metric          |
  | ----------------------------- | ------------------- |
  | carousel\_album\_engagement   | total\_interactions |
  | carousel\_album\_impressions  | impressions         |
  | carousel\_album\_reach        | reach               |
  | carousel\_album\_saved        | saved               |
  | carousel\_album\_video\_views | video\_views        |
  | engagement                    | total\_interactions |

note

You may see different results: `engagement` count includes likes, comments, and saves while `total_interactions` count includes likes, comments, and saves, as well as shares.

New metrics for Reels: `ig_reels_avg_watch_time`, `ig_reels_video_view_total_time`

* `User Lifetime Insights`

  * Metric `audience_locale` will become unavailable.
  * Metrics `audience_city`, `audience_country`, and `audience_gender_age` will be consolidated into a single metric named `follower_demographics`, featuring respective breakdowns for `city`, `country`, and `age,gender`.
  * Primary key will be changed to `["business_account_id", "breakdown"]`.

note

Due to Instagram limitations, the "Metric Type" will be set to `total_value` for `follower_demographics` metric. Refer to the [docs](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights#metric-type) for more info.

* `Story Insights`

  Metrics: `exits`, `taps_back`, `taps_forward` will become unavailable.

Please follow the instructions below to migrate to version 3.0.0:

1. Select **Connections** in the main navbar. 1.1 Select the connection(s) affected by the update.
2. Select the **Replication** tab. 2.1 Select **Refresh source schema**. `note Any detected schema changes will be listed for your review. `2.2 Select **OK**.
3. Select **Save changes** at the bottom of the page. 3.1 Ensure the **Reset affected streams** option is checked. `note Depending on destination type, you may not be prompted to reset your data.`
4. Select **Save connection**. `note This will reset the data in your destination and initiate a fresh sync.`

For more information on resetting your data in Airbyte, see [this page](/platform/operator-guides/clear.md).

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

This release adds a default primary key for the streams UserLifetimeInsights and UserInsights, and updates the format of timestamp fields in the UserLifetimeInsights, UserInsights, Media and Stories streams to include timezone information.

To ensure uninterrupted syncs, users should:

* Refresh the source schema
* Reset affected streams
