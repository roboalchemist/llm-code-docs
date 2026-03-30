# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/functional-difference/sqlServerFDM.md

# SnowConvert AI - SQL Server-Azure Synapse Functional Differences

Applies to

* SQL Server
* Azure Synapse Analytics

## SSC-FDM-TS0001

> **Note:**
>
> This FDM is deprecated, please refer to [SSC-EWI-TS0077](../conversion-issues/sqlServerEWI.md) documentation

### Description

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
--           --** SSC-FDM-TS0001 - COLLATION Albanian_BIN NOT SUPPORTED **
--           COLLATE Albanian_BIN
                               ;

SELECT 'a'
--           --** SSC-FDM-TS0001 - COLLATION Albanian_CI_AI NOT SUPPORTED **
--           COLLATE Albanian_CI_AI
                                 ;

CREATE OR REPLACE TABLE ExampleTable (
    ID INT,
    Name VARCHAR(50)
--                     --** SSC-FDM-TS0001 - COLLATION collateName NOT SUPPORTED **
--                     COLLATE collateName
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0002

### Description

This message is shown when there is a collate clause that is not supported in Snowflake.

#### Code Example

##### Input Code

```sql
 SELECT 'a' COLLATE Latin1_General_CI_AS_WS;
```

##### Generated Code

```sql
 SELECT 'a' COLLATE 'EN-CI-AS' /*** SSC-FDM-TS0002 - COLLATION FOR VALUE WS NOT SUPPORTED ***/;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0003

XP_LOGININFO mapped to custom UDF

### Description

This message is shown when the XP_LOGININFO procedure is executed and returns the following set of columns ([See SQL SERVER documentation for more info](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/xp-logininfo-transact-sql?view=sql-server-ver16))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| account name | type | privilege | mapped login name | permission path |

To replicate this behavior, there is a query that select the columns from the APPLICABLE_ROLES view in Snowflake, which returns the following set of columns ([See Snowflake documentation for more info](https://docs.snowflake.com/en/sql-reference/info-schema/applicable_roles.html))

| GRANTEE | ROLE_NAME | ROLE_OWNER | IS_GRANTABLE |
| --- | --- | --- | --- |

SQL Server original columns are mapped as shown in the next table. They may be not completely equivalent.

| SQL Server | Snowflake |  |
| --- | --- | --- |
| account name | GRANTEE |  |
| type | ROLE_OWNER |  |
| privilege | ROLE_NAME |  |
| mapped login name | GRANTEE |  |
| permission path | NULL |  |

#### Example code

##### Input code

```sql
 EXEC xp_logininfo

EXEC xp_logininfo 'USERNAME'
```

##### Generated Code

```sql
 --** SSC-FDM-TS0003 - XP_LOGININFO MAPPED TO CUSTOM UDF XP_LOGININFO_UDF AND MIGHT HAVE DIFFERENT BEHAVIOR **
SELECT
*
FROM
TABLE(XP_LOGININFO_UDF());

--** SSC-FDM-TS0003 - XP_LOGININFO MAPPED TO CUSTOM UDF XP_LOGININFO_UDF AND MIGHT HAVE DIFFERENT BEHAVIOR **
SELECT
*
FROM
TABLE(XP_LOGININFO_UDF('USERNAME'));
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0004

### Description

This message is shown when a `BULK INSERT` was transformed and a `PUT` command is added to the output code. It happens because the `PUT` command cannot be executed using the SnowSQL Web UI. To successfully execute it, any user should have the SnowCLI installed before.

#### Code Example

##### Input Code

```sql
 BULK INSERT #temptable FROM 'path/to/file.txt'
WITH
(
   FIELDTERMINATOR ='\t',
   ROWTERMINATOR ='\n'
);
```

##### Generated Code

```sql
 CREATE OR REPLACE FILE FORMAT FILE_FORMAT_638466175888203490
FIELD_DELIMITER = '\t'
RECORD_DELIMITER = '\n';

CREATE OR REPLACE STAGE STAGE_638466175888203490
FILE_FORMAT = FILE_FORMAT_638466175888203490;

--** SSC-FDM-TS0004 - PUT STATEMENT IS NOT SUPPORTED ON WEB UI. YOU SHOULD EXECUTE THE CODE THROUGH THE SNOWFLAKE CLI **
PUT file://path/to/file.txt @STAGE_638466175888203490 AUTO_COMPRESS = FALSE;

--** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "#temptable" **
COPY INTO T_temptable FROM @STAGE_638466175888203490/file.txt;
```

#### Best Practices

* Install SnowCLI.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0005

TRY_CONVERT/TRY_CAST could not be converted to TRY_CAST

### Description

This FDM is added when a TRY_CONVERT or TRY_CAST cannot be converted to a TRY_CAST in Snowflake.

[Snowflake’s TRY_CAST](https://docs.snowflake.com/en/sql-reference/functions/try_cast) function has a limitation as it only allows the conversion of string expressions. However, Transact’s `TRY_CONVERT` and `TRY_CAST` functions allow any data type expression.

Currently, the transformation from `TRY_CONVERT` or `TRY_CAST` to Snowflake’s `TRY_CAST` is only performed for string expressions or expressions that the tool can identify as strings in its context.

#### Code Example

##### Input Code

```sql
 SELECT TRY_CAST(14.85 AS INT);
SELECT TRY_CONVERT(VARCHAR, 1234);
SELECT TRY_CONVERT(CHAR, 1);
SELECT TRY_CONVERT(SQL_VARIANT, '2017-01-01 12:00:00');
SELECT TRY_CONVERT(GEOGRAPHY, 'LINESTRING(-122.360 47.656, -122.343 47.656 )');
```

##### Generated Code

```sql
 SELECT
CAST(14.85 AS INT) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/;
SELECT
TO_VARCHAR(1234);
SELECT
TO_CHAR(1);
SELECT
TO_VARIANT('2017-01-01 12:00:00');
SELECT
TO_GEOGRAPHY('LINESTRING(-122.360 47.656, -122.343 47.656 )');
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0006

EXECUTE AS ‘user_name’ clause does not exist in Snowflake and the user calling the procedure should have all the required privileges.

### Description

This message is shown when SnowConvert AI finds a procedure with an `EXECUTE AS 'user_name'` clause. This is not supported in Snowflake, so it is changed `EXECUTE AS CALLER.`

This clause specifies the security context under which to execute the procedure.

> **Note:**
>
> For more details see the [documentation](https://learn.microsoft.com/en-us/sql/t-sql/statements/execute-as-clause-transact-sql?view=sql-server-ver16&amp;tabs=sqlserver) about the clause functionality.

#### Code Example

##### Input Code

```sql
 CREATE PROCEDURE SelectAllCustomers
WITH EXECUTE AS 'user_name'
AS
BEGIN
      SELECT * FROM Customers;
END;
```

##### Generated Code

```sql
 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "Customers" **
CREATE OR REPLACE PROCEDURE SelectAllCustomers ()
RETURNS TABLE()
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
--** SSC-FDM-TS0006 - EXECUTE AS 'user_name' CLAUSE DOES NOT EXIST IN SNOWFLAKE AND THE USER CALLING THE PROCEDURE SHOULD HAVE ALL THE REQUIRED PRIVILEGES **
AS
$$
      DECLARE
            ProcedureResultSet RESULTSET;
      BEGIN
            ProcedureResultSet := (
            SELECT
                  *
            FROM
                  Customers);
            RETURN TABLE(ProcedureResultSet);
      END;
$$;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0007

FOR REPLICATION clause does not exist in Snowflake.

### Description

This message is shown when SnowConvert AI finds a procedure with a `FOR REPLICATION` clause. This is not supported in Snowflake, so it is removed.

This clause specifies that the procedure is created for replication. Consequently, it can’t be executed on the Subscriber.

> **Note:**
>
> For more details see the [documentation](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-procedure-transact-sql?view=sql-server-ver16#for-replication) about the clause functionality.

#### Code Example

##### Input Code

```sql
 CREATE PROCEDURE SelectAllCustomers
WITH FOR REPLICATION
AS
BEGIN
      SELECT * FROM Customers;
END;
```

##### Generated Code

```sql
 --** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "Customers" **
CREATE OR REPLACE PROCEDURE SelectAllCustomers ()
RETURNS TABLE()
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
--** SSC-FDM-TS0007 - FOR REPLICATION CLAUSE DOES NOT EXIST IN SNOWFLAKE **
AS
$$
      DECLARE
            ProcedureResultSet RESULTSET;
      BEGIN
            ProcedureResultSet := (
            SELECT
                  *
            FROM
                  Customers);
            RETURN TABLE(ProcedureResultSet);
      END;
$$;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0008

FORMATMESSAGE function was converted to UDF

### Description

This Warning is added because the `FORMATMESSAGE` function is being used and it was replaced by `FORMATMESSAGE_UDF`. The reason to add the warning is because the `FORMATMESSAGE_UDF` used to replace the `FORMATMESSAGE` does not handle properly all kinds of formats and it may throw an error on certain conditions.

Unsigned numerical values that are given as negative will preserve the sign instead of converting the value. Also, the `%I64d` placeholder is not supported by the UDF so it will throw an error when it is used.

In the FORMATMESSAGE_UDF, an error will happen if the given number of arguments is different than the number of placeholders.

This UDF does not support using message number IDs.

#### Code Example

##### Input Code

```sql
 SELECT FORMATMESSAGE('Unsigned int %u, %u', 50, -50); -- Unsigned int 50, 4294967246
SELECT FORMATMESSAGE('Unsigned octal %o, %o', 50, -50); -- Unsigned octal 62, 37777777716
SELECT FORMATMESSAGE('Unsigned hexadecimal %X, %x', -11, -50); -- Unsigned hexadecimal FFFFFFF5, ffffffce
SELECT FORMATMESSAGE('Unsigned octal with prefix: %#o', -50); -- Unsigned octal with prefix: 037777777716
SELECT FORMATMESSAGE('Unsigned hexadecimal with prefix: %#X, %x', -11,-50); -- Unsigned hexadecimal with prefix: 0XFFFFFFF5, ffffffce
SELECT FORMATMESSAGE('Bigint %I64d', 3000000000); -- Bigint 3000000000
SELECT FORMATMESSAGE('My message: %s %s %s', 'Hello', 'World'); -- My message: Hello World (null)
```

##### Generated Code

```sql
 SELECT
--** SSC-FDM-TS0008 - FORMATMESSAGE WAS CONVERTED TO CUSTOM UDF FORMATMESSAGE_UDF AND IT MIGHT HAVE A DIFFERENT BEHAVIOR. **
FORMATMESSAGE_UDF('Unsigned int %u, %u', ARRAY_CONSTRUCT(50, -50)); -- Unsigned int 50, 4294967246
SELECT
--** SSC-FDM-TS0008 - FORMATMESSAGE WAS CONVERTED TO CUSTOM UDF FORMATMESSAGE_UDF AND IT MIGHT HAVE A DIFFERENT BEHAVIOR. **
FORMATMESSAGE_UDF('Unsigned octal %o, %o', ARRAY_CONSTRUCT(50, -50)); -- Unsigned octal 62, 37777777716
SELECT
--** SSC-FDM-TS0008 - FORMATMESSAGE WAS CONVERTED TO CUSTOM UDF FORMATMESSAGE_UDF AND IT MIGHT HAVE A DIFFERENT BEHAVIOR. **
FORMATMESSAGE_UDF('Unsigned hexadecimal %X, %x', ARRAY_CONSTRUCT(-11, -50)); -- Unsigned hexadecimal FFFFFFF5, ffffffce
SELECT
--** SSC-FDM-TS0008 - FORMATMESSAGE WAS CONVERTED TO CUSTOM UDF FORMATMESSAGE_UDF AND IT MIGHT HAVE A DIFFERENT BEHAVIOR. **
FORMATMESSAGE_UDF('Unsigned octal with prefix: %#o', ARRAY_CONSTRUCT(-50)); -- Unsigned octal with prefix: 037777777716
SELECT
--** SSC-FDM-TS0008 - FORMATMESSAGE WAS CONVERTED TO CUSTOM UDF FORMATMESSAGE_UDF AND IT MIGHT HAVE A DIFFERENT BEHAVIOR. **
FORMATMESSAGE_UDF('Unsigned hexadecimal with prefix: %#X, %x', ARRAY_CONSTRUCT(-11, -50)); -- Unsigned hexadecimal with prefix: 0XFFFFFFF5, ffffffce
SELECT
--** SSC-FDM-TS0008 - FORMATMESSAGE WAS CONVERTED TO CUSTOM UDF FORMATMESSAGE_UDF AND IT MIGHT HAVE A DIFFERENT BEHAVIOR. **
FORMATMESSAGE_UDF('Bigint %I64d', ARRAY_CONSTRUCT(3000000000)); -- Bigint 3000000000
SELECT
--** SSC-FDM-TS0008 - FORMATMESSAGE WAS CONVERTED TO CUSTOM UDF FORMATMESSAGE_UDF AND IT MIGHT HAVE A DIFFERENT BEHAVIOR. **
FORMATMESSAGE_UDF('My message: %s %s %s', ARRAY_CONSTRUCT('Hello', 'World')); -- My message: Hello World (null)
```

#### Best Practices

* Avoid using `%I64d` placeholder in the message.
* Use directly the message as a string instead of using a message ID for the first argument.
* Make sure the number of placeholders is the same as the number of arguments after the message.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0009

Encrypted with not supported in Snowflake.

### Description

This warning is added when there is an `ENCRYPTED WITH` used in a Column Definition. Since this is not supported in Snowflake, it is being removed and a warning is added.

#### Code Example

##### Input Code

```sql
 CREATE TABLE [SCHEMA1].[TABLE1] (
    [COL1] NVARCHAR(60)
        ENCRYPTED WITH (
            COLUMN_ENCRYPTION_KEY = MyCEK,
            ENCRYPTION_TYPE = RANDOMIZED,
            ALGORITHM = 'AEAD_AES_256_CBC_HMAC_SHA_256'
        )
);
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE SCHEMA1.TABLE1 (
    COL1 VARCHAR(60)
--    --** SSC-FDM-TS0009 - ENCRYPTED WITH NOT SUPPORTED IN SNOWFLAKE **
--           ENCRYPTED WITH (
--               COLUMN_ENCRYPTION_KEY = MyCEK,
--               ENCRYPTION_TYPE = RANDOMIZED,
--               ALGORITHM = 'AEAD_AES_256_CBC_HMAC_SHA_256'
--           )
   )
   COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"transact"}}'
   ;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0010

CURRENT_DATABASE function has different behavior in certain cases.

### Description

This EWI is added when the function DB_NAME is transformed to CURRENT_DATABASE because Snowflake does not support the database_id parameter and the CURRENT_DATABASE function will always return the current database name.

#### Code Example

##### Input Code

```sql
 SELECT DB_NAME(someId);
```

##### Generated Code

```sql
 SELECT
CURRENT_DATABASE() /*** SSC-FDM-TS0010 - CURRENT_DATABASE function has different behavior in certain cases ***/;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0011

Default value not allowed in Snowflake.

> **Note:**
>
> This FDM is deprecated, please refer to [SSC-EWI-TS0078](../conversion-issues/sqlServerEWI.md) documentation

### Description

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
--                         --** SSC-FDM-TS0011 - DEFAULT OPTION NOT ALLOWED IN SNOWFLAKE **
--                         DEFAULT RANDOM(10)
                                           ;
```

#####

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0012

Information for the column was not found. STRING used to match CAST operation

### Description

This EWI is added in Table-Valued User Defined Functions where the return type of a column can not be determined during the conversion. `STRING` is used as a default to match the `CAST` operation in the `SELECT` statement <!–TODO: search for a broken reference.->

#### Code Example

##### Input Code

```sql
 CREATE FUNCTION GetDepartmentInfo()
RETURNS TABLE
AS
RETURN
(
  SELECT DepartmentID, Name, GroupName
  FROM HumanResources.Department
);
```

##### Generated Code

```sql
 CREATE OR REPLACE FUNCTION GetDepartmentInfo ()
RETURNS TABLE(
  DepartmentID STRING /*** SSC-FDM-TS0012 - INFORMATION FOR THE COLUMN DepartmentID WAS NOT FOUND. STRING DATATYPE USED TO MATCH CAST AS STRING OPERATION ***/,
  Name STRING /*** SSC-FDM-TS0012 - INFORMATION FOR THE COLUMN Name WAS NOT FOUND. STRING DATATYPE USED TO MATCH CAST AS STRING OPERATION ***/,
  GroupName STRING /*** SSC-FDM-TS0012 - INFORMATION FOR THE COLUMN GroupName WAS NOT FOUND. STRING DATATYPE USED TO MATCH CAST AS STRING OPERATION ***/
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
AS
$$
    SELECT
    CAST(DepartmentID AS STRING),
    CAST(Name AS STRING),
    CAST(GroupName AS STRING)
    FROM
    HumanResources.Department
$$;
```

#### Best Practices

* The user should check which is the correct data type that could not be found and change it in the `RETURNS TABLE` statement definition.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0013

Snowflake Scripting cursor rows are not modifiable.

### Description

This EWI is added when Cursors are open to modification in the input code. Snowflake Scripting does not allow modifying cursor rows.

#### Example Code

##### Input Code

```sql
 CREATE OR ALTER PROCEDURE modifiablecursorTest
AS
BEGIN
    -- Should be marked with SSC-FDM-TS0013
    DECLARE CursorVar CURSOR
 FOR
 SELECT FirstName
 FROM vEmployee;
    DECLARE CursorVar2 INSENSITIVE CURSOR
 FOR
 SELECT FirstName
 FROM vEmployee;
    DECLARE CursorVar3 CURSOR KEYSET SCROLL_LOCKS
 FOR
 SELECT FirstName
 FROM vEmployee;
    DECLARE CursorVar4 CURSOR DYNAMIC OPTIMISTIC
 FOR
 SELECT FirstName
 FROM vEmployee;
    DECLARE CursorVar6 CURSOR STATIC
 FOR
 SELECT FirstName
 FROM vEmployee;
    DECLARE CursorVar7 CURSOR READ_ONLY
 FOR
 SELECT FirstName
 FROM vEmployee;
    -- Shouid not be marked
    DECLARE CursorVar5 CURSOR STATIC READ_ONLY
 FOR
 SELECT FirstName
 FROM vEmployee;
    RETURN 'DONE';
END;
```

##### Generated Code

```sql
 CREATE OR REPLACE PROCEDURE modifiablecursorTest ()
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
EXECUTE AS CALLER
AS
$$
 DECLARE
  -- Should be marked with SSC-FDM-TS0013
  --** SSC-FDM-TS0013 - SNOWFLAKE SCRIPTING CURSOR ROWS ARE NOT MODIFIABLE **
  CursorVar CURSOR
  FOR
   SELECT
    FirstName
   FROM
    vEmployee;
  --** SSC-FDM-TS0013 - SNOWFLAKE SCRIPTING CURSOR ROWS ARE NOT MODIFIABLE **
  CursorVar2 CURSOR
  FOR
   SELECT
    FirstName
   FROM
    vEmployee;
  --** SSC-FDM-TS0013 - SNOWFLAKE SCRIPTING CURSOR ROWS ARE NOT MODIFIABLE **
  CursorVar3 CURSOR
  FOR
   SELECT
    FirstName
   FROM
    vEmployee;
  --** SSC-FDM-TS0013 - SNOWFLAKE SCRIPTING CURSOR ROWS ARE NOT MODIFIABLE **
  CursorVar4 CURSOR
  FOR
   SELECT
    FirstName
   FROM
    vEmployee;
  --** SSC-FDM-TS0013 - SNOWFLAKE SCRIPTING CURSOR ROWS ARE NOT MODIFIABLE **
  CursorVar6 CURSOR
  FOR
   SELECT
    FirstName
   FROM
    vEmployee;
  --** SSC-FDM-TS0013 - SNOWFLAKE SCRIPTING CURSOR ROWS ARE NOT MODIFIABLE **
  CursorVar7 CURSOR
  FOR
   SELECT
    FirstName
   FROM
    vEmployee;
  -- Shouid not be marked
  CursorVar5 CURSOR
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

## SSC-FDM-TS0014

Computed column transformed

### Description

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
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},{"attributes":{"component":"transact"}}'
;
```

#### Best Practices

* No additional user actions are required; it is just informative.
* Add manual changes to the not-transformed expression.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0016

XML columns in Snowflake might have a different format

### Description

This warning is added when an SQL Server FOR XML clause is transformed to its Snowflake equivalent. It is added because columns in XML could be different.

#### Code Example

Given the following table called `employee` as an example.

| Id | Name | Hint |
| --- | --- | --- |
| 1 | Kinslee Park | Developer |
| 2 | Ezra Mata | Developer |
| 3 | Aliana Quinn | Manager |

##### Input Code

##### Code

```sql
 SELECT
   e.id,
   e.name as full_name,
   e.hint
  FROM
   employee e
  FOR XML PATH;
```

##### Output

```html
 <row>
    <id>1</id>
    <full_name>Kinslee Park</full_name>
    <hint>Developer</hint>
</row>
<row>
    <id>2</id>
    <full_name>Ezra Mata</full_name>
    <hint>Developer</hint>
</row>
<row>
    <id>3</id>
    <full_name>Aliana Quinn</full_name>
    <hint>Manager</hint>
</row>
```

##### Generated Code

##### Code

```sql
 SELECT
 --** SSC-FDM-TS0016 - XML COLUMNS IN SNOWFLAKE MIGHT HAVE A DIFFERENT FORMAT **
 FOR_XML_UDF(OBJECT_CONSTRUCT('id', e.id, 'full_name', e.name, 'hint', e.hint), 'row')
FROM
 employee e;
```

##### Output

```html
 <row type="OBJECT">
    <full_name type="VARCHAR">Kinslee Park</full_name>
    <hint type="VARCHAR">Developer</hint>
    <id type="INTEGER">1</id>
</row>
<row type="OBJECT">
    <full_name type="VARCHAR">Ezra Mata</full_name>
    <hint type="VARCHAR">Developer</hint>
    <id type="INTEGER">2</id>
</row>
<row type="OBJECT">
    <full_name type="VARCHAR">Aliana Quinn</full_name>
    <hint type="VARCHAR">Manager</hint>
    <id type="INTEGER">3</id>
</row>
```

#### Best Practices

* No additional user actions are required; it is just informative.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0017

CURRENT_USER function does not support a user ID as a parameter.

### Description

This EWI is added when functions like `SUSER_NAME` or `SUSER_SNAME` contain the user identifier as a parameter because this last one is not supported in the CURRENT_USER function in Snowflake.

#### Input Code

```sql
 SELECT SUSER_NAME(0x010500000000000515000000a065cf7e784b9b5fe77c87705a2e0000);
```

##### Generated Code

```sql
 SELECT
CURRENT_USER() /*** SSC-FDM-TS0017 - User ID parameter used in SUSER_NAME function is not supported in CURRENT_USER function and it was removed. ***/;
```

#### Best Practices

* No additional user actions are required.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0018

Database console command is not supported

> **Note:**
>
> This FDM is deprecated, please refer to [SSC-EWI-TS0079](../conversion-issues/sqlServerEWI.md) documentation

### Description

This FDM is added when SnowConvert AI finds a DBCC statement inside the input code.
Most DBCC statements are not supported in Snowflake.

#### Code Example

##### Input Code

```sql
 DBCC CHECKIDENT(@a, RESEED, @b) WITH NO_INFOMSGS
```

##### Generated Code

```sql
 ----** SSC-FDM-TS0018 - DATABASE CONSOLE COMMAND 'CHECKIDENT' IS NOT SUPPORTED. **
--DBCC CHECKIDENT(@a, RESEED, @b) WITH NO_INFOMSGS
```

#### Best Practices

* No additional user actions are required; it is just informative.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0019

RAISERROR Error Message may differ because of the SQL Server string format.

### Description

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
  --** SSC-FDM-TS0019 - RAISERROR ERROR MESSAGE MAY DIFFER BECAUSE OF THE SQL SERVER STRING FORMAT **
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

## SSC-FDM-TS0020

Default constraint was commented out and may have been added to a table definition.

### Description

This FDM is added when the default constraint is present in an Alter Table statement.

Currently, support for that constraint is unavailable. A workaround to transform it is to define the table before using Alter Table. This allows SnowConvert AI to identify the references, and the default constraint is consolidated in the table definition. Otherwise, the constraint is only commented out.

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
  CONSTRAINT col1_constraint DEFAULT (getdate()) FOR col1;
```

##### Generated Code

```sql
 CREATE OR REPLACE TABLE table1 (
  col1 INTEGER DEFAULT 50,
  col2 VARCHAR COLLATE 'EN-CS',
  col3 DATE
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"transact"}}'
;

