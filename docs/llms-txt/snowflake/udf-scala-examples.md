# Source: https://docs.snowflake.com/en/developer-guide/udf/scala/udf-scala-examples.md

# Scala UDF handler examples

This topic includes simple examples of UDF handler code written in Scala.

For information on using Scala to create a scalar UDF handler, refer to [Writing a scalar UDF in Scala](udf-scala-scalar.md). For general
coding guidelines, refer to [General Scala UDF handler coding guidelines](udf-scala-general.md).

## Creating and calling a simple in-line Scala UDF

The following statements create and call an in-line Scala UDF. This code returns the VARCHAR passed to it.

This function is declared with the optional `CALLED ON NULL INPUT` clause to indicate that the function is
called even if the value of the input is NULL. (This function would return NULL with or without this clause, but
you could modify the code to handle NULL another way, for example, to return an empty string.)

### Create the UDF

Scala 2.12Scala 2.13 (Preview)

```sqlexample-scala
CREATE OR REPLACE FUNCTION echo_varchar(x VARCHAR)
  RETURNS VARCHAR
  LANGUAGE SCALA
  CALLED ON NULL INPUT
  RUNTIME_VERSION = 2.12
  HANDLER='Echo.echoVarchar'
  AS
  $$
  class Echo {
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
  CALLED ON NULL INPUT
  RUNTIME_VERSION = 2.13
  HANDLER='Echo.echoVarchar'
  AS
  $$
  class Echo {
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

### Passing a NULL to an in-line Scala UDF

This uses the `echo_varchar()` UDF defined above. The SQL `NULL` value is implicitly converted to
Scala [Null](https://www.scala-lang.org/api/2.12.17/scala/Null.html), and that Scala `Null` is returned and implicitly converted
back to SQL `NULL`:

Call the UDF:

```sqlexample
SELECT echo_varchar(NULL);
```

## Returning NULL explicitly from an in-line UDF

The following code shows how to return a NULL value explicitly. The Scala value `Null` is converted to
SQL `NULL`.

### Create the UDF

Scala 2.12Scala 2.13

```sqlexample-scala
CREATE OR REPLACE FUNCTION return_a_null()
  RETURNS VARCHAR
  LANGUAGE SCALA
  RUNTIME_VERSION = 2.12
  HANDLER='TemporaryTestLibrary.returnNull'
  AS
  $$
  class TemporaryTestLibrary {
    def returnNull(): String = {
      return null
    }
  }
  $$;
```

```sqlexample-scala
CREATE OR REPLACE FUNCTION return_a_null()
  RETURNS VARCHAR
  LANGUAGE SCALA
  RUNTIME_VERSION = 2.13
  HANDLER='TemporaryTestLibrary.returnNull'
  AS
  $$
  class TemporaryTestLibrary {
    def returnNull(): String = {
      return null
    }
  }
  $$;
```

### Call the UDF

```sqlexample
SELECT return_a_null();
```

## Passing an OBJECT to an in-line Scala UDF

The following example uses the SQL [OBJECT](../../../sql-reference/data-types-semistructured.md) data type and the corresponding Scala
data type (`Map[String, String]`), and extracts a value from the OBJECT. This example also shows that you
can pass multiple parameters to a Scala UDF.

Create and load a table that contains a column of type OBJECT:

```sqlexample
CREATE TABLE objectives (o OBJECT);
INSERT INTO objectives SELECT PARSE_JSON('{"outer_key" : {"inner_key" : "inner_value"} }');
```

### Create the UDF

Scala 2.12Scala 2.13 (Preview)

```sqlexample-scala
CREATE OR REPLACE FUNCTION extract_from_object(x OBJECT, key VARCHAR)
  RETURNS VARIANT
  LANGUAGE SCALA
  RUNTIME_VERSION = 2.12
  HANDLER='VariantLibrary.extract'
  AS
  $$
  import scala.collection.immutable.Map

  class VariantLibrary {
    def extract(m: Map[String, String], key: String): String = {
      return m(key)
    }
  }
  $$;
```

```sqlexample-scala
CREATE OR REPLACE FUNCTION extract_from_object(x OBJECT, key VARCHAR)
  RETURNS VARIANT
  LANGUAGE SCALA
  RUNTIME_VERSION = 2.13
  HANDLER='VariantLibrary.extract'
  AS
  $$
  import scala.collection.immutable.Map

  class VariantLibrary {
    def extract(m: Map[String, String], key: String): String = {
      return m(key)
    }
  }
  $$;
```

### Call the UDF

```sqlexample
SELECT extract_from_object(o, 'outer_key'),
  extract_from_object(o, 'outer_key')['inner_key'] FROM OBJECTIVES;
