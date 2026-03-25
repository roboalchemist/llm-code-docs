# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/db2/db2-from-clause.md

# SnowConvert AI - IBM DB2 - From Clause

## Description

> The FROM clause specifies an intermediate result table

See the [DB2 FROM clause documentation](https://www.ibm.com/docs/en/db2/11.5?topic=subselect-from-clause) for this syntax.

## Grammar Syntax

## Table Reference

### Description

> A *table-reference* specifies an intermediate result table.

See the [DB2 table reference documentation](https://www.ibm.com/docs/en/db2/11.5?topic=clause-table-reference) for this syntax.

### Grammar Syntax

Navigate to the following pages to get more details about the translation spec for the subsections of the Table Reference grammar.

## Analyze Table Expression

### Description

> Returns the result of executing a specific data mining model by using an in-database analytics provider, a named model implementation, and input data.

Click [here](https://www.ibm.com/docs/en/db2/11.5?topic=clause-table-reference#sdx-synid_analyze_table-expression) to navigate to the IBM DB2 documentation page for this syntax.

Analyze Table Expressions are not supported in Snowflake. The output query can be malformed

### Grammar Syntax

### Sample Source Patterns

#### IBM DB2

```sql
 SELECT
   *
FROM v1 ANALYZE_TABLE(
   IMPLEMENTATION 'PROVIDER=SAS; ROUTINE_SOURCE_TABLE=ETLIN.SOURCE_TABLE; ROUTINE_SOURCE_NAME=SCORING_FUN3;')
ORDER BY 1;
```

##### Snowflake

```sql
SELECT
   *
FROM
   !!!RESOLVE EWI!!! /*** SSC-EWI-DB0019 - ANALYZE TABLE FACTOR IS NOT SUPPORTED ***/!!!
 v1 ANALYZE_TABLE(
   IMPLEMENTATION 'PROVIDER=SAS; ROUTINE_SOURCE_TABLE=ETLIN.SOURCE_TABLE; ROUTINE_SOURCE_NAME=SCORING_FUN3;')
ORDER BY 1;
```

### Related EWIs

1. [SSC-EWI-DB0019](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/db2EWI.md): ANALYZE TABLE FACTOR IS NOT SUPPORTED

## Collection Derived Table

### Description

> A collection-derived-table can be used to convert the elements of an array into values of a column in separate rows. If WITH ORDINALITY is specified, an extra column of data type INTEGER is appended. This column contains the position of the element in the array.

Click [here](https://www.ibm.com/docs/en/db2/11.5?topic=clause-table-reference#sdx-synid_frag-collection-derived-table) to navigate to the IBM DB2 documentation page for this syntax.

Collection Derived Tables are not supported in Snowflake.

### Grammar Syntax

### Sample Source Patterns

#### IBM DB2

```sql
SELECT
   *
FROM
   UNNEST(testArray) WITH ORDINALITY;
```

##### Snowflake

```sql
SELECT
   *
FROM
   !!!RESOLVE EWI!!! /*** SSC-EWI-DB0016 - UNNEST FUNCTION IS NOT SUPPORTED ***/!!!
   UNNEST(test) WITH ORDINALITY;
```

### Related EWIs

1. [SSC-EWI-DB0016](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/db2EWI.md): UNNEST FUNCTION IS NOT SUPPORTED

## Data Change Table Reference

### Description

> A *data-change-table-reference* clause specifies an intermediate result table. This table is based on the rows that are directly changed by the searched UPDATE, searched DELETE, or INSERT statement that is included in the clause.

Click [here](https://www.ibm.com/docs/en/db2/11.5?topic=clause-table-reference#sdx-synid_data-change-table-reference) to navigate to the IBM DB2 documentation page for this syntax.

Data Change Table Reference is not supported in Snowflake. The output query can be malformed.

### Grammar Syntax

### Sample Source Patterns

#### IBM DB2

```sql
 SELECT
   *
FROM
   OLD Table(UPDATE T1 SET NAME = 'Tony' where ID = 4)
```

#### Snowflake

```sql
SELECT
   *
FROM
   !!!RESOLVE EWI!!! /*** SSC-EWI-DB0006 - INTERMEDIATE RESULT TABLE IS NOT SUPPORTED. ***/!!!
   OLD Table(UPDATE T1 SET NAME = 'Tony' where ID = 4);
```

### Related EWIs

1. [SSC-EWI-DB0006](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/db2EWI.md): INTERMEDIATE RESULT TABLE IS NOT SUPPORTED.

## External Table Reference

### Description

> An external table resides in a text-based, delimited or non-delimited file outside of a database. An external-table-reference specifies the name of the file that contains an external table.

Click [here](https://www.ibm.com/docs/en/db2/11.5?topic=clause-table-reference#sdx-synid_external-table-reference) to navigate to the IBM DB2 documentation page for this syntax.

External Table Reference is not supported in Snowflake. The output query can be malformed.

### Grammar Syntax

### Sample Source Patterns

#### IBM DB2

```sql
 SELECT
   *
FROM
   EXTERNAL SOMENAME AS T1 LIKE TABLE2 USING(COMPRESS NO)
```

##### Snowflake

```sql
SELECT
   *
FROM
   !!!RESOLVE EWI!!! /*** SSC-EWI-DB0014 - THE USE OF EXTERNAL TABLE REFERENCES IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
   EXTERNAL SOMENAME AS T1 LIKE TABLE2 USING(COMPRESS NO);
```

### Related EWIs

1. [SSC-EWI-DB0014](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/db2EWI.md): THE USE OF EXTERNAL TABLE REFERENCES IS NOT SUPPORTED IN SNOWFLAKE

## Nested Table Expression

### Description

> A fullselect in parentheses is called a *nested table expression*. The intermediate result table is the result of that fullselect.

Click [here](https://www.ibm.com/docs/en/db2/11.5?topic=clause-table-reference#sdx-synid_frag-nested-table-expression) to navigate to the IBM DB2 documentation page for this syntax.

> **Warning:**
>
> Nested Table Expression is partially applicable in Snowflake.

### Grammar Syntax

### Sample Source Patterns

#### Unsupported cases

##### IBM DB2

```sql
 Select
   AValue
from
   LATERAL RETURN DATA UNTIL FEDERATED SQLSTATE VALUE 'stringConstant' WITHIN(
      Select
         AValue
      from
         ATable
   );
```

##### Snowflake

```sql
Select
   AValue
from
   LATERAL
--           --** SSC-FDM-0027 - REMOVED NEXT STATEMENT, NOT APPLICABLE IN SNOWFLAKE. CONTINUE HANDLER **
--           RETURN DATA UNTIL FEDERATED SQLSTATE VALUE 'stringConstant' WITHIN
                                                                             (
      Select
         AValue
      from
         ATable
   );
```

### Related EWIs

1. [SSC-FDM-0027](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/generalFDM.md): REMOVED NEXT STATEMENT, NOT APPLICABLE IN SNOWFLAKE.

## ONLY TABLE REFERENCE

### Description

> The use of ONLY(table-name) or ONLY(view-name) means that the rows of the applicable subtables or subviews are not included in the intermediate result table.

Click [here](https://www.ibm.com/docs/en/db2/11.5?topic=clause-table-reference#sdx-synid_only-table-reference) to navigate to the IBM DB2 documentation page for this syntax.

### Grammar Syntax

### Sample Source Patterns

#### IBM DB2

```sql
 Select * from ONLY(ATable) AS CorrelationName;
```

##### Snowflake

```sql
 Select * from
   ATable AS CorrelationName;
```

## OUTER TABLE REFERENCE

### Description

> The use of OUTER(table-name) or OUTER(view-name) represents a virtual table.

Click [here](https://www.ibm.com/docs/en/db2/11.5?topic=clause-table-reference#sdx-synid_outer-table-reference) to navigate to the IBM DB2 documentation page for this syntax.

> **Warning:**
>
> OUTER TABLE REFERENCE is not applicable in Snowflake.

### Grammar Syntax

### Sample Source Patterns

#### IBM DB2

```sql
 Select * from OUTER(ATable) AS CorrelationName;
```

##### Snowflake

```sql
 Select * from
   !!!RESOLVE EWI!!! /*** SSC-EWI-DB0004 - OUTER TABLE REFERENCE IS NOT SUPPORTED IN SNOWFLAKE. ***/!!! OUTER(ATable) AS CorrelationName;
```

### Related EWIs

1. [SSC-EWI-DB0004](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/db2EWI.md): OUTER TABLE REFERENCE IS NOT SUPPORTED IN SNOWFLAKE.

## Period Specification

> A period-specification identifies an intermediate result table consisting of the rows of the referenced table where the period matches the specification. A period-specification can be specified following the name of a temporal table or the name of a view

Click [here](https://www.ibm.com/docs/en/db2/11.5?topic=clause-table-reference#sdx-synid_period-specification) to navigate to the IBM DB2 documentation page for this syntax.

Period Specification is currently not supported by Snowflake.

### Grammar Syntax

### Sample Source Patterns

#### IBM DB2

```sql
 SELECT
   *
FROM
   Table1
FOR BUSINESS_TIME AS OF "12-12-12"
```

#### Snowflake

```sql
SELECT
   *
FROM
   Table1
   !!!RESOLVE EWI!!! /*** SSC-EWI-DB0003 - PERIOD SPECIFICATION IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
FOR BUSINESS_TIME AS OF "12-12-12";
```

### Related EWIs

1. [SSC-EWI-DB0003](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/db2EWI.md): PERIOD SPECIFICATION IS NOT SUPPORTED IN SNOWFLAKE.

## Table Function Reference

### Description

> Table functions return columns of a table, resembling a table created through a simple CREATE TABLE statement. A table function can be used only in the FROM clause of a statement.

Click [here](https://www.ibm.com/docs/en/db2/11.5?topic=clause-table-reference#sdx-synid_table-function-reference) to navigate to the IBM DB2 documentation page for this syntax.

> **Warning:**
>
> Table Function Reference is not applicable in Snowflake.

### Grammar Syntax

### Sample Source Patterns

For the transformation of Table Function Reference, we must comment out the table-UDF-cardinality-clause. This clause is used for performance reasons, and is not relevant in Snowflake.

#### IBM DB2

```sql
 SELECT * FROM TABLE(TUDF1(3) CARDINALITY 30) AS X;
```

##### Snowflake

```sql
SELECT * FROM TABLE(TUDF1(3)) AS X;
```

Note that each function along with the type of its arguments specified in the table reference must exist, otherwise it will cause errors.