ALTER TABLE table1
ADD col4 INTEGER;

----** SSC-FDM-TS0020 - DEFAULT CONSTRAINT MAY HAVE BEEN ADDED TO TABLE DEFINITION **

--ALTER TABLE table1
--ADD
--CONSTRAINT col1_constraint DEFAULT 50 FOR col1
                                              ;

----** SSC-FDM-TS0020 - DEFAULT CONSTRAINT MAY HAVE BEEN ADDED TO TABLE DEFINITION **

--ALTER TABLE table1
--ADD
--CONSTRAINT col1_constraint DEFAULT (CURRENT_TIMESTAMP() :: TIMESTAMP) FOR col1
                                                                              ;
```

#### Known Issues

* When different default constraints are declared over the same column, only the first will be reflected on the Create Table Statement.
* When a default constraint is declared on a missing column, the transformation cannot be performed due to the lack of dependencies.

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0021

A MASKING POLICY was created as a substitute for MASKED WITH.

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

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
 --** SSC-FDM-TS0022 - MASKING ROLE MUST BE DEFINED PREVIOUSLY BY THE USER **
CREATE OR REPLACE MASKING POLICY "default" AS
(val STRING)
RETURNS STRING ->
CASE
WHEN current_role() IN ('YOUR_DEFINED_ROLE_HERE')
THEN val
ELSE 'xxxxx'
END;

ALTER TABLE IF EXISTS table_name MODIFY COLUMN column_name/*** SSC-FDM-TS0021 - A MASKING POLICY WAS CREATED AS SUBSTITUTE FOR MASKED WITH ***/  SET MASKING POLICY "default";
```

