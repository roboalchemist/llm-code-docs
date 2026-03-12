# Source: https://docs.snowflake.com/en/sql-reference/classes/anomaly-insights/methods/get_hourly_spend_for_anomaly.md

# ANOMALY_INSIGHTS!GET_HOURLY_SPEND_FOR_ANOMALY

Returns the hourly consumption in the current account on a specific day.

## Syntax

```sqlsyntax
SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_HOURLY_SPEND_FOR_ANOMALY(
  '<date>' )
```

## Arguments

`'date'`
:   Specifies the day for which you want to return consumption data.

    Data type: DATE

## Output

Returns a table with the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| HOUR | INTEGER | Specifies the hour of the day during which consumption occurred. |
| CONSUMPTION | NUMBER | Specifies the amount of consumption during the hour in credits. |

## Access control requirements

Users with any of the following roles can call this method:

* ACCOUNTADMIN system role
* GLOBALORGADMIN system role
* SNOWFLAKE.APP_USAGE_ADMIN application role
* SNOWFLAKE.APP_USAGE_VIEWER application role

## Usage notes

* A day is defined by a 24-hour period in UTC. This might differ from a user’s local time zone.
* This method returns consumption data for the current account. It cannot be used to return data for other accounts or the entire
  organization.
* This method returns credits consumed for the account (not currency).

## Example

The following example returns the hourly consumption on October 17, 2024.

```sqlexample
CALL SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_HOURLY_SPEND_FOR_ANOMALY('2024-10-17');
```
