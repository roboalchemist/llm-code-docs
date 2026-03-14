# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/storage_daily_history.md

Schema:
:   [ORGANIZATION_USAGE](../organization-usage.md)

# STORAGE_DAILY_HISTORY view

The STORAGE_DAILY_HISTORY view in the ORGANIZATION_USAGE schema can be used to query the average daily storage usage, in bytes, for all accounts in the organization for the last 365 days (1 year).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| SERVICE_TYPE | VARCHAR | The type of service, which can be one of `STORAGE`, `STORAGE_READER`. |
| ORGANIZATION_NAME | VARCHAR | Name of the organization. |
| ACCOUNT_NAME | VARCHAR | Name of the account (user-defined). |
| USAGE_DATE | DATE | The date (in the UTC time zone) on which the usage took place. |
| AVERAGE_BYTES | NUMBER | Average number of bytes of database storage and stage storage used on this date, including data in Time Travel and Fail-safe. |
| REGION | VARCHAR | ID of the Snowflake Region where the account is located. |
| ACCOUNT_LOCATOR | VARCHAR | Locator for the account (system-defined). |
| CREDITS | NUMBER | Total number of storage credits used for the account on this date. (Calculated as AVERAGE_BYTES, converted to tebibytes, divided by the number of days in the month.) |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).
* The data is retained for 365 days (1 year).
