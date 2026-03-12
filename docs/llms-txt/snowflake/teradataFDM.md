# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/functional-difference/teradataFDM.md

# SnowConvert AI - Teradata Functional Differences

## SSC-FDM-TD0001

Column converted from Blob data type.

### Description

This message is shown when SnowConvert AI finds a data type BLOB. Since BLOB is not supported in Snowflake, the type is changed to Binary.

#### Code Example

##### Input Code

```sql
 CREATE TABLE TableExample
(
ColumnExample BLOB
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE TableExample
(
ColumnExample BINARY /*** SSC-FDM-TD0001 - COLUMN CONVERTED FROM BLOB DATA TYPE ***/
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0002

Column converted from Clob data type.

### Description

This message is shown when SnowConvert AI finds a data type CLOB. Since CLOB is not supported in SnowConvert AI, the type is changed to VARCHAR.

#### Code Example

##### Input Code

```sql
 CREATE TABLE TableExample
(
ColumnExample CLOB
)
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE TableExample
(
ColumnExample VARCHAR /*** SSC-FDM-TD0002 - COLUMN CONVERTED FROM CLOB DATA TYPE ***/
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0003

Bash variables found, using SnowSQL with variable substitution enabled is required to run this script

### Description

When the source code of a script file migrated to Snowflake Scripting contains Bash variables placeholders ($variable or ${variable}), SnowConvert AI transforms them into SnowSQL variables (&variable or &{variable}).

This warning is generated to point out that the execution of the migrated script now depends on SnowSQL to work, please consider the following when running the script in SnowSQL:

* Variable substitution [must be enabled](https://docs.snowflake.com/en/user-guide/snowsql-use.html#enabling-variable-substitution).
* All variables [must be defined](https://docs.snowflake.com/en/user-guide/snowsql-use.html#defining-variables).
* Run the file as a [batch script](https://docs.snowflake.com/en/user-guide/snowsql-use.html#running-batch-scripts).

#### Example Code

##### Input Code

```sql
 .LOGON dbc, dbc;

select '$variable', '${variable}', '${variable}_concatenated';

select $colname from $tablename where info = $id;

select ${colname} from ${tablename} where info = ${id};

.LOGOFF;
```

##### Generated Code

```sql
EXECUTE IMMEDIATE
$$
  --** SSC-FDM-TD0003 - BASH VARIABLES FOUND, USING SNOWSQL WITH VARIABLE SUBSTITUTION ENABLED IS REQUIRED TO RUN THIS SCRIPT **
  DECLARE
    STATUS_OBJECT OBJECT := OBJECT_CONSTRUCT('SQLCODE', 0);
  BEGIN
    --.LOGON dbc, dbc
    !!!RESOLVE EWI!!! /*** SSC-EWI-0073 - PENDING FUNCTIONAL EQUIVALENCE REVIEW FOR 'BTLogOn' NODE ***/!!!
    null;
    BEGIN
      SELECT
        '&#x26;variable',
        '&#x26;{variable}',
        '&#x26;{variable}_concatenated';
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLROWCOUNT', SQLROWCOUNT);
    EXCEPTION
      WHEN OTHER THEN
        STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
    END;
    BEGIN
      SELECT
        &#x26;colname
      from
        &#x26;tablename
      where
        info = &#x26;id;
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLROWCOUNT', SQLROWCOUNT);
    EXCEPTION
      WHEN OTHER THEN
        STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
    END;
    BEGIN
      SELECT
        &#x26;{colname}
      from
        &#x26;{tablename}
      where
        info = &#x26;{id};
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLROWCOUNT', SQLROWCOUNT);
    EXCEPTION
      WHEN OTHER THEN
        STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
    END;
    --.LOGOFF
    !!!RESOLVE EWI!!! /*** SSC-EWI-0073 - PENDING FUNCTIONAL EQUIVALENCE REVIEW FOR 'LogOff' NODE ***/!!!
    null;
  END
$$
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0004

Period types are handled as two data fields

### Description

Teradata has a period data type used to represent a time interval, with instances of this type having a beginning and ending bound of the same type (time, date or timestamp) along with a set of functions that allow initializing and manipulating period data such as PERIOD, BEGIN, END, and OVERLAPS.

Since the period type is not supported by Snowflake, SnowConvert AI transforms this type and its related functions using the following rules:

* Any period type declaration in column tables is migrated as a two column of the same type.
* The [period value constructor function](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/SQL-Date-and-Time-Functions-and-Expressions/Period-Functions-and-Operators) is migrated into two different constructors of the period subtype one with the begin value and the other with the end value.
* Supported functions that expect period type parameters are migrated to UDFs as well, these UDFs expect almost two parameters for the begin value and the end value.

#### Example code

##### Input code

```sql
 -- Additional Params: --SplitPeriodDatatype
CREATE TABLE DateTable
(
 COL1 PERIOD(DATE) DEFAULT PERIOD (DATE '2005-02-03', UNTIL_CHANGED)
);
```

##### Generated Code

```sql
CREATE OR REPLACE TABLE DateTable
(
 COL1_begin DATE DEFAULT DATE '2005-02-03',
 COL1_end DATE DEFAULT DATE '9999-12-31' /*** SSC-FDM-TD0004 - PERIOD DATA TYPES ARE HANDLED AS TWO DATA FIELDS ***/
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0005

Non-standard time zone offsets are not supported in Snowflake, rounded to nearest valid time zone

### Description

While Teradata provides the flexibility to define any time zone offset between `-12:59` and `+14:00` using the `SET TIME ZONE` query, Snowflake exclusively supports time zones listed in the [IANA Time Zone Database](https://www.iana.org/time-zones).

If the specified offset in the SET TIME ZONE query does not align with an IANA standard time zone, Snowflake will automatically round it to the nearest standard time zone with the closest offset. In such a case, a warning message will be generated.

#### Example Code

##### Input Code

```sql
-- Will be rounded to Asia/Colombo (+05:30)
SET TIME ZONE '05:26';
```

##### Generated Code

```sql
 -- Will be rounded to Asia/Colombo (+05:30)
--** SSC-FDM-TD0005 - NON-STANDARD TIME ZONE OFFSETS NOT SUPPORTED IN SNOWFLAKE, ROUNDED TO NEAREST VALID TIME ZONE **
ALTER SESSION SET TIMEZONE = 'Asia/Colombo';
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0006

View With Check Option Not Supported.

### Description

This message is shown when SnowConvert AI finds a view with the WITH CHECK OPTION clause. Which is not supported in Snowflake, so it is commented out from the code.

This clause works with updatable views that can be used to execute INSERT and UPDATE commands over the view and internally update the table associated with the view.

The clause is used to restrict the rows that will be affected by the command using the WHERE clause in the view.

For more details see the [documentation](https://docs.teradata.com/r/SQL-Data-Definition-Language-Syntax-and-Examples/July-2021/View-Statements/CREATE-VIEW-and-REPLACE-VIEW/CREATE-VIEW-and-REPLACE-VIEW-Syntax-Elements/WITH-CHECK-OPTION) about the clause functionality.

#### Example code

##### Input code

```sql
REPLACE VIEW VIEWWITHOPTIONTEST AS
LOCKING ROW FOR ACCESS
SELECT
    *
FROM SOMETABLE
WHERE app_id = 'SUPPLIER'
WITH CHECK OPTION;
```

##### Generated Code

```sql
 CREATE OR REPLACE VIEW VIEWWITHOPTIONTEST
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/02/2025",  "domain": "no-domain-provided" }}'
AS
SELECT
    *
FROM
    SOMETABLE
WHERE
    UPPER(RTRIM( app_id)) = UPPER(RTRIM('SUPPLIER'))
--    --** SSC-FDM-TD0006 - VIEW WITH OPTION NOT SUPPORTED IN SNOWFLAKE **
--    WITH CHECK OPTION
                     ;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0007

Variant column does not support collation.

### Description

This message is shown when SnowConvert AI a Variant data type in the transformation of a code has a COLLATE clause. Since COLLATE is not supported with the data type VARIANT, it will be removed and a message will be added.

#### Example code

##### Input code

```sql
-- Additional Params: --useCollateForCaseSpecification
CREATE TABLE TableExample
(
ColumnExample JSON(2500) NOT CASESPECIFIC
)
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE TableExample
(
ColumnExample VARIANT
--                      NOT CASESPECIFIC /*** SSC-FDM-TD0007 - VARIANT COLUMN DOES NOT SUPPORT COLLATION ***/
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
;
```

The data type JSON is converted to VARIANT, while NOT CASESPECIFIC is converted to a COLLATE clause.

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0008

When NVP_UDF fourth parameter is non-literal and it contains a backslash, that backslash needs to be escaped.

### Description

Non-literal delimiters with spaces need their backslash escaped in Snowflake.

#### Example code

##### Input code

```sql
SELECT NVP('store = whole foods&#x26;&#x26;store: ?Bristol farms','store', '&#x26;&#x26;', valueDelimiter, 2);
```

##### Generated Code

```sql
 SELECT
PUBLIC.NVP_UDF('store = whole foods&&store: ?Bristol farms', 'store', '&&', valueDelimiter, 2) /*** SSC-FDM-TD0008 - WHEN NVP_UDF FOURTH PARAMETER IS NON-LITERAL AND IT CONTAINS A BACKSLASH, THAT BACKSLASH NEEDS TO BE ESCAPED ***/;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0009

Converted from integer to varchar for current session default.

### Description

This message is shown when SnowConvert AI finds a DEFAULT SESSION and the data type is NOT a VARCHAR. If that is the case, the data type is changed to VARCHAR and a message is added.

#### Code Example

##### Input Code

```sql
 CREATE TABLE TableExample
(
ColumnExample INTEGER DEFAULT SESSION,
ColumnExample2 VARCHAR DEFAULT SESSION
)
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE TableExample
(
ColumnExample VARCHAR DEFAULT CURRENT_SESSION() /*** SSC-FDM-TD0009 - CONVERTED FROM INTEGER TO VARCHAR FOR CURRENT_SESSION DEFAULT ***/,
ColumnExample2 VARCHAR DEFAULT CURRENT_SESSION()
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
;
```

Let’s look at the example. Note that ColumnExample has a data type INTEGER with DEFAULT SESSION. Since the data type is not VARCHAR, in the output it is transformed to VARCHAR.

The data type of ColumnExample2 hasn’t changed since it is already VARCHAR.

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0010

Table columns between tables (Teradata) DBC.COLUMNSV and INFORMATION_SCHEMA.COLUMNS (Snowflake). But some columns might not have an exact match in Snowflake.

### Description

Uses of the table `DBC.COLUMNSV` in Teradata are converted to `INFORMATION_SCHEMA.COLUMNS`, but some columns might not have an exact match in Snowflake. That means there are some columns in Teradata for which there is **no** equivalent in Snowflake, and there are others that do have a matching column but the content is not exactly the same.

Notice, for example, that there is no equivalent column for *“ColumnFormat*” in Snowflake and notice also that *“DATA_TYPE”* seems to be the match for the column *“ColumnType”* in Teradata, but their content greatly differ.

#### Code Example

##### Input Code

```sql
 SELECT columnname FROM dbc.columnsV WHERE tablename = 'TableN';
```

##### Generated Code

```sql
 SELECT
COLUMN_NAME AS COLUMNNAME
FROM
--** SSC-FDM-TD0010 - USES OF TABLE DBC.COLUMNSV ARE CONVERTED TO INFORMATION_SCHEMA.COLUMNS, BUT SOME COLUMNS MIGHT NOT HAVE AND EXACT MATCH IN SNOWFLAKE **
INFORMATION_SCHEMA.COLUMNS
WHERE
UPPER(RTRIM(TABLE_NAME)) = UPPER(RTRIM('TableN'));
```

#### Best Practices

* Review what columns were used in Teradata and check if the available content in Snowflake matches your needs.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0011

Unicode BMP escape is not supported.

### Description

Snowflake doesn’t support Unicode BMP, so this message is shown when SnowConvert AI transforms Teradata [Unicode Delimited Character Literal](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/SQL-Data-Types-and-Literals/Data-Literals/Unicode-Delimited-Character-Literals) with Unicode BMP escape to Snowflake.

#### Example code

##### Input Code

```sql
 SELECT U&'hola #+005132 mundo' UESCAPE '#';
```

##### Generated Code

```sql
 SELECT
--** SSC-FDM-TD0011 - UNICODE BMP IS NOT SUPPORTED IN SNOWFLAKE **
'hola \u+005132 mundo';
```

#### Best Practices

* Check if a Unicode equivalent exists.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0012

Invalid default value.

> **Note:**
>
> This FDM is deprecated, please refer to [SSC-EWI-TD0006](../conversion-issues/teradataEWI.md) documentation

### Description

The **DEFAULT TIME** / **DEFAULT DATE** / **DEFAULT CURREN_DATE** */* **DEFAULT DEFAULT CURRENT_TIME** */* **DEFAULT CURRENT_TIMESTAMP** column specifications are not supported for the **FLOAT** data type.

#### Example Code

##### Teradata

```sql
CREATE TABLE T_2004
(
    -- In the output code all of these columns will be FLOAT type
    -- and will include the SSC-FDM-TD0012 message.
    COL1 FLOAT DEFAULT TIME,
    COL2 FLOAT DEFAULT DATE,
    COL3 FLOAT DEFAULT CURRENT_DATE,
    COL4 FLOAT DEFAULT CURRENT_TIME,
    COL5 FLOAT DEFAULT CURRENT_TIMESTAMP
);
```

##### Snowflake Scripting

```sql
 CREATE TABLE T_2004
(
    -- In the output code all of these columns will be FLOAT type
    -- and will include the SSC-FDM-TD0012 message.
    COL1 FLOAT DEFAULT TIME /*** SSC-FDM-TD0012 - DEFAULT CURRENT_TIME NOT VALID FOR DATA TYPE ***/,
    COL2 FLOAT DEFAULT DATE /*** SSC-FDM-TD0012 - DEFAULT CURRENT_DATE NOT VALID FOR DATA TYPE ***/,
    COL3 FLOAT DEFAULT CURRENT_DATE /*** SSC-FDM-TD0012 - DEFAULT CURRENT_DATE NOT VALID FOR DATA TYPE ***/,
    COL4 FLOAT DEFAULT CURRENT_TIME /*** SSC-FDM-TD0012 - DEFAULT CURRENT_TIME NOT VALID FOR DATA TYPE ***/,
    COL5 FLOAT DEFAULT CURRENT_TIMESTAMP /*** SSC-FDM-TD0012 - DEFAULT CURRENT_TIMESTAMP NOT VALID FOR DATA TYPE ***/
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0013

The Snowflake error code doesn’t match the original Teradata error code.

### Description

This message is shown because the error code saved in the BTEQ ERRORCODE built-in variable could not be the same in Snowflake Scripting.

#### Example code

##### Input code

```sql
SELECT * FROM table1;

.IF ERRORCODE<>0 THEN .EXIT 1

.QUIT 0
```

##### Generated Code

```sql
 -- Additional Params: -q snowscript

EXECUTE IMMEDIATE
$$
  DECLARE
    STATUS_OBJECT OBJECT := OBJECT_CONSTRUCT('SQLCODE', 0);
  BEGIN
    BEGIN
      SELECT
        *
      FROM
        table1;
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLROWCOUNT', SQLROWCOUNT);
    EXCEPTION
      WHEN OTHER THEN
        STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
    END;
    IF (STATUS_OBJECT['SQLCODE'] /*** SSC-FDM-TD0013 - THE SNOWFLAKE ERROR CODE MISMATCH THE ORIGINAL TERADATA ERROR CODE ***/ != 0) THEN
      RETURN 1;
    END IF;
    RETURN 0;
  END
$$
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0014

File execution inconsistency

### Description

This EWI appears when the migrated code is a BTEQ sentence executing an environment file with SQL statements E.g. $(<$INPUT_SQL_FILE). The difference between the BTEQ execution and the python generated code is that BTEQ continues with the other statements in the file when one of them fails but the python execution stops whenever an error occurs.

#### Example Code

##### Teradata BTEQ

```sql
 .logmech LDAP;
.logon $LOGON_STR;
.SET DEFAULTS;

$(<$INPUT_SQL_FILE)

.export reset
.logoff
.quit
```

##### Python

```python
#*** Generated code is based on the SnowConvert AI Python Helpers version 2.0.6 ***

from snowconvert.helpers import exec_file
import os
import sys
import snowconvert.helpers
from snowconvert.helpers import Export
from snowconvert.helpers import exec
from snowconvert.helpers import BeginLoading
con = None
#** SSC-FDM-TD0022 - SHELL VARIABLES FOUND, RUNNING THIS CODE IN A SHELL SCRIPT IS REQUIRED **
def main():
  snowconvert.helpers.configure_log()
  con = snowconvert.helpers.log_on()
  #** SSC-FDM-0027 - REMOVED NEXT STATEMENT, NOT APPLICABLE IN SNOWFLAKE. LOGMECH **
  #.logmech LDAP;

  #** SSC-FDM-0027 - REMOVED NEXT STATEMENT, NOT APPLICABLE IN SNOWFLAKE. LOGON **
  #.logon $LOGON_STR

  #** SSC-EWI-TD0005 - THE STATEMENT WAS CONVERTED BUT ITS FUNCTIONALITY IS NOT IMPLEMENTED YET **
  Export.defaults()
  #** SSC-FDM-TD0014 - EXECUTION OF FILE WITH SQL STATEMENTS STOPS WHEN AN ERROR OCCURS **
  exec_file("$INPUT_SQL_FILE")
  #** SSC-EWI-TD0005 - THE STATEMENT WAS CONVERTED BUT ITS FUNCTIONALITY IS NOT IMPLEMENTED YET **
  Export.reset()
  #** SSC-FDM-0027 - REMOVED NEXT STATEMENT, NOT APPLICABLE IN SNOWFLAKE. LOGOFF **
  #.logoff

  snowconvert.helpers.quit_application()

if __name__ == "__main__":
  main()
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0015

Regexp_Substr Function only supports POSIX regular expressions.

> **Note:**
>
> This FDM is deprecated, please refer to [SSC-EWI-0009](../conversion-issues/generalEWI.md) documentation

### Description

Currently, there is no support in Snowflake for extended regular expression beyond the POSIX Basic Regular Expression syntax.

This EWI is added every time a function call to *REGEX_SUBSTR, REGEX_REPLACE,* or *REGEX_INSTR* is transformed to Snowflake to warn the user about possible unsupported regular expressions. Some of the features **not supported** are lookahead, lookbehind, and non-capturing groups.

#### Example Code

##### Teradata

```sql
 SELECT REGEXP_SUBSTR('qaqequ','q(?=u)', 1, 1);
```

##### Snowflake Scripting

```sql
 SELECT
--** SSC-FDM-TD0015 - REGEXP_SUBSTR FUNCTION ONLY SUPPORTS POSIX REGULAR EXPRESSIONS **
REGEXP_SUBSTR('qaqequ','q(?=u)', 1, 1);
```

#### Best Practices

* Check the regular expression used in each case to determine whether it needs manual intervention. More information about expanded regex support and alternatives in Snowflake can be found [**here**](https://community.snowflake.com/s/question/0D50Z00007ENLKsSAP/expanded-support-for-regular-expressions-regex)**.**
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0016

Value ‘l’ for parameter ‘match_arg’ is not supported in Snowflake

### Description

In Teradata functions like *REGEX_SUBSTR, REGEX_REPLACE,* or *REGEX_INSTR* have a parameter called *“match_arg*”, a character argument with the following valid values:

* `'i'`: case-insensitive matching.
* `'c'`: case sensitive matching.
* `'n'`: the period character (match any character) can match the newline character.
* `'m'`: source string is treated as multiple lines instead of as a single line.
* **`'l'`**: if source_string exceeds the current maximum allowed source_string size (currently 16 MB), a NULL is returned instead of an error.
* `'x'`: ignore whitespace (only affects the pattern string).

The argument can contain more than one character.

In Snowflake, the equivalent argument for these functions is *`regexp_parameters.`*A *s*tring of one or more characters that specifies the regular expression parameters used for searching for matches. The supported values are:

* `c`: case-sensitive.
* `i`: case-insensitive.
* `m`: multi-line mode.
* `e`: extract sub-matches.
* `s`: the ‘.’ the wildcard also matches the newline character as well.

As it can be seen, values `'i', 'c', 'm'` are the same in both languages, and the `'n'` value in Teradata is mapped to `'s'`. However, values `'l', 'x'` don’t have an equivalent counterpart.

For the `'x'` value, the functionality is replicated by generating a call to the `REGEXP_REPLACE` function. However, the `'l'` parameter can not be replicated so this warning is generated for these cases.

#### Input Code

```sql
 SELECT REGEXP_SUBSTR('Chip Chop','ch(i|o)p', 1, 1, 'i'),
       REGEXP_SUBSTR('Chip Chop','ch(i|o)p', 1, 1, 'c'),
       REGEXP_SUBSTR('Chip Chop','ch(i|o)p', 1, 1, 'm'),
       REGEXP_SUBSTR('Chip Chop','ch(i|o)p', 1, 1, 'n'),
       REGEXP_SUBSTR('Chip Chop','ch(i|o)p', 1, 1, 'l'),
       REGEXP_SUBSTR('Chip Chop','ch(i|o)p', 1, 1, 'x');
```

##### Generated Code

```sql
 SELECT
       REGEXP_SUBSTR('Chip Chop', 'ch(i|o)p', 1, 1, 'i'),
       REGEXP_SUBSTR('Chip Chop', 'ch(i|o)p', 1, 1, 'c'),
       REGEXP_SUBSTR('Chip Chop', 'ch(i|o)p', 1, 1, 'm'),
       REGEXP_SUBSTR('Chip Chop', 'ch(i|o)p', 1, 1, 's'),
       --** SSC-FDM-TD0016 - VALUE 'l' FOR PARAMETER 'match_arg' IS NOT SUPPORTED IN SNOWFLAKE **
       REGEXP_SUBSTR('Chip Chop', 'ch(i|o)p', 1, 1),
       REGEXP_SUBSTR('Chip Chop', 'ch(i|o)p', 1, 1);
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0017

The use of foreign tables is not supported in Snowflake.

> **Note:**
>
> This FDM is deprecated, please refer to [SSC-EWI-TD0076](../conversion-issues/teradataEWI.md) documentation

### Description

[Foreign tables](https://docs.teradata.com/r/Teradata-VantageTM-SQL-Data-Definition-Language-Syntax-and-Examples/September-2020/Table-Statements/CREATE-FOREIGN-TABLE) enable access to data in external object storage, such as semi-structured and unstructured data in Amazon S3, Azure Blob storage, and Google Cloud Storage. This syntax is not supported in Snowflake. However, there are other alternatives in Snowflake that can be used instead, such as external tables, iceberg tables, and standard tables.

#### Example code

##### Input code

```sql
 SELECT cust_id, income, age FROM
FOREIGN TABLE (SELECT cust_id, income, age FROM twm_customer)@hadoop1 T1;
```

##### Generated Code

```sql
 SELECT
cust_id,
income,
age FROM
--** SSC-FDM-TD0017 - THE USE OF FOREIGN TABLES IS NOT SUPPORTED IN SNOWFLAKE. **
 FOREIGN TABLE (SELECT cust_id, income, age FROM twm_customer)@hadoop1 T1;
```

#### Best Practices

* Instead of foreign tables in Teradata, you can use [Snowflake external tables](https://docs.snowflake.com/en/user-guide/tables-external.html). External tables reference data files located in a cloud storage (Amazon S3, Google Cloud Storage, or Microsoft Azure) data lake. This enables querying data stored in files in a data lake as if it were inside a database. External tables can access data stored in any format supported by [COPY INTO <table>](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table.html) statements.
* Another alternative is [Snowflake’s Iceberg tables](https://www.snowflake.com/blog/iceberg-tables-powering-open-standards-with-snowflake-innovations/?lang=es). So, you can think of Iceberg tables as tables that use open formats and customer-supplied cloud storage. This data is stored in Parquet files.
* Finally, there are the [standard Snowflake tables](https://docs.snowflake.com/en/sql-reference/sql/create-table.html) which can be an option to cover the functionality of foreign tables in Teradata
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0018

JSON path was not recognized

> **Note:**
>
> This FDM is deprecated, please refer to [SSC-EWI-TD0063](../conversion-issues/teradataEWI.md) documentation

### Description

This message is shown when SnowConvert AI cannot deserialize a JSON path, because the string does not have the expected format or is not supported in Snowflake.

#### Example code

##### Input Code

```sql
 SELECT
    *
FROM
JSON_TABLE (
    ON (
        SELECT
            id,
            trainSchedule as ts
        FROM
            demo.PUBLIC.Train T
    ) USING rowexpr('$weekShedule.Monday[*]') colexpr(
        '[{"jsonpath"  "$.time",
              "type"" : "CHAR ( 12 )"}]'
    )
) AS JT(Id, Ordinal, Time, City);
```

##### Generated Code

```sql
 SELECT
    *
FROM
    --** SSC-FDM-TD0018 - UNRECOGNIZED JSON PATH $weekShedule.Monday[*] **
JSON_TABLE (
    ON
       !!!RESOLVE EWI!!! /*** SSC-EWI-0108 - THE FOLLOWING SUBQUERY MATCHES AT LEAST ONE OF THE PATTERNS CONSIDERED INVALID AND MAY PRODUCE COMPILATION ERRORS ***/!!! (
           SELECT
               id,
               trainSchedule as ts
FROM
               demo.PUBLIC.Train T
    ) USING rowexpr('$weekShedule.Monday[*]') colexpr(
        '[{"jsonpath"  "$.time",
              "type"" : "CHAR ( 12 )"}]'
    )
) AS JT(Id, Ordinal, Time, City);
```

#### Best Practices

* Check if the JSON path have an unexpected character, or do not have the right format.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0019

Transaction and profile level query tags not supported in Snowflake, referencing session query tag instead

### Description

Teradata allows users to define query bands at transaction, session, and profile levels, as well as consulting them with functions like GetQueryBandValue.

Snowflake equivalent for query bands is the query_tag parameter, which can be set for session, user or account. Also, Snowflake does not have profiles.

Due to these differences, this FDM is added to warn the user that transaction or profile-level query tags can not be defined nor consulted in Snowflake and that session-level query tags will be used as a replacement, which may cause functional differences in some cases.

#### Example Code

##### Input Code

```sql
 SELECT GETQUERYBANDVALUE(3, 'account');
```

##### Generated Code

```sql
 SELECT
--** SSC-FDM-TD0019 - TRANSACTION AND PROFILE LEVEL QUERY TAGS NOT SUPPORTED IN SNOWFLAKE, REFERENCING SESSION QUERY TAG INSTEAD **
GETQUERYBANDVALUE_UDF('account');
```

#### Best Practices

* Modify your code logic to use query bands at the session level.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0020

JSON value was not recognized due to invalid format

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

This message is shown when SnowConvert AI needs to deserialize JSON data for a transformation context, but the JSON value didn’t have the expected format or is not valid JSON.

#### Example code

##### Input Code

```sql
 SELECT
*
FROM
 JSON_TABLE
(ON (SELECT id,
trainSchedule as ts
FROM demo.PUBLIC.Train T)
USING rowexpr('$.weekShedule.Monday[*]')
      colexpr('[ {"ordinal"  true},
                 {"jsonpath"  "$.time",
                  "type"" : "CHAR ( 12 )"},
                 {"jsonpath"  "$.city",
                  "type" : "VARCHAR ( 12 )"}]'))
AS JT(Id, Ordinal, Time, City);

SELECT
*
FROM
 JSON_TABLE
(ON (SELECT id,
trainSchedule as ts
FROM demo.PUBLIC.Train T)
USING rowexpr('$.weekShedule.Monday[*]')
      colexpr('{"jsonpath"  "$.time",
                  "type"" : "CHAR ( 12 )"}'))
AS JT(Id, Ordinal, Time, City);
```

##### Generated Code

```sql
 SELECT
 *
 FROM
 (
  SELECT
   id
  --** SSC-FDM-TD0020 - UNRECOGNIZED JSON LITERAL [ {"ordinal" true}, {"jsonpath" "$.time", "type"" : "CHAR ( 12 )"}, {"jsonpath" "$.city", "type" : "VARCHAR ( 12 )"}] **
  FROM
   demo.PUBLIC.Train T,
   TABLE(FLATTEN(INPUT =>
   trainSchedule:weekShedule.Monday)) rowexpr
 ) JT;

 SELECT
 *
 FROM
 (
  SELECT
   id
  --** SSC-FDM-TD0020 - UNRECOGNIZED JSON LITERAL {"jsonpath" "$.time", "type"" : "CHAR ( 12 )"} **
  FROM
   demo.PUBLIC.Train T,
   TABLE(FLATTEN(INPUT =>
   trainSchedule:weekShedule.Monday)) rowexpr
 ) JT;
```

#### Best Practices

* Be sure the JSON has the expected format according to the Teradata grammar.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0021

Built-in reference to {0} is not supported in Snowflake.

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-EWI-TD0046](../conversion-issues/teradataEWI.md) documentation

### Description

This error appears when a query referencing [DBC.DATABASES](https://www.docs.teradata.com/r/hNI_rA5LqqKLxP~Y8vJPQg/GqTx8VuBIkfaC4fso9f5cw) table is executed, and the selected column has no equivalence in Snowflake.

#### Example Code

##### Input

```sql
 CREATE VIEW SAMPLE_VIEW
AS
SELECT PROTECTIONTYPE FROM DBC.DATABASES;
```

##### Output

```sql
 CREATE OR REPLACE VIEW SAMPLE_VIEW
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "08/14/2024" }}'
AS
SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-TD0046 - BUILT-IN REFERENCE TO PROTECTIONTYPE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
PROTECTIONTYPE FROM
INFORMATION_SCHEMA.DATABASES;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0022

Shell variables found, running this code in a shell script is required.

### Description

In Teradata scripts, shell variables are used to store temporary values that can be accessed and manipulated throughout the script. Shell variables are defined using the dollar sign ($) followed by a name (which can be enclosed by curly braces), and their values can be set using the assignment operator (=).

```none
#!/bin/bash

## define a shell variable
tablename="mytable"

## use the variable in a Teradata SQL query
bteq <<EOF
    .LOGON myhost/myuser,mypassword
    SELECT * FROM ${tablename};
    .LOGOFF
EOF
```

You can think of shell variables having the same or similar function as string interpolation. Thus, it is important to keep this functionality when transformed.

When converting Scripts to Python, shell variables keep their functionality by running the converted code in a shell script (.sh file). For this reason, these shell variables must keep the same format as the input code.

### Example Code

#### Input Code

```sql
 SELECT $column FROM ${tablename}
```

##### Generated Code

```sql
 #*** Generated code is based on the SnowConvert AI Python Helpers version 2.0.6 ***

import os
import sys
import snowconvert.helpers
from snowconvert.helpers import Export
from snowconvert.helpers import exec
from snowconvert.helpers import BeginLoading
con = None
#** SSC-FDM-TD0022 - SHELL VARIABLES FOUND, RUNNING THIS CODE IN A SHELL SCRIPT IS REQUIRED **
def main():
  snowconvert.helpers.configure_log()
  con = snowconvert.helpers.log_on()
  exec("""
    SELECT
      $column
    FROM
      ${tablename}
    """)
  snowconvert.helpers.quit_application()

if __name__ == "__main__":
  main()
```

#### Best Practices

* Running the converted code in a shell script is required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0023

String Similarity might have a different behavior.

### Description

This FDM is shown when SnowConvert AI transforms the Similarity Function from Teradata to Snowflake. It indicates the results might have different behavior.

#### Example Code

Given the following data as an example

| Id | a | b |
| --- | --- | --- |
| 1 |  |  |
| 2 | Gute nacht | Ich weis nicht |
| 3 | Ich weiß nicht | Ich wei? nicht |
| 4 | Ich weiß nicht | Ich wei? nicht |
| 5 | Ich weiß nicht | Ich weiss nicht |
| 6 | Snowflake | Oracle |
| 7 | święta | swieta |
| 8 | NULL |  |
| 9 | NULL | NULL |

##### Input Code

##### Query

```sql
-- Additional Params: -q SnowScript
SELECT * FROM StringSimilarity (
  ON (
    SELECT id, CAST(a AS VARCHAR(200)) AS a, CAST(b AS VARCHAR(200)) AS b
    FROM table_1
  ) PARTITION BY ANY
  USING
  ComparisonColumnPairs ('jaro_winkler(a,b) AS sim_fn')
  Accumulate ('id')
) AS dt ORDER BY 1;
```

##### Result

| Id | sim_fn |
| --- | --- |
| 1 | 0 |
| 2 | 0.565079365 |
| 3 | 1 |
| 4 | 0.959047619 |
| 5 | 0 |
| 6 | 0.611111111 |
| 7 | 0.7777777777777777 |
| 8 | 0 |
| 9 | 0 |

##### Generated Code

##### Query

```sql
 SELECT
* FROM
--** SSC-FDM-TD0023 - STRING SIMILARITY MIGHT HAVE A DIFFERENT BEHAVIOR. **
(
   SELECT
     id,
     JAROWINKLER_UDF(a, b) AS sim_fn
   FROM table_1
 ) dt ORDER BY 1;
```

##### Result

| ID | SIM_FN |
| --- | --- |
| 1 | 0.000000 |
| 2 | 0.560000 |
| 3 | 0.970000 |
| 4 | 0.950000 |
| 5 | 0.000000 |
| 6 | 0.610000 |
| 7 | 0.770000 |
| 8 | 0.000000 |
| 9 | 0.000000 |

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0024

Set table functionality not supported.

### Description

This EWI is shown when SnowConvert AI finds a Create Table with the SET option. Since the SET TABLE is not supported in Snowflake, it is removed.

#### Example Code

##### Teradata

```sql
 CREATE SET TABLE TableExample
(
ColumnExample Number
)
```

```sql
 CREATE SET VOLATILE TABLE SOMETABLE, LOG AS
(SELECT ColumnExample FROM TableExample);
```

##### Snowflake Scripting

```sql
 --** SSC-FDM-TD0024 - SET TABLE FUNCTIONALITY NOT SUPPORTED. TABLE MIGHT HAVE DUPLICATE ROWS **
CREATE OR REPLACE TABLE TableExample
(
ColumnExample NUMBER(38, 18)
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
;
```

```sql
 --** SSC-FDM-TD0024 - SET TABLE FUNCTIONALITY NOT SUPPORTED. TABLE MIGHT HAVE DUPLICATE ROWS **
CREATE OR REPLACE TEMPORARY TABLE SOMETABLE
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
AS
(
SELECT
ColumnExample FROM
TableExample
);
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0025

Teradata Database Temporal Table is not supported in Snowflake

### Description

The [Teradata Database Temporal Support](https://docs.teradata.com/r/0TSAVrLIwk23SLHbA4nUvQ/root) involves the creation of temporal tables and temporal DDL and DML objects. The support for temporal (time-aware) tables and data are not supported in Snowflake since there is not an absolute equivalent.

All these statements are recognized (parsed) by SnowConvert AI, but to execute the queries in Snowflake, these elements are removed in the translation process.

It is worth noting that in cases where an `abort` statement is encountered, it will be transformed into a `Delete` command to keep the equivalence functionality allows you to undo operations performed during a transaction and restore the database to the state it had at the beginning.

#### Example code

The following example shows a Temporal-form Select being translated to a usual Select.

##### Input code

```sql
 SEQUENCED VALIDTIME
   SELECT
   Policy_ID,
   Customer_ID
   FROM Policy
      WHERE Policy_Type = 'AU';
```

##### Generated Code

```sql
 ----** SSC-FDM-TD0025 - TEMPORAL FORMS ARE NOT SUPPORTED IN SNOWFLAKE **
--SEQUENCED VALIDTIME
SELECT
   Policy_ID,
   Customer_ID
   FROM
   Policy
      WHERE
   UPPER(RTRIM( Policy_Type)) = UPPER(RTRIM('AU'));
```

Case where the `Abort` command is used in the context of a transaction.

##### Input code

```sql
 CREATE OR REPLACE PROCEDURE TEST.ABORT_STATS()
BEGIN
    CURRENT VALIDTIME AND NONSEQUENCED TRANSACTIONTIME ABORT
     FROM table_1
     WHERE table_1.x1 = 1;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE TEST.ABORT_STATS ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
EXECUTE AS CALLER
AS
$$
    BEGIN
        --    CURRENT VALIDTIME AND NONSEQUENCED TRANSACTIONTIME
        --** SSC-FDM-TD0025 - TEMPORAL FORMS ARE NOT SUPPORTED IN SNOWFLAKE **
        LET _ROW_COUNT FLOAT;
        SELECT
            COUNT(*)
        INTO
            _ROW_COUNT
            FROM
            table_1
                 WHERE table_1.x1 = 1;
            IF (_ROW_COUNT > 0) THEN
            ROLLBACK;
            END IF;
    END;
$$;
```

####

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0026

GOTO statement was removed due to if statement inversion.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

It is common to use GOTO command with IF and LABEL commands to replicate the functionality of an SQL if statement. When used in this way, it is possible to transform them directly into an if, if-else, or even an if-elseif-else statement. However, in these cases, the GOTO commands become unnecessary and should be removed to prevent them from being replaced by a LABEL section.

#### Example Code

**Input Code:**

```sql
 -- Additional Params: --scriptsTargetLanguage SnowScript
.If ActivityCount = 0 THEN .GOTO endIf
DROP TABLE TABLE1;
.Label endIf
SELECT A FROM TABLE1;
```

**Output Code**

```sql
 EXECUTE IMMEDIATE
$$
  DECLARE
    STATUS_OBJECT OBJECT := OBJECT_CONSTRUCT('SQLCODE', 0);
  BEGIN
    IF (NOT (STATUS_OBJECT['SQLROWCOUNT'] = 0)) THEN
      --** SSC-FDM-TD0026 - GOTO endIf WAS REMOVED DUE TO IF STATEMENT INVERSION **

      BEGIN
        DROP TABLE TABLE1;
        STATUS_OBJECT := OBJECT_CONSTRUCT('SQLROWCOUNT', SQLROWCOUNT);
      EXCEPTION
        WHEN OTHER THEN
          STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
      END;
    END IF;
    /*.Label endIf*/
    --** SSC-FDM-0027 - REMOVED NEXT STATEMENT, NOT APPLICABLE IN SNOWFLAKE.  **

    BEGIN
      SELECT
        A
      FROM
        TABLE1;
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLROWCOUNT', SQLROWCOUNT);
    EXCEPTION
      WHEN OTHER THEN
        STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
    END;
  END
$$
```

##### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0027

TD_UNPIVOT transformation requires column information that could not be found, columns missing in result

> **Note:**
>
> This FDM is deprecated, please refer to [SSC-EWI-TD0061](../conversion-issues/teradataEWI.md) documentation.

### Description

SnowConvert AI supports and transforms the [TD_UNPIVOT](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/SQL-Operators-and-User-Defined-Functions/Table-Operators/TD_UNPIVOT) function, which can be used to represent columns from a table as rows.

However, this transformation requires information about the table/tables columns to work, more specifically the names of the columns. When this information is not present the transformation may be left in an incomplete state where columns are missing from the result, this EWI is generated in these cases.

#### Example code

##### Input Code

```sql
 CREATE TABLE unpivotTable  (
 myKey INTEGER NOT NULL PRIMARY KEY,
 firstSemesterIncome DECIMAL(10,2),
 secondSemesterIncome DECIMAL(10,2),
 firstSemesterExpenses DECIMAL(10,2),
 secondSemesterExpenses DECIMAL(10,2)
);

SELECT * FROM
 TD_UNPIVOT(
  ON unpivotTable
  USING
  VALUE_COLUMNS('Income', 'Expenses')
  UNPIVOT_COLUMN('Semester')
  COLUMN_LIST('firstSemesterIncome, firstSemesterExpenses', 'secondSemesterIncome, secondSemesterExpenses')
  COLUMN_ALIAS_LIST('First', 'Second')
 )X ORDER BY mykey;

SELECT * FROM
 TD_UNPIVOT(
  ON unknownTable
  USING
  VALUE_COLUMNS('MonthIncome')
  UNPIVOT_COLUMN('Months')
  COLUMN_LIST('januaryIncome', 'februaryIncome', 'marchIncome', 'aprilIncome')
  COLUMN_ALIAS_LIST('January', 'February', 'March', 'April')
 )X ORDER BY yearKey;
```

##### Generated Code

```sql
 CREATE TABLE unpivotTable (
 myKey INTEGER NOT NULL PRIMARY KEY,
 firstSemesterIncome DECIMAL(10,2),
 secondSemesterIncome DECIMAL(10,2),
 firstSemesterExpenses DECIMAL(10,2),
 secondSemesterExpenses DECIMAL(10,2)
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"teradata"}}'
;

SELECT
 * FROM
 (
  SELECT
   myKey,
   TRIM(GET_IGNORE_CASE(OBJECT_CONSTRUCT('FIRSTSEMESTERINCOME', 'First', 'FIRSTSEMESTEREXPENSES', 'First', 'SECONDSEMESTERINCOME', 'Second', 'SECONDSEMESTEREXPENSES', 'Second'), Semester), '"') AS Semester,
   Income,
   Expenses
  FROM
   unpivotTable UNPIVOT(Income FOR Semester IN (
    firstSemesterIncome,
    secondSemesterIncome
   )) UNPIVOT(Expenses FOR Semester1 IN (
    firstSemesterExpenses,
    secondSemesterExpenses
   ))
  WHERE
   Semester = 'FIRSTSEMESTERINCOME'
   AND Semester1 = 'FIRSTSEMESTEREXPENSES'
   OR Semester = 'SECONDSEMESTERINCOME'
   AND Semester1 = 'SECONDSEMESTEREXPENSES'
 ) X ORDER BY mykey;

 SELECT
 * FROM
 --** SSC-FDM-TD0027 - TD_UNPIVOT TRANSFORMATION REQUIRES COLUMN INFORMATION THAT COULD NOT BE FOUND, COLUMNS MISSING IN RESULT **
 (
  SELECT
   TRIM(GET_IGNORE_CASE(OBJECT_CONSTRUCT('JANUARYINCOME', 'January', 'FEBRUARYINCOME', 'February', 'MARCHINCOME', 'March', 'APRILINCOME', 'April'), Months), '"') AS Months,
   MonthIncome
  FROM
   unknownTable UNPIVOT(MonthIncome FOR Months IN (
    januaryIncome,
    februaryIncome,
    marchIncome,
    aprilIncome
   ))
 ) X ORDER BY yearKey;
```

#### Best Practices

* There are two ways of supplying the information about columns to the conversion tool: put the table specification in the same file as the TD_UNPIVOT call or specify a column list in the SELECT query of the ON expression instead of SELECT \* or the table name.
* This issue can be safely ignored if ALL the columns from the input table/tables are unpivoted, otherwise, the result will have missing columns.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0028

JSON_TABLE not transformed, column names could not be retrieved from semantic information

> **Note:**
>
> This FDM is deprecated, please refer to [SSC-EWI-TD0060](../conversion-issues/teradataEWI.md) documentation.

### Description

The JSON_TABLE function can be transformed by SnowConvert AI, however, this transformation requires knowing the name of the columns that are being selected in the JSON_TABLE ON subquery.

This message is generated to warn the user that the column names were not explicitly put in the subquery (for example, a SELECT \* was used) and the semantic information of the tables being referenced was not found, meaning the column names could not be extracted.

#### Example code

##### Input Code

```sql
 CREATE TABLE demo.Train (
    firstCol INT,
    jsonCol JSON(400),
    thirdCol VARCHAR(30)
);

SELECT * FROM JSON_TABLE
(ON (SELECT T.*
           FROM demo.Train T)
USING rowexpr('$.schools[*]')
               colexpr('[ {"jsonpath" : "$.name",
                           "type" : "CHAR(20)"},
                          {"jsonpath" : "$.type",
                           "type" : "VARCHAR(20)"}]')
)
AS JT;

SELECT * FROM JSON_TABLE
(ON (SELECT T.*
           FROM demo.missingTable T)
USING rowexpr('$.schools[*]')
               colexpr('[ {"jsonpath" : "$.name",
                           "type" : "CHAR(20)"},
                          {"jsonpath" : "$.type",
                           "type" : "VARCHAR(20)"}]')
)
AS JT;
```

##### Generated Code

```sql
 CREATE TABLE demo.Train (
    firstCol INT,
    jsonCol VARIANT,
    thirdCol VARCHAR(30)
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;

SELECT
    * FROM
    (
        SELECT
            firstCol,
            rowexpr.value:name :: CHAR(20) AS Column_0,
            rowexpr.value:type :: VARCHAR(20) AS Column_1,
            thirdCol
        FROM
            demo.Train T,
            TABLE(FLATTEN(INPUT => jsonCol:schools)) rowexpr
    ) JT;

    SELECT
    * FROM
    --** SSC-FDM-TD0028 - JSON_TABLE NOT TRANSFORMED, COLUMN NAMES COULD NOT BE RETRIEVED FROM SEMANTIC INFORMATION **
    JSON_TABLE
   (ON
       !!!RESOLVE EWI!!! /*** SSC-EWI-0108 - THE FOLLOWING SUBQUERY MATCHES AT LEAST ONE OF THE PATTERNS CONSIDERED INVALID AND MAY PRODUCE COMPILATION ERRORS ***/!!! (
        SELECT
            T.*
                  FROM
            demo.missingTable T)
   USING rowexpr('$.schools[*]')
                  colexpr('[ {"jsonpath" : "$.name",
                           "type" : "CHAR(20)"},
                          {"jsonpath" : "$.type",
                           "type" : "VARCHAR(20)"}]')
   )
   AS JT;
```

#### Best Practices

* Please check the code provided to SnowConvert AI is complete, if you did not provide the table definition please re-execute the code with the table definition present.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0029

Snowflake supported formats for TO_CHAR differ from Teradata and may fail or have different behavior

### Format elements that depend on session parameters

Some Teradata format elements are mapped to Snowflake functions that depend on the value of session parameters. To avoid functional differences in the results you should set these session parameters to the same values they have in Teradata. Identified format elements that are mapped to this kind of functions are:

* **D**: Mapped to `DAYOFWEEK` function, the results of this function depend on the `WEEK_START` session parameter, by default Teradata considers Sunday as the first day of the week, while in Snowflake it is Monday.
* **WW**: Mapped to `WEEK` function, this function depends on the session parameter `WEEK_OF_YEAR_POLICY` which by default is set to use the ISO standard (the first week of year is the first to contain at least four days of January) but in Teradata is set to consider January first as the start of the first week.

To modify session parameters, use `ALTER SESSION SET parameter_name = value`. For more information, see the [Snowflake session parameters reference](https://docs.snowflake.com/en/sql-reference/parameters.html).

#### Single parameter version of TO_CHAR

The single parameter version of `TO_CHAR(Datetime)` makes use of the default formats specified in the session parameters `TIMESTAMP_LTZ_OUTPUT_FORMAT`, `TIMESTAMP_NTZ_OUTPUT_FORMAT`, `TIMESTAMP_TZ_OUTPUT_FORMAT` and `TIME_OUTPUT_FORMAT`. To avoid differences in behavior please set them to the same values used in Teradata.

For `TO_CHAR(Numeric)` Snowflake generates the varchar representation using either the `TM9` or `TME` formats to get a compact representation of the number, Teradata also generates compact representations of the numbers so no action is required.

#### Example Code

##### Input Code

```sql
 select to_char(date '2008-09-13', 'DD/RM/YYYY');

select to_char(date '2010-10-20', 'DS');

select to_char(1255.495, 'SC9999.9999', 'nls_iso_currency = ''EUR''');

select to_char(45620);
```

##### Generated Code

```sql
 SELECT
TO_CHAR(date '2008-09-13', 'DD/') || PUBLIC.ROMAN_NUMERALS_MONTH_UDF(date '2008-09-13') || TO_CHAR(date '2008-09-13', '/YYYY') /*** SSC-FDM-TD0029 - SNOWFLAKE SUPPORTED FORMATS FOR TO_CHAR DIFFER FROM TERADATA AND MAY FAIL OR HAVE DIFFERENT BEHAVIOR ***/;

SELECT
TO_CHAR(date '2010-10-20', 'MM/DD/YYYY') /*** SSC-FDM-TD0029 - SNOWFLAKE SUPPORTED FORMATS FOR TO_CHAR DIFFER FROM TERADATA AND MAY FAIL OR HAVE DIFFERENT BEHAVIOR ***/;

SELECT
PUBLIC.INSERT_CURRENCY_UDF(TO_CHAR(1255.495, 'S9999.0000'), 2, 'EUR') /*** SSC-FDM-TD0029 - SNOWFLAKE SUPPORTED FORMATS FOR TO_CHAR DIFFER FROM TERADATA AND MAY FAIL OR HAVE DIFFERENT BEHAVIOR ***/;

SELECT
TO_CHAR(45620) /*** SSC-FDM-TD0029 - SNOWFLAKE SUPPORTED FORMATS FOR TO_CHAR DIFFER FROM TERADATA AND MAY FAIL OR HAVE DIFFERENT BEHAVIOR ***/;
```

### Best Practices

* When using FF either try to use DateTime types with the same precision that you use in Teradata or add a precision to the format element to avoid the different behavior.
* When using timezone-related format elements, use the first parameter of type `TIMESTAMP_TZ` to avoid different behavior. Also remember that the `TIME` type cannot have time zone information in Snowflake.
* Set the necessary session parameters with the default values from Teradata to avoid different behavior.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0030

A return statement was added at the end of the label section to ensure the same execution flow

### Description

When a Goto statement is replaced with a Label section and does not contain a return statement, one is added at the end of the section to ensure the same execution flow.

BTEQ after a Goto command is executed, the statements between the goto command and the label command with the same name are ignored. So, to avoid those statements being executed the label section should contain a return statement.

In addition, it is worth value mentioning the Goto command skips all the other statements except for the Label with the same name, which is when the execution resumes. Therefore, the execution will never resume in a label section defined before the Goto command.

#### Example Code

##### Input Code

```sql
 -- Additional Params: --scriptsTargetLanguage SnowScript
.LOGON dbc,dbc;
select 'STATEMENTS';
.GOTO LABEL_B
select 'IGNORED STATEMENTS';
.label LABEL_B
select 'LABEL_B STATEMENTS';
```

##### Generated Code

```sql
 EXECUTE IMMEDIATE
$$
  DECLARE
    STATUS_OBJECT OBJECT := OBJECT_CONSTRUCT('SQLCODE', 0);
  BEGIN
    -- Additional Params: --scriptsTargetLanguage SnowScript
    --.LOGON dbc,dbc
    !!!RESOLVE EWI!!! /*** SSC-EWI-0073 - PENDING FUNCTIONAL EQUIVALENCE REVIEW FOR 'BTLogOn' NODE ***/!!!
    null;
    BEGIN
      SELECT
        'STATEMENTS';
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLROWCOUNT', SQLROWCOUNT);
    EXCEPTION
      WHEN OTHER THEN
        STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
    END;

    /*.label LABEL_B*/

    BEGIN
      SELECT
        'LABEL_B STATEMENTS';
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLROWCOUNT', SQLROWCOUNT);
    EXCEPTION
      WHEN OTHER THEN
        STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
    END;
    --** SSC-FDM-TD0030 - A RETURN STATEMENT WAS ADDED AT THE END OF THE LABEL SECTION LABEL_B TO ENSURE THE SAME EXECUTION FLOW **
    RETURN 0;
    BEGIN
      SELECT
        'IGNORED STATEMENTS';
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLROWCOUNT', SQLROWCOUNT);
    EXCEPTION
      WHEN OTHER THEN
        STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
    END;
    /*.label LABEL_B*/
    --** SSC-FDM-0027 - REMOVED NEXT STATEMENT, NOT APPLICABLE IN SNOWFLAKE.  **

    BEGIN
      SELECT
        'LABEL_B STATEMENTS';
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLROWCOUNT', SQLROWCOUNT);
    EXCEPTION
      WHEN OTHER THEN
        STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
    END;
  END
$$
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0031

ST_DISTANCE results are slightly different from ST_SPHERICALDISTANCE

### Description

The Teradata function ST_SPHERICALDISTANCE calculates the distance between two spherical coordinates on the planet using the Haversine formula, on the other side, the Snowflake ST_DISTANCE function does not utilize the haversine formula to calculate the minimum distance between two geographical points.

#### Example Code

##### Input Code

```sql
 --The distance between New York and Los Angeles
Select Cast('POINT(-73.989308 40.741895)' As ST_GEOMETRY) As location1,
 Cast('POINT(40.741895 34.053691)' As ST_GEOMETRY) As location2,
 location1.ST_SPHERICALDISTANCE(location2) As Distance_In_km;
```

##### Teradata Output

| location1 | location2 | Distance_In_Km |
| --- | --- | --- |
| POINT (-73.989308 40.741895) | POINT (40.741895 34.053691) | 9351139.978062356 |

##### Generated Code

```sql
 --The distance between New York and Los Angeles
SELECT
 TO_GEOGRAPHY('POINT(-73.989308 40.741895)') As location1,
 TO_GEOGRAPHY('POINT(40.741895 34.053691)') As location2,
 --** SSC-FDM-TD0031 - ST_DISTANCE RESULTS ARE SLIGHTLY DIFFERENT FROM ST_SPHERICALDISTANCE **
 ST_DISTANCE(
 location1, location2) As Distance_In_km;
```

##### Snowflake Output

| LOCATION1 | LOCATION2 | DISTANCE_IN_KM |
| --- | --- | --- |
| { “coordinates”: [ -73.989308, 40.741895 ], “type”: “Point” } | { “coordinates”: [ 40.741895, 34.053691 ], “type”: “Point” } | 9351154.65572674 |

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0032

CASESPECIFIC clause was removed from LIKE expression

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

This error appears when the `LIKE` expression is accompanied by the `[NOT] CASESPECIFIC` clause.

#### Example Code

##### Input Code

```sql
 SELECT * FROM MY_TABLE
WHERE Name Like 'Marco%' (NOT CASESPECIFIC);
```

##### Generated Code

```sql
 SELECT
    * FROM
    MY_TABLE
WHERE Name ILIKE 'Marco%' /*** SSC-FDM-TD0032 - NOT CASESPECIFIC CLAUSE WAS REMOVED ***/;
```

#### Best Practices

* Case-Specific Behavior in TERADATA depends on TMODE system configuration.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0033

ACTIVITY_COUNT transformation might require manual adjustments

### Description

The `ACTIVITY_COUNT` status variable returns the number of rows affected by an SQL DML statement in an embedded SQL or stored procedure application. For more information, see the [Teradata ACTIVITY_COUNT documentation](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/SQL-Stored-Procedures-and-Embedded-SQL/Result-Code-Variables/ACTIVITY_COUNT).

As explained in its translation specification, there is a workaround to emulate `ACTIVITY_COUNT`’s behavior through:

```sql
 SELECT $1 FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()));
```

However, this presents some limitations listed below.

### Limitations

#### First case

If `ACTIVITY_COUNT` is called twice or more times before executing another DML statement, the transformation might not return the expected values.

##### Teradata

```sql
 REPLACE PROCEDURE InsertEmployeeSalaryAndLog_1 ()
BEGIN
    DECLARE row_count1 INT;

    INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
    VALUES (101, 'Alice', 'Smith', 10, 70000.00);

    -- Get the ACTIVITY_COUNT
    SET row_count1 = ACTIVITY_COUNT;
    SET row_count1 = ACTIVITY_COUNT;

    -- Insert the ACTIVITY_COUNT into the activity_log table
    INSERT INTO activity_log (operation, row_count)
    VALUES ('INSERT PROCEDURE', row_count1);
END;

REPLACE PROCEDURE InsertEmployeeSalaryAndLog_2 ()
BEGIN
    DECLARE row_count1 INT;
    DECLARE message VARCHAR(100);

    INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
    VALUES (101, 'Alice', 'Smith', 10, 70000.00);

    -- Get the ACTIVITY_COUNT
    SET row_count1 = ACTIVITY_COUNT + 1;
    SET row_count1 = ACTIVITY_COUNT;

    -- Insert the ACTIVITY_COUNT into the activity_log table
    INSERT INTO activity_log (operation, row_count)
    VALUES ('INSERT PROCEDURE', row_count1);
END;
```

##### Snowflake

```sql
 CREATE OR REPLACE PROCEDURE InsertEmployeeSalaryAndLog_1 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/15/2024" }}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        row_count1 INT;
    BEGIN

        INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
        VALUES (101, 'Alice', 'Smith', 10, 70000.00);

           -- Get the ACTIVITY_COUNT
        row_count1 := (
            SELECT
                $1
            FROM
                TABLE(RESULT_SCAN(LAST_QUERY_ID()))
        ) /*** SSC-FDM-TD0033 - 'ACTIVITY_COUNT' TRANSFORMATION MIGHT REQUIRE MANUAL ADJUSTMENTS ***/;
        row_count1 := (
            SELECT
                $1
            FROM
                TABLE(RESULT_SCAN(LAST_QUERY_ID()))
        ) /*** SSC-FDM-TD0033 - 'ACTIVITY_COUNT' TRANSFORMATION MIGHT REQUIRE MANUAL ADJUSTMENTS ***/;

        -- Insert the ACTIVITY_COUNT into the activity_log table
        INSERT INTO activity_log (operation, row_count)
        VALUES ('INSERT PROCEDURE', :row_count1);
    END;
$$;

CREATE OR REPLACE PROCEDURE InsertEmployeeSalaryAndLog_2 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/15/2024" }}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        row_count1 INT;
        message VARCHAR(100);
    BEGIN

        INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
        VALUES (101, 'Alice', 'Smith', 10, 70000.00);

           -- Get the ACTIVITY_COUNT
        row_count1 := (
            SELECT
                $1
            FROM
                TABLE(RESULT_SCAN(LAST_QUERY_ID()))
        ) /*** SSC-FDM-TD0033 - 'ACTIVITY_COUNT' TRANSFORMATION MIGHT REQUIRE MANUAL ADJUSTMENTS ***/ + 1;
        row_count1 := (
            SELECT
                $1
            FROM
                TABLE(RESULT_SCAN(LAST_QUERY_ID()))
        ) /*** SSC-FDM-TD0033 - 'ACTIVITY_COUNT' TRANSFORMATION MIGHT REQUIRE MANUAL ADJUSTMENTS ***/;

        -- Insert the ACTIVITY_COUNT into the activity_log table
        INSERT INTO activity_log (operation, row_count)
        VALUES ('INSERT PROCEDURE', :row_count1);
    END;
$$;
```

In both procedures, `ACTIVITY_COUNT` is called twice before another DML statement is called. In Teradata, `ACTIVITY_COUNT` will return the number of rows in the `INSERT` statement above them, even when called twice. However, since the Snowflake transformation uses `LAST_QUERY_ID()`, the result depends on the result set held by `LAST_QUERY_ID()`.

`InsertEmployeeSalaryAndLog_1()` requires no manual adjustments. Check the Query History (bottom-up):

1. `INSERT` statement is executed. `LAST_QUERY_ID()` will point to this statement.
2. `SELECT` (first `ACTIVITY_COUNT`) is executed, and `$1` will be `1`. `LAST_QUERY_ID()` will point to this statement.
3. `SELECT` (second `ACTIVITY_COUNT`) is executed; since the last statement result was `1`, `$1` will be `1` for this `SELECT` as well.
4. Finally, `row_count1` holds the value `1`, which is inserted in `activity_log`.

On the other side, `InsertEmployeeSalaryAndLog_2()` does require manual adjustments. Check the Query History (bottom-up):

1. `INSERT` statement is executed. `LAST_QUERY_ID()` will point to this statement.
2. SELECT (first `ACTIVITY_COUNT`) is executed, and `$1` will be `1`. However, notice how `QUERY_TEXT` has the `+ 10`; this will affect the result that will be scanned. `LAST_QUERY_ID()` will point to this statement.
3. `SELECT` (second `ACTIVITY_COUNT`) is executed. The result for the last query is `11`; thus `$1` will hold `11` instead of the expected `1`.
4. Finally, `row_count1` holds the value `11`, which is inserted in `activity_log`.

These are the values inserted in `activity_log`:

| LOG_ID | OPERATION | ROW_COUNT | LOG_TIMESTAMP |
| --- | --- | --- | --- |
| 1 | INSERT PROCEDURE | 1 | 2024-07-15 09:22:21.725 |
| 101 | INSERT PROCEDURE | 11 | 2024-07-15 09:22:26.248 |

#### Adjustments for the first case

As per Snowflake’s documentation for [LAST_QUERY_ID](https://docs.snowflake.com/en/sql-reference/functions/last_query_id), you can specify the query to return, based on the position of the query. `LAST_QUERY_ID(-1)` returns the latest query, `(-2)` the second last query, and so on.

The fix for the problem in `InsertEmployeeSalaryAndLog_2()` will be to simply specify `LAST_QUERY_ID(-2)` in the second use of `ACTIVITY_COUNT` (second `SELECT`) so that it gets the results from the `INSERT` statement instead:

```sql
 ...
INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
        VALUES (101, 'Alice', 'Smith', 10, 70000.00);

           -- Get the ACTIVITY_COUNT
        row_count1 := (
            SELECT
                $1
            FROM
                TABLE(RESULT_SCAN(LAST_QUERY_ID()))
        ) /*** SSC-FDM-TD0033 - 'ACTIVITY_COUNT' TRANSFORMATION MIGHT REQUIRE MANUAL ADJUSTMENTS ***/ + 1;
        row_count1 := (
            SELECT
                $1
            FROM
                TABLE(RESULT_SCAN(LAST_QUERY_ID(-2)))
        ) /*** SSC-FDM-TD0033 - 'ACTIVITY_COUNT' TRANSFORMATION MIGHT REQUIRE MANUAL ADJUSTMENTS ***/;
...
```

#### Second case

If `ACTIVITY_COUNT` is called after a non DML statement was executed, the transformation will not return the expected values.

##### Teradata

```sql
REPLACE PROCEDURE InsertEmployeeSalaryAndLog_3 ()
BEGIN
    DECLARE row_count1 INT;
    DECLARE emp_id INT;
    DECLARE message VARCHAR(100);

    INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
    VALUES (101, 'Alice', 'Smith', 10, 70000.00);

    SELECT employee_id INTO emp_id FROM employees;
    -- Get the ACTIVITY_COUNT
    SET row_count1 = ACTIVITY_COUNT;
    SET message = 'EMPLOYEE INSERTED - ID: ' || emp_id;

    -- Insert the ACTIVITY_COUNT into the activity_log table
    INSERT INTO activity_log (operation, row_count)
    VALUES (message, row_count1);
END;
```

##### Snowflake

```sql
 CREATE OR REPLACE PROCEDURE InsertEmployeeSalaryAndLog_3 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/15/2024" }}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        row_count1 INT;
        emp_id INT;
        message VARCHAR(100);
    BEGIN

        INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
        VALUES (101, 'Alice', 'Smith', 10, 70000.00);
        SELECT
            employee_id INTO
            :emp_id
        FROM
            employees;
               -- Get the ACTIVITY_COUNT
               row_count1 := (
            SELECT
                $1
            FROM
                TABLE(RESULT_SCAN(LAST_QUERY_ID()))
               ) /*** SSC-FDM-TD0033 - 'ACTIVITY_COUNT' TRANSFORMATION MIGHT REQUIRE MANUAL ADJUSTMENTS ***/;
               message := 'EMPLOYEE INSERTED - ID: ' || emp_id;

               -- Insert the ACTIVITY_COUNT into the activity_log table
               INSERT INTO activity_log (operation, row_count)
               VALUES (:message, :row_count1);
    END;
$$;
```

Similar to the previous, `LAST_QUERY_ID` does not point to the correct query and thus returns an incorrect value, which is assigned to row_count1. Check the Query History (bottom-up):

1. `INSERT` statement is executed. `LAST_QUERY_ID()` will point to this statement.
2. `SELECT INTO` is executed, and $1 will be 101. `LAST_QUERY_ID()` will point to this statement.
3. `SELECT` (`ACTIVITY_COUNT`) is executed. The result for the last query is `101`; thus `$1` will hold `101` instead of the expected 1.
4. Finally, `row_count1` holds the value `101`, which is inserted in `activity_log`.

These are the values inserted in activity_log:

| LOG_ID | OPERATION | ROW_COUNT | LOG_TIMESTAMP |
| --- | --- | --- | --- |
| 1 | EMPLOYEE INSERTED - ID: 101 | 101 | 2024-07-15 11:00:38.000 |

#### Adjustments for the second case

1. One possible fix is to specify the correct query to return by `LAST_QUERY_ID`. For example, here `LAST_QUERY_ID(-2)` will be the correct query to point to.

```sql
 ...
row_count1 := (
            SELECT
                $1
            FROM
                TABLE(RESULT_SCAN(LAST_QUERY_ID(-2)))
               ) /*** SSC-FDM-TD0033 - 'ACTIVITY_COUNT' TRANSFORMATION MIGHT REQUIRE MANUAL ADJUSTMENTS ***/;
               ...
```

1. Another possible fix is to use `ACTIVITY_COUNT` (`SELECT`) immediately after executing the `INSERT` statement.

```sql
...
INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
VALUES (101, 'Alice', 'Smith', 10, 70000.00);
-- Get the ACTIVITY_COUNT
       row_count1 := (
    SELECT
        $1
    FROM
        TABLE(RESULT_SCAN(LAST_QUERY_ID()))
       ) /*** SSC-FDM-TD0033 - 'ACTIVITY_COUNT' TRANSFORMATION MIGHT REQUIRE MANUAL ADJUSTMENTS ***/;
SELECT
    employee_id INTO
    :emp_id
FROM
    employees;
       message := 'EMPLOYEE INSERTED - ID: ' || emp_id;
...
```

#### Best Practices

* Make sure to point to the correct query when using `LAST_QUERY_ID`.
* Make sure `ACTIVITY_COUNT` is used immediately after the DML statement to evaluate.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0034

Period contains transformed to user defined function.

### Description

The Teradata `CONTAINS` expression performs a validation indicating whether the element at the right is contained in the element at the left which is supposed to be of `PERIOD` type. The CONTAINS only applies for `DATE`, `TIME`, `TIMESTAMP` or `PERIOD`. Since `PERIOD` is not supported in Snowflake, an user-defined function will emulate the logic of the native `CONTAINS` behavior.

#### Example Code

##### Input Code

```sql
  UPDATE TABLE1
  SET COL1 = CURRENT_TIMESTAMP
  WHERE COL3 CONTAINS CURRENT_TIMESTAMP;
```

##### Generated Code

```sql
  UPDATE TABLE1
  SET
    COL1 = CURRENT_TIMESTAMP()
  WHERE
    PUBLIC.PERIOD_CONTAINS_UDF(COL3, CURRENT_TIMESTAMP()) /*** SSC-FDM-TD0034 - PERIOD CONTAINS EXPRESSION TRANSFORMED TO USER DEFINED FUNCTION. ***/
```

#### Best Practices

* The `VARCHAR` used instead of `PERIOD` assumes `<PERIOD_BEGIN>*<PERIOD_END>` format in all the values. If the values are split by a token different than `*`, you can change the value returned from the `PUBLIC.GET_PERIOD_SEPARATOR` UDF provided by SnowConvert AI. Notice that the structure should have a token that marks the begin and end of a PERIOD, so the two dates, times or timestamps should be always separated with the same token.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0035

Statistics function not needed in Snowflake.

> **Note:**
>
> This FDM is deprecated, please refer to [SSC-EWI-0037](generalFDM.md) documentation

### Description

DROP, COLLECT, or HELP statistics are not needed in Snowflake. Snowflake already collects statistics used for automatic query optimization, which is why these statistics statements are used in Teradata.

#### Example Code

##### Input Code

```sql
  HELP STATISTICS TestName;
```

##### Generated Code

```sql
  ----** SSC-FDM-TD0035 - HELP STATISTICS NOT NEEDED. SNOWFLAKE AUTOMATICALLY COLLECTS STATISTICS. **
  --HELP STATISTICS TestName
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0036

Snowflake does not support the period datatype, all periods are handled as varchar instead

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Precision of generated varchar representations

PERIOD_UDF generates the varchar representation of a period using the default formats for timestamps and time specified in Snowflake, this means timestamps will have three precision digits and time variables will have zero, because of this you may find that the results have a higher/lower precision from the expected, there are two options to modify how many precision digits are included in the resulting string:

* Use the three parameters version of PERIOD_UDF: This overload of the function takes the`PRECISIONDIGITS`parameter, an integer between 0 and 9 to control how many digits of the fractional time part will be included in the result. Note that even if Snowflake supports up to nine digits of precision the maximum in Teradata is six. Example:

| Call | Result |
| --- | --- |
| `PUBLIC.PERIOD_UDF(time '13:30:45.870556', time '15:35:20.344891', 0)` | `'13:30:45*15:35:20'` |
| `PUBLIC.PERIOD_UDF(time '13:30:45.870556', time '15:35:20.344891', 2)` | `'13:30:45.87*15:35:20.34'` |
| `PUBLIC.PERIOD_UDF(time '13:30:45.870556', time '15:35:20.344891', 5)` | `'13:30:45.87055*15:35:20.34489'` |

* Alter the session parameters `TIMESTAMP_NTZ_OUTPUT_FORMAT` and `TIME_OUTPUT_FORMAT`: The commands `ALTER SESSION SET TIMESTAMP_NTZ_OUTPUT_FORMAT = <format>` and`ALTER SESSION SET TIME_OUTPUT_FORMAT = <format>`

  can be used to modify the formats Snowflake uses by default for the current session, modifying them to include the desired number of precision digits changes the result of future executions of PERIOD_UDF for the current session.

#### Example code

##### Input code

```sql
 create table vacations (
    employeeName varchar(50),
    duration period(date)
);

insert into vacations values ('Richard', period(date '2021-05-15', date '2021-06-15'));

select end(duration) from vacations;
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE vacations (
    employeeName varchar(50),
    duration VARCHAR(24) /*** SSC-FDM-TD0036 - SNOWFLAKE DOES NOT SUPPORT THE PERIOD DATATYPE, ALL PERIODS ARE HANDLED AS VARCHAR INSTEAD ***/
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;

INSERT INTO vacations
VALUES ('Richard', PUBLIC.PERIOD_UDF(date '2021-05-15', date '2021-06-15') /*** SSC-FDM-TD0036 - SNOWFLAKE DOES NOT SUPPORT THE PERIOD DATATYPE, ALL PERIODS ARE HANDLED AS VARCHAR INSTEAD ***/);

SELECT
    PUBLIC.PERIOD_END_UDF(duration) /*** SSC-FDM-TD0036 - SNOWFLAKE DOES NOT SUPPORT THE PERIOD DATATYPE, ALL PERIODS ARE HANDLED AS VARCHAR INSTEAD ***/ from
    vacations;
```

#### Best Practices

* Since the behavior of`PERIOD`and its related functions is emulated using varchar, we recommend reviewing the results obtained to ensure its correctness.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0037

LOGTABLE removed.

### Description

The [`.LOGTABLE`](https://docs.teradata.com/r/Enterprise_IntelliFlex_Lake_VMware/Teradata-MultiLoad-Reference-20.00/Teradata-MultiLoad-Commands/LOGTABLE) command in [MLoad](https://docs.teradata.com/r/Enterprise_IntelliFlex_Lake_VMware/Teradata-MultiLoad-Reference-20.00/Using-Teradata-MultiLoad) is used for checkpoint and restart metadata, but Snowflake handles these features automatically. Instead of `.LOGTABLE`, you can monitor and audit your data loads in Snowflake using the [`COPY_HISTORY`](https://docs.snowflake.com/en/sql-reference/functions/copy_history) function and related [account usage views](https://docs.snowflake.com/en/sql-reference/account-usage).

#### Code Example

##### Input Code

```sql
.LOGTABLE ${DATABASE}.LT_EMPLOYEES;
```

##### Generated Code

```sql
--** SSC-FDM-TD0037 - REMOVED NEXT STATEMENT. USE COPY_HISTORY() FOR MONITORING **
-- .LOGTABLE ${DATABASE}.LT_EMPLOYEES;
```

#### Best Practices

* Use [`COPY_HISTORY`](https://docs.snowflake.com/en/sql-reference/functions/copy_history) and related Snowflake account usage views to monitor load history.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0038

PUT command requires SnowSQL execution.

### Description

The [`PUT`](https://docs.snowflake.com/en/sql-reference/sql/put) command lets you upload files to a Snowflake [stage](https://docs.snowflake.com/en/sql-reference/sql/create-stage), but it only works when you run your script with [SnowSQL](https://docs.snowflake.com/en/user-guide/snowsql). It won’t work inside scripts, procedures, or the web UI. If your script includes a `PUT` command, make sure to run it using SnowSQL.

#### Code Example

##### Generated Code

```sql
CREATE TEMPORARY STAGE IF NOT EXISTS sc_import_stage;

--** SSC-FDM-TD0038 - PUT COMMAND REQUIRES EXECUTION THROUGH SNOWSQL. **
PUT file://employees.csv @sc_import_stage;

EXECUTE IMMEDIATE
$$
  DECLARE
    STATUS_OBJECT OBJECT := OBJECT_CONSTRUCT('SQLCODE', 0);
  BEGIN
    BEGIN
      COPY INTO employees (
        employee_id,
        first_name,
        last_name
      )
      FROM
      (
        SELECT
          $1,
          $2,
          $3
        FROM
          @sc_import_stage/employees.csv
      )
      FILE_FORMAT = (TYPE = CSV FIELD_DELIMITER = ',')
      ON_ERROR = 'CONTINUE';
    END;
  EXCEPTION
    WHEN OTHER CONTINUE THEN
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
  END
$$
```

#### Best Practices

* Run scripts containing [`PUT`](https://docs.snowflake.com/en/sql-reference/sql/put) commands using [SnowSQL](https://docs.snowflake.com/en/user-guide/snowsql).
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TD0039

Collation handled at query level for this table, any new query over this table should apply collation appropriately.

### Description

When the “Disable use of COLLATE for Case Specification” [general conversion setting](../../../getting-started/running-snowconvert/conversion/teradata-conversion-settings.md) is enabled, SnowConvert AI will emulate the case insensitive behavior of the NOT CASESPECIFIC clause by modifying comparisons in queries with the UPPER function, this is performed at query level instead of using collation at the column level. This warning will be generated on any table whose case sensitivity is being emulated at the query level to remind the user that any new query over these tables will require to properly handle the case sensitivity behavior on comparisons.

#### Example code

##### Input code

```sql
CREATE TABLE my_table
(
    col1 VARCHAR(50) NOT CASESPECIFIC
);

SELECT * FROM my_table WHERE col1 = 'test';
```

##### Generated Code

```sql
--** SSC-FDM-TD0039 - COLLATION HANDLED AT QUERY LEVEL FOR THIS TABLE, ANY NEW QUERY OVER THIS TABLE SHOULD APPLY COLLATION APPROPRIATELY **
CREATE OR REPLACE TABLE my_table
(
    col1 VARCHAR(50)
);

SELECT
    * FROM
    my_table
WHERE
    UPPER(RTRIM( col1)) = UPPER(RTRIM('test'));
```

#### Best Practices

* If you provided all your queries over the table to SnowConvert as part of your transformation then no additional actions are required, this FDM is informational only.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
