# Source: https://docs.snowflake.com/en/sql-reference/account-usage/internal_stage_network_access_history.md

Schemas:
:   [ACCOUNT_USAGE](../account-usage.md)

# INTERNAL_STAGE_NETWORK_ACCESS_HISTORY view

This Account Usage view can be used to query any network access attempts to an internal stage within the last 365 days (1 year).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| EVENT_TIMESTAMP | TIMESTAMP_LTZ | Cloud service provider event timestamp. |
| EVENT_ID | VARCHAR | Cloud service provider event ID. |
| EVENT_NAME | VARCHAR | Cloud service provider event name. |
| EVENT_TYPE | VARCHAR | Cloud service provider event type. |
| CLOUD_PROVIDER | VARCHAR | Cloud service provider. |
| USER_NAME | VARCHAR | User associated with this event. |
| CLIENT_IP | VARCHAR | Client IP accessing the internal stage. |
| CLIENT_PRIVATELINK_ID | VARCHAR | Client private link ID accessing the internal stage: for example, a VPCE ID. |
| BYTES_IN | NUMBER | Bytes transferred into the stage. |
| BYTES_OUT | NUMBER | Bytes transferred out of the stage. |
| IS_SUCCESS | BOOLEAN | Whether the user’s request was successful or not. |
| ERROR_CODE | VARCHAR | Error code, if the request was not successful. |
| ERROR_MESSAGE | VARCHAR | Error message returned to the user, if the request was not successful. |
| AUTHENTICATION_METHOD | VARCHAR | Cloud service provider authentication method, such as `AuthHeader` or `QueryString`. |
| STAGE_PATH | VARCHAR | Network directory path for the internal stage location. For example, the path appearing after the AWS bucket name in the URL. |

## Usage notes

* Latency for the view may be up to 360 minutes (6 hours).
* To enable the view in your account, call the [SYSTEM$OPT_IN_INTERNAL_STAGE_NETWORK_LOGS](../functions/system_opt_in_internal_stage_network_logs.md) function.
* To disable the view in your account, call the [SYSTEM$OPT_OUT_INTERNAL_STAGE_NETWORK_LOGS](../functions/system_opt_out_internal_stage_network_logs.md) function.

* Network access record collection starts at the time you enable the view.
* Network access records are retained for 1 year, starting at the time you enable the view.
