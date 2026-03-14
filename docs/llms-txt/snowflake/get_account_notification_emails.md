# Source: https://docs.snowflake.com/en/sql-reference/classes/anomaly-insights/methods/get_account_notification_emails.md

# ANOMALY_INSIGHTS!GET_ACCOUNT_NOTIFICATION_EMAILS

Returns the email addresses where notifications are sent when there is an [account-level cost anomaly](../../../../user-guide/cost-anomalies.md) in
the current account.

## Syntax

```sqlsyntax
SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_ACCOUNT_NOTIFICATION_EMAILS()
```

## Arguments

None.

## Output

Returns a table with the following column:

| Column name | Data type | Description |
| --- | --- | --- |
| EMAIL_LIST | VARCHAR | Comma-delimited list of email addresses where notifications are sent when there is a cost anomaly in the current account. |

## Access control requirements

Users with any of the following roles can call this method:

* ACCOUNTADMIN system role
* GLOBALORGADMIN system role
* SNOWFLAKE.APP_USAGE_ADMIN application role

## Usage notes

This method retrieves the email notification list for the account in which it is called.

## Example

The following example returns the email addresses where notifications are sent.

```sqlexample
CALL SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_ACCOUNT_NOTIFICATION_EMAILS();
```
