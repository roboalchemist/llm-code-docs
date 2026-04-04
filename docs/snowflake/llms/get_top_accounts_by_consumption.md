# Source: https://docs.snowflake.com/en/sql-reference/classes/anomaly-insights/methods/get_top_accounts_by_consumption.md

# ANOMALY_INSIGHTS!GET_TOP_ACCOUNTS_BY_CONSUMPTION

Returns accounts with the highest absolute change in consumption between a given date and the previous date. Helps investigate
[organization-level cost anomalies](../../../../user-guide/cost-anomalies.md).

## Syntax

```sqlsyntax
SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_TOP_ACCOUNTS_BY_CONSUMPTION(
  '<date>',
  <number_of_accounts> )
```

## Arguments

`'date'`
:   Specifies the date for which you want to return consumption data.

    Data type: DATE

`number_of_accounts`
:   Limits the number of accounts returned by the method. For example, if you specify `5`, the method returns only the top five accounts in
    the organization in terms of change in consumption.

    Data type: NUMBER

## Output

Returns a table with the following columns. Results are ordered by largest daily change in absolute value.

| Column name | Data type | Description |
| --- | --- | --- |
| ACCOUNT_NAME | VARCHAR | Name of the account where consumption occurred. |
| CONSUMPTION | NUMBER | Amount of consumption measured in CURRENCY. |
| CURRENCY | VARCHAR | Unit of measure for the consumption. For information about why the unit of measure is credits or a currency, see [Unit of measure for cost data](../../../../user-guide/cost-anomalies.md). |
| COST_CHANGE | NUMBER | Difference between consumption on the specified day and the previous day. |

## Access control requirements

Users with any of the following roles can call this method:

* ACCOUNTADMIN system role
* GLOBALORGADMIN system role
* SNOWFLAKE.APP_USAGE_ADMIN application role
* SNOWFLAKE.APP_USAGE_VIEWER application role

## Usage notes

You must call this method from the [organization account](../../../../user-guide/organization-accounts.md) or an
[ORGADMIN-enabled account](../../../../user-guide/organization-administrators.md).

## Example

The following example returns the top seven accounts in terms of change in consumption when comparing December 16, 2024, and December 17,
2024.

```sqlexample
CALL SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_TOP_ACCOUNTS_BY_CONSUMPTION('2024-12-17', 7);
```
