# Source: https://docs.snowflake.com/en/sql-reference/name-resolution.md

# Object name resolution

A fully-qualified schema object (table, view, file format etc.) has the form:

> `<database_name>.<schema_name>.<object_name>`

However, because this can be tedious to write, the user is allowed to omit qualifications, from left to right. This topic describes how schema object names are resolved.

## Resolution when database omitted

> `(''<schema_name>.<object_name>'')`

The object name is augmented with the current database. The current database is set to a default value, depending on the account’s settings, when a session is initiated. Afterwards, it can be changed using the
[USE DATABASE](sql/use-database.md) command. The [CREATE DATABASE](sql/create-database.md) command also implicitly changes the current database to the newly created one. The name of the current database is returned by the
[CURRENT_DATABASE](functions/current_database.md) function.

For example:

```sqlexample
SELECT CURRENT_DATABASE();
```

```output
+--------------------+
| CURRENT_DATABASE() |
+--------------------+
| TESTDB             |
+--------------------+
```

```sqlexample
CREATE DATABASE db1;
```

```output
+------------------------------------+
|               status               |
+------------------------------------+
| Database DB1 successfully created. |
+------------------------------------+
```

```sqlexample
SELECT CURRENT_DATABASE();
```

```output
+--------------------+
| CURRENT_DATABASE() |
+--------------------+
| DB1                |
+--------------------+
```

```sqlexample
USE DATABASE testdb;
```

```output
+----------------------------------+
|              status              |
+----------------------------------+
| Statement executed successfully. |
+----------------------------------+
```

```sqlexample
SELECT CURRENT_DATABASE();
```

```output
+--------------------+
| CURRENT_DATABASE() |
+--------------------+
| TESTDB             |
+--------------------+
```

## Resolution when schema omitted (double-dot notation)

> `(''<database_name>..<object_name>'')`

The two dots indicate that the schema name is not specified. The PUBLIC default schema is always referenced.

Note that this notational format is provided mostly for compatibility with other systems, such as Microsoft SQL Server and IBM Netezza. Using this notation in new queries is discouraged.

## Unqualified objects

Unqualified objects (single identifiers) are resolved in two different ways, depending on whether they appear in a DDL or DML statement or in a query.

### DDL and DML statements

In DDL and DML statements, unqualified objects are augmented with the current database and schema. The current schema is maintained similarly to the current database. The current schema always belongs to the current database.

When a session is initiated, the current schema is initialized based on the connection’s settings. When the current database is changed, the current schema defaults to the value of an internal property (normally set to PUBLIC).
The current schema can be changed (always within the current database) by using the [USE SCHEMA](sql/use-schema.md) command. It is also implicitly changed by the [CREATE SCHEMA](sql/create-schema.md) command. The name of the
current schema is returned by the [CURRENT_SCHEMA](functions/current_schema.md) function.

For example:

```sqlexample
SELECT CURRENT_SCHEMA();
```

```output
+------------------+
| CURRENT_SCHEMA() |
+------------------+
| TESTSCHEMA       |
+------------------+
```

```sqlexample
CREATE DATABASE db1;
```

```output
+------------------------------------+
|               status               |
+------------------------------------+
| Database DB1 successfully created. |
+------------------------------------+
```

```sqlexample
SELECT CURRENT_SCHEMA();
```

```output
+------------------+
| CURRENT_SCHEMA() |
+------------------+
| PUBLIC           |
+------------------+
```

```sqlexample
CREATE SCHEMA sch1;
```

```output
+-----------------------------------+
|              status               |
+-----------------------------------+
| Schema SCH1 successfully created. |
+-----------------------------------+
```

```sqlexample
SELECT current_schema();
```

```output
+------------------+
| CURRENT_SCHEMA() |
|------------------+
| SCH1             |
|------------------+
```

### Name resolution in queries

In queries, unqualified object names are resolved through a search path.

The search path usually contains the current schema, but can also contain other schemas.

The search path is stored in the session-level parameter SEARCH_PATH. Similar to any other parameter, it can be
changed using the [ALTER SESSION](sql/alter-session.md) command.

The value of the search path is a comma-separated list of identifiers. The list can contain
fully- or partially-qualified schema names. Each schema name can be a [Double-quoted identifiers](identifiers-syntax.md).

The search path can also contain the following pseudo-variables:

> $current
> :   Specifies the current schema (see above).
>
> $public
> :   Specifies the public schema of the current database. The public schema’s name is determined by an
> internal property, maintained by Snowflake, that is typically set to PUBLIC (for the PUBLIC schema
> automatically created for each database).

These pseudo-variable names are case-insensitive.

The default value of the search path is `$current, $public`.

If the user specifies a new value for the search path, the new value will be validated. Every schema identifier specified in the new value must correspond to an existing schema. (In particular, every unqualified schema must
correspond to an existing schema in the current database). Otherwise an error will be raised and search_path will retain its previous value. However, the pseudo-variables can be used freely. For example, *$public* can be used even
if the current database has no public schema.

The value of the SEARCH_PATH parameter is reinterpreted every time it is used. Therefore, changing the current schema changes the meaning of `$current`, and changing the current database changes the meaning of `$public`, as
well as the meaning of any unqualified schemas.

If a schema in the search path is dropped, or if the current database is changed and some unqualified schemas in the search path don’t exist in the new database, no error is raised.

The SEARCH_PATH is not used inside [views](../user-guide/views-introduction.md) or [UDFs](../developer-guide/udf/udf-overview.md).
All unqualified objects in a view or UDF definition will be resolved in the view’s or UDF’s schema only.

