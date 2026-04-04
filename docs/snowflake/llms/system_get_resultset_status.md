# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_resultset_status.md

Categories:
:   [System functions](../functions-system.md) (Query Information)

# SYSTEM$GET_RESULTSET_STATUS

Returns the status of a [RESULTSET](../../developer-guide/snowflake-scripting/resultsets.md) in a Snowflake Scripting
stored procedure.

This function can be useful for getting the status an
[asynchronous child job](../../developer-guide/snowflake-scripting/asynchronous-child-jobs.md)
that is running for a RESULTSET.

## Syntax

```sqlsyntax
SYSTEM$GET_RESULTSET_STATUS( <resultset_name> )
```

## Arguments

`resultset_name`
:   The name of the RESULTSET.

## Returns

This function returns the status of the RESULTSET in a value of type VARCHAR.
The following status values are possible:

| Status | Description |
| --- | --- |
| RUNNING | The query is still running. |
| SUCCESS | The query finished successfully. |
| ABORTING | The query is in the process of being aborted on the server side. |
| FAILED_WITH_ERROR | The query finished unsuccessfully due to an error in the query. |
| FAILED_WITH_INCIDENT | The query finished unsuccessfully due to an incident on the server side. |
| ABORTED | The query was aborted on the server side. |
| QUEUED | The query is queued for execution (that is, hasn’t yet started running), typically because it is waiting for resources. |
| DISCONNECTED | The session’s connection is broken. The query’s state will change to FAILED_WITH_ERROR soon. |
| RESUMING_WAREHOUSE | The warehouse is starting up, and the query isn’t yet running. |
| QUEUED_REPAIRING_WAREHOUSE | The warehouse is being repaired, and the query is queued for execution. |
| RESTARTED | The query restarted. |
| BLOCKED | The query is waiting on a lock held by another statement. |

## Usage notes

This function can only be called in a [Snowflake Scripting block](../../developer-guide/snowflake-scripting/blocks.md).

## Examples

The following example calls SYSTEM$GET_RESULTSET_STATUS twice to return the status of an asynchronous
child job that is running for a RESULTSET. The example calls the function while the asynchronous child job is
running and after it completes.

```sqlexample
EXECUTE IMMEDIATE $$
DECLARE
  status2 VARCHAR DEFAULT 'invalid';
BEGIN
  LET res RESULTSET := ASYNC (SELECT SYSTEM$WAIT(3));
  LET status VARCHAR := SYSTEM$GET_RESULTSET_STATUS(res);

  AWAIT res;
  status2 := SYSTEM$GET_RESULTSET_STATUS(res);
  RETURN [status, status2];
END;
$$;
```

```output
+------------------+
| GET_QUERY_STATUS |
+------------------+
| [                |
|   "RUNNING",     |
|   "SUCCESS"      |
| ]                |
+------------------+
```
