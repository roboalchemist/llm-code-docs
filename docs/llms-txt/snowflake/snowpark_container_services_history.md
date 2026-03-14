# Source: https://docs.snowflake.com/en/sql-reference/account-usage/snowpark_container_services_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# SNOWPARK_CONTAINER_SERVICES_HISTORY view

The SNOWPARK_CONTAINER_SERVICES_HISTORY view in the ACCOUNT_USAGE schema can be used to return the hourly
[compute pool](../../developer-guide/snowpark-container-services/working-with-compute-pool.md) credit usage for an account within the last 365 days (1 year).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | The date and beginning of the hour (in the local time zone) in which the usage took place. |
| END_TIME | TIMESTAMP_LTZ | The date and end of the hour (in the local time zone) in which the usage took place. |
| COMPUTE_POOL_NAME | VARCHAR | Name of the compute pool which incurred the credit usage. |
| IS_EXCLUSIVE | BOOLEAN | TRUE, if the compute pool was created for an [application](../../developer-guide/native-apps/native-apps-about.md). |
| APPLICATION_NAME | VARCHAR | The name of the application for which the compute pool was created. NULL if the compute pool was not created for an application or if the application no longer exists. |
| APPLICATION_ID | VARCHAR | The ID of the application for which the compute pool was created; otherwise NULL. |
| CREDITS_USED | NUMBER | Number of credits the compute pool used in the hour. |

## Usage notes

* Latency for the view may be up to 180 minutes (3 hours).

* The view provides hourly [compute pool](../../developer-guide/snowpark-container-services/working-with-compute-pool.md) credit usage for an account within the last 365 days (1 year).
* The credit rate usage is determined based on the machine type (instance family) of the compute pool, as outlined in the consumption table.
