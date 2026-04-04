# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/functional-difference/bigqueryFDM.md

# SnowConvert AI - BigQuery Functional Differences

> **Note:**
>
> **Conversion Scope**
>
> SnowConvert AI for Google BigQuery currently supports assessment and translation for TABLES and VIEWS. Although SnowConvert AI can recognize other types of statements, they are not fully supported.

## SSC-FDM-BQ0001

Accessing arrays produces NULL instead of an error for positive out of bounds indexes in Snowflake.

### Description

When accessing an ARRAY object by index in Snowflake, specifying an index greater than the size of the array will result in a NULL value, this differs with the behavior of BigQuery, where accessing an ARRAY with an index that is out of bounds will produce an error, unless the functions `SAFE_OFFSET` or `SAFE_ORDINAL` are used.

This FDM is added to any ARRAY access that is not safe.

#### Code Example

##### Input Code

##### BigQuery

```sql
 SELECT ([40, 12, 30])[8];

SELECT ([40, 12, 30])[SAFE_OFFSET(8)];
```

##### Generated Code

##### Snowflake

```sql
 SELECT
--** SSC-FDM-BQ0001 - ACCESSING ARRAYS PRODUCES NULL INSTEAD OF AN ERROR FOR POSITIVE OUT OF BOUNDS INDEXES IN SNOWFLAKE **
([40, 12, 30])[8];

SELECT
PUBLIC.SAFE_OFFSET_UDF( ([40, 12, 30]), 8);
```

#### Best Practices

* Analyze the uses of array access in the code. If there was never the risk of getting an out of bounds error in the original code, no difference will be observed and this FDM can be safely ignored.
* If the original code relies on out-of-bounds access raising an error (e.g., for flow control), add explicit bounds checking in Snowflake using `ARRAY_SIZE` before accessing the array.

## SSC-FDM-BQ0002

Exception system variables are not supported in Snowflake.

### Description

