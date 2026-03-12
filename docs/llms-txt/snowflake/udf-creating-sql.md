# Source: https://docs.snowflake.com/en/developer-guide/udf/udf-creating-sql.md

# Creating a user-defined function

You can create a [user-defined function (UDF)](udf-overview.md) using any of several methods available with Snowflake.
These methods are described in this topic.

## Create a UDF

1. Write function logic as a handler using one of several supported languages, including Python, Java, and Scala.
2. Choose a tool or API to create the function with the handler you wrote.

   For more information about each of these, see Tools for creating UDFs.

   |  |  |
   | --- | --- |
   | SQL | Use SQL and write logic in one of several languages. |
   | Snowpark | Use the Snowpark API for Java, Python, or Scala. |
   | Command line | Execute CLI commands to create the function. |
   | Python API | Execute client-side Python commands to create the function. |
   | REST | Make requests to a RESTful API to create the function. |

3. [Execute the function](udf-calling-sql.md) using one of several tools, depending on your needs.

## Tools for creating UDFs

You can create a [UDF](udf-overview.md) using any of several methods available with Snowflake, depending on the
language and skill set you have available. Choose the tool that’s right for your needs from the following table.

| Language | Approach |
| --- | --- |
| **SQL**  Execute a SQL command, such as by using Snowsight. | Execute the SQL CREATE FUNCTION command to create a function with handler code written in one of the following languages:   *[Java](java/udf-java-introduction.md)* [JavaScript](javascript/udf-javascript-introduction.md) *[Python](python/udf-python-introduction.md)* [Scala](scala/udf-scala-introduction.md) * [SQL](sql/udf-sql-introduction.md) |
| **Java, Python, or Scala with Snowpark**  Write code in one of the supported languages, then execute the code locally to perform operations in Snowflake. | Execute client code that uses Snowpark APIs in one of the following languages.   *Java [UDFs](../snowpark/java/creating-udfs.md)* Python [UDFs](../snowpark/python/creating-udfs.md) | [UDTFs](../snowpark/python/creating-udtfs.md)   | [UDAFs](../snowpark/python/creating-udafs.md) * Scala [UDFs](../snowpark/scala/creating-udfs.md) |
| **Command line**  Create and manage Snowflake entities by executing commands from the command line. | Execute commands of the [Snowflake CLI](../snowflake-cli/objects/manage-objects.md). |
| **Python**  On the client, write code that executes management operations on Snowflake. | Execute code that uses the [Snowflake Python API](../snowflake-python-api/snowflake-python-managing-functions-procedures.md). |
| **RESTful APIs** (language-agnostic)  Make requests of RESTful endpoints to create and manage Snowflake entities. | Make a request to create a procedure using the [Snowflake REST API](../snowflake-rest-api/user-defined-function/user-defined-function-introduction.md) |

## Key properties

The following describes some of the properties required or typically used when creating a function.

Function name:
:   The function name does not need to match the name of the handler. For more about name constraints and conventions, see
    [Naming and overloading procedures and UDFs](../udf-stored-procedure-naming-conventions.md).

Arguments:
:   For more information on requirements, see [Defining arguments for UDFs and stored procedures](../udf-stored-procedure-arguments.md).

Return type:
:   For information about how Snowflake maps SQL data types to handler data types, see
    [Data Type Mappings Between SQL and Handler Languages](../udf-stored-procedure-data-type-mapping.md).

Handler name:
:   When required, this is the name of the class or method containing code that executes when the function is executed. You need specify a
    handler name only for handlers written in Java, Python, and Scala. For JavaScript and SQL handlers, all code specified
    in-line will be executed as the handler.

Dependencies:
:   For a handler written in Java, Python, or Scala, you might also need to specify the Snowpark library, such as when creating the function.

    For more about making dependencies available to your handler, see [Making dependencies available to your code](../upload-dependencies.md).

Handler language runtime:
:   When the handler language is Java, Python, or Scala, specify the runtime version to indicate which supported runtime version to use.
    Keep in mind that if you use the default version, that default will change over time.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE FUNCTION | Schema | The privilege only enables the creation of user-defined functions in the schema.  If you want to enable the creation of data metric functions, the role must have the CREATE DATA METRIC FUNCTION privilege. |
