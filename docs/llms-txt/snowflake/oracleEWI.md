# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/conversion-issues/oracleEWI.md

# SnowConvert AI - Oracle Issues

## SSC-EWI-OR0001

Sequence start value with ‘LIMIT VALUE’ is not supported by Snowflake.

### Description

This error appears when the `START WITH` statement value is `LIMIT VALUE`.

In Oracle this clause is used only in ALTER TABLE

> * `START` `WITH` `LIMIT VALUE`, which is specific to `identity_options`, can only be used with `ALTER` `TABLE` `MODIFY`. If you specify `START` `WITH` `LIMIT VALUE`, then Oracle Database locks the table and finds the maximum identity column value in the table (for increasing sequences) or the minimum identity column value (for decreasing sequences) and assigns the value as the sequence generator’s high water mark. The next value returned by the sequence generator will be the high water mark + `INCREMENT` `BY` `integer` for increasing sequences, or the high water mark - `INCREMENT` `BY` `integer` for decreasing sequences.

#### [ALTER TABLE ORACLE](https://docs.oracle.com/en/database/oracle/oracle-database/23/sqlrf/ALTER-TABLE.html#GUID-552E7373-BF93-477D-9DA3-B2C9386F2877)

#### Example Code

##### Input Code

```sql
 CREATE SEQUENCE SEQUENCE1
  START WITH LIMIT VALUE;
```

##### Generated Code

```sql
 CREATE OR REPLACE SEQUENCE SEQUENCE1
  !!!RESOLVE EWI!!! /*** SSC-EWI-OR0001 - SEQUENCE START VALUE WITH 'LIMIT VALUE' IS NOT SUPPORTED BY SNOWFLAKE. ***/!!!
  START WITH LIMIT VALUE
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}';
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0002

Columns from expression not found

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

High

### Description

This error happens when the columns of a Select Expression were unable to be resolved, usually when it either refers to a Type Access whose reference wasn’t resolved or a column with a User Defined Type whose columns haven’t been defined; such as a Type Without Body or Object Type with no columns.

#### Example Code

##### Input Code

```sql
 CREATE OR REPLACE PROCEDURE record_unknown_table_proc
AS
    unknownTable_variable_rowtype unknownTable%ROWTYPE;
BEGIN
    INSERT INTO MyTable values unknownTable_variable_rowtype;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE record_unknown_table_proc ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        unknownTable_variable_rowtype OBJECT !!!RESOLVE EWI!!! /*** SSC-EWI-0036 - ROWTYPE DATA TYPE CONVERTED TO OBJECT ***/!!! := OBJECT_CONSTRUCT();
    BEGIN
        INSERT INTO MyTable
        SELECT
            null !!!RESOLVE EWI!!! /*** SSC-EWI-OR0002 - COLUMNS FROM EXPRESSION unknownTable%ROWTYPE NOT FOUND ***/!!!;
    END;
$$;
```

#### Best Practices

* Verify that the type definition that was referenced does have columns within it.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0004

The used syntax in select is not supported in Snowflake.

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Severity

High

### Description

This warning happens when a clause in a select is not supported in Snowflake. The not supported clauses are:

* CONTAINERS
* HIERARCHIES
* EXTERNAL MODIFY
* SHARDS

#### Example Code

##### Input Code

```sql
 SELECT * FROM TABLE1 EXTERNAL MODIFY (LOCATION 'file.csv' REJECT LIMIT UNLIMITED);
```

##### Generated Code

```sql
 SELECT * FROM
TABLE1
       !!!RESOLVE EWI!!! /*** SSC-EWI-OR0004 - THE 'OPTIONAL MODIFIED EXTERNAL' SYNTAX IN SELECT IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
       EXTERNAL MODIFY (LOCATION 'file.csv' REJECT LIMIT UNLIMITED);
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0005

BFILE/BLOB parameters are considered binary. A format may be needed.

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-OR0043](../functional-difference/oracleFDM.md) documentation.

### Severity

Low

### Description

This error happens when a TO_CLOB is converted to a TO_VARCHAR function. A format may be needed for BFILE/BLOB parameters.

#### Example Code

##### Input Code

```sql
 SELECT TO_CLOB('Lorem ipsum dolor sit amet') FROM DUAL;
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0005 - BFILE/BLOB PARAMETERS ARE CONSIDERED BINARY, FORMAT MAY BE NEEDED ***/!!!
TO_VARCHAR('Lorem ipsum dolor sit amet')
FROM DUAL;
```

#### Best Practices

* Check if outputs in the input code and converted code are equivalent and add a format parameter if needed.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0006

It may be needed to set a TimeStampOutput format.

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-OR0047](../functional-difference/oracleFDM.md) documentation.

### Severity

Low

### Description

TIMESTAMP_OUTPUT_FORMAT session parameter may need to be set to ‘DD-MON-YY HH24.MI.SS.FF AM TZH:TZM’ for timestamp output equivalence.

#### Example Code

##### Input Code

```sql
 SELECT SYSTIMESTAMP FROM DUAL;
```

##### Example of default TIMESTAMP output in Oracle

> **Output:**
>
> 13-JAN-21 04.18.37.288656 PM +00:00

##### Generated Code

```sql
 SELECT
CURRENT_TIMESTAMP() !!!RESOLVE EWI!!! /*** SSC-EWI-OR0006 - YOU MAY NEED TO SET TIMESTAMP OUTPUT FORMAT ('DD-MON-YY HH24.MI.SS.FF AM TZH:TZM') ***/!!!
FROM DUAL;
```

##### Example of default TIMESTAMP output in Snowflake

> **Output:**
>
> 2021-01-13 08:18:19.720 -080

#### Best Practices

* To change the timestamp output format in Snowflake use the following query:

  ```
  ALTER SESSION SET TIMESTAMP_OUTPUT_FORMAT = 'DD-MON-YY HH24.MI.SS.FF AM TZH:TZM';
  ```

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0007

Create Type Not Supported in Snowflake

### Description

This message is added when a Create Type statement not supported by Snowflake is used.

#### Example Code

##### Input Code (Oracle)

```sql
 CREATE TYPE type6 UNDER type5(COL1 INTEGER);
