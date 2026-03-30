# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/conversion-issues/sqlServerEWI.md

# SnowConvert AI - SQL Server-Azure Synapse Issues

Applies to

* SQL Server
* Azure Synapse Analytics
* Sybase

## SSC-EWI-TS0001

User defined function body not generated

### Severity

Critical

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI appears when SnowConvert AI handles a critical exception that causes the function body not to be generated during its translation.

#### Example Code

##### SQL Server

```sql
 CREATE FUNCTION func1 ()
RETURNS VARCHAR
SELECT
   *
FROM
   TABLE1
```

##### Snowflake

```sql
 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "TABLE1" **
CREATE OR REPLACE FUNCTION func1 ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
!!!RESOLVE EWI!!! /*** SSC-EWI-TS0001 - THE BODY WAS NOT GENERATED FOR FUNCTION 'func1' ***/!!!
AS
$$

$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0002

The ANSI_PADDING OFF is not supported in Snowflake.

### Severity

Low

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

In Transact-SQL, the statement `SET ANSI_PADDING OFF` removes the trailing spaces in the insertion of char Data types. Since `SET ANSI_PADDING OFF` is not a directly configurable setting in Snowflake; SnowConvert AI will generate this EWI.

#### Example Code

##### SQL Server

```sql
 SET ANSI_PADDING OFF;
```

##### Snowflake

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TS0002 - THE ANSI_PADDING OFF IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
SET ANSI_PADDING OFF;
```

#### Best Practices

* Add `RTRIM` to all `CHAR()` data type insertions to remove this issue, including ETL code.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0003

The ANSI_WARNINGS OFF is not supported in Snowflake.

### Severity

Low

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

In Transact-SQL, the statement `SET ANSI_WARNINGS OFF` disables warnings such as Division by Zero or arithmetic overflow. Since `SET ANSI_WARNINGS OFF` is not a directly configurable setting in Snowflake, SnowConvert AI will generate this EWI.

#### Example Code

##### SQL Server

```sql
 SET ANSI_WARNINGS OFF;
```

##### Snowflake

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TS0003 - THE ANSI_WARNINGS OFF IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
SET ANSI_WARNINGS OFF;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0009

The following transaction may contain nested transactions and this is considered a complex pattern not supported in Snowflake.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

High

#### Description

This error is added to indicate when a transaction may contain nested transactions. In SQL Server, transactions can be nested. This means that it is possible to start a new transaction within an existing transaction. If after the first BEGIN statement, we execute another one, a new transaction will be opened and the current transaction count will be increased by one.\

On the other hand this is not supported in Snowflake, what will happen is that the second BEGIN statement will be ignored and we will still have only one transaction. For more information please refer to [SQL Server Transactions](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/transactions-transact-sql?view=sql-server-ver16).

#### Code Example

##### Input Code

```sql
 CREATE PROC transactionsTest
AS
BEGIN TRANSACTION
   SELECT @@TRANCOUNT AS TransactionCount_AfterFirstTransaction
   INSERT INTO TESTSCHEMA.TESTTABLE(ID) VALUES (1), (2)
   BEGIN TRANSACTION
      SELECT @@TRANCOUNT AS TransactionCount_AfterSecondTransaction
      INSERT INTO TESTSCHEMA.TESTTABLE(ID) VALUES (3), (4)
   COMMIT;
   SELECT @@TRANCOUNT AS TransactionCount_AfterFirstCommit
COMMIT;
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE transactionsTest ()
RETURNS ARRAY
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
 DECLARE
  ProcedureResultSet1 VARCHAR;
  ProcedureResultSet2 VARCHAR;
  ProcedureResultSet3 VARCHAR;
  return_arr ARRAY := array_construct();
 BEGIN
  !!!RESOLVE EWI!!! /*** SSC-EWI-TS0009 - THE FOLLOWING TRANSACTION MAY CONTAIN NESTED TRANSACTIONS WHICH ARE NOT SUPPORTED IN SNOWFLAKE. ***/!!!
  BEGIN TRANSACTION;
  ProcedureResultSet1 := 'RESULTSET_' || REPLACE(UPPER(UUID_STRING()), '-', '_');
  CREATE OR REPLACE TEMPORARY TABLE IDENTIFIER(:ProcedureResultSet1) AS
   SELECT
    :TRANCOUNT AS TransactionCount_AfterFirstTransaction;
  return_arr := array_append(return_arr, :ProcedureResultSet1);
  INSERT INTO TESTSCHEMA.TESTTABLE (ID) VALUES (1), (2);
  BEGIN TRANSACTION;
  ProcedureResultSet2 := 'RESULTSET_' || REPLACE(UPPER(UUID_STRING()), '-', '_');
  CREATE OR REPLACE TEMPORARY TABLE IDENTIFIER(:ProcedureResultSet2) AS
   SELECT
    :TRANCOUNT AS TransactionCount_AfterSecondTransaction;
  return_arr := array_append(return_arr, :ProcedureResultSet2);
  INSERT INTO TESTSCHEMA.TESTTABLE (ID) VALUES (3), (4);
  COMMIT;
  ProcedureResultSet3 := 'RESULTSET_' || REPLACE(UPPER(UUID_STRING()), '-', '_');
  CREATE OR REPLACE TEMPORARY TABLE IDENTIFIER(:ProcedureResultSet3) AS
   SELECT
    :TRANCOUNT AS TransactionCount_AfterFirstCommit;
  return_arr := array_append(return_arr, :ProcedureResultSet3);
  COMMIT;
  --** SSC-FDM-0020 - MULTIPLE RESULT SETS ARE RETURNED IN TEMPORARY TABLES **
  RETURN return_arr;
 END;
$$;
-- ** SSC-EWI-0001 - UNRECOGNIZED TOKEN ON LINE '12' COLUMN '1' OF THE SOURCE CODE STARTING AT 'END'. EXPECTED 'BATCH' GRAMMAR. **
--END
   ;
```

#### Best Practices

* In Snowflake nested transactions will not cause compilation errors, they will simply be ignored. You can access the assessment reports to check if nested transactions are present.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

### Related EWI

1. [SSC-FDM-0020](../functional-difference/generalFDM.md): Multiple result sets are returned in temporary tables
2. [SSC-EWI-0001](generalEWI.md): Unrecognized token on the line of the source code.
3. [SSC-EWI-0040](generalEWI.md): Statement Not Supported.

## SSC-EWI-TS0010

Common table expression in view not supported in Snowflake.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

High

#### Description

This error is added when an invalid CTE is inside a view since views are materialized representations of queries, which means that they only define how data is retrieved and presented, not how it is manipulated.

#### Code Example

##### Input Code

```sql
 Create View viewName
as
with commonTableExpressionName (
   columnName
) as
(
   select
      1
)
((select
   1 as col2)
union
(
   select
      1 as col3
));
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TS0010 - COMMON TABLE EXPRESSION IN VIEW NOT SUPPORTED IN SNOWFLAKE. ***/!!!
CREATE OR REPLACE VIEW viewName
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"transact"}}'
AS
!!!RESOLVE EWI!!! /*** SSC-EWI-0021 - WITH CTE NOT SUPPORTED IN SNOWFLAKE ***/!!!
with commonTableExpressionName (
   columnName
) as
(
   select
      1
)
((select
   1 as col2)
union
(
   select
      1 as col3
));
```

### Related EWI

1. [SSC-EWI-0021](generalEWI.md): Not supported.

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0013

Computed column transformed

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-TS0013](../functional-difference/sqlServerFDM.md) documentation

### Severity

Low

#### Description

This warning is added when an SQL Server computed column is transformed to its Snowflake equivalent. It is added because, in some cases, the functional equivalence could be affected.

#### Code Example

##### Input Code

```sql
 CREATE TABLE [TestTable](
    [Col1] AS (CONVERT ([REAL], ExpressionValue))
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE TestTable (
    Col1 REAL AS (CAST(ExpressionValue AS REAL)) /*** SSC-FDM-TS0014 - COMPUTED COLUMN WAS TRANSFORMED TO ITS SNOWFLAKE EQUIVALENT, FUNCTIONAL EQUIVALENCE VERIFICATION PENDING. ***/
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"transact"}}'
;
```

#### Best Practices

* No additional user actions are required; it is just informative.
* Add manual changes to the not-transformed expression.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0015

Data type is not supported in Snowflake

### Severity

Medium

### Description

This warning is added when an SQL Server column has an unsupported type in Snowflake.

#### Code Example

##### Input Code

```sql
 CREATE TABLE table1
(
    column1 customType,
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE table1
(
    column1 VARIANT !!!RESOLVE EWI!!! /*** SSC-EWI-TS0015 - DATA TYPE CUSTOMTYPE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"transact"}}'
;
```

#### Best Practices