> **Note:**
>
> The MASKING POLICY will be created previous to the ALTER TABLE statement. And it is expected to have an approximate behavior. Some tweaks might be needed in regard to roles and user privileges.

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0022

The user must previously define the masking role.

> **Note:**
>
> Some parts of the output code are omitted for clarity reasons.

### Description

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
 --** SSC-FDM-TS0022 - MASKING ROLE MUST BE DEFINED PREVIOUSLY BY THE USER **
CREATE OR REPLACE MASKING POLICY "partial_1_xxxxx_1" AS
(val STRING)
RETURNS STRING ->
CASE
WHEN current_role() IN ('YOUR_DEFINED_ROLE_HERE')
THEN val
ELSE LEFT(val, 1) || 'xxxxx' || RIGHT(val, 1)
END;

ALTER TABLE IF EXISTS tableName MODIFY COLUMN columnName/*** SSC-FDM-TS0021 - A MASKING POLICY WAS CREATED AS SUBSTITUTE FOR MASKED WITH ***/  SET MASKING POLICY "partial_1_xxxxx_1";
```

> **Note:**
>
> As shown on line 6, there is a placeholder where the defined roles can be placed. There is room for one or several values separated by commas. Also, here, the use of single quotes is mandatory for each of the values.

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0023

Error function could be different in Snowflake

### Description

This EWI is added in the transformation of the following ERRORs functions due to the corresponding behavior change.

* **ERROR_MESSAGE** The message of SQLERRM could be different in Snowflake.
* **ERROR_STATE** The target SQLSTATE property could return a different number due to platform differences.
* **ERROR_PROCEDURE** Transformation changed to return the stored procedure where the function is called.

#### Input Code

```sql
CREATE PROCEDURE ProcError
AS
BEGIN
Declare @ErrorState INT = ERROR_STATE();
Declare @ErrorMessage INT = ERROR_MESSAGE();
Declare @ErrorProc INT = ERROR_PROCEDURE();
Select 1;
END;
```

#### Generated Code

```sql
CREATE OR REPLACE PROCEDURE ProcError ()
RETURNS TABLE()
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "09/01/2025",  "domain": "no-domain-provided" }}'
EXECUTE AS CALLER
AS
$$
DECLARE
ERRORSTATE INT := SQLSTATE /*** SSC-FDM-TS0023 - ERROR STATE COULD BE DIFFERENT IN SNOWFLAKE ***/;
ERRORMESSAGE INT := SQLERRM /*** SSC-FDM-TS0023 - ERROR MESSAGE COULD BE DIFFERENT IN SNOWFLAKE ***/;
ERRORPROC INT := 'ProcError' /*** SSC-FDM-TS0023 - ERROR PROCEDURE NAME COULD BE DIFFERENT IN SNOWFLAKE ***/;
ProcedureResultSet RESULTSET;
BEGIN

