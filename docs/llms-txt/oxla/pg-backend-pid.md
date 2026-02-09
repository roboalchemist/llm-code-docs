# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/pg-backend-pid.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_backend_pid()

## Overview

The <a href="https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-SESSION" target="_blank">pg\_backend\_pid()</a> is a session information function that returns the process ID (PID) of the server process handling the current session. It is useful for identifying the backend process associated with a specific database connection, allowing for monitoring and tasks management.

## Syntax

The syntax for the `pg_backend_pid()` function is as follows:

```sql  theme={null}
pg_backend_pid()
```
