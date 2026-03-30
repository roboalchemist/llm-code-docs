# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/conversion-issues/teradataEWI.md

# SnowConvert AI - Teradata Issues

## SSC-EWI-TD0001

Recursive forward alias error.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Low

#### Description

This EWI is shown whenever SnowConvert AI detects recursion within aliased expressions, therefore being unable to execute the Forward Alias transformation required for the correct functionality of aliases within Snowflake environment.

A recursive alias happens when an aliased expression contains another alias, and the second aliased expression contains the first alias. This may not be as trivial as the example shows, since the recursion can happen further down the line in a *transitive* way.

#### Example Code

**Note:** Recursive aliases are not supported in Snowflake, however, some simple instances are.

> **Note:**
>
> Note that recursive alias is not supported in Snowflake, however, some simple instances are. Check the examples below.

The following example code works in Snowflake after migration:

##### Teradata

```sql
 SELECT
    COL1 AS COL2,
    COL2 AS COL1
FROM
    TABLE_EXAMPLE;
```

##### Snowflake Scripting

```sql
 // SnowConvert AI Helpers Code section is omitted.
SELECT
    COL1 AS COL2,
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0001 - 'COL1' HAS RECURSIVE REFERENCES. FORWARD ALIAS CONVERSION COULD NOT BE COMPLETED ***/!!!
    COL2 AS COL1
FROM
    TABLE_EXAMPLE;
```

However, the following example code does not work:

##### Teradata

```sql
 SELECT
    A + B as C,
    COL2 + C AS A,
    COL3 AS B
FROM
    TABLE_EXAMPLE;
```

##### Snowflake Scripting

```sql
 // SnowConvert AI Helpers Code section is omitted.
SELECT
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0001 - 'A' HAS RECURSIVE REFERENCES. FORWARD ALIAS CONVERSION COULD NOT BE COMPLETED ***/!!!
    COL2 + C AS A,
    COL3 AS B,
    A + B as C
FROM
    TABLE_EXAMPLE;
```

#### Best Practices

* Review your code and make sure recursive forward aliases are not present. The EWI shows the name of the first instance of an alias that has recursive references, but that does not mean that is the only one that has them in your code.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0002

Interval type not supported.

This EWI is deprecated since SnowConvert AI 28.1.100 release

### Severity

High

#### Description

When the selector of a column in a SQL statement is type INTERVAL, the EWI will be added and a Stub function will be created too. This is a type that is not supported in Snowflake and therefore implies pending work after SnowConvert AI finishes.

#### Example Code

##### Teradata

```sql
 SELECT
     CAST('07:00' AS INTERVAL HOUR(2) TO MINUTE),
     CAST('08:00' AS INTERVAL HOUR(2) TO MINUTE) As Test_Interval;
```

##### Snowflake Scripting

```sql
 SELECT
     !!!RESOLVE EWI!!! /*** SSC-EWI-TD0002 - INTERVAL TYPE NOT SUPPORTED IN SNOWFLAKE ***/!!!
     INTERVAL '07 hour, 00 min',
     !!!RESOLVE EWI!!! /*** SSC-EWI-TD0002 - INTERVAL TYPE NOT SUPPORTED IN SNOWFLAKE ***/!!!
     INTERVAL '08 hour, 00 min' As Test_Interval;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0003

Collation not supported in trim functions, add original collation to function result to preserve it.

### Severity

Low

#### Description

In Snowflake, trim functions (`LTRIM, RTRIM,` or `TRIM`) do not support collation unless the characters to trim are empty or white space characters.

If SnowConvert AI detects a `LTRIM, RTRIM` or `TRIM LEADING, TRAILING,` or both function with the scenario mentioned above, the `COLLATE` function will be automatically generated to create a copy without collation of the input column. This EWI is generated to point out that the column collation was removed before the trim function, meaning the result of the function will not have collation, and that this may change the results of further comparisons using the result.

#### Example Code

##### Teradata

```sql
 CREATE TABLE collateTable (
 col1 VARCHAR(50) CHARACTER SET LATIN NOT CASESPECIFIC
);

SELECT
    TRIM(BOTH '0' FROM col1),
    TRIM(LEADING '  ' FROM col1),
    TRIM(TRAILING '0' FROM col1),
    LTRIM(col1, '0'),
    RTRIM(col1)
FROM
    collateTable;
