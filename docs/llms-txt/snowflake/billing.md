# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/migration-assistant/billing.md

# Source: https://docs.snowflake.com/en/developer-guide/streamlit/object-management/billing.md

# Source: https://docs.snowflake.com/en/sql-reference/billing.md

# BILLING schema

In the SNOWFLAKE database, the BILLING schema contains views that display billing information for customers of Snowflake resellers and
distributors. Only resellers and distributors can access the views in the BILLING schema.

## BILLING views

The BILLING schema contains the following views:

| View | Latency | Notes |
| --- | --- | --- |
| [PARTNER_CONTRACT_ITEMS](billing/partner_contract_items.md) | 24 hours |  |
| [PARTNER_RATE_SHEET_DAILY](billing/partner_rate_sheet_daily.md) | 24 hours |  |
| [PARTNER_REMAINING_BALANCE_DAILY](billing/partner_remaining_balance_daily.md) | 24 hours |  |
| [PARTNER_USAGE_IN_CURRENCY_DAILY](billing/partner_usage_in_currency_daily.md) | 24 hours |  |

## Accessing the BILLING schema

The BILLING schema is available in the [organization account](../user-guide/organization-accounts.md) and a regular account that has the
[ORGADMIN role enabled](../user-guide/organization-administrators.md).

You must use the ACCOUNTADMIN role to access the views in the schema.
