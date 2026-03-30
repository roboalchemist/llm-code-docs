# Source: https://docs.snowflake.com/en/developer-guide/snowpark/scala/sql-to-snowpark.md

# Source: https://docs.snowflake.com/en/developer-guide/snowpark/java/sql-to-snowpark.md

# Quick reference: Snowpark Java APIs for SQL commands

This topic provides a quick reference of some of the Snowpark APIs that correspond to SQL commands.

(Note that this is not a complete list of the APIs that correspond to SQL commands.)

## Performing queries

### Selecting columns

To select specific columns, use [select](../reference/java/com/snowflake/snowpark_java/DataFrame.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample SELECT id, name FROM sample_product_data;``` | ```java DataFrame df = session.table("sample_product_data");  DataFrame dfSelectedCols = df.select(Functions.col("id"), Functions.col("name"));  dfSelectedCols.show();``` |

### Renaming columns

To rename a column, use [as](../reference/java/com/snowflake/snowpark_java/Column.md) or [alias](../reference/java/com/snowflake/snowpark_java/Column.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample SELECT id AS item_id FROM sample_product_data;``` | ```java DataFrame df = session.table("sample_product_data");  DataFrame dfRenamedCol = df.select(Functions.col("id").as("item_id"));  dfRenamedCol.show();``` |
|  | ```java DataFrame df = session.table("sample_product_data");  DataFrame dfRenamedCol = df.select(Functions.col("id").alias("item_id"));  dfRenamedCol.show();``` |

### Filtering data

To filter data, use [filter](../reference/java/com/snowflake/snowpark_java/DataFrame.md) or [where](../reference/java/com/snowflake/snowpark_java/DataFrame.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample SELECT * FROM sample_product_data WHERE id = 1;``` | ```java DataFrame df = session.table("sample_product_data");  DataFrame dfFilteredRows = df.filter(Functions.col("id").equal_to(Functions.lit(1)));  dfFilteredRows.show();``` |
|  | ```java DataFrame df = session.table("sample_product_data");  DataFrame dfFilteredRows = df.where(Functions.col("id").equal_to(Functions.lit(1)));  dfFilteredRows.show();``` |

### Sorting data

To sort data, use [sort](../reference/java/com/snowflake/snowpark_java/DataFrame.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample SELECT * FROM sample_product_data ORDER BY category_id;``` | ```java DataFrame df = session.table("sample_product_data");  DataFrame dfSorted = df.sort(Functions.col("category_id"));  dfSorted.show();``` |

### Limiting the number of rows returned

To limit the number of rows returned, use [limit](../reference/java/com/snowflake/snowpark_java/DataFrame.md). See [Limiting the Number of Rows in a DataFrame](working-with-dataframes.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample SELECT * FROM sample_product_data   ORDER BY category_id LIMIT 2;``` | ```java DataFrame df = session.table("sample_product_data");  DataFrame dfSorted = df.sort(Functions.col("category_id")).limit(2);  Row[] arrayRows = dfSorted.collect();``` |

### Performing joins

To perform a join, use [join](../reference/java/com/snowflake/snowpark_java/DataFrame.md) or [naturalJoin](../reference/java/com/snowflake/snowpark_java/DataFrame.md). See [Joining DataFrames](working-with-dataframes.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample SELECT * FROM sample_a   INNER JOIN sample_b   on sample_a.id_a = sample_b.id_a;``` | ```java DataFrame dfLhs = session.table("sample_a");  DataFrame dfRhs = session.table("sample_b");  DataFrame dfJoined =   dfLhs.join(dfRhs, dfLhs.col("id_a").equal_to(dfRhs.col("id_a")));  dfJoined.show();``` |
| ```sqlexample SELECT * FROM sample_a NATURAL JOIN sample_b;``` | ```java DataFrame dfLhs = session.table("sample_a");  DataFrame dfRhs = session.table("sample_b");  DataFrame dfJoined = dfLhs.naturalJoin(dfRhs);  dfJoined.show();``` |

### Querying semi-structured data

To traverse semi-structured data, use [subField(“<field_name>”)](../reference/java/com/snowflake/snowpark_java/Column.md) and [subField(<index>)](../reference/java/com/snowflake/snowpark_java/Column.md). See
[Working with Semi-Structured Data](working-with-dataframes.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample SELECT src:salesperson.name FROM car_sales;``` | ```java DataFrame df = session.table("car_sales");  DataFrame dfJsonField =   df.select(Functions.col("src").subField("salesperson").subField("name"));  dfJsonField.show();``` |

### Grouping and aggregating data

To group data, use [groupBy](../reference/java/com/snowflake/snowpark_java/DataFrame.md). This returns a [RelationalGroupedDataFrame](../reference/java/com/snowflake/snowpark_java/RelationalGroupedDataFrame.md) object, which you can use to perform the aggregations.

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample SELECT category_id, count(*)   FROM sample_product_data GROUP BY category_id;``` | ```java DataFrame df = session.table("sample_product_data");  DataFrame dfCountPerCategory = df.groupBy(Functions.col("category_id")).count();  dfCountPerCategory.show();``` |

### Calling window functions

To call a [window function](../../../user-guide/functions-window-using.md), use the [Window](../reference/java/com/snowflake/snowpark_java/Window.md) object methods to build a [WindowSpec](../reference/java/com/snowflake/snowpark_java/WindowSpec.md)
object, which in turn you can use for windowing functions (similar to using ‘<function> OVER … PARTITION BY … ORDER BY’).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample SELECT category_id, id, SUM(amount) OVER   (PARTITION BY category_id ORDER BY product_date)   FROM sample_product_data ORDER BY product_date;``` | ```java WindowSpec window = Window.partitionBy(   Functions.col("category_id")).orderBy(Functions.col("product_date"));  DataFrame df = session.table("sample_product_data");  DataFrame dfCumulativePrices = df.select(   Functions.col("category_id"), Functions.col("product_date"),   Functions.sum(Functions.col("amount")).over(window)).sort(Functions.col("product_date"));  dfCumulativePrices.show();``` |

## Updating, deleting, and merging rows

To update, delete, and merge rows in a table, use [Updatable](../reference/java/com/snowflake/snowpark_java/Updatable.md). See [Updating, Deleting, and Merging Rows in a Table](working-with-dataframes.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample UPDATE sample_product_data   SET serial_number = 'xyz' WHERE id = 12;``` | ```java import java.util.HashMap; import java.util.Map; ...  Map<Column, Column> assignments = new HashMap<>();  assignments.put(Functions.col("serial_number"), Functions.lit("xyz"));  Updatable updatableDf = session.table("sample_product_data");  UpdateResult updateResult =   updatableDf.update(     assignments,     Functions.col("id").equal_to(Functions.lit(12)));  System.out.println("Number of rows updated: " + updateResult.getRowsUpdated());``` |
| ```sqlexample DELETE FROM sample_product_data   WHERE category_id = 50;``` | ```java Updatable updatableDf = session.table("sample_product_data");  DeleteResult deleteResult =   updatableDf.delete(updatableDf.col("category_id").equal_to(Functions.lit(50)));  System.out.println("Number of rows deleted: " + deleteResult.getRowsDeleted());``` |
| ```sqlexample MERGE  INTO target_table USING source_table   ON target_table.id = source_table.id   WHEN MATCHED THEN     UPDATE SET target_table.description =       source_table.description;``` | ```java import java.util.HashMap; import java.util.Map;  Map<String, Column> assignments = new HashMap<>(); assignments.put("description", source.col("description")); MergeResult mergeResult =   target.merge(source, target.col("id").equal_to(source.col("id")))   .whenMatched.updateColumn(assignments)   .collect();``` |

## Working with stages

For more information on working with stages, see [Working With Files in a Stage](working-with-dataframes.md).

### Uploading and Downloading Files from a Stage

To upload and download files from a stage, use [FileOperation](../reference/java/com/snowflake/snowpark_java/FileOperation.md). See [Uploading and Downloading Files in a Stage](working-with-dataframes.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample PUT file:///tmp/*.csv @myStage OVERWRITE = TRUE;``` | ```java import java.util.HashMap; import java.util.Map; ... Map<String, String> putOptions = new HashMap<>();  putOptions.put("OVERWRITE", "TRUE");  PutResult[] putResults = session.file().put(   "file:///tmp/*.csv", "@myStage", putOptions);  for (PutResult result : putResults) {   System.out.println(result.getSourceFileName() + ": " + result.getStatus()); }``` |
| ```sqlexample GET @myStage file:///tmp PATTERN = '.*.csv.gz';``` | ```java import java.util.HashMap; import java.util.Map; ... Map<String, String> getOptions = new HashMap<>();  getOptions.put("PATTERN", "'.*.csv.gz'");  GetResult[] getResults = session.file().get( "@myStage", "file:///tmp", getOptions);  for (GetResult result : getResults) {   System.out.println(result.getFileName() + ": " + result.getStatus()); }``` |

### Reading data from files in a stage

To read data from files in a stage, use [DataFrameReader](../reference/java/com/snowflake/snowpark_java/DataFrameReader.md) to create a DataFrame for the data. See
[Setting Up a DataFrame for Files in a Stage](working-with-dataframes.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample CREATE FILE FORMAT snowpark_temp_format TYPE = JSON;  SELECT "$1"[0]['salesperson']['name'] FROM (   SELECT $1::VARIANT AS "$1" FROM @mystage/car_sales.json(     FILE_FORMAT => 'snowpark_temp_format')) LIMIT 10;  DROP FILE FORMAT snowpark_temp_format;``` | ```java DataFrame df = session.read().json(   "@mystage/car_sales.json").select(     Functions.col("$1").subField(0).subField("salesperson").subField("name"));  df.show();``` |

### Copying data from files in a stage to a table

To copy data from files in a stage to a table, use [DataFrameReader](../reference/java/com/snowflake/snowpark_java/DataFrameReader.md) to create a [CopyableDataFrame](../reference/java/com/snowflake/snowpark_java/CopyableDataFrame.md) for the data, and use the
[copyInto](../reference/java/com/snowflake/snowpark_java/CopyableDataFrame.md) method to copy the data to the table. See [Copying Data from Files into a Table](working-with-dataframes.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample COPY INTO new_car_sales   FROM @mystage/car_sales.json   FILE_FORMAT = (TYPE = JSON);``` | ```java CopyableDataFrame dfCopyableDf = session.read().json("@mystage/car_sales.json"); dfCopyableDf.copyInto("new_car_sales");``` |

### Saving a DataFrame to files on a stage

To save a DataFrame to files on a stage, use the [DataFrameWriter](../reference/java/com/snowflake/snowpark_java/DataFrameWriter.md) method named after the format of the files that you want to
use. See [Saving a DataFrame to Files on a Stage](working-with-dataframes.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample COPY INTO @mystage/saved_data.json   FROM (  SELECT  *  FROM (car_sales) )   FILE_FORMAT = ( TYPE = JSON COMPRESSION = 'none' )   OVERWRITE = TRUE   DETAILED_OUTPUT = TRUE``` | ```java DataFrame df = session.table("car_sales");  WriteFileResult writeFileResult = df.write().mode(   SaveMode.Overwrite).option(   "DETAILED_OUTPUT", "TRUE").option(   "compression", "none").json(   "@mystage/saved_data.json");``` |

## Creating and calling user-defined functions (UDFs)

To create an anonymous UDF, use [Functions.udf](../reference/java/com/snowflake/snowpark_java/Functions.md).

To create a temporary or permanent UDF that you can call by name, use [UDFRegistration.registerTemporary](../reference/java/com/snowflake/snowpark_java/UDFRegistration.md) or
[UDFRegistration.registerPermanent](../reference/java/com/snowflake/snowpark_java/UDFRegistration.md).

To call a permanent UDF by name, use [Functions.callUDF](../reference/java/com/snowflake/snowpark_java/Functions.md).

For details, see [Creating User-Defined Functions (UDFs) for DataFrames in Java](creating-udfs.md) and [Calling scalar user-defined functions (UDFs)](calling-functions.md).

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample CREATE FUNCTION <temp_function_name>   RETURNS INT   LANGUAGE JAVA   ...   AS   ...;  SELECT ...,   <temp_function_name>(quantity) AS doublenum   FROM sample_product_data;``` | ```java UserDefinedFunction doubleUdf =   Functions.udf(     (Integer x) -> x + x,     DataTypes.IntegerType,     DataTypes.IntegerType);  DataFrame df = session.table("sample_product_data");  DataFrame dfWithDoubleNum =   df.withColumn("doubleNum",     doubleUdf.apply(Functions.col("quantity")));  dfWithDoubleNum.show();``` |
| ```sqlexample CREATE FUNCTION <temp_function_name>   RETURNS INT   LANGUAGE JAVA   ...   AS   ...;  SELECT ...,   <temp_function_name>(quantity) AS doublenum   FROM sample_product_data;``` | ```java UserDefinedFunction doubleUdf =   session     .udf()     .registerTemporary(       "doubleUdf",       (Integer x) -> x + x,       DataTypes.IntegerType,       DataTypes.IntegerType);  DataFrame df = session.table("sample_product_data");  DataFrame dfWithDoubleNum =   df.withColumn("doubleNum",     Functions.callUDF("doubleUdf", Functions.col("quantity"))); dfWithDoubleNum.show();``` |
| ```sqlexample CREATE FUNCTION doubleUdf(arg1 INT)   RETURNS INT   LANGUAGE JAVA   ...   AS   ...;  SELECT ...,   doubleUdf(quantity) AS doublenum   FROM sample_product_data;``` | ```java UserDefinedFunction doubleUdf =   session     .udf()     .registerPermanent(       "doubleUdf",       (Integer x) -> x + x,       DataTypes.IntegerType,       DataTypes.IntegerType,       "mystage");  DataFrame df = session.table("sample_product_data");  DataFrame dfWithDoubleNum =   df.withColumn("doubleNum",     Functions.callUDF("doubleUdf", Functions.col("quantity"))); dfWithDoubleNum.show();``` |

## Creating and calling stored procedures

For a guide on creating stored procedures with Snowpark, see [Creating stored procedures for DataFrames in Java](creating-sprocs.md).

* To create an anonymous or named temporary procedure, use a `registerTemporary` method of [com.snowflake.snowpark_java.SProcRegistration](../reference/java/com/snowflake/snowpark_java/SProcRegistration.md).
* To create a named permanent procedure, use a `registerPermanent` method of the [com.snowflake.snowpark_java.SProcRegistration](../reference/java/com/snowflake/snowpark_java/SProcRegistration.md) class.
* To call a procedure, use the `storedProcedure` method of the [com.snowflake.snowpark_java.Session](../reference/java/com/snowflake/snowpark_java/Session.md) class.

| Example of a SQL Statement | Example of Snowpark Code |
| --- | --- |
| ```sqlexample CREATE PROCEDURE <temp_procedure_name>(x INTEGER, y INTEGER)   RETURNS INTEGER   LANGUAGE JAVA   ...   AS   $$   BEGIN     RETURN x + y;   END   $$   ;  CALL <temp_procedure_name>(2, 3);``` | ```java StoredProcedure sp =   session.sproc().registerTemporary((Session session, Integer x, Integer y) -> x + y,     new DataType[] {DataTypes.IntegerType, DataTypes.IntegerType},     DataTypes.IntegerType);    session.storedProcedure(sp, 2, 3).show();``` |
| ```sqlexample CREATE PROCEDURE sproc(x INTEGER, y INTEGER)   RETURNS INTEGER   LANGUAGE JAVA   ...   AS   $$   BEGIN    RETURN x + y;   END   $$   ;  CALL sproc(2, 3);``` | ```java String name = "sproc";  StoredProcedure sp =   session.sproc().registerTemporary(name,     (Session session, Integer x, Integer y) -> x + y,     new DataType[] {DataTypes.IntegerType, DataTypes.IntegerType},     DataTypes.IntegerType);    session.storedProcedure(name, 2, 3).show();``` |
| ```sqlexample CREATE PROCEDURE add_hundred(x INTEGER)   RETURNS INTEGER   LANGUAGE JAVA   ...   AS   $$   BEGIN    RETURN x + 100;   END   $$   ;  CALL add_hundred(3);``` | ```java String name = "add_hundred"; String stageName = "sproc_libs";  StoredProcedure sp =   session.sproc().registerPermanent(     name,     (Session session, Integer x) -> x + 100,     DataTypes.IntegerType,     DataTypes.IntegerType,     stageName,     true);    session.storedProcedure(name, 3).show();``` |