```

##### Generated Code

```sql
 --!!!RESOLVE EWI!!! /*** SSC-EWI-OR0007 - CREATE TYPE SUBTYPE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
--CREATE TYPE type6 UNDER type5(COL1 INTEGER)
                                           ;
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0008

Unknown format, it may have unexpected behavior.

### Severity

Low

### Description

This error is added for unknown date formats that may have unexpected behavior.

#### Example Code

##### Input Code

```sql
 SELECT TO_CHAR(DATE '1998-12-25','iw-iyyy') FROM DUAL;
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0008 - UNKNOWN FORMAT, MAY HAVE UNEXPECTED BEHAVIOR ***/!!!
 TO_CHAR(DATE '1998-12-25','iw-iyyy'') FROM DUAL;
```

> **Note:**
>
> Note that ‘iw-iyyy’’ is not a supported format.

#### Best Practices

* Check for this [documentation](https://docs.snowflake.com/en/sql-reference/data-types-datetime.html#date-and-time-formats) for the supported timestamp formats.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0009

JSON_TABLE is not supported.

### Severity

High

### Description

JSON_TABLE function is not currently supported.

#### Example Code

##### Input Code

```sql
 SELECT jt.phones
FROM j_purchaseorder,
JSON_TABLE(po_document, '$.ShippingInstructions'
COLUMNS
(phones VARCHAR2(100) FORMAT JSON PATH '$.Phone')) AS jt;
```

##### Generated Code

```sql
 SELECT jt.phones
FROM
j_purchaseorder,
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0009 - JSON_TABLE IS NOT SUPPORTED ***/!!!
JSON_TABLE(po_document, '$.ShippingInstructions'
COLUMNS
(phones VARCHAR(100) FORMAT JSON PATH '$.Phone')) AS jt;
```

#### Best Practices

* You can take advantage of the [FLATTEN](https://docs.snowflake.com/en/sql-reference/functions/flatten.html) function in Snowflake to emulate the functionality of JSON_TABLE.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0010

Partitions Clauses are Handled by Snowflake. It requires manual fix

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Severity

Critical

### Description

This warning appears when the `PARTITION` and `SUBPARTITION` clauses appear within a query. Snowflake handle partitions automatically

#### Example Code

##### Input Code

```sql
 SELECT * FROM table1 PARTITION(col1);
```

##### Generated Code

```sql
 SELECT * FROM
table1
        !!!RESOLVE EWI!!! /*** SSC-EWI-OR0010 - PARTITIONS CLAUSES ARE HANDLED BY SNOWFLAKE. IT REQUIRES MANUAL FIX ***/!!!
        PARTITION(col1);
```

#### Best Practices

* Manual change is required to get equivalent functionality in Snowflake. A `WHERE` condition is needed to filter the rows for the specific partition. However, with this workaround, performance is affected.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0011

The format parameter is not supported.

### Severity

Medium

### Description

The format parameter is not currently supported by Snowflake for Cast functions in especial cases. For example, when we use “MONTH” or “DAY” inside the DATE or TIMESTAMP format.

```none
"MONTH/DD/YYYY" or "MM/DAY/YY" ...
```

Other scenario is when you are working with CAST function using NUMBER currently Snowflake need to have 4 arguments to show the decimal part, for now the output code not offer all arguments needed for Snowflake, you need to add the rest arguments for [TO_NUMBER](https://docs.snowflake.com/en/sql-reference/functions/to_decimal) function.

#### Example Code

##### Input Code

```sql
 SELECT CAST('12.48' AS NUMBER, '99.99') FROM DUAL;
```

##### Generated Code

```sql
 SELECT
TO_NUMBER('12.48', '99.99', 38, 2)
FROM DUAL;
```

##### Input Code

```sql
 SELECT CAST('FEBRUARY/18/24' as DATE, 'MONTH/DD/YY') FROM DUAL;
SELECT CAST('FEB/MON/24' as DATE, 'MON/DAY/YY') FROM DUAL;
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0011 - THE FORMAT PARAMETER 'MONTH/DD/YY' IS NOT SUPPORTED ***/!!!
TO_TIMESTAMP ('FEBRUARY/18/24' , 'MONTH/DD/YY')
FROM DUAL;

SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0011 - THE FORMAT PARAMETER 'MON/DAY/YY' IS NOT SUPPORTED ***/!!!
TO_TIMESTAMP ('FEB/MON/24' , 'MON/DAY/YY')
FROM DUAL;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0013

NLS parameter is not supported.

### Severity

Medium

### Description

NLS parameter is not currently supported for the following functions:

* TOCHAR
* TODATE
* TONUMBER
* TOTIMESTAMP
* CAST

#### Example Code

##### Input Code

```sql
 SELECT TO_NUMBER('-AusDollars100','9G999D99', ' NLS_NUMERIC_CHARACTERS = '',.''NLS_CURRENCY= ''AusDollars''') "Amount" FROM DUAL;
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0013 - NLS PARAMETER ' NLS_NUMERIC_CHARACTERS = '',.''NLS_CURRENCY= ''AusDollars''' NOT SUPPORTED ***/!!!
TO_NUMBER('-AusDollars100', '9G999D99') "Amount" FROM DUAL;
```

## SSC-EWI-OR0014

NLSSORT not supported.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Medium

### Description

NLSSORT function is not currently supported in the body of a select.

#### Example Code

##### Input Code

```sql
 SELECT NLSSORT(name, 'NLS_SORT = ENGLISH') FROM products;
```

##### Generated Code

```sql
 // SnowConvert AI Helpers Code section is omitted.
SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0014 - FUNCTION NLSSORT IS NOT SUPPORTED ***/!!!
 NLSSORT(name, 'NLS_SORT = ENGLISH') FROM
 products;
```

#### Best Practices

* NLSSORT is converted to a user-defined function (UDF/Stub), so you can modify it to emulate the functionality.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0016

XML is not supported.

### Severity

Medium

### Description

The following XML related functions are not supported:

* EXTRACT
* EXTRACTVALUE
* XMLSEQUENCE
* XMLTYPE

#### Example Code

##### Input Code

```sql
 select * from table(XMLSequence(XMLType('
<Product ProductCode="200">
 <BrandName>Notebook</BrandName>
 <ProductList>
  <Item ItemNo="200A"><Price>900</Price></Item>
  <Item ItemNo="200B"><Price>700</Price></Item>
  <Item ItemNo="200C"><Price>650</Price></Item>
  <Item ItemNo="200D"><<Price>750</Price></Item>
</ProductList>
</Product>')));
```

##### Generated Code

```sql
 select * from table(
                    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0016 - FUNCTION RELATED WITH XML NOT SUPPORTED ***/!!!
XMLSequence(
            !!!RESOLVE EWI!!! /*** SSC-EWI-OR0016 - FUNCTION RELATED WITH XML NOT SUPPORTED ***/!!!XMLType('
<Product ProductCode="200">
 <BrandName>Notebook</BrandName>
 <ProductList>
  <Item ItemNo="200A"><Price>900</Price></Item>
  <Item ItemNo="200B"><Price>700</Price></Item>
  <Item ItemNo="200C"><Price>650</Price></Item>
  <Item ItemNo="200D"><<Price>750</Price></Item>
</ProductList>
</Product>')));
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0020

Negative values not supported for function.

### Severity

Medium

### Description

Snowflake does not support negative values for the function, then this will cause different behavior when executed.

#### Example Code

##### Input Code

```sql
 SELECT INSTR('CORPORATE FLOOR','OR', -3, 2) FROM DUAL;
```

##### Generated Code

```sql
 SELECT
REGEXP_INSTR('CORPORATE FLOOR','OR', -3, 2) !!!RESOLVE EWI!!! /*** SSC-EWI-OR0020 - NEGATIVE VALUES NOT SUPPORTED FOR FUNCTION ***/!!! FROM DUAL;
```

#### Best Practices

* Create a User Defined Function that can handle the negative parameter or look for another alternative.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0023

AGGREGATE function not supported.

### Severity

High

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

This error is added when an aggregate function as

* DENSE_RANK()
* RANK()
* PERCENT_RANK()
* CUME_DIST()

is not supported in Snowflake.

#### Example Code

##### Input Code

```sql
 SELECT DENSE_RANK(12000) WITHIN GROUP (ORDER BY salary DESC NULLS FIRST) FROM employees;

SELECT RANK(12000) WITHIN GROUP (ORDER BY salary DESC NULLS FIRST) FROM employees;

SELECT PERCENT_RANK(12000) WITHIN GROUP (ORDER BY salary DESC NULLS FIRST) FROM employees;

SELECT CUME_DIST(12000) WITHIN GROUP (ORDER BY salary DESC NULLS FIRST) FROM employees;
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0023 - DENSE_RANK AGGREGATE FUNCTION SYNTAX IS NOT SUPPORTED BY SNOWFLAKE. ***/!!!
 DENSE_RANK(12000) WITHIN GROUP (ORDER BY salary DESC NULLS FIRST) FROM
 employees;

SELECT
 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0023 - RANK AGGREGATE FUNCTION SYNTAX IS NOT SUPPORTED BY SNOWFLAKE. ***/!!! RANK(12000) WITHIN GROUP (ORDER BY salary DESC NULLS FIRST) FROM
 employees;

SELECT
 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0023 - PERCENT_RANK AGGREGATE FUNCTION SYNTAX IS NOT SUPPORTED BY SNOWFLAKE. ***/!!! PERCENT_RANK(12000) WITHIN GROUP (ORDER BY salary DESC NULLS FIRST) FROM
 employees;

SELECT
 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0023 - CUME_DIST AGGREGATE FUNCTION SYNTAX IS NOT SUPPORTED BY SNOWFLAKE. ***/!!! CUME_DIST(12000) WITHIN GROUP (ORDER BY salary DESC NULLS FIRST) FROM
 employees;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0026

ROWID is not supported.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Medium

### Description

ROWID statement is not currently supported.

#### Example Code

##### Oracle

```sql
 SELECT QUERY_NAME.ROWID from TABLE1;
```

##### Snowflake Scripting

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0026 - ROWID NOT SUPPORTED ***/!!!
 QUERY_NAME.ROWID from
 TABLE1;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0029

DEFAULT ON CONVERSION ERROR is not supported.

### Description

Default on conversion error not supported in Snowflake

#### Example Code

##### Input Code

```sql
 SELECT TO_NUMBER('2,00' DEFAULT 0 ON CONVERSION ERROR) "Value" FROM DUAL;
```

##### Generated Code

```sql
 SELECT
PUBLIC.TO_NUMBER_UDF('2,00', 0) "Value" FROM DUAL;
```

#### Best Practices

* You might create UDF to emulate the behavior of `DEFAULT` value `ON CONVERSION ERROR`.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0030

KEEP statement used in the aggregate function is not supported

### Severity

Medium

### Description

This error appears to advertise that the KEEP statement used to indicate that only the first or last values of the aggregate function will be returned is not supported

#### Example Code

##### Input Code

```sql
 SELECT
    department_id,
    MIN(salary) KEEP (
        DENSE_RANK FIRST
        ORDER BY
            commission_pct
    ) "Worst"
FROM
    employees;
```

##### Generated Code

```sql
 SELECT
    department_id,
    MIN(salary)
        !!!RESOLVE EWI!!! /*** SSC-EWI-OR0030 - KEEP STATEMENT USED IN THE AGGREGATE FUNCTION IS NOT SUPPORTED ***/!!!
 KEEP (
        DENSE_RANK FIRST
        ORDER BY
            commission_pct
    ) "Worst"
FROM
 employees;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0031

SYS_CONTEXT parameter is not supported.

### Severity

Low

### Description

This error happens when a SYS_CONTEXT function parameter is not supported. Snowflake support similar context functions, check the [page](https://docs.snowflake.com/en/sql-reference/functions-context) to more information

#### Example Code

##### Input Code

```sql
 SELECT SYS_CONTEXT ('USERENV', 'NLS_SORT') FROM DUAL;
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0031 - 'NLS_SORT' SYS_CONTEXT PARAMETER NOT SUPPORTED IN SNOWFLAKE ***/!!!
 SYS_CONTEXT ('USERENV', 'NLS_SORT') FROM DUAL;
```

#### Best Practices

* The function is converted to a user defined function(stub), so you can modify it to emulate the behavior of the SYS_CONTEXT parameter.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0032

Parameter with the specified format is not supported.

### Severity

Medium

### Description

This error happens when a parameter in a function is not supported.

#### Example Code

##### Input Code

```sql
 SELECT TO_CHAR(DATE '1998-12-25', 'AM') FROM DUAL;
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0032 - PARAMETER USED IN THE FUNCTION 'TO_CHAR' WITH FORMAT AM IS NOT SUPPORTED ***/!!!
 TO_CHAR(DATE '1998-12-25', 'AM') FROM DUAL;
```

#### Best Practices

* The function is converted to a user defined function(stub), so you can modify it to emulate the behavior of the parameter.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0033

PL/SQL declaration in WITH is not supported.

### Severity

Medium

### Description

PL/SQL declarations in WITH statements are not supported.

#### Example Code

##### Input Code

```sql
 WITH FUNCTION get_domain ( url VARCHAR2 ) RETURN VARCHAR2 IS pos BINARY_INTEGER;
len BINARY_INTEGER;
BEGIN
pos := INSTR(url, 'www.');
len := INSTR(SUBSTR(url, pos + 4), '.') - 1;
END; SELECT aValue from aTable;
```

##### Generated Code

```sql
 // SnowConvert AI Helpers Code section is omitted.
WITH
     !!!RESOLVE EWI!!! /*** SSC-EWI-OR0033 - PLDECLARATION IN WITH NOT SUPPORTED ***/!!!
 FUNCTION get_domain ( url VARCHAR2 ) RETURN VARCHAR2 IS pos BINARY_INTEGER;
len BINARY_INTEGER;
BEGIN
pos := INSTR(url, 'www.');
len := INSTR(SUBSTR(url, pos + 4), '.') - 1;
END; SELECT aValue from
aTable;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0035

The table function is not supported when it is used as a collection of expressions.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Medium

### Description

TABLE function is not supported in Snowflake when it is used as a collection of expressions.

#### Example Code

##### Input Code

```sql
 SELECT
TABLE2.COLUMN_VALUES
FROM TABLE1 i, TABLE(i.groups) TABLE2;
```

##### Generated Code

```sql
 // SnowConvert AI Helpers Code section is omitted.
SELECT
TABLE2.COLUMN_VALUES
FROM
TABLE1 i,
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0035 - TABLE FUNCTION IS NOT SUPPORTED WHEN IT IS USED AS A COLLECTION OF EXPRESSIONS ***/!!! TABLE(i.groups) TABLE2;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0036

Types resolution issues, the arithmetic operation may not behave correctly between string and date.

### Severity

Low

### Description

This issue happens when an arithmetic operation may not behave correctly between two certain data types.

#### Example Code

##### Input Code

```sql
 SELECT
    SYSDATE,
    SYSDATE + '1',
    SYSDATE + 'A'
from
    dual;
```

##### Generated Code

```sql
 SELECT
    CURRENT_TIMESTAMP(),
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0036 - TYPES RESOLUTION ISSUES, ARITHMETIC OPERATION '+' MAY NOT BEHAVE CORRECTLY BETWEEN Date AND String ***/!!!
    CURRENT_TIMESTAMP() + '1',
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0036 - TYPES RESOLUTION ISSUES, ARITHMETIC OPERATION '+' MAY NOT BEHAVE CORRECTLY BETWEEN Date AND String ***/!!!
    CURRENT_TIMESTAMP() + 'A'
from
    dual;
```

> **Note:**
>
> Note that the operation between a String and Date may not behave correctly.

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0038

Search clause removed from the with element statement.

### Severity

Low

### Description

The [`search_clause`](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/SELECT.html#GUID-CFA006CA-6FF1-4972-821E-6996142A51C6__I2077142) is employed to define the order in which rows are processed in a SELECT statement. This functionality allows for a customized traversal of the data, ensuring that the results are returned in a specific sequence based on the specified criteria. It is important to note, however, that this behavior, characterized by the [`search_clause`](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/SELECT.html#GUID-CFA006CA-6FF1-4972-821E-6996142A51C6__I2077142), is not supported in Snowflake.

In databases such as Oracle, the [`search_clause`](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/SELECT.html#GUID-CFA006CA-6FF1-4972-821E-6996142A51C6__I2077142) is commonly used in conjunction with recursive queries or common table expressions (CTEs) to influence the sequence in which hierarchical data is explored. By designating a particular column or set of columns in the [`search_clause`](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/SELECT.html#GUID-CFA006CA-6FF1-4972-821E-6996142A51C6__I2077142), you can control the depth-first or breadth-first traversal of the hierarchy, impacting the order in which rows are processed.

In Snowflake, [`search_clause`](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/SELECT.html#GUID-CFA006CA-6FF1-4972-821E-6996142A51C6__I2077142) message will be generated, and the [`search_clause`](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/SELECT.html#GUID-CFA006CA-6FF1-4972-821E-6996142A51C6__I2077142) is subsequently eliminated.

#### Example Code

##### Input Code

```sql
 WITH dup_hiredate(eid, emp_last, mgr_id, reportLevel, hire_date, job_id) AS
(SELECT aValue from atable) SEARCH DEPTH FIRST BY hire_date SET order1 SELECT aValue from atable;
```

##### Generated Code

```sql
 WITH dup_hiredate(eid, emp_last, mgr_id, reportLevel, hire_date, job_id) AS
(
SELECT aValue from
atable
) !!!RESOLVE EWI!!! /*** SSC-EWI-OR0038 - SEARCH CLAUSE REMOVED FROM THE WITH ELEMENT STATEMENT ***/!!!
SELECT aValue from
atable;
```

#### Recommendation

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0039

The nocycle clause is not supported in Snowflake.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Low

### Description

This message is shown when SnowConvert AI finds a query with a NOCYCLE clause, which is not supported in Snowflake.

This clause marks when there is a recursion.

For more details see the [documentation](https://docs.oracle.com/en/database/oracle/oracle-database/23/sqlrf/SELECT.html#GUID-CFA006CA-6FF1-4972-821E-6996142A51C6__GUID-8EE64250-3C9A-40C7-A81D-46695F8B2EB9) about the clause functionality.

#### Example Code

#### Connect By

##### Input Code

```sql
 CREATE OR REPLACE FORCE NONEDITIONABLE VIEW VIEW01 AS
SELECT
      UNIQUE A.*
FROM
      TABLITA A
WHERE
      A.X = A.C CONNECT BY NOCYCLE A.C = 0 START WITH A.B = 1
HAVING
      X = 1
GROUP BY
      A.C;
```

##### Generated Code

```sql
 CREATE OR REPLACE VIEW VIEW01
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
AS
SELECT DISTINCT
      A.*
FROM
      TABLITA A
WHERE
      A.X = A.C
GROUP BY
      A.C
HAVING
      X = 1
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0039 - NOCYCLE CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
CONNECT BY
      A.C = 0 START WITH A.B = 1;
```

#### Best Practices

* If there are cycles in the data hierarchy, you can review this [article](https://docs.snowflake.com/en/user-guide/queries-cte#cause-1-cyclic-data-hierarchy) to deal with them.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com).
* Please review the following link for manual workaround: <https://community.snowflake.com/s/article/NOCYCLE-workaround>

## SSC-EWI-OR0042

Model clause is not supported.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Low

### Description

This message is shown when SnowConvert AI finds a query with a MODEL clause, which is not supported in Snowflake.

#### Example Code

##### Input Code

```sql
 SELECT
   employee_id,
   salary
FROM
   employees
MODEL
DIMENSION BY (employee_id)
MEASURES (salary)
();
```

##### Generated Code

```sql
 SELECT
   employee_id,
   salary
FROM
   employees
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0042 - MODEL CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
MODEL
DIMENSION BY (employee_id)
MEASURES (salary)
();
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0045

Cast type L and FML is not supported

### Severity

Medium

### Description

This issue happens when trying to cast using FML or L format that is not applicable in Snowflake, then the code is commented out and this message is being added.

#### Example Code

##### Input Code

```sql
 SELECT CAST(' $123.45' as number, 'L999.99') FROM DUAL;
SELECT CAST('$123.45' as number, 'FML999.99') FROM DUAL;
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0045 - CAST TYPE L AND FML NOT SUPPORTED ***/!!!
 CAST(' $123.45' as NUMBER(38, 18) , 'L999.99') FROM DUAL;

SELECT
 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0045 - CAST TYPE L AND FML NOT SUPPORTED ***/!!! CAST('$123.45' as NUMBER(38, 18) , 'FML999.99') FROM DUAL;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0046

Alter Table syntax is not applicable in Snowflake.

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-EWI-0109](generalEWI.md) documentation

### Severity

Medium

### Description

The Alter Table syntax used is not applicable in Snowflake, then the code is commented out and this message is being added.

#### Example Code

##### Input Code

```sql
 ALTER TABLE SOMENAME DEFAULT COLLATION SOMENAME;

ALTER TABLE SOMENAME ROW ARCHIVAL;

ALTER TABLE SOMENAME MODIFY CLUSTERING;

ALTER TABLE SOMENAME DROP CLUSTERING;

ALTER TABLE SOMENAME SHRINK SPACE COMPACT CASCADE;
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-0109 - ALTER TABLE SYNTAX NOT APPLICABLE IN SNOWFLAKE ***/!!!
--** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "SOMENAME" **
ALTER TABLE SOMENAME
DEFAULT COLLATION SOMENAME;

!!!RESOLVE EWI!!! /*** SSC-EWI-0109 - ALTER TABLE SYNTAX NOT APPLICABLE IN SNOWFLAKE ***/!!!
--** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "SOMENAME" **

ALTER TABLE SOMENAME
ROW ARCHIVAL;

!!!RESOLVE EWI!!! /*** SSC-EWI-0109 - ALTER TABLE SYNTAX NOT APPLICABLE IN SNOWFLAKE ***/!!!
--** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "SOMENAME" **

ALTER TABLE SOMENAME
MODIFY CLUSTERING;

!!!RESOLVE EWI!!! /*** SSC-EWI-0109 - ALTER TABLE SYNTAX NOT APPLICABLE IN SNOWFLAKE ***/!!!
--** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "SOMENAME" **

ALTER TABLE SOMENAME
DROP CLUSTERING;

!!!RESOLVE EWI!!! /*** SSC-EWI-0109 - ALTER TABLE SYNTAX NOT APPLICABLE IN SNOWFLAKE ***/!!!
--** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "SOMENAME" **

ALTER TABLE SOMENAME
SHRINK SPACE COMPACT CASCADE;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0047

TO_NCHAR transformed to TO_VARCHAR, it may not be compilable in Snowflake.

### Severity

Low

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

This warning is added when the function `TO_NCHAR` was found and it was transformed into a `TO_VARCHAR` function.

There are multiple cases where the transformation causes a compilation error, or the output is not the same.

#### Example Code

##### Input Code

```sql
 select TO_NCHAR(sysdate,'DY','nls_date_language=english') from dual
```

##### Generated Code

```sql
 select
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0047 - TO_NCHAR TRANSFORMED TO TO_VARCHAR, IT MAY NOT BE COMPILABLE IN SNOWFLAKE ***/!!!
TO_VARCHAR(CURRENT_TIMESTAMP(),'DY','nls_date_language=english') from dual;
```

The example from above will result in an error if it is used in Snowflake.

Not all cases are causing errors.

##### Input Code

```sql
 SELECT TO_NCHAR(SYSDATE, 'YYYY-MM-DD') FROM dual;
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0047 - TO_NCHAR TRANSFORMED TO TO_VARCHAR, IT MAY NOT BE COMPILABLE IN SNOWFLAKE ***/!!!
TO_VARCHAR(CURRENT_TIMESTAMP(), 'YYYY-MM-DD') FROM dual;
```

The last example does not cause an error in Snowflake, and the output is equivalent if executed.

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0049

Package constants in stateful package are not supported yet.

### Severity

Critical

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

This warning is added when there is a member of a Stateful Package that is not supported yet.

This feature is planned to be delivered in the future.

#### Example Code

##### Input Code

```sql
 CREATE OR REPLACE PACKAGE MY_PACKAGE
AS
    TYPE COLLECTIONTYPEDEFINITION IS TABLE OF BULKCOLLECTTABLE%ROWTYPE;
END;
```

##### Generated Code

```sql
 CREATE SCHEMA IF NOT EXISTS MY_PACKAGE
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
;

!!!RESOLVE EWI!!! /*** SSC-EWI-OR0049 - PACKAGE TYPE DEFINITIONS in stateful package MY_PACKAGE are not supported yet ***/!!!
TYPE COLLECTIONTYPEDEFINITION IS TABLE OF BULKCOLLECTTABLE%ROWTYPE;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0050

Input Expression is out of the range

### Severity

Medium

### Description

This issue happens when trying to cast an input value that is out of range. It means the precision values are not applicable in Snowflake, then the code is commented out and this message is being added.

#### Example Code

##### Input Code

```sql
 SELECT CAST('123,456E+40' AS NUMBER, '999,999EEE') FROM DUAL;
SELECT CAST('12.34567891234567891234567891234567891267+' AS NUMBER, '99.999999999999999999999999999999999999S') FROM DUAL;
SELECT CAST('12.34567891234567891234567891234567891267' AS NUMBER, '99.999999999999999999999999999999999999') FROM DUAL;
select cast(' 1.0E+123' as number, '9.9EEEE') from dual;
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0050 - INPUT EXPRESSION IS OUT OF THE RANGE '123,456E+40' ***/!!!
 CAST('123,456E+40' AS NUMBER(38, 18) , '999,999EEE') FROM DUAL;

SELECT
 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0050 - INPUT EXPRESSION IS OUT OF THE RANGE '12.34567891234567891234567891234567891267+' ***/!!! CAST('12.34567891234567891234567891234567891267+' AS NUMBER(38, 18) , '99.999999999999999999999999999999999999S') FROM DUAL;

SELECT
 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0050 - INPUT EXPRESSION IS OUT OF THE RANGE '12.34567891234567891234567891234567891267' ***/!!! CAST('12.34567891234567891234567891234567891267' AS NUMBER(38, 18) , '99.999999999999999999999999999999999999') FROM DUAL;

select
 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0050 - INPUT EXPRESSION IS OUT OF THE RANGE ' 1.0E+123' ***/!!! cast(' 1.0E+123' as NUMBER(38, 18) , '9.9EEEE') from dual;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0051

PRAGMA EXCEPTION_INIT is not supported.

### Severity

Low

### Description

This EWI is added when PRAGMA EXCEPTION_INIT function is invoked within a procedure. Exception Name and SQL Code of the exceptions are set in the RAISE function. When it is converted to Snowflake Scripting, the SQL Code is added to the Exception declaration, however, some code values may be invalid in Snowflake Scripting.

#### Example Code

##### Input Code

```sql
 CREATE OR REPLACE PROCEDURE EXCEPTION_DECLARATION_SAMPLE AUTHID DEFINER IS
  NEW_EXCEPTION EXCEPTION;
  PRAGMA EXCEPTION_INIT(NEW_EXCEPTION, -63);
  NEW_EXCEPTION2 EXCEPTION;
  PRAGMA EXCEPTION_INIT ( NEW_EXCEPTION2, -20100 );
BEGIN

  IF true THEN
    RAISE NEW_EXCEPTION;
  END IF;

EXCEPTION
    WHEN NEW_EXCEPTION THEN
        --Handle Exceptions
        NULL;
END;
/
```

##### Generated Code

##### Snowflake script

```sql
 CREATE OR REPLACE PROCEDURE EXCEPTION_DECLARATION_SAMPLE ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
EXECUTE AS CALLER
AS
$$
  DECLARE
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0099 - EXCEPTION CODE NUMBER EXCEEDS SNOWFLAKE SCRIPTING LIMITS ***/!!!
    NEW_EXCEPTION EXCEPTION;
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0051 - PRAGMA EXCEPTION_INIT IS NOT SUPPORTED ***/!!!
    PRAGMA EXCEPTION_INIT(NEW_EXCEPTION, -63);
    NEW_EXCEPTION2 EXCEPTION (-20100, '');
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0051 - PRAGMA EXCEPTION_INIT IS NOT SUPPORTED ***/!!!
  PRAGMA EXCEPTION_INIT ( NEW_EXCEPTION2, -20100 );
  BEGIN
    IF (true) THEN
      RAISE NEW_EXCEPTION;
    END IF;
    EXCEPTION
        WHEN NEW_EXCEPTION THEN
            --Handle Exceptions
            NULL;
    END;
$$;
```

#### Best Practices

* No end-user action is required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0052

Exception declaration is handled by the raise function.

### Severity

Low

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

> **Note:**
>
> Generate Procedures and Macros using JavaScript as the target language adding the following flag `-t JavaScript` or `--PLTargetLanguage JavaScript`

### Description

Exceptions can be defined in both languages, Oracle and Snowflake, but the RAISE function is designed to do declaration, assignment, and throw the error. This is why the Exception declaration is commented out and the warning is displayed.

#### Example Code

##### Input Code

```sql
 -- Additional Params: -t JavaScript
CREATE OR REPLACE PROCEDURE EXCEPTION_DECLARATION_SAMPLE AUTHID DEFINER IS
  NEW_EXCEPTION EXCEPTION;
  PRAGMA EXCEPTION_INIT(NEW_EXCEPTION, -63);
BEGIN

  IF true THEN
    RAISE NEW_EXCEPTION;
  END IF;

EXCEPTION
    WHEN NEW_EXCEPTION THEN
        --Handle Exceptions
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE EXCEPTION_DECLARATION_SAMPLE ()
RETURNS STRING
LANGUAGE JAVASCRIPT
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "12/16/2024",  "domain": "test" }}'
EXECUTE AS CALLER
AS
$$
  !!!RESOLVE EWI!!! /*** SSC-EWI-0073 - PENDING FUNCTIONAL EQUIVALENCE REVIEW FOR 'PlInvokerRightsClause' NODE ***/!!!
  //AUTHID DEFINER
  null
  // SnowConvert AI Helpers Code section is omitted.

  try {
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0052 - EXCEPTION DECLARATION IS HANDLED BY RAISE FUNCTION ***/!!!
    /*   NEW_EXCEPTION EXCEPTION */
    ;
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0051 - PRAGMA EXCEPTION_INIT IS NOT SUPPORTED ***/!!!
    /*   PRAGMA EXCEPTION_INIT(NEW_EXCEPTION, -63) */
    ;
    if (true) {
      RAISE(-63,`NEW_EXCEPTION`,`NEW_EXCEPTION`);
    }
  } catch(error) {
    switch(error.name) {
      case `NEW_EXCEPTION`: {
        break;
      }
      default: {
        throw error;
        break;
      }
    }
  }
  //Handle Exceptions
  ;
$$;
```

> **Note:**
>
> Some parts of the output code are omitted to improve readability.

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0053

Incorrect input format

### Severity

Medium

### Description

This issue happens when trying to cast using a wrong input format, then the code is commented out and this message is being added.

#### Example Code

##### Input Code

```sql
 SELECT CAST('12sdsd3,456E+40' AS NUMBER, '999,999EEE') FROM DUAL;
SELECT CAST('12345sdsd' AS NUMBER, '99999') FROM DUAL;
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0053 - INCORRECT INPUT FORMAT '12sdsd3,456E+40' ***/!!!
 CAST('12sdsd3,456E+40' AS NUMBER(38, 18) , '999,999EEE') FROM DUAL;

SELECT
 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0053 - INCORRECT INPUT FORMAT '12345sdsd' ***/!!! CAST('12345sdsd' AS NUMBER(38, 18) , '99999') FROM DUAL;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0057

Transformation for nested procedure or function is not supported in this scenario.

### Severity

Critical

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

Translation of nested functions inside other functions or procedures is not supported. Similarly, procedures nested within functions or anonymous blocks are not currently supported.

However, nested procedures within other procedures or packages are supported. For additional details, see the [Nested Procedures Documentation](../../../../translation-references/oracle/pl-sql-to-snowflake-scripting/README.md).

#### Example Code

##### Input Code

```sql
CREATE OR REPLACE function FOO1 RETURN INTEGER AS
    FUNCTION FOO2 RETURN INTEGER AS
    BEGIN
        RETURN 123;
    END;
BEGIN
    RETURN FOO2() + 456;
END;
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-0068 - USER DEFINED FUNCTION WAS TRANSFORMED TO SNOWFLAKE PROCEDURE ***/!!!!!!RESOLVE EWI!!! /*** SSC-EWI-0046 - NESTED FUNCTION/PROCEDURE DECLARATIONS ARE NOT SUPPORTED IN SNOWFLAKE. ***/!!!
CREATE OR REPLACE PROCEDURE FOO1 ()
RETURNS INTEGER
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        !!!RESOLVE EWI!!! /*** SSC-EWI-OR0057 - TRANSFORMATION FOR NESTED FUNCTION IS NOT SUPPORTED IN THIS SCENARIO ***/!!!
        FUNCTION FOO2 RETURN INTEGER AS
        BEGIN
            RETURN 123;
        END;
    BEGIN
        RETURN FOO2() + 456;
    END;
$$;
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0067

Multiple constraint definition in a single statement is not supported in Snowflake.

### Severity

Medium

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

Multiple Constraint Definition in a single ALTER TABLE statement is not supported in Snowflake.

#### Example Code

##### Oracle

```sql
 ALTER TABLE TABLE1 ADD (
  CONSTRAINT TABLE1_PK
  PRIMARY KEY
  (ID)
  ENABLE VALIDATE,
  CONSTRAINT TABLE1_FK foreign key(ID2)
  references TABLE2 (ID) ON DELETE CASCADE);
```

##### Snowflake Scripting

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0067 - MULTIPLE CONSTRAINT DEFINITION IN A SINGLE STATEMENT IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
ALTER TABLE TABLE1
ADD (
  CONSTRAINT TABLE1_PK
  PRIMARY KEY
  (ID) ,
  CONSTRAINT TABLE1_FK foreign key(ID2)
  references TABLE2 (ID) ON DELETE CASCADE);
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0068

The sequence start value exceeds the max value allowed by Snowflake.

### Severity

Medium

### Description

This error appears when the `START WITH` statement value exceeds the maximum value allowed by Snowflake. What Snowflake said about the start value is: *Specifies the first value returned by the sequence. Supported values are any value that can be represented by a 64-bit two’s complement integer (from `-2^63` to `2^63-1`)*. So according to the previously mentioned, the max value allowed is **9223372036854775807** for positive numbers and **9223372036854775808** for negative numbers.

#### Example Code

##### Input Code

```sql
 CREATE SEQUENCE SEQUENCE1
START WITH 9223372036854775808;
```

```sql
 CREATE SEQUENCE SEQUENCE2
START WITH -9223372036854775809;
```

##### Generated Code

```sql
 CREATE OR REPLACE SEQUENCE SEQUENCE1
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0068 - SEQUENCE START VALUE EXCEEDS THE MAX VALUE ALLOWED BY SNOWFLAKE. ***/!!!
START WITH 9223372036854775808
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}';
```

```sql
 CREATE OR REPLACE SEQUENCE SEQUENCE2
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0068 - SEQUENCE START VALUE EXCEEDS THE MAX VALUE ALLOWED BY SNOWFLAKE. ***/!!!
START WITH -9223372036854775809
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}';
```

#### Best Practices

* It can be recommended to just reset the sequence and modify its usage too. **NOTE**: the target column must have enough space to hold this value.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0069

The sequence CURRVAL property is not supported in Snowflake.

### Severity

Medium

### Description

The sequence CURRVAL property is not supported in Snowflake.

#### Example Code

##### Oracle

```sql
 select seq1.currval from dual;
```

##### Snowflake Scripting

```sql
 select
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0069 - THE SEQUENCE CURRVAL PROPERTY IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
 seq1.currval from dual;
```

#### Best Practices

* You can check this [link](https://docs.snowflake.com/en/user-guide/querying-sequences.html#currval-not-supported) to see what Snowflake suggests to handle situations where the CURRVAL property is used.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0070

Binary Operation Not Supported

### Severity

Medium

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

A binary operation is not currently supported, a user-defined function is added.

#### Example Code

##### Oracle

```sql
 -- Unsupported operation: EXCEPT DISTINCT
SELECT someValue MULTISET EXCEPT DISTINCT multiset_except FROM customers_demo;
```

##### Snowflake Scripting

```sql
 -- Unsupported operation: EXCEPT DISTINCT
SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0070 - BINARY OPERATION MULTISET EXCEPT IS NOT SUPPORTED ***/!!!
 someValue MULTISET EXCEPT DISTINCT multiset_except FROM
 customers_demo;
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0071

Set Quantifier Not Supported

### Severity

Low

### Description

Quantifier ‘all’ is not supported in Snowflake. The modifier is removed from the source code, and a warning is added; the resulting code may behave unexpectedly.

#### Example Code

##### Input Code

```sql
 SELECT location_id  FROM locations
MINUS ALL
SELECT location_id  FROM departments;
```

##### Generated Code

```sql
 SELECT location_id  FROM
locations
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0071 - QUANTIFIER 'ALL' NOT SUPPORTED FOR THIS SET OPERATOR, RESULTS MAY DIFFER ***/!!!
MINUS
SELECT location_id  FROM
departments;
```

In Snowflake, the INTERSECT and MINUS/EXCEPT operators will always remove duplicate values.

#### Best Practices

* Check alternatives in Snowflake to emulate the functionality of the “all” quantifier. Below is a workaround for `MINUS ALL` and `EXCEPT ALL`.

```sql
 SELECT location_id FROM
(
    SELECT location_id, ROW_NUMBER()OVER(PARTITION BY location_id ORDER BY 1) rn
    FROM locations
    MINUS
    SELECT number_val, ROW_NUMBER()OVER(PARTITION BY location_id ORDER BY 1) rn
    FROM departments
);
```

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0072

Procedural Member not supported

### Severity

Medium

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

> **Note:**
>
> Generate Procedures and Macros using JavaScript as the target language adding the following flag -t JavaScript or –PLTargetLanguage JavaScript

### Description

A procedural member is not currently supported. Example of procedural members:

* Constant declarations.
* Cursor declarations.
* Pragma declarations.
* Variable declarations.

#### Example Code

##### Oracle

```sql
 -- Additional Params: -t JavaScript
CREATE OR REPLACE EDITIONABLE PROCEDURE PROCEDURE1
   IS
   PRAGMA AUTONOMOUS_TRANSACTION;
BEGIN
    NULL;
END;
```

##### Snowflake Scripting

```sql
 --** SSC-FDM-OR0007 - SNOWFLAKE DOESN'T SUPPORT VERSIONING OF OBJECTS. DEVELOPERS SHOULD CONSIDER ALTERNATE APPROACHES FOR CODE VERSIONING. **
CREATE OR REPLACE PROCEDURE PROCEDURE1 ()
RETURNS STRING
LANGUAGE JAVASCRIPT
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "12/16/2024",  "domain": "test" }}'
EXECUTE AS CALLER
AS
$$
   // SnowConvert AI Helpers Code section is omitted.

   !!!RESOLVE EWI!!! /*** SSC-EWI-OR0072 - PROCEDURAL MEMBER PRAGMA DECLARATION NOT SUPPORTED. ***/!!!
   /*    PRAGMA AUTONOMOUS_TRANSACTION */
   ;
   null;
