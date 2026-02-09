# Source: https://docs.oxla.com/system-catalogs/catalogs/pg_constraint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_constraint

## Overview

The `pg_constraint` stores information about table constraints. It mimics the [pg\_constraint](https://www.postgresql.org/docs/current/catalog-pg-constraint.html) PostgreSQL system catalog.

<Warning>Please note that Oxla doesn’t support the custom types</Warning>

## Columns

<Note>This table is designed for compatibility with tools that require PostgreSQL system tables, so it mostly has dummy data. Please note that not all columns in `pg_constraint` are applicable to every type of relation.</Note>

The following columns are available for querying in `pg_constraint`:

| Column           | Type   | Description                                                        |
| ---------------- | ------ | ------------------------------------------------------------------ |
| `oid`            | `int`  | This column represents the row identifier                          |
| `conname`        | `text` | This column represents the constraint name                         |
| `connamespace`   | `int`  | This column represents the namespace that contains this constraint |
| `contype`        | `text` | **unused**                                                         |
| `condeferrable`  | `bool` | **unused**                                                         |
| `condeferred`    | `bool` | **unused**                                                         |
| `convalidated`   | `bool` | **unused**                                                         |
| `conrelid`       | `int`  | **unused**                                                         |
| `contypid`       | `int`  | **unused**                                                         |
| `conindid`       | `int`  | **unused**                                                         |
| `conparentid`    | `int`  | **unused**                                                         |
| `confrelid`      | `int`  | **unused**                                                         |
| `confupdtype`    | `text` | **unused**                                                         |
| `confdeltype`    | `text` | **unused**                                                         |
| `confmatchtype`  | `text` | **unused**                                                         |
| `conislocal`     | `bool` | **unused**                                                         |
| `coninhcount`    | `int`  | **unused**                                                         |
| `connoinherit`   | `bool` | **unused**                                                         |
| `conkey`         | `text` | **unused**                                                         |
| `confkey`        | `text` | **unused**                                                         |
| `conpfeqop`      | `text` | **unused**                                                         |
| `conppeqop`      | `text` | **unused**                                                         |
| `conffeqop`      | `text` | **unused**                                                         |
| `confdelsetcols` | `text` | **unused**                                                         |
| `conexclop`      | `text` | **unused**                                                         |
| `conbin`         | `text` | **unused**                                                         |