BigQuery’s [exception system variables](https://cloud.google.com/bigquery/docs/reference/standard-sql/procedural-language#beginexceptionend) (`@@error.message`, `@@error.stack_trace`, `@@error.statement_text`, `@@error.formatted_stack_trace`) have no direct equivalent in Snowflake. SnowConvert AI replaces exception variable references with `OBJECT_CONSTRUCT('SQLERRM', SQLERRM, 'SQLCODE', SQLCODE, 'SQLSTATE', SQLSTATE)` as a workaround. This workaround provides basic error information but does not include stack trace or statement text details available in BigQuery. For more information, see [Handling Exceptions in Snowflake](../../../../../../developer-guide/snowflake-scripting/exceptions.md).

#### Code Example

##### Input Code

##### BigQuery

```sql
 CREATE OR REPLACE PROCEDURE test.proc1()
BEGIN
  SELECT 1/0;
EXCEPTION WHEN ERROR THEN
  SELECT
    @@error.message as message,
    @@error.stack_trace as stack_trace,
    @@error.statement_text as statement_text,
    @@error.formatted_stack_trace as formatted_stack_trace;
END;
```

##### Result

```json
 [{
  "message": "Query error: division by zero: 1 / 0 at [snowflake-snowconvert-team.test.proc1:2:3]",
  "stack_trace": [{
    "line": "2",
    "column": "3",
    "filename": null,
    "location": "snowflake-snowconvert-team.test.proc1"
  }, {
    "line": "1",
    "column": "1",
    "filename": null,
    "location": null
  }],
  "statement_text": "SELECT 1/0",
  "formatted_stack_trace": "At snowflake-snowconvert-team.test.proc1[2:3]\nAt [1:1]\n"
}]
```

##### Generated Code

##### Snowflake

```sql
 CREATE OR REPLACE PROCEDURE test.proc1 ()
RETURNS VARCHAR
LANGUAGE SQL
EXECUTE AS CALLER
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "bigquery",  "convertedOn": "04/09/2025",  "domain": "test" }}'
AS
$$
    BEGIN
    SELECT 1/0;
  EXCEPTION WHEN OTHER THEN
--      --** SSC-FDM-BQ0002 - EXCEPTION SYSTEM VARIABLES ARE NOT SUPPORTED IN SNOWFLAKE. **
--    SELECT
--      @@error.message as message,
--      @@error.stack_trace as stack_trace,
--      @@error.statement_text as statement_text,
--      @@error.formatted_stack_trace as formatted_stack_trace;
      RETURN OBJECT_CONSTRUCT('SQLERRM', SQLERRM, 'SQLCODE', SQLCODE, 'SQLSTATE', SQLSTATE);
    END;
$$;
```

##### Result

```json
 {
  "SQLCODE": 100051,
  "SQLERRM": "Division by zero",
  "SQLSTATE": "22012"
}
```

#### Best Practices

* Snowflake provides three built-in exception variables as an alternative to BigQuery’s `@@error` system variables:

  | BigQuery Variable | Snowflake Equivalent | Notes |
  | --- | --- | --- |
  | `@@error.message` | `SQLERRM` | Error message text |
  | `@@error.statement_text` | N/A | No direct equivalent in Snowflake |
  | `@@error.stack_trace` | N/A | No direct equivalent in Snowflake |
  | `@@error.formatted_stack_trace` | N/A | No direct equivalent in Snowflake |
  | N/A | `SQLSTATE` | 5-character ANSI SQL state code |
  | N/A | `SQLCODE` | 5-digit signed integer error code |

* Review the generated `OBJECT_CONSTRUCT('SQLERRM', SQLERRM, 'SQLCODE', SQLCODE, 'SQLSTATE', SQLSTATE)` workaround and adjust it based on your specific error-handling requirements.
* For more information, see [Handling Exceptions in Snowflake](../../../../../../developer-guide/snowflake-scripting/exceptions.md).

## SSC-FDM-BQ0003

Unable to generate correct return table clause due to missing dependent object information.

> **Note:**
>
> This issue is deprecated and no longer generated by SnowConvert AI. Check [SSC-EWI-BQ0009](../conversion-issues/bigqueryEWI.md) for the issue now generated for this scenario

### Description

Snowflake requires a valid RETURNS TABLE clause for CREATE TABLE FUNCTION statements.

If the original BigQuery source code does not have a RETURNS TABLE clause, SnowConvert AI must build one. To do this, an analysis is made to the CREATE TABLE FUNCTION query to properly infer the types of the columns of the resulting table. When SnowConvert AI cannot gather the required information, this EWI is added.

#### Code Example

##### Input Code

##### BigQuery

```sql
 CREATE OR REPLACE TABLE FUNCTION function_name_noreturns_asterisk_join (parameter_name INTEGER)
AS
  SELECT *
  FROM unknownTable1 t1
  JOIN unknownTable2 t2 ON t1.col1 = t2.fk_col1;
```

##### Generated Code

##### Snowflake

```sql
 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECTS "unknownTable1", "unknownTable2" **

CREATE OR REPLACE FUNCTION function_name_noreturns_asterisk_join (parameter_name INTEGER)
----** SSC-FDM-BQ0003 - UNABLE TO GENERATE CORRECT RETURNS TABLE CLAUSE DUE TO MISSING DEPENDENT OBJECT INFORMATION. **
--RETURNS TABLE (
--)
AS
    $$
      SELECT *
      FROM
      unknownTable1 t1
      JOIN
          unknownTable2 t2 ON t1.col1 = t2.fk_col1
    $$;
```

#### Best Practices

* Always try to include any dependent object definitions in the input code, so that SnowConvert AI has access to important information.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-BQ0004

The INFER_SCHEMA function requires a file path without wildcards to generate the table template, replace the FILE_PATH placeholder with it

> **Warning:**
>
> This FDM is deprecated; please refer to [SSC-FDM-0035](generalFDM.md) for the latest version of this FDM.

### Description

The [INFER_SCHEMA](https://docs.snowflake.com/en/sql-reference/functions/infer_schema) function is used in Snowflake to generate the columns definition of a table based on the structure of a file, it requires a LOCATION parameter that specifies the path to a file or folder that will be used to construct the table columns, however, this path does not support regex, meaning that the wildcard `*` character is not supported.

When the table has no columns, SnowConvert AI will check all URIS to find one that does not use wildcards and use it in the INFER_SCHEMA function. When no URI meets such criteria, this FDM and a FILE_PATH placeholder is generated, and the placeholder has to be replaced with the path of one of the files referenced by the external table to generate the table columns.

#### Code Example

##### Input Code

##### BigQuery

```sql
 CREATE OR REPLACE EXTERNAL TABLE test.my_external_table_json2
OPTIONS(
  FORMAT='JSON',
  URIS=['gs://sc_external_table_bucket/folder_with_json/*']
);
```

##### Generated Code

##### Snowflake

```sql
 CREATE OR REPLACE TEMPORARY FILE FORMAT SC_TEST_MY_EXTERNAL_TABLE_JSON2_FORMAT
TYPE = JSON;

CREATE OR REPLACE EXTERNAL TABLE test.my_external_table_json2 USING TEMPLATE (
SELECT
  ARRAY_AGG(OBJECT_CONSTRUCT('COLUMN_NAME', COLUMN_NAME, 'TYPE', TYPE, 'NULLABLE', NULLABLE, 'EXPRESSION', EXPRESSION))
FROM
  --** SSC-FDM-BQ0004 - THE INFER_SCHEMA FUNCTION REQUIRES A FILE PATH WITHOUT WILDCARDS TO GENERATE THE TABLE TEMPLATE, REPLACE THE FILE_PATH PLACEHOLDER WITH IT **
  TABLE(INFER_SCHEMA(LOCATION => '@EXTERNAL_STAGE/FILE_PATH', FILE_FORMAT => 'SC_TEST_MY_EXTERNAL_TABLE_JSON2_FORMAT'))
)
!!!RESOLVE EWI!!! /*** SSC-EWI-BQ0015 - EXTERNAL TABLE REQUIRES AN EXTERNAL STAGE TO ACCESS gs://sc_external_table_bucket, DEFINE AND REPLACE THE EXTERNAL_STAGE PLACEHOLDER ***/!!!
LOCATION = @EXTERNAL_STAGE
AUTO_REFRESH = false
PATTERN = 'folder_with_json/.*'
FILE_FORMAT = (TYPE = JSON);
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-BQ0005

Parsing the CSV header is not supported in external tables, columns must be renamed to match the original names

### Description

Snowflake external tables do not support parsing the header of CSV files. SKIP_HEADER is used as a workaround to avoid runtime errors, but the resulting table column names will have auto-generated names (`c1`, `c2`, …, `cN`) instead of the original header names.

When SnowConvert AI detects an external table with CSV file format and no explicit column list, it adds the `SKIP_HEADER = 1` file format option. The columns must be manually renamed to match the original names from the CSV header.

#### Code Example

##### Input Code

##### BigQuery

```sql
 CREATE OR REPLACE EXTERNAL TABLE test.my_external_table_csv
OPTIONS(
  FORMAT='CSV',
  URIS=['gs://sc_external_table_bucket/folder_with_csv/Employees.csv']
);
```

##### Generated Code

##### Snowflake

```sql
 CREATE OR REPLACE TEMPORARY FILE FORMAT SC_TEST_MY_EXTERNAL_TABLE_CSV_FORMAT
TYPE = CSV
SKIP_HEADER = 1;

CREATE OR REPLACE EXTERNAL TABLE test.my_external_table_csv
--** SSC-FDM-BQ0005 - PARSING THE CSV HEADER IS NOT SUPPORTED IN EXTERNAL TABLES, COLUMNS MUST BE RENAMED TO MATCH THE ORIGINAL NAMES **
USING TEMPLATE (
SELECT
  ARRAY_AGG(OBJECT_CONSTRUCT('COLUMN_NAME', COLUMN_NAME, 'TYPE', TYPE, 'NULLABLE', NULLABLE, 'EXPRESSION', EXPRESSION))
FROM
  TABLE(INFER_SCHEMA(LOCATION => '@EXTERNAL_STAGE/folder_with_csv/Employees.csv', FILE_FORMAT => 'SC_TEST_MY_EXTERNAL_TABLE_CSV_FORMAT'))
)
!!!RESOLVE EWI!!! /*** SSC-EWI-0032 - EXTERNAL TABLE REQUIRES AN EXTERNAL STAGE TO ACCESS gs://sc_external_table_bucket, DEFINE AND REPLACE THE EXTERNAL_STAGE PLACEHOLDER ***/!!!
LOCATION = @EXTERNAL_STAGE
AUTO_REFRESH = false
PATTERN = 'folder_with_csv/Employees.csv'
FILE_FORMAT = (TYPE = CSV SKIP_HEADER = 1);
```

#### Best Practices

* Rename the auto-generated column names (`c1`, `c2`, …, `cN`) back to the original column names from the CSV file header.
* If the original column names are known, use `ALTER TABLE ... RENAME COLUMN` or recreate the external table with explicit column definitions.
* For non-external-table loading scenarios, consider using `MATCH_BY_COLUMN_NAME` with `PARSE_HEADER = TRUE` in the file format to automatically match columns by header names.

## SSC-FDM-BQ0006

Reading from Google Drive is not supported in Snowflake, upload the files to the external location and replace the FILE_PATH placeholders

### Description

Snowflake does not support reading data from files hosted in Google Drive, this FDM is generated to notify it, please upload the Google Drive files to the external location so they can be accessed through the external stage.

The PATTERN clause will hold autogenerated placeholders FILE_PATH0, FILE_PATH1, …, FILE_PATHN that should be replaced with the file/folder path after the files were moved to the external location.

#### Code Example

##### Input Code

##### BigQuery

```sql
 CREATE OR REPLACE EXTERNAL TABLE test.my_external_table_drive_test
OPTIONS(
  FORMAT='JSON',
  URIS=['https://drive.google.com/open?id=someFileId']
);
```

##### Generated Code

##### Snowflake

```sql
 CREATE OR REPLACE TEMPORARY FILE FORMAT SC_TEST_MY_EXTERNAL_TABLE_DRIVE_TEST_FORMAT
TYPE = JSON;

CREATE OR REPLACE EXTERNAL TABLE test.my_external_table_drive_test USING TEMPLATE (
SELECT
  ARRAY_AGG(OBJECT_CONSTRUCT('COLUMN_NAME', COLUMN_NAME, 'TYPE', TYPE, 'NULLABLE', NULLABLE, 'EXPRESSION', EXPRESSION))
FROM
  --** SSC-FDM-0035 - THE INFER_SCHEMA FUNCTION REQUIRES A FILE PATH WITHOUT WILDCARDS TO GENERATE THE TABLE TEMPLATE, REPLACE THE FILE_PATH PLACEHOLDER WITH IT **
  TABLE(INFER_SCHEMA(LOCATION => '@EXTERNAL_STAGE/FILE_PATH', FILE_FORMAT => 'SC_TEST_MY_EXTERNAL_TABLE_DRIVE_TEST_FORMAT'))
)
!!!RESOLVE EWI!!! /*** SSC-EWI-0032 - EXTERNAL TABLE REQUIRES AN EXTERNAL STAGE TO ACCESS AN EXTERNAL LOCATION, DEFINE AND REPLACE THE EXTERNAL_STAGE PLACEHOLDER ***/!!!
LOCATION = @EXTERNAL_STAGE
AUTO_REFRESH = false
--** SSC-FDM-BQ0006 - READING FROM GOOGLE DRIVE IS NOT SUPPORTED IN SNOWFLAKE, UPLOAD THE FILES TO THE EXTERNAL LOCATION AND REPLACE THE FILE_PATH PLACEHOLDERS **
PATTERN = 'FILE_PATH0'
FILE_FORMAT = (TYPE = JSON);
```

#### Best Practices

* Download the files from Google Drive and upload them to a cloud storage location accessible by Snowflake (e.g., Amazon S3, Azure Blob Storage, or Google Cloud Storage).
* Create or configure an external stage in Snowflake pointing to the cloud storage location.
* Replace the `FILE_PATH` placeholders in the `PATTERN` clause with the actual file or folder paths relative to the external stage.

## SSC-FDM-BQ0007

The GOOGLE_SHEETS format is not supported in Snowflake. CSV file type is used as a workaround.

### Description

The GOOGLE_SHEETS format is not supported in Snowflake. CSV file type is used as a workaround because the structure of Google Sheets data is similar to CSV.

When SnowConvert AI detects an external table using the GOOGLE_SHEETS format, it produces an external table with the CSV file format instead. The resulting table expects a CSV file rather than a Google Sheets source.

#### Code Example

##### Input Code

##### BigQuery

```sql
 CREATE OR REPLACE EXTERNAL TABLE test.spreadsheetTable
(
  Name STRING,
  Code INTEGER,
  Price INTEGER,
  Expiration_date DATE
)
OPTIONS(
  format="GOOGLE_SHEETS",
  skip_leading_rows = 1,
  uris=['https://docs.google.com/spreadsheets/d/someFileId/edit?usp=sharing']
);
```

##### Generated Code

##### Snowflake

```sql
--** SSC-FDM-BQ0007 - THE GOOGLE_SHEETS FORMAT IS NOT SUPPORTED IN SNOWFLAKE. CSV FILE TYPE IS USED AS A WORKAROUND. **
CREATE OR REPLACE EXTERNAL TABLE test.spreadsheetTable
(
  Name STRING AS CAST(GET_IGNORE_CASE($1, 'c1') AS STRING),
  Code INTEGER AS CAST(GET_IGNORE_CASE($1, 'c2') AS INTEGER),
  Price INTEGER AS CAST(GET_IGNORE_CASE($1, 'c3') AS INTEGER),
  Expiration_date DATE AS CAST(GET_IGNORE_CASE($1, 'c4') AS DATE)
)
!!!RESOLVE EWI!!! /*** SSC-EWI-0032 - EXTERNAL TABLE REQUIRES AN EXTERNAL STAGE TO ACCESS AN EXTERNAL LOCATION, DEFINE AND REPLACE THE EXTERNAL_STAGE PLACEHOLDER ***/!!!
LOCATION = @EXTERNAL_STAGE
AUTO_REFRESH = false
--** SSC-FDM-BQ0006 - READING FROM GOOGLE DRIVE IS NOT SUPPORTED IN SNOWFLAKE, UPLOAD THE FILES TO THE EXTERNAL LOCATION AND REPLACE THE FILE_PATH PLACEHOLDERS **
PATTERN = 'FILE_PATH0'
FILE_FORMAT = (TYPE = CSV SKIP_HEADER = 1)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "bigquery",  "convertedOn": "07/16/2025",  "domain": "no-domain-provided" }}';
```

#### Best Practices

* Export the Google Sheets data as CSV files and upload them to a cloud storage location accessible by Snowflake.
* Verify that the CSV export preserves the expected data types and formatting, especially for dates, numbers, and text fields with commas.
* If the external table also references Google Drive URIs, see SSC-FDM-BQ0006 for instructions on migrating the files to an external stage.

## SSC-FDM-BQ0008

Where clause references a column of STRUCT type. Comparison operations may produce different results in Snowflake.

### Description

BigQuery STRUCT types have no direct equivalent in Snowflake. VARIANT is used as a workaround (see [SSC-FDM-0034](generalFDM.md)). When a comparison involves a Snowflake VARIANT created from a BigQuery STRUCT, the results may differ because Snowflake compares both keys and values, whereas BigQuery compares only values regardless of field names.

This FDM is added when a WHERE clause comparison involves a column of STRUCT type that was converted to VARIANT.

#### Code Example

##### Input Code

##### BigQuery

```sql
 CREATE OR REPLACE TABLE test.compExprTable
