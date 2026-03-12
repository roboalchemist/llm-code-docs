# Source: https://docs.snowflake.com/en/developer-guide/snowpark-connect/snowpark-connect-compatibility.md

# Snowpark Connect for Spark compatibility guide

This guide documents the compatibility between the Snowpark Connect for Spark implementation of the Spark DataFrame APIs and native
Apache Spark. It is intended to help users understand the key differences, unsupported features, and migration considerations when moving
Spark workloads to Snowpark Connect for Spark.

Snowpark Connect for Spark aims to provide a familiar Spark DataFrame API experience on top of the Snowflake execution engine.
However, there are the compatibility gaps described in this topic. This guide highlights those differences to help you plan and adapt
your migration. These might be addressed in a future release.

## DataTypes

### Unsupported data types

* [DayTimeIntervalType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DayTimeIntervalType.html)
* [YearMonthIntervalType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/YearMonthIntervalType.html)
* [UserDefinedTypes](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/UserDefinedType.html)

### Implicit data type conversion

When using Snowpark Connect for Spark, keep in mind how data types are handled. Snowpark Connect for Spark implicitly represents `ByteType`,
`ShortType`, and `IntegerType` as `LongType`. This means that while you might define columns or data with
`ByteType`, `ShortType`, or `IntegerType`, the data will be represented and returned by Snowpark Connect for Spark as
`LongType`. Similarly, implicit conversion might also occur for `FloatType` and
`DoubleType` depending on the specific operations and context. The Snowflake execution engine will internally handle data
type compression and may in fact store the data as `Byte` or `Short`, but these are considered implementation details and not exposed to the
end user.

Semantically, this representation will not impact the correctness of your Spark queries.

| Data type from native PySpark | Data type from Snowpark Connect for Spark |
| --- | --- |
| `ByteType` | `LongType` |
| `ShortType` | `LongType` |
| `IntegerType` | `LongType` |
| `LongType` | `LongType` |

The following example shows a difference in how Spark and Snowpark Connect for Spark handle data types in query results.

#### Query

```python
query = """
    SELECT * FROM VALUES
    (float(1.0), double(1.0), 1.0, "1", true, :code:`NULL`),
    (float(2.0), double(2.0), 2.0, "2", false, :code:`NULL`),
    (float(3.0), double(3.0), :code:`NULL`, "3", false, :code:`NULL`)
    AS tab(a, b, c, d, e, f)
    """
```

#### Spark

```python
spark.sql(query).printSchema()
```

```output
root
 |-- a: float (nullable = false)
 |-- b: double (nullable = false)
 |-- c: decimal(2,1) (nullable = true)
 |-- d: string (nullable = false)
 |-- e: boolean (nullable = false)
 |-- f: void (nullable = true)
```

#### Snowpark Connect for Spark

```python
snowpark_connect_spark.sql(query).printSchema()
```

```output
root
 |-- a: double (nullable = false)
 |-- b: double (nullable = false)
 |-- c: decimal (nullable = true)
 |-- d: string (nullable = false)
 |-- e: boolean (nullable = true)
 |-- f: string (nullable = true)
```

### `NullType` nuance

Snowpark Connect for Spark doesn’t support the [NullType](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.types.NullType.html)
datatype, which is a supported data type in Spark. This causes behavior changes when using `Null` or `None` in dataframes.

In Spark, a literal `NULL` (for example, with `lit(None)`) is automatically inferred as a `NullType`. In Snowpark Connect for Spark, it is inferred as a
`StringType` during schema inference.

```python
df = self.spark.range(1).select(lit(None).alias("null_col"))
field = df.schema["null_col"]

# Spark: StructField('null_col', :code:`NullType`(), True)
# Snowpark Connect for Spark: StructField('null_col', :code:`StringType`(), True)
```

### Structured data types in `ArrayType`, `MapType`, and `ObjectType`

While structured type support is not available by default in Snowpark Connect for Spark, `ARRAY`, `MAP` and `Object` datatypes are
treated as generic, untyped collections. This means there is no enforcement of element types, field names, schema, or nullability, unlike
what would be provided by structured type support.

If you have a dependency on this support, please work with your account team to enable this feature for your account.

## Unsupported Spark APIs

The following are the APIs supported by classic Spark and Spark Connect but not supported in Snowpark Connect for Spark.

* [Dataframe.hint](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.hint.html):
  Snowpark Connect for Spark ignores any hint that is set on a dataframe. The Snowflake query optimizer automatically determines the
  most efficient execution strategy.
* [DataFrame.repartition](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.repartition.html):
  This is a no-op in Snowpark Connect for Spark. Snowflake automatically manages data distribution and partitioning across its distributed
  computing infrastructure.
* [pyspark.RDD](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.html): RDD APIs are not supported in
  Spark Connect (including Snowpark Connect for Spark).
