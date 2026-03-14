# Source: https://docs.snowflake.com/en/sql-reference/classes/anomaly-insights/methods/set_org_notification_emails.md

# ANOMALY_INSIGHTS!SET_ORG_NOTIFICATION_EMAILS

Defines the list of email addresses that will receive a notification when there is an
[organization-level cost anomaly](../../../../user-guide/cost-anomalies.md).

An organization-level anomaly occurs when the aggregate consumption all of accounts falls outside an expected range. If you want to define
a list of email addresses that will receive a notification when a specific account has a cost anomaly, see
[ANOMALY_INSIGHTS!SET_ACCOUNT_NOTIFICATION_EMAILS](set_account_notification_emails.md).

> **Note:**
>
> Email notifications are processed through Snowflake’s Amazon Web Services (AWS) deployments, using AWS Simple Email Service
> (SES). The content of an email message sent using AWS may be retained by Snowflake for up to thirty days to manage the delivery
> of the message. After this period, the message content is deleted.

## Syntax

```sqlsyntax
SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!SET_ORG_NOTIFICATION_EMAILS(
  '<email_address> [, <email_address> ... ]' )
```

## Arguments

`'email_address [, email_address ... ]'`
:   Comma-delimited list of email addresses that will receive a notification when there is an organization-level cost anomaly.

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

## Usage notes

* Each email address must have been [verified by the user](../../../../user-guide/ui-snowsight-profile.md).
* You can use a group email address, such as a distribution list, for notifications, but this email address must be verified. Before adding
  a group email address to the notification list, you might need to create a new Snowflake user with the group email address so you can
  verify it.

## Example

Set the email notification list so that users with email addresses `user1@example.com` and `user2@example.com` receive a notification
when there is an organization-level cost anomaly:

```sqlexample
CALL SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!SET_ORG_NOTIFICATION_EMAILS(
  'user1@example.com, user2@example.com');
```
