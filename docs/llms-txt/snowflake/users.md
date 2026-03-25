# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/users.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/users.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# USERS view

This Account Usage view can be used to query a list of all users in the account.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| USER_ID | NUMBER | Internal/system-generated identifier for the user. |
| NAME | VARCHAR | A unique identifier for the user. |
| CREATED_ON | TIMESTAMP_LTZ | Date and time (in the UTC time zone) when the user’s account was created. |
| DELETED_ON | TIMESTAMP_LTZ | Date and time (in the UTC time zone) when the user’s account was deleted. |
| LOGIN_NAME | VARCHAR | Name that the user enters to log into the system. |
| DISPLAY_NAME | VARCHAR | Name displayed for the user in the Snowflake web interface. |
| FIRST_NAME | VARCHAR | First name of the user. |
| LAST_NAME | VARCHAR | Last name of the user. |
| EMAIL | VARCHAR | Email address for the user. |
| MUST_CHANGE_PASSWORD | BOOLEAN | Specifies whether the user is forced to change their password on their next login. |
| HAS_PASSWORD | BOOLEAN | Specifies whether a password was created for the user. |
| COMMENT | VARCHAR | Comment for the user. |
| DISABLED | VARIANT | Specified whether the user account is disabled preventing the user from logging in to the Snowflake and running queries. |
| SNOWFLAKE_LOCK | VARIANT | Specifies whether a temporary lock has been placed on the user’s account. |
| DEFAULT_WAREHOUSE | VARCHAR | The virtual warehouse that is active by default for the user’s session upon login. |
| DEFAULT_NAMESPACE | VARCHAR | The namespace (database only or database and schema) that is active by default for the user’s session upon login. |
| DEFAULT_ROLE | VARCHAR | The role that is active by default for the user’s session upon login. |
| EXT_AUTHN_DUO | BOOLEAN | Specifies whether Duo Security is enabled for the user, which requires the user to use MFA (multi-factor authorization) for login. |
| EXT_AUTHN_UID | VARCHAR | The authorization ID used for Duo Security. |
| HAS_MFA | BOOLEAN | Specifies whether the user is enrolled for multi-factor authentication. |
| BYPASS_MFA_UNTIL | TIMESTAMP_LTZ | The number of minutes to temporarily bypass MFA for the user. |
| LAST_SUCCESS_LOGIN | TIMESTAMP_LTZ | Date and time (in the UTC time zone) when the user last logged in to the Snowflake. |
| EXPIRES_AT | TIMESTAMP_LTZ | The date and time when the user’s status is set to `EXPIRED` and the user can no longer log in. This is useful for defining temporary users (e.g. users who should only have access to Snowflake for a limited time period). |
| LOCKED_UNTIL_TIME | TIMESTAMP_LTZ | Specifies the number of minutes until the temporary lock on the user login is cleared. |
| HAS_RSA_PUBLIC_KEY | BOOLEAN | Specifies whether RSA public key used for key pair authentication has been set up for the user. |
| PASSWORD_LAST_SET_TIME | TIMESTAMP_LTZ | The timestamp on which the last non-null password was set for the user. Default to null if no password has been set yet or if Snowflake is unable to determine the timestamp for the user before the inclusion of this column. |
| OWNER | VARCHAR | Specifies the role with the OWNERSHIP privilege on the object. |
| DEFAULT_SECONDARY_ROLE | VARCHAR | Specifies the default secondary role for the user (that is, ALL) or NULL if not set. |
| HAS_PAT | BOOLEAN | If TRUE, a [programmatic access token (PAT)](../../user-guide/programmatic-access-tokens.md) has been generated for the user. |
| HAS_WORKLOAD_IDENTITY | BOOLEAN | If TRUE, the user is configured to use [workload identity federation](../../user-guide/workload-identity-federation.md) to authenticate with Snowflake. |
| TYPE | VARCHAR | Specifies the [type of user](../../user-guide/admin-user-management.md). |
| DATABASE_NAME | VARCHAR | When the user TYPE is SNOWFLAKE_SERVICE, it specifies the service’s database name; otherwise, it’s NULL. |
| DATABASE_ID | NUMBER | When the user TYPE is SNOWFLAKE_SERVICE, it specifies the internal, Snowflake-generated identifier for the service’s database; otherwise, it’s NULL. |
| SCHEMA_NAME | VARCHAR | When the user TYPE is SNOWFLAKE_SERVICE, it specifies the service’s schema name; otherwise, it’s NULL. |
| SCHEMA_ID | NUMBER | When the user TYPE is SNOWFLAKE_SERVICE, it specifies the internal, Snowflake-generated identifier for the service’s schema; otherwise, it’s NULL. |
| IS_FROM_ORGANIZATION_USER | BOOLEAN | If TRUE, the user was imported from an [organization user](../../user-guide/organization-users.md). |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The `LAST_SUCCESS_LOGIN` column may have a value that differs from the `last_success_login` column in the
  SHOW USERS command output because of different methodologies used to record near-real-time and historical logins. The
  column might have a NULL value if the login history data for the user is outside the one-year retention period of
  historical data.
* Columns that are not applicable to service users (that is, users with `TYPE=SERVICE`) contain NULL values. For example,
  `HAS_PASSWORD` contains NULL values for service users.
* The `deletedOn` column might not be accurate for Snowpark Container Services [service user](../../developer-guide/snowpark-container-services/spcs-execute-sql.md). For services created before release 8.42.0, the `deletedOn` column of the service user shows as empty even if the associated service is dropped; For services created after release 8.42.0, the `deletedOn` column of the service user shows as the deletion time of the associating service.

### Internal Snowflake User for Snowsight

The first time [Snowsight](../../user-guide/ui-snowsight.md) is accessed in an account, Snowflake creates an internal WORKSHEETS_APP_USER user to support the web interface. This user is used to cache query results in an internal stage in an account. For more information, see [Getting started with Snowsight](../../user-guide/ui-snowsight-gs.md).
