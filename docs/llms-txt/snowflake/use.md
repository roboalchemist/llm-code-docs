# Source: https://docs.snowflake.com/en/sql-reference/sql/use.md

# USE *<object>*

Specifies the role, warehouse, database, or schema to use for the current session.

## USE commands

For specific syntax, usage notes, and examples, see:

* [USE ROLE](use-role.md)
* [USE SECONDARY ROLES](use-secondary-roles.md)
* [USE WAREHOUSE](use-warehouse.md)
* [USE DATABASE](use-database.md)
* [USE SCHEMA](use-schema.md)

## Viewing the current session context

To view the current role, secondary roles, database, schema, and warehouse for the session, use the corresponding context functions.
For example:

```sqlexample
SELECT CURRENT_ROLE(),
       CURRENT_SECONDARY_ROLES(),
       CURRENT_WAREHOUSE(),
       CURRENT_DATABASE(),
       CURRENT_SCHEMA();
```

```output
+----------------+--------------------------+---------------------+--------------------+------------------+
| CURRENT_ROLE() | CURRENT_SECONDARY_ROLES  | CURRENT_WAREHOUSE() | CURRENT_DATABASE() | CURRENT_SCHEMA() |
|----------------+--------------------------+---------------------+--------------------+------------------|
| SYSADMIN       | ALL                      | MYWH                | MYTESTDB           | PUBLIC           |
+----------------+--------------------------+---------------------+--------------------+------------------+
```

For more details, see [Context functions](../functions-context.md).
