# Source: https://docs.snowflake.com/en/sql-reference/classes/anomaly-insights/methods/get_daily_consumption_anomaly_data.md

# ANOMALY_INSIGHTS!GET_DAILY_CONSUMPTION_ANOMALY_DATA

Returns daily consumption for a specific account or the entire organization, and identifies whether that consumption is considered a
[cost anomaly](../../../../user-guide/cost-anomalies.md).

> **Note:**
>
> This method returns consumption with a currency as the unit of measure. If you want to return consumption in credits instead, see
> [ANOMALY_INSIGHTS!GET_ACCOUNT_ANOMALIES_IN_CREDITS](get_account_anomalies_in_credits.md).

## Syntax

```sqlsyntax
SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_DAILY_CONSUMPTION_ANOMALY_DATA(
  '<start_date>',
  '<end_date>',
  <account_name> )
```

## Arguments

`'start_date'`
:   Specifies the beginning of the time period for which consumption data is returned.

    Data type: DATE

`'end_date'`
:   Specifies the end of the time period for which consumption data is returned.

    Data type: DATE

`account_name`
:   Specifies an expression that determines the account(s) for which consumption data is returned. You can specify the following values:

    * `'account_name'`: Returns data for the specified account. You must specify the account name, not the account locator.
    * `CURRENT_ACCOUNT_NAME()`: Returns data for the current account.
    * `NULL`: Returns data for the entire organization, not a specific account.

## Output

Returns a table with the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| USAGE_DATE | DATE | Day in UTC when the consumption occurred. |
| CONSUMPTION | NUMBER (38,2) | Amount of consumption measured in CURRENCY_TYPE. |
| FORECASTED_CONSUMPTION | NUMBER (38,2) | Predicted consumption based on the anomaly-detecting algorithm, measured in CURRENCY_TYPE. |
| UPPER_BOUND | NUMBER (38,2) | Predicted highest level of consumption based on the anomaly-detecting algorithm, measured in CURRENCY_TYPE. Consumption levels above this value are considered an anomaly. |
| LOWER_BOUND | NUMBER (38,2) | Predicted lowest level of consumption based on the anomaly-detecting algorithm, measured in CURRENCY_TYPE. Consumption levels below this value are considered an anomaly. |
| IS_ANOMALY | BOOLEAN | If true, consumption has been identified as a cost anomaly because it has gone outside the range of the upper and lower bound. |
| CURRENCY_TYPE | VARCHAR | Unit of measure for the consumption. For information about why the unit of measure is credits or a currency, see [Unit of measure for cost data](../../../../user-guide/cost-anomalies.md). |
| ANOMALY_ID | VARCHAR | System-generated identifier. |

## Access control requirements

Users with any of the following roles can call this method:

* ACCOUNTADMIN system role
* GLOBALORGADMIN system role
* ORGANIZATION_BILLING_VIEWER application role in the organization account
* SNOWFLAKE.APP_ORGANIZATION_BILLING_VIEWER application role in an ORGADMIN-enabled account

## Usage notes

To return data for a different account or the entire organization, you must execute this method from the
[organization account](../../../../user-guide/organization-accounts.md) or an
[ORGADMIN-enabled account](../../../../user-guide/organization-administrators.md).

## Example

Identify organization-level anomalies based on consumption between January 1, 2024, and March 31, 2024:

```sqlexample
CALL SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_DAILY_CONSUMPTION_ANOMALY_DATA(
  '2024-01-01', '2024-03-31', NULL);
```

Identify anomalies in the current account based on consumption between January 1, 2024, and March 31, 2024:

```sqlexample
CALL SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_DAILY_CONSUMPTION_ANOMALY_DATA(
  '2024-01-01', '2024-03-31', current_account_name());
```

Identify anomalies in the account `prod_acct1` based on consumption between January 1, 2024, and March 31, 2024:

```sqlexample
CALL SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_DAILY_CONSUMPTION_ANOMALY_DATA(
  '2024-01-01', '2024-03-31', 'prod_acct1');
```
