# Source: https://docs.snowflake.com/en/developer-guide/udf/scala/udf-scala-introduction.md

# Introduction to Scala UDFs

You can write the handler for a user-defined function (UDF) in Scala. A handler executes as the function’s logic when it’s called in SQL.

Once you have a handler, you create the UDF with SQL. For information on using SQL to create or call a UDF, refer to
[Creating a user-defined function](../udf-creating-sql.md) or [Executing a UDF](../udf-calling-sql.md).

For an introduction to UDFs, including a list of languages in which you can write a UDF handler, refer to [User-defined functions overview](../udf-overview.md).

> **Note:**
>
> For limitations related to Scala handlers, refer to [Scala UDF limitations](udf-scala-limitations.md).

You can also use Scala to write a UDF when using the Snowpark API. For more information, refer to
[Creating User-Defined Functions (UDFs) for DataFrames in Scala](../../snowpark/scala/creating-udfs.md).

## Prerequisites

Snowflake currently supports writing UDFs in the following versions of Scala:

[Preview Feature](../../../release-notes/preview-features.md) — Open

Support for version 2.13 is in preview. Available to all accounts.

* 2.13
* 2.12

For more information, see [Writing code to support different Scala versions](../../scala-version-differences.md).

## How a handler works

When a user calls a UDF, the user passes UDF’s name and arguments to Snowflake. Snowflake calls the handler method associated with the UDF
to execute the UDF’s logic. The handler method then returns the output to Snowflake, which passes it back to the client.

For a scalar function (one that returns a single value), the UDF returns a single value for each row passed to the UDF.

To support your handler’s logic, your code can make calls to libraries that are external to the handler. For example, if you already have
data analysis code in Scala, then you can probably use it from your handler code.

For general information on writing a handler in Scala, refer to [General Scala UDF handler coding guidelines](udf-scala-general.md). For information on
writing a scalar function, refer to [Writing a scalar UDF in Scala](udf-scala-scalar.md).

### Example

Code in the following example creates a UDF called `echo_varchar` with a handler method `TestFunc.echoVarchar`. The Scala
argument and return types are converted to and from SQL by Snowflake according to mappings described in
[SQL-Scala Data Type Mappings](../../udf-stored-procedure-data-type-mapping.md).

Scala 2.12Scala 2.13 (Preview)

```sqlexample-scala
CREATE OR REPLACE FUNCTION echo_varchar(x VARCHAR)
  RETURNS VARCHAR
  LANGUAGE SCALA
  RUNTIME_VERSION = 2.12
  HANDLER='TestFunc.echoVarchar'
  AS
  $$
  class TestFunc {
    def echoVarchar(x : String): String = {
      return x
    }
  }
  $$;
```

```sqlexample-scala
CREATE OR REPLACE FUNCTION echo_varchar(x VARCHAR)
  RETURNS VARCHAR
  LANGUAGE SCALA
  RUNTIME_VERSION = 2.13
  HANDLER='TestFunc.echoVarchar'
  AS
  $$
  class TestFunc {
    def echoVarchar(x : String): String = {
      return x
    }
  }
  $$;
```

### Call the UDF

```sqlexample
SELECT echo_varchar('Hello');
```

## Design considerations

Keep in mind the following for designing a useful handler.

* **General considerations.** For considerations common to UDFs and procedures, refer to
  [Design Guidelines and Constraints for Functions and Procedures](../../udf-stored-procedure-guidelines.md).
* **Staying within Snowflake-imposed constraints.** For information on designing handler code that runs well on Snowflake,
  refer to [Designing Handlers that Stay Within Snowflake-Imposed Constraints](../../udf-stored-procedure-constraints.md).
* **SQL-Scala type mapping.** When exchanging argument and return values with a UDF, Snowflake converts between the handler language and SQL.
  For more information on choosing data types for your handler code, refer to [SQL-Scala Data Type Mappings](../../udf-stored-procedure-data-type-mapping.md).
* **Code packaging.** You can make your handler code available either in-line with the CREATE FUNCTION statement or on a stage as compiled
  code in a JAR. For more information on the difference, refer to [Keeping handler code in-line or on a stage](../../inline-or-staged.md).

  For information on using sbt to package the compiled code for your Scala handler, refer to
  [Packaging Scala Handler Code with sbt](../../udf-stored-procedure-build-sbt.md).
* **Code optimization.** For information about optimizing your handler code, such as when the code handles state shared across rows,
  refer to [Controlling global state in scalar Scala UDFs](udf-scala-optimizing.md).
* **Best practices.** For information about best practices, refer to [Best practices](udf-scala-general.md) and
  [Security Practices for UDFs and Procedures](../../udf-stored-procedure-security-practices.md).

## Handler coding

From basics to detailed examples, the following topics describe how to write a UDF handler in Scala.

* **General guidelines.** For general information about handler coding, including handling errors, choosing data types, and more, refer to
  [General Scala UDF handler coding guidelines](udf-scala-general.md).
* **Writing a scalar function** For more information, refer to [Writing a scalar UDF in Scala](udf-scala-scalar.md).
* **Logging and event tracing.** For information on capturing log and trace data as your handler code executes, refer to
  [Logging, tracing, and metrics](../../logging-tracing/logging-tracing-overview.md).
* **Code examples** For a range of handler examples, refer to [Scala UDF handler examples](udf-scala-examples.md).
* **Dependencies.** You can make dependencies available to your code at run time by uploading them to a stage. For more information, refer
  to [Making dependencies available to your code](../../upload-dependencies.md).
* **Handler files organization.** If you intend to package compiled handler code into a JAR file to stage, organize and build your code
  using the suggestions in [Scala UDF handler project and packaging](udf-scala-packaging.md).