$$;
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0075

Labels in statements not supported

### Severity

Medium

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

> **Note:**
>
> Generate Procedures and Macros using JavaScript as the target language adding the following flag -t JavaScript or –PLTargetLanguage JavaScript

### Description

Labels in statements not supported to reference a code block.

#### Example Code

##### Oracle

```sql
 --Additional Params: -t JavaScript
CREATE OR REPLACE EDITIONABLE PROCEDURE PROCEDURE1
IS
BEGIN
    -- procedure body
    EXIT loop_b;
    -- procedure body continuation
END;
```

##### Snowflake Scripting

```sql
--Additional Params: -t JavaScript
--** SSC-FDM-OR0007 - SNOWFLAKE DOESN'T SUPPORT VERSIONING OF OBJECTS. DEVELOPERS SHOULD CONSIDER ALTERNATE APPROACHES FOR CODE VERSIONING. **
CREATE OR REPLACE PROCEDURE PROCEDURE1 ()
RETURNS STRING
LANGUAGE JAVASCRIPT
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "07/16/2025",  "domain": "no-domain-provided" }}'
EXECUTE AS CALLER
AS
$$
    // REGION SnowConvert AI Helpers Code
    var RAISE = function (code,name,message) {
        message === undefined && ([name,message] = [message,name])
        var error = new Error(message);
        error.name = name
        SQLERRM = `${(SQLCODE = (error.code = code))}: ${message}`
        throw error;
    };
    var SQL = {
        FOUND : false,
        NOTFOUND : false,
        ROWCOUNT : 0,
        ISOPEN : false
    };
    var _RS, _ROWS, SQLERRM = "normal, successful completion", SQLCODE = 0;
    var getObj = (_rs) => Object.assign(new Object(),_rs);
    var getRow = (_rs) => (values = Object.values(_rs)) && (values = values.splice(-1 * _rs.getColumnCount())) && values;
    var fetch = (_RS,_ROWS,fmode) => _RS.getRowCount() && _ROWS.next() && (fmode ? getObj : getRow)(_ROWS) || (fmode ? new Object() : []);
    var EXEC = function (stmt,binds,opts) {
        try {
            binds = !(arguments[1] instanceof Array) && ((opts = arguments[1]) && []) || (binds || []);
            opts = opts || new Object();
            binds = binds ? binds.map(fixBind) : binds;
            _RS = snowflake.createStatement({
                    sqlText : stmt,
                    binds : binds
                });
            _ROWS = _RS.execute();
            if (opts.sql !== 0) {
                var isSelect = stmt.toUpperCase().trimStart().startsWith("SELECT");
                var affectedRows = isSelect ? _RS.getRowCount() : _RS.getNumRowsAffected();
                SQL.FOUND = affectedRows != 0;
                SQL.NOTFOUND = affectedRows == 0;
                SQL.ROWCOUNT = affectedRows;
            }
            if (opts.row === 2) {
                return _ROWS;
            }
            var INTO = function (opts) {
                if (opts.vars == 1 && _RS.getColumnCount() == 1 && _ROWS.next()) {
                    return _ROWS.getColumnValue(1);
                }
                if (opts.rec instanceof Object && _ROWS.next()) {
                    var recordKeys = Object.keys(opts.rec);
                    Object.assign(opts.rec,Object.fromEntries(new Map(getRow(_ROWS).map((element,Index) => [recordKeys[Index],element]))))
                    return opts.rec;
                }
                return fetch(_RS,_ROWS,opts.row);
            };
            var BULK_INTO_COLLECTION = function (into) {
                for(let i = 0;i < _RS.getRowCount();i++) {
                    FETCH_INTO_COLLECTIONS(into,fetch(_RS,_ROWS,opts.row));
                }
                return into;
            };
            if (_ROWS.getRowCount() > 0) {
                return _ROWS.getRowCount() == 1 ? INTO(opts) : BULK_INTO_COLLECTION(opts);
            }
        } catch(error) {
            RAISE(error.code,error.name,error.message)
        }
    };
    var FETCH_INTO_COLLECTIONS = function (collections,fetchValues) {
        for(let i = 0;i < collections.length;i++) {
            collections[i].push(fetchValues[i]);
        }
    };
    var IS_NULL = (arg) => !(arg || arg === 0);
    var formatDate = (arg) => (new Date(arg - (arg.getTimezoneOffset() * 60000))).toISOString().slice(0,-1);
    var fixBind = function (arg) {
        arg = arg instanceof Date ? formatDate(arg) : IS_NULL(arg) ? null : arg;
        return arg;
    };
    // END REGION

    /*     -- procedure body
        EXIT loop_b */
    // procedure body
    // procedure body
    ;
    // procedure body continuation
    ;
$$;
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0076

Built In Package Not Supported.

### Severity

Medium

### Description

Translation for built-in packages is not currently supported.

#### Example Code

##### Input Code (Oracle)

```sql
 SELECT
