# Source: https://docs.snowflake.com/en/sql-reference/functions/system_abort_session.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$ABORT_SESSION

Aborts the specified session.

## Syntax

```sqlsyntax
SYSTEM$ABORT_SESSION( <session_id> )
```

## Arguments

`session_id`
:   Identifier for the session to abort. To obtain the ID for a session, log into the web interface as an account administrator (user with the ACCOUNTADMIN role) and go to:

    > Account  » Sessions

## Examples

```sqlexample
SELECT SYSTEM$ABORT_SESSION(1065153868222);

+-------------------------------------+
| SYSTEM$ABORT_SESSION(1065153868222) |
|-------------------------------------|
| session [1065153868222] terminated. |
+-------------------------------------+
```
