# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/current-database.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# current_database()

## Overview

The <a href="https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-SESSION" target="_blank">current\_database()</a> is a session information function that returns the current database's name.

## Syntax

The syntax for`current_database()` function is as follows:

```sql  theme={null}
SELECT current_database();
```

## Example

In the following example, we will obtain the database name to which we are currently connected:

```sql  theme={null}
SELECT current_database();
```

By executing the query above, we will get the following output:

```sql  theme={null}
+------------+
| f          |
+------------+
| Oxla       |
+------------+
```
