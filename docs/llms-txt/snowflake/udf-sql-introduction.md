# Source: https://docs.snowflake.com/en/developer-guide/udf/sql/udf-sql-introduction.md

# Introduction to SQL UDFs

You can write the handler for a user-defined function (UDF) in SQL. Topics in this section describe how to design and write a SQL
handler. You’ll also find examples.

For an introduction to UDFs, including a list of languages in which you can write a UDF handler, see [User-defined functions overview](../udf-overview.md).

After you have a handler, you create the UDF with SQL. For information about using SQL to create or call a UDF, see
[Creating a user-defined function](../udf-creating-sql.md) or [Executing a UDF](../udf-calling-sql.md).

> **Note:**
>
> For limitations related to SQL UDF handlers, see [SQL UDF limitations](udf-sql-limitations.md).

## How a SQL handler works

When a user calls a UDF, the user passes UDF’s name and arguments to Snowflake. Snowflake calls the associated handler code
(with arguments, if any) to execute the UDF’s logic. The handler method then returns the output to Snowflake, which passes it back to the
client.

The function definition can be a SQL expression that returns either a scalar — that is, single — value or, if defined as a
table function, a set of rows.

### Example

Code in the following example creates a UDF called `area_of_circle` containing handler code that calculates a circle’s area from
the radius value received by the UDF as an argument.

```sqlexample
CREATE FUNCTION area_of_circle(radius FLOAT)
  RETURNS FLOAT
  AS
  $$
    pi() * radius * radius
  $$
  ;
```

## General usage

A SQL UDF evaluates an arbitrary SQL expression and returns the results of the expression.

The function definition can be a SQL expression that returns either a scalar — that is, single — value or,
if defined as a table function, a set of rows.

## Security/privilege requirements for SQL UDFs

If a function definition refers to an unqualified table, then that table is resolved in the schema containing the function. A reference
to another schema object — such as a table, view, or other function — requires that the owner of the function has privileges to access that
schema object. The invoker of the function need not have access to the objects referenced in the function definition, but only needs the
privilege to use the function.

For example, an administrator owns a table named `users`, which contains sensitive data that is not generally accessible, but the
administrator can expose the total user count through a function which other users have access privileges on:

```sqlexample
USE ROLE dataadmin;

DESC TABLE users;
```

```output
+-----------+--------------+--------+-------+---------+-------------+------------+--------+------------+---------+
| name      | type         | kind   | null? | default | primary key | unique key | check  | expression | comment |
|-----------+--------------+--------+-------+---------+-------------+------------+--------+------------+---------|
| USER_ID   | NUMBER(38,0) | COLUMN | Y     | [NULL]  | N           | N          | [NULL] | [NULL]     | [NULL]  |
| USER_NAME | VARCHAR(100) | COLUMN | Y     | [NULL]  | N           | N          | [NULL] | [NULL]     | [NULL]  |
  ...
  ...
  ...
+-----------+--------------+--------+-------+---------+-------------+------------+--------+------------+---------+
```

```sqlexample
CREATE FUNCTION total_user_count() RETURNS NUMBER AS 'select count(*) from users';

GRANT USAGE ON FUNCTION total_user_count() TO ROLE analyst;

USE ROLE analyst;

-- This will fail because the role named "analyst" does not have the
-- privileges required in order to access the table named "users".
SELECT * FROM users;
```

```output
FAILURE: SQL compilation error:
Object 'USERS' does not exist.
```

```sqlexample
-- However, this will succeed.
SELECT total_user_count();
```

```output
+--------------------+
| TOTAL_USER_COUNT() |
|--------------------+
| 123                |
+--------------------+
```

For more information about using roles and privileges to manage access control, see [Overview of Access Control](../../../user-guide/security-access-control-overview.md).
