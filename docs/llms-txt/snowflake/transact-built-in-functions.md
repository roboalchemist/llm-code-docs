# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/transact/transact-built-in-functions.md

# SnowConvert AI - SQL Server-Azure Synapse - Built-in functions

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> For more information about built-in functions and their Snowflake equivalents, also see [Common built-in functions](../general/built-in-functions.md).

## Aggregate

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| TransactSQL | Snowflake | Notes |
| APPROX_COUNT_DISTINCT | APPROX_COUNT_DISTINCT |  |
| AVG​ | AVG |  |
| CHECKSUM_AGG | *\*to be defined* |  |
| COUNT | COUNT |  |
| COUNT_BIG | *\*to be defined* |  |
| GROUPING | GROUPING |  |
| GROUPING_ID | GROUPING_ID |  |
| MAX | MAX |  |
| MIN | MIN |  |
| STDEV | STDDEV, STDEV_SAMP |  |
| STDEVP | STDDEV_POP |  |
| SUM | SUM |  |
| VAR | VAR_SAMP |  |
| VARP | VAR_POP​ |  |

## Analytic

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| CUME_DIST | CUME_DIST |  |
| FIRST_VALUE | FIRST_VALUE |  |
| LAG | LAG |  |
| LAST_VALUE | LAST_VALUE |  |
| LEAD | LEAD |  |
| PERCENTILE_CONT | PERCENTILE_CONT |  |
| PERCENTILE_DISC | PERCENTILE_DISC |  |
| PERCENT_RANK | PERCENT_RANK |  |

## Collation

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| COLLATIONPROPERTY | *\*to be defined* |  |
| TERTIARY_WEIGHTS | *\*to be defined* |  |

