# Source: https://docs.snowflake.com/en/developer-guide/udf-stored-procedure-arguments.md

# Defining arguments for UDFs and stored procedures

In the [CREATE FUNCTION](../sql-reference/sql/create-function.md) or [CREATE PROCEDURE](../sql-reference/sql/create-procedure.md) that you execute to define a
function or procedure, you specify arguments that can be passed in. For example:

```sqlexample
CREATE FUNCTION my_function(integer_argument INT, varchar_argument VARCHAR)
  ...
```

```sqlexample
CREATE PROCEDURE my_procedure(boolean_argument BOOLEAN, date_argument DATE)
  ...
```

When you call a function or procedure, the argument values are bound to the handler’s arguments. They may be bound based on
matching names or by argument position, depending on the language you’re using for the handler.

This topic provides guidelines on specifying the arguments for a function or procedure.

## Limits on the number of input arguments

Scalar functions (UDFs) have a limit of 500 input arguments.

## Specify the data types for the arguments

Choose the SQL data type that corresponds to the data type of the argument that you are using in the handler code.

For information about how Snowflake maps SQL data types to handler data types, see
[Data Type Mappings Between SQL and Handler Languages](udf-stored-procedure-data-type-mapping.md).

## Omit the `Session` argument for Java, Python, and Scala procedures

In the [CREATE PROCEDURE](../sql-reference/sql/create-procedure.md) statement for a procedure written in Java, Python, or Scala, do not define the
argument for the Snowpark `Session` object.

For example, suppose that your handler code passes in a `Session` object and a `String` object:

```java
public String queryTable(Session session, String tableName) { ... }
```

In the CREATE PROCEDURE statement, do not define an argument for the `Session` object. Instead, just define an argument
for the input string:

```sqlexample
CREATE OR REPLACE PROCEDURE query_table(table_name VARCHAR)
  ...
```

`Session` is an implicit argument that you do not specify when calling the procedure. At runtime, when you call your stored
procedure, Snowflake creates a `Session` object and passes it to your stored procedure.

## Specify optional arguments

You can specify that an argument is optional. For details, see the next sections:

* Designating an argument as optional
* Overloading functions and procedures with optional arguments
* Calling functions and procedures that have optional arguments

### Designating an argument as optional

If you want an argument to be optional, use the DEFAULT keyword to specify the default value for the argument.
For example:

```sqlexample
CREATE OR REPLACE FUNCTION build_string_udf(
    word VARCHAR,
    prefix VARCHAR DEFAULT 'pre-',
    suffix VARCHAR DEFAULT '-post'
  )
  ...
```

```sqlexample
CREATE OR REPLACE PROCEDURE build_string_proc(
    word VARCHAR,
    prefix VARCHAR DEFAULT 'pre-',
    suffix VARCHAR DEFAULT '-post'
  )
  ...
```

For the default value of the argument, you can use an expression. For example:

```sqlexample
CREATE OR REPLACE FUNCTION my_date_udf(optional_date_arg DATE DEFAULT CURRENT_DATE())
  ...
```

You must specify optional arguments after the required arguments (if any). You cannot
specify an optional argument before a required argument.

```sqlexample
-- This is not allowed.
CREATE FUNCTION wrong_order(optional_argument INTEGER DEFAULT 0, required_argument INTEGER)
  ...
```

### Overloading functions and procedures with optional arguments

If you are [overloading](udf-stored-procedure-naming-conventions.md) a function or procedure, you cannot use an optional
argument to distinguish between different signatures. For example, suppose that you create the following UDF that passes in
no arguments:

```sqlexample
CREATE FUNCTION my_udf_a()
  ...
```

If you attempt to create a UDF with the same name that passes in an optional argument, the CREATE FUNCTION statement fails:

```sqlexample
CREATE FUNCTION my_udf_a(optional_arg INTEGER DEFAULT 0)
  ...
```

```output
000949 (42723): SQL compilation error:
  Cannot overload FUNCTION 'MY_UDF_A' as it would cause ambiguous FUNCTION overloading.
```

As another example, suppose that you create a UDF that passes in a required INTEGER argument:

```sqlexample
CREATE FUNCTION my_udf_b(required_arg INTEGER)
  ...
```

If you attempt to create a UDF with the same name that passes in a required INTEGER argument and an optional argument, the CREATE
FUNCTION statement fails:

```sqlexample
CREATE FUNCTION my_udf_b(required_arg INTEGER, optional_arg INTEGER DEFAULT 0)
  ...
```

```output
000949 (42723): SQL compilation error:
  Cannot overload FUNCTION 'MY_UDF_B' as it would cause ambiguous FUNCTION overloading.
```

This also affects cases in which you use [ALTER FUNCTION … RENAME](../sql-reference/sql/alter-function.md) or
[ALTER PROCEDURE … RENAME](../sql-reference/sql/alter-procedure.md) to rename a function or procedure. If you want to rename a
function or procedure, there cannot be an existing function with the same name and signature. Optional arguments do not
distinguish one signature from another.

For example, suppose that you create a UDF named `abc_udf` that passes in a required INTEGER argument:

```sqlexample
CREATE FUNCTION abc_udf(required_arg INTEGER)
  ...
```

Suppose that you create a UDF with a different name (`def_udf`) that passes in a required INTEGER argument and an optional
argument:

```sqlexample
CREATE FUNCTION def_udf(required_arg INTEGER, optional_arg INTEGER DEFAULT 0)
  ...
```

If you attempt to change the name of `def_udf` to `abc_udf`, an error occurs because there is already a UDF that has the
same name and the same types of required arguments:

```output
000949 (42723): SQL compilation error:
  Cannot overload FUNCTION 'ABC_UDF' as it would cause ambiguous FUNCTION overloading.
```

### Calling functions and procedures that have optional arguments

To call functions and procedures that have optional arguments, see:

* [Calling a UDF that has optional arguments](udf/udf-calling-sql.md)
* [Specifying optional arguments](stored-procedure/stored-procedures-calling.md)
