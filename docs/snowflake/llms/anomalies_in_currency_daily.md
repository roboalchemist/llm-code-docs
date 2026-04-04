# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/anomalies_in_currency_daily.md

Schema:
:   [ORGANIZATION_USAGE](../organization-usage.md)

# ANOMALIES_IN_CURRENCY_DAILY view

This Organization Usage view provides insights into whether [cost anomalies](../../user-guide/cost-anomalies.md) occurred in accounts in the
organization.

Each row provides the consumption of an account on a specific day, and whether that consumption was a cost anomaly.

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| DATE | DATE | Day in UTC when the consumption occurred. |
| ANOMALY_ID | VARCHAR | System-generated identifier. |
| IS_ANOMALY | BOOLEAN | If true, consumption has been identified as a cost anomaly because it has gone outside the range of the upper and lower bound. |
| ORGANIZATION_NAME | VARCHAR | Name of the organization. |
| ACCOUNT_NAME | VARCHAR | Name of the account where consumption occurred. |
| ACCOUNT_LOCATOR | VARCHAR | Account locator of the account where consumption occurred. |
| REGION | VARCHAR | Snowflake region where the account is located. |
| ACTUAL_VALUE | NUMBER | Amount of consumption measured in CURRENCY. |
| CURRENCY | VARCHAR | Unit of measure for the consumption. |
| UPPER_BOUND | NUMBER | Predicted highest level of consumption based on the anomaly-detecting algorithm, measured in CURRENCY. Consumption levels above this value are considered an anomaly. |
| LOWER_BOUND | NUMBER | Predicted lowest level of consumption based on the anomaly-detecting algorithm, measured in CURRENCY. Consumption levels below this value are considered an anomaly. |
| FORECASTED_VALUE | NUMBER | Predicted consumption based on the anomaly-detecting algorithm, measured in CURRENCY. |

## Usage notes

Latency for the view might be up to 8 hours.
