# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/conversion-issues/postgresqlEWI.md

# SnowConvert AI - PostgreSQL Issues

> **Note:**
>
> **Conversion Scope**
>
> SnowConvert AI for PostgreSQL focuses its assessment and translation capabilities primarily on TABLES and VIEWS.
> While SnowConvert AI can recognize other types of ANSI-standard statements, these are not yet fully supported for conversion. This means that while the tool may identify them, it won’t perform a complete translation for these unsupported code units.

## SSC-EWI-PG0001

Age is not supported on Snowflake

### Severity

Medium

#### Description

This error is added because SnowConvert AI does not support the `age()` functionality.

#### Code Example

##### Input Code

##### PostgreSQL

```sql
 SELECT
   age(date1::date, date2::date)
FROM
   Table1;
```

##### Generated Code

##### Snowflake

```sql
 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECTS "age", "Table1" **
SELECT
   !!!RESOLVE EWI!!! /*** SSC-EWI-PG0001 - AGE IS NOT SUPPORTED ON SNOWFLAKE. ***/!!!
   AGE(date1::date, date2::date)
FROM
   Table1;
```

#### Best Practices

* The `Datediff` time function can solve some cases where the objective of the query is to obtain a specific range of values but this has to be handled manually for each scenario. For more information please refer to the Snowflake documentation about [Datediff](https://docs.snowflake.com/en/sql-reference/functions/datediff.html).
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0002

Constraint index parameter not supported

### Severity

Low

#### Description

The use of the following index parameters in constraints are not supported by Snowflake.

* INCLUDE
* WITH
* USING INDEX TABLESPACE

#### Code Example

##### Input Code

##### PostgreSQL

```sql
 CREATE TABLE Table1 (
    code        char(5),
    date_prod   date,
    CONSTRAINT production UNIQUE(date_prod) INCLUDE(code)
);

CREATE TABLE Table2 (
    name    varchar(40),
    UNIQUE(name) WITH (fillfactor=70)
);

CREATE TABLE Table3 (
    name    varchar(40),
    PRIMARY KEY(name) USING INDEX TABLESPACE tablespace_name
);
```

##### Generated Code

##### Snowflake

```sql
 CREATE TABLE Table1 (
    code        char(5),
    date_prod   date,
    CONSTRAINT production UNIQUE(date_prod)
                                            !!!RESOLVE EWI!!! /*** SSC-EWI-PG0002 - INCLUDE PARAMETER NOT APPLICABLE. CONSTRAINT INDEX PARAMETERS ARE NOT SUPPORTED IN SNOWFLAKE. ***/!!! INCLUDE(code)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "postgresql",  "convertedOn": "09/17/2024" }}';

CREATE TABLE Table2 (
    name    varchar(40),
    UNIQUE(name)
                 !!!RESOLVE EWI!!! /*** SSC-EWI-PG0002 - WITH PARAMETER NOT APPLICABLE. CONSTRAINT INDEX PARAMETERS ARE NOT SUPPORTED IN SNOWFLAKE. ***/!!! WITH (fillfactor=70)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "postgresql",  "convertedOn": "09/17/2024" }}';

CREATE TABLE Table3 (
    name    varchar(40),
    PRIMARY KEY(name)
                      !!!RESOLVE EWI!!! /*** SSC-EWI-PG0002 - USING PARAMETER NOT APPLICABLE. CONSTRAINT INDEX PARAMETERS ARE NOT SUPPORTED IN SNOWFLAKE. ***/!!! USING INDEX TABLESPACE tablespace_name
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "postgresql",  "convertedOn": "09/17/2024" }}';
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0003

Inheritance not supported

### Severity

Low

#### Description

Inheritance between tables is allowed in PostgreSQL, but Snowflake does not support it. For more information about inheritance in PostgreSQL click [here](https://www.postgresql.org/docs/current/ddl-inherit.html).

#### Code Example

##### Input Code

##### PostgreSQL

```sql
 ALTER TABLE Table1
ADD CONSTRAINT const3 UNIQUE (zip);
```

##### Generated Code

##### Snowflake

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-PG0003 - TABLE INHERITANCE IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
ALTER TABLE Table1
ADD CONSTRAINT const3 UNIQUE (zip);
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0004

Exclude constraint not supported

### Severity

Medium

#### Description

The exclude constraint used in PostgreSQL is not supported by Snowflake.

#### Code Example

##### Input Code

##### PostgreSQL

```sql
 CREATE TABLE Table1 (
    id      int,
    EXCLUDE USING gist (id WITH &&)
);
```

##### Generated Code

##### Snowflake

```sql
 CREATE TABLE Table1 (
    id      int,
    !!!RESOLVE EWI!!! /*** SSC-EWI-PG0004 - EXCLUDE CONSTRAINT IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
    EXCLUDE USING gist (id WITH &&)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "postgresql",  "convertedOn": "09/17/2024" }}';
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0006

Reference to a variable using the Label is not supported by Snowflake.

### Severity

Medium

#### Description

This error is added when a FOR loop’s body references a variable using the label. Snowflake does not support referencing a variable using the qualified name.

#### Code Example

##### Input Code

##### PostgreSQL

```sql
 CREATE OR REPLACE PROCEDURE procedure1(out result VARCHAR(100))
LANGUAGE plpgsql
AS $$
BEGIN
result := '<';
<<outer_loop>>
for i in 1..3 loop
  <<inner_loop>>
  for i in 4..6 loop
  result := result || '(' || outer_loop.i || ', ' || i || ')';
  end loop inner_loop;
end loop outer_loop;
result := result || '>';
END;
$$;
```

##### Generated Code

##### Snowflake

```sql
 CREATE OR REPLACE PROCEDURE procedure1 (result OUT VARCHAR(100))
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "postgresql",  "convertedOn": "07/16/2025",  "domain": "no-domain-provided" }}'
AS $$
BEGIN
result := '<';
for i in 1 TO 3
                --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **
                loop
  for i in 4 TO 6
                  --** SSC-PRF-0008 - PERFORMANCE REVIEW - LOOP USAGE **
                  loop
  result := result || '(' ||
                             !!!RESOLVE EWI!!! /*** SSC-EWI-PG0006 - REFERENCE TO A VARIABLE USING THE LABEL IS NOT SUPPORTED BY SNOWFLAKE. ***/!!! outer_loop.i || ', ' || i || ')';
  end loop inner_loop;
end loop outer_loop;
result := result || '>';
END;
$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0007

Into clause in Dynamic SQL is not support in Snowflake

### Severity

Low

#### Description

PostgreSQL Dynamic SQL allows the `INTO` clause to store query results in variables. Snowflake does not support this functionality. Therefore, the `INTO` clause will be flagged with an EWI’.

#### Code Example

##### Input Code

##### PostgreSQL

```sql
 CREATE OR REPLACE PROCEDURE get_max_id(table_name VARCHAR, OUT max_id INTEGER)
AS $$
DECLARE
    sql_statement VARCHAR;
BEGIN
    sql_statement := 'SELECT MAX(id) FROM ' || table_name || ';';
    EXECUTE sql_statement INTO max_id;
END;
$$ LANGUAGE plpgsql;
```

##### Generated Code

##### Snowflake

```sql
 CREATE OR REPLACE PROCEDURE get_max_id (table_name VARCHAR, max_id OUT INTEGER)
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "postgresql",  "convertedOn": "07/16/2025",  "domain": "no-domain-provided" }}'
AS $$
DECLARE
    sql_statement VARCHAR;
BEGIN
    sql_statement := 'SELECT MAX(id) FROM ' || table_name || ';';
    EXECUTE IMMEDIATE sql_statement
                                    !!!RESOLVE EWI!!! /*** SSC-EWI-PG0007 - INTO CLAUSE IN DYNAMIC SQL IS NOT SUPPORTED IN SNOWFLAKE. ***/!!! INTO max_id;
END;
$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0008

The use of interval within a to_char function is not compatible with Snowflake.

### Severity

High

#### Description

The use of `interval` within the `to_char` to convert date/times data types into text is not supported in Snowflake.

#### Code Example

##### Input Code

##### PostgreSQL

```sql
 SELECT to_char(interval '15h 2m 12s', 'HH24:MI:SS');
```

##### Generated Code

##### Snowflake

```sql
 SELECT to_char(INTERVAL '15h, 2m, 12s', 'HH24:MI:SS') !!!RESOLVE EWI!!! /*** SSC-EWI-PG0008 - THE USE OF INTERVAL WITHIN TO_CHAR IS NOT SUPPORTED BY SNOWFLAKE. ***/!!!;
```

For more information please refer to

* PostgreSQL [to_char](https://www.postgresql.org/docs/15/functions-formatting.html).
* Snowflake [to_char](https://docs.snowflake.com/en/sql-reference/functions/to_char).

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0009

Comment on ‘Type’ is not supported by Snowflake.

### Severity

Low

#### Description

In the original code, there are various objects that can receive comments. However, in Snowflake, several of these objects do not exist, and thus, comments cannot be assigned to them. The code for handling these scenarios is commented out to prevent any potential errors.

#### Code Example

##### Input Code

##### PostgreSQL

```sql
 COMMENT ON RULE rule_name on TABLE_NAME IS 'this is a comment';
```

##### Generated Code

##### Snowflake

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-PG0009 - COMMENT ON 'RULE' IS NOT SUPPORTED BY SNOWFLAKE. ***/!!!
COMMENT ON RULE rule_name on TABLE_NAME IS 'this is a comment';
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0010

Create temporary sequence is not supported by Snowflake

### Severity

Low

#### Description

When a temporary sequence is created in PostgreSQL, it is only created for the active session and is automatically deleted when you log out of the session. However, this functionality is not available in Snowflake, so it is generated as a normal sequence. When executed, a similar sequence name may already exist, which will cause an error for an existing object.

#### Code Example

##### Input code

##### PostgreSQL

```sql
 CREATE TEMPORARY SEQUENCE sequence1;
CREATE TEMP SEQUENCE sequence2;
```

##### Generated Code

##### Snowflake

```sql
 --** SSC-FDM-PG0009 - THE SEQUENCE NEXTVAL PROPERTY SNOWFLAKE DOES NOT GUARANTEE GENERATING SEQUENCE NUMBERS WITHOUT GAPS. **
CREATE TEMPORARY !!!RESOLVE EWI!!! /*** SSC-EWI-PG0010 - CREATE TEMPORARY SEQUENCE IS NOT SUPPORTED BY SNOWFLAKE. ***/!!! SEQUENCE sequence1;

--** SSC-FDM-PG0009 - THE SEQUENCE NEXTVAL PROPERTY SNOWFLAKE DOES NOT GUARANTEE GENERATING SEQUENCE NUMBERS WITHOUT GAPS. **
 CREATE TEMP !!!RESOLVE EWI!!! /*** SSC-EWI-PG0010 - CREATE TEMPORARY SEQUENCE IS NOT SUPPORTED BY SNOWFLAKE. ***/!!! SEQUENCE sequence2;
```

### Best Practices

* If you have a creation problem, you can try to rename the sequence to avoid collisions.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com).

## SSC-EWI-PG0011

The sequence option ‘option_name’ is not supported by Snowflake.

### Severity

Low

#### Description

Some options available in PostgreSQL for the sequence statement are not supported by Snowflake.

The unsupported options are:

* Unlogged.
* AS <data_type>.
* MinValue.
* MaxValue.
* No MinValue.
* No MaxValue.
* Cache.
* Cycle.
* Owner By.

#### Code Example

##### Input code

##### PostgreSQL

```sql
 CREATE UNLOGGED SEQUENCE sequence_name;
```

##### Generated Code

##### Snowflake

```sql
 --** SSC-FDM-PG0009 - THE SEQUENCE NEXTVAL PROPERTY SNOWFLAKE DOES NOT GUARANTEE GENERATING SEQUENCE NUMBERS WITHOUT GAPS. **
CREATE UNLOGGED !!!RESOLVE EWI!!! /*** SSC-EWI-PG0011 - 'UNLOGGED' IS NOT SUPPORTED BY SNOWFLAKE. ***/!!! SEQUENCE sequence_name;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0012

NOT VALID constraint option is not supported by Snowflake.

### Description

The [`NOT VALID`](https://www.postgresql.org/docs/current/sql-altertable.html#SQL-ALTERTABLE-DESC-ADD-TABLE-CONSTRAINT) constraint option is used in the context of adding or altering a constraint to indicate that the constraint should be added or modified without checking the existing data for compliance with the constraint. This clause is not supported by Snowflake.

#### Code Example

##### Input Code

##### PostgreSQL

```sql
 ALTER TABLE Table1 *
ADD CONSTRAINT const UNIQUE (zip) NOT VALID;
```

##### Generated Code

##### Snowflake

```sql
 ALTER TABLE Table1
ADD CONSTRAINT const UNIQUE (zip)
                                  !!!RESOLVE EWI!!! /*** SSC-EWI-PG0012 - NOT VALID CONSTRAINT OPTION IS NOT SUPPORTED BY SNOWFLAKE. ***/!!! NOT VALID;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0014

Snowflake scripting cursors do not support fetch orientation

### Severity

Medium

#### Description

In Snowflake, the [FETCH cursor](https://docs.snowflake.com/en/sql-reference/snowflake-scripting/fetch) statement always fetches the next row in the cursor. When transforming the code, SnowConvert AI will transform cursor orientations that are equivalent to a FETCH NEXT as they are functionally equivalent in Snowflake, namely:

* `FETCH NEXT`
* `FETCH FORWARD`
* `FETCH RELATIVE 1`
* `FETCH` (no orientation specified)

Any other orientation is unsupported and the FETCH statement will be marked with this EWI to reflect that.

#### Code Example

##### Input Code

##### PostgreSQL

```sql
 CREATE OR REPLACE PROCEDURE cursor_test()
AS $$
BEGIN
   FETCH FORWARD FROM cursor1 INTO my_var;
   FETCH FIRST FROM cursor1 INTO my_var;
   FETCH LAST FROM cursor1 INTO my_var;
END;
$$;
```

##### Generated Code

##### Snowflake

```sql
 CREATE OR REPLACE PROCEDURE cursor_test ()
RETURNS VARCHAR
AS $$
BEGIN
   FETCH
    cursor1 INTO my_var;
   !!!RESOLVE EWI!!! /*** SSC-EWI-PG0014 - SNOWFLAKE SCRIPTING CURSORS DO NOT SUPPORT FETCH ORIENTATION. ***/!!!
   FETCH FIRST FROM cursor1 INTO my_var;
   !!!RESOLVE EWI!!! /*** SSC-EWI-PG0014 - SNOWFLAKE SCRIPTING CURSORS DO NOT SUPPORT FETCH ORIENTATION. ***/!!!
   FETCH LAST FROM cursor1 INTO my_var;
END;
$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0015

Fetch cursor without target variables is not supported in Snowflake

### Severity

Medium

#### Description

In PostgreSQL, it is possible to use a [FETCH statement](https://www.postgresql.org/docs/current/sql-fetch.html) without INTO to print on the console the values of fetched rows. However, Snowflake requires the [FETCH statement](https://docs.snowflake.com/en/sql-reference/snowflake-scripting/fetch) to specify the INTO clause with the variables where the fetched row values are going to be stored.

Whenever a FETCH with no INTO is found in the code, SnowConvert AI will generate this EWI to notify the user that this type of FETCH is not supported.

#### Code Example

##### Input Code

##### PostgreSQL

```sql
 FETCH PRIOR FROM cursor1;
```

##### Generated Code

##### Snowflake

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-PG0015 - FETCH CURSOR WITHOUT TARGET VARIABLES IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
FETCH PRIOR FROM cursor1;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0016

Bit String Type converted to Varchar Type

### Severity

Low

#### Description

When migrating from PostgreSQL, be aware that its BIT String Types and related functions are not natively supported in Snowflake. These data types will be converted to Snowflake’s VARCHAR. This conversion means that any PostgreSQL queries or application logic that depend on bitwise operations on these columns will require significant modification to achieve the same functionality in Snowflake.

#### Code Example

##### Input Code

##### PostgreSQL

```sql
 CREATE TABLE table1 (
   col1 bit(10)
);
```

##### Generated Code

##### Snowflake

```sql
 CREATE TABLE table1 (
   col1 CHARACTER(10) !!!RESOLVE EWI!!! /*** SSC-EWI-PG0016 - BIT DATA TYPE CONVERTED TO CHARACTER ***/!!!
);
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-PG0017

Transformation for routine body literal is not supported.

### Severity

Low

#### Description

SnowConvert AI does not support transformation for quoted literal routine body. Use the [arrange option](../../../getting-started/running-snowconvert/conversion/postgresql-conversion-settings.md) to modify them to dollar routine body.

#### Code Example

##### Input Code

##### PostgreSQL

```sql
CREATE OR REPLACE PROCEDURE proc1 (x varchar default 'pigs')
LANGUAGE plpgsql
AS
'
begin
    --test
   insert into tabletest2 values ($$Dianne''s pigs$$);
   x = ''Diannes pigs'';
end;
';
```

##### Generated Code

##### Snowflake

```sql
CREATE OR REPLACE PROCEDURE proc1 (x varchar default 'pigs' !!!RESOLVE EWI!!! /*** SSC-EWI-0073 - PENDING FUNCTIONAL EQUIVALENCE REVIEW FOR 'ParameterDefaultExpr' NODE ***/!!!)
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "postgresql",  "convertedOn": "01/13/2026",  "domain": "no-domain-provided",  "migrationid": "m7mbAfEK5XyHKQR4pRek1g==" }}'
EXECUTE AS CALLER
AS
   !!!RESOLVE EWI!!! /*** SSC-EWI-PG0017 - TRANSFORMATION FOR ROUTINE BODY LITERAL IS NOT SUPPORTED. USE ARRANGE OPTION. ***/!!!
'
begin
    --test
   insert into tabletest2 values ($$Dianne''s pigs$$);
   x = ''Diannes pigs'';
end;
';
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
