# Source: https://docs.snowflake.com/en/sql-reference/account-usage/ingress_network_access_history.md

Schemas:
:   [ACCOUNT_USAGE](../account-usage.md)

# INGRESS_NETWORK_ACCESS_HISTORY view

This Account Usage view can be used to query any network access attempts to your Snowflake account within the last 365 days (1 year).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| EVENT_TIMESTAMP | TIMESTAMP_LTZ | Time, (in the UTC time zone) of the ingress event occurrence. |
| REQUEST_ID | VARCHAR | Ingress request ID. |
| REQUEST METHOD | VARCHAR. | Ingress request method, such as GET or POST. |
| REQUEST PATH | VARCHAR | Ingress request path. |
| USER_NAME | VARCHAR. | User associated with this event. |
| CLIENT_IP | VARCHAR | Client IP. |
| CLIENT_PRIVATELINK_ID | VARCHAR | Client private link ID. |
| BYTES_RX | NUMBER | Bytes transferred into Snowflake. |
| BYTES_TX | NUMBER | Bytes transferred out of Snowflake. |
| IS_SUCCESS | BOOLEAN | Whether the user’s request was successful or not. |
| ERROR_CODE | VARCHAR | Error code, if the request was not successful. |
| ERROR_MESSAGE | VARCHAR | Error message returned to the user, if the request was not successful. |
| JOB_UUID | VARCHAR | Number automatically assigned to a query job. |
| REQUEST_AUTHORITY | VARCHAR | The URL that a client used to access a Snowflake ingress location. |

## Usage notes

* Latency for the view may be up to 240 minutes (4 hours).

* Although the [INTERNAL_STAGE_NETWORK_ACCESS_HISTORY view](internal_stage_network_access_history.md) is user-enabled, the INGRESS_NETWORK_ACCESS_HISTORY view is enabled by default
  in your Snowflake account.
