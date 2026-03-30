# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/referential_constraints.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/referential_constraints.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/referential_constraints.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# REFERENTIAL_CONSTRAINTS view

This Account Usage view displays a row for each FOREIGN KEY constraint that is defined for tables in the account.

FOREIGN KEY constraints are used to enforce referential integrity. For more information, see
[Constraints](../constraints.md) and [Referential Integrity Constraints](../../user-guide/table-considerations.md).

To return information about other constraint types (as well as FOREIGN KEY constraints), query the [TABLE_CONSTRAINTS view](table_constraints.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| CONSTRAINT_CATALOG_ID | NUMBER | Internal/system-generated identifier for the database of the constraint. |
| CONSTRAINT_CATALOG | VARCHAR | Database that the constraint belongs to |
| CONSTRAINT_SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema of the constraint. |
| CONSTRAINT_SCHEMA | VARCHAR | Schema that the constraint belongs to |
| CONSTRAINT_NAME | VARCHAR | Name of the constraint |
| UNIQUE_CONSTRAINT_CATALOG_ID | NUMBER | Internal/system-generated identifier for the database of the current constraint. |
| UNIQUE_CONSTRAINT_CATALOG | VARCHAR | Database of the unique constraint referenced by the current constraint. |
| UNIQUE_CONSTRAINT_SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema of the constraint. |
| UNIQUE_CONSTRAINT_SCHEMA | VARCHAR | Schema of the unique constraint referenced by the current constraint. |
| UNIQUE_CONSTRAINT_NAME | VARCHAR | Name of the unique constraint referenced by the current constraint. |
| MATCH_OPTION | VARCHAR | Match option for the constraint. |
| UPDATE_RULE | VARCHAR | Update Rule for the current constraint. |
| DELETE_RULE | VARCHAR | Delete Rule for the current constraint. |
| COMMENT | VARCHAR | Comment for the constraint. |
| CREATED | TIMESTAMP_LTZ | Date and time when the constraint was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| DELETED | TIMESTAMP_LTZ | Date and time when the constraint was dropped. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The view only displays objects for which the current role for the session has been granted access privileges.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.
