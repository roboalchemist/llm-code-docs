# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/data_transfer_daily_history.md

Schema:
:   [ORGANIZATION_USAGE](../organization-usage.md)

# DATA_TRANSFER_DAILY_HISTORY view

The DATA_TRANSFER_DAILY_HISTORY view in the ORGANIZATION_USAGE schema can be used to query the history of data transferred from Snowflake tables into a different cloud storage provider’s network (i.e. from Snowflake on Amazon Web Services (AWS), Google Cloud Platform, or Microsoft Azure into the other cloud provider’s network) and/or geographical region within the last 365 days (1 year).

The view includes the history of data transfer for all accounts in your Snowflake organization.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| SERVICE_TYPE | VARCHAR | Either `DATA_TRANSFER` or [INTERNAL_DATA_TRANSFER](../../developer-guide/snowpark-container-services/accounts-orgs-usage-views.md). |
| ORGANIZATION_NAME | VARCHAR | Name of the organization . |
| ACCOUNT_NAME | VARCHAR | Name of the account. |
| USAGE_DATE | DATE | Date (in the UTC time zone) in which the usage took place. |
| TB_TRANSFERED | FLOAT | Number of terabytes transferred during the USAGE_DATE. |
| REGION | VARCHAR | ID of the Snowflake Region where the account is located. |
| ACCOUNT_LOCATOR | VARCHAR | Account locator for the account. |

## Usage notes

* Latency for the view may be up to 24 hours.