UTL_RAW.CAST_TO_RAW('some magic here'),
DBMS_UTILITY.GET_TIME
FROM DUAL;
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0076 - TRANSLATION FOR BUILT-IN PACKAGE 'UTL_RAW.CAST_TO_RAW' IS NOT CURRENTLY SUPPORTED. ***/!!!
'' AS CAST_TO_RAW,
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0076 - TRANSLATION FOR BUILT-IN PACKAGE 'DBMS_UTILITY.GET_TIME' IS NOT CURRENTLY SUPPORTED. ***/!!!
'' AS GET_TIME
FROM DUAL;
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0078

Unable to parse dynamic SQL statement inside Execute Immediate.

### Severity

Medium

### Description

SnowConvert AI could not parse the dynamic SQL statement inside the Execute Immediate.

> **Note:**
>
> Generate Procedures and Macros using JavaScript as the target language adding the following flag `-t JavaScript` or `--PLTargetLanguage JavaScript`

#### Example Code

##### Oracle

```sql
 --Additional Params: -t JavaScript
CREATE OR REPLACE PROCEDURE PROC1 AS
BEGIN
    EXECUTE IMMEDIATE 'NOT A VALID SQL STATEMENT';
END;
```

##### Snowflake Scripting

```sql
 CREATE OR REPLACE PROCEDURE PROC1 ()
RETURNS STRING
LANGUAGE JAVASCRIPT
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "12/16/2024",  "domain": "test" }}'
EXECUTE AS CALLER
AS
$$
    // SnowConvert AI Helpers Code section is omitted.

    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0078 - UNABLE TO PARSE DYNAMIC SQL STATEMENT ***/!!!
    /*EXEC(`NOT A VALID SQL STATEMENT`)*/
    ;
$$;
```

#### Best Practices

* Check the dynamic SQL statement for any syntax error.
* Review the SnowConvert AI documentation to see if the statement is still unsupported.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0082

