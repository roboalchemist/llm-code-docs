# Source: https://docs.snowflake.com/en/sql-reference/account-usage/openflow_usage_history.md

Schemas:
:   [ACCOUNT_USAGE](../account-usage.md)

# OPENFLOW_USAGE_HISTORY view

This Account Usage view returns the hourly runtime credit usage for an account within the last 365 days (1 year).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | The date and beginning of the hour (in the local time zone) in which the usage took place. |
| END_TIME | TIMESTAMP_LTZ | The date and end of the hour (in the local time zone) in which the usage took place. |
| DATA_PLANE_ID | VARCHAR | ID of the data plane which incurred the credit usage. |
| DATA_PLANE_NAME | VARCHAR | Name of the data plane which incurred the credit usage. |
| DATA_PLANE_TYPE | VARCHAR | Type of the data plane. Supported values include:  *`BYOC`* `SNOWFLAKE` |
| DATA_PLANE_CREDITS_USED | NUMBER | Number of compute credits the data plane used in the hour. The data plane credits are only incurred for SNOWFLAKE data planes. For `BYOC`, there are no credits incurred for data planes and customers are charged credits only for runtime usage. |
| RUNTIME_ID | VARCHAR | ID of the runtime which incurred the credit usage. |
| RUNTIME_NAME | VARCHAR | Name of the runtime which incurred the credit usage. |
| RUNTIME_TYPE | VARCHAR | Type of the runtime. Supported values include:   *`RUNTIME`* `READ_ONLY RUNTIME` |
| RUNTIME_CREDITS_USED | NUMBER | Number of compute credits the runtime used in the hour. This does not include the credits used by the data plane or the credits used to ingest the data in Snowflake. |