```

##### Snowflake Scripting

```sql
 CREATE OR REPLACE TABLE collateTable (
 col1 VARCHAR(50)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
;

SELECT
 TRIM(COLLATE(col1, ''), '0') !!!RESOLVE EWI!!! /*** SSC-EWI-TD0003 - COLLATION NOT SUPPORTED IN TRIM FUNCTIONS, ADD ORIGINAL COLLATION TO FUNCTION RESULT TO PRESERVE IT ***/!!!,
 LTRIM(col1, '  '),
 RTRIM(COLLATE(col1, ''), '0') !!!RESOLVE EWI!!! /*** SSC-EWI-TD0003 - COLLATION NOT SUPPORTED IN TRIM FUNCTIONS, ADD ORIGINAL COLLATION TO FUNCTION RESULT TO PRESERVE IT ***/!!!,
 LTRIM(COLLATE(col1, ''), '0') !!!RESOLVE EWI!!! /*** SSC-EWI-TD0003 - COLLATION NOT SUPPORTED IN TRIM FUNCTIONS, ADD ORIGINAL COLLATION TO FUNCTION RESULT TO PRESERVE IT ***/!!!,
 RTRIM(col1)
 FROM
 collateTable;
```

#### Best Practices

* To avoid functional differences during comparisons, please add the original collation of the column to the `TRIM` function result string, this can be achieved using the `COLLATE` function and specifying the original column collation as the second argument, this argument has to be a literal string with the collation value.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0004

Not supported SQL Exception on continue handler.

### Severity

Low

#### Description

In Snowflake procedures there is no equivalent transformation for Teradata Continue Handler. For some supported Exception codes, SnowConvert AI does some treatment to emulate this behavior. This EWI is added to Continue Handler statements having an exception code that is not supported.

#### Example Code

##### Teradata

```sql
 REPLACE PROCEDURE PURGING_ADD_TABLE
(
 IN inDatabaseName      VARCHAR(30),
 IN inTableName      VARCHAR(30)
)
BEGIN
 DECLARE vCHAR_SQLSTATE CHAR(5);
 DECLARE vSUCCESS       CHAR(5);

  DECLARE CONTINUE HANDLER FOR SQLSTATE 'UNSUPPORTED'
  BEGIN
     SET vCHAR_SQLSTATE = SQLCODE;
     SET vSUCCESS    = SQLCODE;
  END;

  SELECT 1;

END;
```

##### Snowflake Scripting

```sql
 CREATE OR REPLACE PROCEDURE PURGING_ADD_TABLE
(INDATABASENAME VARCHAR(30), INTABLENAME VARCHAR(30)
)
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/04/2024" }}'
EXECUTE AS CALLER
AS
$$
 DECLARE
  vCHAR_SQLSTATE CHAR(5);
  vSUCCESS       CHAR(5);
 BEGIN

  !!!RESOLVE EWI!!! /*** SSC-EWI-TD0004 - NOT SUPPORTED SQL EXCEPTION ON CONTINUE HANDLER ***/!!!

  DECLARE CONTINUE HANDLER FOR SQLSTATE 'UNSUPPORTED'
  BEGIN
   vCHAR_SQLSTATE := SQLCODE;
   vSUCCESS := SQLCODE;
  END;
  SELECT
   1;
 END;
$$;
```

#### Best Practices

* Check the possible statements that can throw the exception code and encapsulate them in a similar code block as seen in [Continue Handler Translation Reference](../../../../translation-references/teradata/teradata-to-snowflake-scripting-translation-reference.md).
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0005

The statement was converted but its functionality is not implemented yet.

### Severity

Critical

#### Description

The statement was recognized and it was converted but the converted code will not have the expected functionality because the implementation is not done yet.

The warning is added for the user to be aware that when the script uses this statement the script will not have the expected functionally equivalent.

#### Example source

##### BTEQ Input code

```sql
 .SET SIDETITLES ON
```

##### Python Output code

```python
 #*** Generated code is based on the SnowConvert AI Python Helpers version 2.0.6 ***

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
  #** SSC-EWI-TD0005 - THE STATEMENT WAS CONVERTED BUT ITS FUNCTIONALITY IS NOT IMPLEMENTED YET **
  Export.side_titles(True)
  snowconvert.helpers.quit_application()

if __name__ == "__main__":
  main()
```

#### Best Practices

* For more information please refer to [translation spec of BTEQ to Python](../../../../translation-references/teradata/scripts-to-snowflake-sql-translation-reference/bteq.md).
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0006

Invalid default value.

### Severity

Low

#### Description

The **DEFAULT TIME** / **DEFAULT DATE** / **DEFAULT CURREN_DATE** */* **DEFAULT DEFAULT CURRENT_TIME** */* **DEFAULT CURRENT_TIMESTAMP** column specifications are not supported for the **FLOAT** data type.

#### Example Code

##### Teradata

```
CREATE TABLE T_2004
(
    -- In the output code all of these columns will be FLOAT type
    -- and will include the SSC-EWI-TD0006 message.
    COL1 FLOAT DEFAULT TIME,
    COL2 FLOAT DEFAULT DATE,
    COL3 FLOAT DEFAULT CURRENT_DATE,
    COL4 FLOAT DEFAULT CURRENT_TIME,
    COL5 FLOAT DEFAULT CURRENT_TIMESTAMP
);
```

##### Snowflake Scripting

```sql
 CREATE OR REPLACE TABLE T_2004
(
    -- In the output code all of these columns will be FLOAT type
    -- and will include the SSC-EWI-TD0006 message.
    COL1 FLOAT DEFAULT TIME !!!RESOLVE EWI!!! /*** SSC-EWI-TD0006 - DEFAULT CURRENT_TIME NOT VALID FOR DATA TYPE ***/!!!,
    COL2 FLOAT DEFAULT DATE !!!RESOLVE EWI!!! /*** SSC-EWI-TD0006 - DEFAULT CURRENT_DATE NOT VALID FOR DATA TYPE ***/!!!,
    COL3 FLOAT DEFAULT CURRENT_DATE !!!RESOLVE EWI!!! /*** SSC-EWI-TD0006 - DEFAULT CURRENT_DATE NOT VALID FOR DATA TYPE ***/!!!,
    COL4 FLOAT DEFAULT CURRENT_TIME !!!RESOLVE EWI!!! /*** SSC-EWI-TD0006 - DEFAULT CURRENT_TIME NOT VALID FOR DATA TYPE ***/!!!,
    COL5 FLOAT DEFAULT CURRENT_TIMESTAMP !!!RESOLVE EWI!!! /*** SSC-EWI-TD0006 - DEFAULT CURRENT_TIMESTAMP NOT VALID FOR DATA TYPE ***/!!!
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0007

GROUP BY clause unsupported in Teradata Mode for string comparison

### Severity

Low

#### Description

This error message indicates a possible issue when migrating Teradata SQL queries to Snowflake, particularly related to differences in how the GROUP BY clause handles string comparison sensitivity in Teradata mode.

In Teradata mode, string comparisons in GROUP BY clauses are case-insensitive by default (NOT CASESPECIFIC), whereas Snowflake is case-sensitive unless columns are explicitly defined with a case-insensitive COLLATE clause. This difference can cause queries that rely on case-insensitive grouping in Teradata to produce different results in Snowflake.

#### Example Code

##### Teradata

```sql
CREATE TABLE employees (
    employee_id INTEGER,
    first_name VARCHAR(50) NOT CASESPECIFIC,
    department VARCHAR(50)
);

INSERT INTO employees VALUES (1, 'John', 'Sales');
INSERT INTO employees VALUES (2, 'JOHN', 'sales');
INSERT INTO employees VALUES (3, 'john', 'SALES');

SELECT first_name, COUNT(*)
FROM employees
GROUP BY first_name;
```

##### Snowflake Scripting

```sql
CREATE OR REPLACE TABLE employees (
    employee_id INTEGER,
    first_name VARCHAR(50),
    department VARCHAR(50)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "10/20/2025",  "domain": "no-domain-provided",  "migrationid": "kwOaAavBVnCx8OhdxEITfg==" }}'
;

INSERT INTO employees
VALUES (1, 'John', 'Sales');

INSERT INTO employees
VALUES (2, 'JOHN', 'sales');

INSERT INTO employees
VALUES (3, 'john', 'SALES');

SELECT
    first_name,
    COUNT(*)
FROM
    employees
!!!RESOLVE EWI!!! /*** SSC-EWI-TD0007 - GROUP BY IS NOT EQUIVALENT IN TERADATA MODE ***/!!!
GROUP BY first_name;
```

#### Expected Behavior Differences

| Platform | Grouping Behavior | Example Result Rows |
| --- | --- | --- |
| **Teradata Mode** | Groups ‘John’, ‘JOHN’, and ‘john’ together | `John` (or `JOHN`/`john`), 3 |
| **Snowflake** | Treats ‘John’, ‘JOHN’, and ‘john’ as separate | `John`, 1 `JOHN`, 1 `john`, 1 |

#### Best Practices

* **Review GROUP BY clauses** involving string columns when migrating from Teradata mode to ensure expected grouping behavior.

**Note:** When using expressions like `RTRIM(UPPER(first_name))` or `RTRIM(first_name)` in the `GROUP BY` clause to achieve case-insensitive or trimmed grouping, you must apply the same expression consistently in all parts of the query where the column is referenced. For example:

```sql
SELECT RTRIM(UPPER(first_name))
FROM employees
WHERE RTRIM(UPPER(first_name)) = 'JOHN'
GROUP BY RTRIM(UPPER(first_name));
```

This ensures that filtering, selection, and grouping all use the same logic, avoiding mismatches or unexpected results.

* **Define columns with COLLATE** during table creation if consistent case-insensitive behavior is required:

  ```sql
  CREATE TABLE employees (
      first_name VARCHAR(50) COLLATE 'en-cs'
  );
  ```

* **Enable the –UseCollateForCaseSpecification CLI flag or Conversion Setting to use COLLATE for case specification** during conversion. This option ensures that case specification (such as CASESPECIFIC or NOT CASESPECIFIC) is handled using COLLATE functions instead of UPPER functions. For details, refer to the [CLI documentation](../../../user-guide/snowconvert/command-line-interface/teradata.md) or [conversion settings](../../../getting-started/running-snowconvert/conversion/teradata-conversion-settings.md).
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0008

Function for comparing strings is not supported

### Severity

Low

#### Description

Currently, there is no equivalence for some string-comparing functions in Snowflake.

This EWI is added whenever the comparison type is *jaro*, *n_gram*, *LD*, *LDWS*, *OSA*, *DL*, *hamming*, *LCS*, *jaccard*, *cosine* and *soundexcode*.

#### Example Code

##### Teradata

```sql
 SELECT * FROM StringSimilarity (
  ON (
    SELECT CAST(a AS VARCHAR(200)) AS a, CAST(b AS VARCHAR(200)) AS b
    FROM table_1
  ) PARTITION BY ANY
  USING
  ComparisonColumnPairs ('ld(a,b) AS sim_fn')
) AS dt ORDER BY 1;
```

##### Snowflake Scripting

```sql
 SELECT
  * FROM
  !!!RESOLVE EWI!!! /*** SSC-EWI-TD0008 - FUNCTION FOR COMPARING STRINGS IS NOT SUPPORTED ***/!!! StringSimilarity (
   ON (
     SELECT CAST(a AS VARCHAR(200)) AS a, CAST(b AS VARCHAR(200)) AS b
     FROM table_1
   ) PARTITION BY ANY
   USING
   ComparisonColumnPairs ('ld(a,b) AS sim_fn')
 ) AS dt ORDER BY 1;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0009

TEMPORAL column not supported.

### Severity

Low

#### Description

Teradata provides temporal table support at the column level using derived period columns. These columns are not supported in Snowflake.

#### Example Code

##### Teradata

```sql
 CREATE MULTISET TABLE Policy(
      Policy_ID INTEGER,
      Customer_ID INTEGER,
      Policy_Type CHAR(2) NOT NULL,
      Policy_Details CHAR(40),
      Policy_Start DATE NOT NULL,
      Policy_End DATE NOT NULL,
      PERIOD FOR Validity(Policy_Start,Policy_End) AS VALIDTIME
      )
   PRIMARY INDEX(Policy_ID);
```

##### Snowflake Scripting

```sql
 CREATE OR REPLACE TABLE Policy (
   Policy_ID INTEGER,
   Customer_ID INTEGER,
   Policy_Type CHAR(2) NOT NULL,
   Policy_Details CHAR(40),
   Policy_Start DATE NOT NULL,
   Policy_End DATE NOT NULL,
   !!!RESOLVE EWI!!! /*** SSC-EWI-TD0009 - TEMPORAL COLUMN NOT SUPPORTED ***/!!!
         PERIOD FOR Validity(Policy_Start,Policy_End) AS VALIDTIME
         )
         COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
         ;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0010

UPPERCASE not supported by Snowflake.

### Severity

Low

#### Description

The UPPERCASE column attribute is not supported in Snowflake.

#### Example Code

##### Teradata

```sql
 CREATE TABLE T_2010
(
    col1 VARCHAR(1) UPPERCASE
);
```

##### Snowflake Scripting

```sql
 CREATE OR REPLACE TABLE T_2010 (
    col1 VARCHAR(1)
                    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0010 - UPPERCASE NOT SUPPORTED BY SNOWFLAKE ***/!!!
 UPPERCASE
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;
```

#### Best Practices

* Since the `UPPERCASE` clause indicates that characters typed as ‘aaa’ are stored as ‘AAA’, a possible workaround can be adding to all the insert references the [UPPER](https://docs.snowflake.com/en/sql-reference/functions/upper) function. However, external data loading by ETL processes would also have to be modified.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0012

Binary does not support default.

### Severity

Low

#### Description

This EWI is shown when SnowConvert AI finds a data type BINARY along with a DEFAULT value specification. Since default values are not allowed in BINARY columns, it is removed.

#### Example Code

##### Teradata

```sql
 CREATE TABLE TableExample
(
ColumnExample BINARY DEFAULT '00000000'XB NOT NULL
)
```

##### Snowflake Scripting

```sql
 CREATE OR REPLACE TABLE TableExample (
ColumnExample BINARY DEFAULT NOT TO_BINARY('00000000') !!!RESOLVE EWI!!! /*** SSC-EWI-TD0012 - BINARY DOES NOT SUPPORT DEFAULT NOT TO_BINARY('00000000') ***/!!! NULL
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0017

Global temporary table trace functionality not supported.

### Severity

Low

#### Description

This EWI is shown when SnowConvert AI finds a Create Table with the GLOBAL TEMPORARY TRACE option. Review the following Teradata documentation about the [TRACE functionality](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/SQL-Data-Definition-Language-Syntax-and-Examples/Table-Statements/CREATE-GLOBAL-TEMPORARY-TRACE-TABLE). Since it is not supported in Snowflake, it is removed.

#### Example Code

##### Teradata

```sql
 CREATE GLOBAL TEMPORARY TRACE TABLE TableExample
(
ColumnExample Number
)
```

##### Snowflake Scripting

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TD0017 - GLOBAL TEMPORARY TABLE TRACE FUNCTIONALITY NOT SUPPORTED ***/!!!
CREATE OR REPLACE TABLE TableExample (
ColumnExample NUMBER(38, 18)
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;
```

#### Best Practices

* Note: It might be possible to replicate some tracing functionality in Snowflake by using an `EVENT TABLE`. Review the following Snowflake documentation about [Loggin and Tracing](https://docs.snowflake.com/en/developer-guide/logging-tracing/logging-tracing-overview).
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0020

Regexp_Substr Function only supports POSIX regular expressions.

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-EWI-0009](generalEWI.md) documentation

### Severity

Low

#### Description

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
!!!RESOLVE EWI!!! /*** SSC-EWI-0009 - REGEXP_SUBSTR FUNCTION ONLY SUPPORTS POSIX REGULAR EXPRESSIONS ***/!!!
REGEXP_SUBSTR('qaqequ','q(?=u)', 1, 1);
```

#### Best Practices

* Check the regular expression used in each case to determine whether it needs manual intervention. More information about expanded regex support and alternatives in Snowflake can be found [**here**](https://community.snowflake.com/s/question/0D50Z00007ENLKsSAP/expanded-support-for-regular-expressions-regex)**.**
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0023

ACTIVITY_COUNT inside SELECT/SET INTO VARIABLE requires manual fix

### Severity

Low

### Description

The `ACTIVITY_COUNT` status variable returns the number of rows affected by an SQL DML statement in an embedded SQL or stored procedure application. For more information, see the [Teradata ACTIVITY_COUNT documentation](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/SQL-Stored-Procedures-and-Embedded-SQL/Result-Code-Variables/ACTIVITY_COUNT).

As explained in its translation specification, there is a workaround to emulate `ACTIVITY_COUNT`’s behavior through:

```sql
 SELECT $1 FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()));
```

When using `ACTIVITY_COUNT` in a `SELECT/SET INTO VARIABLE` statement, it can not be simply replaced by the workaround mentioned above.

### Example Code

#### Teradata

```
REPLACE PROCEDURE InsertEmployeeSalaryAndLog_4 ()
BEGIN
    DECLARE rowCount INT;
    DECLARE message VARCHAR(100);

    INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
    VALUES (101, 'Alice', 'Smith', 10, 70000.00);

    SELECT ACTIVITY_COUNT INTO rowCount;
    SET message = 'ROWS INSERTED: ' || rowCount;

    -- Insert the ACTIVITY_COUNT into the activity_log table
    INSERT INTO activity_log (operation, row_count)
    VALUES (message, rowCount);
END;
```

#### Snowflake

```sql
 CREATE OR REPLACE PROCEDURE InsertEmployeeSalaryAndLog_4 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/15/2024" }}'
EXECUTE AS CALLER
AS
$$
    DECLARE
               rowCount INT;
               message VARCHAR(100);
    BEGIN

               INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
               VALUES (101, 'Alice', 'Smith', 10, 70000.00);
               SELECT
            ACTIVITY_COUNT !!!RESOLVE EWI!!! /*** SSC-EWI-TD0023 - ACTIVITY_COUNT INSIDE SELECT/SET INTO VARIABLE REQUIRES MANUAL FIX ***/!!! INTO
            :rowCount;
            message := 'ROWS INSERTED: ' || rowCount;

            -- Insert the ACTIVITY_COUNT into the activity_log table
            INSERT INTO activity_log (operation, row_count)
            VALUES (:message, :rowCount);
    END;
$$;
```

#### Manual Fix

Part of the workaround presented above can be used to still get the number of rows inserted/updated/deleted like this:

```sql
 CREATE OR REPLACE PROCEDURE InsertEmployeeSalaryAndLog_4 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/15/2024" }}'
EXECUTE AS CALLER
AS
$$
    DECLARE
               rowCount INT;
               message VARCHAR(100);
    BEGIN

               INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
               VALUES (101, 'Alice', 'Smith', 10, 70000.00);
               SELECT $1 INTO :rowCount FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()));
            message := 'ROWS INSERTED: ' || rowCount;

            -- Insert the ACTIVITY_COUNT into the activity_log table
            INSERT INTO activity_log (operation, row_count)
            VALUES (:message, :rowCount);
    END;
