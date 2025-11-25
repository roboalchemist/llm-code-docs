# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/pg-get-expr.md

# pg_get_expr()

## Overview

The <a href="https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-CATALOG" target="_blank">pg\_get\_expr()</a> is a system catalog information function that retrieves the internal form of an individual expression, such as the default value for a column.

## Syntax

There are two available syntax versions of the `pg_get_expr()` function:

<CodeGroup>
  ```sql Version 1 theme={null}
  SELECT pg_get_expr('expr_text', relation_oid);
  ```

  ```sql Version 2 theme={null}
  SELECT pg_get_expr('expr_text', relation_oid, pretty_bool);
  ```
</CodeGroup>

Both versions of the `pg_get_expr()` function return an empty string `""`.

## Parameters

The following parameters are required to execute this function:

* `expr_text`: expression for which you want to obtain the internal representation (can be any string value)
* `relation_oid`: OID (Object Identifier) of the table the expression belongs to (integer type)
* `pretty_bool`: boolean value determining whether to format the expression in a more human-readable format (`TRUE`) or not (`FALSE`)

## Example

For the needs of this section, first we will create a sample table named **employees**

```sql  theme={null}
CREATE TABLE employees (
    id INT,
    name TEXT,
    salary TEXT
);
```

Then we will get the OID of the table

```sql  theme={null}
SELECT oid FROM pg_class WHERE relname = 'employees';
```

```sql  theme={null}
 oid  
------
 1018
```

As the last step, we will retrieve the internal form for the `salary` column using `pg_get_expr()` function

```sql  theme={null}
-- Version 1
SELECT pg_get_expr('salary', 1018);

-- Version 2
SELECT pg_get_expr('salary', 1018, TRUE);
```

By executing any of the queries above, we will get the following output:

```sql  theme={null}
 pg_get_expr 
-------------

```