(
  COL1 STRUCT<sc1 INT64>,
  COL2 STRUCT<sc2 INT64>
);

SELECT * FROM test.compExprTable WHERE COL1 <> (COL2);
```

##### Output Code

##### Snowflake

```sql
 CREATE OR REPLACE TABLE test.compExprTable
(
  COL1 VARIANT /*** SSC-FDM-0034 - STRUCT<INT64> CONVERTED TO VARIANT. SOME OF ITS USAGES MIGHT HAVE FUNCTIONAL DIFFERENCES. ***/,
  COL2 VARIANT /*** SSC-FDM-0034 - STRUCT<INT64> CONVERTED TO VARIANT. SOME OF ITS USAGES MIGHT HAVE FUNCTIONAL DIFFERENCES. ***/
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "bigquery",  "convertedOn": "07/02/2025",  "domain": "no-domain-provided" }}';

SELECT * FROM
  test.compExprTable
--** SSC-FDM-BQ0008 - WHERE CLAUSE REFERENCES A COLUMN OF STRUCT TYPE. COMPARISON OPERATIONS MAY PRODUCE DIFFERENT RESULTS IN SNOWFLAKE. **
WHERE COL1 <> (COL2);
```

#### Best Practices

* Review WHERE clause comparisons involving STRUCT-derived VARIANT columns. If the original BigQuery query compared STRUCTs by value only, extract and compare individual fields explicitly in Snowflake.
* For example, replace `WHERE col1 <> col2` with `WHERE col1:sc1 <> col2:sc2` to compare specific field values instead of the entire VARIANT object.
* For more information on VARIANT comparison behavior, see the [Snowflake VARIANT documentation](https://docs.snowflake.com/en/sql-reference/data-types-semistructured).

## SSC-FDM-BQ0010

Geography function is not required in Snowflake.

### Description

Snowflake automatically detects GEOGRAPHY data from [WGS 84](https://spatialreference.org/ref/epsg/wgs-84/) formatted strings (WKT, WKB, GeoJSON), so explicit geography conversion functions like `ST_GEOGFROMTEXT` are not required in VALUES clause inserts. SnowConvert AI removes the function call and passes the string literal directly. This FDM is added to notify that the geography function was removed.

#### Code Example

##### Input Code

##### BigQuery

```sql
 CREATE OR REPLACE TABLE test.geographyType
