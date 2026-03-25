# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/session_policies.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/session_policies.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# SESSION_POLICIES view

This Account Usage view provides the [session policies](../../user-guide/session-policies.md) in your account.

Each row in this view corresponds to a different session policy.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | NUMBER | Internal/system-generated identifier for the session policy. |
| NAME | VARCHAR | Name of the session policy. |
| SCHEMA_ID | VARCHAR | Internal/system-generated identifier for the schema in which the policy resides. |
| SCHEMA | VARCHAR | Schema to which the session policy belongs. |
| DATABASE_ID | VARCHAR | Internal/system-generated identifier for the database in which the policy resides. |
| DATABASE | VARCHAR | Database to which the session policy belongs. |
| OWNER | VARCHAR | Name of the role that owns the session policy. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| SESSION_IDLE_TIMEOUT_MINS | NUMBER | Session idle timeout in minutes for the policy. |
| SESSION_UI_IDLE_TIMEOUT_MINS | NUMBER | UI session idle timeout in minutes for the policy. |
| COMMENT | VARCHAR | Comments entered for the session policy (if any). |
| CREATED | TIMESTAMP_LTZ | Date and time when the session policy was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| DELETED | TIMESTAMP_LTZ | Date and time when the session policy was dropped. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.
