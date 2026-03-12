# Source: https://docs.airbyte.com/integrations/sources/facebook-marketing-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-facebook-marketing/latest/icon.svg)

# Facebook Marketing Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [5.0.1](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-facebook-marketing)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-facebook-marketing)(last updated 15 days ago)

* CDK Version

  [7.4.1](https://pypi.org/project/airbyte-cdk/7.4.1/)

* Sync Success Rate

* Usage Rate

* Definition ID

  `e7778cfc-e97c-4458-9ecb-b4f2bba8946c`

## Upgrading to 5.0.0[​](#upgrading-to-500 "Direct link to Upgrading to 5.0.0")

This version includes three breaking schema changes:

### 1. Level-based primary keys for Custom Insights[​](#1-level-based-primary-keys-for-custom-insights "Direct link to 1. Level-based primary keys for Custom Insights")

Custom Insights streams now use level-based primary keys. Previously, all Custom Insights streams used `ad_id` as part of their primary key regardless of the configured `level` setting. This caused issues when using `level=adset`, `level=campaign`, or `level=account` because the `ad_id` field would be null, making deduplication impossible.

With this update, the primary key now correctly reflects the configured level:

| Level          | Primary Key Fields                                             |
| -------------- | -------------------------------------------------------------- |
| `ad` (default) | `date_start`, `account_id`, `ad_id`, plus any breakdowns       |
| `adset`        | `date_start`, `account_id`, `adset_id`, plus any breakdowns    |
| `campaign`     | `date_start`, `account_id`, `campaign_id`, plus any breakdowns |
| `account`      | `date_start`, `account_id`, plus any breakdowns                |

### 2. Removed deprecated attribution window columns[​](#2-removed-deprecated-attribution-window-columns "Direct link to 2. Removed deprecated attribution window columns")

The `7d_view` and `28d_view` columns have been removed from all Ads Insights streams. Meta deprecated these attribution windows on January 12, 2026, and they have been returning null values since that date. Only `1d_view` remains as a supported view-through attribution window. The click-through windows (`1d_click`, `7d_click`, `28d_click`) are unaffected.

### 3. Removed `wish_bid` field[​](#3-removed-wish_bid-field "Direct link to 3-removed-wish_bid-field")

The `wish_bid` field has been removed from Ads Insights streams. This field was already excluded from API requests because it caused data inaccuracies (incorrect `spend` values) and has been returning null.

### Who is affected?[​](#who-is-affected "Direct link to Who is affected?")

All users syncing any Ads Insights stream (built-in or custom) are affected by the schema column removals (changes 2 and 3). Users that sync Custom Insights streams with `level=adset`, `level=campaign`, or `level=account` are additionally affected by the primary key change (change 1). Users syncing only default `level=ad` Custom Insights or only built-in Ads Insights streams only need to refresh their schema for the column removals.

### Steps to upgrade[​](#steps-to-upgrade "Direct link to Steps to upgrade")

1. Select **Connections** in the main navbar.
   <!-- -->
   1. Select the connection(s) affected by the update.

2. Select the **Schema** tab.

   <!-- -->

   1. Select **Refresh source schema**.
   2. Select **OK**.

   note

   Any detected schema changes will be listed for your review.

3. Select **Save changes** at the bottom of the page.
   <!-- -->
   1. Ensure the **Clear affected streams** option is checked.

4. Select **Save connection**.

   <!-- -->

   note

   This will reset the data in your destination and initiate a fresh sync.

For more information on resetting your data in Airbyte, see [this page](/platform/operator-guides/clear.md).

## Upgrading to 4.0.0[​](#upgrading-to-400 "Direct link to Upgrading to 4.0.0")

The connector has been updated to use [v23.0 of Meta's Marketing API](https://developers.facebook.com/docs/marketing-api/marketing-api-changelog/version23.0) as v21.0 will be deprecated on September 9, 2025.

Three fields from the `AdCreatives` stream have been deprecated:

* `instagram_actor_id` -> `instagram_user_id`
* `effective_instagram_story_id` -> `effective_instagram_media_id`
* `instagram_story_id` -> `source_instagram_media_id`

See the [v22.0 changelog](https://developers.facebook.com/docs/marketing-api/marketing-api-changelog/version22.0) for more information

### Steps to refresh the AdCreatives stream schema:[​](#steps-to-refresh-the-adcreatives-stream-schema "Direct link to Steps to refresh the AdCreatives stream schema:")

1. Select **Connections** in the main navbar.
   <!-- -->
   1. Select the connection(s) affected by the update.

2. Select the **Schema** tab.

   <!-- -->

   1. Select **Refresh source schema**.
   2. Select **OK**
   3. Select **Save changes** at the bottom of the page.

   note

   Any detected schema changes will be listed for your review.

## Upgrading to 3.1.0[​](#upgrading-to-310 "Direct link to Upgrading to 3.1.0")

The `AdsInsights` Reports now don't have the possibility to fetch the next root level properties (fields):

* cost\_per\_conversion\_lead
* conversion\_lead\_rate

### Refresh affected AdsInsights Report:[​](#refresh-affected-adsinsights-report "Direct link to Refresh affected AdsInsights Report:")

1. Select **Connections** in the main navbar.
   <!-- -->
   1. Select the connection(s) affected by the update.

2. Select the **Schema** tab.

   <!-- -->

   1. Select **Refresh source schema**.
   2. Select **OK**
   3. Select **Save changes** at the bottom of the page.

   note

   Any detected schema changes will be listed for your review.

### Custom streams[​](#custom-streams "Direct link to Custom streams")

Custom streams will not be able to rely on `cost_per_conversion_lead` and `conversion_lead_rate` as `fields` anymore. Those streams will need to updated considering the fact that the information is not available in Facebook Marketing.

## Upgrading to 3.0.0[​](#upgrading-to-300 "Direct link to Upgrading to 3.0.0")

Custom Insights Reports now have updated schema for following breakdowns:

* body\_asset
* call\_to\_action\_asset
* description\_asset
* image\_asset
* link\_url\_asset
* title\_asset
* video\_asset

| Field                  | Old Type | New Type | Example                                                                                                                           |
| ---------------------- | -------- | -------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `body_asset`           | string   | object   | `{"text": "Body Text", "id": "12653412653"}`                                                                                      |
| `call_to_action_asset` | string   | object   | `{"name": "Action Name", "id": "12653412653"}`                                                                                    |
| `description_asset`    | string   | object   | `{"text": "Description", "id": "12653412653"}`                                                                                    |
| `image_asset`          | string   | object   | `{"hash": "hash_value", "url": "http://url","id": "12653412653" }`                                                                |
| `link_url_asset`       | string   | object   | `{"website_url": "http://url","id": "12653412653" }`                                                                              |
| `title_asset`          | string   | object   | `{"text": "Text", "id": "12653412653" }`                                                                                          |
| `video_asset`          | string   | object   | `{"video_id": "2412334234", "url": "http://url", "thumbnail_url: "http://url", "video_name": "Video Name", "id": "12653412653" }` |

### Refresh affected Custom Insights Report above and clear data if it uses breakdowns[​](#refresh-affected-custom-insights-report-above-and-clear-data-if-it-uses-breakdowns "Direct link to Refresh affected Custom Insights Report above and clear data if it uses breakdowns")

1. Select **Connections** in the main navbar.

   1. Select the connection(s) affected by the update.

2. Select the **Schema** tab.

   1. Select **Refresh source schema**.
   2. Select **OK**
   3. Select **Save changes** at the bottom of the page.

   note

   Any detected schema changes will be listed for your review.

3. Navigate to a connection's **Settings** tab and click **Clear data** to clear all streams. This action will clear data for all streams in the connection. To clear data for a single stream navigate to the **Status** tab, click the **three grey dots** next to the affected stream, and select **Clear data**. Do this for all affected streams in the connection.

For more information on clearing your data in Airbyte, see [this page](/platform/operator-guides/clear.md).

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

Streams Ads-Insights-\* streams now have updated schemas.

danger

Please note that data older than 37 months will become unavailable due to Facebook limitations. It is recommended to create a backup at the destination before proceeding with migration.

### Update Custom Insights Reports (this step can be skipped if you did not define any)[​](#update-custom-insights-reports-this-step-can-be-skipped-if-you-did-not-define-any "Direct link to Update Custom Insights Reports (this step can be skipped if you did not define any)")

1. Select **Sources** in the main navbar.
   <!-- -->
   1. Select the Facebook Marketing Connector.
2. Select the **Retest saved source**.
3. Remove unsupported fields from the list in Custom Insights section.
4. Select **Test and Save**.

### Refresh affected schemas and reset data[​](#refresh-affected-schemas-and-reset-data "Direct link to Refresh affected schemas and reset data")

1. Select **Connections** in the main navbar.
   <!-- -->
   1. Select the connection(s) affected by the update.

2. Select the **Replication** tab.

   <!-- -->

   1. Select **Refresh source schema**.
   2. Select **OK**.

note

Any detected schema changes will be listed for your review.

3. Select **Save changes** at the bottom of the page. 1. Ensure the **Reset affected streams** option is checked.

   <!-- -->

   note

   Depending on destination type you may not be prompted to reset your data.

4. Select **Save connection**.

   <!-- -->

   note

   This will reset the data in your destination and initiate a fresh sync.

For more information on resetting your data in Airbyte, see [this page](/platform/operator-guides/clear.md).
