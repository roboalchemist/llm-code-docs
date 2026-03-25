# Source: https://docs.snowflake.com/en/sql-reference/functions/sys_context_snowflake_session.md

Categories:
:   [Context functions](../functions-context.md) (General)

# SYS_CONTEXT (SNOWFLAKE$SESSION namespace)

Returns information about the session in which the function is called.

You can call this function in the following contexts:

* You can call this function directly in the current session.
* You can run a caller’s rights executable (for example, a caller’s rights stored procedure) that calls this function.
* You can run an owner’s rights executable (for example, an owner’s rights stored procedure) that calls this function, provided
  that the owner role has been granted the READ SESSION privilege on the account.

In any other context, the function returns NULL.

See also:
:   [SYS_CONTEXT](sys_context.md) ,
    [SYS_CONTEXT (SNOWFLAKE$APPLICATION namespace)](sys_context_snowflake_application.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ENVIRONMENT namespace)](sys_context_snowflake_environment.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION namespace)](sys_context_snowflake_organization.md)

## Syntax

**Syntax for retrieving properties:**

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$SESSION' ,
  '<property>'
)
```

**Syntax for calling functions:**

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$SESSION' ,
  '<function>' , '<argument>' [ , ... ]
)
```

## Arguments

`'SNOWFLAKE$SESSION'`
:   Specifies that you want to retrieve a property or call a function to return information about the session in which the function
    is called.

`'property'`
:   Name of the property that you want to retrieve. You can specify the following properties:

    | Property | Description |
    | --- | --- |
    | `PRINCIPAL_NAME` | Name of the principal (the user, [task](../../user-guide/tasks-intro.md), or [SPCS service](../../developer-guide/snowpark-container-services/overview.md)) that started the session. The name depends on the value of the `PRINCIPAL_TYPE` property:   * If `PRINCIPAL_TYPE` is one of the following values, the value of the `PRINCIPAL_NAME` property is the name of the   user:    + `USER`   + `USER_PERSON`   + `USER_SERVICE`   + `USER_LEGACY_SERVICE` * If `PRINCIPAL_TYPE` is `TASK`, the value is the name of the task. * If `PRINCIPAL_TYPE` is `SNOWSERVICE`, the value is the name of the SPCS service. |
    | `PRINCIPAL_TYPE` | Type of the principal that started the session. This property can have one of the following values:   * `USER` or `USER_suffix`, if a user started the session. `suffix` depends on the type of the user:    + If the user object has no TYPE property, the value is `USER`.   + If the TYPE property is `PERSON`, the value is `USER_PERSON`.   + If the TYPE property is `SERVICE`, the value is `USER_SERVICE`.   + If the TYPE property is `LEGACY_SERVICE`, the value is `USER_LEGACY_SERVICE`. * `TASK`, if a [task](../../user-guide/tasks-intro.md) started the session. * `SNOWSERVICE`, if an [SPCS service](../../developer-guide/snowpark-container-services/overview.md) started the session. |
    | `PRINCIPAL_EMAIL` | Email address that is associated with the principal. If there is no associated email address, the value of this property is NULL. |
    | `PRINCIPAL_DATABASE` | Name of the database containing the object for the principal. For example, if the principal is a task, the value of this property is the name of the database that contains the task.  If the principal is an account-level object (such as a user), the value of this property is NULL. |
    | `PRINCIPAL_SCHEMA` | Name of the schema containing the object for the principal. For example, if the principal is a task, the value of this property is the name of the schema that contains the task.  If the principal is an account-level object (such as a user), the value of this property is NULL. |
    | `ID` | Identifier for the session in which the function was called. |
    | `ROLE` | Primary role for the session in which the function was called. |
    | `ROLE_TYPE` | Type of the primary role. This property can have one of the following values:   * `ROLE`, if the primary role is an account role. |
    | `ROLE_DATABASE` | Name of the database that contains the database role, if the primary role is a database role. |
    | `SECONDARY_ROLES` | JSON array of the account-level roles activated as secondary roles in the session. The activated roles include roles that are hierarchically under the requested role. For example, suppose that the user executed:  ```sqlexample USE SECONDARY ROLES ACCOUNTADMIN; ```  The JSON array for this property includes the ACCOUNTADMIN role and the SECURITYADMIN, SYSADMIN, and USERADMIN roles, which are under the ACCOUNTADMIN role. |
    | `WANTED_SECONDARY_ROLES` | JSON array of the account-level roles requested by the user. For example, suppose that the user executed:  ```sqlexample USE SECONDARY ROLES ACCOUNTADMIN; ```  The JSON array for this property just includes the ACCOUNTADMIN role. |
    | `DATABASE` | Current database in use for the session, if the role that called the function has privileges to access the database. |
    | `SCHEMA` | Current schema in use for the session, if the role that called the function has privileges to access the schema. |
    | `SCHEMAS` | Current [search path](../name-resolution.md) of schemas for the session, if the role that called the function has privileges to access the current database. |
    | `WAREHOUSE` | Current warehouse in use for the session. |

