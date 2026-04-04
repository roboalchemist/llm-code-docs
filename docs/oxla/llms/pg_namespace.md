# Source: https://docs.oxla.com/system-catalogs/catalogs/pg_namespace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_namespace

## Overview

The `pg_namespace` contains information about schema definitions. It mimics the [pg\_namespace](https://www.postgresql.org/docs/current/catalog-pg-namespace.html) PostgreSQL system catalog.

<Note>To learn more about Schema and how it is managed in Oxla, please refer to the [schema documentation](/sql-reference/schema).</Note>

## Columns

<Note>This table is designed for compatibility with tools that require PostgreSQL system tables, so it mostly has dummy data. Please note that not all columns in `pg_namespace` are applicable to every type of relation.</Note>

The `pg_namespace` catalog has the following key columns:

| Column     | Type   | Description                                                                          |
| ---------- | ------ | ------------------------------------------------------------------------------------ |
| `oid`      | `int`  | This column represents the Object ID, a unique identifier assigned to each namespace |
| `nspname`  | `text` | This column represents the name of the namespace                                     |
| `nspowner` | `int`  | This column represents the owner of the namespace                                    |
| `nspacl`   | `text` | *unused*                                                                             |

## Example

### 1. Create a Schema

In this example, we create "sales" and "hr" schemas using the query below:

```sql  theme={null}
CREATE SCHEMA sales;
CREATE SCHEMA hr;
```

The successful result would look like this:

```sql  theme={null}
COMPLETE
COMPLETE
```

### 2. View Schema Definitions

We then use a `SELECT` statement on the `pg_namespace` catalog to show the schema definitions.

```sql  theme={null}
SELECT nspname AS schema_name, oid AS schema_oid
FROM pg_namespace;
```

The result shows the list of schemas and its ID, as shown below:

```sql  theme={null}
 schema_name | schema_oid 
-------------+------------
 public      |          0
 sales       |          3
 hr          |          4
```
