# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/pg-table-is-visible.md

# pg_table_is_visible()

## Overview

The <a href="https://www.postgresql.org/docs/9.4/functions-admin.html" target="_blank">pg\_table\_is\_visible()</a> is a schema visibility inquiry function that checks whether a specified table or other database object is visible in the current schema search path.

## Syntax

The syntax for the `pg_table_is_visible()` function is as follows:

<pre><code>pg\_table\_is\_visible(table\_or\_index\_oid)</code></pre>

## Parameters

The following parameters are required to run this function:

* `table_or_index_oid`: specifies the object identifier (OID) of a table or it's name

## Examples

```sql  theme={null}
SELECT pg_table_is_visible(-1);
 pg_table_is_visible
----------------------------

```

```sql  theme={null}
SELECT pg_table_is_visible(16386);
 pg_table_is_visible
----------------------------
 t
```

```sql  theme={null}
SELECT pg_table_is_visible(16381);
 pg_table_is_visible
----------------------------
 f
```
