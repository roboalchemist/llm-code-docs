# Source: https://docs.oxla.com/system-catalogs/catalogs/pg_index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_index

## Overview

The `pg_index` stores information about indexes on tables. It mimics the [pg\_index](https://www.postgresql.org/docs/current/catalog-pg-index.html) PostgreSQL system catalog.

## Columns

<Note>This table is designed for compatibility with tools that require PostgreSQL system tables, so it mostly has dummy data. Please note that not all columns in `pg_index` are applicable to every type of relation.</Note>

The following columns are available for querying in `pg_index`:

| Column                | Type   | Description                                                                       |
| --------------------- | ------ | --------------------------------------------------------------------------------- |
| `indexrelid`          | `int`  | This column represents OID of the index                                           |
| `indrelid`            | `int`  | This column represents OID (Object ID) of the table on which the index is defined |
| `indnatts`            | `int`  | This column represents number of columns in the index                             |
| `indnkeyatts`         | `int`  | This column represents number of key columns in the index                         |
| `indisunique`         | `bool` | The default value is `false`                                                      |
| `indnullsnotdistinct` | `bool` | *unused*                                                                          |
| `indisprimary`        | `bool` | *unused*                                                                          |
| `indisexclusion`      | `bool` | *unused*                                                                          |
| `indimmediate`        | `bool` | *unused*                                                                          |
| `indisclustered`      | `bool` | *unused*                                                                          |
| `indisvalid`          | `bool` | *unused*                                                                          |
| `indcheckxmin`        | `bool` | *unused*                                                                          |
| `indisready`          | `bool` | *unused*                                                                          |
| `indislive`           | `bool` | *unused*                                                                          |
| `indisreplident`      | `bool` | *unused*                                                                          |
| `indkey`              | `int`  | *unused*                                                                          |
| `indcollation`        | `int`  | *unused*                                                                          |
| `indclass`            | `int`  | *unused*                                                                          |
| `indoption`           | `int`  | *unused*                                                                          |
| `indexprs`            | `int`  | *unused*                                                                          |
| `indpred`             | `int`  | *unused*                                                                          |