* Check the Snowflake data types [documentation](https://docs.snowflake.com/en/sql-reference/data-types.html) to find an equivalent for the data type.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0016

Translation for ODBC Scalar function pending

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

This EWI is added when SnowConvert AI finds an ODBC Scalar function inside the input code.
User-defined functions are not supported in ODBC Scalar Function.

#### Code Example

##### Input Code

```sql
 SELECT {fn CURRENT_DATE_UDF()};
```

##### Generated Code

```sql
 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "CURRENT_DATE_UDF" **
SELECT
CURRENT_DATE_UDF() !!!RESOLVE EWI!!! /*** SSC-EWI-0073 - PENDING FUNCTIONAL EQUIVALENCE REVIEW FOR 'CURRENT_DATE_UDF' NODE ***/!!!!!!RESOLVE EWI!!! /*** SSC-EWI-TS0016 - USER DEFINED FUNCTIONS ARE NOT SUPPORTED IN ODBC SCALAR FUNCTION. ***/!!!;
```

### Related EWI

1. [SSC-EWI-0073](generalEWI.md): Pending Functional Equivalence Review.

#### Best Practices

* No additional user actions are required; it is just informative.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0017

Masking not supported

### Severity

Low

#### Description

This EWI is added when SnowConvert AI finds a masked column inside a `CREATE TABLE` statement. This functionality doesn’t work by adding the option in the column declaration. Manual effort is needed to have the same behavior as SQL Server.

#### Code Example

##### Input Code

```sql
 CREATE TABLE TABLE1
(
  [COL1] nvarchar MASKED WITH (FUNCTION = 'default()') NULL,
  [COL2] varchar(100) MASKED WITH (FUNCTION = 'partial(1, "xxxxx", 1)') NULL,
  [COL3] varchar(100) MASKED WITH (FUNCTION = 'email()') NOT NULL,
  [COL4] smallint MASKED WITH (FUNCTION = 'random(1, 100)') NULL
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE TABLE1
(
  COL1 VARCHAR
               !!!RESOLVE EWI!!! /*** SSC-EWI-TS0017 - COLUMN MASKING NOT SUPPORTED IN CREATE TABLE ***/!!!
               MASKED WITH (FUNCTION = 'default()') NULL,
  COL2 VARCHAR(100)
                    !!!RESOLVE EWI!!! /*** SSC-EWI-TS0017 - COLUMN MASKING NOT SUPPORTED IN CREATE TABLE ***/!!!
 MASKED WITH (FUNCTION = 'partial(1, "xxxxx", 1)') NULL,
  COL3 VARCHAR(100)
                    !!!RESOLVE EWI!!! /*** SSC-EWI-TS0017 - COLUMN MASKING NOT SUPPORTED IN CREATE TABLE ***/!!!
 MASKED WITH (FUNCTION = 'email()') NOT NULL,
  COL4 SMALLINT
                !!!RESOLVE EWI!!! /*** SSC-EWI-TS0017 - COLUMN MASKING NOT SUPPORTED IN CREATE TABLE ***/!!!
                MASKED WITH (FUNCTION = 'random(1, 100)') NULL
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
;
```

#### Best Practices

SnowConvert AI is not generating `MASKING POLICIES` in the current version, so they have to be created manually. E.g.:

The first step is to create a masking policy administrator role.

```sql
 create role masking_admin;
```

The second one is to grant the necessary privileges to the created role.

```sql
 grant create masking policy on schema PUBLIC to role masking_admin;
allow table_owner role to set or unset the ssn_mask masking policy -- (optional)
grant apply on masking policy ssn_mask to role table_owner;
```

The next step is to create the masking policy functions.

```sql
 -- default mask
create or replace masking policy default_mask as (val string) returns string ->
case
when current_role() in ('ANALYST') then val
else 'xxxx'
end;

-- partial mask
create or replace masking policy partial_mask as (val string) returns string ->
case
when current_role() in ('ANALYST') then val
else LEFT(val,1) || 'xxxxx' || RIGHT(val,1)
end;

-- email mask
create or replace masking policy email_mask as (val string) returns string ->
case
when current_role() in ('ANALYST') then val
else LEFT(val,1) || 'XXX@XXX.com'
end;

-- random mask
create or replace masking policy random_mask as (val smallint) returns smallint ->
case
when current_role() in ('ANALYST') then val
else UNIFORM(1,100,RANDOM())::SMALLINT
end;
```

> **Note:**
>
> For sample purposes, we are taking some examples of masking functions in SQL Server, and manually translating it into its equivalent in Snowflake.

The final step is to add the masking policy to the column that originally had the masking option in SQL Server.

```sql
 alter table if exists TABLE1 modify column COL1 set masking policy default_mask;
alter table if exists TABLE1 modify column COL2 set masking policy partial_mask;
alter table if exists TABLE1 modify column COL3 set masking policy email_mask;
alter table if exists TABLE1 modify column COL4 set masking policy random_mask;
```

If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0023

Bulk option not supported

### Severity

Low

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI is added when some option in a `BULK INSERT` could not be mapped. The translated bulk options should be reflected as `FILE FORMAT` options.

#### Code Example

##### Input Code

```sql
 BULK INSERT #PCE FROM 'E:\PCE_Look-up_table.txt'
WITH
(
   FIELDTERMINATOR ='\t',
   ROWTERMINATOR ='\n',
   FIRE_TRIGGERS
);
```

##### Generated Code

```sql
 CREATE OR REPLACE FILE FORMAT FILE_FORMAT_638461199649565070
FIELD_DELIMITER = '\t'
RECORD_DELIMITER = '\n'
!!!RESOLVE EWI!!! /*** SSC-EWI-TS0023 - 'FIRE_TRIGGERS' BULK OPTION COULD NOT BE TRANSFORMED TO ANY OF THE EXISTING FILE FORMAT OPTIONS ***/!!!
FIRE_TRIGGERS;

CREATE OR REPLACE STAGE STAGE_638461199649565070
FILE_FORMAT = FILE_FORMAT_638461199649565070;

--** SSC-FDM-TS0004 - PUT STATEMENT IS NOT SUPPORTED ON WEB UI. YOU SHOULD EXECUTE THE CODE THROUGH THE SNOWFLAKE CLI **
PUT file://E:\PCE_Look-up_table.txt @STAGE_638461199649565070 AUTO_COMPRESS = FALSE;

COPY INTO T_PCE FROM @STAGE_638461199649565070/PCE_Look-up_table.txt;
```

#### Best Practices

* Visit the SnowSQL CLI [user guide](https://docs.snowflake.com/en/user-guide/snowsql.html).
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

### Related EWI

1. [SSC-FDM-TS0004](../functional-difference/sqlServerFDM.md): PUT statement not supported on UI.

## SSC-EWI-TS0024

Incomplete transformation for Bulk Insert

### Severity

Low

#### Description

This EWI is added when a `BULK INSERT` inside a stored procedure was not identified at all, so the dependencies for the complete transformation will not be generated. Also the transformed `COPY INTO` retrieves the file from a `tempStage` that needs to be created manually.

#### Code Example

##### Input Code

```sql
 CREATE PROCEDURE BULK_PROC2
AS
BULK INSERT dbo.table1 FROM 'E:\test.txt'
WITH
(
   FIELDTERMINATOR ='\t',
   ROWTERMINATOR ='\n'
);

GO
```

##### Generated Code

```sql
 CREATE OR REPLACE FILE FORMAT FILE_FORMAT_638461207064166040
FIELD_DELIMITER = '\t'
RECORD_DELIMITER = '\n';

CREATE OR REPLACE STAGE STAGE_638461207064166040
FILE_FORMAT = FILE_FORMAT_638461207064166040;

--** SSC-FDM-TS0004 - PUT STATEMENT IS NOT SUPPORTED ON WEB UI. YOU SHOULD EXECUTE THE CODE THROUGH THE SNOWFLAKE CLI **
PUT file://E:\test.txt @STAGE_638461207064166040 AUTO_COMPRESS = FALSE;

CREATE OR REPLACE PROCEDURE BULK_PROC2 ()
RETURNS STRING
LANGUAGE JAVASCRIPT
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
   // REGION SnowConvert AI Helpers Code
   // END REGION

   EXEC(`COPY INTO dbo.table1 FROM @STAGE_638461207064166040/test.txt`);
$$
```

#### Best Practices

* To retrieve the file, manually create a [STAGE](https://docs.snowflake.com/en/sql-reference/sql/create-stage.html) and a [FILE FORMAT](https://docs.snowflake.com/en/sql-reference/sql/create-file-format.html).
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0025

ERROR_SEVERITY function transformed

### Severity

Low

> **Note:**
>
> Generate Procedures and Macros using JavaScript as the target language adding the following flag -t JavaScript or –PLTargetLanguage JavaScript

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI is added when [ERROR_SEVERITY](https://docs.microsoft.com/en-us/sql/t-sql/functions/error-severity-transact-sql?view=sql-server-ver15) built-in function is translated. By default, the function will return 16 as it is the most common severity in SQL Server. The generated UDF should retrie

#### Code Example

##### Input Code

```sql
 -- Additional Params: -t JavaScript
CREATE procedure proc1()
as
BEGIN TRY
    -- Generate a divide-by-zero error.
    SELECT 1/0 from table1;
END TRY
BEGIN CATCH
    return ERROR_SEVERITY();
END CATCH;
GO
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE proc1 ()
RETURNS STRING
LANGUAGE JAVASCRIPT
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
    // SnowConvert AI Helpers Code section is omitted.

    try {
        EXEC(`    -- Generate a divide-by-zero error.
    SELECT
       TRUNC( 1/0) from
       table1`);
    } catch(error) {
        return SELECT(`   !!!RESOLVE EWI!!! /*** SSC-EWI-TS0025 - CUSTOM UDF 'ERROR_SEVERITY_UDF' INSERTED FOR ERROR_SEVERITY FUNCTION. ***/!!!
   ERROR_SEVERITY_UDF()`);
    }
$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0026

With Delete Query turned to Create Table.

### Severity

Low

#### Description

This EWI is added when a Common Table Expression With a Delete From is transformed to a Create or Replace Table.

#### Code Example

##### Input Code

```sql
 WITH Duplicated AS (
SELECT *, ROW_NUMBER() OVER (PARTITION BY ID ORDER BY ID) AS RN
FROM WithQueryTest
)
DELETE FROM Duplicated
WHERE Duplicated.RN > 1
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TS0026 - WITH DELETE QUERY TURNED TO CREATE TABLE ***/!!!
CREATE OR REPLACE TABLE WithQueryTest AS
SELECT
*
FROM
WithQueryTest
QUALIFY
ROW_NUMBER()
OVER (PARTITION BY
ID
ORDER BY ID) = 1;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0032

Bulk Insert Partially Translated

> **Warning:**
>
> The EWI is only generated when Javascript is the target language for Stored Procedures. This is a deprecated translation feature, as Snowflake Scripting is the recommended target language for Stored Procedures.

### Severity

High

> **Note:**
>
> Generate Procedures and Macros using JavaScript as the target language adding the following flag -t JavaScript or –PLTargetLanguage JavaScript

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI is added to a literal that was originally a concatenation, when the contained code had a `BULK INSERT` statement. The `PUT` command resulting from the `BULK INSERT` translation is not supported when executing code that was originally Dynamic SQL.

For this reason, the `PUT` command must be extracted from the output code and executed manually outside of the procedure that contains it. Keep in mind that if there are many `BULK INSERT` statements in Dynamic SQL sentences within the procedure, it is advised to split this procedure to be able to manually execute the corresponding `PUT` command for each translated `BULK INSERT`.

#### Code Example

##### Input Code

```sql
 -- Additional Params: -t JavaScript
CREATE PROCEDURE  [dbo].[Load_FuelMgtMasterData]
AS
    BEGIN
        SET NOCOUNT ON;

        DECLARE
            @SQLString VARCHAR(500)
        ,   @ImportName VARCHAR(200)
        ,   @Today DATE
        ,   @Yesterday DATE
        ,   @SourceAffiliates VARCHAR(200);

        SET @Today = GETDATE();
        SET @Yesterday = DATEADD(DAY, -1, @Today);
        TRUNCATE TABLE dbo.SourceFM_Affiliates;
        SET @ImportName = '\\' + +@@ServerName
            + '\WorkA\merchantportal\affiliates.txt';
        SET @SQLString = 'BULK INSERT ' + @SourceAffiliates + ' FROM '''
            + @ImportName + '''';
        EXEC (@SQLString);
    END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE dbo.Load_FuelMgtMasterData ()
RETURNS STRING
LANGUAGE JAVASCRIPT
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
    // SnowConvert AI Helpers Code section is omitted.

    /*** SSC-EWI-0040 - THE 'SET' CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/
    /*        SET NOCOUNT ON*/
    ;
    let SQLSTRING;
    let IMPORTNAME;
    let TODAY;
    let YESTERDAY;
    let SOURCEAFFILIATES;
    TODAY = SELECT(`   CURRENT_TIMESTAMP() :: TIMESTAMP`);
    YESTERDAY = SELECT(`   DATEADD(DAY, -1, ?)`,[TODAY]);
    EXEC(`        TRUNCATE TABLE dbo.SourceFM_Affiliates`);
    IMPORTNAME = `\\` + SERVERNAME + `\WorkA\merchantportal\affiliates.txt`;
    SQLSTRING =
        // ** SSC-EWI-TS0032 - THE BULK INSERT WAS PART OF A DYNAMIC SQL, WHICH MAKES SOME OF THE TRANSLATED ELEMENTS INVALID UNLESS EXECUTED OUTSIDE DYNAMIC CODE. **
        `CREATE OR REPLACE FILE FORMAT FILE_FORMAT_638923328992788100;

CREATE OR REPLACE STAGE STAGE_638923328992788100
FILE_FORMAT = FILE_FORMAT_638923328992788100;

PUT file://${IMPORTNAME} @STAGE_638923328992788100 AUTO_COMPRESS = FALSE;

COPY INTO ${SOURCEAFFILIATES}
FROM @STAGE_638923328992788100/${IMPORTNAME}`;
    EXEC(`${SQLSTRING}`);
$$;
```

#### Best Practices

* Extract the `PUT` command that resulted from the Dynamic `BULK INSERT` statement, and execute it before calling the procedure.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0034

RETURNS clause incomplete due to missing symbols

### Severity

High

#### Description

This EWI is added to the output code when the `RETURNS TABLE` clause of a `CREATE FUNCTION` could not be properly generated. This happens when the columns that must be specified in the resulting `RETURNS TABLE` clause cannot be inferred by SnowConvert AI, thus leaving the `RETURNS TABLE` clause empty.

#### Code Example

##### Input Code

```sql
 CREATE FUNCTION Sales.ufn_SalesByStore2()
RETURNS TABLE
AS
RETURN
(
  WITH CTE AS (
  SELECT DepartmentID, Name, GroupName
  FROM HumanResources.Department
  )
  SELECT tab.* FROM CTE tab
);

GO

SELECT * FROM GetDepartmentInfo();
```

##### Generated Code

```sql
 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "HumanResources.Department" **
CREATE OR REPLACE FUNCTION Sales.ufn_SalesByStore2 ()
RETURNS TABLE(
  DepartmentID STRING /*** SSC-FDM-TS0012 - INFORMATION FOR THE COLUMN DepartmentID WAS NOT FOUND. STRING DATATYPE USED TO MATCH CAST AS STRING OPERATION ***/,
  Name STRING /*** SSC-FDM-TS0012 - INFORMATION FOR THE COLUMN Name WAS NOT FOUND. STRING DATATYPE USED TO MATCH CAST AS STRING OPERATION ***/,
  GroupName STRING /*** SSC-FDM-TS0012 - INFORMATION FOR THE COLUMN GroupName WAS NOT FOUND. STRING DATATYPE USED TO MATCH CAST AS STRING OPERATION ***/
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
AS
$$
  --** SSC-PRF-TS0001 - PERFORMANCE WARNING - RECURSION FOR CTE NOT CHECKED. MIGHT REQUIRE RECURSIVE KEYWORD **
    WITH CTE AS (
    SELECT
      DepartmentID,
      Name,
      GroupName
    FROM
      HumanResources.Department
    )
    SELECT tab.* FROM
    CTE tab
$$;

--** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "GetDepartmentInfo" **

SELECT
    *
FROM
    TABLE(GetDepartmentInfo());
```

#### Best Practices

* The causes for this issue may vary. Be sure to include all the objects that your code needs. If the issue persists even though the migration has access to all the necessary objects, please do contact us with information about your specific scenario.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0035

Declaring a Cursor Variable that it is never initialized is not supported.

### Severity

Medium

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

Currently, a Cursor Variable that is declared but never initialized is not supported by Snowflake. Thus, the EWI is added, and the code commented out.

#### Code Example

##### Input Code

```sql
 CREATE OR ALTER PROCEDURE notInitializedCursorTest
AS
BEGIN
    -- Should be marked with SSC-EWI-TS0035
    DECLARE @MyCursor CURSOR, @MyCursor2 CURSOR;
    -- Should not be marked
    DECLARE cursorVar CURSOR FORWARD_ONLY STATIC READ_ONLY
        FOR
        SELECT someCol
        FROM someTable;
    RETURN 'DONE';
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE notInitializedCursorTest ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        -- Should be marked with SSC-EWI-TS0035
        !!!RESOLVE EWI!!! /*** SSC-EWI-TS0035 - CURSOR VARIABLE DECLARED BUT NEVER INITIALIZED, THIS IS NOT SUPPORTED IN SNOWFLAKE SCRIPTING ***/!!!
        MYCURSOR CURSOR;
        !!!RESOLVE EWI!!! /*** SSC-EWI-TS0035 - CURSOR VARIABLE DECLARED BUT NEVER INITIALIZED, THIS IS NOT SUPPORTED IN SNOWFLAKE SCRIPTING ***/!!!
        MYCURSOR2 CURSOR;
        -- Should not be marked
        cursorVar CURSOR
        FOR
            SELECT
                someCol
            FROM
                someTable;
    BEGIN

        RETURN 'DONE';
    END;
$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0036

Snowflake Scripting only supports Local Cursors.

### Severity

Medium

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI is added when Cursors other than Local Cursors are identified. Currently, Snowflake Scripting only supports Local Cursors. Thus, all Cursors are translated as Local Cursors.

#### Code Example

##### Input Code

```sql
 CREATE OR ALTER PROCEDURE globalCursorTest
AS
BEGIN
    -- Should be marked with SSC-EWI-TS0036
    DECLARE MyCursor CURSOR GLOBAL STATIC READ_ONLY
        FOR
        SELECT *
        FROM exampleTable;
    -- Should not be marked
    DECLARE MyCursor2 CURSOR LOCAL STATIC READ_ONLY
        FOR
        SELECT testCol
        FROM myTable;
    RETURN 'DONE';
END;
```

```sql
 CREATE OR REPLACE PROCEDURE globalCursorTest ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        -- Should be marked with SSC-EWI-TS0036
        !!!RESOLVE EWI!!! /*** SSC-EWI-TS0036 - SNOWFLAKE SCRIPTING ONLY SUPPORTS LOCAL CURSORS ***/!!!
        MyCursor CURSOR
        FOR
            SELECT
                *
            FROM
                exampleTable;
        -- Should not be marked
        MyCursor2 CURSOR
        FOR
            SELECT
                testCol
            FROM
                myTable;
    BEGIN

        RETURN 'DONE';
    END;
$$;
```

```sql

```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0037

Snowflake Scripting Cursors are non-scrollable.

### Severity

Medium

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

Snowflake Scripting Cursors are non-scrollable. Currently, only FETCH NEXT is supported.

#### Code Example

##### Input Code

```sql
 CREATE OR ALTER PROCEDURE scrollablecursorTest
AS
BEGIN
    -- Should be marked with SSC-EWI-TS0037
    DECLARE CursorVar CURSOR SCROLL STATIC READ_ONLY
 FOR
 SELECT FirstName
 FROM vEmployee;
    -- Should not be marked
    DECLARE CursorVar2 CURSOR STATIC READ_ONLY
 FOR
 SELECT FirstName
 FROM vEmployee;
    DECLARE CursorVar3 CURSOR FORWARD_ONLY STATIC READ_ONLY
 FOR
 SELECT FirstName
 FROM vEmployee;
    RETURN 'DONE';
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE scrollablecursorTest ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
 DECLARE
  -- Should be marked with SSC-EWI-TS0037
  !!!RESOLVE EWI!!! /*** SSC-EWI-TS0037 - SNOWFLAKE SCRIPTING CURSORS ARE NON-SCROLLABLE, ONLY FETCH NEXT IS SUPPORTED ***/!!!
  CursorVar CURSOR
  FOR
   SELECT
    FirstName
   FROM
    vEmployee;
  -- Should not be marked
  CursorVar2 CURSOR
  FOR
   SELECT
    FirstName
   FROM
    vEmployee;
  CursorVar3 CURSOR
  FOR
   SELECT
    FirstName
   FROM
    vEmployee;
 BEGIN

  RETURN 'DONE';
 END;
$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0039

Multiple SET Statements for the same cursor found.

### Severity

Medium

#### Description

This EWI is added when multiple SET Statements for the same cursor are found; All additional SET Statements are also commented out. This happens because having multiple SET Statements for the same cursor is not valid in Snowflake Scripting.

#### Example Code

##### This EWI is added when multiple SET Statements for the same cursor are found; All additional SET Statements are also commented out. This happens because having multiple SET Statements for the same cursor is not valid in Snowflake Scripting

#### Example Code

##### Input Code

```sql
 CREATE OR ALTER PROCEDURE multipleSetExample
AS
BEGIN
    DECLARE @MyCursor CURSOR;
    DECLARE @MyCursor2 CURSOR STATIC READ_ONLY
 FOR
 SELECT FirstName
 FROM vEmployee;
    DECLARE @MyCursor3 CURSOR;

    SET @MyCursor = CURSOR STATIC READ_ONLY
        FOR
        SELECT col3
        FROM defaultTable;

    SET @MyCursor3 = CURSOR STATIC READ_ONLY
    FOR
    SELECT *
    FROM someTable;

    SET @MyCursor = CURSOR DYNAMIC
        FOR
        SELECT col2
        FROM exampleTable;

    SET @MyCursor2 = CURSOR STATIC READ_ONLY
        FOR
        SELECT col3
        FROM defaultTable;

    RETURN 'DONE';
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE multipleSetExample ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
 DECLARE
  MYCURSOR CURSOR
  FOR
   SELECT col3
   FROM defaultTable;
  MYCURSOR2 CURSOR
  FOR
   SELECT
    FirstName
   FROM
    vEmployee;
  MYCURSOR3 CURSOR
  FOR
   SELECT *
   FROM someTable;
 BEGIN

  DECLARE
  MYCURSOR CURSOR
  FOR
   SELECT col3
   FROM defaultTable;
  MYCURSOR2 CURSOR
  FOR
   SELECT
    FirstName
   FROM
    vEmployee;
  MYCURSOR3 CURSOR
  FOR
   SELECT *
   FROM someTable;
 BEGIN

  !!!RESOLVE EWI!!! /*** SSC-EWI-0040 - THE 'SET CURSOR' CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!!!!RESOLVE EWI!!! /*** SSC-EWI-TS0039 - CURSOR VARIABLE MYCURSOR SET MULTIPLE TIMES, THIS IS NOT VALID IN SNOWFLAKE SCRIPTING ***/!!!

  SET @MyCursor = CURSOR DYNAMIC
      FOR
      SELECT col2
      FROM exampleTable;
  !!!RESOLVE EWI!!! /*** SSC-EWI-0040 - THE 'SET CURSOR' CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!!!!RESOLVE EWI!!! /*** SSC-EWI-TS0039 - CURSOR VARIABLE MYCURSOR2 SET MULTIPLE TIMES, THIS IS NOT VALID IN SNOWFLAKE SCRIPTING ***/!!!

    SET @MyCursor2 = CURSOR STATIC READ_ONLY
        FOR
        SELECT col3
        FROM defaultTable;
  RETURN 'DONE';
 END;
$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0041

XML data type methods are not supported in Snowflake.

### Severity

Medium

#### Description

This EWI is added for the following [XML data type methods](https://docs.microsoft.com/en-us/sql/t-sql/xml/xml-data-type-methods?view=sql-server-ver15) that are not supported in Snowflake SQL:

* Value
* Query
* Exist
* Modify
* Nodes

#### Code Example

##### Input Code

```sql
 CREATE PROCEDURE xml_procedure
    @inUserGroupsXML XML
AS
BEGIN
    SELECT  entities.entity.value('TypeID[1]', 'VARCHAR(100)') AS TypeID
        ,entities.entity.value('Name[1]', 'VARCHAR(100)') AS Name
    INTO  #tmpUserGroups
    FROM  @inUserGroupsXML.nodes('/entities/entity') entities(entity)
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE xml_procedure (INUSERGROUPSXML TEXT)
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
    BEGIN
        CREATE OR REPLACE TEMPORARY TABLE T_tmpUserGroups AS
            SELECT
                XMLGET(entity, '$') :: VARCHAR(100) AS TypeID
                ,
                XMLGET(entity, '$') :: VARCHAR(100) AS Name
            FROM
                !!!RESOLVE EWI!!! /*** SSC-EWI-TS0041 - XML TYPE METHOD nodes IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
                T_inUserGroupsXML('/entities/entity') entities (
                    entity
                );
    END;
$$;
```

#### Best Practices

* Consider using UDFs to emulate the behavior of the source code
* You can [check this documentation](https://medium.com/snowflake/working-with-xml-in-snowflake-part-ii-774b4d32399) and review some possible approaches to work with XML datatypes in Snowflake.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0043

WITH XMLNAMESPACES is not supported in Snowflake.

### Severity

Medium

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI is added fort the [WITH XMLNAMESPACES](https://docs.microsoft.com/en-us/sql/relational-databases/xml/add-namespaces-to-queries-with-with-xmlnamespaces?view=sql-server-ver15) clause which is not supported in Snowflake SQL

#### Code Example

##### Input Code

```sql
 WITH XMLNAMESPACES ('uri' as ns1)
SELECT ProductID as 'ns1:ProductID',
Name      as 'ns1:Name',
Color     as 'ns1:Color'
FROM Production.Product
WHERE ProductID = 316
FOR XML RAW, ELEMENTS XSINIL
```

##### Generated Code

```sql
 --** SSC-PRF-TS0001 - PERFORMANCE WARNING - RECURSION FOR CTE NOT CHECKED. MIGHT REQUIRE RECURSIVE KEYWORD **
WITH
     !!!RESOLVE EWI!!! /*** SSC-EWI-TS0043 - WITH XMLNAMESPACES IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
 XMLNAMESPACES ('uri' as VARIANT !!!RESOLVE EWI!!! /*** SSC-EWI-TS0015 - DATA TYPE NS1 IS NOT SUPPORTED IN SNOWFLAKE ***/!!! NOT NULL)
SELECT
ProductID AS "ns1:ProductID",
Name AS "ns1:Name",
Color AS "ns1:Color"
FROM
Production.Product
WHERE
ProductID = 316
!!!RESOLVE EWI!!! /*** SSC-EWI-TS0044 - FOR XML RAW CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
FOR XML RAW, ELEMENTS XSINIL;
```

#### Best Practices

* Consider using UDFs to emulate the behavior of the source code. The following code provides suggestions of UDFs that can be used to achieve recreating the original behavior:

##### SQL Server

```sql
 CREATE  TABLE PRODUCT (ProductID INTEGER, Name VarChar(20), Color VarChar(20));
INSERT INTO PRODUCT(PRODUCTID, NAME, COLOR) VALUES(1,'UMBRELLA','RED');
INSERT INTO PRODUCT(PRODUCTID, NAME, COLOR) VALUES(2,'SHORTS','BLUE');
INSERT INTO PRODUCT(PRODUCTID, NAME, COLOR) VALUES(3,'BALL','YELLOW');

WITH XMLNAMESPACES ('uri' as ns1)
SELECT ProductID as 'ns1:ProductID',
       Name      as 'ns1:Name',
       Color     as 'ns1:Color'
FROM Product
FOR XML RAW
```

##### Snowflake SQL

```sql
 CREATE OR REPLACE TABLE PRODUCT (
       ProductID INTEGER,
       Name VARCHAR(20),
       Color VARCHAR(20))
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "07/12/2024" }}'
;

INSERT INTO PRODUCT (PRODUCTID, NAME, COLOR) VALUES(1,'UMBRELLA','RED');
INSERT INTO PRODUCT (PRODUCTID, NAME, COLOR) VALUES(2,'SHORTS','BLUE');
INSERT INTO PRODUCT (PRODUCTID, NAME, COLOR) VALUES(3,'BALL','YELLOW');

--** SSC-PRF-TS0001 - PERFORMANCE WARNING - RECURSION FOR CTE NOT CHECKED. MIGHT REQUIRE RECURSIVE KEYWORD **

WITH
     !!!RESOLVE EWI!!! /*** SSC-EWI-TS0043 - WITH XMLNAMESPACES IS NOT SUPPORTED IN SNOWFLAKE ***/!!! XMLNAMESPACES ('uri' as ns1)
SELECT
       ProductID AS "ns1:ProductID",
       Name AS "ns1:Name",
       Color AS "ns1:Color"
FROM
       Product
!!!RESOLVE EWI!!! /*** SSC-EWI-TS0044 - FOR XML RAW CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
FOR XML RAW;
```

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

### Related EWI

1. [SSC-PRF-TS0001](../performance-review/sqlServerPRF.md): Performance warning - recursion for CTE not checked. Might require a recursive keyword.
2. SSC-EWI-TS0044: FOR XML clause is not supported in Snowflake.
3. SSC-EWI-TS0015: Data type not supported in Snowflake

## SSC-EWI-TS0044

FOR XML clause is not supported in Snowflake.

### Severity

Critical

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI is added for the [FOR XML](https://docs.microsoft.com/en-us/sql/relational-databases/xml/for-xml-sql-server?view=sql-server-ver15) clause which is not supported in Snowflake SQL

#### Code Example

##### Input Code

```sql
 SELECT TOP 1 LastName
FROM AdventureWorks2019.Person.Person
FOR XML AUTO;
```

##### Generated Code

```sql
 SELECT TOP 1
LastName
FROM
AdventureWorks2019.Person.Person
!!!RESOLVE EWI!!! /*** SSC-EWI-TS0044 - FOR XML AUTO CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
FOR XML AUTO;
```

#### Best Practices

* Consider using UDFs to emulate the behavior of the source code. The following code provides suggestions of UDFs that can be used to achieve recreating the original behavior:

SQL Server

##### Query

```sql
 CREATE TABLE TEMPTABLE (Ref INT, Des NVARCHAR(100), Qty INT)

INSERT INTO tempTable VALUES (100001, 'Normal', 1), (100002, 'Foobar', 1), (100003, 'Hello World', 2)

GO

-- FOR XML
SELECT *
FROM TempTable
FOR XML AUTO

GO

-- FOR XML RAW
SELECT *
FROM TempTable
FOR XML RAW
```

##### Result

```sql
 -- FOR XML
<TempTable Ref="100001" Des="Normal" Qty="1"/><TempTable Ref="100002" Des="Foobar" Qty="1"/><TempTable Ref="100003" Des="Hello World" Qty="2"/>

-- FOR XML RAW
<row Ref="100001" Des="Normal" Qty="1"/><row Ref="100002" Des="Foobar" Qty="1"/><row Ref="100003" Des="Hello World" Qty="2"/>
```

##### *Snowflake*

##### Query

```sql
 CREATE OR REPLACE TABLE TEMPTABLE (
Ref INT,
Des VARCHAR(100),
Qty INT
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
;

INSERT INTO tempTable VALUES (100001, 'Normal', 1), (100002, 'Foobar', 1), (100003, 'Hello World', 2);

-- FOR XML
SELECT
*
FROM
TempTable
!!!RESOLVE EWI!!! /*** SSC-EWI-TS0044 - FOR XML AUTO CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
FOR XML AUTO;

-- FOR XML RAW
SELECT
*
FROM
TempTable
!!!RESOLVE EWI!!! /*** SSC-EWI-TS0044 - FOR XML RAW CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
FOR XML RAW;
```

##### Result

```sql
 -- FOR XML
<TempTable DES="Normal" QTY="1" REF="100001"  /><TempTable DES="Foobar" QTY="1" REF="100002"  /><TempTable DES="Hello World" QTY="2" REF="100003"  />

-- FOR XML RAW
<row DES="Normal" QTY="1" REF="100001"  /><row DES="Foobar" QTY="1" REF="100002"  /><row DES="Hello World" QTY="2" REF="100003"  />
```

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0045

Labeled Statement is not supported in Snowflake Scripting.

### Severity

Low

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI is added for all the LABELS used with the [GOTO](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/goto-transact-sql?view=sql-server-ver15) statement in SQL Server.

#### Code Example

##### Input Code

```sql
 CREATE PROCEDURE GoToProcedure
AS
BEGIN
DECLARE @TotalMaarks INT
SET @TotalMaarks = 49
IF @TotalMaarks >= 50
    GOTO Pass
IF @TotalMaarks < 50
    GOTO Fail
Pass:
    SELECT 1;
    SELECT * FROM TABLE1;
    RETURN 1;
Fail:
    SELECT 2;
    SELECT * FROM TABLE2;
    RETURN 2;
END
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE GoToProcedure ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        TOTALMAARKS INT;
    BEGIN

        TOTALMAARKS := 49;
        IF (:TOTALMAARKS >= 50) THEN
            !!!RESOLVE EWI!!! /*** SSC-EWI-0073 - PENDING FUNCTIONAL EQUIVALENCE REVIEW FOR 'GOTO' NODE ***/!!!
            GOTO Pass
        END IF;
        IF (:TOTALMAARKS < 50) THEN
            !!!RESOLVE EWI!!! /*** SSC-EWI-0073 - PENDING FUNCTIONAL EQUIVALENCE REVIEW FOR 'GOTO' NODE ***/!!!
            GOTO Fail
        END IF;
        !!!RESOLVE EWI!!! /*** SSC-EWI-TS0045 - LABELED STATEMENT IS NOT SUPPORTED IN SNOWFLAKE SCRIPTING ***/!!!
        Pass:
        SELECT 1;
    SELECT
            *
        FROM
            TABLE1;
        RETURN 1;

        !!!RESOLVE EWI!!! /*** SSC-EWI-TS0045 - LABELED STATEMENT IS NOT SUPPORTED IN SNOWFLAKE SCRIPTING ***/!!!
        Fail:
        SELECT 2;
    SELECT
            *
        FROM
            TABLE2;
        RETURN 2;

    END;
$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

### Related EWI

1. [SSC-EWI-0073](generalEWI.md): Pending Functional Equivalence Review.

## SSC-EWI-TS0046

System table is not supported in Snowflake.

### Severity

Medium

#### Description

This EWI is added when referencing [SQL Server system tables](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/object-catalog-views-transact-sql?view=sql-server-ver15) not supported or without equivalent in Snowflake SQL. See the [supported and unsupported system tables reference](../../../../translation-references/transact/transact-system-tables.md) for the complete list.

#### Code Example

##### Input Code

```sql
 SELECT *
FROM
    sys.all_sql_modules
WHERE
    [STATE] = 0; -- state must be ONLINE
```

##### Generated Code

```sql
 SELECT
    *
FROM
    !!!RESOLVE EWI!!! /*** SSC-EWI-TS0046 - SYSTEM TABLE sys.all_sql_modules IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
    sys.all_sql_modules
WHERE
    STATE = 0; -- state must be ONLINE
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0047

RAISERROR Error Message may differ because of the SQL Server string format.

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-TS0019](../functional-difference/sqlServerFDM.md) documentation

### Severity

Low

#### Description

This EWI is added to notify that the RAISERROR Error Message may differ because of the SQL Server string format.

#### Code Example

##### Input Code

```sql
 CREATE PROCEDURE RAISERROR_PROCEDURE
AS
BEGIN
RAISERROR ('This is a sample error message with the first parameter %d and the second parameter %*.*s',
           10,
           1,
           123,
    7,
    7,
    'param2');
END
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE RAISERROR_PROCEDURE ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
 BEGIN
  !!!RESOLVE EWI!!! /*** SSC-EWI-TS0047 - RAISERROR ERROR MESSAGE MAY DIFFER BECAUSE OF THE SQL SERVER STRING FORMAT ***/!!!
  SELECT
   RAISERROR_UDF('This is a sample error message with the first parameter %d and the second parameter %*.*s',
   10,
   1, array_construct(
   123,
7,
7,
'param2'));
 END;
$$;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0049

Multiple Line If Body translation planned to be delivered in the future.

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Severity

Medium

#### Description

Most of the cases in`IF` statements that contain a `Begin ... End` block inside their body are supported. This is a successful scenario (no SSC-EWI-TS0049 generated).

#### Code Example

##### Input Code

```sql
 CREATE OR ALTER FUNCTION [PURCHASING].[FOO](@status INT)
Returns INT
As
Begin
    declare @result as int = 10;
    SELECT @result = quantity FROM TABLE1 WHERE COL1 = @status;
    IF @result = 3
    BEGIN
        IF @result>0 SELECT @result=0  ELSE SELECT @result=1
        SELECT @result = 1
    END
    return @result;
End
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-0068 - USER DEFINED FUNCTION WAS TRANSFORMED TO SNOWFLAKE PROCEDURE ***/!!!
--** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "TABLE1" **
CREATE OR REPLACE PROCEDURE PURCHASING.FOO (STATUS INT)
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "07/14/2025",  "domain": "no-domain-provided" }}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        RESULT INT := 10;
    BEGIN

        SELECT
            quantity
        INTO
            :RESULT
        FROM
            TABLE1
        WHERE
            COL1 = :STATUS;
        IF (:RESULT = 3) THEN
            BEGIN
                IF (:RESULT >0) THEN SELECT
                        0
                    INTO
                        :RESULT;
                ELSE
                    SELECT
                        1
                    INTO
                        :RESULT;
                END IF;
        SELECT
                    1
                INTO
                    :RESULT;
            END;
        END IF;
        RETURN :RESULT;
    END;
$$;
```

> **Note:**
>
> In a general code example (Like the on top) the conversion is done successfully. But there are some edge cases where the “IF” statement is not converted and the EWI will be generated.

#### Manual Support

##### Case 1: Single Statement

For these cases, the transformation would be straightforward, since the transformed statement would appear in a select clause

```sql
 IF @result = 0
BEGIN
    SET @result =1
END
```

```sql
 CASE WHEN (SELECT RESULT FROM CTE2)= 0 THEN
( SELECT 1 AS RESULT )
```

##### Case 2: Multiple Statements

For cases in which multiple statements are being transformed, we should transform the N Statement, and use it as the source table for the N+1 Statement.

```sql
 IF @result = 0
BEGIN
    Statement1
    Statement2
    Statement3
END
```

```sql
 CASE WHEN (SELECT RESULT FROM CTE2)= 0 THEN
(
    SELECT TransformedStatement3
    FROM (
        SELECT TransformedStatement2
        FROM (
            SELECT TransformedStatement1
        ) T1
    ) T2
)
```

##### Case 3: Multiple set statements

For these cases, it will be necessary to replicate a transformation for each set statement.

```sql
 IF @result = 0
BEGIN
    SET @var1 = 1
    SET @var2 = 3
    SET @var3 = @var2
END
```

```sql
 WITH CTE1 AS (
    SELECT
        CASE WHEN (SELECT
                        RESULT
                    FROM
                        CTE0) = 0 THEN
        (SELECT 1) AS VAR1)
WITH CTE2 AS (
    SELECT
        CASE WHEN (SELECT
                        RESULT
                    FROM
                        CTE0)= 0 THEN
        (SELECT 3) AS VAR2)
WITH CTE3 AS (
    SELECT
        CASE WHEN (SELECT
                        RESULT
                    FROM
                        CTE0)= 0 THEN
        (SELECT T1.VAR2
        FROM ((SELECT 3) AS VAR2) AS T1) AS VAR3)
...
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0055

Default constraint was commented out and may have been added to a table definition.

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-TS0020](../functional-difference/sqlServerFDM.md) documentation.

### Severity

Medium

#### Description

This EWI is added when the default constraint is present in an Alter Table statement.

Currently, there is no support for that constraint. A workaround available to transform it, is when the table is previously defined to the Alter Table, in this way we identify the references, and the default constraint is unified on the table definition; otherwise, the constraint is only commented out.

#### Code Example

##### Input Code

```sql
 CREATE TABLE table1(
  col1 integer,
  col2 varchar collate Latin1_General_CS,
  col3 date
);

ALTER TABLE table1
ADD col4 integer,
  CONSTRAINT col1_constraint DEFAULT 50 FOR col1,
  CONSTRAINT col1_constraint DEFAULT 30 FOR col1;
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE table1 (
  col1 INTEGER DEFAULT 50,
  col2 VARCHAR COLLATE 'EN-CS',
  col3 DATE
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
;

ALTER TABLE table1
ADD col4 INTEGER,
  CONSTRAINT col1_constraint
                             !!!RESOLVE EWI!!! /*** SSC-EWI-TS0055 - DEFAULT CONSTRAINT MAY HAVE BEEN ADDED TO TABLE DEFINITION ***/!!!
                             DEFAULT 50 FOR col1,
  CONSTRAINT col1_constraint
                             !!!RESOLVE EWI!!! /*** SSC-EWI-TS0055 - DEFAULT CONSTRAINT MAY HAVE BEEN ADDED TO TABLE DEFINITION ***/!!!
                             DEFAULT 30 FOR col1;
```

> **Note:**
>
> If all the content of the Alter Table is invalid, the Alter Table will be commented out.

#### Known Issues

When different default constraints are declared over the same column, only the first will be reflected on the Create Table Statement.

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0056

A MASKING POLICY was created as a substitute for MASKED WITH.

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-TS0021](../functional-difference/sqlServerFDM.md) documentation

### Severity

Low

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI is added when the Alter Table statement contains a MASKED WITH clause. The reason this is added is to inform that an approximate MASKING POLICY was created as a substitute for the MASKED WITH function.

#### Code Example

##### Input Code

```sql
 ALTER TABLE table_name
ALTER COLUMN column_name
ADD MASKED WITH (FUNCTION = 'default()');
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TS0057 - MASKING ROLE MUST BE DEFINED PREVIOUSLY BY THE USER ***/!!!
CREATE OR REPLACE MASKING POLICY "default" AS
(val STRING)
RETURNS STRING ->
CASE
WHEN current_role() IN ('YOUR_DEFINED_ROLE_HERE')
THEN val
ELSE 'xxxxx'
END;

ALTER TABLE IF EXISTS table_name MODIFY COLUMN column_name!!!RESOLVE EWI!!! /*** SSC-EWI-TS0056 - A MASKING POLICY WAS CREATED AS SUBSTITUTE FOR MASKED WITH ***/!!!  SET MASKING POLICY "default";
```

> **Note:**
>
> The MASKING POLICY will be created previous to the ALTER TABLE statement. And it is expected to have and approximate behaviour. Some tweaks might be needed in regards to roles and user privileges. <!– TODO: You can relate to Broken link broken-reference “mention” for further details.>

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0057

The user must previously define the masking role.

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-TS0022](../functional-difference/sqlServerFDM.md) documentation

### Severity

Low

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This is EWI occurs when a MASKING POLICY is created and a role or privilege must be linked to it so the data masking could work properly.

#### Code Example

##### Input code

```sql
 ALTER TABLE tableName
ALTER COLUMN columnName
ADD MASKED WITH (FUNCTION = 'partial(1, "xxxxx", 1)');
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TS0057 - MASKING ROLE MUST BE DEFINED PREVIOUSLY BY THE USER ***/!!!
CREATE OR REPLACE MASKING POLICY "partial_1_xxxxx_1" AS
(val STRING)
RETURNS STRING ->
CASE
WHEN current_role() IN ('YOUR_DEFINED_ROLE_HERE')
THEN val
ELSE LEFT(val, 1) || 'xxxxx' || RIGHT(val, 1)
END;

ALTER TABLE IF EXISTS tableName MODIFY COLUMN columnName!!!RESOLVE EWI!!! /*** SSC-EWI-TS0056 - A MASKING POLICY WAS CREATED AS SUBSTITUTE FOR MASKED WITH ***/!!!  SET MASKING POLICY "partial_1_xxxxx_1";
```

> **Note:**
>
> As shown on line 6, there is a placeholder where the defined roles can be placed. There is room for one or several values separated by commas. Also, here, the use of single quotes is mandatory for each of the values.

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0060

Datetime interval not supported by Snowflake.

### Severity

Medium

#### Description

This EWI is added when one of the following time parts is used as a parameter for a date-related function because they are not supported in Snowflake. For more information go to ‘supported date time parts ([Date & Time Functions | Snowflake Documentation](https://docs.snowflake.com/en/sql-reference/functions-date-time#label-supported-date-time-parts)).

#### Code Example

##### Input code

```sql
 SELECT
    -- Supported
    DATEPART(second, getdate()),
    -- Not supported
    DATEPART(millisecond, getdate()),
    DATEPART(microsecond, getdate());
```

##### Generated Code

```sql
 SELECT
    -- Supported
    DATE_PART(second, CURRENT_TIMESTAMP() :: TIMESTAMP),
    -- Not supported
    !!!RESOLVE EWI!!! /*** SSC-EWI-TS0060 - TIME PART 'millisecond' NOT SUPPORTED AS A FUNCTION PARAMETER ***/!!!
    DATEPART(millisecond, CURRENT_TIMESTAMP() :: TIMESTAMP),
    !!!RESOLVE EWI!!! /*** SSC-EWI-TS0060 - TIME PART 'microsecond' NOT SUPPORTED AS A FUNCTION PARAMETER ***/!!!
    DATEPART(microsecond, CURRENT_TIMESTAMP() :: TIMESTAMP);
```

#### Best Practices

* An UDF could be created to manually extract unsupported time parts in Snowflake.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0061

ALTER COLUMN not supported

### Severity

Medium

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI is added whenever there is an unsupported ALTER COLUMN statement

#### Code Example

##### Input Code

```sql
 ALTER TABLE SampleTable
ALTER COLUMN SampleColumn INT NULL SPARSE;
```

##### Generated Code

```sql
 ALTER TABLE IF EXISTS SampleTable
ALTER COLUMN SampleColumn
                          !!!RESOLVE EWI!!! /*** SSC-EWI-TS0061 - ALTER COLUMN COMMENTED OUT BECAUSE SPARSE COLUMN IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
                          INT NULL SPARSE;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0063

Time zone not supported in Snowflake.

### Severity

Critical

#### Description

This EWI is added when there are Time zones that are not supported in Snowflake

#### Code Example

##### Input Code

```sql
 SELECT current_timestamp at time zone 'Turks And Caicos Standard Time';
```

##### Generated Code

```sql
 SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-TS0063 - TIME ZONE NOT SUPPORTED IN SNOWFLAKE ***/!!!
CURRENT_TIMESTAMP() at time zone 'Turks And Caicos Standard Time'
                                                                 ;
```

#### Best Practices

* A user defined function can be created to support multiple timezones.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0067

Invalid parameters in OPENXML table-valued function.

### Severity

Critical

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI is added when there are invalid parameters in the OPENXML, specifically when the XML path cannot be accessed.

To avoid this EWI, please send the explicit node path through the parameters.

##### Input Code

```sql
 SELECT
    *
FROM
    OPENXML (@idoc, @path, 1) WITH (
        CustomerID VARCHAR(10),
        ContactName VARCHAR(20)
    );
```

##### Generated Code

```sql
 SELECT
    *
FROM
    !!!RESOLVE EWI!!! /*** SSC-EWI-TS0067 - INVALID PARAMETERS IN OPENXML TABLE-VALUED FUNCTION ***/!!!
    OPENXML(@idoc, @path, 1);
```

##### Input code (Explicit parameter)

```sql
 SELECT
    *
FROM
    OPENXML (@idoc, '/ROOT/Customer', 1) WITH(
        CustomerID VARCHAR(10),
        ContactName VARCHAR(20)
    );
```

##### Generated Code (Explicit parameter)

```sql
 SELECT
    Left(value:Customer['@CustomerID'], '10') AS 'CustomerID',
    Left(value:Customer['@ContactName'], '20') AS 'ContactName'
FROM
    OPENXML_UDF($idoc, ':ROOT:Customer');
```

#### Best Practices

* Try to see if the path can be explicitly passed as a parameter.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0070

CURRENT_TIMESTAMP in At Time Zone statement may have a different behavior in certain cases.

> **Note:**
>
> This `EWI` is deprecated, please refer to [SSC-FDM-TS0024](../functional-difference/sqlServerFDM.md) documentation.

### Description

This EWI is added when the At Time Zone has the CURRENT_TIMESTAMP. This is because the result may have different results in some instances.

The main difference is that in SQL Server, CURRENT_TIMESTAMP returns the current system date and time in the server time zone and in Snowflake CURRENT_TIMESTAMP returns the current date and time in the UTC (Coordinated Universal Time) time zone.

#### Input Code

##### Sql Server

```sql
 SELECT current_timestamp at time zone 'Hawaiian Standard Time';
```

##### Result

`2024-02-08 16:52:55.317 -10:00`

##### Generated Code

##### Snowflake

```sql
 SELECT
CONVERT_TIMEZONE('Pacific/Honolulu', CURRENT_TIMESTAMP() !!!RESOLVE EWI!!! /*** SSC-EWI-TS0070 - CURRENT_TIMESTAMP in At Time Zone statement may have a different behavior in certain cases ***/!!!);
```

##### Result

`2024-02-08 06:53:46.994 -1000`

#### Best Practices

This is an example if you want to keep the same format in Snowflake.

##### SQL Server

```sql
 SELECT current_timestamp at time zone 'Hawaiian Standard Time';
```

##### Result

`2024-02-08 16:33:49.143 -10:00`

In Snowflake you can use [ALTER SESSION](https://docs.snowflake.com/en/sql-reference/sql/alter-session) to change the default time zone. For example:

##### Snowflake

```sql
 ALTER SESSION SET TIMEZONE = 'Pacific/Honolulu';

SELECT
CONVERT_TIMEZONE('Pacific/Honolulu', 'UTC', CURRENT_TIMESTAMP());
```

##### Result

`2024-02-08 16:33:49.143`

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0072

RETURN statement will be ignored due to previous RETURN statement

### Severity

Low

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI is added when SELECT statements and OUPUT parameters should be returned. In this case, the resultsets from the SELECT statements are prioritized.

##### Input Code

```sql
 CREATE PROCEDURE SOMEPROC(@product_count INT OUTPUT,  @123 INT OUTPUT)
AS
BEGIN
  SELECT * from AdventureWorks.HumanResources.Department;
        SELECT * from AdventureWorks.HumanResources.Employee;
END
```

##### Generated Code

```sql
--** SSC-FDM-0007 - MISSING DEPENDENT OBJECTS "AdventureWorks.HumanResources.Department", "AdventureWorks.HumanResources.Employee" **
CREATE OR REPLACE PROCEDURE SOMEPROC (PRODUCT_COUNT OUT INT, _123 OUT INT)
RETURNS ARRAY
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "07/16/2025",  "domain": "no-domain-provided" }}'
EXECUTE AS CALLER
AS
$$
 DECLARE
  ProcedureResultSet1 VARCHAR;
  ProcedureResultSet2 VARCHAR;
  return_arr ARRAY := array_construct();
 BEGIN
  ProcedureResultSet1 := 'RESULTSET_' || REPLACE(UPPER(UUID_STRING()), '-', '_');
  CREATE OR REPLACE TEMPORARY TABLE IDENTIFIER(:ProcedureResultSet1) AS
   SELECT
    *
   from
    AdventureWorks.HumanResources.Department;
  return_arr := array_append(return_arr, :ProcedureResultSet1);
  ProcedureResultSet2 := 'RESULTSET_' || REPLACE(UPPER(UUID_STRING()), '-', '_');
  CREATE OR REPLACE TEMPORARY TABLE IDENTIFIER(:ProcedureResultSet2) AS
   SELECT
    *
   from
    AdventureWorks.HumanResources.Employee;
  return_arr := array_append(return_arr, :ProcedureResultSet2);
  --** SSC-FDM-0020 - MULTIPLE RESULT SETS ARE RETURNED IN TEMPORARY TABLES **
  RETURN return_arr;
 END;
$$;
```

#### Best Practices

* Remove the RETURN statement that should be ignored.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

### Related EWI

1. [SSC-FDM-0020](../functional-difference/generalFDM.md): Multiple result sets are returned in temporary tables;

## SSC-EWI-TS0073

Error message could be different in snowflake

> **Note:**
>
> This EWI is deprecated, please refer to [SSC-FDM-TS0023](../functional-difference/sqlServerFDM.md) documentation

### Severity

Low

#### Description

This EWI is added in the transformation of ERROR_MESSAGE(). The exact message of the error could change in Snowflake.

##### Input Code

```sql
 SET @varErrorMessage = ERROR_MESSAGE()
```

##### Generated Code

```sql
 BEGIN
VARERRORMESSAGE := SQLERRM !!!RESOLVE EWI!!! /*** SSC-EWI-TS0073 - ERROR MESSAGE COULD BE DIFFERENT IN SNOWFLAKE ***/!!!;
END;
```

#### Recommendation

If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com).

## SSC-EWI-TS0074

Cast result may be different from TRY_CAST/TRY_CONVERT function due to missing dependencies

### Severity

Low

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

#### Description

This EWI is added in the transformation of TRY_CAST and TRY_CONVERT functions. The exact result of these functions may change in Snowflake due to missing dependencies (SnowConvert AI couldn’t resolve some data types). This could be because the dependency was not in the source code.

##### Input Code

```sql
 SELECT TRY_CONVERT( INT, col1) FROM TABLE1;

SELECT TRY_CAST(COL1 AS FLOAT) FROM TABLE1
```

##### Generated Code

```sql
 SELECT
CAST(col1 AS INT) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/!!!RESOLVE EWI!!! /*** SSC-EWI-TS0074 - CAST RESULT MAY BE DIFFERENT FROM TRY_CONVERT FUNCTION DUE TO MISSING DEPENDENCIES ***/!!!
FROM
TABLE1;

SELECT
CAST(COL1 AS FLOAT) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/!!!RESOLVE EWI!!! /*** SSC-EWI-TS0074 - CAST RESULT MAY BE DIFFERENT FROM TRY_CAST FUNCTION DUE TO MISSING DEPENDENCIES ***/!!!
FROM
TABLE1;
```

#### Recommendation

If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com).

## SSC-EWI-TS0075

Built In Procedure Not Supported

### Severity

Medium

#### Description

Translation for built-in procedures is not currently supported.

#### Example Code

##### Input Code

```sql
 EXEC sp_column_privileges_rowset_rmt 'Caption';
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TS0075 - TRANSLATION FOR BUILT-IN PROCEDURE 'sp_column_privileges_rowset_rmt' IS NOT CURRENTLY SUPPORTED. ***/!!!
EXEC sp_column_privileges_rowset_rmt 'Caption';
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0076

Default Parameters May Need To Be Reordered

> **Note:**
>
> This EWI is deprecated. SnowConvert AI now automatically reorders default parameters to the end of the parameter list. Please refer to [SSC-FDM-0041](../functional-difference/generalFDM.md) for the updated behavior.

### Severity

Medium

#### Description

Default parameters may need to be reordered. Snowflake only supports default parameters at the end of the parameters declarations.

#### Example Code

##### Input Code

```sql
 CREATE PROCEDURE MySampleProc
    @Param1 NVARCHAR(50) = NULL,
    @Param2 NVARCHAR(10),
    @Param3 NVARCHAR(10) = NULL,
    @Param4 NVARCHAR(10)
AS
    SELECT 1;
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TS0076 - DEFAULT PARAMETERS MAY NEED TO BE REORDERED. SNOWFLAKE ONLY SUPPORTS DEFAULT PARAMETERS AT THE END OF THE PARAMETERS DECLARATIONS. ***/!!!
CREATE OR REPLACE PROCEDURE MySampleProc (PARAM1 STRING DEFAULT NULL, PARAM2 STRING, PARAM3 STRING DEFAULT NULL, PARAM4 STRING)
RETURNS TABLE()
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        ProcedureResultSet RESULTSET;
    BEGIN
        ProcedureResultSet := (
        SELECT 1);
        RETURN TABLE(ProcedureResultSet);
    END;
$$;
```

#### Best Practices

* No end-user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0077

Collation Not Supported

### Severity

Low

#### Description

This message is shown when there is a collate clause that is not supported in Snowflake.

#### Code example

##### Input Code

```sql
 SELECT 'a' COLLATE Albanian_BIN;

SELECT 'a' COLLATE Albanian_CI_AI;

CREATE TABLE ExampleTable (
    ID INT,
    Name VARCHAR(50) COLLATE collateName
);
```

##### Generated Code

```sql
 SELECT 'a'
--           !!!RESOLVE EWI!!! /*** SSC-EWI-TS0077 - COLLATION Albanian_BIN NOT SUPPORTED ***/!!!
-- COLLATE Albanian_BIN
                     ;

SELECT 'a'
--           !!!RESOLVE EWI!!! /*** SSC-EWI-TS0077 - COLLATION Albanian_CI_AI NOT SUPPORTED ***/!!!
-- COLLATE Albanian_CI_AI
                       ;

CREATE OR REPLACE TABLE ExampleTable (
    ID INT,
    Name VARCHAR(50)
--                     !!!RESOLVE EWI!!! /*** SSC-EWI-TS0077 - COLLATION collateName NOT SUPPORTED ***/!!!
-- COLLATE collateName
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"transact"}}'
;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0078

Default value not allowed in Snowflake.

### Severity

Medium

#### Description

This error is added to the code when expressions like function calls, variable names, or named constants follow the default option.

Snowflake only supports explicit constants like numbers or strings.

#### Code Example

##### Input Code

```sql
 ALTER TABLE
    T_ALTERTABLETEST
ADD
    COLUMN COL10 INTEGER DEFAULT RANDOM(10);
```

##### Generated Code

```sql
 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECTS "T_ALTERTABLETEST", "RANDOM" **
ALTER TABLE IF EXISTS T_ALTERTABLETEST
ADD
    COLUMN COL10 INTEGER
                         !!!RESOLVE EWI!!! /*** SSC-EWI-TS0078 - DEFAULT OPTION NOT ALLOWED IN SNOWFLAKE ***/!!!
                         DEFAULT RANDOM(10);
```

#####

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0079

Database console command is not supported

### Severity

Medium

#### Description

This EWI is added when SnowConvert AI finds a DBCC statement inside the input code.
Most DBCC statements are not supported in Snowflake.

#### Code Example

##### Input Code

```sql
 DBCC CHECKIDENT(@a, RESEED, @b) WITH NO_INFOMSGS
```

##### Generated Code

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-TS0079 - DATABASE CONSOLE COMMAND 'CHECKIDENT' IS NOT SUPPORTED. ***/!!!
DBCC CHECKIDENT(@a, RESEED, @b) WITH NO_INFOMSGS;
```

#### Best Practices

* No additional user actions are required; it is just informative.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0080

Changing the execution context at runtime is not supported in Snowflake

### Severity

High

#### Description

Users in SQL Server can use the command `EXECUTE AS` to temporarily change the execution context, this modifies the execution privileges and affects the results of context-dependent functions like `USER_NAME()`. The `REVERT` command can be used to restore the context previous to the last `EXECUTE AS`.

Snowflake only supports the definition of an execution context in procedures, using either the `CREATE PROCEDURE` or `ALTER PROCEDURE` statements. Changing the context at runtime is not supported.

#### Code Example

Input Code:

```sql
 CREATE PROCEDURE proc1()
WITH EXECUTE AS OWNER
AS
BEGIN
 SELECT USER_NAME();
 EXECUTE AS CALLER;
 SELECT USER_NAME();
 REVERT;
 SELECT USER_NAME();
END

GO
```

Output Code:

```sql
 CREATE OR REPLACE PROCEDURE proc1 ()
RETURNS ARRAY
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "07/05/2024" }}'
EXECUTE AS OWNER
AS
$$
 DECLARE
  ProcedureResultSet1 VARCHAR;
  ProcedureResultSet2 VARCHAR;
  ProcedureResultSet3 VARCHAR;
  return_arr ARRAY := array_construct();
 BEGIN
  ProcedureResultSet1 := 'RESULTSET_' || REPLACE(UPPER(UUID_STRING()), '-', '_');
  CREATE OR REPLACE TEMPORARY TABLE IDENTIFIER(:ProcedureResultSet1) AS
   SELECT
    CURRENT_USER();
  return_arr := array_append(return_arr, :ProcedureResultSet1);
  !!!RESOLVE EWI!!! /*** SSC-EWI-TS0080 - CHANGING THE EXECUTION CONTEXT AT RUNTIME IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
 EXECUTE AS CALLER;
  ProcedureResultSet2 := 'RESULTSET_' || REPLACE(UPPER(UUID_STRING()), '-', '_');
  CREATE OR REPLACE TEMPORARY TABLE IDENTIFIER(:ProcedureResultSet2) AS
   SELECT
    CURRENT_USER();
  return_arr := array_append(return_arr, :ProcedureResultSet2);
  !!!RESOLVE EWI!!! /*** SSC-EWI-TS0080 - CHANGING THE EXECUTION CONTEXT AT RUNTIME IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
 REVERT;
  ProcedureResultSet3 := 'RESULTSET_' || REPLACE(UPPER(UUID_STRING()), '-', '_');
  CREATE OR REPLACE TEMPORARY TABLE IDENTIFIER(:ProcedureResultSet3) AS
   SELECT
    CURRENT_USER();
  return_arr := array_append(return_arr, :ProcedureResultSet3);
  --** SSC-FDM-0020 - MULTIPLE RESULT SETS ARE RETURNED IN TEMPORARY TABLES **
  RETURN return_arr;
 END;
$$;
```

#### Best Practices

* Refactor the code so it works without having to switch the context.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0081

Using a full join in a delete statement is not supported

### Description

When transforming the DELETE statement, SnowConvert AI extracts the table references found in the FROM clause of the statement and moves them to the USING clause of the Snowflake delete statement.

The following EWI warns the user about the limitations of the outer join (+) syntax in Snowflake. To preserve the LEFT and RIGHT JOINs used in the original code, outer join syntax (+) is added to the conditions to indicate such behavior. However, in Snowflake, the (+) syntax can’t be used to indicate FULL JOINs. For more information, see [Joins in the WHERE clause](https://docs.snowflake.com/en/sql-reference/constructs/where#joins-in-the-where-clause).

#### Example code

##### Input Code

```sql
DELETE Employees
FROM Employees FULL OUTER JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID
WHERE Departments.DepartmentID IS NULL;
```

##### Generated Code

```sql
!!!RESOLVE EWI!!! /*** SSC-EWI-TS0081 - USING A FULL JOIN IN A DELETE STATEMENT IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
DELETE FROM
Employees
USING Departments
WHERE
Departments.DepartmentID IS NULL
AND Employees.DepartmentID = Departments.DepartmentID;
```

#### Best Practices

* Check the logic of your FULL JOIN, it might be possible to rewrite it as other type of JOIN. For example, the code included in the example code is essentially the same as a LEFT JOIN:

Input:

```sql
DELETE Employees
FROM Employees LEFT OUTER JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID
WHERE Departments.DepartmentID IS NULL;
```

Output:

```sql
 DELETE FROM
    Employees
USING Departments
WHERE
    Departments.DepartmentID IS NULL
    AND Employees.DepartmentID = Departments.DepartmentID(+);
```

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0082

CROSS APPLY has been converted to LEFT OUTER JOIN and requires manual validation.

### Description

Manual validation is required because the conversion from CROSS APPLY to LEFT OUTER JOIN can lead to incorrect results or unexpected behavior in Snowflake. While the two functions might seem similar, they handle certain situations differently, especially when the subquery has no matches or the subquery is correlated with the outer table.

#### Example code

##### Setup Data

```sql
-- Create a table to store monthly sales or metric data
CREATE TABLE sales_metrics (
    metric_id INT PRIMARY KEY,
    january_value VARCHAR(35),
    february_value VARCHAR(35),
    march_value VARCHAR(35)
);

-- Insert sample data
INSERT INTO sales_metrics (metric_id, january_value, february_value, march_value) VALUES
(1, 'sales-jan-1', 'sales-feb-1', 'sales-march-1'),
(2, 'sales-jan-2', 'sales-feb-2', 'sales-march-2');
```

##### Input Code

```sql
SELECT
    m.metric_id,
    monthly_data.metric_value,
    monthly_data.month_number
FROM
    sales_metrics m
CROSS APPLY (
    SELECT m.january_value AS metric_value, '01' AS month_number
    UNION ALL
    SELECT m.february_value AS metric_value, '02' AS month_number
    UNION ALL
    SELECT m.march_value AS metric_value, '03' AS month_number
) AS monthly_data;
```

##### Generated Code

```sql
SELECT
    m.metric_id,
    monthly_data.metric_value,
    monthly_data.month_number
FROM
    sales_metrics m
    !!!RESOLVE EWI!!! /*** SSC-EWI-TS0082 - CROSS APPLY HAS BEEN CONVERTED TO LEFT OUTER JOIN AND REQUIRES MANUAL VALIDATION. ***/!!!
    LEFT OUTER JOIN
        (
               SELECT
                m.january_value AS metric_value, '01' AS month_number
               UNION ALL
               SELECT
                m.february_value AS metric_value, '02' AS month_number
               UNION ALL
               SELECT
                m.march_value AS metric_value, '03' AS month_number
           ) AS monthly_data;
```

#### Best Practices

### Key Scenarios Where LEFT OUTER JOIN May Fail

* **Filtering Behavior:** If the original `CROSS APPLY` was intended to filter out rows from the main table that have no matches in the subquery, a `LEFT OUTER JOIN` will not replicate this behavior. Instead, it will include those rows with `NULL` values for the joined columns, which may not be the intended result.
* **Correlated Subqueries:** `CROSS APPLY` is specifically designed to support correlated subqueries, where the subquery references columns from the outer query. A standard `LEFT OUTER JOIN` does not support this pattern in the same way. Attempting to convert a correlated `CROSS APPLY` to a `LEFT OUTER JOIN` can lead to syntax errors, Cartesian products (duplicate rows), or logically incorrect results.
* **Result Set Differences:** The semantics of `CROSS APPLY` and `LEFT OUTER JOIN` differ, especially when the subquery returns no rows. `CROSS APPLY` will exclude such rows from the result, while `LEFT OUTER JOIN` will include them with `NULL` values.

**Recommendation:** Always review and test the output of queries where `CROSS APPLY` has been converted to `LEFT OUTER JOIN` to ensure correctness.

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-TS0083

### Error Message

**ROLLBACK TRANSACTION requires the appropriate setup to work as intended.**

### Severity

**Low**

### Description

This EWI is generated when a `ROLLBACK TRANSACTION` statement is encountered, indicating that SnowConvert has successfully transformed the statement into a Snowflake-compatible format. However, the transformation requires manual verification because Snowflake’s transaction rollback behavior differs significantly from SQL Server’s `ROLLBACK TRANSACTION` functionality.

### Example Code

#### Input (SQL Server)

```sql
BEGIN TRANSACTION MyTransaction;

    -- Some operations
    INSERT INTO Employees (Name, Department) VALUES ('Alice', 'Engineering');

    IF @@ERROR <> 0
    BEGIN
        ROLLBACK TRANSACTION MyTransaction;  -- Named transaction rollback
    END
    ELSE
    BEGIN
        COMMIT TRANSACTION MyTransaction;
    END
```

#### Output (Snowflake Scripting)

```sql
BEGIN
    !!!RESOLVE EWI!!! /*** SSC-EWI-0073 - PENDING FUNCTIONAL EQUIVALENCE REVIEW FOR 'BeginTransaction' NODE ***/!!!
    BEGIN TRANSACTION MyTransaction;

        -- Some operations
    --** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "Employees" **
        INSERT INTO Employees (Name, Department) VALUES ('Alice', 'Engineering');
    IF (:ERROR <> 0) THEN
        BEGIN
            !!!RESOLVE EWI!!! /*** SSC-EWI-TS0083 - ROLLBACK TRANSACTION REQUIRES THE APPROPRIATE SETUP TO WORK AS INTENDED. ***/!!!
            ROLLBACK TRANSACTION MyTransaction;  -- Named transaction rollback

        END;
    ELSE
        BEGIN
            COMMIT;
        END;
    END IF;
END;
```

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
