# Source: https://docs.oxla.com/system-catalogs/catalogs/pg_statio_user_tables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_statio_user_tables

## Overview

The `pg_statio_user_tables` contains one row for each user table in the current database, showing statistics columns filled with zeros.

## Columns

<Note>This table is designed for compatibility with tools that require PostgreSQL system tables, so it mostly has dummy data. Please note that not all columns in `pg_statio_user_tables` are applicable to every type of relation</Note>

The following columns are available for querying in `pg_statio_user_tables` :

| Column            | Type   | Description                                                  |
| ----------------- | ------ | ------------------------------------------------------------ |
| `relid`           | `int`  | This column represents the table ID                          |
| `relname`         | `text` | This column represents the table name                        |
| `schemaname`      | `text` | This column represents the schema name that this table is in |
| `heap_blks_read`  | `int`  | *unused*                                                     |
| `heap_blks_hit`   | `int`  | *unused*                                                     |
| `idx_blks_read`   | `int`  | *unused*                                                     |
| `idx_blks_hit`    | `int`  | *unused*                                                     |
| `toast_blks_read` | `int`  | *unused*                                                     |
| `toast_blks_hit`  | `int`  | *unused*                                                     |
| `tidx_blks_read`  | `int`  | *unused*                                                     |
| `tidx_blks_hit`   | `int`  | *unused*                                                     |

## Example

1. Create a new table:

```sql  theme={null}
CREATE TABLE example_table (
    data text,
    cluster text,
    storage int
);
```

2. Run the query combined with a `WHERE` clause to look up based on the table name (`relname`):

```sql  theme={null}
SELECT relid, schemaname, relname FROM pg_statio_user_tables;
```

3. It will return the table size in bytes:

```sql  theme={null}
 relid | schemaname |  relname    
-------+------------+---------------
 16384 | public     | job          
 16385 | public     | example_table
(2 rows)
```
