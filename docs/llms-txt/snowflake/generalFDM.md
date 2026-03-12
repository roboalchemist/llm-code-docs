# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/functional-difference/generalFDM.md

# SnowConvert AI - General Functional Differences

## SSC-FDM-0001

Views selecting all columns from a single table are not required in Snowflake

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

Views that only select all columns of a single table and do not have any filtering clauses are not required in Snowflake and may affect performance.

#### Code Example

##### Input Code (Oracle)

```sql
 CREATE OR REPLACE VIEW simpleView1
AS
SELECT
*
FROM
simpleTable;

CREATE OR REPLACE VIEW simpleView2
AS
SELECT
*
FROM
simpleTable GROUP BY col1;
```

##### Generated Code

```sql
 CREATE OR REPLACE VIEW simpleView1
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
AS
--** SSC-FDM-0001 - VIEWS SELECTING ALL COLUMNS FROM A SINGLE TABLE ARE NOT REQUIRED IN SNOWFLAKE AND MAY IMPACT PERFORMANCE. **
SELECT
*
FROM
simpleTable;

CREATE OR REPLACE VIEW simpleView2
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
AS
--** SSC-FDM-0001 - VIEWS SELECTING ALL COLUMNS FROM A SINGLE TABLE ARE NOT REQUIRED IN SNOWFLAKE AND MAY IMPACT PERFORMANCE. **
SELECT
*
FROM
simpleTable
GROUP BY col1;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0002

Correlated Subquery May Have Functional Differences

### Description

This message is reported when a `Correlated Subquery` (subquery that refers to a column from the outer query) is located. This type of subqueries can, in some cases, present some functional differences in Snowflake ([Working with Subqueries](https://docs.snowflake.com/en/user-guide/querying-subqueries#correlated-vs-uncorrelated-subqueries)).

#### Code Example

##### Input Code

```sql
 CREATE TABLE schema1.table1(column1 NVARCHAR(50), column2 NVARCHAR(50));
CREATE TABLE schemaA.tableA(columnA NVARCHAR(50), columnB NVARCHAR(50));

--Correlated Subquery
SELECT columnA FROM schemaA.tableA ta WHERE columnA = (SELECT SUM(column1) FROM schema1.table1 t1 WHERE t1.column1 = ta.columnA);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE schema1.table1 (
column1 VARCHAR(50),
column2 VARCHAR(50))
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "10/11/2024",  "domain": "test" }}'
;

CREATE OR REPLACE TABLE schemaA.tableA (
columnA VARCHAR(50),
columnB VARCHAR(50))
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "10/11/2024",  "domain": "test" }}'
;

--Correlated Subquery
SELECT
columnA
FROM
schemaA.tableA ta
WHERE
columnA =
          --** SSC-FDM-0002 - CORRELATED SUBQUERIES MAY HAVE SOME FUNCTIONAL DIFFERENCES. **
          (SELECT
          SUM(column1) FROM
          schema1.table1 t1
          WHERE
          t1.column1 = ta.columnA
          );
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0003

Conversion Rate Inconsistency

### Description

This message is reported when a conversion rate inconsistency is found on the assessment field specified. These situations are resolved automatically by SnowConvert AI, so this is just an informative warning.

> **Note:**
>
> This Informative warning will only be visible in the assessment documents and not the output code

#### Best Practices

* Despite SnowConvert AI’s ability to automatically fix the issue, you can still notify the SnowConvert AI support team by emailing [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com) and specifying the issue.

## SSC-FDM-0004

External table translated to regular table

### Description