## Configuration

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| ​@@DBTS | *\*to be defined* |  |
| @@LANGID | *\*to be defined* |  |
| @@LANGUAGE | *\*to be defined* |  |
| @@LOCK_TIMEOUT | *\*to be defined* |  |
| @@MAX_CONNECTIONS | *\*to be defined* |  |
| @@MAX_PRECISION | *\*to be defined* |  |
| @@NESTLEVEL | *\*to be defined* |  |
| @@OPTIONS | *\*to be defined* |  |
| @@REMSERVER | *\*to be defined* |  |
| @@SERVERNAME | CONCAT(’[app.snowflake.com](http://app.snowflake.com/)’, CURRENT_ACCOUNT( )) |  |
| @@SERVICENAME | *\*to be defined* |  |
| @@SPID | *\*to be defined* |  |
| @@TEXTSIZE | *\*to be defined* |  |
| @@VERSION | *\*to be defined* | Can be mimicked by using CURRENT_VERSION |

## Conversion

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| CAST | CAST | Returns NULL if the value isn’t a number, otherwise returns the numeric value as its. When using operators such as <, >, =, <> then must be followed by a NULL |
| CONVERT | Check CONVERT | Same behavior as CAST |
| PARSE | *\*to be defined* |  |
| TRY_CAST | TRY_CAST | Returns NULL if the value isn’t a number, otherwise returns the numeric value as its. When using operators such as <, >, =, <> then must be followed by a NULL |
| TRY_CONVERT | *\*to be defined* | Same behavior as TRY_CAST |
| TRY_PARSE | TRY_CAST | Behavior may be different when parsing an integer as date or timestamp. |

## Cryptographic

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| ASYMKEY_ID | *\*to be defined* |  |
| ASYMKEYPROPERTY | *\*to be defined* |  |
| CERTENCODED | *\*to be defined* |  |
| CERTPRIVATEKEY | *\*to be defined* |  |
| DECRYPTBYASYMKEY | *\*to be defined* |  |
| DECRYPTBYCERT | *\*to be defined* |  |
| DECRYPTBYKEY | *\*to be defined* |  |
| DECRYPTBYKEYAUTOASYMKEY | *\*to be defined* |  |
| DECRYPTBYKEYAUTOCERT | *\*to be defined* |  |
| DECRYPTBYPASSPHRASE | _\*to be defined_​ | Can be mimicked by using DENCRYPT_RAW |
| ENCRYPTBYASYMKEY | *\*to be defined* |  |
| ENCRYPTBYCERT | *\*to be defined* |  |
| ENCRYPTBYKEY | *\*to be defined* |  |
| ENCRYPTBYPASSPHRASE | *\*to be defined* | Can be mimicked by using ENCRYPT_RAW |
| HASHBYTES | **MD5, SHA1, SHA2** | Currently only supported separated hash. Use proper one according to the required algorithm  **MD5**, is a 32-character hex-encoded  **SHA1**, has a 40-character hex-encoded string containing the 160-bit  **SHA2**, a hex-encoded string containing the N-bit SHA-2 message digest. Sizes are:  224 = SHA-224  256 = SHA-256 (Default)  384 = SHA-384  512 = SHA-512 |
| IS_OBJECTSIGNED | *\*to be defined* |  |
| KEY_GUID | *\*to be defined* |  |
| KEY_ID | *\*to be defined* |  |
| KEY_NAME | *\*to be defined* |  |
| SIGNBYASYMKEY | *\*to be defined* |  |
| SIGNBYCERT | *\*to be defined* |  |
| SYMKEYPROPERTY | *\*to be defined* |  |
| VERIFYSIGNEDBYCERT | *\*to be defined* |  |

## Cursor

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| @@CURSOR_ROWS | *\*to be defined* | ​ |
| @@FETCH_STATUS | *\*to be defined* |  |
| CURSOR_STATUS | *\*to be defined* |  |

## Data type

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| DATALENGTH | OCTET_LENGTH | ​Snowflake doesn’t use fractional bytes so length is always calculated as 8 \* OCTET_LENGTH |
| IDENT_SEED | *\*to be defined* |  |
| IDENT_CURRENT | *\*to be defined* |  |
| IDENTITY | *\*to be defined* |  |
| IDENT_INCR | *\*to be defined* |  |
| SQL_VARIANT_PROPERTY | *\*to be defined* |  |

## Date & Time

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| @@DATEFIRST | *\*to be defined* |  |
| @@LANGUAGE | *\*to be defined* |  |
| CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |  |
| CURRENT_TIMEZONE | *\*to be defined* |  |
| DATEADD | DATEADD |  |
| DATEDIFF | DATEDIFF |  |
| DATEDIFF_BIG | *\*to be defined* |  |
| DATEFROMPARTS | DATE_FROM_PARTS |  |
| DATENAME | *\*to be defined* | This function receives two arguments: a datepart and date. It returns a string. Here are the supported dateparts from TSQL to Snowflake  **year, yyyy, yy** -> DATE_PART(YEAR, “$date”) **quarter, qq, q** -> DATE_PART(QUARTER, “$date”) **month, mm, m** -> **MONTHNAME**( “$date”), though only providing a three-letter english month name **dayofyear, dy, y** -> DATE_PART(DAYOFYEAR, “$date”) **day, dd, d** -> DATE_PART(DAY, “$date”) **week, wk, ww** -> DATE_PART(WEEK, “$date”)  **weekday, dw** -> **DAYNAME**(“$date”), though only providing an three-letter english day name **hour, hh** -> DATE_PART(HOUR, “$date”) **minute, n** -> DATE_PART(MINUTE, “$date”) **second, ss, s** -> DATE_PART(SECOND, “$date”) **millisecond, ms** -> DATE_PART(MS, “$date”) **microsecond, mcs** -> DATE_PART(US, “$date”) **nanosecond, ns** -> DATE_PART(NS, “$date”) **TZoffset, tz** -> needs a special implementation to get the time offset |
| DATEPART | DATE_PART |  |
| DATETIME2FROMPARTS | *\*to be defined* |  |
| DATETIMEFROMPARTS | *\*to be defined* | ​Can be mimicked by using a combination of **DATE_FROM_PARTS and TIME_FROM_PARTS** |
| DATETIMEOFFSETFROMPARTS | *\*to be defined* |  |
| DAY | DAY |  |
| EOMONTH | *\*to be defined* | Can be mimicked by using **LAST_DAY** |
| GETDATE | GETDATE |  |
| GETUTCDATE | *\*to be defined* | Can be mimicked by using **CONVERT_TIMEZONE** |
| ISDATE | *\*to be defined* | Can be mimicked by using **TRY_TO_DATE**  Returns NULL if the value isn’t a **date**, otherwise returns the date value as its. When using operators such as <, >, =, <> then must be followed by a NULL |
| MONTH | MONTH |  |
| SMALLDATETIMEFROMPARTS | *\*to be defined* | ​​Can be mimicked by using a combination of **DATE_FROM_PARTS and TIME_FROM_PARTS** |
| SWITCHOFFSET | *\*to be defined* | ​Can be mimicked by using **CONVERT_TIMEZONE** |
| SYSDATETIME | LOCALTIME |  |
| SYSDATETIMEOFFSET | *\*to be defined* | ​Can be mimicked by using **CONVERT_TIMEZONE and LOCALTIME** |
| SYSUTCDATETIME | *\*to be defined* | ​​Can be mimicked by using **CONVERT_TIMEZONE and LOCALTIME** |
| TIMEFROMPARTS | TIME_FROM_PARTS | ​ |
| TODATETIMEOFFSET | *\*to be defined* | ​Can be mimicked by using **CONVERT_TIMEZONE** |
| YEAR | YEAR |  |

## JSON

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| ISJSON | CHECK_JSON | ​This is a ‘preview feature’ in Snowflake |
| JSON_VALUE | *\*to be defined* | Can be mimic by using  TO_VARCHAR(GET_PATH(PARSE_JSON(JSON), PATH)) |
| JSON_QUERY | *\*to be defined* |  |
| JSON_MODIFY | *\*to be defined* |  |

## Mathematical

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| ABS | ABS |  |
| ACOS | ACOS |  |
| ASIN | ASIN |  |
| ATAN | ATAN |  |
| ATN2 | ATAN2 |  |
| CEILING | CEIL |  |
| COS | COS |  |
| COT | COT |  |
| DEGREES | DEGREES |  |
| EXP | EXP |  |
| FLOOR | FLOOR |  |
| LOG | LN |  |
| LOG10 | LOG |  |
| PI | PI |  |
| POWER | POWER |  |
| RADIANS | RADIANS |  |
| RAND | RANDOM |  |
| ROUND | ROUND |  |
| SIGN | SIGN |  |
| SIN | SIN |  |
| SQRT | SQRT |  |
| SQUARE | SQUARE |  |

## Logical

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| CHOOSE | *\*to be defined* | Can be mimic by using DECODE |
| GREATEST | GREATEST |  |
| IIF | IIF |  |
| LEAST | LEAST |  |
| NULLIF | NULLIF |  |

## Metadata

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| TransactSQL | Snowflake | Notes |
| @@PROCID | *\*to be defined* |  |
| APP_NAME | *\*to be defined* |  |
| APPLOCK_MODE | *\*to be defined* |  |
| APPLOCK_TEST | *\*to be defined* |  |
| ASSEMBLYPROPERTY | *\*to be defined* |  |
| COL_LENGTH | A UDF named COL_LENGTH_UDF is provided to retrieve this information. This UDF works only with VARCHAR types, as specified in the Transact-SQL documentation. For other data types, it returns NULL. |  |
| COL_NAME | *\*to be defined* |  |
| COLUMNPROPERTY | *\*to be defined* |  |
| DATABASE_PRINCIPAL_ID | *\*to be defined* | Maps to CURRENT_USER when no args |
| DATABASEPROPERTYEX | *\*to be defined* |  |
| DB_ID | *\*to be defined* | We recommend changing to CURRENT_DATABASE(). If there is a need to emulate this functionality.  SELECT DATE_PART(EPOCH,CREATED) FROM INFORMATION_SCHEMA.DATABASES WHERE DATABASE_NAME = ‘DB’ ;  Can achieve something similar |
| DB_NAME | *\*to be defined* | Mostly used in the procedurename mentioned above |
| FILE_ID | *\*to be defined* |  |
| FILE_IDEX | *\*to be defined* |  |
| FILE_NAME | *\*to be defined* |  |
| FILEGROUP_ID | *\*to be defined* |  |
| FILEGROUP_NAME | *\*to be defined* |  |
| FILEGROUPPROPERTY | *\*to be defined* |  |
| FILEPROPERTY | *\*to be defined* |  |
| FULLTEXTCATALOGPROPERTY | *\*to be defined* |  |
| FULLTEXTSERVICEPROPERTY | *\*to be defined* |  |
| INDEX_COL | *\*to be defined* |  |
| INDEXKEY_PROPERTY | *\*to be defined* |  |
| INDEXPROPERTY | *\*to be defined* |  |
| NEXT VALUE FOR | *\*to be defined* |  |
| OBJECT_DEFINITION | *\*to be defined* |  |
| OBJECT_ID | *\*to be defined* | In most cases can be replaced. Most cases are like: IF OBJECT_ID(‘dbo.TABLE’) IS NOT NULL DROP TABLE dbo.Table which can be replaced by a DROP TABLE IF EXISTS (this syntax is also supported in SQL SERVER). If the object_id needs to be replicated, a UDF is added depending on the second parameter of the function call. |
| OBJECT_NAME | *\*to be defined* | Can be replaced by: CREATE OR REPLACE PROCEDURE FOO() RETURNS STRING LANGUAGE JAVASCRIPT AS ‘ var rs = snowflake.execute({sqlText:`SELECT CURRENT_DATABASE() | '.' | ?`, binds:[arguments.callee.name]}); rs.next(); var procname = rs.getColumnValue(1); return procname; ‘; |
| OBJECT_NAME(@@PROCID) | ‘ObjectName’ | This transformation only occurs when it is inside a DeclareStatement.  ObjectName is the name of the TopLevelObject that contains the Function. |
| OBJECT_SCHEMA_NAME | *\*to be defined* |  |
| OBJECT_SCHEMA_NAME(@@PROCID) | :OBJECT_SCHEMA_NAME | This transformation only occurs when it is inside a DeclareStatement. |
| OBJECTPROPERTY | *\*to be defined* |  |
| OBJECTPROPERTYEX | *\*to be defined* |  |
| ORIGINAL_DB_NAME | *\*to be defined* |  |
| PARSENAME | PARSENAME_UDF | It creates a UDF to emulate the same behavior of Parsename function. |
| *\*to be defined* |  |  |
| SCHEMA_NAME | *\*to be defined* |  |
| SCOPE_IDENTITY | *\*to be defined* | It this is needed I would recommend to use sequences, and capture the value before insert |
| SERVERPROPERTY | *\*to be defined* |  |
| STATS_DATE | *\*to be defined* |  |
| TYPE_ID | *\*to be defined* |  |
| TYPE_NAME | *\*to be defined* |  |
| TYPEPROPERTY | *\*to be defined* |  |
| VERSION | *\*to be defined* |  |

## Ranking

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| DENSE_RANK | DENSE_RANK |  |
| NTILE | NTILE |  |
| RANK | RANK |  |
| ROW_NUMBER | ROW_NUMBER |  |

## Replication

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| PUBLISHINGSERVERNAME | *\*to be defined* |  |

## Rowset

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| OPENDATASOURCE | *\*to be defined* |  |
| OPENJSON | *\*to be defined* |  |
| QPENQUERY | *\*to be defined* |  |
| OPENROWSET | *\*to be defined* |  |
| OPENXML | OPENXML_UDF | User-defined function used as a equivalent behavior in Snowflake. |
| STRING_SPLIT | SPLIT_TO_TABLE | The enable_ordinal flag in Transact-SQL’s STRING_SPLIT is not directly supported by Snowflake’s SPLIT_TO_TABLE function. If the ordinal column is required, a user-defined function (UDF) named STRING_SPLIT_UDF will be generated to replicate this behavior. Without the ordinal column, note that STRING_SPLIT returns a single column named value, while SPLIT_TO_TABLE returns three columns: value, index (equivalent to ordinal), and seq. For additional details, see the [SPLIT_TO_TABLE documentation](https://docs.snowflake.com/en/sql-reference/functions/split_to_table). |

## Security

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| CERTENCODED | *\*to be defined* |  |
| CERTPRIVATEKEY | *\*to be defined* |  |
| CURRENT_USER | CURRENT_USER |  |
| DATABASE_PRINCIPAL_ID | *\*to be defined* |  |
| HAS_PERMS_BY_NAME | *\*to be defined* |  |
| IS_MEMBER | *\*to be defined* | Change to query INFORMATION_SCHEMA although the client might require defining new roles |
| IS_ROLEMEMBER | *\*to be defined* | Snowflake’s a similar function  **IS_ROLE_IN_SESSION** |
| IS_SRVROLEMEMBER | *\*to be defined* |  |
| LOGINPROPERTY | *\*to be defined* |  |
| ORIGINAL_LOGIN | *\*to be defined* |  |
| PERMISSIONS | *\*to be defined* |  |
| PWDCOMPARE | *\*to be defined* |  |
| PWDENCRYPT | *\*to be defined* |  |
| SCHEMA_ID | *\*to be defined* |  |
| SCHEMA_NAME | *\*to be defined* |  |
| SESSION_USER | *\*to be defined* |  |
| SUSER_ID | *\*to be defined* |  |
| SUSER_NAME | *\*to be defined* |  |
| SUSER_SID | *\*to be defined* |  |
| SUSER_SNAME | *\*to be defined* |  |
| sys.fn_builtin_permissions | *\*to be defined* |  |
| sys.fn_get_audit_file | *\*to be defined* |  |
| sys.fn_my_permissions | *\*to be defined* |  |
| SYSTEM_USER | *\*to be defined* |  |
| USER_ID | *\*to be defined* |  |
| USER_NAME | *\*to be defined* | Maps to CURRENT_USER |

## String

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| ASCII | ASCII |  |
| CHAR | CHR, CHAR |  |
| CHARINDEX | CHARINDEX |  |
| CONCAT | CONCAT |  |
| CONCAT_WS | CONCAT_WS |  |
| COALESCE | COALESCE |  |
| DIFFERENCE | *\*to be defined* |  |
| FORMAT | TO_CHAR | The SSC-EWI-0006 or SSC-FDM-0036 could be generated when the format (numeric or date time) is not fully supported. |
| LEFT | LEFT |  |
| LEN | LEN |  |
| LOWER | LOWER |  |
| LTRIM | LTRIM |  |
| NCHAR | *\*to be defined* |  |
| PATINDEX | *\*to be defined* | Map to REGEXP_INSTR |
| QUOTENAME | QUOTENAME_UDF | It creates a UDF to emulate the same behavior of Quotename function |
| REPLACE | REPLACE |  |
| REPLICATE | REPEAT |  |
| REVERSE | REVERSE |  |
| RIGHT | RIGHT |  |
| RTRIM | RTRIM |  |
| SOUNDEX | SOUNDEX |  |
| SPACE | *\*to be defined* |  |
| STR | *\*to be defined* |  |
| STRING_AGG | *\*to be defined* |  |
| STRING_ESCAPE | *\*to be defined* |  |
| STRING_SPLIT | SPLIT_TO_TABLE |  |
| STUFF | *\*to be defined* | CREATE OR REPLACE FUNCTION STUFF(S string, STARTPOS int, LENGTH int, NEWSTRING string) RETURNS string LANGUAGE SQL AS ‘ left(S, STARTPOS) |
| SUBSTRING | SUBSTRING |  |
| TRANSLATE | TRANSLATE |  |
| TRIM | TRIM |  |
| UNICODE | UNICODE |  |
| UPPER | UPPER |  |

## System

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| $PARTITION | *\*to be defined* |  |
| @@ERROR | *\*to be defined* |  |
| @@IDENTITY | *\*to be defined* | It this is needed I would recommend to use sequences, and capture the value before insert |
| @@PACK_RECEIVED | *\*to be defined* |  |
| @@ROWCOUNT | *\*to be defined* |  |
| @@TRANCOUNT | *\*to be defined* |  |
| BINARY_CHECKSUM | *\*to be defined* |  |
| CHECKSUM | *\*to be defined* |  |
| COMPRESS | COMPRESS | ​Snowflake’s version has a method argument to indicate the compression method. These are the valid values: **SNAPPY, ZLIB, ZSTD, BZ2**  The compression level is specified in parentheses and must be a non-negative integer |
| CONNECTIONPROPERTY | *\*to be defined* |  |
| CONTEXT_INFO | *\*to be defined* |  |
| CURRENT_REQUEST_ID | *\*to be defined* |  |
| CURRENT_TRANSACTION_ID | *\*to be defined* |  |
| DECOMPRESS | *\*to be defined* | Snowflake has two functions for these: **DECOMPRESS_BINARY** and **DECOMPRESS_STRING**​ |
| ERROR_LINE | *\*to be defined* | SnowScript: Not supported in Snowflake with **[SSC-EWI-0040](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md)**.  JavaScript: Will map to **ERROR_LINE** helper. EXEC helper will capture the Exception line property from the stack trace. |
| ERROR_MESSAGE | SQLERRM | Added **SSC-FDM-TS0023** returned error message could be different in Snowflake. |
| ERROR_NUMBER | *\*to be defined* | SnowScript: Not supported in Snowflake with **[SSC-EWI-0040](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md)**.  JavaScript: Will map to **ERROR_NUMBER** helper. EXEC helper will capture the Exception code property. |
| ERROR_PROCEDURE | *Mapped* | SnowScript: Use current procedure name, added **SSC-FDM-TS0023** result value is based on the stored procedure where the function is called instead of where the exception occurs.  JavaScript: Will map to **ERROR_PROCEDURE** helper, taken from the `arguments.callee.name` procedure property |
| ERROR_SEVERITY | *\*to be defined* | SnowScript: Not supported in Snowflake with **[SSC-EWI-0040](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md)**. |
| ERROR_STATE | SQLSTATE | SnowScript: Converted to **SQLSTATE** snowflake property, added **SSC-FDM-TS0023** returned value could be different in Snowflake.  JavaScript: Helper will capture Exception state property |
| FORMATMESSAGE | FORMATEMESSAGE_UDF | It creates a UDF to emulate the same behavior of FORMATMESSAGE function but with some limitations. |
| GET_FILESTREAM_TRANSACTION_CONTEXT | *\*to be defined* |  |
| GETANSINULL | *\*to be defined* |  |
| HOST_ID | *\*to be defined* |  |
| HOST_NAME | *\*to be defined* |  |
| ISNULL | NVL |  |
| ISNUMERIC | *\*to be defined* | No direct equivalent but can be mapped to a custom UDF, returning the same values as in TSQL. |
| MIN_ACTIVE_ROWVERSION | *\*to be defined* | ​ |
| NEWID | *\*to be defined* | ​Maps to UUID_STRING |
| NEWSEQUENTIALID | *\*to be defined* | ​ |
| ROWCOUNT_BIG | *\*to be defined* | ​ |
| SESSION_CONTEXT | *\*to be defined* | ​ |
| SESSION_ID | *\*to be defined* | ​ |
| XACT_STATE | *\*to be defined* | ​ |

## System Statistical

| TransactSql | Snowflake | Notes |
| --- | --- | --- |
| @@CONNECTIONS | *\*to be defined* | ​Snowflake’s a similar function: **LOGIN_HISTORY.**  Returns login events within a specified time range |
| @@PACK_RECEIVED | *\*to be defined* |  |
| @@CPU_BUSY | *\*to be defined* |  |
| @@PACK_SENT | *\*to be defined* |  |
| @@TIMETICKS | *\*to be defined* |  |
| @@IDLE | *\*to be defined* |  |
| @@TOTAL_ERRORS | *\*to be defined* |  |
| @@IO_BUSY | *\*to be defined* |  |
| @@TOTAL_READ | *\*to be defined* |  |
| @@PACKET_ERRORS | *\*to be defined* |  |
| @@TOTAL_WRITE | *\*to be defined* |  |

## Text & Image

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| TEXTPTR | *\*to be defined* |  |
| TEXTVALID | *\*to be defined* |  |

## Trigger

| TransactSQL | Snowflake | Notes |
| --- | --- | --- |
| COLUMNS_UPDATED | *\*to be defined* |  |
| EVENTDATA | *\*to be defined* |  |
| TRIGGER_NESTLEVEL | *\*to be defined* |  |
| UPDATE | *\*to be defined* |  |

# System functions

This section describes the functional equivalents of system functions in Transact-SQL to Snowflake SQL and JavaScript code, oriented to the creation of UDFs in Snowflake.

## ISNULL

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Replaces NULL with the specified replacement value. ([ISNULL in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/isnull-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
ISNULL ( check_expression , replacement_value )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/nvl.html)

```sql
NVL( <expr1> , <expr2> )
```

### Examples

#### SQL Server

```sql
SELECT ISNULL(NULL, 'SNOWFLAKE') AS COMPANYNAME;
```

**Result:**

| COMPANYNAME |
| --- |
| SNOWFLAKE |

##### Snowflake SQL

```sql
SELECT
NVL(NULL, 'SNOWFLAKE') AS COMPANYNAME;
```

**Result:**

| COMPANYNAME |
| --- |
| SNOWFLAKE |

## NEWID

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Creates a unique value of type uniqueidentifier. ([NEWID in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/newid-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
NEWID ( )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/nvl.html)

```sql
UUID_STRING()
```

### Examples

> **Warning:**
>
> Outputs may differ because it generates a unique ID in runtime

#### SQL Server

```sql
SELECT NEWID ( ) AS ID;
```

**Result:**

| ID |
| --- |
| 47549DDF-837D-41D2-A59C-A6BC63DF7910 |

##### Snowflake SQL

```sql
SELECT
UUID_STRING( ) AS ID;
```

**Result:**

| ID |
| --- |
| 6fd4312a-7925-4ad9-85d8-e039efd82089 |

## NULLIF

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a null value if the two specified expressions are equal.

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
NULLIF ( check_expression , replacement_value )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/nullif.html)

```sql
NULLIF( <expr1> , <expr2> )
```

### Examples

#### SQL Server

```sql
SELECT NULLIF(6,9) AS RESULT1, NULLIF(5,5) AS RESULT2;
```

**Result:**

| RESULT1 | RESULT2 |
| --- | --- |
| 6 | null |

##### Snowflake SQL

```sql
SELECT
NULLIF(6,9) AS RESULT1,
NULLIF(5,5) AS RESULT2;
```

**Result:**

| RESULT1 | RESULT2 |
| --- | --- |
| 6 | null |

## @@ROWCOUNT

Applies to

* SQL Server

### Description

Returns the number of rows affected by the last statement. ([@@ROWCOUNT in Transact-SQL](https://learn.microsoft.com/en-us/sql/t-sql/functions/rowcount-transact-sql?view=sql-server-ver16)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
@@ROWCOUNT
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/developer-guide/snowflake-scripting/dml-status)

```sql
SQLROWCOUNT
```

### Examples

#### SQL Server

```sql
CREATE TABLE table1
(
    column1 INT
);

CREATE PROCEDURE procedure1
AS
BEGIN
    declare @addCount int = 0;

    INSERT INTO table1 (column1) VALUES (1),(2),(3);
    set @addCount = @addCount + @@ROWCOUNT

   select @addCount
END
;
GO

EXEC procedure1;
```

**Result:**

|  |
| --- |
| 3 |

##### Snowflake SQL

```sql
CREATE OR REPLACE TABLE table1
(
    column1 INT
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "11/13/2024",  "domain": "test" }}'
;

CREATE OR REPLACE PROCEDURE procedure1 ()
RETURNS TABLE()
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "11/13/2024",  "domain": "test" }}'
EXECUTE AS CALLER
AS
$$
    DECLARE
        ADDCOUNT INT := 0;
        ProcedureResultSet RESULTSET;
    BEGIN

        INSERT INTO table1 (column1) VALUES (1),(2),(3);
        ADDCOUNT := :ADDCOUNT + SQLROWCOUNT;
        ProcedureResultSet := (

       select
            :ADDCOUNT);
        RETURN TABLE(ProcedureResultSet);
    END;
$$;

CALL procedure1();
```

**Result:**

| :ADDCOUNT |
| --- |
| 3 |

## FORMATMESSAGE

Applies to

* SQL Server

### Description

Constructs a message from an existing message in sys.messages or from a provided string. ([FORMATMESSAGE in Transact-SQL](https://learn.microsoft.com/en-us/sql/t-sql/functions/formatmessage-transact-sql?view=sql-server-ver16)).

### Sample Source Pattern

Since Snowflake does not support `FORMATMESSAGE` function, the FORMATMESSAGE_UDF is added to simulate its behavior.

### Syntax

#### SQL Server

```sql
FORMATMESSAGE ( { msg_number  | ' msg_string ' | @msg_variable} , [ param_value [ ,...n ] ] )
```

### Examples

#### SQL Server

```sql
SELECT FORMATMESSAGE('This is the %s and this is the %s.', 'first variable', 'second variable') AS RESULT;
```

**Result:**

| RESULT |
| --- |
| This is the first variable and this is the second variable. |

#### Snowflake

```sql
SELECT
--** SSC-FDM-TS0008 - FORMATMESSAGE WAS CONVERTED TO CUSTOM UDF FORMATMESSAGE_UDF AND IT MIGHT HAVE A DIFFERENT BEHAVIOR. **
FORMATMESSAGE_UDF('This is the %s and this is the %s.', ARRAY_CONSTRUCT('first variable', 'second variable')) AS RESULT;
```

**Result:**

| RESULT |
| --- |
| This is the first variable and this is the second variable. |

### Related EWIs

1. [SSC-FDM-TS0008](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/sqlServerFDM.md): FORMATMESSAGE function was converted to UDF.

## FORMATMESSAGE_UDF

Snowflake does not have a function with the functionality of `FORMATMESSAGE`. SnowConvert AI generates the following Python UDF to emulate the behavior of `FORMATMESSAGE`.

```sql
CREATE OR REPLACE FUNCTION FORMATMESSAGE_UDF(MESSAGE STRING, ARGS ARRAY)
RETURNS STRING
LANGUAGE python
IMMUTABLE
RUNTIME_VERSION = '3.8'
HANDLER = 'format_py'
as
$$
def format_py(message,args):
  return message % (*args,)
$$;
```

This UDF may not work correctly on some cases:

* Using the `%I64d` placeholder will throw an error.
* If the number of substitution arguments is different than the number of place holders, it will throw an error.
* Some unsigned placeholders like `%u` or `%X` will not behave properly when formatting the value.
* It cannot handle message_ids.

## String functions

This section describes the functional equivalents of string functions in Transact-SQL to Snowflake SQL and JavaScript code, oriented to the creation of UDFs in Snowflake.

## CHAR

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a single-byte character with the integer sent as a parameter on the ASCII table ([CHAR in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/char-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
CHAR( expression )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/chr.html)

```sql
{CHR | CHAR} ( <input> )
```

##### JavaScript

[JavaScript complete documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode)

```sql
String.fromCharCode( expression1, ... , expressionN )
```

### Examples

#### SQL Server

```sql
SELECT CHAR(170) AS SMALLEST_A
```

**Output:**

| SMALLEST_A |
| --- |
| ª |

##### Snowflake SQL

```sql
SELECT
CHAR(170) AS SMALLEST_A;
```

**Result:**

| SMALLEST_A |
| --- |
| ª |

##### JavaScript

```sql
CREATE OR REPLACE FUNCTION get_char(expression float)
RETURNS string
LANGUAGE JAVASCRIPT
AS
$$
  return String.fromCharCode( EXPRESSION );
$$;

SELECT GET_CHAR(170) SMALLEST_A;
```

**Result:**

| SMALLEST_A |
| --- |
| ª |

## CHARINDEX

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the index of the first occurrence of the specified value sent as a parameter when it matches ([CHARINDEX in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/charindex-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
CHARINDEX( expression_to_find, expression_to_search [, start] )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/charindex.html)

```sql
CHARINDEX( <expr1>, <expr2> [ , <start_pos> ] )
```

##### JavaScript

[JavaScript complete documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/indexOf)

```sql
String.indexOf( search_value [, index] )
```

### Examples

#### SQL Server

```sql
SELECT CHARINDEX('t', 'Customer') AS MatchPosition;
```

**Result:**

| INDEX |
| --- |
| 33 |

##### Snowflake SQL

```sql
SELECT
CHARINDEX('t', 'Customer') AS MatchPosition;
```

**Result:**

| INDEX |
| --- |
| 33 |

##### JavaScript

> **Note:**
>
> Indexes in Transact start at 1, instead of JavaScript which start at 0.

```sql
CREATE OR REPLACE FUNCTION get_index
(
  expression_to_find varchar,
  expression_to_search varchar,
  start_index  float
)
  RETURNS float
  LANGUAGE JAVASCRIPT
AS
$$
  return EXPRESSION_TO_SEARCH.indexOf(EXPRESSION_TO_FIND, START_INDEX)+1;
$$;

SELECT GET_INDEX('and', 'Give your heart and soul to me, and life will always be la vie en rose', 20) AS INDEX;
```

**Result:**

| INDEX |
| --- |
| 33 |

## COALESCE

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

Evaluates the arguments in order and returns the current value of the first expression that initially doesn’t evaluate to NULL. For example,SELECT COALESCE(NULL, NULL, ‘third_value’, ‘fourth_value’); returns the third value because the third value is the first value that isn’t null. ([COALESCE in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/coalesce-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
COALESCE ( expression [ ,...n ] )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/coalesce.html)

```sql
COALESCE( <expr1> , <expr2> [ , ... , <exprN> ] )
```

### Examples

#### SQL Server

```sql
SELECT TOP 10 StartDate,
COALESCE(EndDate,'2000-01-01') AS FIRST_NOT_NULL
FROM HumanResources.EmployeeDepartmentHistory
```

**Result:**

| StartDate | FIRST_NOT_NULL |
| --- | --- |
| 2009-01-14 | 2000-01-01 |
| 2008-01-31 | 2000-01-01 |
| 2007-11-11 | 2000-01-01 |
| 2007-12-05 | 2010-05-30 |
| 2010-05-31 | 2000-01-01 |
| 2008-01-06 | 2000-01-01 |
| 2008-01-24 | 2000-01-01 |
| 2009-02-08 | 2000-01-01 |
| 2008-12-29 | 2000-01-01 |
| 2009-01-16 | 2000-01-01 |

##### Snowflake SQL

```sql
SELECT TOP 10
StartDate,
COALESCE(EndDate,'2000-01-01') AS FIRST_NOT_NULL
FROM
HumanResources.EmployeeDepartmentHistory;
```

**Result:**

| StartDate | FIRST_NOT_NULL |
| --- | --- |
| 2009-01-14 | 2000-01-01 |
| 2008-01-31 | 2000-01-01 |
| 2007-11-11 | 2000-01-01 |
| 2007-12-05 | 2010-05-30 |
| 2010-05-31 | 2000-01-01 |
| 2008-01-06 | 2000-01-01 |
| 2008-01-24 | 2000-01-01 |
| 2009-02-08 | 2000-01-01 |
| 2008-12-29 | 2000-01-01 |
| 2009-01-16 | 2000-01-01 |

## CONCAT

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Makes a concatenation of string values with others. ([CONCAT in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/concat-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
CONCAT ( string_value1, string_value2 [, string_valueN ] )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/concat.html)

```sql
CONCAT( <expr1> [ , <exprN> ... ] )

<expr1> || <expr2> [ || <exprN> ... ]
```

##### JavaScript

[JavaScript complete documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/concat)

```sql
 String.concat( expression1, ..., expressionN )
```

### Examples

#### SQL Server

```sql
SELECT CONCAT('Ray',' ','of',' ','Light') AS TITLE;
```

**Output:**

| TITLE |
| --- |
| Ray of Light |

##### Snowflake SQL

```sql
SELECT
CONCAT('Ray',' ','of',' ','Light') AS TITLE;
```

**Output:**

| TITLE |
| --- |
| Ray of Light |

##### JavaScript

```sql
CREATE OR REPLACE FUNCTION concatenate_strs(strings array)
RETURNS string
LANGUAGE JAVASCRIPT
AS
$$
  var result = ""
  STRINGS.forEach(element => result = result.concat(element));
  return result;
$$;
SELECT concatenate_strs(array_construct('Ray',' ','of',' ','Light')) TITLE;
```

**Output:**

```none
   TITLE|
```

————|
Ray of Light|

## LEFT

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the right part of a character string with the specified number of characters. ([RIGHT in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/right-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
LEFT ( character_expression , integer_expression )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/left.html)

```sql
LEFT ( <expr> , <length_expr> )
```

##### JavaScript

Function used to emulate the behavior

```sql
function LEFT(string, index){
    if(index < 0){
        throw new RangeError('Invalid INDEX on LEFT function');
    }
    return string.slice( 0, index);
  }
return LEFT(STR, INDEX);
```

### Examples

#### SQL Server

```sql
SELECT LEFT('John Smith', 5) AS FIRST_NAME;
```

**Output:**

| FIRST_NAME |
| --- |
| John |

##### Snowflake SQL

```sql
SELECT LEFT('John Smith', 5) AS FIRST_NAME;
```

**Output:**

| FIRST_NAME |
| --- |
| John |

##### JavaScript

```sql
CREATE OR REPLACE FUNCTION left_str(str varchar, index float)
RETURNS string
LANGUAGE JAVASCRIPT
AS
$$
    function LEFT(string, index){
      if(index < 0){
          throw new RangeError('Invalid INDEX on LEFT function');
      }
      return string.slice( 0, index);
    }
  return LEFT(STR, INDEX);
$$;
SELECT LEFT_STR('John Smith', 5) AS FIRST_NAME;
```

**Output:**

| FIRST_NAME |
| --- |
| John |

## LEN

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the length of a string ([LEN in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/len-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
LEN( string_expression )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/length.html)

```sql
LENGTH( <expression> )
LEN( <expression> )
```

##### JavaScript

[JavaScript SQL complete documentation](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/length)

```sql
 string.length
```

### Examples

#### SQL Server

```sql
SELECT LEN('Sample text') AS [LEN];
```

**Output:**

| LEN |
| --- |
| 11 |

##### Snowflake SQL

```sql
SELECT LEN('Sample text') AS LEN;
```

**Output:**

| LEN |
| --- |
| 11 |

##### JavaScript

```sql
CREATE OR REPLACE FUNCTION get_len(str varchar)
RETURNS float
LANGUAGE JAVASCRIPT
AS
$$
  return STR.length;
$$;
SELECT GET_LEN('Sample text') LEN;
```

**Output:**

| LEN |
| --- |
| 11 |

## LOWER

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Converts a string to lowercase ([LOWER in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/lower-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
LOWER ( character_expression )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/lower.html)

```sql
LOWER( <expr> )
```

##### JavaScript

[JavaScript SQL complete documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)

```sql
 String.toLowerCase( )
```

### Examples

#### SQL Server

```sql
SELECT LOWER('YOU ARE A PREDICTION OF THE GOOD ONES') AS LOWERCASE;
```

**Output:**

| LOWERCASE |
| --- |
| you are a prediction of the good ones |

##### Snowflake SQL

```sql
SELECT LOWER('YOU ARE A PREDICTION OF THE GOOD ONES') AS LOWERCASE;
```

**Output:**

| LOWERCASE |
| --- |
| you are a prediction of the good ones |

##### JavaScript

```sql
CREATE OR REPLACE FUNCTION to_lower(str varchar)
RETURNS string
LANGUAGE JAVASCRIPT
AS
$$
  return STR.toLowerCase();
$$;

SELECT TO_LOWER('YOU ARE A PREDICTION OF THE GOOD ONES') LOWERCASE;
```

**Output:**

| LOWERCASE |
| --- |
| you are a prediction of the good ones |

## NCHAR

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the UNICODE character of an integer sent as a parameter ([NCHAR in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/nchar-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

```sql
NCHAR( expression )
```

##### Arguments

`expression`: Integer expression.

##### Return Type

String value, it depends on the input received.

### Examples

#### Query

```sql
SELECT NCHAR(170);
```

##### Result

|  |
| --- |
| ª |

> **Note:**
>
> The equivalence for this function in JavaScript is documented in CHAR.

## REPLACE

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Replaces all occurrences of a specified string value with another string value. ([REPLACE in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/replace-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
REPLACE ( string_expression , string_pattern , string_replacement )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/replace.html)

```sql
REPLACE( <subject> , <pattern> [ , <replacement> ] )
```

##### JavaScript

```sql
 String.replace( pattern, new_expression)
```

### Examples

#### SQL Server

```sql
SELECT REPLACE('Real computer software', 'software','science') AS COLUMNNAME;
```

**Output:**

```sql
COLUMNNAME           |
---------------------|
Real computer science|
```

##### Snowflake SQL

```sql
SELECT REPLACE('Real computer software', 'software','science') AS COLUMNNAME;
```

**Output:**

```sql
COLUMNNAME           |
---------------------|
Real computer science|
```

##### JavaScript

```sql
 CREATE OR REPLACE FUNCTION REPLACER (str varchar, pattern varchar, new_expression varchar)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
   return STR.replace( PATTERN, NEW_EXPRESSION );
$$;

SELECT REPLACER('Real computer software', 'software', 'science') AS COLUMNNAME;
```

**Output:**

```sql
COLUMNNAME             |
---------------------|
Real computer science|
```

## REPLICATE

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Replicates a string value a specified number of times ([REPLICATE in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/replicate-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
REPLICATE( string_expression, number_expression )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/repeat.html)

```sql
REPEAT(<input>, <n>)
```

##### JavaScript

[JavaScript Documentation](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/repeat)

```sql
String.repeat( number_expression )
```

### Examples

#### SQL Server

```sql
SELECT REPLICATE('Staying alive',5) AS RESULT
```

**Result:**

```sql
RESULT                                                           |
-----------------------------------------------------------------|
Staying aliveStaying aliveStaying aliveStaying aliveStaying alive|
```

##### Snowflake SQL

```sql
SELECT REPEAT('Staying alive',5) AS RESULT;
```

**Result:**

```sql
RESULT                                                           |
-----------------------------------------------------------------|
Staying aliveStaying aliveStaying aliveStaying aliveStaying alive|
```

##### JavaScript

```sql
 CREATE OR REPLACE FUNCTION REPEAT_STR (str varchar, occurrences float)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$

   return STR.repeat( OCCURRENCES );
$$;

SELECT REPEAT_STR('Staying alive ', 5) AS RESULT;
```

**Result:**

```sql
RESULT                                                           |
-----------------------------------------------------------------|
Staying aliveStaying aliveStaying aliveStaying aliveStaying alive|
```

## RIGHT

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the right part of a character string with the specified number of characters. ([RIGHT in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/right-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
RIGHT ( character_expression , integer_expression )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/right.html)

```sql
RIGHT( <expr> , <length_expr> )
```

##### JavaScript

UDF used to emulate the behavior

```sql
 function RIGHT(string, index){
      if(index< 0){
          throw new RangeError('Invalid INDEX on RIGHT function');
      }
      return string.slice( string.length - index, string.length );
    }
```

### Examples

#### SQL Server

```sql
SELECT RIGHT('John Smith', 5) AS LAST_NAME;
```

**Output:**

```sql
   LAST_NAME|
------------|
       Smith|
```

##### Snowflake SQL

```sql
SELECT RIGHT('John Smith', 5) AS LAST_NAME;
```

**Output:**

```sql
   LAST_NAME|
------------|
       Smith|
```

##### JavaScript

```sql
 CREATE OR REPLACE FUNCTION right_str(str varchar, index float)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
    function RIGHT(string, index){
      if(index< 0){
          throw new RangeError('Invalid INDEX on RIGHT function');
      }
      return string.slice( string.length - index, string.length );
    }
  return RIGHT(STR, INDEX);
$$;

SELECT RIGHT_STR('John Smith', 5) AS LAST_NAME;
```

**Output:**

```sql
   LAST_NAME|
------------|
       Smith|
```

## RTRIM

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a character expression after it removes leading blanks ([RTRIM in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/rtrim-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
RTRIM( string_expression )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/rtrim.html)

```sql
RTRIM(<expr> [, <characters> ])
```

##### JavaScript

Custom function used to emulate the behavior

```sql
 function RTRIM(string){
    return string.replace(/s+$/,"");
}
```

### Examples

#### SQL Server

**Input:**

```sql
SELECT RTRIM('LAST TWO BLANK SPACES  ') AS [RTRIM]
```

**Output:**

```sql
RTRIM                |
---------------------|
LAST TWO BLANK SPACES|
```

##### Snowflake SQL

```sql
SELECT RTRIM('LAST TWO BLANK SPACES  ') AS RTRIM;
```

**Result:**

```sql
RTRIM                |
---------------------|
LAST TWO BLANK SPACES|
```

##### JavaScript

```sql
 CREATE OR REPLACE FUNCTION rtrim(str varchar)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
  function RTRIM(string){
    return string.replace(/s+$/,"");
    }
   return RTRIM( STR );
$$;

SELECT RTRIM('LAST TWO BLANK SPACES  ') AS RTRIM;
```

**Result:**

```sql
RTRIM                |
---------------------|
LAST TWO BLANK SPACES|
```

## SPACE

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a number of occurrences of blank spaces ([SPACE in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/space-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
SPACE ( integer_expression )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/space.html)

```sql
SPACE(<n>)
```

##### JavaScript

Custom function used to emulate the behavior

```sql
 function SPACE( occurrences ){
    return ' '.repeat( occurrences );
}
```

### Examples

#### SQL Server

**Input:**

```sql
SELECT CONCAT('SOME', SPACE(5), 'TEXT') AS RESULT;
```

**Output:**

```sql
RESULT       |
-------------|
SOME     TEXT|
```

##### Snowflake SQL

**Input:**

```sql
SELECT CONCAT('SOME', SPACE(5), 'TEXT') AS RESULT;
```

**Output:**

```sql
RESULT       |
-------------|
SOME     TEXT|
```

##### JavaScript

**Input:**

```sql
 CREATE OR REPLACE FUNCTION SPACE(occurrences float)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
    function SPACE( occurrences ){
    return ' '.repeat( occurrences );
    }
    return SPACE( OCCURRENCES );
$$;

SELECT CONCAT('SOME', SPACE(5), 'TEXT') RESULT;
```

**Output:**

```sql
RESULT       |
-------------|
SOME     TEXT|
```

## SUBSTRING

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a character expression after it removes leading blanks ([RTRIM in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/rtrim-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
SUBSTRING( string_expression, start, length )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/substr.html)

```sql
SUBSTR( <base_expr>, <start_expr> [ , <length_expr> ] )

SUBSTRING( <base_expr>, <start_expr> [ , <length_expr> ] )
```

##### JavaScript

Custom function used to emulate the behavior

```sql
 string.substring( indexA [, indexB])
```

### Examples

#### SQL Server

**Input:**

```sql
SELECT SUBSTRING('abcdef', 2, 3) AS SOMETEXT;
```

**Output:**

```sql
SOMETEXT|
--------|
bcd     |
```

##### Snowflake SQL

```sql
SELECT SUBSTRING('abcdef', 2, 3) AS SOMETEXT;
```

**Result:**

```sql
SOMETEXT|
--------|
bcd     |
```

##### JavaScript

```sql
 CREATE OR REPLACE FUNCTION REPLACER_LENGTH(str varchar, index float, length float)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
    var start = INDEX - 1;
    var end = STR.length - (LENGTH - 1);
    return STR.substring(start, end);
$$;

SELECT REPLACER_LENGTH('abcdef', 2, 3) AS SOMETEXT;
```

**Result:**

```sql
SOMETEXT|
--------|
bcd     |
```

## UPPER

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Converts a string to uppercase ([UPPER in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/upper-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
UPPER( string_expression )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/upper.html)

```sql
UPPER( <expr> )
```

##### JavaScript

[JavaScript SQL complete documentation](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)

```sql
 String.toUpperCase( )
```

### Examples

#### SQL Server

```sql
SELECT UPPER('you are a prediction of the good ones') AS [UPPER]
```

**Output:**

```sql
+-------------------------------------|
|UPPER                                |
+-------------------------------------|
|YOU ARE A PREDICTION OF THE GOOD ONES|
+-------------------------------------|
```

##### Snowflake SQL

```sql
SELECT
UPPER('you are a prediction of the good ones') AS UPPER;
```

**Output:**

```sql
+-------------------------------------|
|UPPER                                |
+-------------------------------------|
|YOU ARE A PREDICTION OF THE GOOD ONES|
+-------------------------------------|
```

##### JavaScript

```sql
 CREATE OR REPLACE FUNCTION to_upper(str varchar)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
  return STR.toUpperCase();
$$;

SELECT TO_UPPER('you are a prediction of the good ones') UPPER;
```

**Output:**

```sql
UPPER                                |
-------------------------------------|
YOU ARE A PREDICTION OF THE GOOD ONES|
```

## ASCII

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the number code of a character on the ASCII table ([ASCII in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/ascii-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
ASCII( expression )
```

#### Arguments

`expression`: `VARCVHAR` or `CHAR` expression.

#### Return Type

`INT`.

### Examples

### Query

```sql
SELECT ASCII('A') AS A , ASCII('a') AS a;
```

#### Result

```sql
          A|          a|
-----------| ----------|
         65|         97|
```

## ASCII in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This function returns the number code of a character on the ASCII table ([JavaScript charCodeAt function Documentation](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt)).

### Sample Source Pattern

#### Syntax

```sql
 string.charCodeAt( [index] )
```

##### Arguments

`index`(Optional): Index of string to get character and return its code number on the ASCII table. If this parameter is not specified, it takes 0 as default. \

##### Return Type

`Int`.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION get_ascii(c char)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
  return C.charCodeAt();
$$;

SELECT GET_ASCII('A') A, GET_ASCII('a') a;
```

##### Result

```sql
          A|          a|
-----------| ----------|
         65|         97|
```

## QUOTENAME

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a string delimited using quotes ([QUOTENAME in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/quotename-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
QUOTENAME( string_expression [, quote_character])
```

#### Arguments

`string_expression`: String to delimit.

`quote_character`: one-character to delimit the string.

#### Return Type

`NVARCHAR(258)`. Null if the quote is different of (‘), ([]), (“), ( () ), ( >< ), ({}) or (`).

### Examples

### Query

```sql
SELECT QUOTENAME('Hello', '`') AS HELLO;
```

#### Result

```sql
    HELLO|
---------|
  `Hello`|
```

## QUOTENAME in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Unfortunately, this function is not available in JavaScript, but it can be implemented using predefined functions.

### Sample Source Pattern

#### Implementation Example

```sql
 function QUOTENAME(string, quote){
    return quote.concat(string, quote);
}
```

##### Arguments

`string`: String expression to delimit.

`quote`: Quote to be used as a delimiter.

##### Return Type

String.

### Examples

#### Query

```sql
CREATE OR REPLACE FUNCTION QUOTENAME(str varchar, quote char)
RETURNS string
LANGUAGE JAVASCRIPT
AS
$$
  function QUOTENAME(string, quote){
    const allowed_quotes = /[\']|[\"]|[(]|[)]|[\[]|[\]]|[\{]|[\}]|[\`]/;

    if(!allowed_quotes.test(quote)) throw new TypeError('Invalid Quote');

    return quote.concat(string, quote);
  }
   return QUOTENAME(STR, QUOTE);
$$;

SELECT QUOTENAME('Hola', '`') HELLO;
```

##### Result

```sql
    HELLO|
---------|
  `Hello`|
```

## CONCAT_WS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Makes a concatenation of string values with others using a separator between them ([CONCAT_WS in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/concat-ws-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
CONCAT_WS( separator, expression1, ... ,expressionN )
```

#### Arguments

`separator`: Separator to join.

`expression1, ... ,expressionN:` Expression to be found into a string.

#### Return Type

String value, depends on the input received.

### Examples

### Query

```sql
SELECT CONCAT_WS(' ', 'Mariah','Carey') AS NAME;
```

#### Result

```sql
        NAME|
------------|
Mariah Carey|
```

## Join in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Concatenates the string arguments to the calling string using a separator ([JavaScript Join function Documentation](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/join)).

### Sample Source Pattern

#### Syntax

```sql
 Array.join( separator )
```

##### Arguments

`separator`: Character to join.

##### Return Type

`String`.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION join_strs(separator varchar, strings array)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
  return STRINGS.join(SEPARATOR);
$$;
SELECT join_strs(' ',array_construct('Mariah','Carey')) NAME;
```

##### Result

```sql
        NAME|
------------|
Mariah Carey|
```

## SOUNDEX

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a four-character code to evaluate the similarity of two strings ([SOUNDEX in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/soundex-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
SOUNDEX( string_expression )
```

#### Arguments

`string_expression`: String expression to reverse.

#### Return Type

The same data type of the string expression sent as a parameter.

### Examples

### Query

```sql
SELECT SOUNDEX('two') AS TWO , SOUNDEX('too') AS TOO;
```

#### Result

```sql
      TWO|      TOO|
---------|---------|
     T000|     T000|
```

## SOUNDEX in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Unfortunately, JavaScript does not provide a method that executes the SOUNDEX algorithm, but it can be implemented manually.

### Sample Source Pattern

#### Implementation Example

```sql
 const dic = {A:0, B:1, C:2, D:3, E:0, F:1, G:2, H:0, I:0, J:2, K:2, L:4, M:5, N:5, O:0, P:1, Q:2, R:6, S:2, T:3, U:0, V:1, W:0, X:2, Y:0, Z:2};

  function getCode(letter){
      return dic[letter.toUpperCase()];
  }

  function SOUNDEX(word){
    var initialCharacter = word[0].toUpperCase();
    var initialCode = getCode(initialCharacter);
    for(let i = 1; i < word.length; ++i) {
        const letterCode = getCode(word[i]);
        if (letterCode && letterCode != initialCode) {
             initialCharacter += letterCode;
             if(initialCharacter.length == 4) break;
        }
        initialCode = letterCode;
    }

      return initialCharacter.concat( '0'.repeat( 4 - initialCharacter.length));

  }
```

##### Arguments

`word`: String expression to get its SOUNDEX equivalence.

##### Return Type

String.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION get_soundex(str varchar)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
  const dic = {A:0, B:1, C:2, D:3, E:0, F:1, G:2, H:0, I:0, J:2, K:2, L:4, M:5, N:5, O:0, P:1, Q:2, R:6, S:2, T:3, U:0, V:1, W:0, X:2, Y:0, Z:2};

  function getCode(letter){
      return dic[letter.toUpperCase()];
  }

  function SOUNDEX(word){
    var initialCharacter = word[0].toUpperCase();
    var initialCode = getCode(initialCharacter);
    for(let i = 1; i < word.length; ++i) {
        const letterCode = getCode(word[i]);
        if (letterCode && letterCode != initialCode) {
             initialCharacter += letterCode;
             if(initialCharacter.length == 4) break;
        }
        initialCode = letterCode;
    }

    return initialCharacter.concat( '0'.repeat( 4 - initialCharacter.length));
  }

  return SOUNDEX( STR );
$$;

SELECT GET_SOUNDEX('two') AS TWO , GET_SOUNDEX('too') AS TOO;
```

##### Result

```sql
      TWO|      TOO|
---------|---------|
     T000|     T000|
```

## REVERSE

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Reverses a string ([REVERSE in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/reverse-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
REVERSE( string_expression )
```

#### Arguments

`string_expression`: String expression to reverse.

#### Return Type

The same data type of the string expression sent as a parameter.

### Examples

### Query

```sql
SELECT REVERSE('rotator') AS PALINDROME;
```

#### Result

```sql
      PALINDROME|
----------------|
         rotator|
```

## reverse in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Unfortunately, this function is not available in JavaScript, but it can be implemented using predefined functions.

### Sample Source Pattern

#### Implementation Example

```sql
 function REVERSE(string){
    return string.split("").reverse().join("");
}
```

##### Arguments

`string`: String expression to reverse.

##### Return Type

String.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION REVERSE(str varchar)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
   return STR.split("").reverse().join("");
$$;

SELECT REVERSE('rotator') PALINDROME;
```

##### Result

```sql
      PALINDROME|
----------------|
         rotator|
```

## STRING_ESCAPE

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Escapes special characters in texts and returns text with escaped characters. ([STRING_ESCAPE in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/string-escape-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
STRING_ESCAPE( text, type )
```

#### Arguments

`text`: Text to escape characters.

`type`: Format type to escape characters. Currently, JSON is the only format supported.

#### Return Type

`VARCHAR`.

### Examples

### Query

```sql
SELECT STRING_ESCAPE('\   /  \\    "     ', 'json') AS [ESCAPE];
```

#### Result

```sql
ESCAPE|
--------------------------|
  \\   \/  \\\\    \"     |
```

## stringify in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Converts an object to a JSON string format ([JavaScript stringify function Documentation](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)).

### Sample Source Pattern

#### Syntax

```sql
 JSON.stringify( value )
```

##### Arguments

`value`: Object expression to convert.

##### Return Type

String.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION string_escape (str varchar)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
   return JSON.stringify( STR );
$$;

SELECT STRING_ESCAPE('\   /  \\    "     ') ESCAPE;
```

##### Result

```sql
                    ESCAPE|
--------------------------|
  \\   \/  \\\\    \"     |
```

## TRIM

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a character expression without blank spaces ([TRIM in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/trim-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
TRIM( string_expression )
```

#### Arguments

`string_expression:` String expressions to convert.

#### Return Type

`VARCHAR` or `NVARCHAR`

### Examples

### SQL Server

```sql
SELECT TRIM('  FIRST AND LAST TWO BLANK SPACES  ') AS [TRIM];
```

**Output:**

```sql
+-------------------------------|
|TRIM                           |
+-------------------------------|
|FIRST AND LAST TWO BLANK SPACES|
+-------------------------------|
```

#### Snowflake SQL

```sql
SELECT TRIM('  FIRST AND LAST TWO BLANK SPACES  ') AS TRIM;
```

**Output:**

```sql
+-------------------------------|
|TRIM                           |
+-------------------------------|
|FIRST AND LAST TWO BLANK SPACES|
+-------------------------------|
```

## trim in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Replaces the occurrences of a pattern using a new one sent as a parameter ([JavaScript Replace function Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)).

### Sample Source Pattern

#### Syntax

```sql
 String.trim( )
```

##### Arguments

This function does not receive any parameters.

##### Return Type

String.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION TRIM_STR(str varchar)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
   return STR.trim( );
$$;

SELECT TRIM_STR('  FIRST AND LAST TWO BLANK SPACES  ')TRIM
```

##### Result

```sql
                           TRIM|
-------------------------------|
FIRST AND LAST TWO BLANK SPACES|
```

## DIFFERENCE

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns an integer measuring the difference between two strings using the SOUNDEX algorithm ([DIFFERENCE in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/difference-transact-sql?view=sql-server-ver15)).
It counts the common characters of the strings resulting by executing the SOUNDEX algorithm.

### Sample Source Pattern

### Syntax

```sql
DIFFERENCE( expression1, expression1 )
```

#### Arguments

`expression1, expression2:` String expressions to be compared.

#### Return Type

`Int`.

### Examples

### Query

```sql
SELECT DIFFERENCE('Like', 'Mike');
```

#### Result

```sql
    Output |
-----------|
         3 |
```

## DIFFERENCE in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Unfortunately, this functionality is not available in JS, but this can be implemented easily.

> **Note:**
>
> This functions requires the SOUNDEX algorithm implementation.

### Sample Source Pattern

#### Implementation Example

```sql
 function DIFFERENCE(strA, strB) {
    var count = 0;
    for (var i = 0; i < strA.length; i++){
       if ( strA[i] == strB[i] ) count++;
    }

    return count;
}
```

##### Arguments

`strA, strB`: String expressions resulting by executing the SOUNDEX algorithm.

##### Return Type

`String`.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION SOUNDEX_DIFFERENCE(str_1 varchar, str_2 varchar)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
    function DIFFERENCE(strA, strB) {
      var count = 0;
      for (var i = 0; i < strA.length; i++){
         if ( strA[i] == strB[i] ) count++;
      }

    return count;
    }

    return DIFFERENCE(STR_1, STR_2);
$$;

SELECT SOUNDEX_DIFFERENCE(GET_SOUNDEX('two'), GET_SOUNDEX('too')) DIFFERENCE;
```

##### Result

```sql
   DIFFERENCE|
-------------|
            4|
```

## FORMAT

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a value formatted with the specified format and optional culture ([FORMAT in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/format-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
FORMAT( value, format [, culture])
```

#### Arguments

`value:` String expressions to give format.

format: Desired format.

culture (Optional): NVarchar argument specifying culture. If it is not specified, takes the languages of the current session.

#### Return Type

NULL if the culture parameter is invalid, otherwise, it follows the next data types:

| Category |  | .NET type |
| --- | --- | --- |
| Numeric | bigint | Int64 |
| Numeric | int | Int32 |
| Numeric | smallint | Int16 |
| Numeric | tinyint | Byte |
| Numeric | decimal | SqlDecimal |
| Numeric | numeric | SqlDecimal |
| Numeric | float | Double |
| Numeric | real | Single |
| Numeric | smallmoney | Decimal |
| Numeric | money | Decimal |
| Date and Time | date | DateTime |
| Date and Time | time | TimeSpan |
| Date and Time | datetime | DateTime |
| Date and Time | smalldatetime | DateTime |
| Date and Time | datetime2 | DateTime |
| Date and Time | datetimeoffset | DateTimeOffset |

### Examples

### Query

```sql
SELECT FORMAT(CAST('2022-01-24' AS DATE), 'd', 'en-gb')  AS 'Great Britain';
```

#### Result

```sql
  GREAT BRITAIN|
---------------|
     24/01/2022|
```

##### Query

```sql
SELECT FORMAT(244900.25, 'C', 'cr-CR')  AS 'CURRENCY';
```

##### Result

| CURRENCY |
| --- |
| ₡244,900.25 |

## FORMAT in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

There are different functions to format date and integer values in JavaScript. Unfortunately, these functionalities are not integrated into one method.

### DateTime values

#### Syntax

```sql
 Intl.DateTimeFormat( format ).format( value )
```

##### Arguments

`locales` (Optional): String expression of the format to apply.

`options` (Optional): Object with different supported properties for formats of numeric expressions ([JavaScript NumberFormat function Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat)).

`value`: Numeric expression to format.

##### Return Type

`String`.

### Numeric values

#### Syntax

```sql
 Intl.NumberFormat( [locales [, options]] ).format( value )
```

##### Arguments

`locales` (Optional): String expression of the format to apply.

`options` (Optional): Object with different supported properties for formats of numeric expressions ([JavaScript NumberFormat function Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat)).

`value`: Numeric expression to format.

##### Return Type

`String`.

### Examples

#### DateTime

##### Query

```sql
 CREATE OR REPLACE FUNCTION format_date(date timestamp, format varchar)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
  return new Intl.DateTimeFormat( FORMAT ).format( DATE );
$$;
SELECT FORMAT_DATE(TO_DATE('2022-01-24'), 'en-gb') GREAT_BRITAIN;
```

##### Result

```sql
  GREAT_BRITAIN|
---------------|
     24/01/2022|
```

#### Numeric

##### Query

```sql
 CREATE OR REPLACE FUNCTION format_numeric(number float, locales varchar, options variant)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
  return new Intl.NumberFormat( LOCALES , OPTIONS ).format( NUMBER );
$$;
SELECT FORMAT_NUMERIC(244900.25, 'de-DE', PARSE_JSON('{ style: "currency", currency: "CRC" }')) CURRENCY;
```

##### Result

```sql
       CURRENCY|
---------------|
 244.900,25 CRC|
```

## PATINDEX

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the starting position of the first occurrence of a pattern in a specified expression ([PATINDEX in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/patindex-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
PATINDEX( pattern, expression )
```

#### Arguments

`pattern`: Pattern to find.

`expression`: Expression to search.

#### Return Type

Integer. Returns 0 if the pattern is not found.

### Examples

### Query

```sql
SELECT PATINDEX( '%on%', 'No, no, non esistono più') AS [PATINDEX]
```

#### Result

```sql
    PATINDEX|
------------|
          10|
```

## search in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Finds the index of a pattern using REGEX ([JavaScript search function Documentation](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/search)).

### Sample Source Pattern

#### Syntax

```sql
 String.search( regex )
```

##### Arguments

`regex`: Regular expression which matches with the desired pattern.

##### Return Type

Integer. If the pattern does not match with any part of the string, returns -1.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION get_index_pattern(pattern varchar, str varchar)
  RETURNS float
  LANGUAGE JAVASCRIPT
AS
$$
  function GET_PATTERN(pattern, string){
    return string.search(new RegExp( pattern ));
    }
   return GET_PATTERN(PATTERN, STR) + 1;
$$;

SELECT GET_INDEX_PATTERN('on+', 'No, no, non esistono più') PATINDEX;
```

##### Result

```sql
    PATINDEX|
------------|
          10|
```

## STR

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns character data converted from numeric data. The character data is right-justified, with a specified length and decimal precision. ([STR in Transact-SQL](https://learn.microsoft.com/en-us/sql/t-sql/functions/str-transact-sql?view=sql-server-ver16)).

### Sample Source Pattern

### Syntax

#### SQL Server

```bnf
STR ( float_expression [ , length [ , decimal ] ] )
```

##### Snowflake SQL

```sql
STR_UDF( numeric_expression, number_format )
```

#### Arguments

`numeric_expression`: Float expression with a decimal point.

`length` (Optional): Length that the returning expression will have, including point notation, decimal, and float parts.

`decimal`(Optional): Is the number of places to the right of the decimal point.

#### Return Type

`VARCHAR`.

### Examples

### SQL Server

**Input:**

```sql
/* 1 */
SELECT STR(123.5);

/* 2 */
SELECT STR(123.5, 2);

/* 3 */
SELECT STR(123.45, 6);

/* 4 */
SELECT STR(123.45, 6, 1);
```

**Output:**

```sql
1) 124
2) **
3) 123
4) 123.5
```

#### Snowflake SQL

**Input:**

```sql
/* 1 */
SELECT
PUBLIC.STR_UDF(123.5, '99999');

/* 2 */
SELECT
PUBLIC.STR_UDF(123.5, '99');

/* 3 */
SELECT
PUBLIC.STR_UDF(123.45, '999999');

/* 4 */
SELECT
PUBLIC.STR_UDF(123.45, '9999.9');
```

**Output:**

```sql
1) 124

2) ##

3) 123
4) 123.5
```

## STR in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Unfortunately, this functionality is not available in JS, but it can be implemented easily using the predefined functions for strings.

### Sample Source Pattern

#### Implementation Example

```sql
 function validLength(number, max_length, float_precision) {
  var float_point = number.match(/[\.][0-9]+/);
  /*if the number does not have point float, checks if the float precision
   * and current number are greater than max_length
   */
   if(!float_point) return number.length + float_precision + 1 < max_length;
    //removes the '.' and checks if there is overflow with the float_precision
    return number.length - float_point[0].trim('.').length + float_precision  < max_length;
}
 function STR(number, max_length, float_precision) {
  var number_str = number.toString();
   //if the expression exceeds the max_length, returns '**'
   if(number_str.length > max_length || float_precision > max_length) return '**';
   if(validLength(number_str, max_length, float_precision)) {
      return number.toFixed(float_precision);
    }
    return number.toFixed(max_length - float_precision);
}
```

##### Arguments

`number`: Float expression with a decimal point.

`max_length`: Length that the returning expression will have, including point notation, decimal, and float parts.

`float_precision`: Is the number of places to the right of the decimal point.

##### Return Type

String.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION STR(number float, max_length float, float_precision float)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
    function validLength(number, max_length, float_precision) {
        var float_point = number.match(/[\.][0-9]+/);
        if(!float_point) return number.length + float_precision + 1 < max_length;
        return number.length - float_point[0].trim('.').length + float_precision  < max_length;
    }
    function STR(number, max_length, float_precision) {
      var number_str = number.toString();
      if(number_str.length > max_length || float_precision > max_length) return '**';
      if(validLength(number_str, max_length, float_precision)) {
        return number.toFixed(float_precision);
      }
      return number.toFixed(max_length - float_precision);
    }
    return STR( NUMBER, MAX_LENGTH, FLOAT_PRECISION );
$$;

SELECT STR(12345.674, 12, 6);
```

##### Result

```sql
           STR|
--------------|
  12345.674000|
```

## LTRIM

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a character expression after it removes leading blanks ([LTRIM in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/ltrim-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
LTRIM( string_expression )
```

#### Arguments

`string_expression:` String expressions to convert.

#### Return Type

`VARCHAR` or `NVARCHAR`

### Examples

### Query

```sql
SELECT LTRIM('  FIRST TWO BLANK SPACES') AS [LTRIM]
```

#### Result

```sql
                 LTRIM|
----------------------|
FIRST TWO BLANK SPACES|
```

## LTRIM in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Unfortunately, this function is not available in JavaScript, but it can be implemented using regular expressions.

### Sample Source Pattern

#### Implementation Example

```sql
 function LTRIM(string){
    return string.replace(/^s+/,"");
}
```

##### Arguments

`string`: String expression to remove blank spaces.

##### Return Type

String.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION ltrim(str varchar)
  RETURNS string
  LANGUAGE JAVASCRIPT
AS
$$
  function LTRIM(string){
    return string.replace(/^s+/,"");
    }
   return LTRIM(S TR );
$$;

SELECT LTRIM('  FIRST TWO BLANK SPACES') AS LTRIM;
```

##### Result

```sql
                 LTRIM|
----------------------|
FIRST TWO BLANK SPACES|
```

## Ranking functions

This section describes the functional equivalents of ranking functions in Transact-SQL to Snowflake SQL and JavaScript code, oriented to their usage in stored procedures in Snowflake.

## DENSE_RANK

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

This function returns the rank of each row within a result set partition, with no gaps in the ranking values. The rank of a specific row is one plus the number of distinct rank values that come before that specific row. ([DENSE_RANK in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/dense-rank-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
 DENSE_RANK ( ) OVER ( [ <partition_by_clause> ] < order_by_clause > )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/dense_rank.html)

```sql
 DENSE_RANK( )
-- ** SSC-EWI-0001 - UNRECOGNIZED TOKEN ON LINE '1' COLUMN '15' OF THE SOURCE CODE STARTING AT 'OVER'. EXPECTED 'BATCH' GRAMMAR. CODE '80'. **
--              OVER ( [ <partition_by_clause> ] < order_by_clause > )
```

### Examples

#### SQL Server

```sql
SELECT TOP 10 BUSINESSENTITYID, NATIONALIDNUMBER, RANK() OVER (ORDER BY NATIONALIDNUMBER) AS RANK FROM HUMANRESOURCES.EMPLOYEE AS TOTAL
```

**Result:**

```sql
BUSINESSENTITYID|NATIONALIDNUMBER|DENSE_RANK|
----------------|----------------|----------|
              57|10708100        |         1|
              54|109272464       |         2|
             273|112432117       |         3|
               4|112457891       |         4|
             139|113393530       |         5|
             109|113695504       |         6|
             249|121491555       |         7|
             132|1300049         |         8|
             214|131471224       |         9|
              51|132674823       |        10|
```

##### Snowflake SQL

```sql
SELECT TOP 10
BUSINESSENTITYID,
NATIONALIDNUMBER,
RANK() OVER (ORDER BY NATIONALIDNUMBER) AS RANK
FROM
HUMANRESOURCES.EMPLOYEE AS TOTAL;
```

**Result:**

```sql
BUSINESSENTITYID|NATIONALIDNUMBER|DENSE_RANK|
----------------|----------------|----------|
              57|10708100        |         1|
              54|109272464       |         2|
             273|112432117       |         3|
               4|112457891       |         4|
             139|113393530       |         5|
             109|113695504       |         6|
             249|121491555       |         7|
             132|1300049         |         8|
             214|131471224       |         9|
              51|132674823       |        10|
```

#### Related EWIs

* [SSC-EWI-0001](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Unrecognized token on the line of the source code.

## RANK

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the rank of each row within the partition of a result set. The rank of a row is one plus the number of ranks that come before the row in question. ([RANK in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/rank-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
 RANK ( ) OVER ( [ partition_by_clause ] order_by_clause )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/rank.html)

```sql
 RANK( )
-- ** SSC-EWI-0001 - UNRECOGNIZED TOKEN ON LINE '1' COLUMN '9' OF THE SOURCE CODE STARTING AT 'OVER'. EXPECTED 'BATCH' GRAMMAR. CODE '80'. **
--        OVER ( [ partition_by_clause ] order_by_clause )
```

### Examples

#### SQL Server

```sql
SELECT TOP 10 BUSINESSENTITYID, NATIONALIDNUMBER, RANK() OVER (ORDER BY NATIONALIDNUMBER) AS RANK FROM HUMANRESOURCES.EMPLOYEE AS TOTAL
```

**Result:**

```sql
BUSINESSENTITYID|NATIONALIDNUMBER|RANK|
----------------|----------------|----|
              57|10708100        |   1|
              54|109272464       |   2|
             273|112432117       |   3|
               4|112457891       |   4|
             139|113393530       |   5|
             109|113695504       |   6|
             249|121491555       |   7|
             132|1300049         |   8|
             214|131471224       |   9|
              51|132674823       |  10|
```

##### Snowflake SQL

```sql
SELECT TOP 10
BUSINESSENTITYID,
NATIONALIDNUMBER,
RANK() OVER (ORDER BY NATIONALIDNUMBER) AS RANK
FROM
HUMANRESOURCES.EMPLOYEE AS TOTAL;
```

**Result:**

```sql
BUSINESSENTITYID|NATIONALIDNUMBER|RANK|
----------------|----------------|----|
              57|10708100        |   1|
              54|109272464       |   2|
             273|112432117       |   3|
               4|112457891       |   4|
             139|113393530       |   5|
             109|113695504       |   6|
             249|121491555       |   7|
             132|1300049         |   8|
             214|131471224       |   9|
              51|132674823       |  10|
```

#### Related EWIs

* [SSC-EWI-0001](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Unrecognized token on the line of the source code.

## ROW_NUMBER

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

Numbers the output of a result set. More specifically, returns the sequential number of a row within a partition of a result set, starting at 1 for the first row in each partition. ([ROW_NUMBER in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/row-number-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
 ROW_NUMBER ( )
    OVER ( [ PARTITION BY value_expression , ... [ n ] ] order_by_clause )
```

##### Snowflake SQL

[Snowflake SQL complete documentation](https://docs.snowflake.com/en/sql-reference/functions/row_number.html)

```sql
 ROW_NUMBER( )
-- ** SSC-EWI-0001 - UNRECOGNIZED TOKEN ON LINE '2' COLUMN '5' OF THE SOURCE CODE STARTING AT 'OVER'. EXPECTED 'BATCH' GRAMMAR. CODE '80'. **
--    OVER ( [ PARTITION BY value_expression , ... [ n ] ] order_by_clause )
```

### Examples

#### SQL Server

```sql
SELECT
ROW_NUMBER() OVER(ORDER BY NAME  ASC) AS RowNumber,
NAME
FROM HUMANRESOURCES.DEPARTMENT
```

**Output:**

```sql
RowNumber|NAME                      |
---------|--------------------------|
        1|Document Control          |
        2|Engineering               |
        3|Executive                 |
        4|Facilities and Maintenance|
        5|Finance                   |
        6|Human Resources           |
        7|Information Services      |
        8|Marketing                 |
        9|Production                |
       10|Production Control        |
       11|Purchasing                |
       12|Quality Assurance         |
       13|Research and Development  |
       14|Sales                     |
       15|Shipping and Receiving    |
       16|Tool Design               |
```

##### Snowflake SQL

```sql
SELECT
ROW_NUMBER() OVER(ORDER BY NAME ASC) AS RowNumber,
NAME
FROM
HUMANRESOURCES.DEPARTMENT;
```

**Output:**

```sql
RowNumber|NAME                      |
---------|--------------------------|
        1|Document Control          |
        2|Engineering               |
        3|Executive                 |
        4|Facilities and Maintenance|
        5|Finance                   |
        6|Human Resources           |
        7|Information Services      |
        8|Marketing                 |
        9|Production                |
       10|Production Control        |
       11|Purchasing                |
       12|Quality Assurance         |
       13|Research and Development  |
       14|Sales                     |
       15|Shipping and Receiving    |
       16|Tool Design               |
```

#### Related EWIs

* [SSC-EWI-0001](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Unrecognized token on the line of the source code.

## Logical functions

This section describes the functional equivalents of logical functions in Transact-SQL to Snowflake SQL and JavaScript code, oriented to their usage in stored procedures in Snowflake.

## IIF

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns one of two values, depending on whether the Boolean expression evaluates to true or false. ([IIF in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/logical-functions-iif-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
IIF( boolean_expression, true_value, false_value )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/iff.html)

```sql
IFF( <condition> , <expr1> , <expr2> )
```

### Examples

#### SQL Server

```sql
SELECT IIF( 2 > 3, 'TRUE', 'FALSE' ) AS RESULT
```

**Result:**

```sql
RESULT|
------|
 FALSE|
```

##### Snowflake SQL

```sql
SELECT
IFF( 2 > 3, 'TRUE', 'FALSE' ) AS RESULT;
```

**Result:**

```sql
RESULT|
------|
 FALSE|
```

## XML Functions

This section describes the translation of XML functions in Transact-SQL to Snowflake SQL.

## Query

Applies to

* SQL Server

> **Warning:**
>
> This transformation will be delivered in the future

### Description

Specifies an XQuery against an instance of the **xml** data type. The result is of **xml** type. The method returns an instance of untyped XML. ([`Query() in Transact-SQL`](https://learn.microsoft.com/en-us/sql/t-sql/xml/query-method-xml-data-type?view=sql-server-ver16))

### Sample Source Patterns

The following example details the transformation for .query( )

#### SQL Server

##### Input

```sql
 CREATE TABLE xml_demo(object_col XML);

INSERT INTO xml_demo (object_col)
   SELECT
        '<Root>
<ProductDescription ProductID="1" ProductName="Road Bike">
<Features>
  <Warranty>1 year parts and labor</Warranty>
  <Maintenance>3 year parts and labor extended maintenance is available</Maintenance>
</Features>
</ProductDescription>
</Root>';

INSERT INTO xml_demo (object_col)
   SELECT
        '<Root>
<ProductDescription ProductID="2" ProductName="Skate">
<Features>
  <Warranty>1 year parts and labor</Warranty>
  <Maintenance>3 year parts and labor extended maintenance is available</Maintenance>
</Features>
</ProductDescription>
</Root>';

SELECT
    xml_demo.object_col.query('/Root/ProductDescription/Features/Warranty') as Warranty,
    xml_demo.object_col.query('/Root/ProductDescription/Features/Maintenance') as Maintenance
from xml_demo;
```

##### Output

```sql
 Warranty                                     | Maintenance                                                                          |
----------------------------------------------|--------------------------------------------------------------------------------------|
<Warranty>1 year parts and labor</Warranty>   | <Maintenance>3 year parts and labor extended maintenance is available</Maintenance>  |
<Warranty>1 year parts and labor</Warranty>   | <Maintenance>3 year parts and labor extended maintenance is available</Maintenance>  |
```

##### Snowflake SQL

##### Input

```sql
 CREATE OR REPLACE TABLE xml_demo (
    object_col VARIANT !!!RESOLVE EWI!!! /*** SSC-EWI-0036 - XML DATA TYPE CONVERTED TO VARIANT ***/!!!
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "07/11/2025",  "domain": "no-domain-provided" }}'
;

INSERT INTO xml_demo (object_col)
SELECT
        '<Root>
<ProductDescription ProductID="1" ProductName="Road Bike">
<Features>
  <Warranty>1 year parts and labor</Warranty>
  <Maintenance>3 year parts and labor extended maintenance is available</Maintenance>
</Features>
</ProductDescription>
</Root>';

INSERT INTO xml_demo (object_col)
SELECT
        '<Root>
<ProductDescription ProductID="2" ProductName="Skate">
<Features>
  <Warranty>1 year parts and labor</Warranty>
  <Maintenance>3 year parts and labor extended maintenance is available</Maintenance>
</Features>
</ProductDescription>
</Root>';

SELECT
    XMLGET(XMLGET(XMLGET(object_col, 'ProductDescription'), 'Features'), 'Warranty') as Warranty,
    XMLGET(XMLGET(XMLGET(object_col, 'ProductDescription'), 'Features'), 'Maintenance') as Maintenance
from
    xml_demo;
```

##### Output

```sql
 Warranty                                     | Maintenance                                                                          |
----------------------------------------------|--------------------------------------------------------------------------------------|
<Warranty>1 year parts and labor</Warranty>   | <Maintenance>3 year parts and labor extended maintenance is available</Maintenance>  |
<Warranty>1 year parts and labor</Warranty>   | <Maintenance>3 year parts and labor extended maintenance is available</Maintenance>  |
```

### Known Issues

No issues were found.

### Related EWIs

1. [SSC-EWI-0036](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Data type converted to another data type.

## Value

Applies to

* SQL Server

> **Warning:**
>
> This transformation will be delivered in the future

### Description

Performs an XQuery against the XML and returns a value of SQL type. This method returns a scalar value. ([`value() in Transact-SQL`](https://learn.microsoft.com/en-us/sql/t-sql/xml/value-method-xml-data-type?view=sql-server-ver16)).

### Sample Source Patterns

The following example details the transformation for .value( )

#### SQL Server

##### Input

```sql
 CREATE TABLE xml_demo(object_col XML);

INSERT INTO xml_demo (object_col)
   SELECT
        '<Root>
<ProductDescription ProductID="1" ProductName="Road Bike">
<Features>
  <Warranty>1 year parts and labor</Warranty>
  <Maintenance>3 year parts and labor extended maintenance is available</Maintenance>
</Features>
</ProductDescription>
</Root>';

INSERT INTO xml_demo (object_col)
   SELECT
        '<Root>
<ProductDescription ProductID="2" ProductName="Skate">
<Features>
  <Warranty>1 year parts and labor</Warranty>
  <Maintenance>3 year parts and labor extended maintenance is available</Maintenance>
</Features>
</ProductDescription>
</Root>';

SELECT
    xml_demo.object_col.value('(/Root/ProductDescription/@ProductID)[1]', 'int' ) as ID,
    xml_demo.object_col.value('(/Root/ProductDescription/@ProductName)[1]', 'varchar(max)' ) as ProductName,
    xml_demo.object_col.value('(/Root/ProductDescription/Features/Warranty)[1]', 'varchar(max)' ) as Warranty
from xml_demo;
```

##### Output

```sql
 ID | ProductName | Warranty               |
----|-------------|------------------------|
1   | Road Bike   | 1 year parts and labor |
2   | Skate       | 1 year parts and labor |
```

##### Snowflake SQL

##### Input

```sql
 CREATE OR REPLACE TABLE xml_demo (
    object_col VARIANT !!!RESOLVE EWI!!! /*** SSC-EWI-0036 - XML DATA TYPE CONVERTED TO VARIANT ***/!!!
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "transact",  "convertedOn": "07/11/2025",  "domain": "no-domain-provided" }}'
;

INSERT INTO xml_demo (object_col)
SELECT
        '<Root>
<ProductDescription ProductID="1" ProductName="Road Bike">
<Features>
  <Warranty>1 year parts and labor</Warranty>
  <Maintenance>3 year parts and labor extended maintenance is available</Maintenance>
</Features>
</ProductDescription>
</Root>';

INSERT INTO xml_demo (object_col)
SELECT
        '<Root>
<ProductDescription ProductID="2" ProductName="Skate">
<Features>
  <Warranty>1 year parts and labor</Warranty>
  <Maintenance>3 year parts and labor extended maintenance is available</Maintenance>
</Features>
</ProductDescription>
</Root>';

SELECT
    GET(XMLGET(object_col, 'ProductDescription'), '@ProductID') :: INT as ID,
    GET(XMLGET(object_col, 'ProductDescription'), '@ProductName') :: VARCHAR as ProductName,
    GET(XMLGET(XMLGET(XMLGET(object_col, 'ProductDescription'), 'Features'), 'Warranty', 0), '$') :: VARCHAR as Warranty
from
    xml_demo;
```

##### Output

```sql
 ID | PRODUCTNAME | WARRANRTY              |
----|-------------|------------------------|
1   | Road Bike   | 1 year parts and labor |
2   | Skate       | 1 year parts and labor |
```

### Known Issues

No issues were found.

### Related EWIs

1. [SSC-EWI-0036](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Data type converted to another data type.

## Aggregate functions

This section describes the functional equivalents of aggregate functions in Transact-SQL to Snowflake SQL and JavaScript code, oriented to the creation of UDFs in Snowflake.

## COUNT

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

This function returns the number of items found in a group. COUNT operates like the COUNT_BIG function. These functions differ only in the data types of their return values. COUNT always returns an int data type value. COUNT_BIG always returns a bigint data type value. ([COUNT in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/count-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
COUNT ( { [ [ ALL | DISTINCT ] expression ] | * } )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/count.html)

```sql
COUNT( [ DISTINCT ] <expr1> [ , <expr2> ... ] )
```

### Examples

#### SQL Server

```sql
SELECT COUNT(NATIONALIDNUMBER) FROM HUMANRESOURCES.EMPLOYEE AS TOTAL;
```

**Result:**

| TOTAL |
| --- |
| 290 |

##### Snowflake SQL

```sql
SELECT
COUNT(NATIONALIDNUMBER) FROM
HUMANRESOURCES.EMPLOYEE AS TOTAL;
```

**Result:**

| TOTAL |
| --- |
| 290 |

## COUNT_BIG

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

This function returns the number of items found in a group. COUNT_BIG operates like the COUNT function. These functions differ only in the data types of their return values. COUNT_BIG always returns a bigint data type value. COUNT always returns an int data type value. ([COUNT_BIG in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/count-big-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
COUNT_BIG ( { [ [ ALL | DISTINCT ] expression ] | * } )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/count.html)

```sql
COUNT( [ DISTINCT ] <expr1> [ , <expr2> ... ] )
```

### Examples

#### SQL Server

```sql
SELECT COUNT_BIG(NATIONALIDNUMBER) FROM HUMANRESOURCES.EMPLOYEE AS TOTAL;
```

**Result:**

| TOTAL |
| --- |
| 290 |

##### Snowflake SQL

```sql
SELECT
COUNT(NATIONALIDNUMBER) FROM
HUMANRESOURCES.EMPLOYEE AS TOTAL;
```

**Result:**

| TOTAL |
| --- |
| 290 |

## SUM

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

Returns the sum of all the values, or only the DISTINCT values, in the expression. SUM can be used with numeric columns only. Null values are ignored. ([SUM in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/sum-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
SUM ( [ ALL | DISTINCT ] expression )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/sum.html)

```sql
SUM( [ DISTINCT ] <expr1> )
```

### Examples

#### SQL Server

```sql
SELECT SUM(VACATIONHOURS) FROM HUMANRESOURCES.EMPLOYEE AS TOTALVACATIONHOURS;
```

**Result:**

| TOTALVACATIONHOURS |
| --- |
| 14678 |

##### Snowflake SQL

```sql
SELECT
SUM(VACATIONHOURS) FROM
HUMANRESOURCES.EMPLOYEE AS TOTALVACATIONHOURS;
```

**Result:**

| TOTALVACATIONHOURS |
| --- |
| 14678 |

## SnowConvert AI custom UDFs

### Description

Some Transact-SQL functions or behaviors may not be available or may behave differently in Snowflake. To minimize these differences, some functions are replaced with SnowConvert AI Custom UDFs.

These UDFs are automatically created during migration, in the `UDF Helper` folder, inside the `Output` folder. There is one file per custom UDF.

## OPENXML UDF

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

This custom UDF is added to process a rowset view over an XML document. This would be used for declarations in because it works as a rowset provider.

[Optional parameters](https://learn.microsoft.com/en-us/sql/t-sql/functions/openxml-transact-sql?view=sql-server-ver16#remarks) and different node types are not supported in this version of the UDF. The element node is processed by default.

### Custom UDF overloads

**Parameters**

1. **XML**: A `VARCHAR` that represents the readable content of the XML.
2. **PATH**: A varchar that contains the pattern of the nodes to be processed as rows.

#### UDF

```sql
CREATE OR REPLACE FUNCTION OPENXML_UDF(XML VARCHAR, PATH VARCHAR)
RETURNS TABLE(VALUE VARIANT)
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"udf"}}'
AS
$$
SELECT VALUE from TABLE(FLATTEN(input=>XML_JSON_SIMPLE(PARSE_XML(XML)), path=>PATH))
$$;

CREATE OR REPLACE FUNCTION XML_JSON_SIMPLE(XML VARIANT)
RETURNS OBJECT
LANGUAGE JAVASCRIPT
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"udf"}}'
AS
$$
function toNormalJSON(xmlJSON) {
    var finalres = {};
    var name=xmlJSON['@'];
    var res = {};
    finalres[name] = res;
    for(var key in xmlJSON)
    {
        if (key == "@")
        {
            res["$name"] = xmlJSON["@"];
        }
        else if (key == "$") {
            continue;
        }
        else if (key.startsWith("@"))
        {
            // This is an attribute
            res[key]=xmlJSON[key];
        }
        else
        {
            var elements = xmlJSON['$']
            var value = xmlJSON[key];
            res[key] = [];
            if (Array.isArray(value))
            {
                for(var elementKey in value)
                {
                    var currentElement = elements[elementKey];
                    var fixedElement = toNormalJSON(currentElement);
                    res[key].push(fixedElement);
                }
            }
            else if (value === 0)
            {
                var fixedElement = toNormalJSON(elements);
                res[key].push(fixedElement);
            }
        }
    }
    return finalres;
}
return toNormalJSON(XML);
$$;
```

##### Transact-SQL

##### Query

```sql
DECLARE @idoc INT, @doc VARCHAR(1000);
SET @doc ='
<ROOT>
<Customer CustomerID="VINET" ContactName="Paul Henriot">
   <Order CustomerID="VINET" EmployeeID="5" OrderDate="1996-07-04T00:00:00">
      <OrderDetail OrderID="10248" ProductID="11" Quantity="12"/>
      <OrderDetail OrderID="10248" ProductID="42" Quantity="10"/>
   </Order>
</Customer>
<Customer CustomerID="LILAS" ContactName="Carlos Gonzlez">
   <Order CustomerID="LILAS" EmployeeID="3" OrderDate="1996-08-16T00:00:00">
      <OrderDetail OrderID="10283" ProductID="72" Quantity="3"/>
   </Order>
</Customer>
</ROOT>';

EXEC sp_xml_preparedocument @idoc OUTPUT, @doc;

SELECT *  FROM OPENXML (@idoc, '/ROOT/Customer',1)
WITH (CustomerID  VARCHAR(10), ContactName VARCHAR(20));
```

##### Result

```sql
CustomerID  | ContactName
----------------------------|
VINET     | Paul Henriot
LILAS     | Carlos Gonzlez
```

##### Snowflake

> **Note:**
>
> The following example is isolated into a stored procedure because environment variables only support 256 bytes of storage, and the XML demo code uses more than that limit.

##### Query

```sql
DECLARE
IDOC INT;
DOC VARCHAR(1000);
BlockResultSet RESULTSET;
BEGIN
DOC := '
<ROOT>
<Customer CustomerID="VINET" ContactName="Paul Henriot">
   <Order CustomerID="VINET" EmployeeID="5" OrderDate="1996-07-04T00:00:00">
      <OrderDetail OrderID="10248" ProductID="11" Quantity="12"/>
      <OrderDetail OrderID="10248" ProductID="42" Quantity="10"/>
   </Order>
</Customer>
<Customer CustomerID="LILAS" ContactName="Carlos Gonzlez">
   <Order CustomerID="LILAS" EmployeeID="3" OrderDate="1996-08-16T00:00:00">
      <OrderDetail OrderID="10283" ProductID="72" Quantity="3"/>
   </Order>
</Customer>
</ROOT>';
!!!RESOLVE EWI!!! /*** SSC-EWI-TS0075 - TRANSLATION FOR BUILT-IN PROCEDURE 'sp_xml_preparedocument' IS NOT CURRENTLY SUPPORTED. ***/!!!

EXEC sp_xml_preparedocument :IDOC OUTPUT, :DOC;
BlockResultSet := (

SELECT
Left(value:Customer['@CustomerID'], '10') AS 'CustomerID',
Left(value:Customer['@ContactName'], '20') AS 'ContactName'
FROM
OPENXML_UDF(:IDOC, ':ROOT:Customer'));
RETURN TABLE(BlockResultSet);
END;
```

##### Result

| CustomerID | ContactName |
| --- | --- |
| VINET | Paul Henriot |
| LILAS | Carlos Gonzlez |

##### Query

```sql
SET code = '<ROOT>
<Customer CustomerID="VINET" ContactName="Paul Henriot">
   <Order CustomerID="VINET" EmployeeID="5" OrderDate="1996-07-04T00:00:00">
      <OrderDetail OrderID="10248" ProductID="11" Quantity="12"/>
   </Order>
</Customer>
</ROOT>';
SELECT
Left(value:Customer['@CustomerID'],10) as "CustomerID",
Left(value:Customer['@ContactName'],20) as "ContactName"
FROM TABLE(OPENXML_UDF($code,'ROOT:Customer'));
```

##### Result

| CustomerID | ContactName |
| --- | --- |
| VINET | Paul Henriot |

### Known Issues

No issues were found.

### Related EWIs

1. [SSC-EWI-TS0075](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/sqlServerEWI.md): Built In Procedure Not Supported.

## STR UDF

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This custom UDF converts numeric data to character data.

### Custom UDF overloads

#### Parameters

1. **FLOAT_EXPR**: A numeric expression to be converted to varchar.
2. **FORMAT**: A varchar expression with the length and number of decimals of the resulting varchar. This format is automatically generated in SnowConvert.

##### UDF

```sql
 CREATE OR REPLACE FUNCTION PUBLIC.STR_UDF(FLOAT_EXPR FLOAT, FORMAT VARCHAR)
RETURNS VARCHAR
LANGUAGE SQL
IMMUTABLE
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"udf"}}'
AS
$$
    TRIM(TRIM(SELECT TO_CHAR(FLOAT_EXPR, FORMAT)), '.')
$$;

CREATE OR REPLACE FUNCTION PUBLIC.STR_UDF(FLOAT_EXPR FLOAT)
RETURNS VARCHAR
LANGUAGE SQL
IMMUTABLE
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"udf"}}'
AS
$$
    STR_UDF(FLOAT_EXPR, '999999999999999999')
$$;
```

##### Transact-SQL

##### Query

```sql
SELECT
    STR(123.5) as A,
    STR(123.5, 2) as B,
    STR(123.45, 6) as C,
    STR(123.45, 6, 1) as D;
```

##### Result

| A | B | C | D |
| --- | --- | --- | --- |
| 124 | \*\* | 123 | 123.5 |

##### Snowflake

##### Query

```sql
SELECT
    PUBLIC.STR_UDF(123.5, '99999') as A,
    PUBLIC.STR_UDF(123.5, '99') as B,
    PUBLIC.STR_UDF(123.45, '999999') as C,
    PUBLIC.STR_UDF(123.45, '9999.9') as D;
```

## SWITCHOFFSET_UDF

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This custom UDF is added to return a datetimeoffset value that is changed from the stored time zone offset to a specified new time zone offset.

### Custom UDF overloads

**Parameters**

1. **source_timestamp**: A TIMESTAMP_TZ that can be resolved to a datetimeoffset(n) value.
2. **target_tz**: A varchar that represents the time zone offset

#### UDF

```sql
CREATE OR REPLACE FUNCTION PUBLIC.SWITCHOFFSET_UDF(source_timestamp TIMESTAMP_TZ, target_tz varchar)
RETURNS TIMESTAMP_TZ
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"udf"}}'
AS
$$
WITH tz_values AS (
SELECT
    RIGHT(source_timestamp::varchar, 5) as source_tz,

    REPLACE(source_tz::varchar, ':', '') as source_tz_clean,
    REPLACE(target_tz::varchar, ':', '') as target_tz_clean,

    target_tz_clean::integer - source_tz_clean::integer as offset,

    RIGHT(offset::varchar, 2) as tz_min,
    PUBLIC.OFFSET_FORMATTER(RTRIM(offset::varchar, tz_min)) as tz_hrs,

    TIMEADD( hours, tz_hrs::integer, source_timestamp ) as adj_hours,
    TIMEADD( minutes, (LEFT(tz_hrs, 1) || tz_min)::integer, adj_hours::timestamp_tz ) as new_timestamp

FROM DUAL)
SELECT
    (LEFT(new_timestamp, 24) || ' ' || target_tz)::timestamp_tz
FROM tz_values
$$;

-- ==========================================================================
-- Description: The function OFFSET_FORMATTER(offset_hrs varchar) serves as
-- an auxiliary function to format the offset hours and its prefix operator.
-- ==========================================================================
CREATE OR REPLACE FUNCTION PUBLIC.OFFSET_FORMATTER(offset_hrs varchar)
RETURNS varchar
LANGUAGE SQL
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"udf"}}'
AS
$$
CASE
   WHEN LEN(offset_hrs) = 0 THEN '+' || '0' || '0'
   WHEN LEN(offset_hrs) = 1 THEN '+' || '0' || offset_hrs
   WHEN LEN(offset_hrs) = 2 THEN
        CASE
            WHEN LEFT(offset_hrs, 1) = '-' THEN '-' || '0' || RIGHT(offset_hrs, 1)
            ELSE '+' || offset_hrs
        END
    ELSE offset_hrs
END
$$;
```

##### Transact-SQL

##### Query

```sql
SELECT
  '1998-09-20 7:45:50.71345 +02:00' as fr_time,
  SWITCHOFFSET('1998-09-20 7:45:50.71345 +02:00', '-06:00') as cr_time;
```

##### Result

```sql
SELECT
  '1998-09-20 7:45:50.71345 +02:00' as fr_time,
  SWITCHOFFSET('1998-09-20 7:45:50.71345 +02:00', '-06:00') as cr_time;
```

##### Snowflake

##### Query

```sql
SELECT
  '1998-09-20 7:45:50.71345 +02:00' as fr_time,
  PUBLIC.SWITCHOFFSET_UDF('1998-09-20 7:45:50.71345 +02:00', '-06:00') as cr_time;
```

##### Result

| fr_time | cr_time |
| --- | --- |
| 1998-09-20 7:45:50.71345 +02:00 | 1998-09-19 23:45:50.7134500 -06:00 |

## Metadata functions

This section describes the functional equivalents of metadata functions in Transact-SQL to Snowflake SQL and JavaScript code, oriented to their usage in stored procedures in Snowflake.

## DB_NAME

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This function returns the name of a specified database.([DB_NAME in Transact-SQL](https://learn.microsoft.com/en-us/sql/t-sql/functions/db-name-transact-sql?view=sql-server-ver16)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
 DB_NAME ( [ database_id ] )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/current_database.html)

```sql
 CURRENT_DATABASE() /*** SSC-FDM-TS0010 - CURRENT_DATABASE function has different behavior in certain cases ***/
```

### Examples

#### SQL Server

```sql
SELECT DB_NAME();
```

**Result:**

| RESULT |
| --- |
| ADVENTUREWORKS2019 |

##### Snowflake SQL

```sql
SELECT
CURRENT_DATABASE() /*** SSC-FDM-TS0010 - CURRENT_DATABASE function has different behavior in certain cases ***/;
```

**Result:**

| RESULT |
| --- |
| ADVENTUREWORKS2019 |

### Known issues

**1. CURRENT_DATABASE function has different behavior in certain cases**

DB_NAME function can be invoked with the **database_id** parameter, which returns the name of the specified database. Without parameters, the function returns the current database name. However, Snowflake does not support this parameter and the CURRENT_DATABASE function will always return the current database name.

### Related EWIs

1. [SSC-FDM-TS0010](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/sqlServerFDM.md): CURRENT_DATABASE function has different behavior in certain cases.

## OBJECT_ID

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This function returns the database object identification number of a schema-scoped object.[(OBJECT_ID in Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/object-id-transact-sql?view=sql-server-ver16).

#### SQL Server syntax

```sql
 OBJECT_ID ( '[ database_name . [ schema_name ] . | schema_name . ]
  object_name' [ ,'object_type' ] )
```

### Sample Source Patterns

#### 1. Default transformation

##### SQL Server

```sql
 IF OBJECT_ID_UDF('DATABASE2.DBO.TABLE1') is not null) THEN
            DROP TABLE IF EXISTS TABLE1;
        END IF;
```

##### Snowflake SQL

```sql
 BEGIN
-- ** SSC-EWI-0001 - UNRECOGNIZED TOKEN ON LINE '1' COLUMN '0' OF THE SOURCE CODE STARTING AT 'IF'. EXPECTED 'If Statement' GRAMMAR. LAST MATCHING TOKEN WAS 'null' ON LINE '1' COLUMN '48'. FAILED TOKEN WAS ')' ON LINE '1' COLUMN '52'. CODE '70'. **
--IF OBJECT_ID_UDF('DATABASE2.DBO.TABLE1') is not null) THEN
--** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "TABLE1" **
DROP TABLE IF EXISTS TABLE1;
END;
```

#### 2. Unknown database

##### SQL Server

```sql
 IF OBJECT_ID_UDF('DATABASE1.DBO.TABLE1') is not null) THEN
            DROP TABLE IF EXISTS TABLE1;
        END IF;
```

##### Snowflake SQL

```sql
  IF (
 OBJECT_ID_UDF('DATABASE1.DBO.TABLE1') is not null) THEN
     DROP TABLE IF EXISTS TABLE1;
 END IF;
```

#### 3. Different object names

##### SQL Server

```sql
 IF OBJECT_ID_UDF('DATABASE1.DBO.TABLE2') is not null) THEN
            DROP TABLE IF EXISTS TABLE1;
        END IF;
```

##### Snowflake SQL

```sql
  IF (
 OBJECT_ID_UDF('DATABASE1.DBO.TABLE2') is not null) THEN
     DROP TABLE IF EXISTS TABLE1;
 END IF;
```

### Known issues

**1. OBJECT_ID_UDF function has different behavior in certain cases**

OBJECT_ID returns the object identification number but the OBJECT_ID_UDF returns a boolean value, so that they are equivalent only when OBJECT_ID is used with not null condition.

### Related EWIs

* [SSC-EWI-0001](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Unrecognized token on the line of the source code.
* [SSC-FDM-0007](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/generalFDM.md): Element with missing dependencies

## Analytic Functions

This section describes the functional equivalents of analytic functions in Transact-SQL to Snowflake SQL and JavaScript code, oriented to the creation of UDFs in Snowflake.

## LAG

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

Accesses data from a previous row in the same result set without the use of a self-join starting with SQL Server 2012 (11.x).
LAG provides access to a row at a given physical offset that comes before the current row.
Use this analytic function in a SELECT statement to compare values in the current row with values in a previous row. (COUNT in Transact-SQL).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
LAG (scalar_expression [,offset] [,default])
    OVER ( [ partition_by_clause ] order_by_clause )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/count.html)

```sql
COUNT( [ DISTINCT ] <expr1> [ , <expr2> ... ] )
```

### Examples

#### SQL Server

```sql
SELECT TOP 10
LAG(E.VacationHours,1) OVER(ORDER BY E.NationalIdNumber) as PREVIOUS,
E.VacationHours AS ACTUAL
FROM HumanResources.Employee E
```

**Result:**

| PREVIOUS | ACTUAL |
| --- | --- |
| NULL | 10 |
| 10 | 89 |
| 89 | 10 |
| 10 | 48 |
| 48 | 0 |
| 0 | 95 |
| 95 | 55 |
| 55 | 67 |
| 67 | 84 |
| 84 | 85 |

##### Snowflake SQL

```sql
SELECT TOP 10
LAG(E.VacationHours,1) OVER(ORDER BY E.NationalIdNumber) as PREVIOUS,
E.VacationHours AS ACTUAL
FROM
HumanResources.Employee E;
```

**Result:**

| PREVIOUS | ACTUAL |
| --- | --- |
| NULL | 10 |
| 10 | 89 |
| 89 | 10 |
| 10 | 48 |
| 48 | 0 |
| 0 | 95 |
| 95 | 55 |
| 55 | 67 |
| 67 | 84 |
| 84 | 85 |

## Data Type functions

This section describes the functional equivalents of data type functions in Transact-SQL to Snowflake SQL and JavaScript code.

## DATALENGTH

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This function returns the number of bytes used to represent any expression. ([DATALENGTH in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/datalength-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
DATALENGTH ( expression )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/cast.html)

```sql
OCTET_LENGTH(<string_or_binary>)
```

### Examples

#### SQL Server

```sql
SELECT DATALENGTH('SomeString') AS SIZE;
```

**Result:**

| SIZE |
| --- |
| 10 |

##### Snowflake SQL

```sql
SELECT OCTET_LENGTH('SomeString') AS SIZE;
```

**Result:**

| SIZE |
| --- |
| 10 |

## Mathematical functions

This section describes the functional equivalents of mathematical functions in Transact-SQL to Snowflake SQL and JavaScript code, oriented to their usage in stored procedures in Snowflake.

## ABS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

A mathematical function that returns the absolute (positive) value of the specified numeric expression. (`ABS` changes negative values to positive values. `ABS` has no effect on zero or positive values.) ([ABS in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/abs-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
ABS( expression )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/abs.html)

```sql
ABS( <num_expr> )
```

##### JavaScript

[JavaScript complete documentation](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Math/abs)

```sql
Math.abs( expression )
```

### Examples

#### SQL Server

```sql
SELECT ABS(-5);
```

**Result:**

| ABS(-5) |
| --- |
| 5 |

##### Snowflake SQL

```sql
SELECT ABS(-5);
```

**Result:**

| ABS(-5) |
| --- |
| 5 |

##### JavaScript

```sql
CREATE OR REPLACE FUNCTION compute_abs(a float)
RETURNS float
LANGUAGE JAVASCRIPT
AS
$$
  return Math.abs(A);
$$
;
SELECT COMPUTE_ABS(-5);
```

**Result:**

| COMPUTE_ABS(-5) |
| --- |
| 5 |

### Related Documentation

* [Transact-SQL supported numeric types](https://docs.microsoft.com/en-us/sql/t-sql/data-types/numeric-types?view=sql-server-ver15)

## AVG

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

> **Note:**
>
> SnowConvert AI Helpers Code section is omitted.

This function returns the average of the values in a group. It ignores null values. ([AVG in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/avg-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
AVG ( [ ALL | DISTINCT ] expression )
   [ OVER ( [ partition_by_clause ] order_by_clause ) ]
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/avg.html)

```sql
AVG( [ DISTINCT ] <expr1> )

AVG( [ DISTINCT ] <expr1> ) OVER (
                                 [ PARTITION BY <expr2> ]
                                 [ ORDER BY <expr3> [ ASC | DESC ] [ <window_frame> ] ]
                                 )
```

### Examples

#### SQL Server

```sql
SELECT AVG(VACATIONHOURS) AS AVG_VACATIONS FROM HUMANRESOURCES.EMPLOYEE;
```

**Result:**

| AVG_VACATIONS |
| --- |
| 50 |

##### Snowflake SQL

```sql
SELECT AVG(VACATIONHOURS) AS AVG_VACATIONS FROM HUMANRESOURCES.EMPLOYEE;
```

**Result:**

| AVG_VACATIONS |
| --- |
| 50 |

## CEILING

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

A mathematical function that returns the smallest greater integer greater/equal to the number sent as a parameter ([CEILING in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/ceiling-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
CEILING( expression )
```

##### Snowflake SQL

```sql
CEIL( <input_expr> [, <scale_expr> ] )
```

##### JavaScript

```sql
 Math.ceil( expression )
```

### Examples

#### SQL Server

```sql
SELECT CEILING(642.20);
```

**Result:**

| CEILING(642.20) |
| --- |
| 643 |

##### Snowflake SQL

```sql
SELECT CEIL(642.20);
```

**Result:**

| CEIL(642.20) |
| --- |
| 643 |

##### JavaScript

```sql
CREATE OR REPLACE FUNCTION compute_ceil(a double)
RETURNS double
LANGUAGE JAVASCRIPT
AS
$$
  return Math.ceil(A);
$$
;
SELECT COMPUTE_CEIL(642.20);
```

**Result:**

```sql
COMPUTE_CEIL(642.20)|
--------------------|
                 643|
```

## FLOOR

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the largest integer less than or equal to the specified numeric expression. ([FLOOR in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/floor-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
FLOOR ( numeric_expression )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/floor.html)

```sql
FLOOR( <input_expr> [, <scale_expr> ] )
```

### Examples

#### SQL Server

```sql
SELECT FLOOR (124.87) AS FLOOR;
```

**Result:**

```sql
FLOOR|
-----|
  124|
```

##### Snowflake SQL

```sql
SELECT FLOOR (124.87) AS FLOOR;
```

**Result:**

```sql
FLOOR|
-----|
  124|
```

## POWER

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the value of the specified expression to the specified power. ([POWER in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/power-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
POWER ( float_expression , y )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/pow.html)

```sql
POW(x, y)

POWER (x, y)
```

### Examples

#### SQL Server

```sql
SELECT POWER(2, 10.0) AS IntegerResult
```

**Result:**

```sql
IntegerResult |
--------------|
          1024|
```

##### Snowflake SQL

```sql
SELECT POWER(2, 10.0) AS IntegerResult;
```

**Result:**

```sql
IntegerResult |
--------------|
          1024|
```

### Related Documentation

* [SQL Server supported numeric types](https://docs.microsoft.com/en-us/sql/t-sql/data-types/numeric-types?view=sql-server-ver15)

## ROUND

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a numeric value, rounded to the specified length or precision. ([ROUND in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/round-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
ROUND ( numeric_expression , length [ ,function ] )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/round.html)

```sql
ROUND( <input_expr> [, <scale_expr> ] )
```

### Examples

#### SQL Server

```sql
SELECT ROUND(123.9994, 3) AS COL1, ROUND(123.9995, 3) AS COL2;
```

**Result:**

```sql
COL1    |COL2    |
--------|--------|
123.9990|124.0000|
```

##### Snowflake SQL

```sql
SELECT ROUND(123.9994, 3) AS COL1,
ROUND(123.9995, 3) AS COL2;
```

**Result:**

```sql
COL1   | COL2  |
--------|------|
123.999|124.000|
```

### Related Documentation

* [SQL Server supported numeric types](https://docs.microsoft.com/en-us/sql/t-sql/data-types/numeric-types?view=sql-server-ver15)

## SQRT

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the square root of the specified float value. ([SQRT in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/sqrt-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
SQRT ( float_expression )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/sqrt.html)

```sql
SQRT(expr)
```

### Examples

#### SQL Server

```sql
SELECT SQRT(25) AS RESULT;
```

**Result:**

```sql
RESULT|
------|
   5.0|
```

##### Snowflake SQL

```sql
SELECT SQRT(25) AS RESULT;
```

**Result:**

```sql
RESULT|
------|
   5.0|
```

## SQUARE

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the square of the specified float value. ([SQUARE in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/square-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
SQUARE ( float_expression )  ****
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/square.html)

```sql
SQUARE(expr)
```

### Examples

#### SQL Server

```sql
SELECT SQUARE (5) AS SQUARE;
```

**Result:**

```sql
SQUARE|
------|
  25.0|
```

##### Snowflake SQL

```sql
SELECT SQUARE (5) AS SQUARE;
```

**Result:**

```sql
SQUARE|
------|
    25|
```

## STDEV

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

Returns the statistical standard deviation of all values in the specified expression. ([STDEV in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/degrees-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
 STDEV ( [ ALL | DISTINCT ] expression )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/stddev.html)

```sql
 STDDEV( [ DISTINCT ] <expression_1> )
```

### Examples

#### SQL Server

```sql
SELECT
    STDEV(VACATIONHOURS)
FROM
    HUMANRESOURCES.EMPLOYEE AS STDEV;
```

**Result:**

```sql
           STDEV|
----------------|
28.7862150320948|
```

##### Snowflake SQL

```sql
SELECT
    STDDEV(VACATIONHOURS)
FROM
    HUMANRESOURCES.EMPLOYEE AS STDEV;
```

**Result:**

```sql
       STDEV|
------------|
28.786215034|
```

## STDEVP

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

Returns the statistical standard deviation for the population for all values in the specified expression. ([STDVEP in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/degrees-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
STDEVP ( [ ALL | DISTINCT ] expression )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/stddev_pop.html)

```sql
STDDEV_POP( [ DISTINCT ] expression_1)
```

### Examples

#### SQL Server

```sql
SELECT
    STDEVP(VACATIONHOURS) AS STDEVP_VACATIONHOURS
FROM
    HumanResources.Employee;
```

**Result:**

```sql
STDEVP_VACATIONHOURS|
--------------------|
  28.736540767245085|
```

##### Snowflake SQL

```sql
SELECT
    STDDEV_POP(VACATIONHOURS) AS STDEVP_VACATIONHOURS
FROM
    HumanResources.Employee;
```

**Result:**

```sql
STDEVP_VACATIONHOURS|
--------------------|
        28.736540763|
```

## VAR

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

Returns the statistical variance of all values in the specified expression. ([VAR in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/var-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
VAR ( [ ALL | DISTINCT ] expression )
```

##### Snowflake SQL

```sql
VAR_SAMP( [DISTINCT] <expr1> )
```

### Examples

#### SQL Server

```sql
SELECT
    VAR(VACATIONHOURS)
FROM
    HUMANRESOURCES.EMPLOYEE AS VAR;
```

**Result:**

```sql
             VAR|
----------------|
28.7862150320948|
```

##### Snowflake SQL

```sql
SELECT
    VAR_SAMP(VACATIONHOURS)
FROM
    HUMANRESOURCES.EMPLOYEE AS VAR;
```

**Result:**

```sql
       VAR|
----------|
828.646176|
```

## POWER

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the value of the specified expression for a specific power.
([POWER in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/power-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
POWER( base, exp )
```

#### Arguments

`base`: Base of number, it must be a float expression.
`exp`: Power to which raise the base.

#### Return Type

The return type depends on the input expression:

| Input Type | Return Type |
| --- | --- |
| float, real | float |
| decimal(p, s) | decimal(38, s) |
| int, smallint, tinyint | int |
| bigint | bigint |
| money, smallmoney | money |
| bit, char, nchar, varchar, nvarchar | float |

### Examples

### Query

```sql
SELECT POWER(2, 3)
```

#### Result

```sql
POWER(2, 3)|
-----------|
        8.0|
```

## POW in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the base of the exponent power.
([JavaScript POW function Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/pow)).

### Sample Source Pattern

#### Syntax

```sql
 Math.pow( base, exp )
```

##### Arguments

`base`: Base of number, it must be a float expression.
`exp`: Power to which raise the base.

##### Return Type

Same data type sent through parameter as a numeric expression.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION compute_pow(base float, exp float)
  RETURNS float
  LANGUAGE JAVASCRIPT
AS
$$
    return Math.pow(BASE, EXP);
$$
;
SELECT COMPUTE_POW(2, 3);
```

##### Result

```sql
COMPUTE_POW(2, 3)|
-----------------|
                8|
```

## ACOS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Function that returns the arccosine in radians of the number sent as a parameter ([ACOS in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/acos-transact-sql?view=sql-server-ver15)).

Mathematically, the arccosine is the inverse function of the cosine, resulting in the following definition:
$$y = cos^{-1} \Leftrightarrow x = cos(y)$$

For $$y = cos^{-1}(x)$$:
* Range: $$0\leqslant y \leqslant \pi$$ or $$0^{\circ}\leqslant y \leqslant 180^{\circ}$$
* Domain: $$-1\leqslant x \leqslant 1$$

### Sample Source Pattern

### Syntax

```sql
ACOS ( expression )
```

#### Arguments

`expression`: Numeric **float** expression, where expression is in$$[-1,1]$$.

#### Return Type

Numeric float expression between 0 and π. If the numeric expression sent by parameter is out of the domain $$[-1, 1]$$, the database engine throws an error.

### Examples

### Query

```sql
SELECT ACOS(-1.0);
```

#### Result

```sql
ACOS(-1.0)       |
-----------------|
3.141592653589793|
```

## ACOS in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Function that returns the arccosine of a specified number
([JavaScript ACOS function Documentation](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Math/acos)).

### Sample Source Pattern

#### Syntax

```sql
 Math.acos( expression )
```

##### Arguments

`expression`: Numeric expression, where expression is in$$[-1,1]$$.

##### Return Type

Numeric expression between 0 and π. If the numeric expression sent by parameter is out of the range of the arccosine in radians $$[-1, 1]$$, the function returns NaN.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION compute_acos(a double)
  RETURNS double
  LANGUAGE JAVASCRIPT
AS
$$
  return Math.acos(A);
$$
;
SELECT COMPUTE_ACOS(-1);
```

##### Result

```sql
COMPUTE_ACOS(-1)|
---------------|
    3.141592654|
```

## ASIN

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Function that returns the arcsine in radians of the number sent as parameter ([ASIN in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/asin-transact-sql?view=sql-server-ver15)).

The arcsine is the inverse function of the sine , summarized in the next definition:
$$y = sin^{-1} \Leftrightarrow x = sin(x)$$

For $$y = sin^{-1}(x)$$:
* Range: $$-\frac{\pi}{2}\leqslant y \leqslant \frac{\pi}{2}$$ or $$-90^{\circ}\leqslant y \leqslant 90^{\circ}$$
* Domain: $$-1\leqslant x \leqslant 1$$

### Sample Source Pattern

### Syntax

```sql
ASIN( expression )
```

#### Arguments

`expression`: Numeric **float** expression, where expression is in$$[-1,1]$$.

#### Return Type

Numeric float expression between $$-\frac{\pi}{2}$$ and $$\frac{\pi}{2}$$. If the numeric expression sent by parameter is not in $$[-1, 1]$$, the database engine throws an error.

### Examples

### Query

```sql
SELECT ASIN(0.5);
```

#### Result

```sql
ASIN(0.5)         |
------------------|
0.5235987755982989|
```

## ASIN in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Function that returns the arcsine of a specified number
([JavaScript ASIN function Documentation](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Math/asin)).

### Sample Source Pattern

#### Syntax

```sql
 Math.asin( expression )
```

##### Arguments

`expression`: Numeric expression, where expression is in$$[-1,1]$$.

##### Return Type

Numeric expression between $$-\frac{\pi}{2}$$ and $$\frac{\pi}{2}$$. If the numeric expression sent by parameter is out of the domain of the arccosine $$[-1, 1]$$, the function returns NaN.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION compute_asin(a float)
  RETURNS float
  LANGUAGE JAVASCRIPT
AS
$$
  return Math.asin(A);
$$
;
SELECT COMPUTE_ASIN(0.5);
```

##### Result

```sql
COMPUTE_ASIN(1)   |
------------------|
      0.5235987756|
```

## COS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Function that returns the cosine of the angle sent through parameters (must be measured in radians) ([COS in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/cos-transact-sql?view=sql-server-ver15)).

The cosine is defined as:
$$y = cos(x)$$

### Sample Source Pattern

### Syntax

```sql
COS( expression )
```

#### Arguments

`expression`: Numeric **float** expression, where expression is in $$\mathbb{R}$$.

#### Return Type

Numeric float expression in $$[-1, 1]$$.

### Examples

### Query

```sql
SELECT COS(PI())
```

#### Result

```sql
COS(PI())|
---------|
     -1.0|
```

## COS in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Static function that returns the cosine of an angle in radians
([JavaScript COS function Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/cos)).

### Sample Source Pattern

#### Syntax

```sql
 Math.cos( expression )
```

##### Arguments

`expression:` Numeric expressions.

##### Return Type

Same data type sent through parameter as a numeric expression.

### Examples

#### Query

```sql
CREATE OR REPLACE FUNCTION compute_cos(angle float)
RETURNS float
LANGUAGE JAVASCRIPT
AS
$$
  return Math.cos(ANGLE);
$$
;
SELECT COMPUTE_COS(PI());
```

##### Result

```sql
COMPUTE_COS(PI())|
-----------------|
               -1|
```

## COT

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the cotangent of the angle in radians sent through parameters ([COT in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/cot-transact-sql?view=sql-server-ver15)).

The cosine is defined as:
$$cot(x) = \frac{cos(x)}{sin(x)}$$ or $$cot(x) = \frac{1}{tan(x)}$$
To calculate the cosine, the parameter must comply with the constraints of sine and cosine functions.

### Sample Source Pattern

### Syntax

```sql
COT( expression )
```

#### Arguments

`expression`: Numeric **float** expression, where expression is in $$\mathbb{R}-{sin(expression)=0 \wedge tan(expression) =0}$$.

#### Return Type

Numeric float expression in $$\mathbb{R}$$.

### Examples

### Query

```sql
SELECT COT(1)
```

#### Result

```sql
COT(1)            |
------------------|
0.6420926159343306|
```

## COT in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Unfortunately, the object `Math`in JavaScript does not provide a method to calculate the cotangent of a given angle.
This could be calculated using the equation: $$cot(x) = \frac{cos(x)}{sin(x)}$$

### Sample Source Pattern

#### Implementation example

```sql
 function cot(angle){
    return Math.cos(angle)/Math.sin(angle);
}
```

##### Arguments

`angle:` Numeric expression in radians.

##### Return Type

Same data type sent through parameter as a numeric expression.

### Examples

#### Query

```sql
CREATE OR REPLACE FUNCTION compute_cot(angle float)
RETURNS float
LANGUAGE JAVASCRIPT
AS
$$
  function cot(angle){
    return Math.cos(angle)/Math.sin(angle);
  }
  return cot(ANGLE);

$$
;
SELECT COMPUTE_COT(1);
```

##### Result

```sql
COMPUTE_COT(1);   |
------------------|
0.6420926159343308|
```

## RADIANS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Converts degrees to radians.
([RADIANS in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/radians-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
RADIANS( expression )
```

#### Arguments

`expression`: Numeric expression in degrees.

#### Return Type

Same data type sent through parameter as a numeric expression in radians.

### Examples

### Query

```sql
SELECT RADIANS(180.0)
```

#### Result

| RADIANS(180) |
| --- |
| 3.141592653589793116 |

> **Note:**
>
> Cast the parameter of this function to float, otherwise, the above statement will return 3 instead of PI value.

## RADIANS in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

JavaScript does not provide a method to convert degrees to radians of a given angle.
This could be calculated using the equation: $$Radians = \frac{\pi}{180^{\circ}} \cdot angle$$

### Sample Source Pattern

#### Implementation example

```sql
 function radians(angle){
    return (Math.PI/180) * angle;
}
```

##### Arguments

`angle`: Float expression in degrees.

##### Return Type

Same data type sent through parameter as a numeric expression in radians.

### Examples

#### Query

```sql
CREATE OR REPLACE FUNCTION RADIANS(angle float)
RETURNS float
LANGUAGE JAVASCRIPT
AS
$$
    function radians(angle){
      return (Math.PI/180) * angle;
    }
    return radians(ANGLE);
$$
;
SELECT RADIANS(180);
```

##### Result

| RADIANS(180) |
| --- |
| 3.141592654 |

## PI

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the constant value of PI
([PI in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/pi-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
PI( )
```

#### Arguments

This method does not receive any parameters.

#### Return Type

Float.

### Examples

### Query

```sql
CREATE PROCEDURE CIRCUMFERENCE @radius float
AS
    SELECT 2 * PI() * @radius;
GO:

EXEC CIRCUMFERENCE @radius = 2;
```

#### Result

```sql
CIRCUMFERENCE @radius = 2 |
--------------------------|
          12.5663706143592|
```

## PI in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Constant which represents the PI number (approximately 3.141592…)
([JavaScript PI Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/PI)).

### Sample Source Pattern

#### Syntax

```sql
 Math.PI
```

### Examples

#### Query

```sql
CREATE OR REPLACE FUNCTION circumference(radius float)
RETURNS float
LANGUAGE JAVASCRIPT
AS
$$
  function circumference(r){
    return 2 * Math.PI * r;
  }
  return circumference(RADIUS);
$$
;
SELECT CIRCUMFERENCE(2);
```

##### Result

```sql
  CIRCUMFERENCE(2)|
------------------|
12.566370614359172|
```

## DEGREES

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Converts the angle in radians sent through parameters to degrees ([DEGREES in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/degrees-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
DEGREES( expression )
```

#### Arguments

`expression`: Numeric **float** expression in radians.

#### Return Type

Same data type sent through parameter as a numeric expression.

### Examples

### Query

```sql
SELECT DEGREES(PI())
```

#### Result

```sql
DEGREES(PI())|
-------------|
        180.0|
```

## DEGREES in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

JavaScript does not provide a method to convert radians to degrees of a given angle.
This could be calculated using the equation: $$Degrees = \frac{180^{\circ}}{\pi} \cdot angle$$

### Sample Source Pattern

#### Implementation example

```sql
 function degress(angle){
    return (180/Math.PI) * angle;
}
```

##### Arguments

`angle`: Numeric expression in radians.

##### Return Type

Same data type sent through parameter as a numeric expression.

### Examples

#### Query

```sql
CREATE OR REPLACE FUNCTION compute_degrees(angle float)
RETURNS float
LANGUAGE JAVASCRIPT
AS
$$
  function degrees(angle){
    return (180/Math.PI) * angle;
  }
  return degrees(ANGLE);

$$
;
SELECT COMPUTE_DEGREES(PI());
```

##### Result

```sql
COMPUTE_DEGREES(PI())|
---------------------|
                180.0|
```

## LOG

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the natural logarithm of a number
([LOG in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/log-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
LOG( expression [, base ] )
```

#### Arguments

`expression`: Numeric expression.

`base` (optional): Base to calculate the logarithm of a number, it is Euler by default.

#### Return Type

Float.

### Examples

### Query

```sql
SELECT LOG(8, 2)
```

#### Result

```sql
LOG(8, 2)  |
-----------|
          3|
```

## LOG in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the logarithm using the Euler’s number as a base. ([JavaScript LOG function Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log)).

> **Warning:**
>
> Unfortunately, JavaScript does not provide a method that receives a logarithm base through its parameters, but this can be solved by dividing the base by the argument.

### Sample Source Pattern

#### Syntax

```sql
 Math.log( expression )
```

##### Arguments

`expression`: Numeric expression. It must be positive, otherwise returns NaN.\

##### Return Type

Same data type sent through parameter as a numeric expression.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION base_log(base float, exp float)
  RETURNS float
  LANGUAGE JAVASCRIPT
AS
$$
  function getBaseLog(x, y){
    return Math.log(y)/Math.log(x);
  }
  return getBaseLog(EXP, BASE)
$$
;
SELECT BASE_LOG(2, 8);
```

##### Result

```sql
BASE_LOG(2, 8)|
--------------|
             3|
```

## ATAN

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Function that returns the arctangent in radians of the number sent as a parameter ([ATAN in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/atan-transact-sql?view=sql-server-ver15)).

The arctangent is the inverse function of the tangent, summarized in the next definition:
$$y = arctan^{-1} \Leftrightarrow x = tan(x)$$

For $$y = tan^{-1}(x)$$:
* Range: $$-\frac{\pi}{2}\leqslant y \leqslant \frac{\pi}{2}$$ or $$-90^{\circ}\leqslant y \leqslant 90^{\circ}$$
* Domain: $$\mathbb{R}$$

### Sample Source Pattern

### Syntax

```sql
ATAN( expression )
```

#### Arguments

`expression`: Numeric **float** expression, or a numeric type which could be converted to float.

#### Return Type

Numeric float expression between $$-\frac{\pi}{2}$$ and $$\frac{\pi}{2}$$.

### Examples

### Query

```sql
SELECT ATAN(-30);
```

#### Result

```sql
ATAN(-30)          |
-------------------|
-1.5374753309166493|
```

## ATAN in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Function that returns the arctangent of a specified number
([JavaScript ATAN function Documentation](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Math/atan)).

### Sample Source Pattern

#### Syntax

```sql
 Math.atan( expression )
```

##### Arguments

`expression`: Numeric expression.

##### Return Type

Numeric expression between $$-\frac{\pi}{2}$$ and $$\frac{\pi}{2}$$.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION compute_atan(a float)
  RETURNS float
  LANGUAGE JAVASCRIPT
AS
$$
  return Math.atan(A);
$$
;
SELECT COMPUTE_ATAN(-30);
```

##### Result

```sql
COMPUTE_ATAN(-30)|
-----------------|
     -1.537475331|
```

## ATN2

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Function that returns the arctangent in radians of two coordinates sent as a parameter ([ATN2 in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/atn2-transact-sql?view=sql-server-ver15)).

For $$z = tan^{-1}(x, y)$$:
* Range: $$-\pi\leqslant z \leqslant \pi$$ or $$-180^{\circ}\leqslant z \leqslant 180^{\circ}$$
* Domain: $$\mathbb{R}$$

### Sample Source Pattern

### Syntax

```sql
ATN2( expression_1, expression_2 )
```

#### Arguments

`expression1`and `expression2`: Numeric expressions.

#### Return Type

Numeric expression between $$-\pi$$ and $$\pi$$.

### Examples

### Query

```sql
SELECT ATN2(7.5, 2);
```

#### Result

```sql
ATN2(7.5, 2)      |
------------------|
1.3101939350475555|
```

## ATAN2 in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Function that returns the arctangent of two parameters
([JavaScript ATAN2 function Documentation](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2)).

### Sample Source Pattern

#### Syntax

```sql
 Math.atan2( expression_1, expression_2 )
```

##### Arguments

`expression_1`and `expression_2`: Numeric expressions.

##### Return Type

Numeric expression between $$-\pi$$ and $$\pi$$.

### Examples

#### Query

```sql
CREATE OR REPLACE FUNCTION compute_atan2(x float, y float)
RETURNS float
LANGUAGE JAVASCRIPT
AS
$$
  return Math.atan2(X, Y);
$$
;
SELECT COMPUTE_ATAN2(7.5, 2);
```

##### Result

```sql
ATAN2(7.5, 3)     |
------------------|
       1.310193935|
```

## LOG10

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the base 10 logarithm of a number
([LOG10 in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/log10-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
LOG10( expression )
```

#### Arguments

`expression`: Numeric expression, must be positive.

#### Return Type

Float.

### Examples

### Query

```sql
SELECT LOG10(5)
```

#### Result

```sql
LOG10(5)         |
-----------------|
0.698970004336019|
```

## LOG10 in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the base 10 logarithm of a number
([JavaScript LOG10 function Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log10)).

### Sample Source Pattern

#### Syntax

```sql
 Math.log10( expression )
```

##### Arguments

`expression`: Numeric expression. It must be positive, otherwise returns NaN.\

##### Return Type

Same data type sent through parameter as a numeric expression.

### Examples

#### Query

```sql
 CREATE OR REPLACE FUNCTION compute_log10(argument float)
  RETURNS float
  LANGUAGE JAVASCRIPT
AS
$$
    return Math.log10(ARGUMENT);
$$
;
SELECT COMPUTE_LOG10(7.5);
```

##### Result

```sql
COMPUTE_LOG10(5)|
----------------|
    0.6989700043|
```

## EXP

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the exponential value of Euler ([EXP in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/exp-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

### Syntax

```sql
EXP( expression )
```

#### Arguments

`expression`: Numeric expression.

#### Return Type

Same data type sent through parameter as a numeric expression.

### Examples

### Query

```sql
SELECT EXP(LOG(20)), LOG(EXP(20))
GO
```

#### Result

```sql
EXP(LOG(20))   |LOG(EXP(20))    |
---------------|----------------|
           20.0|            20.0|
```

## EXP in JS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Constant which represents Euler’s number (approximately 2.718…)
([JavaScript Euler’s Number Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/E)).
JavaScript allows make different operations using this constant, instead of Transact-SQL which only supports the exponential of Euler.

### Sample Source Pattern

#### Syntax

```sql
 Math.E
```

### Examples

#### Query

```sql
CREATE OR REPLACE FUNCTION compute_exp(x float)
RETURNS float
LANGUAGE JAVASCRIPT
AS
$$
  return Math.E**X;
$$
;
SELECT COMPUTE_EXP(LN(20)), LN(COMPUTE_EXP(20));
```

##### Result

```sql
COMPUTE_EXP(LOG(20))|LOG(COMPUTE_EXP(20))|
--------------------|--------------------|
                20.0|                20.0|
```

## Conversion functions

This section describes the functional equivalents of date & time functions in Transact-SQL to Snowflake SQL code.

## CONVERT

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Convert an expression of one data type to another. ([CONVERT in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/cast-and-convert-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
CONVERT ( data_type [ ( length ) ] , expression [ , style ] )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/cast.html)

```sql
CAST( <source_expr> AS <target_data_type> )
```

### Examples

#### SQL Server

```sql
SELECT CONVERT(INT, '1998') as MyDate
```

##### Result

| MyDate |
| --- |
| 1998 |

##### Snowflake SQL

```sql
SELECT
CAST('1998' AS INT) as MyDate;
```

##### Result

| MYDATE |
| --- |
| 1998 |

##### Casting date type to varchar

##### SQL Server

```sql
SELECT CONVERT(varchar, getdate(), 1) AS RESULT;
```

##### Result

| RESULT |
| --- |
| 12/08/22 |

##### Swowflake SQL

```sql
SELECT
TO_VARCHAR(CURRENT_TIMESTAMP() :: TIMESTAMP, 'mm/dd/yy') AS RESULT;
```

##### Result

| RESULT |
| --- |
| 12/08/22 |

##### Casting date type to varchar with size

##### SQL Server

```sql
SELECT CONVERT(varchar(2), getdate(), 1) AS RESULT;
```

##### Result

| RESULT |
| --- |
| 07 |

##### Snowflake SQL

```sql
SELECT
LEFT(TO_VARCHAR(CURRENT_TIMESTAMP() :: TIMESTAMP, 'mm/dd/yy'), 2) AS RESULT;
```

##### Result

| RESULT |
| --- |
| 07 |

The supported formats for dates casts are:

**Date formats**

| Code | Format |
| --- | --- |
| 1 | mm/dd/yy |
| 2 | yy.mm.dd |
| 3 | dd/mm/yy |
| 4 | dd.mm.yy |
| 5 | dd-mm-yy |
| 6 | dd-Mon-yy |
| 7 | Mon dd, yy |
| 10 | mm-dd-yy |
| 11 | yy/mm/dd |
| 12 | yymmdd |
| 23 | yyyy-mm-dd |
| 101 | mm/dd/yyyy |
| 102 | yyyy.mm.dd |
| 103 | dd/mm/yyyy |
| 104 | dd.mm.yyyy |
| 105 | dd-mm-yyyy |
| 106 | dd Mon yyyy |
| 107 | Mon dd, yyyy |
| 110 | mm-dd-yyyy |
| 111 | yyyy/mm/dd |
| 112 | yyyymmdd |

**Time formats**

| Code | Format |
| --- | --- |
| 8 | hh:mm:ss |
| 14 | hh:mm:ss:ff3 |
| 24 | hh:mm:ss |
| 108 | hh:mm:ss |
| 114 | hh:mm:ss:ff3 |

**Date and time formats**

|  |  |
| --- | --- |
| 0 | Mon dd yyyy hh:mm AM/PM |
| 9 | Mon dd yyyy hh:mm:ss:ff3 AM/PM |
| 13 | dd Mon yyyy hh:mm:ss:ff3 AM/PM |
| 20 | yyyy-mm-dd hh:mm:ss |
| 21 | yyyy-mm-dd hh:mm:ss:ff3 |
| 22 | mm/dd/yy hh:mm:ss AM/PM |
| 25 | yyyy-mm-dd hh:mm:ss:ff3 |
| 100 | Mon dd yyyy hh:mm AM/PM |
| 109 | Mon dd yyyy hh:mm:ss:ff3 AM/PM |
| 113 | dd Mon yyyy hh:mm:ss:ff3 |
| 120 | yyyy-mm-dd hh:mm:ss |
| 121 | yyyy-mm-dd hh:mm:ss:ff3 |
| 126 | yyyy-mm-dd T hh:mm:ss:ff3 |
| 127 | yyyy-mm-dd T hh:mm:ss:ff3 |

**Islamic calendar dates**

| Code | Format |
| --- | --- |
| 130 | dd mmm yyyy hh:mi:ss:ff3 AM/PM |
| 131 | dd mmm yyyy hh:mi:ss:ff3 AM/PM |

If there is no pattern matching with the current code, it will be formatted to `yyyy-mm-dd hh:mm:ss`

## TRY_CONVERT

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a value cast to the specified data type if the cast succeeds; otherwise, returns null.

([SQL Server Language Reference TRY_CONVERT](https://docs.microsoft.com/en-us/sql/t-sql/functions/try-convert-transact-sql?view=sql-server-ver15))

#### Syntax

```sql
TRY_CONVERT ( data_type [ ( length ) ], expression [, style ] )
```

### Source Patterns

#### Basic Transformation

To transform this function, we have to check the parameters of the TRY_CONVERT first.

```sql
TRY_CONVERT( INT, 'test')
```

If the expression that needs to be casted is a string, it will be transfomed to TRY_CAST, which is a function of Snowflake.

```sql
TRY_CAST( 'test' AS INT)
```

#### TRY_CAST

The TRY_CAST shares the same transformation with TRY_CONVERT.

##### Example

##### Sql Server

```sql
SELECT TRY_CAST('12345' AS NUMERIC) NUMERIC_RESULT,
 TRY_CAST('123.45' AS DECIMAL(20,2)) DECIMAL_RESULT,
 TRY_CAST('123' AS INT) INT_RESULT,
 TRY_CAST('123.02' AS FLOAT) FLOAT_RESULT,
 TRY_CAST('123.02' AS DOUBLE PRECISION) DOUBLE_PRECISION_RESULT,

 TRY_CAST('2017-01-01 12:00:00' AS DATE) DATE_RESULT,
 TRY_CAST('2017-01-01 12:00:00' AS DATETIME) DATETIME_RESULT,
 TRY_CAST('2017-01-01 12:00:00' AS SMALLDATETIME) SMALLDATETIME_RESULT,
 TRY_CAST('12:00:00' AS TIME) TIME_RESULT,
 TRY_CAST('2017-01-01 12:00:00' AS TIMESTAMP) TIMESTAMP_RESULT,
 TRY_CAST('2017-01-01 12:00:00' AS DATETIMEOFFSET) DATETIMEOFFSET_RESULT,

 TRY_CAST(1234 AS VARCHAR) VARCHAR_RESULT,
 TRY_CAST(1 AS CHAR) CHAR_RESULT,
 TRY_CAST('2017-01-01 12:00:00' AS SQL_VARIANT) SQL_VARIANT_RESULT,
 TRY_CAST('LINESTRING(-122.360 47.656, -122.343 47.656 )' AS GEOGRAPHY) GEOGRAPHY_RESULT;
```

The result will be the same with the example of TRY_CONVERT.

##### Snowflake

```sql
SELECT
 TRY_CAST('12345' AS NUMERIC(38, 18)) NUMERIC_RESULT,
 TRY_CAST('123.45' AS DECIMAL(20,2)) DECIMAL_RESULT,
 TRY_CAST('123' AS INT) INT_RESULT,
 TRY_CAST('123.02' AS FLOAT) FLOAT_RESULT,
 TRY_CAST('123.02' AS DOUBLE PRECISION) DOUBLE_PRECISION_RESULT,
 TRY_CAST('2017-01-01 12:00:00' AS DATE) DATE_RESULT,
 TRY_CAST('2017-01-01 12:00:00' AS TIMESTAMP_NTZ(3)) DATETIME_RESULT,
 TRY_CAST('2017-01-01 12:00:00' AS TIMESTAMP_NTZ(0)) SMALLDATETIME_RESULT,
 TRY_CAST('12:00:00' AS TIME(7)) TIME_RESULT,
 TRY_CAST('2017-01-01 12:00:00' AS BINARY(8)) TIMESTAMP_RESULT,
 TRY_CAST('2017-01-01 12:00:00' AS TIMESTAMP_TZ(7)) DATETIMEOFFSET_RESULT,
 TO_VARCHAR(1234) VARCHAR_RESULT,
 TO_CHAR(1) CHAR_RESULT,
 TRY_CAST('2017-01-01 12:00:00' AS VARIANT) SQL_VARIANT_RESULT,
 TRY_CAST('LINESTRING(-122.360 47.656, -122.343 47.656 )' AS GEOGRAPHY) GEOGRAPHY_RESULT;
```

### Known Issues

If the data type is Varchar or Char, then it will be transformed differently.

```sql
TRY_CONVERT(VARCHAR, 1234);
TRY_CONVERT(CHAR, 1);
```

If TRY_CAST is used with VARCHAR or CHAR in Snowflake, it will cause an error, so it will be transformed to

```sql
TO_VARCHAR(1234);
TO_CHAR(1);
```

The same happens with the data types of SQL_VARIANT and GEOGRAPHY.

```sql
TRY_CONVERT(SQL_VARIANT, '2017-01-01 12:00:00');
TRY_CONVERT(GEOGRAPHY, 'LINESTRING(-122.360 47.656, -122.343 47.656 )');
```

Are transformed to

```sql
TO_VARIANT('2017-01-01 12:00:00');
TO_GEOGRAPHY('LINESTRING(-122.360 47.656, -122.343 47.656 )');
```

If the expression is not a string, there is a very high chance that it will fail, since the TRY_CAST of snowflake works only with string expressions.

In this case, another transformation will be done

```sql
TRY_CAST(14.85 AS INT)
```

Will be transformed to

```sql
CAST(14.85 AS INT) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/
```

Now, with these transformation, there could be problems depending on what is being done with the functions. The TRY_CONVERT of SqlServer returns nulls if the convertion was not possible.

This can be used to do logic like this

```sql
SELECT
    CASE
        WHEN TRY_CONVERT( INT, 'Expression') IS NULL
        THEN 'FAILED'
        ELSE 'SUCCEDDED'
    END;
```

That type of conditions with the TRY_CONVERT can be used with the TRY_CAST, but what happens if it is transformed to TO_VARCHAR, TOCHAR or to the CAST? If the convertion in those functions fails, it will cause an error instead of just returning null.

#### Examples

In this sample we have several TRY_CONVERT with different data types

##### SQL Server

```sql
SELECT TRY_CONVERT(NUMERIC, '12345') NUMERIC_RESULT,
 TRY_CONVERT(DECIMAL(20,2), '123.45') DECIMAL_RESULT,
 TRY_CONVERT(INT, '123') INT_RESULT,
 TRY_CONVERT(FLOAT, '123.02') FLOAT_RESULT,
 TRY_CONVERT(DOUBLE PRECISION, '123.02') DOUBLE_PRECISION_RESULT,

 TRY_CONVERT(DATE, '2017-01-01 12:00:00') DATE_RESULT,
 TRY_CONVERT(DATETIME, '2017-01-01 12:00:00') DATETIME_RESULT,
 TRY_CONVERT(SMALLDATETIME, '2017-01-01 12:00:00') SMALLDATETIME_RESULT,
 TRY_CONVERT(TIME, '12:00:00') TIME_RESULT,
 TRY_CONVERT(TIMESTAMP, '2017-01-01 12:00:00') TIMESTAMP_RESULT,
 TRY_CONVERT(DATETIMEOFFSET, '2017-01-01 12:00:00') DATETIMEOFFSET_RESULT,

 TRY_CONVERT(VARCHAR, 1234) VARCHAR_RESULT,
 TRY_CONVERT(CHAR, 1) CHAR_RESULT,
 TRY_CONVERT(SQL_VARIANT, '2017-01-01 12:00:00') SQL_VARIANT_RESULT,
 TRY_CONVERT(GEOGRAPHY, 'LINESTRING(-122.360 47.656, -122.343 47.656 )') GEOGRAPHY_RESULT;
```

If we migrate that select, we will get the following result

##### Snowflake

```sql
SELECT
 CAST('12345' AS NUMERIC(38, 18)) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/ NUMERIC_RESULT,
 CAST('123.45' AS DECIMAL(20,2)) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/ DECIMAL_RESULT,
 CAST('123' AS INT) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/ INT_RESULT,
 CAST('123.02' AS FLOAT) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/ FLOAT_RESULT,
 CAST('123.02' AS DOUBLE PRECISION) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/ DOUBLE_PRECISION_RESULT,
 CAST('2017-01-01 12:00:00' AS DATE) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/ DATE_RESULT,
 CAST('2017-01-01 12:00:00' AS TIMESTAMP_NTZ(3)) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/ DATETIME_RESULT,
 CAST('2017-01-01 12:00:00' AS TIMESTAMP_NTZ(0)) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/ SMALLDATETIME_RESULT,
 CAST('12:00:00' AS TIME(7)) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/ TIME_RESULT,
 CAST('2017-01-01 12:00:00' AS BINARY(8)) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/ TIMESTAMP_RESULT,
 CAST('2017-01-01 12:00:00' AS TIMESTAMP_TZ(7)) /*** SSC-FDM-TS0005 - TRY_CONVERT/TRY_CAST COULD NOT BE CONVERTED TO TRY_CAST ***/ DATETIMEOFFSET_RESULT,
 TO_VARCHAR(1234) VARCHAR_RESULT,
 TO_CHAR(1) CHAR_RESULT,
 TO_VARIANT('2017-01-01 12:00:00') SQL_VARIANT_RESULT,
 TO_GEOGRAPHY('LINESTRING(-122.360 47.656, -122.343 47.656 )') GEOGRAPHY_RESULT;
```

Let’s execute each one and compare the result.

| Alias | SqlServer Result | Snowflake Result |
| --- | --- | --- |
| NUMERIC_RESULT | 12345 | 12345 |
| DECIMAL_RESULT | 123.45 | 123.45 |
| INT_RESULT | 123 | 123 |
| FLOAT_RESULT | 123.02 | 123.02 |
| DOUBLE_PRECISION_RESULT | 123.02 | 123.02 |
| DATE_RESULT | 2017-01-01 | 2017-01-01 |
| DATETIME_RESULT | 2017-01-01 12:00:00.000 | 2017-01-01 12:00:00.000 |
| SMALLDATETIME_RESULT | 2017-01-01 12:00:00 | 2017-01-01 12:00:00.000 |
| TIME_RESULT | 12:00:00.0000000 | 12:00:00 |
| TIMESTAMP_RESULT | 0x323031372D30312D | 2017-01-01 12:00:00.000 |
| DATETIMEOFFSET_RESULT | 2017-01-01 12:00:00.0000000 +00:00 | 2017-01-01 12:00:00.000 -0800 |
| VARCHAR_RESULT | 1234 | 1234 |
| CHAR_RESULT | 1 | 1 |
| SQL_VARIANT_RESULT | 2017-01-01 12:00:00 | “2017-01-01 12:00:00” |
| GEOGRAPHY_RESULT | 0xE610000001148716D9CEF7D34740D7A3703D0A975EC08716D9CEF7D34740CBA145B6F3955EC0 | { “coordinates”: [ [ -122.36, 47.656 ], [ -122.343, 47.656 ] ], “type”: “LineString” } |

### Related EWIs

1. [SSC-FDM-TS0005](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/sqlServerFDM.md): TRY_CONVERT/TRY_CAST could not be converted to TRY_CAST.

## Date & Time functions

This section describes the functional equivalents of date & time functions in Transact-SQL to Snowflake SQL and JavaScript code.

## AT TIME ZONE

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Converts an *inputdate* to the corresponding *datetimeoffset* value in the target time zone. ([AT TIME ZONE in Transact-SQL](https://learn.microsoft.com/en-us/sql/t-sql/queries/at-time-zone-transact-sql?view=sql-server-ver16)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
inputdate AT TIME ZONE timezone
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/convert_timezone.html)

```sql
CONVERT_TIMEZONE( <source_tz> , <target_tz> , <source_timestamp_ntz> )

CONVERT_TIMEZONE( <target_tz> , <source_timestamp> )
```

### Examples

#### SQL Server

```sql
SELECT CAST('2022-11-24 11:00:45.2000000 +00:00' as datetimeoffset) at time zone 'Alaskan Standard Time';
```

**Result:**

```sql
                          DATE|
------------------------------|
2022-11-24 02:00:45.200 -09:00|
```

##### Snowflake SQL

```sql
SELECT
CONVERT_TIMEZONE('America/Anchorage', CAST('2022-11-24 11:00:45.2000000 +00:00' as TIMESTAMP_TZ(7)));
```

**Result:**

```sql
                          DATE|
------------------------------|
2022-11-24 02:00:45.200 -09:00|
```

##### SQL Server

```sql
SELECT current_timestamp at time zone 'Central America Standard Time';
```

**Result:**

```sql
                          DATE|
------------------------------|
2022-10-10 10:55:50.090 -06:00|
```

##### Snowflake SQL

```sql
SELECT
CONVERT_TIMEZONE('America/Costa_Rica', CURRENT_TIMESTAMP() /*** SSC-FDM-TS0024 - CURRENT_TIMESTAMP in At Time Zone statement may have a different behavior in certain cases ***/);
```

**Result:**

```sql
                          DATE|
------------------------------|
2022-10-10 10:55:50.090 -06:00|
```

### Known Issues

1. Snowflake does not support all the time zones that SQL Server does. You can check the supported time zones at this [link](https://docs.snowflake.com/en/sql-reference/functions/convert_timezone.html).

#### SQL Server

```sql
SELECT current_timestamp at time zone 'Turks And Caicos Standard Time';
```

**Result:**

```sql
                          DATE|
------------------------------|
2022-12-14 20:04:18.317 -05:00|
```

##### Snowflake SQL

```sql
SELECT
!!!RESOLVE EWI!!! /*** SSC-EWI-TS0063 - TIME ZONE NOT SUPPORTED IN SNOWFLAKE ***/!!!
CURRENT_TIMESTAMP() at time zone 'Turks And Caicos Standard Time';
```

### Related EWIs

1. [SSC-FDM-TS0024](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/sqlServerFDM.md): CURRENT_TIMESTAMP in At Time Zone statement may have a different behavior in certain cases.
2. [SSC-EWI-TS0063](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/sqlServerEWI.md): Time zone not supported in Snowflake.

## DATEADD

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This function returns an integer representing the specified datepart of the specified date. ([DATEPART in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/abs-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
DATEADD (datepart , number , date )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/dateadd.html)

```sql
DATEADD( <date_or_time_part>, <value>, <date_or_time_expr> )
```

### Examples

#### SQL Server

```sql
SELECT DATEADD(year,123, '20060731') as ADDDATE;
```

**Result:**

```sql
                 ADDDATE|
------------------------|
 2129-07-31 00:00:00.000|
```

##### Snowflake SQL

```sql
SELECT
DATEADD(year, 123, '20060731') as ADDDATE;
```

**Result:**

```sql
                 ADDDATE|
------------------------|
 2129-07-31 00:00:00.000|
```

## DATEDIFF

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This function returns the count (as a signed integer value) of the specified datepart boundaries crossed between the specified startdate and enddate. ([DATEDIFF in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/datediff-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
DATEDIFF ( datepart , startdate , enddate )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/datediff.html)

```sql
DATEDIFF( <date_or_time_part>, <date_or_time_expr1>, <date_or_time_expr2> )
```

### Examples

#### SQL Server

```sql
SELECT DATEDIFF(year,'2005-12-31 23:59:59.9999999', '2006-01-01 00:00:00.0000000');
```

**Result:**

| DIFF |
| --- |
| 1 |

##### Snowflake SQL

```sql
SELECT DATEDIFF(year,'2005-12-31 23:59:59.9999999', '2006-01-01 00:00:00.0000000');
```

**Result:**

| DIFF |
| --- |
| 1 |

## DATEFROMPARTS

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This function returns a **date** value that maps to the specified year, month, and day values.([DATEFROMPARTS in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/datefromparts-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
DATEFROMPARTS ( year, month, day )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/date_from_parts.html)

```sql
DATE_FROM_PARTS( <year>, <month>, <day> )
```

### Examples

#### SQL Server

```sql
SELECT DATEFROMPARTS ( 2010, 12, 31 ) AS RESULT;
```

**Result:**

| RESULT |
| --- |
| 2022-12-12 |

##### Snowflake SQL

```sql
SELECT DATE_FROM_PARTS ( 2010, 12, 31 ) AS RESULT;
```

**Result:**

| RESULT |
| --- |
| 2022-12-12 |

## DATENAME

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This function returns a character string representing the specified datepart of the specified date. ([DATENAME in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/datename-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
DATENAME ( datepart , date )
```

##### Snowflake SQL

> **Note:**
>
> This transformation uses several functions depending on the inputs

```sql
DATE_PART( <date_or_time_part> , <date_or_time_expr> )
MONTHNAME( <date_or_timestamp_expr> )
DAYNAME( <date_or_timestamp_expr> )
```

### Examples

#### SQL Server

```sql
SELECT DATENAME(month, getdate()) AS DATE1,
DATENAME(day, getdate()) AS DATE2,
DATENAME(dw, GETDATE()) AS DATE3;
```

**Result:**

| DATE1 | DATE2 | DATE3 |
| --- | --- | --- |
| May | 3 | Tuesday |

##### Snowflake SQL

```sql
SELECT
MONTHNAME_UDF(CURRENT_TIMESTAMP() :: TIMESTAMP) AS DATE1,
DAYNAME_UDF(CURRENT_TIMESTAMP() :: TIMESTAMP) AS DATE2,
DAYNAME(CURRENT_TIMESTAMP() :: TIMESTAMP) AS DATE3;
```

**Result:**

| DATE1 | DATE2 | DATE3 |
| --- | --- | --- |
| May | Tue | Tue |

## DATEPART

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This function returns an integer representing the specified datepart of the specified date. ([DATEPART in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/abs-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
DATEPART ( datepart , date )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/date_part.html)

```sql
DATE_PART( <date_or_time_part> , <date_or_time_expr> )
```

### Examples

#### SQL Server

```sql
SELECT DATEPART(YEAR, '10-10-2022') as YEAR
```

**Result:**

| YEAR |
| --- |
| 2022 |

##### Snowflake SQL

```sql
SELECT
DATE_PART(YEAR, '10-10-2022' :: TIMESTAMP) as YEAR;
```

**Result:**

| YEAR |
| --- |
| 2022 |

## DAY

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This function returns an integer that represents the day (day of the month) of the specified date. ([DAY in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/day-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
DAY ( date )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/year.html)

```sql
DAY( <date_or_timestamp_expr> )
```

### Examples

#### SQL Server

```sql
SELECT DAY('10-10-2022') AS DAY
```

**Result:**

| DAY |
| --- |
| 10 |

##### Snowflake SQL

```sql
SELECT DAY('10-10-2022' :: TIMESTAMP) AS DAY;
```

**Result:**

| DAY |
| --- |
| 10 |

## EOMONTH

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

This function returns the last day of the month containing a specified date, with an optional offset. ([EOMONTH in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/eomonth-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
EOMONTH ( start_date [, month_to_add ] )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/last_day.html)

```sql
LAST_DAY( <date_or_time_expr> [ , <date_part> ] )
```

### Examples

#### SQL Server

```sql
SELECT EOMONTH (GETDATE()) AS Result;
```

**Result:**

| RESULT |
| --- |
| 2022-05-31 |

##### Snowflake SQL

```sql
SELECT
LAST_DAY(DATEADD('month', 0, CURRENT_TIMESTAMP() :: TIMESTAMP)) AS Result;
```

**Result:**

| RESULT |
| --- |
| 2022-05-31 |

## GETDATE

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns the current database system timestamp as a **datetime** value without the database time zone offset. ([GETDATE in Transact-SQL](https://learn.microsoft.com/en-us/sql/t-sql/functions/getdate-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
GETDATE()
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/current_timestamp.html)

```sql
CURRENT_TIMESTAMP( [ <fract_sec_precision> ] )
```

### Examples

#### SQL Server

```sql
SELECT GETDATE() AS DATE;
```

**Result:**

| DATE |
| --- |
| 2022-05-06 09:54:42.757 |

##### Snowflake SQL

```sql
SELECT CURRENT_TIMESTAMP() :: TIMESTAMP AS DATE;
```

**Result:**

| DATE |
| --- |
| 2022-05-06 08:55:05.422 |

## MONTH

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns an integer that represents the month of the specified *date*. ([MONTH in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/month-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
MONTH( date )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/year.html)

```sql
MONTH ( <date_or_timestamp_expr> )
```

### Examples

#### SQL Server

```sql
SELECT MONTH('10-10-2022') AS MONTH
```

**Result:**

| MONTH |
| --- |
| 10 |

##### Snowflake SQL

```sql
SELECT MONTH('10-10-2022' :: TIMESTAMP) AS MONTH;
```

**Result:**

| MONTH |
| --- |
| 10 |

## SWITCHOFFSET

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

The SWITCHOFFSET adjusts a given timestamp value to a specific timezone offset. This is done through numerical values. More information can be found at [SWITCHOFFSET (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/switchoffset-transact-sql?view=sql-server-ver16).

### Sample Source Pattern

#### Syntax

A UDF Helper accomplish functional equivalence, also it shares the same syntax as the SQLServer’s SWITCHOFFSET function.

##### SQLServer

```sql
 SWITCHOFFSET ( datetimeoffset_expression, timezoneoffset_expression )
```

##### Snowflake SQL

```sql
 SWITCHOFFSET_UDF ( timestamp_tz_expression, timezoneoffset_expression )
```

#### Example

##### SQLServer

```sql
SELECT
  '1998-09-20 7:45:50.71345 +02:00' as fr_time,
  SWITCHOFFSET('1998-09-20 7:45:50.71345 +02:00', '-06:00') as cr_time;
```

**Result:**

| fr_time | cr_time |
| --- | --- |
| 1998-09-20 7:45:50.71345 +02:00 | 1998-09-19 23:45:50.7134500 -06:00 |

##### Snowflake SQL

```sql
SELECT
  '1998-09-20 7:45:50.71345 +02:00' as fr_time,
  PUBLIC.SWITCHOFFSET_UDF('1998-09-20 7:45:50.71345 +02:00', '-06:00') as cr_time;
```

**Result:**

| fr_time | cr_time |
| --- | --- |
| 1998-09-20 7:45:50.71345 +02:00 | 1998-09-19 23:45:50.7134500 -06:00 |

## SYSDATETIME

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a datetime2(7) value that contains the date and time of the computer on which the instance of SQL Server is running. ([SYSDATETIME in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/sysdatetime-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
SYSDATETIME ( )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/localtime.html)

```sql
LOCALTIME()
```

### Examples

#### SQL Server

```sql
SELECT SYSDATETIME ( ) AS SYSTEM_DATETIME;
```

**Result:**

| SYSTEM_DATETIME |
| --- |
| 2022-05-06 12:08:05.501 |

##### Snowflake SQL

```sql
SELECT LOCALTIME ( ) AS SYSTEM_DATETIME;
```

**Result:**

| SYSTEM_DATETIME |
| --- |
| 211:09:14 |

## SYSUTCDATETIME

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns a datetime2(7) value that contains the date and time of the computer on which the instance of SQL Server is running. ([SYSUTCDATETIME in Transact-SQL](https://learn.microsoft.com/en-us/sql/t-sql/functions/sysutcdatetime-transact-sql?view=sql-server-ver16)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
SYSUTCDATETIME ( )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/localtime.html)

```sql
SYSDATE()
```

### Examples

#### SQL Server

```sql
SELECT SYSUTCDATETIME() as SYS_UTC_DATETIME;
```

**Result:**

| SYSTEM_UTC_DATETIME |
| --- |
| 2023-02-02 20:59:28.0926502 |

##### Snowflake SQL

```sql
SELECT
SYSDATE() as SYS_UTC_DATETIME;
```

**Result:**

| SYSTEM_UTC_DATETIME |
| --- |
| 2023-02-02 21:02:05.557 |

## YEAR

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Returns an integer that represents the year of the specified *date*. ([YEAR in Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/functions/year-transact-sql?view=sql-server-ver15)).

### Sample Source Pattern

#### Syntax

##### SQL Server

```sql
YEAR( date )
```

##### Snowflake SQL

[Snowflake SQL Documentation](https://docs.snowflake.com/en/sql-reference/functions/year.html)

```sql
YEAR ( <date_or_timestamp_expr> )
```

### Examples

#### SQL Server

```sql
SELECT YEAR('10-10-2022') AS YEAR
```

**Result:**

| YEAR |
| --- |
| 2022 |

##### Snowflake SQL

```sql
SELECT YEAR('10-10-2022' :: TIMESTAMP) AS YEAR;
```

**Result:**

| YEAR |
| --- |
| 2022 |