(
  COL1 GEOGRAPHY
);

INSERT INTO test.geographyType VALUES
(ST_GEOGFROMTEXT('POINT(-122.35 37.55)')),
(ST_GEOGFROMTEXT('LINESTRING(-124.20 42.00, -120.01 41.99)'));

SELECT * FROM test.geographyType;
```

##### Output Code

##### Snowflake

```sql
 CREATE OR REPLACE TABLE test.geographyType
(
  COL1 GEOGRAPHY
);

INSERT INTO test.geographyType
VALUES
    (
     --** SSC-FDM-BQ0010 - THE FUNCTION 'ST_GEOGFROMTEXT' IS NOT REQUIRED IN SNOWFLAKE. **
     'POINT(-122.35 37.55)'), (
     --** SSC-FDM-BQ0010 - THE FUNCTION 'ST_GEOGFROMTEXT' IS NOT REQUIRED IN SNOWFLAKE. **
     'LINESTRING(-124.20 42.00, -120.01 41.99)');

ALTER SESSION SET GEOGRAPHY_OUTPUT_FORMAT = 'WKT';
SELECT * FROM
test.geographyType;
```

#### Best Practices

* This FDM can be safely ignored in most cases. Snowflake natively supports GEOGRAPHY data from WKT, WKB, and GeoJSON string formats without requiring explicit conversion functions.
* If the removed function performed validation or transformation beyond simple type casting, verify that the inserted data is valid GEOGRAPHY data in Snowflake.
* For more information, see the [Snowflake GEOGRAPHY data type documentation](https://docs.snowflake.com/en/sql-reference/data-types-geospatial).

## SSC-FDM-BQ0011

Named parameters in this script were transformed to Snowflake CLI variables.

### Description

BigQuery supports named parameters using the `@parameter_name` syntax in queries. SnowConvert AI transforms these named parameters to Snowflake CLI variables using the `<% parameter_name %>` syntax.

To execute the transformed `.sql` scripts containing named parameters, use Snowflake CLI with variable substitution.

For more information on how to set up and use Snowflake CLI, see [What is Snowflake CLI?](../../../../../../developer-guide/snowflake-cli/index.md)

#### Code Example

##### Input Code

##### BigQuery

```sql
SELECT column1 FROM test.parametersExample WHERE column2 = @searchValue;
```

##### Example execution (using the bq query command)

```bash
bq query \
  --use_legacy_sql=false \
  --parameter=searchValue:Int64:80 \
  'SELECT column1 FROM test.parametersExample WHERE column2 = @searchValue'
