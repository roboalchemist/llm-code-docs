# Source: https://docs.airbyte.com/integrations/sources/amazon-ads-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-amazon-ads/latest/icon.svg)

# Amazon Ads Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [7.3.14](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-amazon-ads)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-amazon-ads)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `c6b0a29e-1da9-4512-9002-7bfd0cba2246`

## Upgrading to 7.0.0[​](#upgrading-to-700 "Direct link to Upgrading to 7.0.0")

* The stream SponsoredDisplayReportStream is split into five:

  * sponsored\_display\_campaigns\_report\_stream
  * sponsored\_display\_adgroups\_report\_stream
  * sponsored\_display\_productads\_report\_stream
  * sponsored\_display\_targets\_report\_stream
  * sponsored\_display\_asins\_report\_stream

* The stream SponsoredProductsReportStream is split into seven:

  * sponsored\_products\_campaigns\_report\_stream
  * sponsored\_products\_adgroups\_report\_stream
  * sponsored\_products\_keywords\_report\_stream
  * sponsored\_products\_targets\_report\_stream
  * sponsored\_products\_productads\_report\_stream
  * sponsored\_products\_asins\_keywords\_report\_stream
  * sponsored\_products\_asins\_targets\_report\_stream

* Changes for all \*-report streams:

  * They have new primary keys (see the following table).
  * metrics have been moved to the root of the schema.
  * metrics have been reset to the proper field type (previously, they were all stored as strings).

### Primary Key changes[​](#primary-key-changes "Direct link to Primary Key changes")

| Stream Name                                            | Old Primary Key                                        | New Primary key                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ---------------------------------------------- |
| sponsored\_brands\_v3\_report\_stream                  | \["profileId", "recordType", "reportDate", "recordId"] | \["profileId", "reportDate", "purchasedAsin"]  |
| SponsoredDisplayReportStream (deprecated)              | \["profileId", "recordType", "reportDate", "recordId"] |                                                |
| - sponsored\_display\_campaigns\_report\_stream        |                                                        | \["profileId", "reportDate", "campaignId"]     |
| - sponsored\_display\_adgroups\_report\_stream         |                                                        | \["profileId", "reportDate", "adGroupId"]      |
| - sponsored\_display\_productads\_report\_stream       |                                                        | \["profileId", "reportDate", "adId"]           |
| - sponsored\_display\_targets\_report\_stream          |                                                        | \["profileId", "reportDate", "targetingId"]    |
| - sponsored\_display\_asins\_report\_stream            |                                                        | \["profileId", "reportDate", "promotedAsin"]   |
| SponsoredProductsReportStream (deprecated)             | \["profileId", "recordType", "reportDate", "recordId"] |                                                |
| - sponsored\_products\_campaigns\_report\_stream       |                                                        | \["profileId", "reportDate", "campaignId"]     |
| - sponsored\_products\_adgroups\_report\_stream        |                                                        | \["profileId", "reportDate", "adGroupId"]      |
| - sponsored\_products\_keywords\_report\_stream        |                                                        | \["profileId", "reportDate", "keywordId"]      |
| - sponsored\_products\_targets\_report\_stream         |                                                        | \["profileId", "reportDate", "keywordId"]      |
| - sponsored\_products\_productads\_report\_stream      |                                                        | \["profileId", "reportDate", "adId"]           |
| - sponsored\_products\_asins\_keywords\_report\_stream |                                                        | \["profileId", "reportDate", "advertisedAsin"] |
| - sponsored\_products\_asins\_targets\_report\_stream  |                                                        | \["profileId", "reportDate", "advertisedAsin"] |

## Upgrading to 6.0.0[​](#upgrading-to-600 "Direct link to Upgrading to 6.0.0")

