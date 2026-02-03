# Source: https://docs.oxla.com/sql-reference/sql-statements/show-tables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SHOW TABLES

## Overview

The `SHOW TABLES` statement allows you to obtain information about existing tables.

<Info>It only shows tables in schemas, on which a user has the `USAGE` grant</Info>

## Example

So as to list all available tables, you need to execute the following query:

```sql  theme={null}
SHOW TABLES;
```

This will produce an output with a list of all existing tables, an example of which is presented below:

```sql  theme={null}
+------------+
| name       |  
+------------+
| lineorder  |
| part       | 
| customer   | 
| supplier   | 
+------------+
```
