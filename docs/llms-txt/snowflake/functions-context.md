# Source: https://docs.snowflake.com/en/sql-reference/functions-context.md

# Context functions

This family of functions allows for the gathering of information about the context in which the statement is executed. These functions are evaluated
at most once per statement.

## List of functions

| Sub-category | Function | Notes |
| --- | --- | --- |
| General context | [CURRENT_CLIENT](functions/current_client.md) |  |
|  | [CURRENT_DATE](functions/current_date.md) |  |
|  | [CURRENT_IP_ADDRESS](functions/current_ip_address.md) |  |
|  | [CURRENT_REGION](functions/current_region.md) |  |
|  | [CURRENT_TIME](functions/current_time.md) |  |
|  | [CURRENT_TIMESTAMP](functions/current_timestamp.md) |  |
|  | [CURRENT_VERSION](functions/current_version.md) |  |
|  | [GETDATE](functions/getdate.md) | Alias for CURRENT_TIMESTAMP. |
|  | [LOCALTIME](functions/localtime.md) | Alias for CURRENT_TIME. |
|  | [LOCALTIMESTAMP](functions/localtimestamp.md) | Alias for CURRENT_TIMESTAMP. |
|  | [SYSDATE](functions/sysdate.md) |  |
|  | [SYSTIMESTAMP](functions/systimestamp.md) |  |
|  | [SYS_CONTEXT](functions/sys_context.md) |  |
| Session context | [ALL_USER_NAMES](functions/all_user_names.md) |  |
|  | [CURRENT_ACCOUNT](functions/current_account.md) | Returns account locator. |
|  | [CURRENT_ACCOUNT_NAME](functions/current_account_name.md) | Returns account name. |
|  | [CURRENT_ORGANIZATION_NAME](functions/current_organization_name.md) |  |
|  | [CURRENT_ORGANIZATION_USER](functions/current_organization_user.md) |  |
|  | [CURRENT_ROLE](functions/current_role.md) |  |
|  | [CURRENT_AVAILABLE_ROLES](functions/current_available_roles.md) |  |
|  | [CURRENT_SECONDARY_ROLES](functions/current_secondary_roles.md) |  |
|  | [CURRENT_SESSION](functions/current_session.md) |  |
|  | [CURRENT_STATEMENT](functions/current_statement.md) |  |
|  | [CURRENT_TRANSACTION](functions/current_transaction.md) |  |
|  | [CURRENT_USER](functions/current_user.md) |  |
|  | [GETVARIABLE](functions/getvariable.md) |  |
|  | [LAST_QUERY_ID](functions/last_query_id.md) |  |
|  | [LAST_TRANSACTION](functions/last_transaction.md) |  |
| Session object context | [CURRENT_DATABASE](functions/current_database.md) |  |
|  | [CURRENT_ROLE_TYPE](functions/current_role_type.md) |  |
|  | [CURRENT_SCHEMA](functions/current_schema.md) |  |
|  | [CURRENT_SCHEMAS](functions/current_schemas.md) |  |
|  | [CURRENT_WAREHOUSE](functions/current_warehouse.md) |  |
|  | [INVOKER_ROLE](functions/invoker_role.md) |  |
|  | [INVOKER_SHARE](functions/invoker_share.md) |  |
|  | [IS_APPLICATION_ROLE_ACTIVATED (SYS_CONTEXT function)](functions/is_application_role_activated.md) |  |
|  | [IS_APPLICATION_ROLE_IN_SESSION](functions/is_application_role_in_session.md) |  |
|  | [IS_DATABASE_ROLE_IN_SESSION](functions/is_database_role_in_session.md) |  |
|  | [IS_GRANTED_TO_INVOKER_ROLE](functions/is_granted_to_invoker_role.md) |  |
|  | [IS_INSTANCE_ROLE_IN_SESSION](functions/is_instance_role_in_session.md) |  |
|  | [IS_ROLE_ACTIVATED (SYS_CONTEXT function)](functions/is_role_activated.md) |  |
|  | [IS_ROLE_IN_SESSION](functions/is_role_in_session.md) |  |
|  | [POLICY_CONTEXT](functions/policy_context.md) |  |
| Alert context | [GET_CONDITION_QUERY_UUID](functions/get_condition_query_uuid.md) |  |
| Organization context | [IS_GROUP_ACTIVATED (SYS_CONTEXT function)](functions/is_group_activated.md) |  |
|  | [IS_GROUP_IMPORTED (SYS_CONTEXT function)](functions/is_group_imported.md) |  |
|  | [IS_USER_IMPORTED (SYS_CONTEXT function)](functions/is_user_imported.md) |  |

## Usage notes

* Context functions generally do not require arguments (except for [SYS_CONTEXT](functions/sys_context.md)).
* To comply with the ANSI standard, the following context functions can be called without parentheses
  in SQL statements:

  * CURRENT_DATE
  * CURRENT_TIME
  * CURRENT_TIMESTAMP
  * CURRENT_USER
  * LOCALTIME
  * LOCALTIMESTAMP
  > **Note:**
  >
  > If you are setting a [Snowflake Scripting variable](../developer-guide/snowflake-scripting/variables.md)
  > to an expression that calls one of these functions (for example, `my_var := <function_name>();`),
  > you must include the parentheses.

## Examples

Display the current warehouse, database, and schema for the session:

```sqlexample
SELECT CURRENT_WAREHOUSE(), CURRENT_DATABASE(), CURRENT_SCHEMA();
```

```output
+---------------------+--------------------+------------------+
| CURRENT_WAREHOUSE() | CURRENT_DATABASE() | CURRENT_SCHEMA() |
|---------------------+--------------------+------------------+
| MY_WAREHOUSE        | MY_DB              | PUBLIC           |
|---------------------+--------------------+------------------+
```

Display the current date, time, and timestamp (note that parentheses are not required to call these functions):

```sqlexample
SELECT CURRENT_DATE, CURRENT_TIME, CURRENT_TIMESTAMP;
```

```output
+--------------+--------------+-------------------------------+
| CURRENT_DATE | CURRENT_TIME | CURRENT_TIMESTAMP             |
|--------------+--------------+-------------------------------|
| 2024-06-07   | 10:45:15     | 2024-06-07 10:45:15.064 -0700 |
+--------------+--------------+-------------------------------+
```

In a Snowflake Scripting block, call the CURRENT_DATE function without parentheses to set a variable in a
SQL statement:

```sqlexample
EXECUTE IMMEDIATE
$$
DECLARE
  currdate DATE;
BEGIN
  SELECT CURRENT_DATE INTO currdate;
  RETURN currdate;
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
| 2024-06-07      |
+-----------------+
```

In a Snowflake Scripting block, attempting to set a variable to an expression that calls the CURRENT_DATE
function without parentheses results in an error:

```sqlexample
EXECUTE IMMEDIATE
$$
DECLARE
  today DATE;
BEGIN
  today := CURRENT_DATE;
  RETURN today;
END;
$$
;
```

```output
000904 (42000): SQL compilation error: error line 5 at position 11
invalid identifier 'CURRENT_DATE'
```

The same block returns the current date when the function is called with the parentheses:

```sqlexample
EXECUTE IMMEDIATE
$$
DECLARE
  today DATE;
BEGIN
  today := CURRENT_DATE();
  RETURN today;
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
| 2024-06-07      |
+-----------------+
```
