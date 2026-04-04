# Source: https://docs.oxla.com/sql-reference/sql-functions/timestamp-functions/current-timestamp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CURRENT_TIMESTAMP

## Overview

The `CURRENT_TIMESTAMP()` returns the current timestamp value representing the date and time the query was executed.

<Info>Note that the time returned by this function is the time when the query was executed.</Info>

## Syntax

```sql  theme={null}
CURRENT_TIMESTAMP() // The parentheses are optional
```

## Examples

The following example shows how to get the current date and time with a `CURRENT_TIMESTAMP()`function:

```sql  theme={null}
SELECT CURRENT_TIMESTAMP AS "Current Time";
```

The final result will display the current date and time in your timezone:

```sql  theme={null}
-----------------------------
 Current Time                
-----------------------------
 2022-08-31 16:56:06.464016  
-----------------------------
```
