# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/stages.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/stages.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/stages.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# STAGES view

This Account Usage view displays a row for each stage defined in the account.

Stages are named objects that can be used for loading/unloading data. For more information, see [CREATE STAGE](../sql/create-stage.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| STAGE_ID | NUMBER | Internal/system-generated identifier for the stage. |
| STAGE_NAME | VARCHAR | Name of the stage. |
| STAGE_SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema of the stage. |
| STAGE_SCHEMA | VARCHAR | Schema that the stage belongs to. |
| STAGE_CATALOG_ID | NUMBER | Internal/system-generated identifier for the database of the stage. |
| STAGE_CATALOG | VARCHAR | Database that the stage belongs to. |
| STAGE_URL | VARCHAR | If the stage is external, location of the stage; NULL if it is internal. |
| STAGE_REGION | VARCHAR | If the stage is external, region where the stage resides; NULL if it is internal. |
| STAGE_TYPE | VARCHAR | Type of stage (`Internal Named`, or `External Named`). |
| STAGE_OWNER | VARCHAR | Name of the role that owns the stage; NULL if it has been dropped. |
| COMMENT | VARCHAR | Comment for the stage. |
| CREATED | TIMESTAMP_LTZ | Date and time when the stage was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| DELETED | TIMESTAMP_LTZ | Date and time when the stage was dropped. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| INSTANCE_ID | NUMBER | Internal/system-generated identifier for the instance which the object belongs to. |
| STORAGE_INTEGRATION | VARCHAR | The name of the storage integration associated with the stage; NULL for internal stages or stages that do not use a storage integration. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The view only displays objects for which the current role for the session has been granted access privileges.
* The view does not recognize the MANAGE GRANTS privilege and consequently may show less information compared to a SHOW command
  executed by a user who holds the MANAGE GRANTS privilege.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.
