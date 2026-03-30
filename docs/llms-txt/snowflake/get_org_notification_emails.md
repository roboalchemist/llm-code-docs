# Source: https://docs.snowflake.com/en/sql-reference/classes/anomaly-insights/methods/get_org_notification_emails.md

# ANOMALY_INSIGHTS!GET_ORG_NOTIFICATION_EMAILS

Returns the email addresses where notifications are sent when there is an [organization-level cost anomaly](../../../../user-guide/cost-anomalies.md).
An organization-level anomaly occurs when the aggregate consumption for all accounts falls outside an expected range.

## Syntax

```sqlsyntax
SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_ORG_NOTIFICATION_EMAILS()
```

## Arguments

None.

## Output

Returns a table with the following column:

| Column name | Data type | Description |
| --- | --- | --- |
| EMAIL_LIST | VARCHAR | Comma-delimited list of email addresses where notifications are sent when there is an organization-level cost anomaly. |

## Access control requirements

Users with any of the following roles can call this method:

* ACCOUNTADMIN system role
* GLOBALORGADMIN system role
* SNOWFLAKE.ORGANIZATION_BILLING_VIEWER application role in the organization account
* SNOWFLAKE.APP_ORGANIZATION_BILLING_VIEWER application role in an ORGADMIN-enabled account

## Example

The following example returns the list of email addresses that are notified when there is an organization-level cost anomaly.

```sqlexample
CALL SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_ORG_NOTIFICATION_EMAILS();
```
