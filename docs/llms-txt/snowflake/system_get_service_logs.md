# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_service_logs.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GET_SERVICE_LOGS

Retrieves local logs from a
[Snowpark Container Services service](../../developer-guide/snowpark-container-services/working-with-services.md) container.

See also:
:   [Publishing and accessing container logs](../../developer-guide/snowpark-container-services/monitoring-services.md)

## Syntax

```sqlsyntax
SYSTEM$GET_SERVICE_LOGS( <service_name>, <instance_id>, <container_name>
   [, <number_of_most_recent_lines> ] [, <retrieve_previous_logs> ])
```

## Arguments

**Required:**

`service_name`
:   Service name.

`instance_id`
:   ID of the service instance, starting with 0.

`container_name`
:   Container name as specified in the service specification file.

**Optional:**

`number_of_most_recent_lines`
:   Number of trailing log lines to retrieve.

    Default: Up to 100 KB of the most recent log lines.

`retrieve_previous_logs`
:   If TRUE, the function retrieves logs from a previously terminated container. You can specify this parameter only if the container has been restarted at least once.

    Default: false (retrieve logs from the currently running container).

## Returns

Returns a string consisting of newline-separated log entries from the specified service container.

## Usage notes

* The current role must have the MONITOR privilege on the service to access the container logs.
* The function returns a container log as a string. You can use the [SPLIT_TO_TABLE](split_to_table.md) function to
  convert the string into a table containing one row for each newline-separated entry.

## Examples

### Retrieving logs from the current container

The following statement retrieves the last 10 log lines from the instance 0 of the “echo_service” service that is running in
the “echo” container:

```sqlexample
SELECT SYSTEM$GET_SERVICE_LOGS('TUTORIAL_DB.data_schema.echo_service', 0, 'echo', 10);
```

You can also follow [Tutorial 1: Create a Snowpark Container Services Service](../../developer-guide/snowpark-container-services/tutorials/tutorial-1.md) to start a service and execute the
preceding command to get the service log from a container.

The function returns a string consisting of newline-separated log entries. You can convert this string into a table using the
[SPLIT_TO_TABLE](split_to_table.md) function and the TABLE() keyword (see [Table functions](../functions-table.md)).

```sqlexample
SELECT value AS log_line
  FROM TABLE(
    SPLIT_TO_TABLE(SYSTEM$GET_SERVICE_LOGS('echo_service', 0, 'echo'), '\n')
  )
```

You can further apply a filter to retrieve only specific log entries. The WHERE clause in the following SELECT statement uses the
[CONTAINS](contains.md) function to retrieve only the log lines containing a specific date string:

```sqlexample
SELECT value AS log_line
  FROM TABLE(
   SPLIT_TO_TABLE(SYSTEM$GET_SERVICE_LOGS('echo_service', '0', 'echo'), '\n')
  )
  WHERE (CONTAINS(log_line, '06/Jun/2023 02:44:'))
  ORDER BY log_line;
```

The following sample output shows three log entry rows retrieved:

```output
+-----------------------------------------------------------------------------------------------------+
| LOG_LINE                                                                                            |
|-----------------------------------------------------------------------------------------------------|
| 10.16.9.193 - - [06/Jun/2023 02:44:04] "GET /healthcheck HTTP/1.1" 200 -                            |
| 10.16.9.193 - - [06/Jun/2023 02:44:09] "GET /healthcheck HTTP/1.1" 200 -                            |
| 10.16.9.193 - - [06/Jun/2023 02:44:14] "GET /healthcheck HTTP/1.1" 200 -                            |
+-----------------------------------------------------------------------------------------------------+
```

### Retrieving logs from a previously terminated container

The following statement retrieves the last 10 log lines from the previously terminated instance of the “echo_service” service that is running in the “echo” container. Here we assume the container restarted at least once:

```sqlexample
SELECT SYSTEM$GET_SERVICE_LOGS('TUTORIAL_DB.data_schema.echo_service', 0, 'echo', 10, true);
```