ProcedureResultSet := (
Select 1);
RETURN TABLE(ProcedureResultSet);
END;
$$;
```

#### Recommendation

If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com).

## SSC-FDM-TS0024

CURRENT_TIMESTAMP in At Time Zone statement may have a different behavior in certain cases.

### Description

This FDM is added when the `At Time Zone` has the `CURRENT_TIMESTAMP`. This is because the result might differ in some instances.

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
CONVERT_TIMEZONE('Pacific/Honolulu', CURRENT_TIMESTAMP() /*** SSC-FDM-TS0024 - CURRENT_TIMESTAMP in At Time Zone statement may have a different behavior in certain cases ***/);
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

## SSC-FDM-TS0025

DB_ID_UDF may have a different behavior in certain cases.

### Description

This FDM is added to clarify that the DB_ID_UDF tries to emulate the [DB_ID](https://learn.microsoft.com/en-us/sql/t-sql/functions/db-id-transact-sql?view=sql-server-ver16) SqlServer function as well as possible. In SqlServer, the identifier assigned to a database is unique, and if the database is deleted, this ID won’t ever be used again; otherwise, in Snowflake, this identifier corresponds to the number assigned to the database when it is created; it is also unique, but it is a consecutive number which means that if this database is deleted, this number is going to be assigned to the database that was created after the deleted one.

#### Input Code

##### Sql Server

```sql
 SELECT DB_ID('my_database');
