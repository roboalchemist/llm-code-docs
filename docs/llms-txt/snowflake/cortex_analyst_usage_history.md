# Source: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_analyst_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CORTEX_ANALYST_USAGE_HISTORY view

The CORTEX_ANALYST_USAGE_HISTORY view can be used to query the usage history of [Cortex Analyst](../../user-guide/snowflake-cortex/cortex-analyst.md).

The information in the view includes the number of credits consumed each time Cortex Analyst is called, aggregated in one-hour increments.
The view also includes relevant metadata, such as the start and end times of the messages and the number of messages sent.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the specified time range in which the Cortex Analyst message request was received. |
| END_TIME | TIMESTAMP_LTZ | End of the specified time range in which the Cortex Analyst message response was sent. |
| REQUEST_COUNT | NUMBER | The number of messages sent to Cortex Analyst. |
| CREDITS | NUMBER | The number of credits billed for a set of messages sent to Cortex Analyst. |
| USERNAME | TEXT | The username of the user who sent the Cortex Analyst message request. The username is included with the session.  For more information about authenticating, see [Authenticating to the server](../../developer-guide/sql-api/authenticating.md). |

## Usage notes

* The view provides up-to-date credit usage for an account within the last 365 days (1 year).
* Credit rate usage is based on the number of messages processed, as outlined in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).