$$;
```

Instead of using the complete query, it needs to be adapted manually to Snowflake’s [SELECT INTO VARIABLE](https://docs.snowflake.com/en/sql-reference/constructs/into) syntax.

Furthermore, if `RESULT_SCAN(LAST_QUERY_ID())` is giving incorrect results, check SSC-FDM-TD0033(../functional-difference/teradataFDM.md#ssc-fdm-td0033) for how to handle possible limitations of using `LAST_QUERY_ID`.

### Best Practices

* Manually adapt the proposed workaround.
* Check SSC-FDM-TD0033(../functional-difference/teradataFDM.md#ssc-fdm-td0033) for how to handle possible limitations of using `LAST_QUERY_ID`.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0024

Abort statement is not supported due to an aggregate function.

### Severity

Low

#### Description

This EWI appears when an `AGGREGATE` function is part of an `ABORT` statement inside of a stored procedure. The statement is commented out.

#### Example Code

##### Teradata

```sql
 REPLACE PROCEDURE ABORT_SAMPLE()
BEGIN
    ABORT WHERE SUM(TABLE1.COL1) < 2;
END;
```

##### Snowflake Scripting

```sql
 CREATE OR REPLACE PROCEDURE ABORT_SAMPLE()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
EXECUTE AS CALLER
AS
$$
    BEGIN
        !!!RESOLVE EWI!!! /*** SSC-EWI-TD0024 - ABORT STATEMENT IS NOT SUPPORTED DUE TO AN AGGREGATE FUNCTION ***/!!!
        ABORT WHERE SUM(TABLE1.COL1) < 2;
    END;
$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0025

Output format not supported.

### Severity

Low

#### Description

This EWI appears when a `CAST` function specifies an output format not supported by Snowflake scripting.

#### Code Example

##### Teradata

```sql
 CREATE TABLE SAMPLE_TABLE
(
    VARCHAR_TYPE VARCHAR
);

REPLACE VIEW SAMPLE_VIEW
AS
SELECT
CAST(VARCHAR_TYPE AS FLOAT FORMAT 'ZZZ.ZZZZZ'),
CAST('01:02.030405' AS TIME(1) WITH TIME ZONE FORMAT 'MI:SS.S(6)')
FROM SAMPLE_TABLE;
```

##### Snowflake Scripting

```sql
 CREATE OR REPLACE TABLE SAMPLE_TABLE
(
    VARCHAR_TYPE VARCHAR
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "03/03/2025",  "domain": "test" }}'
;

CREATE OR REPLACE VIEW SAMPLE_VIEW
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "03/03/2025",  "domain": "test" }}'
AS
SELECT
    TO_NUMBER(VARCHAR_TYPE, '999.00000', 38, 10) !!!RESOLVE EWI!!! /*** SSC-EWI-TD0025 - OUTPUT FORMAT 'ZZZ.ZZZZZ' NOT SUPPORTED. ***/!!!,
    TO_TIME('01:02.030405', 'MI:SS.FF6') !!!RESOLVE EWI!!! /*** SSC-EWI-TD0025 - OUTPUT FORMAT 'MI:SS.S(6)' NOT SUPPORTED. ***/!!!
    FROM
    SAMPLE_TABLE;
```

#### Best Practices

* Check if the output code has functional equivalence with the original code.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0027

Snowflake does not support Teradata built-in time dimensions column options

### Severity

Low

#### Description

The EWI is generated because Snowflake does not support the Teradata built-in time dimensions attributes like VALIDTIME or TRANSACTIONTIME.

#### Example Code

##### Teradata input

```sql
 CREATE MULTISET TABLE SAMPLE_TABLE
(
    COL1 PERIOD(TIMESTAMP(6) WITH TIME ZONE) NOT NULL AS TRANSACTIONTIME
);
```

##### Snowflake output

```sql
 CREATE OR REPLACE TABLE SAMPLE_TABLE (
       COL1 VARCHAR(68) NOT NULL !!!RESOLVE EWI!!! /*** SSC-EWI-TD0027 - SNOWFLAKE DOES NOT SUPPORT 'TRANSACTIONTIME' COLUMN OPTION ***/!!! /*** SSC-FDM-TD0036 - SNOWFLAKE DOES NOT SUPPORT THE PERIOD DATATYPE, ALL PERIODS ARE HANDLED AS VARCHAR INSTEAD ***/
   )
   COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;
```

#### Best Practices