```

##### Result

`6`

##### Generated Code

##### Snowflake

```sql
 SELECT
DB_ID_UDF('my_database') /*** SSC-FDM-TS0025 - DB_ID_UDF MAY HAVE A DIFFERENT BEHAVIOR IN CERTAIN CASES ***/;
```

##### Result

`6`

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0026

DELETE case is not being considered in the temporary table

### Description

There is an INSERT statement pattern that requires a specific transformation, which involves the creation of a temporary table. This FDM notifies that the DELETE case is not considered in the transformation mentioned. Please visit [INSERT with Table DML Factor with MERGE as DML](../../../../translation-references/transact/transact-dmls.md) to get more information about this pattern.

#### Input Code

##### Sql Server

```sql
 INSERT INTO T3
SELECT
 col1,
  col2
FROM (
  MERGE T1 USING T2
   ON T1.col1 = T2.col1
  WHEN NOT MATCHED THEN
    INSERT VALUES ( T2.col1, T2.col2 )
  WHEN MATCHED THEN
    UPDATE SET T1.col2 = t2.col2
  OUTPUT
   $action ACTION_OUT,
    T2.col1,
    T2.col2
) AS MERGE_OUT
 WHERE ACTION_OUT='UPDATE';
```

##### Generated Code

##### Snowflake

```sql
 --** SSC-FDM-TS0026 - DELETE CASE IS NOT BEING CONSIDERED, PLEASE CHECK IF THE ORIGINAL MERGE PERFORMS IT **
