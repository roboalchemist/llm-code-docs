# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/pg-table-size.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_table_size()

## Overview

The <a href="https://www.postgresql.org/docs/9.1/functions-admin.html" target="_blank">pg\_table\_size()</a> is a system administration function that retrieves the size of a specific table, including its associated storage components but excluding indexes.

## Syntax

The syntax for the `pg_table_size()` function is as follows:

```sql  theme={null}
pg_table_size(regclass)
```

## Parameters

The following parameters are required to execute this function:

* `regclass`: name or object identifier (OID) of the table whose size is to be retrieved