```

##### Output Code

##### Snowflake

```sql
--** SSC-FDM-BQ0011 - NAMED PARAMETERS IN THIS SCRIPT WERE TRANSFORMED TO SNOWFLAKE CLI VARIABLES. **
SELECT column1 FROM
test.parametersExample
WHERE column2 = <% searchValue %>;
```

##### Example execution (Snowflake CLI)

```bash
snow sql -f output_file_path -D "searchValue=80"
```

### Best Practices

* Install and configure [Snowflake CLI](../../../../../../developer-guide/snowflake-cli/index.md) to execute the transformed scripts with variable substitution using the `-D` flag (e.g., `snow sql -f script.sql -D "param=value"`).
* Review each transformed `<% parameter_name %>` variable to ensure the parameter name and intended value match the original BigQuery `@parameter_name` usage.
* If the transformed script will be executed outside of Snowflake CLI (e.g., in a Snowflake worksheet), replace `<% parameter_name %>` variables with literal values or session variables as appropriate.

## SSC-FDM-BQ0012

Select \* with multiple UNNEST operators will produce column ambiguity in Snowflake

### Description

As part of the SnowConvert transformation for the UNNEST operator, the [FLATTEN](../../../../../../sql-reference/functions/flatten.md) function is used, this function generates multiple columns not required to emulate the UNNEST operator functionality like the `THIS` or `PATH` columns.

When a SELECT \* with the UNNEST operator is found, SnowConvert will remove the unnecessary columns using the `EXCLUDE` keyword, however, when multiple UNNEST operators are used in the same statement, the columns can not be removed due to ambiguity problems, this FDM will be generated to mark these cases.

It is recommended to expand the SELECT expression list in order to specify only the expected columns and solve this issue.

#### Code Example

##### Input Code

##### BigQuery

```sql
SELECT * FROM UNNEST ([10,20,30]);

