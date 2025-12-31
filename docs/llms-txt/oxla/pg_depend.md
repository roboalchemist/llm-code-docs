# Source: https://docs.oxla.com/system-catalogs/catalogs/pg_depend.md

# pg_depend

## Overview

The `pg_depend` tracks relationships between database objects, such as tables, columns, constraints, and indexes. It mimics the [pg\_depend](https://www.postgresql.org/docs/current/catalog-pg-depend.html) PostgreSQL system catalog.

<Warning>Please note that Oxla doesn’t support the custom types</Warning>

## Columns

<Note>This table is designed for compatibility with tools that require PostgreSQL system tables, so it mostly has dummy data. Please note that not all columns in `pg_depend` are applicable to every type of relation.</Note>

The following columns are available for querying in `pg_depend`:

| Column        | Type   | Description                                                                      |
| ------------- | ------ | -------------------------------------------------------------------------------- |
| `classid`     | `int`  | This column represents the OID of the system catalog the dependent object is in  |
| `objid`       | `int`  | This column represents the OID of the specific dependent object                  |
| `objsubid`    | `int`  | This column represents the column number for a table column                      |
| `refclassid`  | `int`  | This column represents the OID of the system catalog the referenced object is in |
| `refobjid`    | `int`  | This column represents the OID of the specific referenced object                 |
| `refobjsubid` | `int`  | This column represents the column number for a table column                      |
| `deptype`     | `text` | **unused**                                                                       |
