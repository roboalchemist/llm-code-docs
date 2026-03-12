# Source: https://docs.snowflake.com/en/sql-reference/info-schema/usage_privileges.md

# USAGE_PRIVILEGES view

In accordance with the ANSI standard, this view displays a row for each privilege defined for sequences in the specified (or current) database.

To view privileges on other types of objects, use the [OBJECT_PRIVILEGES view](object_privileges.md) view.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| GRANTOR | VARCHAR | Role who granted the usage privilege |
| GRANTEE | VARCHAR | Role to whom the usage privilege is granted |
| GRANTED_TO | VARCHAR | Type of object that has been granted the privilege |
| OBJECT_CATALOG | VARCHAR | Database containing the object on which the privilege is granted |
| OBJECT_SCHEMA | VARCHAR | Schema containing the object on which the privilege is granted |
| OBJECT_NAME | VARCHAR | Name of the object on which the privilege is granted |
| OBJECT_TYPE | VARCHAR | Type of the object on which the privilege is granted |
| PRIVILEGE_TYPE | VARCHAR | Type of the granted privilege |
| IS_GRANTABLE | VARCHAR | Whether the privilege was granted WITH GRANT OPTION |
| CREATED | TIMESTAMP_LTZ | Creation time of the privilege |

## Usage notes

* The view only displays objects for which the current role for the session has been granted access privileges.