Cannot Convert Nested Type Attribute Expression

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Severity

Medium

### Description

This error message appears when a query, like a select, tries to access an attribute within a column that was defined as a type. These cannot be automatically converted, but they can be quickly converted by hand.

#### Example Code

##### Input Code Oracle

```sql
 CREATE TYPE type1 AS OBJECT (
  attribute1 VARCHAR2(20),
  attribute2 NUMBER
);
CREATE TYPE type2 AS OBJECT (
  property1 type1,
  property2 DATE
);
CREATE TABLE my_table (
  id NUMBER PRIMARY KEY,
  column1 type2
);
INSERT INTO my_table VALUES (
  1, type2(type1('value1', 100), SYSDATE)
);
SELECT column1.property1.attribute1, column1.property2
FROM my_table;
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-0056 - CUSTOM TYPES ARE NOT SUPPORTED IN SNOWFLAKE BUT REFERENCES TO THIS CUSTOM TYPE WERE CHANGED TO VARIANT ***/!!!
CREATE TYPE type1 AS OBJECT (
  attribute1 VARCHAR2(20),
  attribute2 NUMBER
)
;

!!!RESOLVE EWI!!! /*** SSC-EWI-0056 - CUSTOM TYPES ARE NOT SUPPORTED IN SNOWFLAKE BUT REFERENCES TO THIS CUSTOM TYPE WERE CHANGED TO VARIANT ***/!!!
CREATE TYPE type2 AS OBJECT (
  property1 type1,
  property2 DATE
)
;

CREATE OR REPLACE TABLE my_table (
  id NUMBER(38, 18) /*** SSC-FDM-0006 - NUMBER TYPE COLUMN MAY NOT BEHAVE SIMILARLY IN SNOWFLAKE. ***/ PRIMARY KEY,
  column1 VARIANT !!!RESOLVE EWI!!! /*** SSC-EWI-0062 - CUSTOM TYPE 'type2' USAGE CHANGED TO VARIANT ***/!!!
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
;

CREATE OR REPLACE VIEW my_table_view
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
AS
SELECT
  id,
  column1:property1:attribute1 :: VARCHAR AS attribute1,
  column1:property1:attribute2 :: NUMBER AS attribute2,
  column1:property2 :: DATE AS property2
FROM
  my_table;

INSERT INTO my_table
VALUES (
  1, type2(type1('value1', 100) !!!RESOLVE EWI!!! /*** SSC-EWI-0073 - PENDING FUNCTIONAL EQUIVALENCE REVIEW FOR 'type1' NODE ***/!!!, CURRENT_TIMESTAMP()) !!!RESOLVE EWI!!! /*** SSC-EWI-0073 - PENDING FUNCTIONAL EQUIVALENCE REVIEW FOR 'type2' NODE ***/!!!
);

SELECT column1.property1.attribute1,
  column1.property2
FROM
  my_table;
```

#### Best Practices

* The code can be manually fixed by changing the ‘.’ accessor for the ‘:’ wherever a type column is being accessed.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0087

Ordering of the Outer Joins failed

### Severity

Low

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

This issue happens when an error occurred while reordering the new ANSI JOIN clauses in a query that previously had outer joins with the (+) operator. A query with a cycle of tables joining each other in the WHERE clause can provoke this issue.

When this EWI is present, the JOIN clauses may not work properly due to their order.

#### Example Code

##### Input Code Oracle

```sql
 SELECT
l.location_id, l.state_province,
r.region_id, r.region_name,
c.country_id, c.country_name
FROM
hr.countries c,  hr.regions r,  hr.locations l, hr.departments d WHERE
l.location_id (+) = c.region_id AND
c.region_id (+) = r.region_id AND
r.region_id (+) = c.region_id AND
l.location_id (+) = d.location_id;
```

##### Generated Code

```sql
 SELECT
l.location_id, l.state_province,
r.region_id, r.region_name,
c.country_id, c.country_name
FROM
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0087 - ORDERING THE OUTER JOINS FAILED. QUERY MAY NOT BEHAVE CORRECTLY ***/!!!
hr.departments d
LEFT OUTER JOIN
hr.locations l
ON
l.location_id = c.region_id
AND
l.location_id = d.location_id
LEFT OUTER JOIN
hr.countries c
ON
c.region_id = r.region_id
LEFT OUTER JOIN
hr.regions r
ON
r.region_id = c.region_id;
```

* Make sure the query is valid and does not have tables that are being joined to each other.
* If the issue still occurs, try qualifying the name of each column in the WHERE clause with the name of the table.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0089

REGEXP_LIKE_UDF match parameter may not behave correctly

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-OR0044](../functional-difference/oracleFDM.md) documentation.

### Severity

Low

### Description

This warning appears when the Oracle `REGEXP_LIKE`condition comes with the third parameter (match parameter)*.* The reason to add the warning is that the `REGEXP_LIKE_UDF`used to replace the `REGEXP_LIKE`does not recognize all the characters used by the match parameter, so the result of the query in Snowflake may not be equivalent to Oracle.

#### Example Code

##### Input Code Oracle

```sql
 SELECT last_name
FROM hr.employees
WHERE REGEXP_LIKE (last_name, '([aeiou])\1', 'i')
ORDER BY last_name;
```

##### Generated Code

```sql
 SELECT last_name
FROM
hr.employees
WHERE
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0089 - REGEXP_LIKE_UDF MATCH PARAMETER MAY HAVE SOME FUNCTIONAL DIFFERENCES COMPARED TO ORACLE. ***/!!!
PUBLIC.REGEXP_LIKE_UDF(last_name, '([aeiou])\\1', 'i')
ORDER BY last_name;
```

* When the `REGEXP_LIKE` condition includes characters that are not supported by the user-defined function, you can change the regular
  expression to simulate the behavior of the missing character in the match parameter. For more information about unsupported characters,
  see [REGEXP_LIKE_UDF](../../../../translation-references/oracle/functions/README.md).
* For additional support, contact Snowflake at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com).

## SSC-EWI-OR0090

Non-Ansi Outer Join has an invalid Between predicate

### Severity

Medium

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

This issue happens when there is an OUTER JOIN with the (+) operator inside a BETWEEN clause that cannot be executed in Snowflake. This generally happens when multiple tables are used in the interval of the BETWEEN clause.

#### Example Code

##### Input Code Oracle

```sql
 SELECT
*
FROM
hr.countries c, hr.regions r,  hr.locations l WHERE
l.location_id  BETWEEN r.region_id(+) AND c.region_id(+);
```

##### Generated Code

```sql
 SELECT
*
FROM
hr.countries c,
hr.regions r,
hr.locations l WHERE
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0090 - INVALID NON-ANSI OUTER JOIN BETWEEN PREDICATE CASE FOR SNOWFLAKE. ***/!!!
l.location_id  BETWEEN r.region_id(+) AND c.region_id(+);
```

#### Best Practices

* Manually change the Outer Join to ANSI syntax.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0092

NUMBER datatype negative scale was removed from output

### Severity

Low

### Description

This issue happens when a NUMBER with a negative scale is being used to apply rounding to the NUMBER. Snowflake does not support this feature, and this message is used to indicate that the Scale was removed.

#### Example Code

##### Input Code Oracle

##### Queries

```sql
 CREATE TABLE number_table
(
 col1 NUMBER(38),
 col2 NUMBER(38, -1),
 col3 NUMBER(*, -2)
);

INSERT INTO number_table(col1, col2, col3) VALUES (555, 555, 555);

SELECT * FROM number_table;
```

##### Result

```none
COL1|COL2|COL3|
----+----+----+
 555| 560| 600|
```

##### Generated Code

##### Queries

```sql
 CREATE OR REPLACE TABLE number_table
 (
  col1 NUMBER(38) /*** SSC-FDM-0006 - NUMBER TYPE COLUMN MAY NOT BEHAVE SIMILARLY IN SNOWFLAKE. ***/,
  col2 NUMBER(38) !!!RESOLVE EWI!!! /*** SSC-EWI-OR0092 - NUMBER DATATYPE NEGATIVE SCALE WAS REMOVED FROM OUTPUT ***/!!! /*** SSC-FDM-0006 - NUMBER TYPE COLUMN MAY NOT BEHAVE SIMILARLY IN SNOWFLAKE. ***/,
  col3 NUMBER(38) !!!RESOLVE EWI!!! /*** SSC-EWI-OR0092 - NUMBER DATATYPE NEGATIVE SCALE WAS REMOVED FROM OUTPUT ***/!!! /*** SSC-FDM-0006 - NUMBER TYPE COLUMN MAY NOT BEHAVE SIMILARLY IN SNOWFLAKE. ***/
 )
 COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
 ;

 INSERT INTO number_table(col1, col2, col3) VALUES (555, 555, 555);

 SELECT * FROM
 number_table;
```

##### Result

```sql
 |COL1|COL2|COL3|
|----|----|----|
|555 |555 |555 |
```

#### Best Practices

* No end-user action is required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0095

Operation Between Interval Type and Date Type not Supported

### Severity

Low

### Description

`INTERVAL YEAR TO MONTH` and `INTERVAL DAY TO SECOND` are not a supported data type, they are transformed to `VARCHAR(20)`. Therefore all arithmetic operations between **Date Types** and the original **Interval Type Columns** are not supported.

Furthermore, operations between an Interval Type and Date Type (in this order) are not supported in Snowflake; and these operations use this EWI as well.

#### Example Code

##### Input Code

```sql
 CREATE TABLE table_with_intervals
(
    date_col DATE,
    time_col TIMESTAMP,
    intervalYearToMonth_col INTERVAL YEAR TO MONTH,
    intervalDayToSecond_col INTERVAL DAY TO SECOND
);

-- Date + Interval Y to M
SELECT date_col + intervalYearToMonth_col FROM table_with_intervals;

-- Date - Interval D to S
SELECT date_col - intervalDayToSecond_col FROM table_with_intervals;

-- Timestamp + Interval D to S
SELECT time_col + intervalDayToSecond_col FROM table_with_intervals;

-- Timestamp - Interval Y to M
SELECT time_col - intervalYearToMonth_col FROM table_with_intervals;
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE table_with_intervals
    (
        date_col TIMESTAMP /*** SSC-FDM-OR0042 - DATE TYPE COLUMN HAS A DIFFERENT BEHAVIOR IN SNOWFLAKE. ***/,
        time_col TIMESTAMP(6),
        intervalYearToMonth_col VARCHAR(20) !!!RESOLVE EWI!!! /*** SSC-EWI-0036 - INTERVAL YEAR TO MONTH DATA TYPE CONVERTED TO VARCHAR ***/!!!,
        intervalDayToSecond_col VARCHAR(20) !!!RESOLVE EWI!!! /*** SSC-EWI-0036 - INTERVAL DAY TO SECOND DATA TYPE CONVERTED TO VARCHAR ***/!!!
    )
    COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
    ;

    -- Date + Interval Y to M
    SELECT
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0095 - OPERATION BETWEEN INTERVAL TYPE AND DATE TYPE NOT SUPPORTED ***/!!! date_col + intervalYearToMonth_col FROM
    table_with_intervals;

    -- Date - Interval D to S
SELECT
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0095 - OPERATION BETWEEN INTERVAL TYPE AND DATE TYPE NOT SUPPORTED ***/!!! date_col - intervalDayToSecond_col FROM
    table_with_intervals;

    -- Timestamp + Interval D to S
SELECT
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0095 - OPERATION BETWEEN INTERVAL TYPE AND DATE TYPE NOT SUPPORTED ***/!!! time_col + intervalDayToSecond_col FROM
    table_with_intervals;

    -- Timestamp - Interval Y to M
SELECT
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0095 - OPERATION BETWEEN INTERVAL TYPE AND DATE TYPE NOT SUPPORTED ***/!!! time_col - intervalYearToMonth_col FROM
    table_with_intervals;
```

#### Best Practices

