# Source: https://docs.airbyte.com/integrations/sources/google-ads-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-google-ads/latest/icon.svg)

# Google Ads Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [4.1.6](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-google-ads)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-google-ads)(last updated 21 days ago)

* CDK Version

  [7.9.2](https://pypi.org/project/airbyte-cdk/7.9.2/)

* Sync Success Rate

* Usage Rate

* Definition ID

  `253487c0-2246-43ba-a21f-5116b20a2c50`

## Upgrading to 4.0.0[​](#upgrading-to-400 "Direct link to Upgrading to 4.0.0")

This release upgrades the Google Ads API from Version 18 to Version 20 which causes the following changes in the schemas:

| Stream          | Current field name                           | New field name                                                                                                   |
| --------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| campaign        | campaign.dynamic\_search\_ads\_setting.feeds | This field has been deleted                                                                                      |
| user\_interests | user\_interest.availabilities                | Updated advertisingChannelSubType enum for the Video channel: removed VIDEO\_OUTSTREAM and added YOUTUBE\_AUDIO. |

For custom queries, the stream may fail if a field was removed during the API update. Additionally, some field values may have changed, such as `user_interest.availabilities`. You can use the [Query Builder](https://developers.google.com/google-ads/api/fields/v20/query_validator) to validate your custom queries.

Users should:

* Refresh the source schema
* Reset affected streams after upgrading to ensure uninterrupted syncs.

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

## Upgrading to 3.0.0[​](#upgrading-to-300 "Direct link to Upgrading to 3.0.0")

This release upgrades the Google Ads API from Version 13 to Version 15 which causes the following changes in the schemas:

| Stream                        | Current field name                                                               | New field name                                                                 |
| ----------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| ad\_listing\_group\_criterion | ad\_group\_criterion.listing\_group.case\_value.product\_bidding\_category.id    | ad\_group\_criterion.listing\_group.case\_value.product\_category.category\_id |
| ad\_listing\_group\_criterion | ad\_group\_criterion.listing\_group.case\_value.product\_bidding\_category.level | ad\_group\_criterion.listing\_group.case\_value.product\_category.level        |
| shopping\_performance\_view   | segments.product\_bidding\_category\_level1                                      | segments.product\_category\_level1                                             |
| shopping\_performance\_view   | segments.product\_bidding\_category\_level2                                      | segments.product\_category\_level2                                             |
| shopping\_performance\_view   | segments.product\_bidding\_category\_level3                                      | segments.product\_category\_level3                                             |
| shopping\_performance\_view   | segments.product\_bidding\_category\_level4                                      | segments.product\_category\_level4                                             |
| shopping\_performance\_view   | segments.product\_bidding\_category\_level5                                      | segments.product\_category\_level5                                             |
| campaign                      | campaign.shopping\_setting.sales\_country                                        | This field has been deleted                                                    |

Users should:

* Refresh the source schema
* Reset affected streams after upgrading to ensure uninterrupted syncs.

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

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

This release updates the Source Google Ads connector so that its default streams and stream names match the related resources in [Google Ads API](https://developers.google.com/google-ads/api/fields/v14/ad_group_ad).

Users should:

* Refresh the source schema
* And reset affected streams after upgrading to ensure uninterrupted syncs.

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

This release introduced fixes to the creation of custom query schemas. For instance, the field ad\_group\_ad.ad.final\_urls in the custom query has had its type changed from `{"type": "string"}` to `{"type": ["null", "array"], "items": {"type": "string"}}`. Users should refresh the source schema and reset affected streams after upgrading to ensure uninterrupted syncs.