The `SponsoredDisplayReportStream` stream now has an updated schema, thanks to a recent change in the Amazon Ads API. You can find more details in the [Amazon Migration Guide (metrics)](https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/reporting-v2-v3#metrics).

Please note that SponsoredBrandsReportStream and SponsoredBrandsVideoReportStream will become unavailable as a result of the deprecation of API V2. We recommend switching to SponsoredBrandsV3ReportStream as a great alternative. see [Amazon Migration Guide (metrics)](https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/reporting-v2-v3#metrics) for more info.

Streams `SponsoredBrandsReportStream` `SponsoredBrandsVideoReportStream` will become unavailable. It is recommended to use `SponsoredBrandsV3ReportStream` as an alternative.

### Refresh affected schemas and reset data[​](#refresh-affected-schemas-and-reset-data "Direct link to Refresh affected schemas and reset data")

1. Select **Connections** in the main navbar.
   <!-- -->
   1. Select the connection(s) affected by the update.

2. Select the **Replication** tab.

   <!-- -->

   1. Select **Refresh source schema**.
   2. Select **OK**.

```
Any detected schema changes will be listed for your review.
```

3. Select **Save changes** at the bottom of the page.
   <!-- -->
   1. Ensure the **Reset affected streams** option is checked.

```
Depending on destination type you may not be prompted to reset your data.
```

4. Select **Save connection**.

```
This will reset the data in your destination and initiate a fresh sync.
```

For more information on resetting your data in Airbyte, see [this page](/platform/operator-guides/clear.md).

## Upgrading to 5.0.0[​](#upgrading-to-500 "Direct link to Upgrading to 5.0.0")

The following streams have updated schemas due to a change with the Amazon Ads API:

* `SponsoredBrandsCampaigns`
* `SponsoredBrandsAdGroups`
* `SponsoredProductsCampaigns`
* `SponsoredProductsAdGroupBidRecommendations`

### Schema Changes - Removed/Added Fields[​](#schema-changes---removedadded-fields "Direct link to Schema Changes - Removed/Added Fields")

| Stream Name                                  | Removed Fields                                                                                                               | Added Fields                                                                                |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `SponsoredBrandsCampaigns`                   | `serviceStatus`, `bidOptimization`, `bidMultiplier`, `adFormat`, `bidAdjustments`, `creative`, `landingPage`, `supplySource` | `ruleBasedBudget`, `bidding`, `productLocation`, `costType`, `smartDefault`, `extendedData` |
| `SponsoredBrandsAdGroups`                    | `bid`, `keywordId`, `keywordText`, `nativeLanuageKeyword`, `matchType`                                                       | `extendedData`                                                                              |
| `SponsoredProductsCampaigns`                 | `campaignType`, `dailyBudget`, `ruleBasedBudget`, `premiumBidAdjustment`, `networks`                                         | `dynamicBidding`, `budget`, `extendedData`                                                  |
| `SponsoredProductsAdGroupBidRecommendations` | `suggestedBid`                                                                                                               | `theme`, `bidRecommendationsForTargetingExpressions`                                        |

### Refresh affected schemas and reset data[​](#refresh-affected-schemas-and-reset-data-1 "Direct link to Refresh affected schemas and reset data")

1. Select **Connections** in the main navbar.
   <!-- -->
   1. Select the connection(s) affected by the update.

2. Select the **Replication** tab.

   <!-- -->

   1. Select **Refresh source schema**.
   2. Select **OK**.

```
Any detected schema changes will be listed for your review.
```

3. Select **Save changes** at the bottom of the page.
   <!-- -->
   1. Ensure the **Reset affected streams** option is checked.

```
Depending on destination type you may not be prompted to reset your data.
```

4. Select **Save connection**.

```
This will reset the data in your destination and initiate a fresh sync.
```

For more information on resetting your data in Airbyte, see [this page](/platform/operator-guides/clear.md).

## Upgrading to 4.0.0[​](#upgrading-to-400 "Direct link to Upgrading to 4.0.0")

Streams `SponsoredBrandsAdGroups` and `SponsoredBrandsKeywords` now have updated schemas.

### Refresh affected schemas and reset data[​](#refresh-affected-schemas-and-reset-data-2 "Direct link to Refresh affected schemas and reset data")

1. Select **Connections** in the main navbar.
   <!-- -->
   1. Select the connection(s) affected by the update.

2. Select the **Replication** tab.

   <!-- -->

   1. Select **Refresh source schema**.
   2. Select **OK**.

```
Any detected schema changes will be listed for your review.
```

3. Select **Save changes** at the bottom of the page.
   <!-- -->
   1. Ensure the **Reset affected streams** option is checked.

```
Depending on destination type you may not be prompted to reset your data.
```

4. Select **Save connection**.

```
This will reset the data in your destination and initiate a fresh sync.
```

For more information on resetting your data in Airbyte, see [this page](/platform/operator-guides/clear.md).

## Upgrading to 3.0.0[​](#upgrading-to-300 "Direct link to Upgrading to 3.0.0")

A major update of attribution report stream schemas. For a smooth migration, a data reset and a schema refresh are needed.