This warning is added to clauses related to external handling. Snowflake recommends that all data should be managed inside the Snowflake data storage. For more information on this subject, see the [Snowflake data storage considerations](https://docs.snowflake.com/en/user-guide/tables-storage-considerations.html#data-storage-considerations).

#### Code Example

##### Input Code

```sql
 CREATE EXTERNAL TABLE ext_csv_file (
    id INT,
    name TEXT,
    age INT,
    city TEXT
)
LOCATION (
    'gpfdist://192.168.1.100:8080/data/my_data.csv'
)
FORMAT 'CSV' (DELIMITER ',' HEADER);
```

##### Generated Code

```sql
 --** SSC-FDM-0004 - EXTERNAL TABLE TRANSLATED TO REGULAR TABLE **
CREATE TABLE ext_csv_file (
       id INT,
       name TEXT,
       age INT,
       city TEXT
   )
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "greenplum",  "convertedOn": "07/09/2025",  "domain": "no-domain-provided" }}'
;
```

#### Best Practices

* The data stored in files of the external tables must be somehow moved into the Snowflake database.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0005

TIME ZONE not supported for time data type

### Description

The Time data type in Snowflake does not store Timezone values

> TIME internally stores “wallclock” time, and all operations on TIME values are performed without taking any time zone into consideration. For more information, see the [Snowflake TIME data type documentation](https://docs.snowflake.com/en/sql-reference/data-types-datetime#time).

#### Example Code

##### Input Code

```sql
 CREATE TABLE TABLE_TIME_TYPE (
    COLNAME TIME (9) WITH TIME ZONE
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE TABLE_TIME_TYPE (
    COLNAME TIME(9) /*** SSC-FDM-0005 - TIME ZONE NOT SUPPORTED FOR TIME DATA TYPE ***/
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
;
```

#### Best Practices

* No end-user action is required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0006

Number type column may not behave similarly in Snowflake

### Description

This functional difference message appears when a `NUMBER` Type column is being created within a Table. The reason for this is due to arithmetic differences when performing operations related to the scales of intermediate values in Snowflake which could make some operations fail. For more information please refer to [Snowflake’s post on intermediate numbers in Snowflake](https://community.snowflake.com/s/question/0D50Z00008HhSHCSA3/sql-compilation-error-invalid-intermediate-datatype-number7148) and [Number out of representable range](https://community.snowflake.com/s/article/Number-out-of-representable-range-error-occurs-during-the-multiplication-of-numeric-values).

To avoid these arithmetic issues, you can run data samplings to verify the needed precision and scales for these operations.

#### Example Codes

#### Simple Table with Number Columns

##### Input Code (Oracle)

```sql
 CREATE TABLE table1
(
column1 NUMBER,
column2 NUMBER (20, 4)
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE table1
(
column1 NUMBER(38, 18) /*** SSC-FDM-0006 - NUMBER TYPE COLUMN MAY NOT BEHAVE SIMILARLY IN SNOWFLAKE. ***/,
column2 NUMBER(20, 4) /*** SSC-FDM-0006 - NUMBER TYPE COLUMN MAY NOT BEHAVE SIMILARLY IN SNOWFLAKE. ***/
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
;
```

#### Arithmetic Issue Examples

The next examples show how the arithmetic issues can happen when using Number columns:

##### Snowflake Code with Division Error

```sql
 CREATE OR REPLACE TABLE number_table( column1 NUMBER(38, 19) );

INSERT INTO number_table VALUES (1);

SELECT column1 / column1 FROM number_table;
```

##### Snowflake Code with Multiplication Error

```sql
 CREATE OR REPLACE TABLE number_table( column1 NUMBER(38, 20) );

INSERT INTO number_table VALUES (1);

SELECT column1 * column1 FROM number_table;
```

When running either `SELECT` statements Snowflake will return an error:

`Number out of representable range: type FIXEDSB16{nullable}, value 1.0000000000000000000`

This is due to the intermediate operation’s result overflowing Snowflake’s maximum capacity; reducing the number scales by 1 on each example will fix the error and work normally:

##### Snowflake Code with Division

```sql
 CREATE OR REPLACE TABLE number_table( column1 NUMBER(38, 18) );

INSERT INTO number_table VALUES (1);

SELECT column1 / column1 FROM number_table;
```

##### Snowflake Code with Multiplication

```sql
 CREATE OR REPLACE TABLE numbertable( column1 NUMBER(38, 19) );

INSERT INTO number_table VALUES (1);

SELECT column1 * column1 FROM number_table;
```

For this reason, SnowConvert AI sets the default scale of Numbers to 18, minimizing the number of errors when migrating.

#### Best Practices

* Verify that your operations’ intermediate values don’t exceed a scale of 37, as that is Snowflake’s maximum.
* Run Data Samplings on your data, to make sure you have the required precision and scales before running any operations.
* In most cases, after doing some data sampling or discussing with the business you might come to the conclusion that the precision can be different. For example, for `MONEY` columns a typical precision is `NUMBER(20,4)`. In snowflake you cannot easily alter a column data type, you can check this [post on our forum](https://www.mobilize.net/blog/how-to-alter-column-datatype-in-snowflake) which provides some guidance on how to alter your columns data types and preserve your data.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0007

Element with missing dependencies

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons

### Description

There is a missing dependency for an object, Snow Convert could not resolve some data types. Also there exists a possibility to have a deployment error if the dependency was not in the source code.

#### Example Code

##### Input Code

```sql
 CREATE VIEW VIEW01 AS SELECT * FROM TABLE1;
```

##### Generated Code

```sql
 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "TABLE1" **
CREATE OR REPLACE VIEW VIEW01
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
AS
--** SSC-FDM-0001 - VIEWS SELECTING ALL COLUMNS FROM A SINGLE TABLE ARE NOT REQUIRED IN SNOWFLAKE AND MAY IMPACT PERFORMANCE. **
SELECT
* FROM
TABLE1;
```

> **Note:**
>
> Note that the TABLE1 definition is missing.

#### Best Practices

* Make sure all the dependencies of the objects are in the source code.
* If not, find the references to the object in the code and check if the operations are well managed.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0008

On Commit not supported

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

The ON COMMIT clauses in your CREATE TABLE statement have been commented out. Snowflake does not support the ON COMMIT clause, as it’s typically used for temporary tables in other SQL dialects. If you need to manage transaction-specific behavior, consider using Snowflake’s transactions or temporary tables with explicit TRUNCATE or DROP statements instead.

#### Example Code

##### Input Code

```sql
CREATE TEMPORARY TABLE TABLE02 (COLNAME VARCHAR(20)) ON COMMIT DELETE ROWS
```

##### Generated Code

```sql
CREATE OR REPLACE TEMPORARY TABLE TABLE02 (
COLNAME VARCHAR(20))
----** SSC-FDM-0008 - ON COMMIT (DELETE ROWS) IS NOT SUPPORTED **
--ON COMMIT DELETE ROWS
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "09/22/2025",  "domain": "no-domain-provided" }}'
;
```

## SSC-FDM-0009

GLOBAL TEMPORARY TABLE functionality not supported.

### Description

Global temporary tables are considered a complex pattern, due to the fact they can come in several variations, as indicated in [Snowflake’s documentation](https://docs.snowflake.com/en/sql-reference/sql/create-table#variant-syntax).

#### Example Code

##### Input Code

```sql
 CREATE OR REPLACE GLOBAL TEMPORARY TABLE GLOBAL_TEMP_TABLE
(
    col3 INTEGER,
    col4 VARCHAR(50)
);
```

##### Generated Code

```sql
 --** SSC-FDM-0009 - GLOBAL TEMPORARY TABLE FUNCTIONALITY NOT SUPPORTED. **
CREATE OR REPLACE TABLE GLOBAL_TEMP_TABLE
    (
        col3 INTEGER,
        col4 VARCHAR(50)
    )
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0010

Type changed to Date.

### Description

This message is shown when SnowConvert AI finds a DEFAULT SYSDATE and the data type is NOT a DATE or TIMESTAMP datatype. In this case, the data type is changed to DATE.

#### Example Code

##### Input Code

```sql
 CREATE TABLE "SYSDATE_DEFAULT_TEST_TABLE_1"(
 "COLUMN1" VARCHAR2(30 BYTE) DEFAULT SYSDATE
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE "SYSDATE_DEFAULT_TEST_TABLE_1" (
  "COLUMN1" TIMESTAMP DEFAULT CURRENT_TIMESTAMP() /*** SSC-FDM-0010 - CONVERTED FROM VARCHAR2 TO DATE FOR CURRENT_DATE DEFAULT ***/
 )
 COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
 ;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0011

Column Name Is Snowflake Reserved Keyword.

> **Note:**
>
> This FDM is deprecated, please refer to [SSC-EWI-0045](../conversion-issues/generalEWI.md) documentation.

### Description

Column names that are valid for the source language but are reserved keywords in Snowflake.

#### Example Code

##### Input Code (Oracle)

```sql
 CREATE TABLE T1
(
    LOCALTIME VARCHAR,
    CURRENT_USER VARCHAR
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE T1
    (
    --** SSC-FDM-0011 - COLUMN NAME 'LOCALTIME' IS A SNOWFLAKE RESERVED KEYWORD **
    "LOCALTIME" VARCHAR,
    --** SSC-FDM-0011 - COLUMN NAME 'CURRENT_USER' IS A SNOWFLAKE RESERVED KEYWORD **
    "CURRENT_USER" VARCHAR
    )
    COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
    ;
```

#### Best Practices

* Consider renaming the columns that use names that are not supported in Snowflake.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0012

Constraint Name in some constraints is not Supported.

### Description

This message is added when a constraint is of type Null, Not Null, or default and was defined with a name. Snowflake does not support the name in those constraints. For that, SnowConvert AI will remove it and add the comment.

#### Example Code

##### Input Code

```sql
 CREATE TABLE TABLE1 (
COL1 VARCHAR (10) CONSTRAINT constraintName DEFAULT ('0') NOT NULL
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE TABLE1 (
COL1 VARCHAR(10) DEFAULT ('0') /*** SSC-FDM-0012 - CONSTRAINT NAME 'constraintName' IN DEFAULT EXPRESSION CONSTRAINT IS NOT SUPPORTED IN SNOWFLAKE ***/ NOT NULL
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "07/02/2025",  "domain": "no-domain-provided" }}'
;
```

#### Best Practices

* No end-user action is required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0013

Timezone expression could not be mapped

### Description

This FDM message is added to indicate scenarios where the actual value of a timezone expression cannot be determined, and therefore, the translated results might be different. When the timezone value used is a literal string, SnowConvert AI can take it and map it to its corresponding timezone value in Snowflake. However, when this value is specified by an expression, SnowConvert AI cannot get the timezone value that will be used at runtime and, therefore, cannot map this value to its corresponding Snowflake equivalent.

#### Example Code

##### Input Code (Oracle)

```sql
 SELECT TIMESTAMP '1998-12-25 09:26:50.12' AT TIME ZONE SESSIONTIMEZONE FROM DUAL;
SELECT TIMESTAMP '1998-12-25 09:26:50.12' AT TIME ZONE Expression FROM DUAL;
```

##### Generated Code

```sql
 SELECT
--** SSC-FDM-0013 - TIMEZONE EXPRESSION COULD NOT BE MAPPED, RESULTS MAY BE DIFFERENT **
TO_TIMESTAMP_LTZ( TIMESTAMP '1998-12-25 09:26:50.12')
FROM DUAL;

SELECT
--** SSC-FDM-0013 - TIMEZONE EXPRESSION COULD NOT BE MAPPED, RESULTS MAY BE DIFFERENT **
CONVERT_TIMEZONE(Expression, TIMESTAMP '1998-12-25 09:26:50.12')
FROM DUAL;
```

##### Input Code (Teradata)

```sql
 select TIMESTAMP '1998-12-25 09:26:50.12' AT TIME ZONE SESSIONTIMEZONE;
select current_timestamp at time zone CONCAT(' America ', ' Pacific');
select current_timestamp at time zone (SELECT COL1 FROM TABLE1 WHERE COL2 = 2);
```

##### Generated Code

```sql
 SELECT
CONVERT_TIMEZONE(SESSIONTIMEZONE, TIMESTAMP '1998-12-25 09:26:50.12') /*** SSC-FDM-0013 - TIMEZONE EXPRESSION COULD NOT BE MAPPED, RESULTS MAY BE DIFFERENT ***/;

SELECT
CONVERT_TIMEZONE(CONCAT(' America ', ' Pacific'), CURRENT_TIMESTAMP) /*** SSC-FDM-0013 - TIMEZONE EXPRESSION COULD NOT BE MAPPED, RESULTS MAY BE DIFFERENT ***/;

SELECT
CONVERT_TIMEZONE((
SELECT
COL1 FROM
TABLE1
WHERE COL2 = 2), CURRENT_TIMESTAMP) /*** SSC-FDM-0013 - TIMEZONE EXPRESSION COULD NOT BE MAPPED, RESULTS MAY BE DIFFERENT ***/;
```

####

> **Note:**
>
> ##### Timezone Compatibility in Oracle
>
> The majority of timezone name expressions in Oracle are directly supported in Snowflake, when this is the case, the migration will run without issues. Additionally, here is a list of which ones are not supported by Snowflake at the moment, and therefore will include the functional difference message.

* Africa/Doula
* Asia/Ulaanbaator
* Asia/Yetaterinburg
* Canada/East-Saskatchewan
* CST
* PST
* US/Pacific-New

#### Best Practices

* No end-user action is required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0014

Check statement not supported.

> **Note:**
>
> This FDM is deprecated, please refer to [SSC-EWI-0035](../conversion-issues/generalEWI.md) documentation.

### Description

***CHECK*** constraint is not supported by Snowflake but it does not affect functionally.

#### Example Code

##### Input Code Oracle

```sql
 CREATE TABLE "Schema"."BaseTable"(
  "COLUMN1" VARCHAR2(255),
  CHECK ( COLUMN1 IS NOT NULL )
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE "Schema"."BaseTable" (
    "COLUMN1" VARCHAR(255)
--                          ,
--    --** SSC-FDM-0014 - CHECK STATEMENT NOT SUPPORTED **
--    CHECK ( COLUMN1 IS NOT NULL )
  )
  COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
  ;
```

##### Input Code Teradata

```sql
 CREATE TABLE TABLE1,
    NO FALLBACK,
    NO BEFORE JOURNAL,
    NO AFTER JOURNAL
(
    COL0 BYTEINT,
    CONSTRAINT constraint_name CHECK (COL1 < COL2)
)
```

##### Generated Code

```sql
 CREATE TABLE TABLE1
(
    COL0 BYTEINT
--                ,
--    --** SSC-FDM-0014 - CHECK STATEMENT NOT SUPPORTED **
--    CONSTRAINT constraint_name CHECK (COL1 < COL2)
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
;
```

##### Input Code SqlServer

```sql
 ALTER TABLE table_name2
ADD column_name VARCHAR(255)
CONSTRAINT constraint_name
CHECK NOT FOR REPLICATION (column_name > 1);
```

##### Generated Code

```sql
 ALTER TABLE IF EXISTS table_name2
ADD column_name VARCHAR(255)
----** SSC-FDM-0014 - CHECK STATEMENT NOT SUPPORTED **
--CONSTRAINT constraint_name
--CHECK NOT FOR REPLICATION (column_name > 1)
                                           ;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0015

​Referenced custom type in query not found.

### Description

This error happens when the definition for a Custom Type was not found or an Oracle built-in data type was not recognized by SnowConvert.

#### Example code

##### Input Code (Oracle)

```sql
 --Type was never defined
--CREATE TYPE type1;

CREATE TABLE table1
(
column1 type1
);
```

##### Generated Code

```sql
 --Type was never defined
--CREATE TYPE type1;

CREATE OR REPLACE TABLE table1
(
column1 VARIANT !!!RESOLVE EWI!!! /*** SSC-EWI-TS0015 - DATA TYPE TYPE1 IS NOT SUPPORTED IN SNOWFLAKE ***/!!! NOT NULL
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}}'
;
```

#### Best Practices

* Verify that the type that the referenced data type was defined in the input code.
* Check the Snowflake data types [documentation](https://docs.snowflake.com/en/sql-reference/data-types.html) to find an equivalent for the data type.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0016

Constants are not supported by Snowflake Scripting. It was transformed to a variable.

### Description

Snowflake Scripting does not support constants. Therefore, all constants inside procedures are being transformed into variables when the Snowflake Scripting flag is active.

#### Example code

##### Oracle

```sql
 CREATE OR REPLACE PROCEDURE p_constants
AS
my_const1 CONSTANT NUMBER := 40;
my_const2 CONSTANT NUMBER NOT NULL := 40;
BEGIN
NULL;
END;
```

##### Snowflake Scripting

```sql
 CREATE OR REPLACE PROCEDURE p_constants ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
EXECUTE AS CALLER
AS
$$
DECLARE
--** SSC-FDM-0016 - CONSTANTS ARE NOT SUPPORTED BY SNOWFLAKE SCRIPTING. IT WAS TRANSFORMED TO A VARIABLE **
my_const1 NUMBER(38, 18) := 40;
--** SSC-FDM-0016 - CONSTANTS ARE NOT SUPPORTED BY SNOWFLAKE SCRIPTING. IT WAS TRANSFORMED TO A VARIABLE **
--** SSC-FDM-OR0025 - NOT NULL CONSTRAINT IS NOT SUPPORTED BY SNOWFLAKE **
my_const2 NUMBER(38, 18) := 40;
BEGIN
NULL;
END;
$$;
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0017

WITH SYSTEM VERSIONING clause is not supported by Snowflake

### Description

The `WITH SYSTEM VERSIONING` clause in ANSI SQL is used to enable system versioning for a table, allowing you to maintain a history of changes to the table’s data over time. This clause is not supported by Snowflake.

#### Code Example

##### Input Code

```sql
 CREATE TABLE t1 (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    SysStartTime TIMESTAMP,
    SysEndTime TIMESTAMP
) WITH SYSTEM VERSIONING;
```

##### Generated Code

```sql
 CREATE TABLE t1 (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    SysStartTime TIMESTAMP,
    SysEndTime TIMESTAMP
)
----** SSC-FDM-0017 - WITH SYSTEM VERSIONING CLAUSE IS NOT SUPPORTED BY SNOWFLAKE. **
--WITH SYSTEM VERSIONING
                      ;
```

#### Best Practices

* You can use [Time Travel](https://docs.snowflake.com/en/user-guide/data-time-travel) in Snowflake, Time Travel enables accessing historical data (that is, data that has been changed or deleted) at any point within a defined period. It serves as a powerful tool for performing the following tasks:

  * Restoring data-related objects (tables, schemas, and databases) that might have been accidentally or intentionally deleted.
  * Duplicating and backing up data from key points in the past.
  * Analyzing data usage/manipulation over specified periods of time.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0018

CHARACTER SET clause is not supported by Snowflake.

### Description

The column option CHARACTER SET determines the allowed set of characters that can be stored in the column, this clause is not supported by Snowflake.

#### Code Example

##### Input Code

```sql
 CREATE TABLE TABLE01(
    COLNAME VARCHAR(20) CHARACTER SET character_specification
);
```

##### Generated Code

```sql
 CREATE TABLE TABLE01 (
    COLNAME VARCHAR(20)
--                        --** SSC-FDM-0018 - CHARACTER SET CLAUSE IS NOT SUPPORTED BY SNOWFLAKE. **
--                        CHARACTER SET character_specification
);
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0019

Semantic information could not be loaded.

### Description

This warning lets the user know that SnowConvert AI was not able to load semantic information for a specific object. This is most likely caused because if there is a duplicated object with the same name, SnowConvert AI could not load the semantic information of this object and complete the analysis.

#### Example Code

##### Input Code

```sql
 CREATE TABLE T1
(
    COL1 INTEGER
);

CREATE TABLE T1
(
    COL2 INTEGER
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE T1
(
    COL1 INTEGER
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
;

--** SSC-FDM-0019 - SEMANTIC INFORMATION COULD NOT BE LOADED FOR T1. CHECK IF THE NAME IS INVALID OR DUPLICATED. **
CREATE TABLE T1
(
    COL2 INTEGER
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
;
```

#### Best Practices

* Check for duplicate objects in the input code since this may affect the loading of semantic information.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0020

Multiple result sets are returned in temporary tables

### Description

Snowflake Scripting procedures only allow one result set to be returned per procedure.

To replicate Teradata behavior, when there are two or more result sets to return, they are stored in temporary tables. The Snowflake Scripting procedure will return an array containing the name of the temporary tables.

#### Example code

##### Input Code (Teradata)

```sql
 REPLACE MACRO sampleMacro AS
(
    SELECT CURRENT_DATE AS DT;
    SELECT CURRENT_DATE AS DT_TWO;
);
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE sampleMacro ()
RETURNS ARRAY
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        return_arr ARRAY := array_construct();
        tbl_nm VARCHAR;
    BEGIN
        tbl_nm := 'RESULTSET_' || REPLACE(UPPER(UUID_STRING()), '-', '_');
        CREATE OR REPLACE TEMPORARY TABLE IDENTIFIER(:tbl_nm) AS
            SELECT
                CURRENT_DATE() AS DT;
        return_arr := array_append(return_arr, :tbl_nm);
        tbl_nm := 'RESULTSET_' || REPLACE(UPPER(UUID_STRING()), '-', '_');
        CREATE OR REPLACE TEMPORARY TABLE IDENTIFIER(:tbl_nm) AS
            SELECT
                CURRENT_DATE() AS DT_TWO;
        return_arr := array_append(return_arr, :tbl_nm);
        --** SSC-FDM-0020 - MULTIPLE RESULT SETS ARE RETURNED IN TEMPORARY TABLES **
        RETURN return_arr;
    END;
$$;
```

#### Best Practices

* To obtain the result sets, it is necessary to run a SELECT query with the name of the temporary tables returned by the procedure.
* As much as possible, avoid procedures that return multiple result sets; instead, make them single-responsibility for more direct results.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0021

Create Index Not Supported

### Description

Due to architectural reasons, Snowflake does not support indexes so, SnowConvert AI will comment out all the code related to the creation of indexes. Snowflake automatically creates micro-partitions for every table that help speed up the performance of DML operations, the user does not have to worry about creating or managing these micro-partitions.

Usually, this is enough to have a very good query performance however, there are ways to improve it by creating data clustering keys. [Snowflake’s official page](https://docs.snowflake.com/en/user-guide/tables-clustering-micropartitions.html) provides more information about micro-partitions and data clustering.

#### Example Code

##### Input Code (Oracle)

```sql
 CREATE INDEX index1
ON table1(column1);
```

##### Generated Code

```sql
 ----** SSC-FDM-0021 - CREATE INDEX IS NOT SUPPORTED BY SNOWFLAKE **
----** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "table1" **
--CREATE INDEX index1
--ON table1(column1)
                  ;
```

#### Best Practices

* Data clustering might be a way to speed up query performance on tables.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0022

Window frame unit was changed to Rows

### Severity

Low

### Description

This warning is added when an unsupported Window Frame Unit was changed into Rows, leading to output differences. One example of this is the GROUPS unit, which is not supported by Snowflake.

Please note that this message is also used in cases where a Window Frame Unit is **partially** unsupported leading to it being changed, like the RANGE unit.

#### Example Code

Given the following data as an example to explain it.

| C_NAME | C_BIRTH_DAY |
| --- | --- |
| USA | 1 |
| USA | 4 |
| Poland | 9 |
| Canada | 10 |
| USA | 5 |
| Canada | 12 |
| Costa Rica | 3 |
| Poland | 4 |
| USA | 2 |
| Costa Rica | 7 |
| Costa Rica | 10 |

##### Oracle

##### Code

```
SELECT
    C_NAME,
    SUM(C_BIRTH_DAY)
    OVER (ORDER BY C_BIRTH_DAY
    RANGE BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) AS MAX1
FROM WINDOW_TABLE;
```

##### Result

| C_NAME | MAX1 |
| --- | --- |
| USA | - |
| USA | 1 |
| Costa Rica | 3 |
| USA | 6 |
| Poland | 6 |
| USA | 14 |
| Costa Rica | 19 |
| Poland | 26 |
| Canada | 35 |
| Costa Rica | 35 |
| Canada | 55 |

##### Snowflake

##### Code

```sql
 SELECT
    C_NAME,
    SUM(C_BIRTH_DAY)
    OVER (ORDER BY C_BIRTH_DAY ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING /*** SSC-FDM-0022 - WINDOW FRAME UNIT 'RANGE' WAS CHANGED TO ROWS ***/) AS MAX1
    FROM
WINDOW_TABLE;
```

##### Result

| C_NAME | MAX1 |
| --- | --- |
| USA | - |
| USA | 1 |
| Costa Rica | 3 |
| USA | 6 |
| Poland | 10 |
| USA | 14 |
| Costa Rica | 19 |
| Poland | 26 |
| Canada | 35 |
| Costa Rica | 45 |
| Canada | 55 |

#### Best Practices

* Ensure deterministic ordering for rows to ensure deterministic outputs when running in Snowflake.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0023

A Global Temporary Table is being referenced.

### Severity

Medium

### Description

SnowConvert AI transforms Global Temporary tables into regular Create Table. References to these tables may behave different than expected.

#### Code example

##### Input

```sql
 create global temporary table t1
    (col1 varchar);
create view view1 as
    select col1 from t1;
```

##### Output

```sql
 --** SSC-FDM-0009 - GLOBAL TEMPORARY TABLE FUNCTIONALITY NOT SUPPORTED. **
CREATE OR REPLACE TABLE t1
    (col1 varchar)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
;

CREATE OR REPLACE VIEW view1
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
AS
select col1 from
    --** SSC-FDM-0023 - A Global Temporary Table is being referenced **
    t1;
```

#### Related Issues

* SSC-FDM-0009: GLOBAL TEMPORARY TABLE functionality not supported.

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0024

Functionality is not currently supported by Snowflake Scripting

> **Note:**
>
> This `FDM` is deprecated, please refer to [SSC-EWI-0058](../conversion-issues/generalEWI.md) documentation.

### Description

This error happens when a statement used in a create procedure is not currently supported by Snowflake Scripting.

#### Example code

##### Input Code (Oracle)

```sql
 CREATE OR REPLACE PROCEDURE PROC01
IS
  number_variable INTEGER;
BEGIN
  EXECUTE IMMEDIATE 'SELECT 1 FROM DUAL' INTO number_variable;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE PROC01 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
EXECUTE AS CALLER
AS
$$
  DECLARE
    number_variable INTEGER;
  BEGIN
    EXECUTE IMMEDIATE 'SELECT 1 FROM DUAL'
--                                           --** SSC-FDM-0024 - FUNCTIONALITY FOR 'EXECUTE IMMEDIATE RETURNING CLAUSE' IS NOT CURRENTLY SUPPORTED BY SNOWFLAKE SCRIPTING **
--                                           INTO number_variable
                                                               ;
  END;
$$;
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0026

Type not supported by Snowflake

> **Note:**
>
> This `FDM` is deprecated, please refer to [SSC-EWI-0028](../conversion-issues/generalEWI.md) documentation.

### Description

This message appears when a type is not supported in Snowflake.

#### Example

##### Input Code (Oracle)

```sql
 CREATE TABLE MYTABLE
(
    COL1 SYS.ANYDATASET
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE MYTABLE
    (
    --** SSC-FDM-0026 - TYPE NOT SUPPORTED BY SNOWFLAKE **
        COL1 SYS.ANYDATASET
    )
    COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
    ;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0027

Removed next statement, not applicable in Snowflake.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

This message appears when a specific statement is not applicable in Snowflake, it means that there is no Snowflake equivalent for this statement and it is no longer needed, and for that reason, it is removed from the source code. However, SnowConvert AI keeps the original statement as part of the comment at the end.

#### Example Code

##### Input Code

```sql
 .LOGTABLE tduser.Employee_log;
   .BEGIN MLOAD TABLES Employee_Stg;
      .LAYOUT Employee;
      .FIELD in_EmployeeNo * VARCHAR(10);
      .FIELD in_FirstName * VARCHAR(30);
      .FIELD in_LastName * VARCHAR(30);
      .FIELD in_BirthDate * VARCHAR(10);
      .FIELD in_JoinedDate * VARCHAR(10);
      .FIELD in_DepartmentNo * VARCHAR(02);

      .dml label EmpLabel
  IGNORE DUPLICATE INSERT ROWS;
      INSERT INTO Employee_Stg (
         EmployeeNo,
         FirstName,
         LastName,
         BirthDate,
         JoinedDate,
         DepartmentNo
      )
      VALUES (
         :in_EmployeeNo,
         :in_FirstName,
         :in_Lastname,
         :in_BirthDate,
         :in_JoinedDate,
         :in_DepartmentNo
      );
      .IMPORT INFILE employee.txt
      FORMAT VARTEXT ','
      LAYOUT Employee
      APPLY EmpLabel;
   .END MLOAD;
LOGOFF;
```

##### Generated Code

```sql
 #*** Generated code is based on the SnowConvert AI Python Helpers version 2.0.6 ***
// SnowConvert AI Helpers Code section is omitted.

import os
import sys
import snowconvert.helpers
from snowconvert.helpers import Export
from snowconvert.helpers import exec
from snowconvert.helpers import BeginLoading
con = None
def main():
  snowconvert.helpers.configure_log()
  con = snowconvert.helpers.log_on()
  #** SSC-FDM-0027 - REMOVED NEXT STATEMENT, NOT APPLICABLE IN SNOWFLAKE.  **
  #.LOGTABLE tduser.Employee_log

  #** SSC-FDM-0027 - REMOVED NEXT STATEMENT, NOT APPLICABLE IN SNOWFLAKE.  **
  #.BEGIN MLOAD TABLES Employee_Stg

  Employee_TableName = "Employee_TEMP_TABLE"
  Employee_Columns = """in_EmployeeNo VARCHAR(10),
in_FirstName VARCHAR(30),
in_LastName VARCHAR(30),
in_BirthDate VARCHAR(10),
in_JoinedDate VARCHAR(10),
in_DepartmentNo VARCHAR(02)"""
  Employee_Conditions = """in_EmployeeNo AS in_EmployeeNo, in_FirstName AS in_FirstName, in_LastName AS in_LastName, in_BirthDate AS in_BirthDate, in_JoinedDate AS in_JoinedDate, in_DepartmentNo AS in_DepartmentNo"""
  def EmpLabel(tempTableName, queryConditions = ""):
    exec(f"""INSERT INTO Employee_Stg (EmployeeNo, FirstName, LastName, BirthDate, JoinedDate, DepartmentNo)
SELECT
   SRC.in_EmployeeNo,
   SRC.in_FirstName,
   :in_Lastname,
   SRC.in_BirthDate,
   SRC.in_JoinedDate,
   SRC.in_DepartmentNo
FROM {tempTableName} SRC {queryConditions}""")
  #** SSC-FDM-0027 - REMOVED NEXT STATEMENT, NOT APPLICABLE IN SNOWFLAKE. TRANSLATED BELOW **
  #.IMPORT INFILE employee.txt FORMAT VARTEXT ',' LAYOUT Employee APPLY EmpLabel

  snowconvert.helpers.import_file_to_temptable(fr"employee.txt", Employee_TableName, Employee_Columns, Employee_Conditions, ',')
  EmpLabel(Employee_TableName)
  exec(f"""DROP TABLE {Employee_TableName}""")

  if con is not None:
    con.close()
    con = None
  snowconvert.helpers.quit_application()

if __name__ == "__main__":
  main()
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0028

Not supported.

> **Note:**
>
> This `FDM` is deprecated, please refer to [SSC-EWI-0021](../conversion-issues/generalEWI.md) documentation.

### Description

This message appears when a specific node or statement from the source code is not supported in Snowflake.

#### Example Code

##### Input Code

```sql
 WITH my_av ANALYTIC VIEW AS
(USING sales_av HIERARCHIES(time_hier) ADD MEASURES(lag_sales AS (LAG(sales) OVER (HIERARCHY time_hier OFFSET 1 ))))
SELECT aValue from my_av;
```

##### Generated Code

```sql
 ----** SSC-FDM-0028 - SubavFactoring NOT SUPPORTED IN SNOWFLAKE **
--WITH my_av ANALYTIC VIEW AS
--(USING sales_av HIERARCHIES(time_hier) ADD MEASURES(lag_sales AS (LAG(sales) OVER (HIERARCHY time_hier OFFSET 1 ))))
--SELECT aValue from my_av
                        ;
```

#### Best Practices

* If this error happens, it is because there is no Snowflake equivalent for the node that is being converted.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0029

User defined function was transformed to a Snowflake procedure.

> **Warning:**
>
> This EWI is deprecated, please refer to [SSC-EWI-0068](../conversion-issues/generalEWI.md) documentation

### Severity

Low

### Description

Snowflake user defined functions do not support the same features as Oracle or SQL Server. To maintain the functional equivalence the function is transformed to a Snowflake stored procedure. This will affect their usage in queries.

#### Example Code

##### SQL Server

##### Input Code

```sql
 CREATE OR ALTER FUNCTION PURCHASING.FOO()
RETURNS INT
AS
BEGIN
    DECLARE @i int = 0, @p int;
    Select @p = COUNT(*) FROM PURCHASING.VENDOR

    WHILE (@p < 1000)
    BEGIN
        SET @i = @i + 1
        SET @p = @p + @i
    END

    IF (@i = 6)
        RETURN 1

    RETURN @p
END;
```

##### Generated Code

```sql
 --** SSC-FDM-0029 - USER DEFINED FUNCTION WAS TRANSFORMED TO SNOWFLAKE PROCEDURE **
CREATE OR REPLACE PROCEDURE PURCHASING.FOO ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        I INT := 0;
        P INT;
    BEGIN

        Select
            COUNT(*)
        INTO
            :P
 FROM
            PURCHASING.VENDOR;
        WHILE (:P < 1000) LOOP
            I := :I + 1;
            P := :P + :I;
        END LOOP;
        IF ((:I = 6)) THEN
            RETURN 1;
        END IF;
        RETURN :P;
    END;
$$;
```

##### Oracle

##### Input Code

```sql
 CREATE FUNCTION employee_function (param1 in NUMBER) RETURN NUMBER is
  var1    employees.employee_ID%TYPE;
  var2    employees.manager_ID%TYPE;
  var3    employees.title%TYPE;
BEGIN
  SELECT employee_ID, manager_ID, title
  INTO var1, var2, var3
  FROM employees
    START WITH manager_ID = param1
    CONNECT BY manager_ID = PRIOR employee_id;
  RETURN var1;
EXCEPTION
   WHEN no_data_found THEN RETURN param1;
END employee_function;
```

##### Generated Code

```sql
 --** SSC-FDM-0029 - USER DEFINED FUNCTION WAS TRANSFORMED TO SNOWFLAKE PROCEDURE **
CREATE OR REPLACE PROCEDURE employee_function (param1 NUMBER(38, 18))
RETURNS NUMBER(38, 18)
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "11/14/2024",  "domain": "test" }}'
EXECUTE AS CALLER
AS
$$
  DECLARE
    var1    employees.employee_ID%TYPE;
    var2    employees.manager_ID%TYPE;
    var3    employees.title%TYPE;
  BEGIN
    SELECT employee_ID, manager_ID, title
    INTO
      :var1,
      :var2,
      :var3
    FROM
      employees
      START WITH manager_ID = :param1
    CONNECT BY
      manager_ID = PRIOR employee_id;
    RETURN :var1;
  EXCEPTION
     WHEN no_data_found THEN
      RETURN :param1;
  END;
$$;
```

### Best Practices

* Separate the inside queries to maintain the same logic.
* The source code may need to be restructured to fit with the Snowflake user-defined functions [approach](https://docs.snowflake.com/en/sql-reference/user-defined-functions.html#udfs-user-defined-functions).
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0030

Replaced invalid characters for new identifier

### Description

The given identifier has invalid characters for the output language. Those characters were replaced with their UTF-8 codes.

#### Example Code

##### Input Code (Oracle)

```sql
 CREATE PROCEDURE PROC1
AS
    "VAR0" INT;
    "VAR`/1ͷ" VARCHAR(20);
    "o*/o" FLOAT;
    " . " INT;
    ". ." INT;
    "123Name" INT;
    "return" INT;
    yield INT;
    ident#10 INT;
BEGIN
    NULL;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE PROC1 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        "VAR0" INT;
        --** SSC-FDM-0030 - IDENTIFIER '"VAR`/1ͷ"' HAS INVALID CHARACTERS. CHARACTERS WERE REPLACED WITH THEIR UTF-8 CODES **
        VAR_u60_u2F1_uCD_B7 VARCHAR(20);
        --** SSC-FDM-0030 - IDENTIFIER '"o*/o"' HAS INVALID CHARACTERS. CHARACTERS WERE REPLACED WITH THEIR UTF-8 CODES **
        o_u2A_u2Fo FLOAT;
        --** SSC-FDM-0030 - IDENTIFIER '" . "' HAS INVALID CHARACTERS. CHARACTERS WERE REPLACED WITH THEIR UTF-8 CODES **
        _u20_u2E_u20 INT;
        --** SSC-FDM-0030 - IDENTIFIER '". ."' HAS INVALID CHARACTERS. CHARACTERS WERE REPLACED WITH THEIR UTF-8 CODES **
        _u2E_u20_u2E INT;
        "123Name" INT;
        "return" INT;
        yield INT;
        IDENT_HASHTAG_10 INT;
    BEGIN
        NULL;
    END;
$$;
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0031

Dynamic Table required parameters set by default

### Description

Materialized Views (and Join Indexes in the case of Teradata) are migrated to Dynamic Tables in Snowflake. Dynamic Tables require two parameters to be set: TARGET_LAG and WAREHOUSE.

If these parameters are not set in the configuration options, they are set by default during conversion.

Read more about the [required Dynamic Tables parameters here](https://docs.snowflake.com/en/sql-reference/sql/create-dynamic-table#required-parameters).

#### Example Code

##### Input Code (Oracle)

```sql
 CREATE MATERIALIZED VIEW mv1
AS SELECT * FROM table1;
```

##### Generated Code

```sql
 CREATE OR REPLACE DYNAMIC TABLE mv1
--** SSC-FDM-0031 - DYNAMIC TABLE REQUIRED PARAMETERS SET BY DEFAULT **
TARGET_LAG='1 day'
WAREHOUSE=UPDATE_DUMMY_WAREHOUSE
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
AS
--** SSC-FDM-0001 - VIEWS SELECTING ALL COLUMNS FROM A SINGLE TABLE ARE NOT REQUIRED IN SNOWFLAKE AND MAY IMPACT PERFORMANCE. **
SELECT * FROM
table1;
```

#### Best Practices

* Configure the dynamic table required parameters according to your needs.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0032

Parameter is not a literal value, transformation could not be fully applied

### Description

For multiple transformations, SnowConvert AI sometimes requires to validate the contents of a parameter, which is only possible if the parameter is a literal value.

This message is generated to warn the user that SnowConvert AI could not retrieve the value of the parameter because it was passed by reference, causing the transformation of the function or statement to not be completed.

#### Example Code

##### Input Code (Redshift)

```sql
 SELECT TO_CHAR(DATE '2001-01-01', 'YYY/MM/DD'),
TO_CHAR(DATE '2001-01-01', f)
FROM (SELECT 'YYY/MM/DD' as f);
```

##### Generated Code

```sql
 SELECT
PUBLIC.YEAR_PART_UDF(DATE '2001-01-01', 3) || TO_CHAR(DATE '2001-01-01', '/MM/DD'),
--** SSC-FDM-0032 - PARAMETER 'format_string' IS NOT A LITERAL VALUE, TRANSFORMATION COULD NOT BE FULLY APPLIED **
TO_CHAR(DATE '2001-01-01', f)
FROM (SELECT 'YYY/MM/DD' as f);
```

#### Best Practices

* Try to provide the specified parameter as a literal value.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0033

Sample clause behaves differently in Snowflake.

### Description

This message is generated to showcase the functional difference while sampling rows in Snowflake. The differences are related to the quantity of rows retrieved. When in Teradata there is the same quantity of rows in the non-deterministic output, it may change in Snowflake and return a few rows more or less. This is because a probability related topic and it is expected to behaves like that in Snowflake.

If there is a requirement of retrieving the same values and the same quantity, a deterministic output, it is recommended to use a seed in the Snowflake query.

#### Example Code

##### Input Code (Teradata)

```sql
 SELECT * FROM Employee SAMPLE 2;
SELECT * FROM Employee SAMPLE 0.25;
```

##### Generated Code

```sql
 SELECT
    * FROM
    Employee
--** SSC-FDM-0033 - SAMPLE CLAUSE BEHAVES DIFFERENTLY IN SNOWFLAKE **
SAMPLE(2 ROWS);

SELECT
    * FROM
    Employee
--** SSC-FDM-0033 - SAMPLE CLAUSE BEHAVES DIFFERENTLY IN SNOWFLAKE **
SAMPLE(25);
```

#### Best Practices

* Try to use the seed part of the query when it is required a deterministic output.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0034

Struct converted to VARIANT. Some of its usages might have functional differences.

### Description

Snowflake does not natively support the STRUCT data type. SnowConvert AI automatically converts STRUCT to VARIANT. When used in INSERT statements, STRUCT data will be handled using `OBJECT_CONSTRUCT`. Be aware that this conversion may introduce functional differences in some use cases.

#### Code Example

##### Input Code

##### BigQuery

```sql
 CREATE OR REPLACE TABLE test.structTypes
(
  COL1 STRUCT<sc1 INT64>,
  COL2 STRUCT<sc2 STRING(10)>,
  COL3 STRUCT<sc3 STRUCT<sc31 INT64, sc32 INT64>>,
  COL4 STRUCT<sc4 ARRAY<INT64>>,
  COL5 STRUCT<sc5 INT64, sc51 INT64>,
  COL7 STRUCT<sc7 INT64 OPTIONS(description = "A repeated STRING field"), sc71 BOOL>,
  COL8 STRUCT<sc8 INT64 NOT NULL, sc81 BOOL NOT NULL OPTIONS(description = "A repeated STRING field")>
);
```

##### Generated Code

##### Snowflake

```sql
 CREATE OR REPLACE TABLE test.structTypes
(
  COL1 VARIANT /*** SSC-FDM-0034 - STRUCT<INT64> CONVERTED TO VARIANT. SOME OF ITS USAGES MIGHT HAVE FUNCTIONAL DIFFERENCES. ***/,
    COL2 VARIANT /*** SSC-FDM-0034 - STRUCT<STRING(10)> CONVERTED TO VARIANT. SOME OF ITS USAGES MIGHT HAVE FUNCTIONAL DIFFERENCES. ***/,
    COL3 VARIANT /*** SSC-FDM-0034 - STRUCT<STRUCT<INT64, INT64>> CONVERTED TO VARIANT. SOME OF ITS USAGES MIGHT HAVE FUNCTIONAL DIFFERENCES. ***/,
    COL4 VARIANT /*** SSC-FDM-0034 - STRUCT<ARRAY<INT64>> CONVERTED TO VARIANT. SOME OF ITS USAGES MIGHT HAVE FUNCTIONAL DIFFERENCES. ***/,
    COL5 VARIANT /*** SSC-FDM-0034 - STRUCT<INT64, INT64> CONVERTED TO VARIANT. SOME OF ITS USAGES MIGHT HAVE FUNCTIONAL DIFFERENCES. ***/,
    COL7 VARIANT /*** SSC-FDM-0034 - STRUCT<INT, BOOL> CONVERTED TO VARIANT. SOME OF ITS USAGES MIGHT HAVE FUNCTIONAL DIFFERENCES. ***/,
    COL8 VARIANT /*** SSC-FDM-0034 - STRUCT<INT64, BOOLEAN> CONVERTED TO VARIANT. SOME OF ITS USAGES MIGHT HAVE FUNCTIONAL DIFFERENCES. ***/
  )
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "bigquery",  "convertedOn": "05/30/2025",  "domain": "no-domain-provided" }}';
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0035

The INFER_SCHEMA function requires a file path without wildcards to generate the table template, replace the FILE_PATH placeholder with it

### Description

The [INFER_SCHEMA](https://docs.snowflake.com/en/sql-reference/functions/infer_schema) function is used in Snowflake to generate the columns definition of a table based on the structure of a file, it requires a LOCATION parameter that specifies the path to a file or folder that will be used to construct the table columns, however, this path does not support regex, meaning that the wildcard `*` character is not supported.

When the table has no columns, SnowConvert AI will check all URIS to find one that does not use wildcards and use it in the INFER_SCHEMA function, when no URI meets such criteria this FDM and a FILE_PATH placeholder will be generated, the placeholder has to be replaced with the path of one of the files referenced by the external table to generate the table columns.

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
  --** SSC-FDM-0035 - THE INFER_SCHEMA FUNCTION REQUIRES A FILE PATH WITHOUT WILDCARDS TO GENERATE THE TABLE TEMPLATE, REPLACE THE FILE_PATH PLACEHOLDER WITH IT **
  TABLE(INFER_SCHEMA(LOCATION => '@EXTERNAL_STAGE/FILE_PATH', FILE_FORMAT => 'SC_TEST_MY_EXTERNAL_TABLE_JSON2_FORMAT'))
)
!!!RESOLVE EWI!!! /*** SSC-EWI-0032 - EXTERNAL TABLE REQUIRES AN EXTERNAL STAGE TO ACCESS gs://sc_external_table_bucket, DEFINE AND REPLACE THE EXTERNAL_STAGE PLACEHOLDER ***/!!!
LOCATION = @EXTERNAL_STAGE
AUTO_REFRESH = false
PATTERN = 'folder_with_json/.*'
FILE_FORMAT = (TYPE = JSON);
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0036

The transformed numeric/date format may have a different behavior in Snowflake.

### Description

The transformed numeric formats to Snowflake use [Fixed position formats](../../../../../../sql-reference/sql-format-models.md). The transformed format can fail and generate a different output when there are more digits in the integer part of the number than there are digit positions in the format; all digits are printed as # to indicate overflow.

> **Note:**
>
> **For SQL Server migrations:** If you are converting SQL Server code that uses custom single-character date format specifiers (for example, `%y`, `%M`, `%d`, `%H`, `%h`, `%m`, `%s`) or advanced numeric format specifiers (for example, `P`, `N`, `%`), consider enabling the `--enableFormatSpecifiersPreview` preview flag. This flag enables access to new Snowflake format specifiers that provide more accurate translations of these formats. See [Preview Features Settings](../../../getting-started/running-snowconvert/conversion/preview-conversion-settings.md) for more details.
>
> **Note:** This requires requesting preview access in your Snowflake account through [this form](https://docs.google.com/forms/u/0/d/1-aIsixSftqhqjkpgBHAzcbSi2mk7s71TMQsRdOBppFw/viewform?edit_requested=true).

#### Code Example

##### Input Code

##### Sql Server

```sql
SELECT
 FORMAT(value, '00.00') as formatted,
 FORMAT(value, '#,##0') as formatSource
 FROM MY_TABLE;
```

##### Generated Code

##### Snowflake

```sql
SELECT
 TO_CHAR(value, 'FM9999999999900.00') /*** SSC-FDM-0036 - TRANSFORMATION OF '00.00' FORMAT MAY HAVE A DIFFERENT BEHAVIOR IN SNOWFLAKE. ***/ as formatted,
 TO_CHAR(value, 'FM9,999,999,999,990') /*** SSC-FDM-0036 - TRANSFORMATION OF '#,##0' FORMAT MAY HAVE A DIFFERENT BEHAVIOR IN SNOWFLAKE. ***/ as formatSource
 FROM
 MY_TABLE;
```

##### Result

```sql
#############
```

#### Best Practices

* If the numeric digit does not fit in the format, please update the format by adding more digits based on the possible input data values.

## SSC-FDM-0037

Statistics function not needed in Snowflake.

### Description

DROP, COLLECT, or HELP statistics are not needed in Snowflake. Snowflake already collects statistics used for automatic query optimization.

#### Example Code

##### Input Code

```sql
  HELP STATISTICS TestName;
```

##### Generated Code

```sql
  ----** SSC-FDM-0037 - HELP STATISTICS NOT NEEDED. SNOWFLAKE AUTOMATICALLY COLLECTS STATISTICS. **
  --HELP STATISTICS TestName
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0038

Micro-partitioning is automatically performed on all Snowflake tables.

### Description

This message is added to the CREATE TABLE statement when a PARTITION BY clause is present. The PARTITION BY clause, which controls table partitioning in some databases, is not supported in Snowflake.

In Snowflake, all tables are automatically divided into micro-partitions—contiguous units of storage ranging from 50 MB to 500 MB of uncompressed data. This architecture enables highly granular pruning of large tables, which may consist of millions of micro-partitions.

Snowflake automatically stores metadata for each micro-partition, including:

* The range of values for each column in the micro-partition.
* The number of distinct values.
* Additional properties used for optimization and efficient query processing.

Tables are transparently partitioned based on the order of data as it is inserted or loaded. For more details, see the [Benefits of Micro-partitioning](https://docs.snowflake.com/en/user-guide/tables-clustering-micropartitions#benefits-of-micro-partitioning).

#### Example Code

##### Input Code

```sql
 CREATE TABLE orders
    (
      storeid INTEGER NOT NULL,
      productid INTEGER NOT NULL,
      orderdate DATE FORMAT 'yyyy-mm-dd' NOT NULL,
      totalorders INTEGER NOT NULL)
      PRIMARY INDEX (storeid, productid)
      PARTITION BY (RANGE_N(totalorders BETWEEN *, 100, 1000 AND *),RANGE_N(orderdate BETWEEN *, '2005-12-31' AND *) );
```

##### Generated Code

```sql
CREATE OR REPLACE TABLE orders
(
 storeid INTEGER NOT NULL,
 productid INTEGER NOT NULL,
 orderdate DATE NOT NULL,
 totalorders INTEGER NOT NULL)
-- --** SSC-FDM-0038 - MICRO-PARTITIONING IS AUTOMATICALLY HANDLED ON ALL SNOWFLAKE TABLES **
-- PARTITION BY (RANGE_N(totalorders BETWEEN *, 100, 1000 AND *)
--              ,RANGE_N(orderdate BETWEEN *, '2005-12-31' AND *) )
 COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "09/17/2025",  "domain": "no-domain-provided" }}'
;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-0041

Default parameters were reordered to the end of the parameter list.

### Description

Snowflake requires all parameters with default values to appear after all non-default parameters. When SnowConvert AI detects a procedure whose default parameters are not at the end of the parameter list, it automatically reorders them. Code not provided to SnowConvert AI that uses positional arguments may need to be updated to match the new parameter order.

> **Note:**
>
> This FDM replaces the deprecated [SSC-EWI-0002](../conversion-issues/generalEWI.md), which previously only warned about the issue without performing the reorder.

#### Example Code

##### Input Code (SQL Server)

```sql
 CREATE PROCEDURE dbo.TestProc (@Param1 INT = 10, @Param2 VARCHAR(50))
AS
BEGIN
   SET @Param1 = @Param1;
END
```

##### Generated Code (SQL Server)

```sql
 CREATE OR REPLACE PROCEDURE dbo.TestProc
--** SSC-FDM-0041 - DEFAULT PARAMETERS WERE REORDERED TO THE END OF THE PARAMETER LIST TO MATCH SNOWFLAKE REQUIREMENTS. CALLERS USING POSITIONAL ARGUMENTS MAY NEED TO BE UPDATED **
(PARAM2 STRING, PARAM1 INT DEFAULT 10)
RETURNS VARCHAR
LANGUAGE SQL
EXECUTE AS CALLER
AS
$$
  BEGIN
    PARAM1 := :PARAM1;
  END;
$$;
```

##### Input Code (Oracle)

```sql
 CREATE OR REPLACE PROCEDURE TestProc (param1 IN NUMBER DEFAULT 10, param2 IN VARCHAR2)
IS
BEGIN
   param1 := param1;
END;
```

##### Generated Code (Oracle)

```sql
 CREATE OR REPLACE PROCEDURE TestProc
--** SSC-FDM-0041 - DEFAULT PARAMETERS WERE REORDERED TO THE END OF THE PARAMETER LIST TO MATCH SNOWFLAKE REQUIREMENTS. CALLERS USING POSITIONAL ARGUMENTS MAY NEED TO BE UPDATED **
(param2 VARCHAR, param1 NUMBER(38, 18) DEFAULT 10)
RETURNS VARCHAR
LANGUAGE SQL
EXECUTE AS CALLER
AS
$$
  BEGIN
    param1 := :param1;
  END;
$$;
```

##### Positional Call Site Conversion

When callers use positional arguments and the parameters have been reordered, SnowConvert AI automatically converts them to named arguments:

```sql
 CREATE PROCEDURE dbo.CallerProc
AS
BEGIN
   EXEC dbo.TestProc 5, 'hello';
END
```

```sql
 CREATE OR REPLACE PROCEDURE dbo.CallerProc ()
RETURNS VARCHAR
LANGUAGE SQL
EXECUTE AS CALLER
AS
$$
  BEGIN
    CALL dbo.TestProc(PARAM1 => 5, PARAM2 => 'hello');
  END;
$$;
```

#### Best Practices

* Review all callers of the affected procedure. If positional arguments are used, update them to match the new parameter order or convert them to named arguments.
* Consider using named arguments (e.g., `param1 => value`) instead of positional arguments to avoid issues with parameter ordering.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
