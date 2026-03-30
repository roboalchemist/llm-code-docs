# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/postgres/ddls/create-table/netezza-create-table.md

# SnowConvert AI - Netezza - CREATE TABLE

Translation from Netezza to Snowflake

## Description

Creates a new table in Netezza. For more information, please refer to [`CREATE TABLE`](https://www.ibm.com/docs/en/netezza?topic=npsscr-create-table) documentation.

> **Warning:**
>
> This grammar is partially supported in Snowflake. Translation pending for these table options:
>
> ```sql
> [ ORGANIZE ON { (<col>) | NONE } ]
> [ ROW SECURITY ]
> [ DATA_VERSION_RETENTION_TIME <number-of-days> ]
> ```

## Grammar Syntax

```sql
CREATE [ TEMPORARY | TEMP ] TABLE [IF NOT EXISTS] <table>
( <col> <type> [<col_constraint>][,<col> <type> [<col_constraint>]…]
<table_constraint> [,<table_constraint>… ] )
[ DISTRIBUTE ON { RANDOM | [HASH] (<col>[,<col>…]) } ]
[ ORGANIZE ON { (<col>) | NONE } ]
[ ROW SECURITY ]
[ DATA_VERSION_RETENTION_TIME <number-of-days> ]
```

## DISTRIBUTE ON RANDOM - DISTRIBUTE ON HASH

> **Note:**
>
> This syntax is not needed in Snowflake.

These clauses controls how table data is physically distributed across the system’s segments. As Snowflake automatically handles data storage, these options will be removed in the migration.

### Grammar Syntax

```sql
DISTRIBUTE ON { RANDOM | [HASH] (<col>[,<col>…]) }
```

### Sample Source Patterns

#### Input Code

##### Greenplum

```sql
CREATE TABLE table1 (colum1 int, colum2 int, colum3 smallint, colum4 int )
DISTRIBUTE ON RANDOM;
```

#### Output Code

##### Snowflake

```sql
CREATE TABLE table1 (colum1 int, colum2 int, colum3 smallint, colum4 int )
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "netezza",  "convertedOn": "05/11/2025",  "domain": "test" }}'
;
```

## Related EWIs

1. [SSC-EWI-0073](../../../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Pending Functional Equivalence Review.
