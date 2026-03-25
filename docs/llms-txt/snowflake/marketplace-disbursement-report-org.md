# Source: https://docs.snowflake.com/en/collaboration/views/marketplace-disbursement-report-org.md

Schema:
:   [Organization Usage](../../sql-reference/organization-usage.md)

# MARKETPLACE_DISBURSEMENT_REPORT View

The MARKETPLACE_DISBURSEMENT_REPORT view in the [Organization Usage](../../sql-reference/organization-usage.md) schema lets you query the history of your earnings from paid
listings in the Snowflake Marketplace.

The view includes the history for all accounts in your Snowflake organization. Only visible to providers of paid listings, this view includes the history of payment statuses per invoice for purchased listings.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| STRIPE_DISPLAY_NUMBER | VARCHAR | The Stripe invoice or display number. |
| EVENT_DATE | DATE | Date when the payment event occurred. |
| EVENT_TYPE | VARCHAR | Type of event (payment). |
| INVOICE_DATE | DATE | Date of the invoice. |
| LISTING_OWNER_ACCOUNT_NAME | VARCHAR | Name of the provider account that owns the listing. |
| LISTING_OWNER_ACCOUNT_LOCATOR | VARCHAR | Account locator for the provider account that owns the listing. For more information about account identifiers, see [Account identifiers](../../user-guide/admin-account-identifier.md). |
| LISTING_NAME | VARCHAR | Identifier for the listing. |
| LISTING_DISPLAY_NAME | VARCHAR | Display name of the listing. |
| LISTING_GLOBAL_NAME | VARCHAR | Global name of the listing. |
| CHARGE_TYPE | VARCHAR | Type of charge assessed. For more information about the components of the pricing model for paid listings, see [Paid listings pricing models](https://other-docs.snowflake.com/collaboration/provider-listings-pricing-model). Possible values: `FIXED`: Per-month charges. Also includes per-query charges if included by the provider in the pricing plan for the listing. `VARIABLE`: Per-query charges only. |
| GROSS | DECIMAL | Gross amount billed to the consumer. |
| FEES | DECIMAL | Pre-tax fees, owed to Snowflake by the provider. Snowflake subtracts the fees from the gross amount. |
| TAXES | DECIMAL | Sales tax (on the fees), owed to Snowflake by the provider. Snowflake subtracts the taxes from the gross amount. |
| NET_AMOUNT | DECIMAL | Actual amount to be paid to the provider. The equation for this is: `NET_AMOUNT` = `GROSS` - `FEES` - `TAXES`. |
| CURRENCY | VARCHAR | USD |
| CONSUMER_ACCOUNT_NAME | VARCHAR | Name of the consumer account. |
| CONSUMER_ACCOUNT_LOCATOR | VARCHAR | Account locator for the consumer account. |
| CONSUMER_ORGANIZATION_NAME | VARCHAR | Name of the consumer organization. |

## Usage Notes

* Latency for the view can be up to 24 hours (1 day).
* The data is retained for 365 days (1 year).

## Examples

Retrieve the total amount disbursed to a provider’s bank account for each month for each listing:

```sqlexample
SELECT
  event_date
, listing_name
, listing_display_name
, listing_global_name
, currency
, SUM(net_amount) AS net_amount
FROM snowflake.organization_usage.marketplace_disbursement_report
WHERE event_type = 'payment'
GROUP BY 1,2,3,4,5;
```

Retrieve the total amount that has been disbursed for each invoice period, grouped by listing and charge type. Note that the invoice period
could be spread out over multiple report dates:

```sqlexample
SELECT
  invoice_date
, listing_name
, listing_display_name
, listing_global_name
, charge_type
, currency
, SUM(gross) AS gross
, SUM(fees) AS fees
, SUM(taxes) AS taxes
, SUM(net_amount) AS net_amount
FROM snowflake.organization_usage.marketplace_disbursement_report
WHERE event_type = 'payment'
GROUP BY 1,2,3,4,5,6;
```