* Manually create TIMESTAMP columns with default values such as CURRENT_TIMESTAMP.
* Leverage the use of table streams, they can record data manipulation changes made to tables as well as metadata about each change. ([Guide](https://docs.snowflake.com/en/user-guide/streams))
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0029

Queue table functionality is not supported.

### Severity

Low

#### Description

This warning appears when a `TABLE` with the [QUEUE](https://www.docs.teradata.com/r/rgAb27O_xRmMVc_aQq2VGw/tHvboDYXkHchWgJ2CD6Uig) attribute is migrated. The `QUEUE` keyword is removed because it is not supported in snowflake.

#### Example Code

##### Input

```sql
 CREATE MULTISET TABLE SAMPLE_TABLE,
QUEUE,
NO FALLBACK
(
    COL1 INTEGER
);
```

##### Output

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TD0029 - QUEUE TABLE FUNCTIONALITY NOT SUPPORTED ***/!!!
CREATE OR REPLACE TABLE SAMPLE_TABLE
(
    COL1 INTEGER
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0031

The result may differ due to char type having a fixed length in Teradata

### Severity

Low

#### Description

Since Teradata CHAR data type has a fixed length, some functions such as LIKE will try to match the complete column instead of the word inserted into the column, resulting in false matches. However, Snowflake the CHAR type is of variable size, meaning that the LIKE functions will always try to match against the inserted values. Take the following code as an example:

#### Example Code

##### Input

```sql
 CREATE TABLE table1
(
    col1 VARCHAR(36),
    col2 CHAR(36)
);

INSERT INTO table1 VALUES ('Gabriel', 'Gabriel');
INSERT INTO table1 VALUES ('Barnum', 'Barnum');
INSERT INTO table1 VALUES ('Sergio', 'Sergio');

SELECT col1 FROM table1 where col1 LIKE 'Barnum';
-- The result is a single row with 'Barnum'
SELECT col2 FROM table1 where col2 LIKE 'Barnum';
-- It does not return any row
```

##### Output

```sql
 CREATE OR REPLACE TABLE table1
(
    col1 VARCHAR(36),
    col2 CHAR(36)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
;

INSERT INTO table1
VALUES ('Gabriel', 'Gabriel');

INSERT INTO table1
VALUES ('Barnum', 'Barnum');

INSERT INTO table1
VALUES ('Sergio', 'Sergio');

SELECT
    col1 FROM
    table1
where col1 ILIKE 'Barnum';
-- The result is a single row with 'Barnum'
    SELECT
    col2 FROM
    table1
    where
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0031 - THE RESULT OF LIKE MAY DIFFER DUE TO CHAR TYPE HAVING A FIXED LENGTH IN TERADATA ***/!!! col2 ILIKE 'Barnum';
    -- It does not return any row
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0034

Multistatement SQL is not supported.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Low

#### Description

Multistatement SQL execution is not supported. The request was handled as a transaction.

> **Note:**
>
> The following EWI is only generated when the PL Target Language flag is set to Javascript, like this: ‘–PLTargetLanguage Javascript’

#### Example Code

##### Input

```
-- Additional Params: --PLTargetLanguage Javascript
REPLACE PROCEDURE proc1()
  BEGIN
    BEGIN REQUEST;
      SELECT* FROM TABLE1;
    END REQUEST;
END;
```

##### Output

```sql
 CREATE OR REPLACE PROCEDURE proc1 ()
RETURNS STRING
LANGUAGE JAVASCRIPT
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
EXECUTE AS CALLER
AS
$$
  // SnowConvert AI Helpers Code section is omitted.

  var TRANSACTION_HANDLER = function (error) {
    throw error;
  };
  // ** SSC-EWI-TD0034 - MULTISTATEMENT SQL EXECUTION NOT SUPPORTED, REQUEST HANDLED AS TRANSACTION **
  try {
    EXEC(`BEGIN`);
    EXEC(`SELECT
   *
FROM
   TABLE1`,[],undefined,TRANSACTION_HANDLER);
    EXEC(`COMMIT`);
  } catch(error) {
    EXEC(`ROLLBACK`);
  }
$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0039

Input format not supported.

### Severity

Medium

#### Description

The specified input format is not supported in Snowflake.

#### Example Code

##### Input

```sql
 SELECT
    CAST('02/032/25' AS DATE FORMAT 'MM/DDD/YY'),
    CAST('02/032/25' AS DATE FORMAT 'MM/D3/YY'),
    CAST('03-Thursday-2025' AS DATE FORMAT 'DD-EEEE-YYYY'),
    CAST('03-Thursday-2025' AS DATE FORMAT 'DD-E4-YYYY');
```

##### Output

```sql
 SELECT
    TO_DATE('02/032/25', 'MM/DDD/YY') !!!RESOLVE EWI!!! /*** SSC-EWI-TD0039 - INPUT FORMAT 'MM/DDD/YY' NOT SUPPORTED ***/!!!,
    TO_DATE('02/032/25', 'MM/D3/YY') !!!RESOLVE EWI!!! /*** SSC-EWI-TD0039 - INPUT FORMAT 'MM/D3/YY' NOT SUPPORTED ***/!!!,
    TO_DATE('03-Thursday-2025', 'DD-EEEE-YYYY') !!!RESOLVE EWI!!! /*** SSC-EWI-TD0039 - INPUT FORMAT 'DD-EEEE-YYYY' NOT SUPPORTED ***/!!!,
    TO_DATE('03-Thursday-2025', 'DD-E4-YYYY') !!!RESOLVE EWI!!! /*** SSC-EWI-TD0039 - INPUT FORMAT 'DD-E4-YYYY' NOT SUPPORTED ***/!!!;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0040

The format in a table is not supported.

### Severity

Low

#### Description

The specified format is not supported.

#### Example Code

##### Input

```sql
 CREATE TABLE T_2040
(
    C1 VARCHAR(255) CHARACTER SET LATIN NOT CASESPECIFIC FORMAT 'X(50)',
    C2 VARCHAR(255) CHARACTER SET LATIN NOT CASESPECIFIC FORMAT 'X(75)'
);
```

##### Output

```sql
 CREATE OR REPLACE TABLE T_2040
(
    C1 VARCHAR(255) FORMAT 'X(50)' !!!RESOLVE EWI!!! /*** SSC-EWI-TD0040 - FORMAT IN TABLE T_2040 NOT SUPPORTED ***/!!!,
    C2 VARCHAR(255) FORMAT 'X(75)' !!!RESOLVE EWI!!! /*** SSC-EWI-TD0040 - FORMAT IN TABLE T_2040 NOT SUPPORTED ***/!!!
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
;
```

## SSC-EWI-TD0041

Trunc function was added to ensure integer.

### Severity

Low

#### Description

When migrating Teradata to Snowflake, you may encounter differences in how numeric conversions are handled. In Teradata, casting a value to `INTEGER` will implicitly truncate any decimal part, even if the original value is a floating-point number or a string representation of a number. However, in Snowflake, casting a non-integer numeric or a string directly to `INTEGER` can result in errors or unexpected results if the value is not already an integer.

To ensure compatibility, the `TRUNC()` function is applied before casting to `INTEGER`. This strips any decimal portion, allowing safe conversion to an integer. However, if the source value is not numeric or is a non-numeric string, errors may still occur and manual intervention may be required. For example, if SnowConvert AI cannot determine the column type due to missing references, you may need to manually adjust the conversion.

#### Example Code

##### Input

```sql
 SELECT
    cast(date_column as integer);
```

##### Output

```sql
 SELECT
    cast(TRUNC(date_column) as integer) !!!RESOLVE EWI!!! /*** SSC-EWI-TD0041 - TRUNC FUNCTION WAS ADDED TO ENSURE INTEGER. MAY NEED CHANGES IF NOT NUMERIC OR STRING. ***/!!!;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0046

Built-in reference is not supported in Snowflake.

### Severity

Medium

#### Description

This error appears when there is a reference to a [DBC](https://docs.teradata.com/r/Teradata-Archive/Recovery-Utility-Reference/March-2019/Archive/Recovery-Operations/Database-DBC) table and the selected column has no equivalence in Snowflake.

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

## SSC-EWI-TD0049

TPT-Statement not processed.

### Severity

High

#### Description

A DML statement in TPT could not be processed and converted by the tool. This can happen for reasons like using concatenation with script variables or using escaping quotes inside the DML statement.

#### Example code

##### Input Code

```sql
 -- Script1.tpt
DEFINE JOB load_job
DESCRIPTION 'LOAD TABLE FROM A FILE'
  (
     DEFINE SCHEMA schema_name
     DESCRIPTION 'define SCHEMA'
   (
       var1 VARCHAR (50)
   );

   STEP setup_tables
   (
      APPLY
       ('RELEASE MLOAD database_name.table_name;')
     TO OPERATOR (DDL_OPERATOR() );

   );
);
```

##### Generated Code

```python
 #*** Generated code is based on the SnowConvert AI Python Helpers version 2.0.6 ***

import os
import sys
import snowconvert.helpers
from snowconvert.helpers import Export
from snowconvert.helpers import exec
from snowconvert.helpers import BeginLoading
import argparse
args = None
## Script1.tpt
class load_job:
    #'LOAD TABLE FROM A FILE'

  jobname = "load_job"
    #'define SCHEMA'

  schema_name = """(
var1 VARCHAR(50)
);"""
  def setup_tables(self):
    self.DDL_OPERATOR()
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0049 - THE FOLLOWING STATEMENT COULD NOT BE PROCESSED ***/!!!
      #'RELEASE MLOAD database_name.table_name;'

con = None
def main():
  snowconvert.helpers.configure_log()
  con = snowconvert.helpers.log_on()
  _load_job = load_job()
  _load_job.setup_tables()
  snowconvert.helpers.quit_application()

if __name__ == "__main__":
  main()
```

### Best Practices

* For this issue, you can type the insert statement manually, and/or since the DML statement is not being supported yet, ask the SnowConvert AI team to add support for that specific case.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0051

Teradata BYTES function results differs from Snowflake LENGTH function for byte columns

### Severity

Low

#### Description

Since Teradata byte datatype has a fixed length, BYTES function [will always count the trailing zeros](https://docs.teradata.com/r/1DcoER_KpnGTfgPinRAFUw/f7V55vW7OB1nU2WltjLxig) inserted to fit smaller byte type values into the column, returning the size of the column instead of the size of the value inserted originally. However, Snowflake binary type has variable size, meaning that the LENGTH function will always return the size of the inserted values. Take the following code as an example:

Teradata:

```sql
 create table exampleTable(
 bytecol byte(10)
);

insert into exampleTable values ('2B'XB);

select bytes(bytecol) from exampleTable;
-- Will return 10, the size of bytecol
```

Equivalent code in Snowflake:

```sql
 CREATE OR REPLACE TABLE exampleTable (
 bytecol BINARY
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;

INSERT INTO exampleTable
VALUES (TO_BINARY('2B'));

SELECT
 LENGTH(bytecol) !!!RESOLVE EWI!!! /*** SSC-EWI-TD0051 - TERADATA BYTES FUNCTION RESULTS DIFFER FROM SNOWFLAKE LENGTH FUNCTION FOR BYTE TYPE COLUMNS ***/!!! from
 exampleTable;
 -- Will return 10, the size of bytecol
```

#### Example code

##### Input code

```sql
 create table sampleTable(
    byteColumn byte(10),
    varbyteColumn varbyte(15)
);

select bytes(byteColumn), bytes(varbyteColumn) from sampleTable;
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE sampleTable (
    byteColumn BINARY,
    varbyteColumn BINARY(15)
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;

SELECT
    LENGTH(byteColumn) !!!RESOLVE EWI!!! /*** SSC-EWI-TD0051 - TERADATA BYTES FUNCTION RESULTS DIFFER FROM SNOWFLAKE LENGTH FUNCTION FOR BYTE TYPE COLUMNS ***/!!!,
    LENGTH(varbyteColumn) from
    sampleTable;
```

#### Best Practices

* Analyze the use given to the BYTES function results, the Snowflake LENGTH function behavior was the one desired from the start and no changes are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0052

Snowflake implicit conversion to numeric differs from Teradata and may fail for non-literal strings

### Severity

Low

#### Description

Both Teradata and Snowflake allow string values to function that expect numeric parameters, these strings are then parsed and converted to their numeric equivalent.

However, there are differences on what the two languages consider a valid numeric string, Teradata is more permissive and successfully parses cases like empty / whitespace-only strings, embedded dashes, having no digits in the mantissa or exponent, currency signs, digit separators or specifying the sign of the number after the digits. For example, the following strings are valid:

* `'1-2-3-4-5' -> 12345`
* `'$50' -> 50`
* `'5000-' -> -5000`
* `'1,569,284.55' -> 1569284.55`

Snowflake applies [automatic optimistic string conversion](https://docs.snowflake.com/en/sql-reference/sql-format-models.html#default-formats-for-parsing), expecting the strings to match either the TM9 or TME formats, so conversion fails for most of the cases mentioned. To solve these differences, SnowConvert AI processes string literals passed to functions that do an implicit conversion to numeric and generates equivalent strings that match TM9 or TME so they can be parsed by Snowflake. This only applies to literal string values, meaning non-literal values have no guarantee to be parsed by Snowflake.

#### Example code

##### Input code

```sql
 create table myTable(
    stringCol varchar(30)
);

insert into myTable values ('   1,236,857.45-');

select cos('   1,236,857.45-');

select cos(stringCol) from myTable;
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE myTable (
    stringCol varchar(30)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
;

INSERT INTO myTable
VALUES ('   1,236,857.45-');

SELECT
    COS('-1236857.45');

    SELECT
    COS(stringCol !!!RESOLVE EWI!!! /*** SSC-EWI-TD0052 - SNOWFLAKE IMPLICIT CONVERSION TO NUMERIC DIFFERS FROM TERADATA AND MAY FAIL FOR NON-LITERAL STRING VALUES ***/!!!)
    from
    myTable;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0053

Snowflake does not support the period datatype, all periods are handled as varchar instead

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-TD0036](../functional-difference/teradataFDM.md) documentation

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
VALUES ('Richard', PUBLIC.PERIOD_UDF(date '2021-05-15', date '2021-06-15') !!!RESOLVE EWI!!! /*** SSC-FDM-TD0036 - SNOWFLAKE DOES NOT SUPPORT THE PERIOD DATATYPE, ALL PERIODS ARE HANDLED AS VARCHAR INSTEAD ***/);

SELECT
    PUBLIC.PERIOD_END_UDF(duration) /*** SSC-FDM-TD0036 - SNOWFLAKE DOES NOT SUPPORT THE PERIOD DATATYPE, ALL PERIODS ARE HANDLED AS VARCHAR INSTEAD ***/ from
    vacations;
```

#### Best Practices

* Since the behavior of`PERIOD`and its related functions is emulated using varchar, we recommend reviewing the results obtained to ensure its correctness.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0055

Snowflake supported formats for TO_CHAR differ from Teradata and may fail or have different behavior

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-TD0029](../functional-difference/teradataFDM.md) documentation

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
TO_CHAR(date '2008-09-13', 'DD/') || PUBLIC.ROMAN_NUMERALS_MONTH_UDF(date '2008-09-13') || TO_CHAR(date '2008-09-13', '/YYYY') !!!RESOLVE EWI!!! /*** SSC-EWI-TD0055 - SNOWFLAKE SUPPORTED FORMATS FOR TO_CHAR DIFFER FROM TERADATA AND MAY FAIL OR HAVE DIFFERENT BEHAVIOR ***/!!!;

SELECT
TO_CHAR(date '2010-10-20', 'MM/DD/YYYY') !!!RESOLVE EWI!!! /*** SSC-EWI-TD0055 - SNOWFLAKE SUPPORTED FORMATS FOR TO_CHAR DIFFER FROM TERADATA AND MAY FAIL OR HAVE DIFFERENT BEHAVIOR ***/!!!;

SELECT
PUBLIC.INSERT_CURRENCY_UDF(TO_CHAR(1255.495, 'S9999.0000'), 2, 'EUR') !!!RESOLVE EWI!!! /*** SSC-EWI-TD0055 - SNOWFLAKE SUPPORTED FORMATS FOR TO_CHAR DIFFER FROM TERADATA AND MAY FAIL OR HAVE DIFFERENT BEHAVIOR ***/!!!;

SELECT
TO_CHAR(45620) !!!RESOLVE EWI!!! /*** SSC-EWI-TD0055 - SNOWFLAKE SUPPORTED FORMATS FOR TO_CHAR DIFFER FROM TERADATA AND MAY FAIL OR HAVE DIFFERENT BEHAVIOR ***/!!!;
```

### Best Practices

* When using FF either try to use DateTime types with the same precision that you use in Teradata or add a precision to the format element to avoid the different behavior.
* When using timezone-related format elements, use the first parameter of type `TIMESTAMP_TZ` to avoid different behavior. Also remember that the `TIME` type cannot have time zone information in Snowflake.
* Set the necessary session parameters with the default values from Teradata to avoid different behavior.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0057

Binary data in NEW JSON is not supported

### Severity

Low

### Description

The NEW JSON function accepts the JSON data represented as a string or in binary format. when the data is in its binary representation the function is not transformed since this binary format is not valid in Snowflake because it cannot interpret the metadata about the JSON object, for more information about this please see Teradata NEW JSON [documentation](https://docs.teradata.com/r/C8cVEJ54PO4~YXWXeXGvsA/QpXrJfufgZ4uyeXFz7Rtcg).

### Example Code

#### Input Code

```sql
 SELECT NEW JSON ('160000000268656C6C6F0006000000776F726C640000'xb, BSON);
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-TD0057 - NEW JSON FUNCTION WITH BINARY DATA IS NOT SUPPORTED ***/!!!!!!RESOLVE EWI!!! /*** SSC-EWI-TD0039 - INPUT FORMAT 'BSON' NOT SUPPORTED ***/!!!
NEW JSON (TO_BINARY('160000000268656C6C6F0006000000776F726C640000'), BSON);
```

### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0059

Snowflake user default time zone may require configuration to match Teradata value

### Severity

Low

#### Description

Same as Teradata, setting a default time zone value to the user will make sessions start using that time zone until a new value is defined for the session.

This warning is generated to remind that the same time zone that was defined for the user in Teradata should be set for the Snowflake user, to do this please use the following query in Snowflake: `ALTER SESSION SET TIMEZONE = 'equivalent_timezone'`, remember that Snowflake only accepts [IANA Time Zone Database](https://www.iana.org/time-zones) standard time zones.

#### Example Code

##### Input Code

```sql
 SET TIME ZONE USER;
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TD0059 - SNOWFLAKE USER DEFAULT TIME ZONE MAY REQUIRE CONFIGURATION TO MATCH TERADATA VALUE ***/!!!
ALTER SESSION UNSET TIMEZONE;
```

#### Best Practices

* Remember to set the default time zone of the user to a time zone equivalent to the one set for the Teradata user.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0060

JSON_TABLE not transformed, column names could not be retrieved from semantic information

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Low

#### Description

The JSON_TABLE function can be transformed by SnowConvert AI, however, this transformation requires knowing the name of the columns that are being selected in the JSON_TABLE ON subquery.

This message is generated to warn the user that the column names were not explicitly put in the subquery (for example, a SELECT \* was used) and the semantic information of the tables being referenced was not found, meaning the column names could not be extracted.

If you want know how to load JSON data into a table check this [page](https://docs.snowflake.com/en/user-guide/script-data-load-transform-json)

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
 CREATE OR REPLACE TABLE demo.Train (
    firstCol INT,
    jsonCol VARIANT,
    thirdCol VARCHAR(30)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "12/16/2024",  "domain": "test" }}'
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
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0060 - JSON_TABLE NOT TRANSFORMED, COLUMN NAMES COULD NOT BE RETRIEVED FROM SEMANTIC INFORMATION ***/!!! JSON_TABLE
   (ON (
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

## SSC-EWI-TD0061

TD_UNPIVOT transformation requires column information that could not be found, columns missing in result

### Severity

Low

#### Description

SnowConvert AI not supports and transforms the [TD_UNPIVOT](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/SQL-Operators-and-User-Defined-Functions/Table-Operators/TD_UNPIVOT) function, which can be used to represent columns from a table as rows.

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
 CREATE OR REPLACE TABLE unpivotTable (
 myKey INTEGER NOT NULL PRIMARY KEY,
 firstSemesterIncome DECIMAL(10,2),
 secondSemesterIncome DECIMAL(10,2),
 firstSemesterExpenses DECIMAL(10,2),
 secondSemesterExpenses DECIMAL(10,2)
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;

--** SSC-FDM-0007 - MISSING DEPENDENT OBJECTS "VALUE_COLUMNS", "UNPIVOT_COLUMN", "COLUMN_LIST", "COLUMN_ALIAS_LIST" **
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

 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECTS "VALUE_COLUMNS", "UNPIVOT_COLUMN", "COLUMN_LIST", "COLUMN_ALIAS_LIST" **
 SELECT
 * FROM
 !!!RESOLVE EWI!!! /*** SSC-EWI-TD0061 - TD_UNPIVOT TRANSFORMATION REQUIRES COLUMN INFORMATION THAT COULD NOT BE FOUND, COLUMNS MISSING IN RESULT ***/!!!
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

## SSC-EWI-TD0063

JSON path was not recognized

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Medium

#### Description

This message is shown when SnowConvert AI cannot deserialize a JSON path because the string does not have the expected JSON format.

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
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0063 - UNRECOGNIZED JSON PATH $weekShedule.Monday[*] ***/!!!
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

* Check if the Json path have an unexpected character, or do not have the right format.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0066

The following identifier has one or more Unicode escape characters that are invalid in snowflake

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Low

#### Description

This message is shown when SnowConvert AI transforms a [Teradata Unicode Delimited Identifier](https://docs.teradata.com/r/Teradata-Database-SQL-Fundamentals/June-2017/Basic-SQL-Syntax/Working-with-Unicode-Delimited-Identifiers) with invalid characters in Snowflake.

#### Example code

##### Input Code

```sql
 SELECT * FROM U&"#000f#ffff" UESCAPE '#';
```

##### Generated Code

```sql
 // SnowConvert AI Helpers Code section is omitted.
SELECT
* FROM
!!!RESOLVE EWI!!! /*** SSC-EWI-TD0066 - THE FOLLOWING IDENTIFIER HAS ONE OR MORE UNICODE ESCAPE CHARACTERS THAT ARE INVALID IN SNOWFLAKE ***/!!!
"\u000f\uffff";
```

#### Best Practices

* Use identifiers with valid Unicode characters in Snowflake.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0068

Snowflake does not support profiles, referencing role instead

### Severity

Medium

#### Description

Teradata profiles allow defining of multiple common parameters related to storage space and password constraints management.

However, [Snowflake works with cloud architecture and automatically manages and optimizes storage](https://docs.snowflake.com/en/user-guide/intro-key-concepts.html#key-concepts-architecture), meaning no storage customization is done on the user side. Also, [Snowflake currently has a password policy](https://docs.snowflake.com/en/user-guide/admin-user-management.html#snowflake-password-policy) defined that applies to all user passwords and is not modifiable.

This error is generated when a reference to a Teradata profile is found to indicate that it was changed to a reference to the user’s role, which is the nearest approximation to a profile in Snowflake, although there might be differences in the query results unless the profile and role names of a user are the same.

#### Example code

##### Input Code

```sql
 SELECT PROFILE;
```

##### Generated Code

```sql
 SELECT
CURRENT_ROLE() !!!RESOLVE EWI!!! /*** SSC-EWI-TD0068 - SNOWFLAKE DOES NOT SUPPORT PROFILES, REFERENCING ROLE INSTEAD ***/!!!;
```

#### Best Practices

* Avoid referencing user profiles, they are not supported, and query results will be different unless the user has the same name for both its profile and role.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0069

ST_DISTANCE results are slightly different from ST_SPHERICALDISTANCE

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-TD0031](../functional-difference/teradataFDM.md) documentation

### Severity

Low

#### Description

The Teradata function ST_SPHERICALDISTANCE calculates the distance between two spherical coordinates on the planet using the Haversine formula, on the other side, the Snowflake ST_DISTANCE function does not utilize the haversine formula to calculate the minimum distance between two geographical points.

#### Example Code

##### Input Code

```sql
 --The distance between New York and Los Angeles
Select Cast('POINT(-73.989308 40.741895)' As ST_GEOMETRY) As location1,
 Cast('POINT(40.741895 34.053691)' As ST_GEOMETRY) As location2,
 location1.ST_SPHERICALDISTANCE(location2) As Distance_In_km;
```

##### Generated Code

```sql
 --The distance between New York and Los Angeles
SELECT
 Cast('POINT(-73.989308 40.741895)' As GEOGRAPHY) As location1,
 Cast('POINT(40.741895 34.053691)' As GEOGRAPHY) As location2,
 !!!RESOLVE EWI!!! /*** SSC-EWI-TD0069 - ST_DISTANCE RESULTS ARE SLIGHTLY DIFFERENT FROM ST_SPHERICALDISTANCE ***/!!!
 ST_DISTANCE(
 location1, location2) As Distance_In_km;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0070

A return statement was added at the end of the label section to ensure the same execution flow

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-TD0030](../functional-difference/teradataFDM.md) documentation

### Severity

Medium

#### Description

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
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0070 - A RETURN STATEMENT WAS ADDED AT THE END OF THE LABEL SECTION LABEL_B TO ENSURE THE SAME EXECUTION FLOW ***/!!!
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

## SSC-EWI-TD0076

The use of foreign tables is not supported in Snowflake.

### Severity

Medium

#### Description

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
!!!RESOLVE EWI!!! /*** SSC-EWI-TD0076 - THE USE OF FOREIGN TABLES IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
 FOREIGN TABLE (SELECT cust_id, income, age FROM twm_customer)@hadoop1 T1;
```

#### Best Practices

* Instead of foreign tables in Teradata, you can use [Snowflake external tables](https://docs.snowflake.com/en/user-guide/tables-external.html). External tables reference data files located in a cloud storage (Amazon S3, Google Cloud Storage, or Microsoft Azure) data lake. This enables querying data stored in files in a data lake as if it were inside a database. External tables can access data stored in any format supported by [COPY INTO <table>](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table.html) statements.
* Another alternative is [Snowflake’s Iceberg tables](https://www.snowflake.com/blog/iceberg-tables-powering-open-standards-with-snowflake-innovations/?lang=es). So, you can think of Iceberg tables as tables that use open formats and customer-supplied cloud storage. This data is stored in Parquet files.
* Finally, there are the [standard Snowflake tables](https://docs.snowflake.com/en/sql-reference/sql/create-table.html) which can be an option to cover the functionality of foreign tables in Teradata
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0077

RESET WHEN clause is not supported in this scenario due to its condition

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Medium

#### Description

SnowConvert AI currently only supports `RESET WHEN` clauses with binary conditions (<=, >= or =). Any other type of condition, such as `IS NOT NULL`, the `RESET WHEN` clause will be removed and an error message will be added since it is not supported in Snowflake.

This error message also appears when the `RESET WHEN` condition references an expression whose definition was not found by the migration tool. Currently, the tool supports the alias references to a column that was defined in the same query.

#### Example Code

##### Condition is not binary

##### Input Code

```sql
 SELECT
    account_id,
    month_id,
    balance,
    ROW_NUMBER() OVER (
        PARTITION BY account_id
        ORDER BY month_id
        RESET WHEN balance IS NOT NULL
        ROWS UNBOUNDED PRECEDING
    ) as balance_increase
FROM account_balance
ORDER BY 1,2;
```

##### Generated Code

```sql
 // SnowConvert AI Helpers Code section is omitted.
SELECT
    account_id,
    month_id,
    balance,
    ROW_NUMBER() OVER (
        PARTITION BY account_id
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0077 - RESET WHEN CLAUSE IS NOT SUPPORTED IN THIS SCENARIO DUE TO ITS CONDITION ***/!!!
        ORDER BY month_id
        ROWS UNBOUNDED PRECEDING
    ) as balance_increase
FROM
    account_balance
ORDER BY 1,2;
```

##### Condition expression was not found

##### Input Code

```sql
 SELECT
    account_id,
    month_id,
    balance,
    ROW_NUMBER() OVER (
        PARTITION BY account_id
        ORDER BY month_id
        RESET WHEN balance <= not_found_expresion
    ) as balance_increase
FROM account_balance
ORDER BY 1,2;
```

##### Generated Code

```sql
 // SnowConvert AI Helpers Code section is omitted.
SELECT
    account_id,
    month_id,
    balance,
    ROW_NUMBER() OVER (
        PARTITION BY account_id
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0077 - RESET WHEN CLAUSE IS NOT SUPPORTED IN THIS SCENARIO DUE TO ITS CONDITION ***/!!!
        ORDER BY month_id
    ) as balance_increase
FROM
    account_balance
ORDER BY 1,2;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0079

The required period type column was not found

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Low

#### Description

This warning is shown because the Period column necessary to replicate the functionality of Normalize clause was not found.

#### Example Code

##### Input Code

```sql
 SELECT NORMALIZE emp_id, duration2 FROM project;
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TD0079 - THE REQUIRED PERIOD TYPE COLUMN WAS NOT FOUND ***/!!!
// SnowConvert AI Helpers Code section is omitted.
WITH NormalizeCTE AS
(
SELECT
T1.*,
SUM(GroupStartFlag)
OVER (
PARTITION BY
emp_id, duration2
ORDER BY
PeriodColumn_begin
ROWS UNBOUNDED PRECEDING) GroupID
FROM
(
SELECT 
emp_id,
duration2,
PUBLIC.PERIOD_BEGIN_UDF(PeriodColumn) PeriodColumn_begin,
PUBLIC.PERIOD_END_UDF(PeriodColumn) PeriodColumn_end,
(CASE
WHEN PeriodColumn_begin <= LAG(PeriodColumn_end)
OVER (
PARTITION BY
emp_id, duration2
ORDER BY
PeriodColumn_begin,
PeriodColumn_end)
THEN 0
ELSE 1
END) GroupStartFlag FROM 
project
) T1
)
SELECT
emp_id,
duration2,
PUBLIC.PERIOD_UDF(MIN(PeriodColumn_begin), MAX(PeriodColumn_end))
FROM
NormalizeCTE
GROUP BY
emp_id,
duration2,
GroupID;
```

#### Best Practices

* To fix this warning manually you just need to find which was the first period column and remove all its references except where is defined, and then replace PeriodColumn with the column found.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0082

Translate function using the current encoding is not supported

### Severity

Medium

#### Description

The usage of the Translate function using the current encoding arguments is not supported in Snowflake. The function is commented out during translation.

#### Example Code

##### Input Code

```sql
 SELECT Translate('abc' USING KANJISJIS_TO_LATIN);
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-TD0082 - TRANSLATE FUNCTION USING KANJISJIS_TO_LATIN ENCODING IS NOT SUPPORTED ***/!!!
Translate('abc' USING KANJISJIS_TO_LATIN);
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0083

Not able to transform two or more complex Select clauses at a time

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Medium

#### Description

SnowConvert AI is not able to transform two or more complex SELECT clauses, as it is necessary to map them to a CTE or composite FROM clause, which causes the mapped code to not compile or enter into a logical cycle.

##### What do we consider a SELECT complex clause?

Those that required to be mapped to a CTE or composite FROM clause such as NORMALIZE, EXPAND ON, or RESET WHEN.

#### Example Code

##### Input Code

```sql
 SELECT
   NORMALIZE emp_id,
   duration,
   dept_id,
   balance,
   (
     ROW_NUMBER() OVER (
       PARTITION BY emp_id
       ORDER BY
         dept_id RESET WHEN balance <= SUM(balance) OVER (
           PARTITION BY emp_id
           ORDER BY dept_id
           ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING
         )
     ) -1
   ) AS balance_increase
FROM project
EXPAND ON duration AS bg BY ANCHOR ANCHOR_SECOND
ORDER BY 1, 2;
```

##### Generated Code

```sql
 // SnowConvert AI Helpers Code section is omitted.
SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-TD0083 - NOT ABLE TO TRANSFORM TWO OR MORE COMPLEX SELECT CLAUSES AT A TIME ***/!!!
NORMALIZE emp_id,
   duration,
   dept_id,
   balance,
   (
     ROW_NUMBER() OVER (
   PARTITION BY
      emp_id, new_dynamic_part
   ORDER BY
         dept_id
     ) -1
   ) AS balance_increase
FROM
   (
      SELECT
         emp_id,
         duration,
         dept_id,
         balance,
         previous_value,
         SUM(dynamic_part) OVER (
                 PARTITION BY emp_id
                 ORDER BY dept_id
         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
               ) AS new_dynamic_part
      FROM
         (
            SELECT
               emp_id,
               duration,
               dept_id,
               balance,
               SUM(balance) OVER (
                       PARTITION BY emp_id
                       ORDER BY dept_id
                       ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING
                     ) AS previous_value,
               (CASE
                  WHEN balance <= previous_value
                     THEN 1
                  ELSE 0
               END) AS dynamic_part
            FROM
               project
         )
   )
!!!RESOLVE EWI!!! /*** SSC-EWI-TD0083 - NOT ABLE TO TRANSFORM TWO OR MORE COMPLEX SELECT CLAUSES AT A TIME ***/!!!
EXPAND ON duration AS bg BY ANCHOR ANCHOR_SECOND
ORDER BY 1, 2;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0087

GOTO statement was removed due to if statement inversion.

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-TD0026](../functional-difference/teradataFDM.md) documentation

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Medium

#### Description

It is common to use GOTO command with IF and LABEL commands to replicate the functionality of an SQL if statement. When used in this way, it is possible to transform them directly into an if, if-else, or even an if-elseif-else statement. However, in these cases, the GOTO commands become unnecessary and should be removed to prevent them from being replaced by a LABEL section.

#### Example Code

##### Input Code

```
-- Additional Params: --scriptsTargetLanguage SnowScript
.If ActivityCount = 0 THEN .GOTO endIf
DROP TABLE TABLE1;
.Label endIf
SELECT A FROM TABLE1;
```

##### Generated Code

```sql
 EXECUTE IMMEDIATE
$$
  DECLARE
    STATUS_OBJECT OBJECT := OBJECT_CONSTRUCT('SQLCODE', 0);
  BEGIN
    IF (NOT (STATUS_OBJECT['SQLROWCOUNT'] = 0)) THEN
      !!!RESOLVE EWI!!! /*** SSC-EWI-TD0087 - GOTO endIf WAS REMOVED DUE TO IF STATEMENT INVERSION ***/!!!

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

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0091

Expression converted as cast with possible errors due to missing dependencies.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons

### Severity

Medium

#### Description

In Teradata scripts, you can use the following syntax to CAST expressions:

```none
<expression> ( <DataType> )
```

Unfortunately, this syntax generates ambiguity when trying to convert a CAST to `DATE` or `TIME` since these keywords also behave as the `CURRENT_DATE` and `CURRENT_TIME` functions respectively.

Thus, without context about the expression to be CAST, there is no sure way to differentiate when we are dealing with an actual case of CAST or a function that accepts DATE or TIME as parameters.

In other words, it is required to know whether `<expression>` is a column or a user-defined function (UDF). To achieve this, when converting the code, one must add the `CREATE TABLE` or `CREATE FUNCTION` from which <expression> is dependant on.

E.g. check the following `SELECT` statement. With no context about `AMBIGUOUS_EXPR`, we have no way to determine if we are dealing with a function call or CAST to `DATE`. However, we do know that `COL1 (DATE)` is indeed a CAST since `COL1` is a column from the table `TAB`.

```none
CREATE TABLE TAB (
    COL1 VARCHAR(23)
)

SELECT
    COL1 (DATE),
    AMBIGUOUS_EXPR (DATE)
FROM TAB;
```

#### Example Code

##### Input Code

```sql
 CREATE TABLE TAB (
    COL1 VARCHAR(23)
)

SELECT
    COL1 (DATE),
    AMBIGUOUS_EXPR (DATE)
FROM TAB;
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE TAB (
    COL1 VARCHAR(23)
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"teradata"}}'
;

SELECT
    TO_DATE(
    COL1, 'YYYY/MM/DD') AS COL1,
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0091 - EXPRESSION CONVERTED AS CAST BY DEFAULT. CONVERSION MIGHT PRESENT ERRORS DUE TO MISSING DEPENDENCIES FOR 'AMBIGUOUS_EXPR'. ***/!!!
    AMBIGUOUS_EXPR :: DATE
    FROM
    TAB;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0092

Translation for Teradata Built-In Table/View is not currently supported

### Severity

Low

#### Description

This EWI is added when SnowConvert AI finds a Teradata system table that is currently not translated.

#### Example Code

##### Input Code

```sql
 SELECT
  CRLF ||
  TRIM(em.ErrorText) INTO :MsgText
FROM
  DBC.ErrorMsgs em
WHERE
  em.ErrorCode = SUBSTR(:SqlStateCode, 2, 4)
```

##### Generated Code

```sql
 SELECT
  CRLF ||
  TRIM(em.ErrorText) INTO :MsgText
FROM
  !!!RESOLVE EWI!!! /*** SSC-EWI-TD0092 - TRANSLATION FOR TERADATA BUILT-IN TABLE/VIEW DBC.ErrorMsgs IS NOT CURRENTLY SUPPORTED. ***/!!!
  DBC.ErrorMsgs em
WHERE
  UPPER(RTRIM(
  em.ErrorCode)) = UPPER(RTRIM(SUBSTR(:SqlStateCode, 2, 4)));
```

#### Best Practices

* Search in Snowflake’s internal tables, such as `Information_Schema` or `SNOWFLAKE.ACCOUNT_USAGE` for equivalents
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0093

Format not supported and must be updated in all its varchar casting uses.

### Severity

High

#### Description

This EWI is added when the CAST function is used to cast a numeric expression to another numeric type with a specified format. While the format does not impact the numeric value itself, if the result is subsequently cast to a string, the intended format will not be correctly applied. Therefore, it is necessary to update all instances where the result is cast to VARCHAR, ensuring the format defined in the EWI is used.

#### Example Code

##### Input Code

```sql
SELECT
   CAST(245222.32 AS FORMAT '-(10)9.9(4)') AS FormattedAmount,
   CAST(FormattedAmount AS VARCHAR(30));
```

##### Generated Code

```sql
SELECT
   245222.32 !!!RESOLVE EWI!!! /*** SSC-EWI-TD0093 - FORMAT '-(10)9.9(4)' IS NOT SUPPORTED AND MUST BE UPDATED TO THE FOLLOWING FORMAT 'S9999999999.0000' IN ALL VARCHAR CAST USAGES. ***/!!! AS FormattedAmount,
   LEFT(LTRIM(TO_VARCHAR(FormattedAmount, 'MI0.00000000000000EEEEE')), 10);
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0094

The IMPORT command was not converted.

### Severity

High

#### Description

This issue indicates that an [`.IMPORT`](https://docs.teradata.com/r/Enterprise_IntelliFlex_Lake_VMware/Teradata-MultiLoad-Reference-20.00/Teradata-MultiLoad-Commands/IMPORT) command was not converted because it uses unsupported features. The original MLoad layout, DML, and import statements are commented out and each line is annotated with this EWI.

**Features pending translation:**

* `BINARY` format
* `FASTLOAD` format
* `.TABLE` type layout
* [`INMOD`](https://docs.teradata.com/r/Enterprise_IntelliFlex_Lake_VMware/Teradata-MultiLoad-Reference-20.00/Teradata-MultiLoad-Commands/IMPORT/INMOD-Specification) option
* `AXSMOD` option
* Non `INSERT-VALUES` DML statements

**Missing required definitions:**

* [`.LAYOUT`](https://docs.teradata.com/r/Enterprise_IntelliFlex_Lake_VMware/Teradata-MultiLoad-Reference-20.00/Teradata-MultiLoad-Commands/LAYOUT) definition was not found in the script
* [`.DML LABEL`](https://docs.teradata.com/r/Enterprise_IntelliFlex_Lake_VMware/Teradata-MultiLoad-Reference-20.00/Teradata-MultiLoad-Commands/DML-LABEL) was not found in the script

#### Example Code

##### Teradata

```sql
.LAYOUT employee_layout;
.FIELD employee_id * CHAR(10);
.FIELD first_name * CHAR(50);

.DML LABEL insert_employees;
INSERT INTO employees (employee_id, first_name) VALUES (:employee_id, :first_name);

.IMPORT INFILE employees.dat FORMAT BINARY LAYOUT employee_layout APPLY insert_employees;
```

##### Snowflake Scripting

```sql
CREATE TEMPORARY STAGE IF NOT EXISTS sc_import_stage;

--** SSC-FDM-TD0038 - PUT COMMAND REQUIRES EXECUTION THROUGH SNOWSQL. **
PUT file://employees.dat @sc_import_stage;

EXECUTE IMMEDIATE
$$
  DECLARE
    STATUS_OBJECT OBJECT := OBJECT_CONSTRUCT('SQLCODE', 0);
  BEGIN
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0094 - THE IMPORT COMMAND WAS NOT CONVERTED: BINARY FORMAT IS PENDING TRANSLATION. ***/!!!
    -- .LAYOUT employee_layout;
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0094 - THE IMPORT COMMAND WAS NOT CONVERTED: BINARY FORMAT IS PENDING TRANSLATION. ***/!!!
    -- .FIELD employee_id * CHAR(10) ;
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0094 - THE IMPORT COMMAND WAS NOT CONVERTED: BINARY FORMAT IS PENDING TRANSLATION. ***/!!!
    -- .FIELD first_name * CHAR(50) ;
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0094 - THE IMPORT COMMAND WAS NOT CONVERTED: BINARY FORMAT IS PENDING TRANSLATION. ***/!!!
    -- .DML LABEL insert_employees ;
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0094 - THE IMPORT COMMAND WAS NOT CONVERTED: BINARY FORMAT IS PENDING TRANSLATION. ***/!!!
    -- INSERT INTO employees (employee_id, first_name) VALUES (:employee_id, :first_name);
    !!!RESOLVE EWI!!! /*** SSC-EWI-TD0094 - THE IMPORT COMMAND WAS NOT CONVERTED: BINARY FORMAT IS PENDING TRANSLATION. ***/!!!
    -- .IMPORT INFILE employees.dat FORMAT BINARY LAYOUT employee_layout APPLY insert_employees;
  EXCEPTION
    WHEN OTHER CONTINUE THEN
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
  END
$$
```

#### Best Practices

* Convert the source file to a supported format (`VARTEXT`, `TEXT`, or `UNFORMAT`) before running SnowConvert AI.
* Manually rewrite the load using [Snowflake stages](https://docs.snowflake.com/en/user-guide/data-load-overview) and [`COPY INTO`](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table).
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0095

DML statement in IMPORT command is pending translation.

### Severity

Medium

#### Description

This issue happens when a `.IMPORT` command uses a DML label that includes statements other than a basic `INSERT ... VALUES` (for example, `UPDATE`, `DELETE`, or more complex `INSERT` logic). In these cases, the converter will only transform the simple `INSERT ... VALUES` part into a [`COPY INTO`](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table) statement for Snowflake. Any other DML statements are left in the output with a warning annotation, and are not automatically converted. This means that important logic—like updates or deletes—will not be migrated, which can affect your results. Please review and update your script to handle these cases, such as by using a [`MERGE`](https://docs.snowflake.com/en/sql-reference/sql/merge) statement for upserts.

#### Example Code

##### Teradata

```sql
.LAYOUT employee_layout;
.FIELD employee_id * VARCHAR(10);
.FIELD first_name * VARCHAR(50);
.FIELD salary * VARCHAR(10);

.DML LABEL upsert_employees;
UPDATE employees SET salary = :salary WHERE employee_id = :employee_id;
INSERT INTO employees (employee_id, first_name, salary) VALUES (:employee_id, :first_name, :salary);

.IMPORT INFILE employees.csv FORMAT VARTEXT ',' LAYOUT employee_layout APPLY upsert_employees;
```

##### Snowflake Scripting

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
      !!!RESOLVE EWI!!! /*** SSC-EWI-TD0095 - THE DML 'UPDATE STATEMENT' USED IN THE IMPORT COMMAND IS PENDING TRANSLATION. ***/!!!
      UPDATE employees SET
        salary = :salary WHERE
        employee_id = :employee_id;

      COPY INTO employees (
        employee_id,
        first_name,
        salary
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

* Implement the equivalent upsert logic in Snowflake using [`MERGE`](https://docs.snowflake.com/en/sql-reference/sql/merge).
* Load data into a [staging table](https://docs.snowflake.com/en/user-guide/data-load-overview) first, then merge into the target table.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0096

COPY INTO requires an explicit target file name.

### Severity

Medium

#### Description

When the `.IMPORT INFILE` path consists solely of a bash variable (for example, `${FILE_PATH}`) and no explicit file name can be inferred, this EWI is raised for the [`COPY INTO`](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table) source. The converter cannot determine the file name to use in the [stage](https://docs.snowflake.com/en/sql-reference/sql/create-stage) path.

#### Example Code

##### Teradata

```sql
.LAYOUT employee_layout;
.FIELD employee_id * VARCHAR(10);
.FIELD first_name * VARCHAR(50);

.DML LABEL insert_employees;
INSERT INTO employees (employee_id, first_name) VALUES (:employee_id, :first_name);

.IMPORT INFILE ${FILE_PATH} FORMAT VARTEXT '|' LAYOUT employee_layout APPLY insert_employees;
```

##### Snowflake Scripting

```sql
--** SSC-FDM-TD0003 - BASH VARIABLES FOUND, USING SNOWSQL WITH VARIABLE SUBSTITUTION ENABLED IS REQUIRED TO RUN THIS SCRIPT **
CREATE TEMPORARY STAGE IF NOT EXISTS sc_import_stage;

--** SSC-FDM-TD0038 - PUT COMMAND REQUIRES EXECUTION THROUGH SNOWSQL. **
PUT file://&{FILE_PATH} @sc_import_stage;

EXECUTE IMMEDIATE
$$
  DECLARE
    STATUS_OBJECT OBJECT := OBJECT_CONSTRUCT('SQLCODE', 0);
  BEGIN
    BEGIN
      COPY INTO employees (
        employee_id,
        first_name
      )
      FROM
      (
        SELECT
          $1,
          $2
        FROM
          !!!RESOLVE EWI!!! /*** SSC-EWI-TD0096 - COPY INTO REQUIRES AN EXPLICIT TARGET FILE NAME. ***/!!!
          @sc_import_stage/&{FILE_PATH}
      )
      FILE_FORMAT = (TYPE = CSV FIELD_DELIMITER = '|')
      ON_ERROR = 'CONTINUE';
    END;
  EXCEPTION
    WHEN OTHER CONTINUE THEN
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
  END
$$
```

#### Best Practices

* Adjust the original [MLoad](https://docs.teradata.com/r/Enterprise_IntelliFlex_Lake_VMware/Teradata-MultiLoad-Reference-20.00/Using-Teradata-MultiLoad) script so that the file name is explicit (separate directory and file name).
* Use a literal file name with variable directory, for example, `.IMPORT INFILE ${DATA_DIR}/employees.csv ...`
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TD0097

Local variables not supported in PUT or COPY INTO.

### Severity

Medium

#### Description

This issue indicates the use of local MLoad variables, such as `&FILE_NAME`, defined with [`.SET`](https://docs.teradata.com/r/Enterprise_IntelliFlex_Lake_VMware/Teradata-MultiLoad-Reference-20.00/Teradata-MultiLoad-Commands/SET) in `INFILE` paths. These cannot be resolved in the generated [`PUT`](https://docs.snowflake.com/en/sql-reference/sql/put) or [`COPY INTO`](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table) statements because Snowflake’s `PUT` command only supports literal paths or [SnowSQL session variables](https://docs.snowflake.com/en/user-guide/snowsql-use#using-variables) (`&{VAR}`), not Snowflake Scripting variables (`:var`).

#### Example Code

##### Teradata

```sql
.SET FILE_NAME TO 'employees.csv';

.LAYOUT employee_layout;
.FIELD employee_id * VARCHAR(10);
.FIELD first_name * VARCHAR(50);

.DML LABEL insert_employees;
INSERT INTO employees (employee_id, first_name) VALUES (:employee_id, :first_name);

.IMPORT INFILE &FILE_NAME FORMAT VARTEXT '|' LAYOUT employee_layout APPLY insert_employees;
```

##### Snowflake Scripting

```sql
CREATE TEMPORARY STAGE IF NOT EXISTS sc_import_stage;

!!!RESOLVE EWI!!! /*** SSC-EWI-TD0097 - LOCAL VARIABLES ARE CURRENTLY NOT SUPPORTED IN THE PUT STATEMENT. ***/!!!
--** SSC-FDM-TD0038 - PUT COMMAND REQUIRES EXECUTION THROUGH SNOWSQL. **
PUT file://&FILE_NAME @sc_import_stage;

EXECUTE IMMEDIATE
$$
  DECLARE
    STATUS_OBJECT OBJECT := OBJECT_CONSTRUCT('SQLCODE', 0);
    FILE_NAME STRING := 'employees.csv';
  BEGIN
    BEGIN
      COPY INTO employees (
        employee_id,
        first_name
      )
      FROM
      (
        SELECT
          $1,
          $2
        FROM
          !!!RESOLVE EWI!!! /*** SSC-EWI-TD0097 - LOCAL VARIABLES ARE CURRENTLY NOT SUPPORTED IN THE COPY INTO STATEMENT. ***/!!!
          @sc_import_stage/&FILE_NAME
      )
      FILE_FORMAT = (TYPE = CSV FIELD_DELIMITER = '|')
      ON_ERROR = 'CONTINUE';
    END;
  EXCEPTION
    WHEN OTHER CONTINUE THEN
      STATUS_OBJECT := OBJECT_CONSTRUCT('SQLCODE', SQLCODE, 'SQLERRM', SQLERRM, 'SQLSTATE', SQLSTATE);
  END
$$
```

#### Best Practices

* Replace local variables with bash variables (resolved by [SnowSQL](https://docs.snowflake.com/en/user-guide/snowsql) before execution).
* Alternatively, hard-code the file name directly.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
