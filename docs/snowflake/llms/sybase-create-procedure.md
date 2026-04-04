# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/sybase/sybase-create-procedure.md

# SnowConvert AI - Sybase IQ - CREATE PROCEDURE

## Description

Creates a stored procedure that encapsulates one or more SQL statements and optional control-flow logic.
SnowConvert AI translates Sybase IQ procedures to Snowflake stored procedures, mapping parameters and data types to Snowflake equivalents.

> **Note:**
>
> Sybase IQ procedures supports Transact-SQL as language. For Transact-SQL to Snowflake guidance, see the SQL Server/Azure Synapse translation reference: [CREATE PROCEDURE](../transact/transact-create-procedure.md).
> This section documents statement translation specific to Sybase IQ.

## Grammar Syntax

```sql
CREATE [ OR REPLACE | TEMPORARY ] PROCEDURE [ owner.]procedure-name
    ( [ parameter-list ] )
    [ AS ]
    compound-statement

parameter-list ::= parameter { , parameter }*

parameter ::= [ IN | OUT | INOUT ] parameter-name datatype

compound-statement ::= BEGIN
    statement-list
END
```

## Sample Source Patterns

### Input Code

#### Sybase

```sql
CREATE PROCEDURE dbo.usp_update_sales
    (p_id INT, p_amount DECIMAL(10,2))
AS
    UPDATE sales
    SET amount = p_amount
    WHERE id = p_id;
```

### Output Code

#### Snowflake

```sql
CREATE OR REPLACE PROCEDURE dbo.usp_update_sales (p_id INT, p_amount DECIMAL(10, 2))
RETURNS VARCHAR
LANGUAGE SQL
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "sybase",  "convertedOn": "02/02/2026",  "domain": "no-domain-provided",  "migrationid": "8x+cAQEkgXqRnjrS+t0q4A==" }}'
EXECUTE AS CALLER
AS
$$
  BEGIN
    UPDATE sales
    SET
        amount = p_amount
    WHERE
        id = p_id;
  END;
$$;
```

## Notes

* Parameter and return data types are translated to their Snowflake equivalents.
* SnowConvert AI may adjust procedure bodies to conform to Snowflake Scripting requirements.