* Implement the UDF to simulate the Oracle behavior.
* Extract the already transformed value that was stored in the column during migration, and use it as a Snowflake [**Interval Constant**](https://docs.snowflake.com/en/sql-reference/data-types-datetime.html#interval-constants) when possible.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

####

## SSC-EWI-OR0097

Procedure Properties are Not Supported in Snowflake Procedures

### Severity

Low

### Description

Oracle `CREATE PROCEDURE` additional properties are not required and have no equivalent by Snowflake `CREATE PROCEDURE`.

#### Example Code

##### Input Code Oracle

```sql
 CREATE OR REPLACE PROCEDURE PROC01
DEFAULT COLLATION USING_NLS_COMP
AUTHID CURRENT_USER
ACCESSIBLE BY (PROCEDURE PROC03)
AS
BEGIN
    NULL;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE PROC01 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
EXECUTE AS CALLER
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0097 - PROCEDURE PROPERTIES ARE NOT SUPPORTED IN SNOWFLAKE PROCEDURES ***/!!!
AS
$$
    BEGIN
        NULL;
    END;
$$;
```

#### Best Practices

* No end-user action is required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0099

The exception code exceeds the Snowflake Scripting limit

### Severity

Low

### Description

This EWI appears when an exception declaration error code exceeds the Snowflake Scripting exception number limits. The number must be an integer between -20000 and -20999.

#### Example Code

##### Input Code

```sql
 CREATE OR REPLACE PROCEDURE procedure_exception
IS
my_exception EXCEPTION;
PRAGMA EXCEPTION_INIT ( my_exception, -19000 );
BEGIN
    NULL;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE procedure_exception ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        !!!RESOLVE EWI!!! /*** SSC-EWI-OR0099 - EXCEPTION CODE NUMBER EXCEEDS SNOWFLAKE SCRIPTING LIMITS ***/!!!
        my_exception EXCEPTION;
        !!!RESOLVE EWI!!! /*** SSC-EWI-OR0051 - PRAGMA EXCEPTION_INIT IS NOT SUPPORTED ***/!!!
        PRAGMA EXCEPTION_INIT ( my_exception, -19000 );
    BEGIN
        NULL;
    END;
$$;
```

#### Best Practices

* Check if the exception code is between the limits allowed by Snowflake Scripting, if not change it for another exception number available.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0100

For Loop With Multiple Conditions Is Currently Not Supported By Snowflake Scripting. Only First Condition Is Used

### Severity

Low

### Description

Oracle allows multiple conditions in a single `FOR LOOP` however, Snowflake Scripting only allows one condition per `FOR LOOP`. Only the first condition is migrated and the others are ignored during transformation.

#### Example Code

##### Input Code

```sql
 CREATE OR REPLACE PROCEDURE P3
AS
BEGIN
FOR i IN REVERSE 1..3,
REVERSE i+5..i+7
LOOP
    NULL;
END LOOP;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE P3 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
EXECUTE AS CALLER
AS
$$
    BEGIN
        --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **
        !!!RESOLVE EWI!!! /*** SSC-EWI-OR0100 - FOR LOOP WITH MULTIPLE CONDITIONS IS CURRENTLY NOT SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!
        FOR i IN REVERSE 1 TO 3
        --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **
        LOOP
            NULL;
        END LOOP;
    END;
$$;
```

#### Best Practices

* Separate the `FOR LOOP` into different loops or rewrite the condition.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0101

Specific For Loop Clause Is Currently Not Supported By Snowflake Scripting

### Severity

Low

### Description

Oracle allows additional clauses to the `FOR LOOP` condition. Like the **BY,** **WHILE,** and **WHEN** clauses. Both **WHILE** and **WHEN** clauses allow for an extra boolean expression as a condition. While the **BY** clause allows a stepped increment in the iteration. These additional clauses are not supported in Snowflake Scripting and are ignored during transformation.

#### Example Code

##### Input Code Oracle

```sql
 CREATE OR REPLACE PROCEDURE P2
AS
BEGIN
FOR i IN 1..10 WHILE i <= 5 LOOP
    NULL;
END LOOP;

FOR i IN 5..15 BY 5 LOOP
    NULL;
END LOOP;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE P2 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
EXECUTE AS CALLER
AS
$$
    BEGIN
        --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **
        !!!RESOLVE EWI!!! /*** SSC-EWI-OR0101 - FOR LOOP WITH "WHILE" CLAUSE IS CURRENTLY NOT SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!
        FOR i IN 1 TO 10
                         --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **
                         LOOP
                                NULL;
END LOOP;
                         !!!RESOLVE EWI!!! /*** SSC-EWI-OR0101 - FOR LOOP WITH "BY" CLAUSE IS CURRENTLY NOT SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!
                         --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **
                         FOR i IN 5 TO 15
                                          --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **
                                          LOOP
                                   NULL;
END LOOP;
    END;
$$;
```

#### Best Practices

* Separate the `FOR LOOP` into different loops or rewrite the condition.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0103

For Loop Format Is Currently Not Supported By Snowflake Scripting

### Severity

High

### Description

Oracle allows different types of conditions for a `FOR LOOP`. It supports boolean expressions, collections, records… However, Snowflake scripting only supports `FOR LOOP` with defined integers as bounds. All other formats are marked as not supported and require additional manual effort to be transformed.

[Oracle iteration control clauses](https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/iterator.html#GUID-BD211E6F-8B4A-494A-AECF-AC26A241FF98) that are not supported in Snowflake `FOR LOOP`:

* `single_expression_control`
* `values_of_control`
* `indices_of_control`
* `pairs_of_control`

> **Danger:**
>
> `cursor_iteration_control` is currently marked as not supported. Removing parenthesis from the expression should transform it as a CURSOR FOR LOOP.
>
> **Original:**
>
> `FOR i IN (cursor_variable) LOOP NULL; END LOOP;`
>
> **Should be changed to:**
>
> `FOR i IN cursor_variable LOOP NULL; END LOOP;`

#### Example Code

##### Input Code Oracle

```sql
 CREATE OR REPLACE PROCEDURE P3
AS
TYPE values_aat IS TABLE OF PLS_INTEGER INDEX BY PLS_INTEGER;
l_employee_values   values_aat;
BEGIN
FOR power IN REPEAT power*2 WHILE power <= 64 LOOP
    NULL;
END LOOP;

FOR i IN VALUES OF l_employee_values LOOP
    NULL;
END LOOP;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE P3 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
EXECUTE AS CALLER
AS
$$
    DECLARE
--        !!!RESOLVE EWI!!! /*** SSC-EWI-0058 - FUNCTIONALITY FOR 'PL COLLECTION TYPE DEFINITION' IS NOT CURRENTLY SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!
--        TYPE values_aat IS TABLE OF PLS_INTEGER INDEX BY PLS_INTEGER;
        l_employee_values VARIANT !!!RESOLVE EWI!!! /*** SSC-EWI-0062 - CUSTOM TYPE 'values_aat' USAGE CHANGED TO VARIANT ***/!!!;
    BEGIN
        !!!RESOLVE EWI!!! /*** SSC-EWI-OR0103 - FOR LOOP FORMAT IS CURRENTLY NOT SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!
        --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **
        !!!RESOLVE EWI!!! /*** SSC-EWI-OR0101 - FOR LOOP WITH "WHILE" CLAUSE IS CURRENTLY NOT SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!
        FOR power IN REPEAT power*2 WHILE power <= 64
                                                      --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **
                                                      LOOP
            NULL;
        END LOOP;
        !!!RESOLVE EWI!!! /*** SSC-EWI-OR0103 - FOR LOOP FORMAT IS CURRENTLY NOT SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!
        --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **

        FOR i IN VALUES OF :l_employee_values
                                              --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **
                                              LOOP
            NULL;
        END LOOP;
    END;
$$;
```

#### Best Practices

* Rewrite the `FOR LOOP` condition or use a different kind of `LOOP` to simulate the behavior.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0104

Unusable collection variable

### Severity

High

### Description

Oracle collections are not currently supported by SnowConvert AI, all the collection types variables and their usages will be commented out.

> **Note:**
>
> Generate Procedures and Macros using JavaScript as the target language adding the following flag `-t JavaScript` or `--PLTargetLanguage JavaScript`

#### Example Code

##### Input Code Oracle

```sql
 -- Additional Params: -t JavaScript
CREATE OR REPLACE PROCEDURE collection_variable_sample_proc
IS
    TYPE POPULATION IS TABLE OF NUMBER INDEX BY VARCHAR2(64); --Associative array
    city_population POPULATION := POPULATION();
    i  VARCHAR2(64);
BEGIN
 city_population('Smallville')  := 2000;
    city_population('Midland')     := 750000;

    i := city_population.FIRST;
    i := city_population.NEXT(1);
END;
```

##### Output Cod

```sql
 CREATE OR REPLACE PROCEDURE collection_variable_sample_proc ()
RETURNS STRING
LANGUAGE JAVASCRIPT
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "12/16/2024",  "domain": "test" }}'
EXECUTE AS CALLER
AS
$$
 // SnowConvert AI Helpers Code section is omitted.

 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0072 - PROCEDURAL MEMBER TYPE DEFINITION NOT SUPPORTED. ***/!!!
 /*     TYPE POPULATION IS TABLE OF NUMBER INDEX BY VARCHAR2(64) */
 ;
 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0104 - UNUSABLE VARIABLE, ITS TYPE WAS NOT TRANSFORMED ***/!!!
 /*     city_population POPULATION := POPULATION() */
 ;
 let I;
 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0104 - UNUSABLE VARIABLE, ITS TYPE WAS NOT TRANSFORMED ***/!!!
 /*  city_population('Smallville')  := 2000 */
 ;
 !!!RESOLVE EWI!!! /*** SSC-EWI-OR0104 - UNUSABLE VARIABLE, ITS TYPE WAS NOT TRANSFORMED ***/!!!
 /*     city_population('Midland')     := 750000 */
 ;
 I =
  !!!RESOLVE EWI!!! /*** SSC-EWI-OR0104 - UNUSABLE VARIABLE, ITS TYPE WAS NOT TRANSFORMED ***/!!!
  /*city_population.FIRST*/
  null;
 I =
  !!!RESOLVE EWI!!! /*** SSC-EWI-OR0104 - UNUSABLE VARIABLE, ITS TYPE WAS NOT TRANSFORMED ***/!!!
  /*city_population.NEXT(1)*/
  null;
$$;
```

#### Best Practices

* No end-user action is required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0105

Additional work is needed for BFILE column usage. BUILD_STAGE_URL function is a recommended workaround

### Severity

Low

### Description

The transformation for `BFILE` datatype is `VARCHAR`. However, the translation for the Oracle built-in functions used to interact with BFILE types is currently not supported. The column is migrated to a `VARCHAR` to store the file path and name. For more information, see the `BFILENAME_UDF` documentation.

> **Note:**
>
> The `BUILD_STAGE_FILE_URL` function is a recommended workaround to work with files in Snowflake. It returns a link to the specified file stored in a [stage](https://docs.snowflake.com/en/sql-reference/sql/create-stage.html#create-stage). See the [BUILD_STAGE_FILE_URL function documentation](https://docs.snowflake.com/en/sql-reference/functions/build_stage_file_url.html#build-stage-file-url).

#### Example Code

##### Input Code Oracle

```sql
 CREATE TABLE bfiletable ( bfile_column BFILE );

INSERT INTO bfiletable VALUES ( BFILENAME('mydirectory', 'myfile.png') );
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE bfiletable ( bfile_column
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0105 - ADDITIONAL WORK IS NEEDED FOR BFILE COLUMN USAGE. BUILD_STAGE_FILE_URL FUNCTION IS A RECOMMENDED WORKAROUND ***/!!!
VARCHAR
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"oracle"}}'
;

INSERT INTO bfiletable
VALUES (PUBLIC.BFILENAME_UDF('mydirectory', 'myfile.png') );
```

#### Best Practices

* Use the `BUILD_STAGE_FILE_URL` and the other [file functions](https://docs.snowflake.com/en/sql-reference/functions-file.html#file-functions) to handle files.

##### Snowflake Query

```sql
 CREATE OR REPLACE TABLE bfiletable ( bfile_column
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0105 - ADDITIONAL WORK IS NEEDED FOR BFILE COLUMN USAGE. BUILD_STAGE_FILE_URL FUNCTION IS A RECOMMENDED WORKAROUND ***/!!!
VARCHAR
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
;

INSERT INTO bfiletable
VALUES (PUBLIC.BFILENAME_UDF('mydirectory', 'myfile.png') );
```

##### Result

```none
URL                                                                                                   |
------------------------------------------------------------------------------------------------------+
https://thecompany.snowflakecomputing.com/api/files/CODETEST/PUBLIC/MY_STAGE/%2Fmydirectory%2Fmyfile.jpg|
```

> **Note:**
>
> This function works with different cloud storage options, but for information regarding using local files with stages, check this [documentation](https://docs.snowflake.com/en/user-guide/data-load-local-file-system-stage.html#staging-data-files-from-a-local-file-system).

* Change the data type to a supported type.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0108

The Following Assignment Statement is Not Supported by Snowflake Scripting

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Medium

### Description

Some Oracle variable types do not have a direct translation in Snowflake. Currently, transformation for cursor, collection, record, and user-defined type variables; as well as placeholders, objects, and output parameters are not supported by Snow Scripting.

Changing these variables to Snowflake [semi-structured data types](https://docs.snowflake.com/en/sql-reference/data-types-semistructured.html#semi-structured-data-types) could help as a workaround in some scenarios.

#### Example Code

##### Input Code

```sql
 CREATE OR REPLACE PROCEDURE pinvalidassign(out_parameter   IN OUT NUMBER)
AS
record_variable       employees%ROWTYPE;

TYPE cursor_type IS REF CURSOR;
cursor1   cursor_type;
cursor2   SYS_REFCURSOR;

TYPE collection_type IS TABLE OF NUMBER INDEX BY VARCHAR(64);
collection_variable     collection_type;

BEGIN
--Record Example
  record_variable.last_name := 'Ortiz';

--Cursor Example
  cursor1 := cursor2;

--Collection
  collection_variable('Test') := 5;

--Out Parameter
  out_parameter := 123;
END;
```

##### Generated Code

```sql
--** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "employees" **
CREATE OR REPLACE PROCEDURE pinvalidassign (out_parameter OUT NUMBER(38, 18))
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "07/16/2025",  "domain": "no-domain-provided" }}'
EXECUTE AS CALLER
AS
$$
  DECLARE
    record_variable OBJECT !!!RESOLVE EWI!!! /*** SSC-EWI-0036 - ROWTYPE DATA TYPE CONVERTED TO OBJECT ***/!!! := OBJECT_CONSTRUCT();
--    !!!RESOLVE EWI!!! /*** SSC-EWI-0058 - FUNCTIONALITY FOR 'PL REF CURSOR TYPE DEFINITION' IS NOT CURRENTLY SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!

--    TYPE cursor_type IS REF CURSOR;
    cursor1_res RESULTSET;
    cursor2_res RESULTSET;
--    !!!RESOLVE EWI!!! /*** SSC-EWI-0058 - FUNCTIONALITY FOR 'PL COLLECTION TYPE DEFINITION' IS NOT CURRENTLY SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!

--    TYPE collection_type IS TABLE OF NUMBER INDEX BY VARCHAR(64);
    collection_variable VARIANT !!!RESOLVE EWI!!! /*** SSC-EWI-0062 - CUSTOM TYPE 'collection_type' USAGE CHANGED TO VARIANT ***/!!!;
  BEGIN
    --Record Example
    record_variable := OBJECT_INSERT(record_variable, 'LAST_NAME', 'Ortiz', true);

    --Cursor Example
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0108 - THE FOLLOWING ASSIGNMENT STATEMENT IS NOT SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!
      cursor1 := :cursor2;

    --Collection
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0108 - THE FOLLOWING ASSIGNMENT STATEMENT IS NOT SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!
      collection_variable('Test') := 5;
    --Out Parameter
    out_parameter := 123;
  END;
$$;
```

#### Best Practices

* Change the variable data type or try to simulate the behavior using Snowflake [semi-structured data types](https://docs.snowflake.com/en/sql-reference/data-types-semistructured.html#semi-structured-data-types).
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0109

Expressions as arguments of Using Clause are not supported by Snowflake Scripting

### Severity

Medium

### Description

Oracle supports using expressions as arguments to any USING Clause for the EXECUTE IMMEDIATE statements. This functionality is not supported by Snowflake Scripting.

Snowflake Scripting does support variable expressions, and this it is possible to replace the expression by manually assigning it to a variable (see example below).

#### Example Code

##### Input Code

```sql
 CREATE OR REPLACE PROCEDURE expression_arguments
IS
  immediate_input INTEGER := 0;
BEGIN
  EXECUTE IMMEDIATE 'INSERT INTO immediate_table VALUES (:value)' USING immediate_input+1;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE expression_arguments ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
EXECUTE AS CALLER
AS
$$
  DECLARE
    immediate_input INTEGER := 0;
  BEGIN
    !!!RESOLVE EWI!!! /*** SSC-EWI-0030 - THE STATEMENT BELOW HAS USAGES OF DYNAMIC SQL. ***/!!!
    EXECUTE IMMEDIATE 'INSERT INTO immediate_table
VALUES (?)' USING (
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0109 - EXPRESSIONS AS ARGUMENTS OF USING CLAUSE IS NOT SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!
    :immediate_input +1);
  END;
$$;
```

##### Manually migrated Execute Immediate procedure

Replacing this procedure with the one above will solve the compilation error, and yield the same results as Oracle.

```sql
 CREATE OR REPLACE PROCEDURE PUBLIC.expression_arguments ()
RETURNS VARCHAR
LANGUAGE SQL
EXECUTE AS CALLER
AS
$$
   DECLARE
      immediate_input INTEGER := 0;
      using_argument_variable INTEGER;
   BEGIN
      using_argument_variable := immediate_input+1;
      EXECUTE IMMEDIATE 'INSERT INTO PUBLIC.immediate_table VALUES (?)' USING (using_argument_variable );
   END;
$$;
```

#### Best Practices

* Procedures can be manually migrated by adding a variable and then assigning the expression to said variable.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0110

For Update Clause is not supported in Snowflake

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

High

### Description

There is no equivalent for `FOR UPDATE` clause in Snow Scripting so an EWI is added and the clause is commented out

#### Example Code

##### Input Code

```sql
 CREATE OR REPLACE PROCEDURE for_update_clause
AS
    update_record f_employee%rowtype;
    CURSOR c1 IS SELECT * FROM f_employee FOR UPDATE OF employee_number nowait;
BEGIN
    FOR CREC IN C1 LOOP
 UPDATE f_employee SET employee_number = employee_number + 1000 WHERE CURRENT OF c1;
 IF crec.id = 2 THEN
     DELETE FROM f_employee WHERE CURRENT OF c1;
     EXIT;
 END IF;
    END LOOP;
END;
```

##### Generated Code

```sql
 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "f_employee" **
CREATE OR REPLACE PROCEDURE for_update_clause ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
EXECUTE AS CALLER
AS
$$
 DECLARE
  update_record OBJECT !!!RESOLVE EWI!!! /*** SSC-EWI-0036 - ROWTYPE DATA TYPE CONVERTED TO OBJECT ***/!!! := OBJECT_CONSTRUCT();
  --** SSC-PRF-0009 - PERFORMANCE REVIEW - CURSOR USAGE **
  c1 CURSOR
  FOR
   SELECT * FROM
    f_employee
   !!!RESOLVE EWI!!! /*** SSC-EWI-OR0110 - FOR UPDATE CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
   FOR UPDATE OF employee_number nowait;
 BEGIN
  OPEN C1;
  --** SSC-PRF-0004 - THIS STATEMENT HAS USAGES OF CURSOR FOR LOOP **
  FOR CREC IN C1 DO
   !!!RESOLVE EWI!!! /*** SSC-EWI-OR0136 - CURRENT OF CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
   UPDATE f_employee
    SET employee_number =
                          !!!RESOLVE EWI!!! /*** SSC-EWI-OR0036 - TYPES RESOLUTION ISSUES, ARITHMETIC OPERATION '+' MAY NOT BEHAVE CORRECTLY BETWEEN unknown AND Number ***/!!! employee_number + 1000 WHERE CURRENT OF c1;
   IF (crec.id = 2) THEN
--    !!!RESOLVE EWI!!! /*** SSC-EWI-0058 - FUNCTIONALITY FOR 'CURRENT OF' IS NOT CURRENTLY SUPPORTED BY SNOWFLAKE SCRIPTING ***/!!!
--    DELETE FROM
--     f_employee
--    WHERE CURRENT OF c1
                       ;
    EXIT;
   END IF;
  END FOR;
  CLOSE C1;
 END;
$$;
```

#### Best Practices

* Handle the column update in the `UPDATE/DELETE` query for more details check SSC-EWI-OR0136.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0116

Operations between Intervals are not supported

### Severity

Medium

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

This error is added when there is an arithmetical operation whose operands are only intervals, this kind of operation is not supported by Snowflake.

#### Example Code

##### Input Code

```sql
 SELECT INTERVAL '1-1' YEAR(2) TO MONTH + INTERVAL '1-1' YEAR(2) + INTERVAL '1-1' YEAR(2) TO MONTH FROM dual;

SELECT INTERVALCOLUMN + INTERVAL '1-1' YEAR(2) TO MONTH FROM INTERVALTABLE;
```

##### Generated Code

```sql
 SELECT
--INTERVAL '1-1 year' + INTERVAL '1y, 1mm' + INTERVAL '1y, 1mm'
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0116 - OPERATIONS BETWEEN INTERVALS ARE NOT SUPPORTED BY SNOWFLAKE ***/!!!
null
FROM dual;

SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0036 - TYPES RESOLUTION ISSUES, ARITHMETIC OPERATION '+' MAY NOT BEHAVE CORRECTLY BETWEEN Unknown AND Interval ***/!!! INTERVALCOLUMN + INTERVAL '1y, 1mm'
FROM
INTERVALTABLE;
```

#### Best Practices

* Depending on where the operation is located, it could be relocated and made valid by adding dates or timestamps.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0118

Built-In Views/Tables are not supported by Snowflake

### Severity

Medium

### Description

Oracle has a [set of built-in views and tables](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/static-data-dictionary-views-1.html#GUID-41B62782-83FA-4066-8C56-0D0B66CC0EC7), that are not present in Snowflake, SnowConvert AI adds an error message to queries and statements that use these elements.

#### Example Code

##### Input Code

```sql
 SELECT * FROM ALL_COL_COMMENTS;
SELECT * FROM (SELECT * FROM ALL_COL_COMMENTS);
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0118 - TRANSLATION FOR ORACLE BUILT-IN TABLE/VIEW 'ALL_COL_COMMENTS' IS NOT CURRENTLY SUPPORTED. ***/!!!
 * FROM
 ALL_COL_COMMENTS;

SELECT * FROM (SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0118 - TRANSLATION FOR ORACLE BUILT-IN TABLE/VIEW 'ALL_COL_COMMENTS' IS NOT CURRENTLY SUPPORTED. ***/!!! * FROM
ALL_COL_COMMENTS);
```

#### Best Practices

* Some information provided by Oracle Built-In views, can be found in Snowflake [Information Schema](https://docs.snowflake.com/en/sql-reference/info-schema.html#snowflake-information-schema) or using [SHOW](https://docs.snowflake.com/en/sql-reference/sql/show.html) command.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0121

Using DBMS_LOB.SUBSTR built-in package with a BFILE column is not supported in Snowflake

### Severity

Medium

### Description

Oracle BFILE columns are migrated to VARCHAR in Snowflake. The file name is stored as a string in the new column. Therefore, using a SUBSTR function, in Snowflake, on the migrated column will return a substring of the file name. While Oracle DBMS_LOB.SUBSTR will return a substring of the file content. For more information review [BFILE data type](../../../../translation-references/oracle/basic-elements-of-oracle-sql/data-types/oracle-built-in-data-types.md).

#### Example Code

##### Input Code

```sql
 CREATE TABLE table1
(
    bfile_column BFILE
)
SELECT
DBMS_LOB.SUBSTR(bfile_column, 15, 1)
FROM table1;
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE table1
    (
        bfile_column
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0105 - ADDITIONAL WORK IS NEEDED FOR BFILE COLUMN USAGE. BUILD_STAGE_FILE_URL FUNCTION IS A RECOMMENDED WORKAROUND ***/!!!
    VARCHAR
    )
    COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
    ;
    SELECT
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0121 - USING DBMS_LOB.SUBSTR ON BFILE SOURCE COLUMN IS NOT SUPPORTED ON SNOWFLAKE ***/!!!
    SUBSTR(bfile_column, 1, 15)
    FROM
    table1;
```

#### Best Practices

* To handle files with Snowflake, see the [UTL_FILE handling documentation](../../../../translation-references/oracle/built-in-packages.md).
* For additional support, contact SnowConvert at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com).

## SSC-EWI-OR0123

Database Link connections not supported

### Severity

Medium

### Description

A database link connection reference was removed from the object name because the database links and its references are not supported in Snowflake. The only part that is kept is the name before the `@` character.

#### Example Code

##### Input Code

```sql
 -- Creation of the database link
CREATE DATABASE LINK mylink
    CONNECT TO user1 IDENTIFIED BY password1
    USING 'connection_str';

-- Statements that use the database link we created
SELECT * FROM employees@mylink;

INSERT INTO employees@mylink
    (employee_id, last_name, email, hire_date, job_id)
    VALUES (999, 'Claus', 'sclaus@oracle.com', SYSDATE, 'SH_CLERK');

UPDATE employees@mylink SET min_salary = 3000
    WHERE job_id = 'SH_CLERK';

DELETE FROM employees@mylink
    WHERE employee_id = 999;
```

##### Generated Code

```sql
 ---- Creation of the database link
----** SSC-OOS - OUT OF SCOPE CODE UNIT. CREATE DATABASE LINK IS OUT OF TRANSLATION SCOPE. **
--CREATE DATABASE LINK mylink
--    CONNECT TO user1 IDENTIFIED BY password1
--    USING 'connection_str'

    -- Statements that use the database link we created
SELECT * FROM
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0123 - DBLINK CONNECTIONS NOT SUPPORTED [ DBLINK : mylink | USER: user1/password1 | CONNECTION: 'connection_str' ] ***/!!!
    employees;

INSERT INTO
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0123 - DBLINK CONNECTIONS NOT SUPPORTED [ DBLINK : mylink | USER: user1/password1 | CONNECTION: 'connection_str' ] ***/!!!
employees
    (employee_id, last_name, email, hire_date, job_id)
    VALUES (999, 'Claus', 'sclaus@oracle.com', CURRENT_TIMESTAMP(), 'SH_CLERK');

UPDATE
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0123 - DBLINK CONNECTIONS NOT SUPPORTED [ DBLINK : mylink | USER: user1/password1 | CONNECTION: 'connection_str' ] ***/!!!
employees
    SET min_salary = 3000
    WHERE job_id = 'SH_CLERK';

DELETE FROM
    !!!RESOLVE EWI!!! /*** SSC-EWI-OR0123 - DBLINK CONNECTIONS NOT SUPPORTED [ DBLINK : mylink | USER: user1/password1 | CONNECTION: 'connection_str' ] ***/!!!
    employees
    WHERE employee_id = 999;
```

#### Best Practices

* It is important to check that all DB Links have different names, if two DB Links share the same and the code is migrated multiple times, then the EWI can change de information based on what DB Link is processed first.
* Move the database objects from the database link reference into the same database instance that is being used in Snowflake.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0126

Unusable object because its built-in custom type is not supported

### Severity

Medium

### Description

This error appears to indicate whether an object with a built-in custom type is being used.

#### Example Code

##### Input Code

```sql
 CREATE OR REPLACE PROCEDURE proc01 is
   var1 DBMS_SQL.VARCHAR2_TABLE;
   var2 CTX_CLS.DOC_TAB;
BEGIN
   varX := var1.property;
   varY := var2(1);
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE proc01 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
EXECUTE AS CALLER
AS
$$
   DECLARE
      var1 VARIANT /*** SSC-FDM-0015 - REFERENCED CUSTOM TYPE 'DBMS_SQL.VARCHAR2_TABLE' IN QUERY NOT FOUND, USAGES MAY BE AFFECTED ***/;
      var2 VARIANT /*** SSC-FDM-0015 - REFERENCED CUSTOM TYPE 'CTX_CLS.DOC_TAB' IN QUERY NOT FOUND, USAGES MAY BE AFFECTED ***/;
   BEGIN
      varX := var1.property !!!RESOLVE EWI!!! /*** SSC-EWI-OR0126 - UNUSABLE OBJECT var1, BUILT-IN CUSTOM TYPES ARE NOT SUPPORTED ***/!!!;
      varY := var2(1) !!!RESOLVE EWI!!! /*** SSC-EWI-OR0126 - UNUSABLE OBJECT var2, BUILT-IN CUSTOM TYPES ARE NOT SUPPORTED ***/!!!;
   END;
$$;
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

### Related EWI

* [SSC-FDM-0015](../functional-difference/generalFDM.md): Data Type Not Recognized.

## SSC-EWI-OR0128

Boolean cursor attribute is not supported.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Low

### Description

This message is used to indicate that a boolean cursor attribute is not supported in SnowScript or that there is no transformation that emulates its functionality in SnowScript. The following table shows the boolean cursor attributes that can be emulated:

| Boolean Cursor Attribute | Status |
| --- | --- |
| `%FOUND` | Can be emulated |
| `%NOTFOUND` | Can be emulated |
| `%ISOPEN` | Not Supported |

#### Example Code

##### Input Code

```sql
 CREATE OR REPLACE PROCEDURE cursor_attributes_proc
IS
    is_open_attr BOOLEAN;
    found_attr BOOLEAN;
    my_record table1%ROWTYPE;
    CURSOR my_cursor IS SELECT * FROM table1;
BEGIN
    OPEN my_cursor;
    LOOP
        FETCH my_cursor INTO my_record;
        EXIT WHEN my_cursor%NOTFOUND;
        is_open_attr := my_cursor%ISOPEN;
        found_attr := my_cursor%FOUND;
    END LOOP;
    CLOSE my_cursor;
END;
```

##### Generated Code

```sql
 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "table1" **
CREATE OR REPLACE PROCEDURE cursor_attributes_proc ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        is_open_attr BOOLEAN;
        found_attr BOOLEAN;
        my_record OBJECT !!!RESOLVE EWI!!! /*** SSC-EWI-0036 - ROWTYPE DATA TYPE CONVERTED TO OBJECT ***/!!! := OBJECT_CONSTRUCT();
        --** SSC-PRF-0009 - PERFORMANCE REVIEW - CURSOR USAGE **
        my_cursor CURSOR
        FOR
            SELECT
                OBJECT_CONSTRUCT( *) sc_cursor_record FROM
                table1;
    BEGIN
        OPEN my_cursor;
        --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **
        LOOP
            --** SSC-PRF-0003 - FETCH INSIDE A LOOP IS CONSIDERED A COMPLEX PATTERN, THIS COULD DEGRADE SNOWFLAKE PERFORMANCE. **
            FETCH my_cursor INTO
                :my_record;
            IF (my_record IS NULL) THEN
                EXIT;
            END IF;
            is_open_attr := null /*my_cursor%ISOPEN*/!!!RESOLVE EWI!!! /*** SSC-EWI-OR0128 - BOOLEAN CURSOR ATTRIBUTE %ISOPEN IS NOT SUPPORTED IN SNOWFLAKE ***/!!!;
            found_attr := my_record IS NOT NULL;
        END LOOP;
    CLOSE my_cursor;
    END;
$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0129

TYPE attribute could not be resolved.

### Severity

Low

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

This warning appears when the `TYPE`attribute referenced item could not be resolved and the referencing item’s data type could not be obtained. So the `VARIANT`data type will be assigned instead.

#### Example Code

##### Input Code

```sql
 CREATE OR REPLACE PROCEDURE procedure01
IS
var1 table01.col1%TYPE;
BEGIN
NULL;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE procedure01 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
EXECUTE AS CALLER
AS
$$
DECLARE
var1 VARIANT !!!RESOLVE EWI!!! /*** SSC-EWI-OR0129 - TYPE ATTRIBUTE 'table01.col1%TYPE' COULD NOT BE RESOLVED, SO IT WAS TRANSFORMED TO VARIANT ***/!!!;
BEGIN
NULL;
END;
$$;
```

#### Best Practices

* Check for the referenced item data type and replace it manually in the referencing item TYPE attribute.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0133

Cursor variable has already been assigned

### Severity

Medium

### Description

When an `OPEN FOR` statement is converted, a cursor assignment with the same name as the cursor variable used in the input code is added along with other statements to emulate its functionality. Since it is possible to use multiple `OPEN FOR` statements with the same cursor variable, there will be multiple cursor assignments with the same name in the output code. Leaving the output code as it is will cause compilation errors when executed in Snowflake.

#### Example code

##### Input code

```sql
 CREATE OR REPLACE PROCEDURE open_for_procedure
AS
 query1 VARCHAR(200) := 'SELECT 123 FROM dual';
 query2 VARCHAR(200) := 'SELECT 456 FROM dual';
 my_cursor_variable SYS_REFCURSOR;
BEGIN
 OPEN my_cursor_variable FOR query1;
 OPEN my_cursor_variable FOR query2;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE open_for_procedure ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}'
EXECUTE AS CALLER
AS
$$
 DECLARE
  query1 VARCHAR(200) := 'SELECT 123 FROM dual';
  query2 VARCHAR(200) := 'SELECT 456 FROM dual';
  my_cursor_variable_res RESULTSET;
 BEGIN
  !!!RESOLVE EWI!!! /*** SSC-EWI-0030 - THE STATEMENT BELOW HAS USAGES OF DYNAMIC SQL. ***/!!!
  my_cursor_variable_res := (
   EXECUTE IMMEDIATE :query1
  );
  LET my_cursor_variable CURSOR
  FOR
   my_cursor_variable_res;
  OPEN my_cursor_variable;
  !!!RESOLVE EWI!!! /*** SSC-EWI-0030 - THE STATEMENT BELOW HAS USAGES OF DYNAMIC SQL. ***/!!!
  my_cursor_variable_res := (
   EXECUTE IMMEDIATE :query2
  );
  !!!RESOLVE EWI!!! /*** SSC-EWI-OR0133 - THE CURSOR VARIABLE NAMED 'my_cursor_variable' HAS ALREADY BEEN ASSIGNED IN ANOTHER CURSOR ***/!!!
  LET my_cursor_variable CURSOR
  FOR
   my_cursor_variable_res;
  OPEN my_cursor_variable;
 END;
$$;
```

### Related EWI

1. [SSC-EWI-0030](generalEWI.md): The statement below has usages of dynamic SQL.

#### Best Practices

* To solve the compilation errors of the output code the cursor assignments that have the SSC-EWI-OR0133 message should be renamed.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0135

Data Retention Period May Produce No Results

### Severity

Low

### Description

If a query is executed in Snowflake using time travel, it could return no results if the specified time is no longer in the range of the data retention period. We recommend to read more about [Snowflake’s Time Travel.](https://docs.snowflake.com/en/user-guide/data-time-travel)

#### Example code

##### Input code

```sql
 SELECT * FROM employees
AS OF TIMESTAMP
TO_TIMESTAMP('2023-09-27 07:00:00', 'YYYY-MM-DD HH:MI:SS')
WHERE last_name = 'SampleName';
```

##### Generated Code

```sql
 SELECT * FROM
employees
!!!RESOLVE EWI!!! /*** SSC-EWI-OR0135 - DATA RETENTION PERIOD MAY PRODUCE NO RESULTS ***/!!!
AT (TIMESTAMP =>
TO_TIMESTAMP('2023-09-27 07:00:00', 'YYYY-MM-DD HH:MI:SS'))
WHERE last_name = 'SampleName';
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0136

Current of clause is not supported in Snowflake

### Severity

Critical

### Description

Some statements like UPDATE and DELETE can use have a CURRENT OF clause inside the WHERE clause, this is not currently supported by Snowflake.

#### Example Code

##### Oracle

```sql
 CREATE OR REPLACE PROCEDURE proc_update_current_of
AS
  CURSOR C1
  IS
    SELECT * FROM F_EMPLOYEE FOR UPDATE OF SALARY nowait;
BEGIN
  FOR CREC IN C1
  LOOP
    UPDATE F_EMPLOYEE SET SALARY=SALARY+2000 WHERE CURRENT OF C1;
  END LOOP;
END;
```

##### Snowflake Scripting

```sql
 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "F_EMPLOYEE" **
CREATE OR REPLACE PROCEDURE proc_update_current_of ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
EXECUTE AS CALLER
AS
$$
  DECLARE
    --** SSC-PRF-0009 - PERFORMANCE REVIEW - CURSOR USAGE **
    C1 CURSOR
    FOR
      SELECT * FROM
        F_EMPLOYEE
      !!!RESOLVE EWI!!! /*** SSC-EWI-OR0110 - FOR UPDATE CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
      FOR UPDATE OF SALARY nowait;
  BEGIN
      OPEN C1;
      --** SSC-PRF-0004 - THIS STATEMENT HAS USAGES OF CURSOR FOR LOOP **
      FOR CREC IN C1 DO
      !!!RESOLVE EWI!!! /*** SSC-EWI-OR0136 - CURRENT OF CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
      UPDATE F_EMPLOYEE
        SET SALARY=
                   !!!RESOLVE EWI!!! /*** SSC-EWI-OR0036 - TYPES RESOLUTION ISSUES, ARITHMETIC OPERATION '+' MAY NOT BEHAVE CORRECTLY BETWEEN unknown AND Number ***/!!!SALARY+2000 WHERE CURRENT OF C1;
      END FOR;
      CLOSE C1;
  END;
$$;
```

### Related EWI

1. SSC-EWI-OR0036: Types resolution issues, the arithmetic operation may not behave correctly between string and date.
2. [SSC-PRF-0004](../performance-review/generalPRF.md): This statement has usages of cursor for loop.
3. SSC-EWI-OR0110: For Update Clause is not supported in Snowflake.

#### Best Practices

* Redesign the query to normal `UPDATE` or `DELETE` specifying the columns in the `WHERE` clause, consider that if there are duplicate records in the table the query can affect them multiple times.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-OR0137

Type attribute reference might be unsupported, so it was transformed to variant data type.

### Severity

Critical

### Description

TYPE ATTRIBUTE ‘TYPEUSED%TYPE’ MIGHT BE UNSUPPORTED, SO IT WAS TRANSFORMED TO VARIANT

#### Example Code

##### Oracle

```sql
CREATE OR REPLACE TABLE MYTABLE
(
  LOG_ID URITYPE
);

CREATE OR REPLACE PROCEDURE some_procedure()
IS
  L_MESSAGE MYTABLE.LOG_ID%TYPE;
BEGIN
  NULL;
END;
```

##### Snowflake Scripting

```sql
CREATE OR REPLACE TABLE MYTABLE
  (
  !!!RESOLVE EWI!!! /*** SSC-EWI-0028 - TYPE NOT SUPPORTED BY SNOWFLAKE ***/!!!
    LOG_ID URITYPE
  )
  COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "10/01/2025",  "domain": "no-domain-provided",  "migrationid": "aqCZAdErg3K0P04NglqCCg==" }}'
  ;

  CREATE OR REPLACE PROCEDURE some_procedure ()
  RETURNS VARCHAR
  LANGUAGE SQL
  COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "oracle",  "convertedOn": "10/01/2025",  "domain": "no-domain-provided",  "migrationid": "aqCZAdErg3K0P04NglqCCg==" }}'
  EXECUTE AS CALLER
  AS
  $$
  DECLARE
      L_MESSAGE VARIANT !!!RESOLVE EWI!!! /*** SSC-EWI-OR0137 - TYPE ATTRIBUTE 'MYTABLE.LOG_ID%TYPE' MIGHT BE UNSUPPORTED, SO IT WAS TRANSFORMED TO VARIANT ***/!!!;
  BEGIN
      NULL;
  END;
  $$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
