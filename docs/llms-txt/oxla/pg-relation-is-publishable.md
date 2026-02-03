# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/pg-relation-is-publishable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_relation_is_publishable()

## Overview

The`pg_relation_is_publishable()` function is used to determine whether a specified relation (table) can be published in a
<a href="https://www.postgresql.org/docs/current/logical-replication-publication.html" target="_blank">publication</a>.

## Syntax

The syntax for the `pg_relation_is_publishable()` function is as follows:

<pre><code>pg\_relation\_is\_publishable(table\_name\_or\_oid)</code></pre>

The function returns `false` for every existing table and `NULL` for any non-existing table.

## Parameters

The following parameters are required to execute this function:

* `table_name_or_oid`: specifies the object identifier (OID) of a table or it's name

## Examples

```sql  theme={null}
SELECT pg_relation_is_publishable('existing_table');
 pg_relation_is_publishable
----------------------------
 f
```

```sql  theme={null}
SELECT pg_relation_is_publishable(16386);
 pg_relation_is_publishable
----------------------------
 f
```
