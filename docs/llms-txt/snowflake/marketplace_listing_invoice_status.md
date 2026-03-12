# Source: https://docs.snowflake.com/en/collaboration/views/marketplace_listing_invoice_status.md

Schema:
:   [Data Sharing Usage](../../sql-reference/data-sharing-usage.md)

# MARKETPLACE_LISTING_INVOICE_STATUS view

The MARKETPLACE_LISTING_INVOICE_STATUS view in the [Data Sharing Usage](../../sql-reference/data-sharing-usage.md) schema lets you query the history of invoices related to paid listings in the Snowflake Marketplace.

Only visible to providers of paid listings, this view includes the history of payment statuses per invoice for purchased listings.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| STRIPE_DISPLAY_NUMBER | VARCHAR | The Stripe invoice or display number. |
| INVOICE_DATE | DATE | Date of invoice. |
| USAGE_MONTH | VARCHAR | The first month when an invoice is generated, in `YYYY-MM-01` format. For example, if the consumer purchases the listing on 12-MAR-2024, then the date in this field is `2024-03-01`. |
| INVOICE_STATUS | VARCHAR | Status of the invoice. Possible values: `closed` Paid to Snowflake; paid to providers within 30 days. `open` Not yet paid. `void` Canceled. `rebilled` Indicates that a voided invoice was rebilled to make an adjustment. If an invoice is canceled and rebilled, there are two rows for that invoice number: one `void` and one `rebilled`; the invoice created to bill the consumer again has a new number and is `open`. |
| PO_NUMBER | VARCHAR | Purchase order (PO) number specified by the consumer to buy a listing. The PO number is manually entered by the consumer. |
| CURRENCY | VARCHAR | Always USD (alternate currencies are not supported in this view). |
| TOTAL_BILLED_AMOUNT | DECIMAL | Total amount billed to the consumer in USD. This amount includes consumer’s taxes. that apply to the consumer and provider fees. |
| SALES_TAX_AMOUNT | DECIMAL | The sales tax in USD payable by the consumer. This amount is included in the `TOTAL_BILLED_AMOUNT` column amount. |
| FEES | DECIMAL | Provider fees. This amount is included in the `TOTAL_BILLED_AMOUNT` column amount. |
| EXPECTED_PAYOUT_AMOUNT | DECIMAL | The total expected payout to the provider in USD. This value is calculated by subtracting `SALES_TAX_AMOUNT` and `FEES` from `TOTAL_BILLED_AMOUNT`. |
| LISTING_DISPLAY_NAME | VARCHAR | Display name of the listing. |
| LISTING_GLOBAL_NAME | VARCHAR | Global name of the listing. |
| CONSUMER_ORGANIZATION_NAME | VARCHAR | Organization name of the consumer. |
| CONSUMER_ACCOUNT_NAME | VARCHAR | Account name of the consumer. |
| CONSUMER_ACCOUNT_LOCATOR | VARCHAR | Account locator of the consumer. |
| CONSUMER_COMPANY_NAME | VARCHAR | Company name of the consumer. |
| CONSUMER_BILLING_EMAIL_ADDRESS | VARCHAR | Email address associated with billing for the consumer. |

## Usage Notes

* Latency for the view can be up to 48 hours (2 days).
* The data is retained for 365 days (1 year).

## Examples

Retrieve billing information for export.

```sqlexample
SELECT
  stripe_display_number AS snowflake_mp_invoice_number,
  invoice_date,
  usage_month AS first_billing_month,
  invoice_status,
  po_number,
  currency,
  total_billed_amount,
  listing_display_name,
  listing_global_name,
  consumer_organization_name,
  consumer_account_name,
  consumer_account_locator,
  consumer_company_name,
  consumer_billing_email_address
FROM snowflake.data_sharing_usage.marketplace_listing_invoice_status;
```

Retrieve details of unpaid invoices by consumer.

```sqlexample
SELECT
  consumer_account_name,
  consumer_account_locator,
  SUM( total_billed_amount ) AS total_outstanding
FROM snowflake.data_sharing_usage.marketplace_listing_invoice_status
WHERE invoice_status IN ('open')
GROUP BY ALL;
```
