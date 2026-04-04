# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/conversion-issues/sparkEWI.md

# SnowConvert AI - Spark Issues

> **Note:**
>
> Conversion Scope
>
> SnowConvert AI for Spark SQL focuses its assessment and translation capabilities primarily on TABLES and VIEWS.
> While SnowConvert AI can recognize other types of ANSI-standard statements, these are not yet fully supported for conversion. This means that while the tool may identify them, it won’t perform a complete translation for these unsupported code units.

This page provides a comprehensive reference for how SnowConvert AI translates Spark grammar elements to Snowflake equivalents. In this translation reference, you will find code examples, functional equivalence results, key differences, recommendations, known issues, and descriptions of each transformation.

## SSC-EWI-SPK0001

CREATE TABLE without columns is not supported in Snowflake

### Severity

Medium

#### Description

This EWI is added when a `CREATE TABLE` statement is encountered without column definitions.

#### Code Example

**Input Code:**

##### Spark

```sql
 CREATE TABLE table_name1;
```

**Output Code:**

##### Snowflake

```sql
 !!!RESOLVE EWI!!! /*** SSC-EWI-SPK0001 - CREATE TABLE WITHOUT COLUMNS IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
CREATE TABLE table_name1;
```
