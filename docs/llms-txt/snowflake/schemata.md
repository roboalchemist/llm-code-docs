# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/schemata.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/schemata.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/schemata.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# SCHEMATA view

This Account Usage view displays a row for each schema in the account except the ACCOUNT_USAGE, READER_ACCOUNT_USAGE, and INFORMATION_SCHEMA schemas.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema. |
| SCHEMA_NAME | VARCHAR | Name of the schema. |
| CATALOG_ID | NUMBER | Internal/system-generated identifier for the database of the schema. |
| CATALOG_NAME | VARCHAR | Database that the schema belongs to. |
| SCHEMA_OWNER | VARCHAR | Name of the role that owns the schema. |
| RETENTION_TIME | NUMBER | Number of days that historical data is retained for Time Travel. |
| IS_TRANSIENT | VARCHAR | Whether the schema is transient. |
| IS_MANAGED_ACCESS | VARCHAR | Whether the schema is a managed access schema. |
| DEFAULT_CHARACTER_SET_CATALOG | VARCHAR | Not applicable for Snowflake. |
| DEFAULT_CHARACTER_SET_SCHEMA | VARCHAR | Not applicable for Snowflake. |
| DEFAULT_CHARACTER_SET_NAME | VARCHAR | Not applicable for Snowflake. |
| SQL_PATH | VARCHAR | Not applicable for Snowflake. |
| COMMENT | VARCHAR | Comment for the schema. |
| CREATED | TIMESTAMP_LTZ | Date and time when the schema was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| DELETED | TIMESTAMP_LTZ | Date and time when the schema was dropped. |
| SCHEMA_TYPE | VARCHAR | Specifies the schema type. Valid values are: . . - STANDARD: normal schema. . - VERSIONED: versioned schema. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| SCHEMA_TYPE | VARCHAR | Type of schema. Possible values are `STANDARD` and `VERSIONED`. |
| VERSION_NAME | VARCHAR | Name of the schema if it is a versioned schema. NULL otherwise. |
| VERSIONED_SCHEMA_ID | NUMBER | Internal/system-generated identifier if the schema is a versioned schema. NULL, otherwise. |
| OBJECT_VISIBILITY | OBJECT | `OBJECT_VISIBILITY`  [Preview Feature](../../release-notes/preview-features.md) — Open  Available to all accounts.  This property controls the [discoverability of the objects](../../user-guide/ui-snowsight/object-visibility-universal-search.md) in the account, enabling users without explicit access privileges to find objects and request access. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The view only displays objects for which the current role for the session has been granted access privileges.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.
