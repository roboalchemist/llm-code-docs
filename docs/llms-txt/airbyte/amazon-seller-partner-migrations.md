# Source: https://docs.airbyte.com/integrations/sources/amazon-seller-partner-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-amazon-seller-partner/latest/icon.svg)

# Amazon Seller Partner Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [5.5.0](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-amazon-seller-partner)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-amazon-seller-partner)(last updated 13 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `e55879a8-0ef8-4557-abcf-ab34c53ec460`

## Upgrading to 5.0.0[​](#upgrading-to-500 "Direct link to Upgrading to 5.0.0")

Two deprecated FBA Subscribe and Save report types have been removed from the connector per Amazon SP-API deprecation:

* `GET_FBA_SNS_FORECAST_DATA` (Subscribe and Save Forecast Report)
* `GET_FBA_SNS_PERFORMANCE_DATA` (Subscribe and Save Performance Report)

These report types were deprecated by Amazon and will return empty responses starting July 25, 2025, and will be completely removed on December 11, 2025. See [Amazon's deprecation notice](https://developer-docs.amazon.com/sp-api/changelog/deprecation-of-two-fba-subscribe-and-save-report-types) for more details.

### Action Required[​](#action-required "Direct link to Action Required")

If you have these streams enabled in your connection:

1. **Refresh the source schema** to remove the deprecated streams from your catalog
2. **No data reset is required** - these streams are simply being removed from the available streams list

### Steps to Update[​](#steps-to-update "Direct link to Steps to Update")

1. Select **Connections** in the main navbar.
   <!-- -->
   1. Select the connection(s) affected by the update.

2. Select the **Replication** tab.

   <!-- -->

   1. Select **Refresh source schema**.
   2. Select **OK**.

```
The deprecated streams will no longer appear in your available streams list.
```

3. Select **Save changes** at the bottom of the page.

```
No data reset is required for this upgrade as the streams are being removed, not modified.
```

4. Select **Save connection**.

For more information on managing your Airbyte connections, see the [Airbyte documentation](/platform/operator-guides/clear.md).

## Upgrading to 4.0.0[​](#upgrading-to-400 "Direct link to Upgrading to 4.0.0")

Stream `GET_FBA_STORAGE_FEE_CHARGES_DATA` now has updated schema, which matches Amazon Seller Partner [docs](https://developer-docs.amazon.com/sp-api/docs/fba-inventory-reports-attributes#get_fba_storage_fee_charges_data).

Users will need to refresh the source schema and reset this stream after upgrading.

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

Streams `GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL` and `GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL` now have updated schemas.

The following streams now have date-time formatted fields:

| Stream                                        | Affected fields                                                               | Format change                                                        |
| --------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL` | `estimated-arrival-date`                                                      | `string YYYY-MM-DDTHH:mm:ssZ` -> `date-time YYYY-MM-DDTHH:mm:ssZ`    |
| `GET_LEDGER_DETAIL_VIEW_DATA`                 | `Date and Time`                                                               | `string YYYY-MM-DDTHH:mm:ssZ` -> `date-time YYYY-MM-DDTHH:mm:ssZ`    |
| `GET_MERCHANTS_LISTINGS_FYP_REPORT`           | `Status Change Date`                                                          | `string MMM D[,] YYYY` -> `date-time YYYY-MM-DD`                     |
| `GET_STRANDED_INVENTORY_UI_DATA`              | `Date-to-take-auto-removal`                                                   | `string YYYY-MM-DDTHH:mm:ssZ` -> `date-time YYYY-MM-DDTHH:mm:ssZ`    |
| `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE`     | `settlement-start-date`, `settlement-end-date`, `deposit-date`, `posted-date` | `string YYYY-MM-DDTHH:mm:ssZ` -> `date-time YYYY-MM-DDTHH:mm:ssZ`    |
| `GET_MERCHANT_LISTINGS_ALL_DATA`              | `open-date`                                                                   | `string YYYY-MM-DD HH:mm:ss ZZZ` -> `date-time YYYY-MM-DDTHH:mm:ssZ` |
| `GET_MERCHANT_LISTINGS_DATA`                  | `open-date`                                                                   | `string YYYY-MM-DD HH:mm:ss ZZZ` -> `date-time YYYY-MM-DDTHH:mm:ssZ` |
| `GET_MERCHANT_LISTINGS_INACTIVE_DATA`         | `open-date`                                                                   | `string YYYY-MM-DD HH:mm:ss ZZZ` -> `date-time YYYY-MM-DDTHH:mm:ssZ` |
| `GET_MERCHANT_LISTINGS_DATA_BACK_COMPAT`      | `open-date`                                                                   | `string YYYY-MM-DD HH:mm:ss ZZZ` -> `date-time YYYY-MM-DDTHH:mm:ssZ` |

Users will need to refresh the source schemas and reset these streams after upgrading.

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

This change removes Brand Analytics and permanently removes deprecated FBA reports (from Airbyte Cloud). Customers who have those streams must refresh their schema OR disable the following streams:

* `GET_BRAND_ANALYTICS_MARKET_BASKET_REPORT`
* `GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORT`
* `GET_BRAND_ANALYTICS_REPEAT_PURCHASE_REPORT`
* `GET_BRAND_ANALYTICS_ALTERNATE_PURCHASE_REPORT`
* `GET_BRAND_ANALYTICS_ITEM_COMPARISON_REPORT`
* `GET_SALES_AND_TRAFFIC_REPORT`
* `GET_VENDOR_SALES_REPORT`
* `GET_VENDOR_INVENTORY_REPORT`

Customers, who have the following streams, will have to disable them:

* `GET_FBA_FULFILLMENT_INVENTORY_ADJUSTMENTS_DATA`
* `GET_FBA_FULFILLMENT_CURRENT_INVENTORY_DATA`
* `GET_FBA_FULFILLMENT_INVENTORY_RECEIPTS_DATA`
* `GET_FBA_FULFILLMENT_INVENTORY_SUMMARY_DATA`
* `GET_FBA_FULFILLMENT_MONTHLY_INVENTORY_DATA`
