# Source: https://docs.snowflake.com/en/sql-reference/sql/create-or-alter.md

# CREATE OR ALTER *<object>*

CREATE OR ALTER commands are DDL commands that combine the functionality of the CREATE command and the ALTER command, enabling you to define
an object using the syntax supported by the CREATE <object> command with the limitations of the ALTER <object> command.

The commands maintain data and associations, meaning that data and other states, tag associations and attached policies, and privilege grants
on the object are preserved. However, some object transformations can result
in dropped data. For example, if a CREATE OR ALTER TABLE statement results in a dropped column, any data contained in the column is lost (but
can still be recovered with Time Travel).

CREATE OR ALTER commands enable you to apply incremental updates to objects using a declarative, idempotent method. When executed, a CREATE OR
ALTER statement results in one of these outcomes:

* If the object doesn’t exist, it’s created according to the definition.
* If the object exists, it’s altered into the object defined in the statement.
* If the object already matches the definition, it remains unchanged.

See also:
:   [CREATE <object>](create.md) , [ALTER <object>](alter.md)

## CREATE OR ALTER commands

For specific syntax, usage notes, and examples, see:

**Account Objects:**

> * [CREATE OR ALTER AUTHENTICATION POLICY](create-authentication-policy.md)
> * [CREATE OR ALTER DATABASE](create-database.md)
> * [CREATE OR ALTER ROLE](create-role.md)
> * [CREATE OR ALTER WAREHOUSE](create-warehouse.md)

**Database Objects:**

> * [CREATE OR ALTER APPLICATION ROLE](create-application-role.md)
> * [CREATE OR ALTER DATABASE ROLE](create-database-role.md)
> * [CREATE OR ALTER DATA METRIC FUNCTION](create-data-metric-function.md)
> * [CREATE OR ALTER DYNAMIC TABLE](create-dynamic-table.md)
> * [CREATE OR ALTER EXTERNAL FUNCTION](create-external-function.md)
> * [CREATE OR ALTER FILE FORMAT](create-file-format.md)
> * [CREATE OR ALTER FUNCTION](create-function.md)
> * [CREATE OR ALTER FUNCTION (Snowpark Container Services)](create-function-spcs.md)
> * [CREATE OR ALTER PROCEDURE](create-procedure.md)
> * [CREATE OR ALTER SCHEMA](create-schema.md)
> * [CREATE OR ALTER STAGE](create-stage.md)
> * [CREATE OR ALTER TABLE](create-table.md)
> * [CREATE OR ALTER TASK](create-task.md)
> * [CREATE OR ALTER VIEW](create-view.md)
> * [CREATE OR ALTER TAG](create-tag.md)

## General usage notes

* **Data governance**: The CREATE OR ALTER commands don’t support data governance changes. Existing tags or policies are unaffected by CREATE
  OR ALTER statements and remain unchanged.
* **Unsetting object properties and parameters**: If a previously set property or parameter is absent in the modified object definition, it
  unsets it.

  If you unset an explicit [parameter](../parameters.md) value, the parameter is reset to the default value. If the parameter
  is set on an object that contains the target object, the target object inherits the value set on the object that contains it. Otherwise,
  the parameter value for the object is reset to the default value.

  Unlike other properies, the CHANGE_TRACKING property will not be unset if not specified in a CREATE OR ALTER command.
* **Atomicity**: The CREATE OR ALTER TABLE command currently does not guarantee atomicity. This means that if a CREATE OR ALTER TABLE
  statement fails during execution, it is possible that a subset of changes might have been applied to the table. If there is a possibility
  of partial changes, the error message, in most cases, includes the following text:

  ```output
  CREATE OR ALTER execution failed. Partial updates may have been applied.
  ```

  For example, if the statement is attempting to drop column `A` and add a new column `B` to a table, and the
  statement is aborted, it is possible that column `A` was dropped but column `B` was not added.

  > **Note:**
  >
  > If changes are partially applied, the resulting table is still in a valid state, and you can use additional ALTER TABLE
  > statements to complete the original set of changes.

  To recover from partial updates, Snowflake recommends the following recovery mechanisms:

  * Fix forward

    * Re-execute the CREATE OR ALTER TABLE statement. If the statements succeeds on the second attempt, the target
      state is achieved.
    * Investigate the error message. If possible, fix the error and re-execute the CREATE OR ALTER TABLE statement.
  * Roll back

    If it is not possible to fix forward, Snowflake recommends manually rolling back partial changes:

    * Investigate the state of the table using the [DESCRIBE TABLE](desc-table.md) and [SHOW TABLES](show-tables.md) commands. Determine which partial
      changes were applied, if any.
    * If any partial changes were applied, execute the appropriate ALTER TABLE statements to transform the table back to its
      original state.

      > **Note:**
      >
      > In some cases, you might not be able to undo partial changes. For more information, see the supported and unsupported
      > actions for modifying column properties in the [ALTER TABLE … ALTER COLUMN](alter-table-column.md) topic.
  * If you need help recovering from a partial update, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

## Limitations

The specific limitations of the CREATE OR ALTER <object> command depend on the object. Some examples of limitations are as follows:

* CREATE OR ALTER TABLE commands don’t support search optimization because search optimization is not part of the CREATE TABLE syntax.
* You can’t change the data type of a column in a table to an incompatible data type.
* You can’t change the definition of an existing view.
* You must suspend a task before you can alter it.
* The variant syntax for creating objects (for example, CREATE OR ALTER TABLE … AS SELECT) is currently not supported.

For the limitations for a specific object, see the reference topic for the object.

## Example use case

If you have SQL scripts that set up Snowflake objects for an application, you can use CREATE OR ALTER <object> statements in your scripts to
make it easier to deploy changes across development, testing, and production environments. As the application evolves, you can make
modifications to the script.

By using a CREATE OR ALTER <object> statement, you can run the script in a new environment, while also re-running the script in an existing
environment. This lets you write the object definition that you want once, and then apply it across environments.