CREATE OR REPLACE TEMPORARY TABLE MERGE_OUT AS
 SELECT
  CASE
   WHEN T1.$1 IS NULL
    THEN 'INSERT'
   ELSE 'UPDATE'
  END ACTION_OUT,
  T2.col1,
  T2.col2
 FROM
  T2
  LEFT JOIN
   T1
   ON T1.col1 = T2.col1;

MERGE INTO T1
USING T2
ON T1.col1 = T2.col1
WHEN NOT MATCHED THEN
    INSERT VALUES (T2.col1, T2.col2)
WHEN MATCHED THEN
 UPDATE SET
  T1.col2 = t2.col2
  !!!RESOLVE EWI!!! /*** SSC-EWI-0021 - OUTPUT CLAUSE NOT SUPPORTED IN SNOWFLAKE ***/!!!
  OUTPUT
   $action ACTION_OUT,
    T2.col1,
    T2.col2 ;

  INSERT INTO T3
  SELECT
 col1,
 col2
  FROM
 MERGE_OUT
  WHERE
 ACTION_OUT ='UPDATE';
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0027

SET ANSI_NULLS ON statement may have a different behavior in Snowflake

### Description

This FDM notifies that the SET ANSI_NULLS ON statement may behave differently in Snowflake. For more information about this statement,
go to the [ANSI_NULLS](../../../../translation-references/transact/transact-ansi-nulls.md) article.

#### Input Code

```sql
 SET ANSI_NULLS ON;
```

##### Generated Code

```sql
 ----** SSC-FDM-TS0027 - SET ANSI_NULLS ON STATEMENT MAY HAVE A DIFFERENT BEHAVIOR IN SNOWFLAKE **
--SET ANSI_NULLS ON
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0028

Output parameters must have the same order as they appear in the executed code

### Description

This FDM notifies that the output parameters in the SP_EXECUTESQL statement must be in the same order as they appear in the SQL string to execute. Otherwise, the output values will not be correctly assigned.

### Code Example

#### Correct case

As can be seen, `@MaxAgeOUT` and `@MaxIdOU`T appear in the same order in both the SQL string and the output parameters.

Thus, when converting the code, the `SELECT $1, $2 INTO :MAXAGE, :MAXID FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()))` will assign the values correctly.

##### Transact

```sql
 CREATE PROCEDURE CORRECT_OUTPUT_PARAMS_ORDER
AS
BEGIN
    DECLARE @MaxAge INT;
    DECLARE @MaxId INT;

    EXECUTE sp_executesql
        N'SELECT @MaxAgeOUT = max(AGE), @MaxIdOut = max(ID) FROM PERSONS WHERE ID < @id AND AGE < @age;',
        N'@age INT, @id INT, @MaxAgeOUT INT OUTPUT, @MaxIdOUT INT OUTPUT',
        30,
        100,
        @MaxAgeOUT = @MaxAge OUTPUT,
        @MaxIdOut = @MaxId OUTPUT;

    SELECT @MaxAge, @MaxId;
END
```

##### Snowflake

```sql
 CREATE OR REPLACE PROCEDURE CORRECT_OUTPUT_PARAMS_ORDER ()