* [pyspark.ml](https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html)
* [pyspark streaming](https://spark.apache.org/docs/latest/streaming-programming-guide.html)

## UDF differences

### `StructType` differences

When Spark converts a `StructType` to be used in a user-defined function (UDF), it converts it to a `tuple` type in Python. Snowpark Connect for Spark will convert a
`StructType` into a `dict` type in Python. This has fundamental differences in element access and output.

* Spark will access indexes with 0, 1, 2, 3, and so on.
* Snowpark Connect for Spark will access indexes using ‘_1’, ‘_2’, and so on.

```python
def f(e):
    return e[0]

    df = self.spark.createDataFrame([((1.0, 1.0), (1, 1))], ["c1", "c2"])
    result = df.select("*", udf(f, DoubleType())("c1"))

# This results in an index access issue. Workaround is to use _1, _2 as indicies.
# Workaround:

def f(e):
    return e['_1']

row = (
    self.spark.range(1)
    .selectExpr("struct(1, 2) as struct")
    .select(
        udf(lambda x: x, "struct<col1:int,col2:int>")("struct"),
    )
    .first()
)

self.assertEquals(row[0], Row(col1=1, col2=2))

# Spark: Row(col1=1, col2=2)

# Snowpark Connect for Spark: {'col1': 1, 'col2': 2}
```

### Iterator Type in UDFs

Iterator isn’t supported as a return type or as an input type.

```python
# This will not work
def func(iterator):
  for _ in iterator:
              ...

df = self.spark.range(10)
actual = df.repartition(1).mapInArrow(func, "a long").collect()
```

### Importing files to a Python UDF

With Snowpark Connect for Spark, you can specify external libraries and files in Python UDFs. Snowflake includes Python files and archives in your code’s
execution context. You can import functions from these included files in a UDF without additional steps. This dependency-handling behavior
works as described in [Creating a Python UDF with code uploaded from a stage](../udf/python/udf-python-creating.md).

To include external libraries and files, you provide stage paths to the files as the value of the configuration setting
`snowpark.connect.udf.imports`. The configuration value should be an array of stage paths to the files, where the paths are
separated by commas.

Code in the following example includes two files in the UDF’s execution context. The UDF imports functions from these files and uses them
in its logic.

```python
# Files need to be previously staged
spark.conf.set("snowpark.connect.udf.imports", "[@stage/library.py, @other_lib.zip]")

@udf(returnType = StringType())
def import_example(input: str) -> str:
  from library import first_function
  from other_lib.custom import second_function

  return first_function(input) + second_function(input)

spark.range(1).select(import_read_example("example_string")).show()
```

You can use the `snowpark.connect.udf.imports` setting to include other kinds of files as well, such as those with data your code
needs to read. Note that when you do this, your code should only read from the included files; any writes to such files will be lost after
the function’s execution ends.

```python
# Files need to be previously staged
spark.conf.set("snowpark.connect.udf.imports", "[@stage/data.csv]")

@udf(returnType = StringType())
def import_read_example(file_name: str) -> str:
  with open(file_name) as f:
    return f.read()

spark.range(1).select(import_read_example("data.csv")).show()
```

## Lambda function limitations

User-defined functions (UDFs) are not supported within lambda expressions. This includes both custom UDFs and
certain built-in functions whose underlying implementation relies on Snowflake UDFs. Attempting to use a UDF inside a lambda expression
will result in an error.

```python
df = spark.createDataFrame([({"a": 123},)], ("data",))
df.select(map_filter("data", lambda _, v: bit_count(v) > 3)).show() # does not work, since `bit_count` is implemented with UDF
```

## Using path-sensitive modules

If the Python UDF body imports a module that requires a precise path, you need to take additional steps. When loading dependencies for UDFs, Snowflake puts all of the files in the working directory without preserving the original path. To preserve the original structure, you must zip dependencies and then add as an import for SCOS by using either `addArtifacts` or configuration `snowpark.connect.udf.python.imports`.

```python
# Make sure to zip module before importing to stage
spark.conf.set("snowpark.connect.udf.python.imports", "[@nested_library.zip]")

@udf(returnType = StringType())
def import_example(input: str) -> str:
  from nested_library.sub_module.functions import example_func

  return example_func(input)

spark.range(1).select(import_read_example("example_string")).show()

#add dependencies for import
spark.addArtifacts("nested_library.zip", pyfile=True)

@udf(returnType = StringType())
def import_example(input: str) -> str:
  from nested_library.sub_module.functions import example_func

  return example_func(input)

spark.range(1).select(import_read_example("example_string")).show()
```

## Data sources

| Data source | Compatibility issues compared with PySpark |
| --- | --- |
| Avro | File type is not supported. |
| CSV | Save mode is not supported for the following: `Append`, `Ignore`.  The followings are known limitations:   *`compression`: This parameter supports only the following values: GZIP, BZ2, BROTLI, ZSTD, DEFLATE, RAW_DEFLATE, NONE, UNCOMPRESSED.* `dateFormat`: Custom date formats must follow the formats at [Datetime Patterns](../../sql-reference/data-types-datetime.md). *`encoding`: Encoding in multiLine mode is not supported.* `lineSep`: This parameter cannot be set to an empty string. *`quote`: This parameter cannot be set to an empty string.* `timestampFormat`: Custom date formats must follow the formats at [Datetime Patterns](../../sql-reference/data-types-datetime.md). * Reading an empty file is not supported.   The following options are not supported: `charToEscapeQuoteEscaping`, `columnNameOfCorruptRecord`, `comment`, `emptyValue`, `enableDateTimeParsingFallback`, `enforceSchema`, `escape`, `escapeQuotes`, `ignoreLeadingWhiteSpace`, `ignoreTrailingWhiteSpace`, `locale`, `maxCharsPerColumn`, `maxColumns`, `mode`, `nanValue`, `negativeInf`, `positiveInf`, `preferDate`, `quoteAll`, `samplingRatio`, `timestampNTZFormat`, `unescapedQuoteHandling`. |
| JSON | Save mode not supported for the following: `Append`, `Ignore`.  The followings are known limitations:   *`compression`: This parameter supports only the following values: GZIP, BZ2, BROTLI, ZSTD, DEFLATE, RAW_DEFLATE, NONE, UNCOMPRESSED.* `dateFormat`: Custom date formats must follow the formats at [Datetime Patterns](../../sql-reference/data-types-datetime.md). *`encoding`: Encoding in multiline mode is not supported.* `timestampFormat`: Custom date formats must follow the formats at [Datetime Patterns](../../sql-reference/data-types-datetime.md). *Difference in `show`: If the value of field is a string, it would be quoted. An extra `n` character would be shown in the result.* Array-of-struct field projection via dot notation is not supported *Reading a JSON file with Spark SQL is not supported.* MapType is not supported.   The following options are not supported: `allowBackslashEscapingAnyCharacter`, `allowComments`, `allowNonNumericNumbers`, `allowNumericLeadingZeros`, `allowSingleQuotes`, `allowUnquotedControlChars`, `allowUnquotedFieldNames`, `columnNameOfCorruptRecord`, `dropFieldIfAllNull`, `enableDateTimeParsingFallback`, `ignoreNullFields`, `lineSep`, `locale`, `mode`, `prefersDecimal`, `primitivesAsString`, `samplingRatio`, `timeZone`, `timestampNTZFormat`. |
| Orc | File type is not supported. |
| Parquet | Save mode is not supported for the following: `Append`, `Ignore`.  The followings are known limitations:   *`compression`: This parameter supports only the following values: GZIP, BZ2, BROTLI, ZSTD, DEFLATE, RAW_DEFLATE, NONE, UNCOMPRESSED.* Date formats must follow the formats at [Datetime Patterns](../../sql-reference/data-types-datetime.md). *MapType and IntervalType are not supported.* Configuration is not supported: (ALL).   The following options are not supported: `datetimeRebaseMode`, `int96RebaseMode`, `mergeSchema`. |
| Text | Save mode is not supported for the following: `Append`, `Ignore`.  The following are known limitations:   *`compression`: This parameter supports only the following values: GZIP, BZ2, BROTLI, ZSTD, DEFLATE, RAW_DEFLATE, NONE, UNCOMPRESSED.* The `lineSep` parameter is not supported in write. * Partitioned directory is not supported. |
| XML | Save mode is not supported for the following: `Append`, `Ignore`.  The followings are known limitations:   *Schema inference is not supported. A schema must be provided using `.schema()`.* Permissive mode is not supported. If input data does not match the user schema type and cannot be coerced, an error will be thrown. *`compression`: This parameter is not supported when `rowTag` is specified. Supports only the following values: GZIP, BZ2, BROTLI, ZSTD, DEFLATE, RAW_DEFLATE, NONE, UNCOMPRESSED.* MapType is not supported. * Reading a XML file with Spark SQL is not supported.   The following options are not supported: `arrayElementName`, `dateFormat`, `declaration`, `inferSchema`, `locale`, `modifiedBefore`, `recursiveFileLookup`, `rootTag`, `samplingRatio`, `timeZone`, `timestampFormat`, `timestampNTZFormat`, `validateName`, `wildcardColName`. |
| Snowflake table | Write to table doesn’t need a provider format.  Bucketing and partitioning are not supported.  Storage format and versioning are not supported. |

## Catalog

### Snowflake Horizon Catalog provider support

* Only Snowflake is supported as a catalog provider.

### Unsupported catalog APIs

* `registerFunction`
* `listFunctions`
* `getFunction`
* `functionExists`
* `createExternalTable`

### Partially supported catalog APIs

* `createTable` (no external table support)

## Iceberg

### Snowflake managed iceberg table

Snowpark Connect for Spark works with Apache Iceberg™ tables, including externally managed Iceberg tables and catalog-linked databases.

#### Read

Time travel is not supported, including historical snapshot, branch, and incremental read.

#### Write

* Using Spark SQL to create tables is not supported.
* Schema merge is not supported.
* To create the table, you must:

  * Create an external volume.
  * Link the external volume needs to the table creation in either of the following ways:

    * Set the EXTERNAL_VOLUME to the database.
    * Set `snowpark.connect.iceberg.external_volume` to Spark configuration.

### External managed Iceberg table

#### Read

* You must create a Snowflake unmanaged table entity.
* Time travel is not supported, including historical snapshot, branch, and incremental read.

#### Write

* Table creation is not supported.
* Writing to the existing Iceberg table is supported.
