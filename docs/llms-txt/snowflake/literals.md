# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/oracle/basic-elements-of-oracle-sql/literals.md

# SnowConvert AI - Oracle - Literals

> The terms literal and constant value are synonymous and refer to a fixed data value.
> ([Oracle SQL Language Reference Literals](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Literals.html#GUID-192417E8-A79D-4A1D-9879-68272D925707))

## Interval Literal

Interval Literal Not Supported In Current Scenario

### Description

Snowflake Intervals can only be used in arithmetic operations. Intervals used in any other scenario are not supported.

#### Example Code

##### Oracle

```sql
SELECT INTERVAL '1-5' YEAR TO MONTH FROM DUAL;
```

##### Snowflake

```sql
SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-0107 - INTERVAL LITERAL IS NOT SUPPORTED BY SNOWFLAKE IN THIS SCENARIO  ***/!!!
 INTERVAL '1-5' YEAR TO MONTH FROM DUAL;
```

### Known Issues

No issues were found.

### Related EWIs

1. [SSC-EWI-0107](../../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Interval Literal Not Supported In Current Scenario.

## Interval Type and Date Type

Operation Between Interval Type and Date Type not Supported

### Description

`INTERVAL YEAR TO MONTH` and `INTERVAL DAY TO SECOND` are not a supported data type, they are transformed to `VARCHAR(20)`. Therefore all arithmetic operations between **Date Types** and the original **Interval Type Columns** are not supported.

Furthermore, operations between an Interval Type and Date Type (in this order) are not supported in Snowflake; and these operations use this EWI as well.

#### Example Code

##### Oracle

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

##### Snowflake

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

#### Recommendations

* Implement the UDF to simulate the Oracle behavior.
* Extract the already transformed value that was stored in the column during migration, and use it as a Snowflake [**Interval Constant**](https://docs.snowflake.com/en/sql-reference/data-types-datetime.html#interval-constants) when possible.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

### Related EWIs

1. [SSC-EWI-0036](../../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Data type converted to another data type.
2. [SSC-EWI-OR0095](../../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/oracleEWI.md): Operation Between Interval Type and Date Type not Supported.
3. [SSC-FDM-OR0042](../../../general/technical-documentation/issues-and-troubleshooting/functional-difference/oracleFDM.md): Date Type Transformed To Timestamp Has A Different Behavior.

## Text literals

### Description

> Use the text literal notation to specify values whenever `string` appears in the syntax of expressions, conditions, SQL functions, and SQL statements in other parts of this reference.
>
> ([Oracle SQL Language Reference Text literals](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Literals.html#GUID-1824CBAA-6E16-4921-B2A6-112FB02248DA))

```sql
[ {N | n} ]
{ '[ c ]...'
| { Q | q } 'quote_delimiter c [ c ]... quote_delimiter'
}
```

### Sample Source Patterns

#### Empty string (‘’)

The empty strings are equivalent to *NULL* in Oracle, so in order to emulate the behavior in Snowflake, the empty strings are converted to *NULL* or *undefined* depending if the literal is used inside a procedure or not.

##### Oracle

```sql
SELECT UPPER('') FROM DUAL;
```

##### Result

| UPPER(‘’) |
| --- |
|  |

##### Snowflake

```sql
SELECT UPPER(NULL) FROM DUAL;
```

##### Result

| UPPER(NULL) |
| --- |
|  |

#### Empty string in stored procedures

##### Oracle

```sql
CREATE TABLE empty_string_table(
col1 VARCHAR(10),
col2 VARCHAR(10));

CREATE OR REPLACE PROCEDURE null_proc AS
    var1 INTEGER := '';
    var3 INTEGER := null;
    var2 VARCHAR(20) := 'hello';
BEGIN
    var1 := var1 + 456;
    var2 := var2 || var1;
    IF var1 IS NULL THEN
        INSERT INTO empty_string_table VALUES (var1, var2);
    END IF;
END;

CALL null_proc();

SELECT * FROM empty_string_table;
```

##### Result

| COL1 | COL2 |
| --- | --- |
|  | hello |

##### Snowflake

```sql
CREATE OR REPLACE TABLE empty_string_table (
    col1 VARCHAR(10),
    col2 VARCHAR(10))
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}}'
;

CREATE OR REPLACE PROCEDURE null_proc ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"oracle"}}}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        var1 INTEGER := NULL;
        var3 INTEGER := null;
        var2 VARCHAR(20) := 'hello';
    BEGIN
        var1 := :var1 + 456;
        var2 := NVL(:var2 :: STRING, '') || NVL(:var1 :: STRING, '');
        IF (:var1 IS NULL) THEN
            INSERT INTO empty_string_table
            VALUES (:var1, :var2);
        END IF;
    END;
$$;

CALL null_proc();

SELECT * FROM
    empty_string_table;
```

##### Result

| COL1 | COL2 |
| --- | --- |
|  | hello |

#### Empty string in built-in functions

> **Warning:**
>
> The transformation does not apply when the empty string is used as an argument of the *REPLACE* and *CONCAT* functions in order to keep the functional equivalence.

##### Oracle

```sql
SELECT REPLACE('Hello world', '', 'l'), CONCAT('A','') FROM DUAL;
```

##### Result

| REPLACE(‘HELLOWORLD’,’’,’L’) | CONCAT(‘A’,’’) |
| --- | --- |
| Hello world | A |

##### Snowflake

```sql
SELECT REPLACE('Hello world', '', 'l'), CONCAT('A','') FROM DUAL;
```

##### Result

| REPLACE(‘HELLO WORLD’, ‘’, ‘L’) | CONCAT(‘A’,’’) |
| --- | --- |
| Hello world | A |

> **Note:**
>
> If the empty strings are replaced by NULL for these cases, the results of the queries will be different.

### Known Issues

No issues were found.

### Related EWIs

No related EWIs.