RETURNS TABLE()
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "10/07/2024" }}'
EXECUTE AS CALLER
AS
$$
  DECLARE
    MAXAGE INT;
    MAXID INT;
    ProcedureResultSet RESULTSET;
  BEGIN

    !!!RESOLVE EWI!!! /*** SSC-EWI-0030 - THE STATEMENT BELOW HAS USAGES OF DYNAMIC SQL. ***/!!!
    EXECUTE IMMEDIATE TRANSFORM_SP_EXECUTE_SQL_STRING_UDF('SELECT
   MAX(AGE),
   MAX(ID) FROM
   PERSONS
WHERE
   ID < @id AND AGE < @age;', '@age INT, @id INT, @MaxAgeOUT INT OUTPUT, @MaxIdOUT INT OUTPUT', ARRAY_CONSTRUCT('', '', 'MAXAGEOUT', 'MAXIDOUT'), ARRAY_CONSTRUCT(
    30,
    100, :MAXAGE, :MAXID));
    --** SSC-FDM-TS0028 - OUTPUT PARAMETERS MUST HAVE THE SAME ORDER AS THEY APPEAR IN THE EXECUTED CODE **
    SELECT
      $1,
      $2
    INTO
      :MAXAGE,
      :MAXID
    FROM
      TABLE(RESULT_SCAN(LAST_QUERY_ID()));
    ProcedureResultSet := (
    SELECT
      :MAXAGE,
      :MAXID);
    RETURN TABLE(ProcedureResultSet);
  END;
$$;
```

#### Problematic case

As can be seen, `@MaxAgeOUT` and `@MaxIdOUT` in the output parameters appear in a different order compared to the SQL string.

Thus, when converting the code, the `SELECT $1, $2 INTO :MAXID, :MAXAGE FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()))` will assign the values incorrectly. `Max(AGE)` will be assigned to `:MAXID` and `Max(ID)` to `:MAXAGE`.

This needs to be manually fixed by either changing the order of the output parameters in the SELECT INTO statement or by changing the order in the SQL string.

##### Transact

```sql
 CREATE PROCEDURE INCORRECT_OUTPUT_PARAMS_ORDER
AS
BEGIN
    DECLARE @MaxAge INT;
    DECLARE @MaxId INT;

    EXECUTE sp_executesql
        N'SELECT @MaxAgeOUT = max(AGE), @MaxIdOut = max(ID) FROM PERSONS WHERE ID < @id AND AGE < @age;',
        N'@age INT, @id INT, @MaxAgeOUT INT OUTPUT, @MaxIdOUT INT OUTPUT',
        30,
        100,
        @MaxIdOut = @MaxId OUTPUT,
        @MaxAgeOUT = @MaxAge OUTPUT;

    SELECT @MaxAge, @MaxId;
END
```

##### Snowflake

```sql
 CREATE OR REPLACE PROCEDURE INCORRECT_OUTPUT_PARAMS_ORDER ()
RETURNS TABLE()
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "10/07/2024" }}'
EXECUTE AS CALLER
AS
$$
  DECLARE
    MAXAGE INT;
    MAXID INT;
    ProcedureResultSet RESULTSET;
  BEGIN

    !!!RESOLVE EWI!!! /*** SSC-EWI-0030 - THE STATEMENT BELOW HAS USAGES OF DYNAMIC SQL. ***/!!!
    EXECUTE IMMEDIATE TRANSFORM_SP_EXECUTE_SQL_STRING_UDF('SELECT
   MAX(AGE),
   MAX(ID) FROM
   PERSONS
WHERE
   ID < @id AND AGE < @age;', '@age INT, @id INT, @MaxAgeOUT INT OUTPUT, @MaxIdOUT INT OUTPUT', ARRAY_CONSTRUCT('', '', 'MAXIDOUT', 'MAXAGEOUT'), ARRAY_CONSTRUCT(
    30,
    100, :MAXID, :MAXAGE));
    --** SSC-FDM-TS0028 - OUTPUT PARAMETERS MUST HAVE THE SAME ORDER AS THEY APPEAR IN THE EXECUTED CODE **
    SELECT
      $1,
      $2
    INTO
      :MAXID,
      :MAXAGE
    FROM
      TABLE(RESULT_SCAN(LAST_QUERY_ID()));
    ProcedureResultSet := (
    SELECT
      :MAXAGE,
      :MAXID);
    RETURN TABLE(ProcedureResultSet);
  END;
$$;
```

### Best Practices

* Make sure the OUTPUT parameters are in the same order as they appear in the SQL string.
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0029

SET NOCOUNT statement is commented out, which is not applicable in Snowflake.

### Description

When SnowConvert AI encounters a `SET NOCOUNT` statement, it adds this FDM. SnowConvert AI then comments out the `SET NOCOUNT` statement because it is not relevant in the Snowflake environment.

### Code example

#### Input Code

```sql
 SET NOCOUNT ON;
```

##### Generated Code

```sql
 ----** SSC-FDM-TS0029 - SET NOCOUNT STATEMENT IS COMMENTED OUT, WHICH IS NOT APPLICABLE IN SNOWFLAKE. **
--SET NOCOUNT ON
```

### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0030

SET ANSI_PADDING ON statement is commented out, which is equivalent in Snowflake.

### Description

Snowflake always preserves trailing spaces in string values when they are inserted into columns. This behavior is equivalent to `SET ANSI_PADDING ON` in SQL Server. Therefore, when SnowConvert AI encounters a `SET ANSI_PADDING ON` statement, it adds this FDM and comments it out.

### Code example

#### Input Code

```sql
 SET ANSI_PADDING ON;
```

##### Generated Code

```sql
 ----** SSC-FDM-TS0030 - SET ANSI_PADDING ON STATEMENT IS COMMENTED OUT, WHICH IS EQUIVALENT IN SNOWFLAKE. **
