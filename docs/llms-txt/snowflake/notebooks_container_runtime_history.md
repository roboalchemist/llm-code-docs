# Source: https://docs.snowflake.com/en/sql-reference/account-usage/notebooks_container_runtime_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# NOTEBOOKS_CONTAINER_RUNTIME_HISTORY view

You can use the NOTEBOOKS_CONTAINER_RUNTIME_HISTORY view in the ACCOUNT_USAGE schema to return the hourly credit usage for notebooks running on Snowpark Container Services within the last 365 days (1 year).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | The date and beginning of the hour (in the local time zone) in which the usage took place. |
| END_TIME | TIMESTAMP_LTZ | The date and end of the hour (in the local time zone) in which the usage took place. |
| NOTEBOOK_NAME | VARCHAR | The name of the notebook (running on Snowpark Container Services) that incurred the credit usage. |
| NOTEBOOK_ID | NUMBER | The ID of the notebook that incurred the credit usage. |
| USER_NAME | VARCHAR | The name of the user associated with the notebook. NULL if the notebook was not run interactively. |
| USER_ID | NUMBER | The ID of the user associated with the notebook. NULL if the notebook was not run interactively. |
| COMPUTE_POOL_NAME | VARCHAR | The name of the compute pool associated with the notebook. |
| COMPUTE_POOL_ID | NUMBER | The ID of the compute pool associated with the notebook. |
| SERVICE_NAME | VARCHAR | The name of the service associated with the notebook. |
| SERVICE_ID | NUMBER | The ID of the service associated with the notebook. |
| NOTEBOOK_EXECUTION_TIME_SECS | NUMBER | The run time of the notebook in the given hour. |
| CREDITS | NUMBER(38, 9) | The number of credits that the notebook used in the hour. |

## Usage notes

* Latency for the view might be up to 180 minutes (3 hours).

* The view provides hourly container notebook credit usage for an account within the last 365 days (1 year).
* The credit rate usage is determined based on the machine type (instance family) of the compute pool, as outlined in the consumption table.