| USAGE | Function | Granting the USAGE privilege on the newly created function to a role allows users with that role to call the function elsewhere in Snowflake (such as masking policy owner role for External Tokenization). |
| USAGE | External access integration | Required on integrations, if any, specified by the EXTERNAL_ACCESS_INTEGRATIONS parameter. For more information, see [CREATE EXTERNAL ACCESS INTEGRATION](../../sql-reference/sql/create-external-access-integration.md). |
| READ | Secret | Required on secrets, if any, specified by the SECRETS parameter. For more information, see [Creating a secret to represent credentials](../external-network-access/creating-using-external-network-access.md) and [Using the external access integration in a function or procedure](../external-network-access/creating-using-external-network-access.md). |
| USAGE | Schema | Required on schemas containing secrets, if any, specified by the SECRETS parameter. For more information, see [Creating a secret to represent credentials](../external-network-access/creating-using-external-network-access.md) and [Using the external access integration in a function or procedure](../external-network-access/creating-using-external-network-access.md). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

The following notes describe usage notes relevant to the languages supported for writing handlers. Although notes in the following
sections refer to clauses of the SQL CREATE FUNCTION command, these clauses are typically represented in other ways in other tools
you can use to create functions.

### All languages

* `function_definition` has size restrictions. The maximum allowable size is subject to change.
* The delimiters around the `function_definition` can be either single quotes or a pair of dollar signs.

  Using `$$` as the delimiter makes it easier to write functions that contain single quotes.

  If the delimiter for the body of the function is the single quote character,
  then any single quotes within `function_definition` (such as string
  literals) must be escaped by single quotes.
* If using a UDF in a [masking policy](../../sql-reference/sql/create-masking-policy.md), ensure the data type of the column, UDF, and masking policy match. For
  more information, see [User-defined functions in a masking policy](../../user-guide/security-column-intro.md).
* If you specify the [CURRENT_DATABASE](../../sql-reference/functions/current_database.md) or [CURRENT_SCHEMA](../../sql-reference/functions/current_schema.md) function in the
  handler code of the UDF, the function returns the database or schema that contains the UDF, not the database or schema in use for
  the session.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../../sql-reference/metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

### Java

* In Java, primitive data types don’t allow NULL values, so passing a NULL for an argument of such a type results in
  an error.
* In the HANDLER clause, the method name is case-sensitive.
* In the IMPORTS and TARGET_PATH clauses:

  * Package, class, and file name(s) are case-sensitive.
  * Stage name(s) are case-insensitive.
* You can use the PACKAGES clause to specify package names and version numbers for Snowflake system-defined dependencies, such as those
  from Snowpark. For other dependencies, specify dependency JAR files with the IMPORTS clause.
* Snowflake validates that:

  * The JAR file specified in the CREATE FUNCTION statement’s HANDLER exists and contains the specified
    class and method.
  * The input and output types specified in the UDF declaration are compatible with the input and output types
    of the Java method.

  Validation can be done at creation time or execution time, depending on whether you are connected to an active Snowflake warehouse.

  * Creation time — If you are connected to an active Snowflake warehouse at the time the CREATE FUNCTION statement is
    executed, the UDF is validated at creation time.
  * Execution time — If you are not connected to an active Snowflake warehouse, the UDF is created, but is not validated
    immediately, and Snowflake returns the following message:

    `Function <name> created successfully, but could not be validated since there is no active warehouse`.

### JavaScript

* Snowflake does not validate JavaScript code at UDF creation time. In other words, creation of the UDF succeeds regardless of whether
  the code is valid. If the code is not valid, Snowflake returns errors when the UDF is called at query time.

### Python

* In the HANDLER clause, the handler function name is case-sensitive.
* In the IMPORTS clause:

  * File name(s) are case-sensitive.
  * Stage name(s) are case-insensitive.
* You can use the PACKAGES clause to specify package names and version numbers for dependencies, such as those
  from Snowpark. For other dependencies, specify dependency files with the IMPORTS clause.
* Snowflake validates that:

  * The function or class specified in the CREATE FUNCTION statement’s HANDLER exists.
  * The input and output types specified in the UDF declaration are compatible with the input and output types
    of the handler.

### Scala