--SET ANSI_PADDING ON
```

### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0031

SET ANSI_WARNINGS ON statement is commented out because Snowflake generally adheres to ANSI-standard behaviors.

### Description

Snowflake generally behaves as if `ANSI_WARNINGS` is `ON` by default, especially concerning error handling for arithmetic overflow, division by zero, and string truncation. You typically don’t need to explicitly “set” an equivalent to `ANSI_WARNINGS` in Snowflake. Therefore, when SnowConvert AI encounters a `SET ANSI_WARNINGS ON` statement, it adds this FDM and comments it out.

### Code example

#### Input Code

```sql
 SET ANSI_WARNINGS ON;
```

##### Generated Code

```sql
 ----** SSC-FDM-TS0031 - SET ANSI_WARNINGS ON STATEMENT IS COMMENTED OUT, WHICH SNOWFLAKE GENERALLY ADHERES TO ANSI-STANDARD BEHAVIORS. **
--SET ANSI_WARNINGS ON
```

### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0032

IDENTITY column property not supported in CREATE TABLE AS STATEMENT, emulated using ROW_NUMBER().

### Description

Snowflake does not have a direct way to perform a CREATE TABLE AS with an identity column. Although SnowConvert adds a ROW_NUMBER column instead of the IDENTITY to simulate the enumeration of the identity. This transformation does not create an identity column, which means rows inserted after creation won’t be automatically incremented.

### Code example

#### Input Code

```sql
with peers as
(
    select
    *
    from (
    values
        ('Luis', 'Miguel'),
        ('Cory', 'Wong'),
        ('Steve', 'Vai'),
        ('John', 'Petrucci'),
        ('Paul', 'Gilbert')
    ) as info(name, lastname)
)
select
    rowm = IDENTITY(int,1,1),
    *
into #MYTABLE
from peers;
```

##### Generated Code

```sql
--** SSC-FDM-TS0032 - IDENTITY COLUMN PROPERTY NOT SUPPORTED IN CREATE TABLE AS STATEMENT, EMULATED WITH USING ROW_NUMBER **
CREATE OR REPLACE TEMPORARY TABLE T_MYTABLE AS
     WITH peers as
(
    select
     *
    from (
    values
        ('Luis', 'Miguel'),
        ('Cory', 'Wong'),
        ('Steve', 'Vai'),
        ('John', 'Petrucci'),
        ('Paul', 'Gilbert')
    ) as info (
      name,
      lastname
     )
)
     SELECT
    ROW_NUMBER()
    OVER (
    ORDER BY
     NULL) AS rowm,
    *
from
    peers;
```

### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0033

SET QUOTED_IDENTIFIER STATEMENT MAY HAVE A DIFFERENT BEHAVIOR IN SNOWFLAKE.

### Description

**SQL Server Behavior**

In SQL Server, SET QUOTED_IDENTIFIER ON is a syntax setting that is separate from collation. The database’s or column’s collation (for example,_CI for Case-Insensitive or _CS for Case-Sensitive) dictates whether quoted identifiers are case-sensitive or not. If a database has a_CI collation, then “MyColumn” and “mycolumn” are treated as the same.

**Snowflake Behavior**

In Snowflake, the behavior is simpler and more strict:

Unquoted Identifiers: Automatically stored and resolved in all uppercase, making them case-insensitive (mytable is the same as MYTABLE).

Quoted Identifiers: By default, identifiers enclosed in double quotes (“MyColumn”) are case-sensitive. They are stored exactly as you typed them.

### Code example

#### Input Code

```sql
SET QUOTED_IDENTIFIER ON
GO

-- the table is defined as "Products Test"
-- this query will work because the case is ignored.
select
*
from [products test];

SET QUOTED_IDENTIFIER OFF

-- this query will fail because the case is preserved
select
*
from [products test];
GO
```

##### Generated Code

```sql
----** SSC-FDM-TS0033 - SET QUOTED_IDENTIFIER STATEMENT MAY HAVE A DIFFERENT BEHAVIOR IN SNOWFLAKE **
--SET QUOTED_IDENTIFIER ON

-- the table is defined as "Products Test"
-- this query will work because the case is ignored.
select
  *
from
  "products test";

----** SSC-FDM-TS0033 - SET QUOTED_IDENTIFIER STATEMENT MAY HAVE A DIFFERENT BEHAVIOR IN SNOWFLAKE **
--SET QUOTED_IDENTIFIER OFF

-- this query will fail because the case is preserved
select
  *
from
  "products test";
```

**How to Achieve Equivalence in Snowflake**

To get the same case-insensitive behavior for quoted identifiers as in SQL Server, you can set the QUOTED_IDENTIFIERS_IGNORE_CASE session parameter to TRUE in Snowflake.

```sql
-- This will make quoted identifiers case-insensitive for the session
ALTER SESSION SET QUOTED_IDENTIFIERS_IGNORE_CASE = TRUE;

-- Now, this query will succeed
select
  *
from
  "products test";
```

### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-TS0034

### Description

This FDM is generated when a `DATA_COMPRESSION` clause is encountered in a `CREATE TABLE` or `ALTER TABLE` statement. In SQL Server, `DATA_COMPRESSION` is used to specify whether data should be compressed (using ROW or PAGE compression) to reduce storage space and improve I/O performance. **Snowflake automatically handles data compression** using its proprietary compression algorithms, making the `DATA_COMPRESSION` clause unnecessary and unsupported. SnowConvert comments out the `DATA_COMPRESSION` clause during conversion.

### Example Code

#### Input (SQL Server)

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name NVARCHAR(100),
    Department NVARCHAR(50),
    Salary DECIMAL(10, 2)
)
WITH (DATA_COMPRESSION = PAGE);
```

#### Output (Snowflake)

```sql
CREATE OR REPLACE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name NVARCHAR(100),
    Department NVARCHAR(50),
    Salary DECIMAL(10, 2)
)
WITH (
--    --** SSC-FDM-TS0034 - DATA_COMPRESSION IS AUTOMATICALLY HANDLED BY SNOWFLAKE. **
--    DATA_COMPRESSION = PAGE
                           )
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "11/06/2025",  "domain": "no-domain-provided",  "migrationid": "sFmaAZAnCnm6VvGeJrE4BQ==" }}'
;
```

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
