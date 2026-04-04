# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/password_policies.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/password_policies.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# PASSWORD_POLICIES view

This Account Usage view provides the user-defined [password policies](../../user-guide/password-authentication.md) in your account.

Each row in this view corresponds to a different password policy.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| NAME | VARCHAR | Name of the policy. |
| ID | NUMBER | Internal/system-generated identifier for the password policy. |
| SCHEMA_ID | VARCHAR | Internal/system-generated identifier for the schema in which the policy resides. |
| SCHEMA | VARCHAR | Schema to which the password policy belongs. |
| DATABASE_ID | VARCHAR | Internal/system-generated identifier for the database in which the policy resides. |
| DATABASE | VARCHAR | Database to which the password policy belongs. |
| OWNER | VARCHAR | Name of the role that owns the password policy. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| PASSWORD_MIN_LENGTH | NUMBER | Minimum password length allowed for the policy. |
| PASSWORD_MAX_LENGTH | NUMBER | Maximum password length allowed for the policy. |
| PASSWORD_MIN_UPPER_CASE_CHARS | NUMBER | Minimum number of uppercase characters allowed for the policy. |
| PASSWORD_MIN_LOWER_CASE_CHARS | NUMBER | Minimum number of lowercase characters allowed for the policy. |
| PASSWORD_MIN_NUMERIC_CHARS | NUMBER | Minimum number of numeric characters allowed for the policy. |
| PASSWORD_MIN_SPECIAL_CHARS | NUMBER | Minimum number of special characters allowed for the policy. |
| PASSWORD_MIN_AGE_DAYS | NUMBER | The number of days a user must wait before a recently changed password can be changed again. |
| PASSWORD_MAX_AGE_DAYS | NUMBER | Maximum number of days password is valid. |
| PASSWORD_MAX_RETRIES | NUMBER | Maximum number of password attempts allowed. |
| PASSWORD_LOCKOUT_TIME_MINS | NUMBER | Minimum time in minutes before password can be retried. |
| COMMENT | VARCHAR | Comments entered for the password policy (if any). |
| CREATED | TIMESTAMP_LTZ | Date and time when the password policy was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time when the password policy was last altered. |
| DELETED | TIMESTAMP_LTZ | Date and time when the password policy was dropped. |
| PASSWORD_HISTORY | NUMBER | The number of the most recent passwords that Snowflake stores. These stored passwords cannot be repeated when a user updates their password value. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.