The literal value of the search path can be examined through the command [SHOW PARAMETERS](sql/show-parameters.md).

To see the schemas that will be searched for unqualified objects in queries, use the [CURRENT_SCHEMAS](functions/current_schemas.md) function. The return value for the function contains a series of fully-qualified schemas in the
search path, separated by commas.

For example:

```sqlexample
SELECT CURRENT_SCHEMAS();
```

```output
+-------------------+
| CURRENT_SCHEMAS() |
+-------------------+
| []                |
+-------------------+
```

```sqlexample
USE DATABASE mytestdb;

SELECT current_schemas();
```

```output
+---------------------+
| CURRENT_SCHEMAS()   |
+---------------------+
| ["MYTESTDB.PUBLIC"] |
+---------------------+
```

```sqlexample
CREATE SCHEMA private;

SELECT current_schemas();
```

```output
+-----------------------------------------+
| CURRENT_SCHEMAS()                       |
+-----------------------------------------+
| ["MYTESTDB.PRIVATE", "MYTESTDB.PUBLIC"] |
+-----------------------------------------+
```

The pseudo-variables are expanded to their current value, unqualified schemas are fully qualified, and schemas that don’t exist or aren’t visible are omitted.

```sqlexample
SHOW PARAMETERS LIKE 'search_path';
```

```output
+-------------+--------------------+--------------------+------------------------------------------------+
| key         | value              | default            | description                                    |
+-------------+--------------------+--------------------+------------------------------------------------+
| SEARCH_PATH | $current, $public, | $current, $public, | Search path for unqualified object references. |
+-------------+--------------------+--------------------+------------------------------------------------+
```

```sqlexample
SELECT current_schemas();
```

```output
+---------------------------------------------------------------------------+
|                       CURRENT_SCHEMAS()                                   |
+---------------------------------------------------------------------------+
| [XY12345.TESTDB.TESTSCHEMA, XY12345.TESTDB.PUBLIC, SAMPLES.COMMON.PUBLIC] |
+---------------------------------------------------------------------------+
```

```sqlexample
CREATE DATABASE db1;
```

```output
+------------------------------------+
|               status               |
+------------------------------------+
| Database DB1 successfully created. |
+------------------------------------+
```

```sqlexample
USE SCHEMA public;
```

```output
+----------------------------------+
|              status              |
+----------------------------------+
| Statement executed successfully. |
+----------------------------------+
```

```sqlexample
SELECT current_schemas();
```

```output
+---------------------------------------------+
|                CURRENT_SCHEMAS()            |
+---------------------------------------------+
| [XY12345.DB1.PUBLIC, SAMPLES.COMMON.PUBLIC] |
+---------------------------------------------+
```

```sqlexample
ALTER SESSION SET search_path='$current, $public, testdb.public';
```

```output
+----------------------------------+
|              status              |
+----------------------------------+
| Statement executed successfully. |
+----------------------------------+
```

```sqlexample
SHOW PARAMETERS LIKE 'search_path';
```

```output
+-------------+----------------------------------+--------------------+------------------------------------------------+
| key         | value                            | default            | description                                    |
+-------------+----------------------------------+--------------------+------------------------------------------------+
| SEARCH_PATH | $current, $public, testdb.public | $current, $public, | Search path for unqualified object references. |
+-------------+----------------------------------+--------------------+------------------------------------------------+
```

```sqlexample
SELECT current_schemas();
```

```output
+---------------------------------------------+
|                CURRENT_SCHEMAS()            |
+---------------------------------------------+
| [XY12345.DB1.PUBLIC, XY12345.TESTDB.PUBLIC] |
+---------------------------------------------+
```

#### Precedence when a column name and an alias match

It is possible (but usually not recommended) to create a query that contains an alias that matches a column name:

```sqlexample
SELECT x, some_expression AS x
  FROM ...
```

If a clause contains a name that matches both a column name and an alias, then the clause uses the column name. The following example demonstrates this behavior using a GROUP BY clause:

Create a table and insert rows:

```sqlexample
CREATE TABLE employees (salary FLOAT, state VARCHAR, employment_state VARCHAR);
INSERT INTO employees (salary, state, employment_state) VALUES
  (60000, 'California', 'Active'),
  (70000, 'California', 'On leave'),
  (80000, 'Oregon', 'Active');
```

The following query returns the sum of the salaries of the employees who are active and the sum of the salaries of the employees who
are on leave:

```sqlexample
SELECT SUM(salary), ANY_VALUE(employment_state)
  FROM employees
  GROUP BY employment_state;
```

```output
+-------------+-----------------------------+
| SUM(SALARY) | ANY_VALUE(EMPLOYMENT_STATE) |
|-------------+-----------------------------|
|      140000 | Active                      |
|       70000 | On leave                    |
+-------------+-----------------------------+
```

The next query uses the alias `state`, which matches the name of a column of the table in the query. When `state` is used in
the GROUP BY clause, Snowflake interprets it as a reference to the column name, not the alias. This query therefore returns the sum of
the salaries of the employees in the state of California and the sum of the salaries of the employees in the state of Oregon,
yet displays `employment_state` information, such as `Active`, rather than the names of states or provinces:

```sqlexample
SELECT SUM(salary), ANY_VALUE(employment_state) AS state
  FROM employees
  GROUP BY state;
```

```output
+-------------+--------+
| SUM(SALARY) | STATE  |
|-------------+--------|
|      130000 | Active |
|       80000 | Active |
+-------------+--------+
```
