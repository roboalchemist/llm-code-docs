# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/pg-get-indexdef.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_get_indexdef()

## Overview

The <a href="https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-CATALOG" target="_blank">pg\_get\_indexdef()</a> is a system catalog information function that reconstructs the PostgreSQL command used to retrieve the definition of a specified index.

## Syntax

Here are the two available syntax versions of the `pg_get_indexdef()` function:

<CodeGroup>
  ```sql Version 1 theme={null}
  pg_get_indexdef(index_oid, column_oid)
  ```

  ```sql Version 2 theme={null}
  pg_get_indexdef(index_oid, column_oid, pretty_bool)
  ```
</CodeGroup>

## Parameters

The following parameters are required to execute this function:

* `index_oid`: specifies the object identifier (OID) of the index
* `column_oid`: indicates the column number within the index (starting from 1)
* `pretty_bool`: controls whether to format the output in a human-readable way

## Example

In this example we'll start from creating a sample table and an index for it

```sql  theme={null}
CREATE TABLE sample_table(col int);
CREATE INDEX sample_index ON sample_table(col);
```

Once that is done, we can get the OID of the index in a following way

```sql  theme={null}
SELECT oid FROM pg_class WHERE relname = 'sample_index';
```

```sql  theme={null}
 oid
------
 16387
```

As the last step we're going to retrieve the index definition

```sql  theme={null}
SELECT pg_get_indexdef(16387);
```

Here is the reconstructed definition:

```sql  theme={null}
                    pg_get_indexdef
-------------------------------------------------------
 CREATE INDEX sample_index ON public.sample_table(col)
(1 row)
```
