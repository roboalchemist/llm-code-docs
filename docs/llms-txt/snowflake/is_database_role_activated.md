# Source: https://docs.snowflake.com/en/sql-reference/functions/is_database_role_activated.md

Categories:
:   [Context functions](../functions-context.md) (General)

# IS_DATABASE_ROLE_ACTIVATED (SYS_CONTEXT function)

Returns the VARCHAR value `'TRUE'` if a database role is activated in the current session.

See also:
:   [SYS_CONTEXT (SNOWFLAKE$SESSION namespace)](sys_context_snowflake_session.md)
    [IS_ROLE_ACTIVATED (SYS_CONTEXT function)](is_role_activated.md)

## Syntax

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$SESSION' ,
  'IS_DATABASE_ROLE_ACTIVATED' ,
  '<database_role>'
)
```

## Arguments

`'SNOWFLAKE$SESSION'`
:   Specifies that you want to call a function to return context information about the current session.

`'IS_DATABASE_ROLE_ACTIVATED'`
:   Calls the IS_DATABASE_ROLE_ACTIVATED function.

`'database_role'`
:   Specifies the database role to check. The name can be fully qualified or relative.

## Returns

The function returns one of the following VARCHAR values:

* `'TRUE'` if the current user’s active primary role or secondary roles in the session inherits the privileges of the specified database
  role.
* `'FALSE'` if the specified database role isn’t in the user’s active role hierarchy, or if the database role doesn’t exist.

To compare this return value against the BOOLEAN value TRUE or FALSE, [cast](../data-type-conversion.md) the return
value to BOOLEAN. For example:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$SESSION', 'IS_DATABASE_ROLE_ACTIVATED', 'my_db_role')::BOOLEAN = TRUE;
```

## Usage notes

* This function isn’t supported in governance policies (such as masking policies, row access policies, or projection policies)
  applied to shared tables. Shared objects can’t access consumer session state.
* If you don’t specify a fully qualified name, the function resolves the database context of the database role as follows:

  * **Queries:** Session database (the database currently in use).
  * **Body of a data protection policy:** Database containing the protected table or view.
  * **Sharing:** Database in the consumer account.
* This function can’t be used in materialized view definitions because the function isn’t deterministic.

## Examples

Check a database role in the current database using a relative name:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$SESSION', 'IS_DATABASE_ROLE_ACTIVATED', 'ANALYST_ROLE');
```

```output
+-------------------------------------------------------------------------+
| SYS_CONTEXT('SNOWFLAKE$SESSION', 'IS_DATABASE_ROLE_ACTIVATED', 'ANA...  |
+-------------------------------------------------------------------------+
| TRUE                                                                    |
+-------------------------------------------------------------------------+
```

Check a database role in a different database using a fully qualified name:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$SESSION', 'IS_DATABASE_ROLE_ACTIVATED', 'DB2.READER_ROLE');
```

```output
+-------------------------------------------------------------------------+
| SYS_CONTEXT('SNOWFLAKE$SESSION', 'IS_DATABASE_ROLE_ACTIVATED', 'DB ...  |
+-------------------------------------------------------------------------+
| TRUE                                                                    |
+-------------------------------------------------------------------------+
```
