# Source: https://docs.snowflake.com/en/release-notes/2024/other/2024-11-12-create-or-alter-pupr.md

# November 12, 2024 — Additional CREATE OR ALTER commands — *Preview*

With this release, we are pleased to announce the preview of additional CREATE OR ALTER commands. These
commands combine the functionality of the CREATE command and the ALTER command. A CREATE OR ALTER statement
executes as a CREATE statement if the object doesn’t exist. If it does exist, it transforms the object
according to the object definition in the statement.

CREATE OR ALTER TABLE provides a declarative and idempotent approach to defining your Snowflake objects. When
used together with the Git integration, this enables an Infrastructure-as-Code (IaC) approach to database
change management.

With this preview, the following additional objects are supported:

* [CREATE OR ALTER APPLICATION ROLE](../../../sql-reference/sql/create-application-role.md): Creates an application role if it doesn’t exist or alters an existing
  application role.
* [CREATE OR ALTER DATABASE](../../../sql-reference/sql/create-database.md): Creates a database if it doesn’t exist or alters an existing
  database.
* [CREATE OR ALTER DATABASE ROLE](../../../sql-reference/sql/create-database-role.md): Creates a database role if it doesn’t exist or alters an existing
  database role.
* [CREATE OR ALTER ROLE](../../../sql-reference/sql/create-role.md): Creates a role if it doesn’t exist or alters an existing role.
* [CREATE OR ALTER SCHEMA](../../../sql-reference/sql/create-schema.md): Creates a schema if it doesn’t exist or alters an existing
  schema.
* [CREATE OR ALTER STAGE](../../../sql-reference/sql/create-stage.md): Creates a stage if it doesn’t exist or alters an existing stage.
* [CREATE OR ALTER VIEW](../../../sql-reference/sql/create-view.md): Creates a view if it doesn’t exist or alters an existing view.
* [CREATE OR ALTER WAREHOUSE](../../../sql-reference/sql/create-warehouse.md): Creates a warehouse if it doesn’t exist or alters an existing warehouse.

For more information, see [CREATE OR ALTER <object>](../../../sql-reference/sql/create-or-alter.md).
