# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/conversion-issues/hiveEWI.md

# SnowConvert AI - Hive Issues

> **Note:**
>
> **Conversion Scope**
>
> SnowConvert AI for Hive focuses its assessment and translation capabilities primarily on TABLES and VIEWS.
> While SnowConvert AI can recognize other types of ANSI-standard statements, these are not yet fully supported for conversion. This means that while the tool may identify them, it won’t perform a complete translation for these unsupported code units.

This page provides a comprehensive reference for how SnowConvert AI translates Hive grammar elements to Snowflake equivalents. In this translation reference, you will find code examples, functional equivalence results, key differences, recommendations, known issues, and descriptions of each transformation.

## SSC-EWI-HV0001

The ROW FORMAT clause is not supported in Snowflake

### Severity

Medium

#### Description

This EWI is added when a ROW FORMAT statement is encountered.

#### Code Example

**Input Code:**

##### Hive

```sql
 CREATE TABLE parquet_table (
id INT, data STRING
)
 ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ESCAPED BY '\\' COLLECTION ITEMS TERMINATED BY ';' MAP KEYS TERMINATED BY ':' LINES TERMINATED BY '\n' NULL DEFINED AS 'NULL_VALUE';
```

**Generated Code:**

##### Snowflake

```sql
 CREATE TABLE parquet_table (
 id INT,
 data STRING
)
!!!RESOLVE EWI!!! /*** SSC-EWI-HV0001 - THE ROW FORMAT CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',' ESCAPED BY '\\'
COLLECTION ITEMS TERMINATED BY ';'
MAP KEYS TERMINATED BY ':'
LINES TERMINATED BY '\n'
NULL DEFINED AS 'NULL_VALUE'
;
```