SELECT * FROM UNNEST ([10,20,30]) AS numbers, UNNEST(['Hi', 'Hello', 'Bye']) AS words;
```

##### Generated Code

##### Snowflake

```sql
SELECT
* EXCLUDE(SEQ, KEY, PATH, THIS, INDEX)
FROM
TABLE(FLATTEN(INPUT => [10,20,30])) AS F0_ (
SEQ,
KEY,
PATH,
INDEX,
F0_,
THIS
);

SELECT
--** SSC-FDM-BQ0012 - SELECT * WITH MULTIPLE UNNEST OPERATORS WILL RESULT IN COLUMN AMBIGUITY IN SNOWFLAKE **
 * FROM
TABLE(FLATTEN(INPUT => [10,20,30])) AS numbers (
SEQ,
KEY,
PATH,
INDEX,
numbers,
THIS
),
TABLE(FLATTEN(INPUT => ['Hi', 'Hello', 'Bye'])) AS words (
SEQ,
KEY,
PATH,
INDEX,
words,
THIS
);
```

#### Recommendations

1. **Expand the SELECT list:** Replace `SELECT *` with an explicit column list specifying only the columns you need from each UNNEST/FLATTEN result. This eliminates the ambiguity caused by duplicate metadata columns.
2. **Use table aliases:** Qualify each column reference with the corresponding table alias to avoid ambiguity between the FLATTEN results.
