# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/functional-difference/sybaseFDM.md

# SnowConvert AI - Sybase IQ Functional Differences

> **Note:**
>
> **Conversion Scope**
>
> SnowConvert AI for Sybase IQ focuses its assessment and translation capabilities primarily on TABLES, VIEWS, STORED PROCEDURES, and FUNCTIONS.
> While SnowConvert AI can recognize other types of ANSI-standard statements, these are not yet fully supported for conversion. This means that while the tool may identify them, it won’t perform a complete translation for these unsupported code units.

## SSC-FDM-SY0001

Calling stored procedure in FROM might have compilation errors

### Description

Snowflake supports calling a stored procedure in the FROM clause when the procedure meets certain [conditions](https://docs.snowflake.com/en/developer-guide/stored-procedure/stored-procedures-selecting-from#limitations-for-selecting-from-a-stored-procedure) otherwise the query fails.

#### Code Example

##### Input Code

##### Sybase

```sql
 SELECT * FROM MyProcedure(1, 'test');
```

##### Generated Code

##### Snowflake

```sql
 SELECT
  *
FROM
  --** SSC-FDM-SY0001 - CALLING STORED PROCEDURE IN FROM CLAUSE MIGHT HAVE COMPILATION ERRORS **
  TABLE(MyProcedure(1, 'test'));
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-FDM-SY0002

Calling stored procedure in FROM might have compilation errors

### Description

Snowflake does not contain indexes for query optimization.

#### Code Example

##### Input Code

##### Sybase

```sql
 SELECT * FROM TABLE1 FORCE INDEX (MyIndex);
```

##### Generated Code

##### Snowflake

```sql
 SELECT
  *
FROM
  TABLE1
--         --** SSC-FDM-SY0002 - FORCE INDEX IS NOT SUPPORTED IN SNOWFLAKE **
--         FORCE INDEX(MyIndex)
                             ;
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
