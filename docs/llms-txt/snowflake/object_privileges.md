# Source: https://docs.snowflake.com/en/sql-reference/info-schema/object_privileges.md

# OBJECT_PRIVILEGES view

This Information Schema view displays a row for each access privilege granted for all objects defined in your account. It includes the privileges displayed in the [TABLE_PRIVILEGES view](table_privileges.md) and
[USAGE_PRIVILEGES view](usage_privileges.md).

For more information about privileges and their impact on object access, see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

See also:
:   [APPLICABLE_ROLES view](applicable_roles.md) , [ENABLED_ROLES view](enabled_roles.md) , [TABLE_PRIVILEGES view](table_privileges.md)

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| GRANTOR | VARCHAR | Role who granted the privilege |
| GRANTEE | VARCHAR | Role to whom the privilege is granted |
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