* In the HANDLER clause, the method name is case-sensitive.
* In the IMPORTS and TARGET_PATH clauses:

  * Package, class, and file name(s) are case-sensitive.
  * Stage name(s) are case-insensitive.
* You can use the PACKAGES clause to specify package names and version numbers for Snowflake system-defined dependencies, such as those
  from Snowpark. For other dependencies, specify dependency JAR files with the IMPORTS clause.
* Snowflake validates that:

  * The JAR file specified in the CREATE FUNCTION statement’s HANDLER exists and contains the specified
    class and method.
  * The input and output types specified in the UDF declaration are compatible with the input and output types
    of the Scala method.

  Validation can be done at creation time or execution time, depending on whether you are connected to an active Snowflake warehouse.

  * Creation time — If you are connected to an active Snowflake warehouse at the time the CREATE FUNCTION statement is
    executed, the UDF is validated at creation time.
  * Execution time — If you are not connected to an active Snowflake warehouse, the UDF is created, but is not validated
    immediately, and Snowflake returns the following message:

    `Function <name> created successfully, but could not be validated since there is no active warehouse`.

### SQL

* Currently, the NOT NULL clause is not enforced for SQL UDFs.

## Create a UDF with SQL

You can create a UDF with SQL using the following steps.

You create a UDF with the following steps:

1. Write handler code that executes when the UDF is called.

   You can use one of the supported handler languages. For more information, see [Supported languages and tools](udf-overview.md).
2. Choose whether you’ll keep the handler code in-line with the CREATE FUNCTION SQL statement or refer to it on a stage.

   Each has its advantages. For more information, see [Keeping handler code in-line or on a stage](../inline-or-staged.md).
3. Execute a [CREATE FUNCTION](../../sql-reference/sql/create-function.md) statement in SQL, specifying properties of the function.

   Code in the following example creates a UDF called `function_name` with the in-line handler
   `HandlerClass.handlerMethod`.

   ```sqlsyntax
   create function function_name(x integer, y integer)
     returns integer
     language java
     handler='HandlerClass.handlerMethod'
     target_path='@~/HandlerCode.jar'
     as
     $$
         class HandlerClass {
             public static int handlerMethod(int x, int y) {
               return x + y;
             }
         }
     $$;
   ```

   The following describes some of the properties required or typically used when creating a function.

   * Function name.

     The UDF name does not need to match the name of the handler. The CREATE FUNCTION statement associates the UDF name with the handler.

     For more about name constraints and conventions, see [Naming and overloading procedures and UDFs](../udf-stored-procedure-naming-conventions.md).
   * Function arguments, if any.

     See [Defining arguments for UDFs and stored procedures](../udf-stored-procedure-arguments.md).
   * Return type with the RETURNS clause.

     For a scalar return value, the RETURNS clause will specify a single return type; for a tabular return value, RETURNS will specify
     the TABLE keyword specifying column type in the tabular return value.

     For information about how Snowflake maps SQL data types to handler data types, see
     [Naming and overloading procedures and UDFs](../udf-stored-procedure-naming-conventions.md).
   * Handler name with the HANDLER clause.

     When required, this is the name of the class or method containing code that executes when the UDF is called. You need specify a
     handler name only for handlers written in Java and Python. For JavaScript and SQL handlers, all code specified in-line will be
     executed as the handler.

     The following table describes the form of the HANDLER clause’s value based on the handler language and function type.

     | Handler Language | UDF | UDTF |
     | --- | --- | --- |
     | Java | Class and method name.  For example: `MyClass.myMethod` | Class name only. Handler method name is predetermined by the required interface. |
     | JavaScript | None. | None. |
     | Python | Class and method name if a class is used; otherwise, function name.  For example: `module.my_function` or `my_function` | Class name only. Handler method name is predetermined by the required interface. |
     | SQL | None. | None. |

   * Dependencies required by the handler, if any, using the IMPORTS or PACKAGES clauses.

     For more about making dependencies available to your handler, see [Making dependencies available to your code](../upload-dependencies.md).
   * Handler language runtime with RUNTIME_VERSION clause.

     When the handler language is Java or Python, use the RUNTIME_VERSION clause to specify which supported runtime version to use.
     Omitting the clause will prompt Snowflake to use the default, which may change in the future.