```

## Passing an ARRAY to an in-line Scala UDF

The following example uses the SQL [ARRAY](../../../sql-reference/data-types-semistructured.md) data type.

### Create the UDF

Scala 2.12Scala 2.13 (Preview)

```sqlexample-scala
CREATE OR REPLACE FUNCTION generate_greeting(greeting_words ARRAY)
  RETURNS VARCHAR
  LANGUAGE SCALA
  RUNTIME_VERSION = 2.12
  HANDLER='StringHandler.handleStrings'
  AS
  $$
  class StringHandler {
    def handleStrings(strings: Array[String]): String = {
      return concatenate(strings)
    }
    private def concatenate(strings: Array[String]): String = {
      var concatenated : String = ""
      for (newString <- strings)  {
          concatenated = concatenated + " " + newString
      }
      return concatenated
    }
  }
  $$;
```

```sqlexample-scala
CREATE OR REPLACE FUNCTION generate_greeting(greeting_words ARRAY)
  RETURNS VARCHAR
  LANGUAGE SCALA
  RUNTIME_VERSION = 2.13
  HANDLER='StringHandler.handleStrings'
  AS
  $$
  class StringHandler {
    def handleStrings(strings: Array[String]): String = {
      return concatenate(strings)
    }
    private def concatenate(strings: Array[String]): String = {
      var concatenated : String = ""
      for (newString <- strings)  {
          concatenated = concatenated + " " + newString
      }
      return concatenated
    }
  }
  $$;
```

## Reading a file with a Scala UDF

You can read the contents of a file with handler code. For example, you might want to read a file to process unstructured data with the
handler.

The file must be on a Snowflake stage that’s available to your handler.

To read the contents of staged files, your handler can read a dynamically-specified file by calling methods of either the
`SnowflakeFile` class or the `InputStream` class.

You might do this if you need to access a file specified by the caller. For more information, see the following in this topic:

* Reading a dynamically-specified file with SnowflakeFile
* Reading a dynamically-specified file with InputStream

`SnowflakeFile` provides features not available with `InputStream`, as described in the following table.

| Class | Input | Notes |
| --- | --- | --- |
| `SnowflakeFile` | URL formats:   *Scoped URL to reduce the risk of file injection attacks when the function’s caller is not also its owner.* File URL or string path for files that the UDF owner has access to.   The file must be located in a named internal stage or an external stage. | Easily access additional file attributes, such as file size. |
| `InputStream` | URL formats:   * Scoped URL to reduce the risk of file injection attacks when the function’s caller is not also its owner.   The file must be located in a named internal stage or an external stage. |  |

> **Note:**
>
> The UDF owner must have access to any files whose locations are not scoped URLs. You can read these staged files by having the handler
> code call the `SnowflakeFile.newInstance` method with a `boolean` value for a new `requireScopedUrl` parameter.
>
> The following example uses `SnowflakeFile.newInstance` while specifying that a scoped URL is not required.
>
> ```scala
> var filename = "@my_stage/filename.txt"
> var sfFile = SnowflakeFile.newInstance(filename, false)
> ```

### Reading a dynamically-specified file with `SnowflakeFile`

Using methods of the `SnowflakeFile` class, you can read files from a stage with your handler code. The `SnowflakeFile`
class is included on the classpath available to Scala UDF handlers on Snowflake.

> **Note:**
>
> To make your code resilient to file injection attacks, always use a scoped URL when passing a file’s location to a UDF, particularly
> when the function’s caller is not also its owner. You can create a scoped URL in SQL using the built-in function
> [BUILD_SCOPED_FILE_URL](../../../sql-reference/functions/build_scoped_file_url.md). For more information about what the BUILD_SCOPED_FILE_URL does, see
> [Introduction to unstructured data](../../../user-guide/unstructured-intro.md).

To develop your UDF code locally, add the Snowpark JAR containing `SnowflakeFile` to your code’s class path. For information about
`snowpark.jar`, see [Setting Up Your Development Environment for Snowpark Scala](../../snowpark/scala/setup.md). Note that Snowpark client applications cannot use this class.

When you use `SnowflakeFile`, it isn’t necessary to also specify either the staged file or the JAR containing
`SnowflakeFile` with an IMPORTS clause when you create the UDF, as in SQL with a CREATE FUNCTION statement.

### Create the UDF

Code in the following example uses `SnowflakeFile` to read a file from a specified stage location. Using an
`InputStream` from the `getInputStream` method, it reads the file’s contents into a `String` variable.

Scala 2.12Scala 2.13 (Preview)

```sqlexample-scala
CREATE OR REPLACE FUNCTION sum_total_sales_snowflake_file(file STRING)
  RETURNS INTEGER
  LANGUAGE SCALA
  RUNTIME_VERSION = 2.12
  PACKAGES=('com.snowflake:snowpark_2.12:latest')
  HANDLER='SalesSum.sumTotalSales'
  AS
  $$
  import java.io.InputStream
  import java.io.IOException
  import java.nio.charset.StandardCharsets
  import com.snowflake.snowpark_java.types.SnowflakeFile

  object SalesSum {
    @throws(classOf[IOException])
    def sumTotalSales(filePath: String): Int = {
      var total = -1

      // Use a SnowflakeFile instance to read sales data from a stage.
      val file = SnowflakeFile.newInstance(filePath)
      val stream = file.getInputStream()
      val contents = new String(stream.readAllBytes(), StandardCharsets.UTF_8)

      // Omitted for brevity: code to retrieve sales data from JSON and assign it to the total variable.

      return total
    }
  }
  $$;
