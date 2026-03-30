# Source: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_provisioned_throughput_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CORTEX_PROVISIONED_THROUGHPUT_USAGE_HISTORY view

This Account Usage view lets you retrieve billing data for provisioned throughputs.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| PROVISIONED_THROUGHPUT_ID | VARCHAR | UUID identifying the provisioned throughput. |
| INTERVAL_START_TIME | TIMESTAMP_TZ | Start of the measurement interval for the billing period. |
| INTERVAL_END_TIME | TIMESTAMP_TZ | End of the measurement interval for the billing period. |
| CLOUD_SERVICE_PROVIDER | VARCHAR | Host cloud provider. |
| MODEL_NAME | VARCHAR | Configured model name. |
| TERM_START_DATE | DATE | Start of the provisioned throughput’s term. |
| TERM_END_DATE | DATE | End of the provisioned throughput’s term. |
| PTU_COUNT | NUMBER | Number of PTUs active. |
| PTU_CREDITS | NUMBER(38,9) | Number of credits billed during this interval. |

## Usage notes

* The view provides up-to-date credit usage for an account within the last 365 days (1 year).