`'function'`
:   Name of the function that you want to call. You can call the following functions:

    * [IS_DATABASE_ROLE_ACTIVATED (SYS_CONTEXT function)](is_database_role_activated.md)
    * [IS_ROLE_ACTIVATED (SYS_CONTEXT function)](is_role_activated.md)

`'argument' [ , ... ]`
:   Arguments to pass to the function that you want to call.

## Returns

The function returns a VARCHAR value or NULL:

* The return value depends on
  the property that you are retrieving or
  the function that you are calling.
* If you call SYS_CONTEXT with the SNOWFLAKE$SESSION namespace outside of
  any of the supported contexts, the function returns NULL.

## Usage notes

* If you are specifying the function call in a double-quoted string in a shell, escape the `$` character with a backslash
  (`\`) so that `$SESSION` is not interpreted as a shell variable.

  For example, if you are using Snowflake CLI and you are
  [specifying the SQL statement as a command-line argument](../../developer-guide/snowflake-cli/sql/execute-sql.md) in double
  quotes:

  ```bash
  snow sql --query "SELECT SYS_CONTEXT('SNOWFLAKE\$SESSION', 'PRINCIPAL_NAME');"
  ```

## Examples

The following examples demonstrate how to retrieve context information about the session:

* Retrieving information about the principal
* Retrieving information about roles
* Retrieving the current database, schema, search path, and warehouse

### Retrieving information about the principal

The following example returns the name and type of the principal that called the function:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$SESSION', 'PRINCIPAL_NAME') AS name,
  SYS_CONTEXT('SNOWFLAKE$SESSION', 'PRINCIPAL_TYPE') AS type,
  SYS_CONTEXT('SNOWFLAKE$SESSION', 'PRINCIPAL_EMAIL') AS email;
```

```output
+--------------+-------------+---------------------+
| NAME         | TYPE        | EMAIL               |
|--------------+-------------+---------------------|
| MY_USER_NAME | USER_PERSON | my.user@example.com |
+--------------+-------------+---------------------+
```

### Retrieving information about roles

The following example returns the name and type of the primary role in the session where the function was called:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$SESSION', 'ROLE') AS role,
  SYS_CONTEXT('SNOWFLAKE$SESSION', 'ROLE_TYPE') AS type;
```

```output
+---------+------+
| ROLE    | TYPE |
|---------+------|
| MY_ROLE | ROLE |
+---------+------+
```

The following example uses the ACCOUNTADMIN role as a secondary role. The example then returns the list of requested secondary
roles in the session (ACCOUNTADMIN) and the list of account-level roles that are activated as secondary roles in the session.

The list of activated roles includes roles that are hierarchically under the requested role. Because the ACCOUTADMIN role is
activated, the list includes SECURITYADMIN, SYSADMIN, and USERADMIN, which are under the ACCOUNTADMIN role.

```sqlexample
USE SECONDARY ROLES ACCOUNTADMIN;

SELECT SYS_CONTEXT('SNOWFLAKE$SESSION', 'WANTED_SECONDARY_ROLES') AS requested_roles,
  SYS_CONTEXT('SNOWFLAKE$SESSION', 'SECONDARY_ROLES') AS requested_roles_with_child_roles;
```

```output
+------------------+---------------------------------------------------------+
| REQUESTED_ROLES  | REQUESTED_ROLES_WITH_CHILD_ROLES                        |
|------------------+---------------------------------------------------------|
| ["ACCOUNTADMIN"] | ["ACCOUNTADMIN","SECURITYADMIN","SYSADMIN","USERADMIN"] |
+------------------+---------------------------------------------------------+
```

### Retrieving the current database, schema, search path, and warehouse

The following example returns the current database, schema, and warehouse in use for the session:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$SESSION', 'DATABASE') AS database,
  SYS_CONTEXT('SNOWFLAKE$SESSION', 'SCHEMA') AS schema,
  SYS_CONTEXT('SNOWFLAKE$SESSION', 'WAREHOUSE') AS warehouse;
```

```output
+----------+--------+--------------+
| DATABASE | SCHEMA | WAREHOUSE    |
|----------+--------+--------------|
| MY_DB    | PUBLIC | MY_WAREHOUSE |
+----------+--------+--------------+
```

The following example returns a JSON array that contains the search path for the session:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$SESSION', 'SCHEMAS');
```

```output
+---------------------------------------------+
| SYS_CONTEXT('SNOWFLAKE$SESSION', 'SCHEMAS') |
|---------------------------------------------|
| ["MY_DB.MY_SCHEMA","MY_DB.PUBLIC"]          |
+---------------------------------------------+
```

The following example returns a row for each element in the search path:

```sqlexample
SELECT value::VARCHAR AS path_element
  FROM TABLE(
    FLATTEN(INPUT => PARSE_JSON(SYS_CONTEXT('SNOWFLAKE$SESSION', 'SCHEMAS'))));
```

```output
+-----------------------+
| PATH_ELEMENT          |
|-----------------------|
| BOOKS_DB.BOOKS_SCHEMA |
| BOOKS_DB.PUBLIC       |
+-----------------------+
```
