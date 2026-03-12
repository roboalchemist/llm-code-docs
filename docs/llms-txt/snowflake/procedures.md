# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/procedures.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/procedures.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/procedures.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# PROCEDURES view

This Account Usage view displays a row for each stored procedure defined in the account.

For more information about stored procedures, see [Stored procedures overview](../../developer-guide/stored-procedure/stored-procedures-overview.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| PROCEDURE_CATALOG | VARCHAR | Database to which the stored procedure belongs. |
| PROCEDURE_SCHEMA | VARCHAR | Schema to which the stored procedure belongs. |
| PROCEDURE_NAME | VARCHAR | Name of the stored procedure. |
| PROCEDURE_OWNER | VARCHAR | Name of the role that owns the stored procedure. |
| ARGUMENT_SIGNATURE | VARCHAR | Type signature of the stored procedure’s arguments. |
| DATA_TYPE | VARCHAR | Return value data type. |
| CHARACTER_MAXIMUM_LENGTH | NUMBER | Maximum length in characters of string return value. |
| CHARACTER_OCTET_LENGTH | NUMBER | Maximum length in bytes of string return value. |
| NUMERIC_PRECISION | NUMBER | Numeric precision of numeric return value. |
| NUMERIC_PRECISION_RADIX | NUMBER | Radix of precision of numeric return value. |
| NUMERIC_SCALE | NUMBER | Scale of numeric return value. |
| PROCEDURE_LANGUAGE | VARCHAR | Language of the stored procedure. |
| PROCEDURE_DEFINITION | VARCHAR | Stored procedure definition. |
| CREATED | TIMESTAMP_LTZ | Creation time of the stored procedure. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| COMMENT | VARCHAR | Comment for this stored procedure. |
| DELETED | TIMESTAMP_LTZ | Date and time when the procedure was dropped. |
| RUNTIME_VERSION | VARCHAR | Runtime version of the language used by the procedure. |
| PACKAGES | VARCHAR | Packages requested by the procedure. |
| INSTALLED_PACKAGES | VARCHAR | All packages installed by the function. Output for Python procedures only. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| PROCEDURE_SCHEMA_ID | NUMBER | Internal/system-generated identifier of the schema to which the stored procedure belongs. |
| PROCEDURE_CATALOG_ID | NUMBER | Internal/system-generated identifier of the database to which the stored procedure belongs. |
| SECRETS | JSON map | Map of [secrets](../sql/create-secret.md) specified by the function’s SECRETS parameter, where map keys are secret variable names and map values are secret object names. |
| EXTERNAL_ACCESS_INTEGRATIONS | VARCHAR | Names of [external access integrations](../../developer-guide/external-network-access/external-network-access-overview.md) specified by the function’s EXTERNAL_ACCESS_INTEGRATION parameter. |

## Usage notes

* The view only displays objects for which the current role for the session has been granted access privileges.
* The view does not honor the MANAGE GRANTS privilege and consequently may show less information compared to a SHOW command when both are
  executed by a user who holds the MANAGE GRANTS privilege.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.