```

```sqlexample-scala
CREATE OR REPLACE FUNCTION sum_total_sales_snowflake_file(file STRING)
  RETURNS INTEGER
  LANGUAGE SCALA
  RUNTIME_VERSION = 2.13
  PACKAGES=('com.snowflake:snowpark_2.13:latest')
  HANDLER='SalesSum.sumTotalSales'
  AS
  $$
  import java.io.InputStream
  import java.io.IOException
  import java.nio.charset.StandardCharsets
  import com.snowflake.snowpark_java.types.SnowflakeFile

  object SalesSum {
    @throws(classOf[IOException])
    def sumTotalSales(filePath: String): Int = {
      var total = -1

      // Use a SnowflakeFile instance to read sales data from a stage.
      val file = SnowflakeFile.newInstance(filePath)
      val stream = file.getInputStream()
      val contents = new String(stream.readAllBytes(), StandardCharsets.UTF_8)

      // Omitted for brevity: code to retrieve sales data from JSON and assign it to the total variable.

      return total
    }
  }
  $$;
```

### Call the UDF

```sqlexample
SELECT sum_total_sales_input_stream(BUILD_SCOPED_FILE_URL('@sales_data_stage', '/car_sales.json'));
```

### Reading a dynamically-specified file with `InputStream`

You can read file contents directly into a `java.io.InputStream` by making your handler function’s argument an `InputStream`
variable. This can be useful when the function’s caller will want to pass a file path as an argument.

> **Note:**
>
> To make your code resilient to file injection attacks scoped URLs are required when passing a file’s location to a UDF. You can create a
> scoped URL in SQL using the built-in function BUILD_SCOPED_FILE_URL. For more information about what the BUILD_SCOPED_FILE_URL does,
> see [Introduction to unstructured data](../../../user-guide/unstructured-intro.md).

### Create the UDF

Code in the following example has a handler function `sumTotalSales` that takes an `InputStream` and returns an `Int`.
At run time, Snowflake automatically assigns the contents of the file at the `file` variable’s path to the `stream`
argument variable.

Scala 2.12Scala 2.13

```sqlexample-scala
CREATE OR REPLACE FUNCTION sum_total_sales_input_stream(file STRING)
  RETURNS NUMBER
  LANGUAGE SCALA
  RUNTIME_VERSION = 2.12
  HANDLER = 'SalesSum.sumTotalSales'
  PACKAGES = ('com.snowflake:snowpark_2.12:latest')
  AS $$
  import com.snowflake.snowpark.types.Variant
  import java.io.InputStream
  import java.io.IOException
  import java.nio.charset.StandardCharsets
  object SalesSum {
    @throws(classOf[IOException])
    def sumTotalSales(stream: InputStream): Int = {
      val total = -1
      val contents = new String(stream.readAllBytes(), StandardCharsets.UTF_8)

      // Omitted for brevity: code to retrieve sales data from JSON and assign it to the total variable.

      return total
    }
  }
  $$;
```

```sqlexample-scala
CREATE OR REPLACE FUNCTION sum_total_sales_input_stream(file STRING)
  RETURNS NUMBER
  LANGUAGE SCALA
  RUNTIME_VERSION = 2.13
  HANDLER = 'SalesSum.sumTotalSales'
  PACKAGES = ('com.snowflake:snowpark_2.13:latest')
  AS $$
  import com.snowflake.snowpark.types.Variant
  import java.io.InputStream
  import java.io.IOException
  import java.nio.charset.StandardCharsets
  object SalesSum {
    @throws(classOf[IOException])
    def sumTotalSales(stream: InputStream): Int = {
      val total = -1
      val contents = new String(stream.readAllBytes(), StandardCharsets.UTF_8)

      // Omitted for brevity: code to retrieve sales data from JSON and assign it to the total variable.

      return total
    }
  }
  $$;
```

### Call the UDF

```sqlexample
SELECT sum_total_sales_input_stream(BUILD_SCOPED_FILE_URL('@sales_data_stage', '/car_sales.json'));
```
