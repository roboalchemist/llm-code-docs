# Source: https://docs.oxla.com/system-catalogs/catalogs/pg_description.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_description

## Overview

The `pg_description` stores descriptions (comments) for each database object. It mimics the [pg\_description](https://www.postgresql.org/docs/current/catalog-pg-description.html) PostgreSQL system catalog.

## Columns

<Note>This table is designed for compatibility with tools that require PostgreSQL system tables, so it mostly has dummy data. Please note that not all columns in `pg_description` are applicable to every type of relation.</Note>

The following columns are available for querying in `pg_description`:

| Column        | Type   | Description                                                                                                                              |
| ------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `objoid`      | `int`  | This column represents the OID (Object ID) of the object for which the description is stored                                             |
| `classoid`    | `int`  | This column represents the OID of the table that the object belongs to                                                                   |
| `objsubid`    | `int`  | If an object has multiple parts (for example, columns in a table), `objsubid` specifies the column number. If not used, this is set to 0 |
| `description` | `text` | This column represents the description for the specified object                                                                          |
