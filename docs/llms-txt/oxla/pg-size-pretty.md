# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/pg-size-pretty.md

# pg_size_pretty()

## Overview

The <a href="https://www.postgresql.org/docs/9.4/functions-admin.html" target="_blank">pg\_size\_pretty()</a> is a database object management function that converts sizes in bytes into a human-readable format.

## Syntax

The syntax for the `pg_size_pretty()` function is as follows:

```sql  theme={null}
pg_size_pretty(size)
```

## Parameters

The following parameters are required to execute this function:

* `size`: specifies the size in bytes that you want to convert

## Examples

```sql  theme={null}
SELECT pg_size_pretty(100);
 pg_size_pretty
----------------
 100 bytes
(1 row)
```

```sql  theme={null}
SELECT pg_size_pretty(1000000);
 pg_size_pretty
----------------
 977 kB
(1 row)
```
