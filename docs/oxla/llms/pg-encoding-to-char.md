# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/pg-encoding-to-char.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_encoding_to_char()

## Overview

The <a href="https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-CATALOG" target="_blank">pg\_encoding\_to\_char()</a> is a system catalog information function that converts an encoding internal identifier to a human-readable name.

## Syntax

The syntax for the `pg_encoding_to_char()` function is as follows:

```sql  theme={null}
pg_encoding_to_char(number)
```

## Parameters

The following parameters are required to execute function:

* `number`: specifies the integer value representing the encoding identifier

## Examples

```sql  theme={null}
SELECT pg_encoding_to_char(1);

 pg_encoding_to_char
---------------------
 EUC_JP
(1 row)
```

```sql  theme={null}
SELECT pg_encoding_to_char(0);

 pg_encoding_to_char
---------------------
 SQL_ASCII
(1 row)
```

```sql  theme={null}
SELECT pg_encoding_to_char(-1);

 pg_encoding_to_char
---------------------

(1 row)
```
