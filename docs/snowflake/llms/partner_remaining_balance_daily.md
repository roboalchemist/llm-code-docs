# Source: https://docs.snowflake.com/en/sql-reference/billing/partner_remaining_balance_daily.md

Schema:
:   [BILLING](../billing.md)

# PARTNER_REMAINING_BALANCE_DAILY view

The PARTNER_REMAINING_BALANCE_DAILY view in the BILLING schema provides the daily remaining balance and the on-demand consumption daily for a reseller’s customers.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ORGANIZATION_NAME | VARCHAR | Name of the reseller’s organization. |
| SOLD_TO_ORGANIZATION_NAME | VARCHAR | Name of the organization of the reseller’s customer. |
| SOLD_TO_CUSTOMER_NAME | VARCHAR | Name of the reseller’s customer. |
| SOLD_TO_PO_NUMBER | VARCHAR | Purchase order number associated with the reseller’s sale to the customer. |
| SOLD_TO_CONTRACT_NUMBER | VARCHAR | Number associated with the customer’s contract with the reseller. |
| DATE | DATE | Date of the FREE_USAGE_BALANCE or CAPACITY_BALANCE in UTC. |
| CURRENCY | VARCHAR | Currency of the FREE_USAGE_BALANCE, or CAPACITY_BALANCE, or ON_DEMAND_CONSUMPTION_BALANCE. |
| FREE_USAGE_BALANCE | NUMBER (38,2) | Amount of free usage in currency that is available for use as of the date. This is the end of day balance. |
| CAPACITY_BALANCE | NUMBER (38,2) | Amount of capacity in currency that is available for use as of the date. This is the end of day balance. |
| ON_DEMAND_CONSUMPTION_BALANCE | NUMBER (38,2) | Amount of consumption at on demand prices that will be invoiced given that all the free usage and capacity balances have been exhausted. This is a negative value (e.g. -250) until the invoice is paid. This is the end of day balance. |
| ROLLOVER_BALANCE | NUMBER (38,2) | Amount of rollover balance in currency that is available for use at the end of the date. At the end of a contract term, it is calculated as sum(AMOUNT) from the CONTRACT_ITEMS view - sum(USAGE_IN_CURRENCY) from the PARTNER_USAGE_IN_CURRENCY_DAILY view. |
| MARKETPLACE_CAPACITY_DRAWDOWN_BALANCE | NUMBER (38,2) | Amount of CAPACITY_BALANCE that is available for purchases in the Snowflake Marketplace. |

## Usage notes

* Latency for the view may be up to 24 hours.
* On demand consumption balance resets after month close (typically on the 3rd or 4th day of the next month) after it is invoiced and paid.
* Until month close, data for a given day in a month can change to account for any end-of-month adjustments or contract amendments between Snowflake organizations.

## Example query

To query the remaining balance for all your customers’ organizations on the last day of February 2022:

```sqlexample
SELECT date AS balancedate,
  *,
  capacity_balance + free_usage_balance + rollover_balance AS total_balance
  FROM snowflake.billing.partner_remaining_balance_daily
  WHERE date = '2022-02-28';
```
