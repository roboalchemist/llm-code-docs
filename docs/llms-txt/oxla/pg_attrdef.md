# Source: https://docs.oxla.com/system-catalogs/catalogs/pg_attrdef.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_attrdef

## Overview

The `pg_attrdef` stores information about column default values. It mimics the [pg\_attrdef](https://www.postgresql.org/docs/current/catalog-pg-attrdef.html) PostgreSQL system catalog.

<Warning>Please note that Oxla doesn’t support the custom types</Warning>

## Columns

<Note>This table is designed for compatibility with tools that require PostgreSQL system tables, so it mostly has dummy data. Please note that not all columns in `pg_attrdef` are applicable to every type of relation.</Note>

The following columns are available for querying in `pg_attrdef`:

| Column    | Type   | Description                                                      |
| --------- | ------ | ---------------------------------------------------------------- |
| `oid`     | `int`  | This column represents the row identifier                        |
| `adrelid` | `int`  | This column represents the table to which this column belongs    |
| `adnum`   | `int`  | This column represents the number of the column within the table |
| `adbin`   | `text` | This column represents the default value for the column          |
