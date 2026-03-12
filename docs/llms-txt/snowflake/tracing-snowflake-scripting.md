# Source: https://docs.snowflake.com/en/developer-guide/logging-tracing/tracing-snowflake-scripting.md

# Emitting trace events in Snowflake Scripting

You can use the Snowflake `SYSTEM` functions to emit trace events from a stored procedure handler written in Snowflake Scripting.

Before emitting trace events, be sure you have the trace level set so that the data you want are stored in the event table. For more
information, see [Setting levels for logging, metrics, and tracing](telemetry-levels.md).

> **Note:**
>
> Before you can begin emitting trace events, you must set up an event table. For more information, see
> [Event table overview](event-table-setting-up.md).

You can access stored trace event data by executing a SELECT command on the event table. For more information, see
[Viewing trace data](tracing-accessing-events.md).

For general information about setting up logging and retrieving messages in Snowflake, see
[Trace events for functions and procedures](tracing.md).

> **Note:**
>
> For guidelines to keep in mind when adding trace events, see [General guidelines for adding trace events](tracing.md).

## Adding trace events

You can add trace events by calling the [SYSTEM$ADD_EVENT](../../sql-reference/functions/system_add_event.md) function,
passing a name for the event. You can also optionally associate attributes (key-value pairs) with an event.

Code in the following example adds two events, `SProcEmptyEvent` and `SProcEventWithAttributes`. With
`SProcEventWithAttributes`, the code also adds two attributes: `key1` and `key2`.

```sqlexample
SYSTEM$ADD_EVENT('SProcEmptyEvent');
SYSTEM$ADD_EVENT('SProcEventWithAttributes', {'key1': 'value1', 'key2': 'value2'});
```

Adding these events results in two rows in the event table, each with a different value in the RECORD column:

```json
{
  "name": "SProcEmptyEvent"
}
```

```json
{
  "name": "SProcEventWithAttributes"
}
```

The `SProcEventWithAttributes` event row includes the following attributes in the row’s RECORD_ATTRIBUTES column:

```json
{
  "key1": "value1",
  "key2": "value2"
}
```

## Adding span attributes

You can set attributes (key-value pairs) associated with spans by calling the
[SYSTEM$SET_SPAN_ATTRIBUTES](../../sql-reference/functions/system_set_span_attributes.md) function.

For details on spans, see [How Snowflake represents trace events](tracing-how-events-work.md).

The SYSTEM$SET_SPAN_ATTRIBUTES function is available in the following form:

```sqlsyntax
SYSTEM$SET_SPAN_ATTRIBUTES(<object>);
```

where

> * `object` is a Snowflake Scripting object with key-value pairs that specify the attributes for this trace event.

Code in the following example creates two attributes and sets their values:

```sqlexample
SYSTEM$SET_SPAN_ATTRIBUTES('{'attr1':'value1', 'attr2':true}');
```

Setting these attributes results in the following in the event table’s RECORD_ATTRIBUTES column:

```json
{
  "attr1": "value1",
  "attr2": "value2"
}
```

## Examples

Code in the following example uses the SYSTEM$ADD_EVENT function to add an event named `name_a` and an event named `name_b`.
With `name_b`, it associates two attributes, `score` and `pass`. The code also uses SYSTEM$SET_SPAN_ATTRIBUTES to
set two attributes for the span, `key1` and `key2`.

```sqlexample
CREATE OR REPLACE PROCEDURE pi_proc()
  RETURNS DOUBLE
  LANGUAGE SQL
  AS $$
  BEGIN
    -- Add an event without attributes
    SYSTEM$ADD_EVENT('name_a');

    -- Add an event with attributes
    LET attr := {'score': 89, 'pass': TRUE};
    SYSTEM$ADD_EVENT('name_b', attr);

    -- Set attributes for the span
    SYSTEM$SET_SPAN_ATTRIBUTES({'key1': 'value1', 'key2': TRUE});

    RETURN 3.14;
  END;
  $$;
```

```sqlexample
CALL pi_proc();
```

## Automatically emit trace events for child jobs and exceptions

You can automatically emit the following additional types of trace events for a Snowflake Scripting stored procedure
in the event table:

* Exception catching.
* Information about child job execution.
* Child job statistics.
* Stored procedure statistics, including execution time and input values.

Automatic trace emission is intended for the following use cases:

* You want to emit predefined trace events without modifying the body of the stored procedure.
* You want to collect information about stored procedure execution that you can analyze later,
  including:

  * Information about child job execution (such as `childJobUUID`, `rowCount`, `exceptionCode`, and so on).
  * Child job execution time.
  * Input argument values.
* You want more visibility into stored procedure execution to make it easier to develop and debug it without
  manually adding tracing code in the procedure.

To automatically emit these additional trace events for a stored procedure, set the [AUTO_EVENT_LOGGING](../../sql-reference/parameters.md) parameter
to `TRACING` or `ALL` using the [ALTER PROCEDURE](../../sql-reference/sql/alter-procedure.md) command. When you set
this parameter to `ALL`, additional [log messages](logging-snowflake-scripting.md) are also generated automatically
for the stored procedure.

> **Important:**
>
> The additional information is added to the event table only if the effective [TRACE_LEVEL](../../sql-reference/parameters.md) is set
> to `ALWAYS` or `ON_EVENT`. For more information, see [Setting levels for logging, metrics, and tracing](telemetry-levels.md).

For example, create a simple table and insert data:

```sqlexample
CREATE OR REPLACE TABLE test_auto_event_logging (id INTEGER, num NUMBER(12, 2));

INSERT INTO test_auto_event_logging (id, num) VALUES
  (1, 11.11),
  (2, 22.22);
```

Next, create a stored procedure named `auto_event_logging_sp`. This sample stored procedure updates a table row and
then queries the table:

```sqlexample
CREATE OR REPLACE PROCEDURE auto_event_logging_sp(
  table_name VARCHAR,
  id_val INTEGER,
  num_val NUMBER(12, 2))
RETURNS TABLE()
LANGUAGE SQL
AS
$$
BEGIN
  UPDATE IDENTIFIER(:table_name)
    SET num = :num_val
    WHERE id = :id_val;
  LET res RESULTSET := (SELECT * FROM IDENTIFIER(:table_name) ORDER BY id);
  RETURN TABLE(res);
EXCEPTION
  WHEN statement_error THEN
    res := (SELECT :sqlcode sql_code, :sqlerrm error_message, :sqlstate sql_state);
    RETURN TABLE(res);
END;
$$
;
```

The following examples set the AUTO_EVENT_LOGGING parameter for the stored procedure:

```sqlexample
ALTER PROCEDURE auto_event_logging_sp(VARCHAR, INTEGER, NUMBER)
  SET AUTO_EVENT_LOGGING = 'TRACING';
```

```sqlexample
ALTER PROCEDURE auto_event_logging_sp(VARCHAR, INTEGER, NUMBER)
  SET AUTO_EVENT_LOGGING = 'ALL';
```

Call the stored procedure:

```sqlexample
CALL auto_event_logging_sp('test_auto_event_logging', 2, 44.44);
```

```output
+----+-------+
| ID |   NUM |
|----+-------|
|  1 | 11.11 |
|  2 | 44.44 |
+----+-------+
```

Query the event table for trace data recorded by the stored procedure named `auto_event_logging_sp`.
For each trace event, print out the timestamp, name, and attributes of the event.

```sqlexample
SELECT
    TIMESTAMP as time,
    RECORD['name'] as event_name,
    RECORD_ATTRIBUTES as attributes,
  FROM
    my_db.public.my_events
  WHERE
    RESOURCE_ATTRIBUTES['snow.executable.name'] LIKE '%AUTO_EVENT_LOGGING_SP%'
    AND RECORD_TYPE LIKE 'SPAN%';
```

```output
+-------------------------+--------------------------+-----------------------------------------------------------------------------------------------+
| TIME                    | EVENT_NAME               | ATTRIBUTES                                                                                    |
|-------------------------+--------------------------+-----------------------------------------------------------------------------------------------|
| 2024-10-25 20:48:49.844 | "snow.auto_instrumented" | {                                                                                             |
|                         |                          |   "childJobTime": 474,                                                                        |
|                         |                          |   "executionTime": 2,                                                                         |
|                         |                          |   "inputArgumentValues": "{ ID_VAL: 2, TABLE_NAME: test_auto_event_logging, NUM_VAL: 44.44 }" |
|                         |                          | }                                                                                             |
| 2024-10-25 20:48:49.740 | "child_job"              | {                                                                                             |
|                         |                          |   "childJobUUID": "01b7ef00-0003-01d1-0000-a99501233092",                                     |
|                         |                          |   "rowCount": 1,                                                                              |
|                         |                          |   "rowsAffected": 1                                                                           |
|                         |                          | }                                                                                             |
| 2024-10-25 20:48:49.843 | "child_job"              | {                                                                                             |
|                         |                          |   "childJobUUID": "01b7ef00-0003-01d1-0000-a99501233096",                                     |
|                         |                          |   "rowCount": 2,                                                                              |
|                         |                          |   "rowsAffected": 0                                                                           |
|                         |                          | }                                                                                             |
+-------------------------+--------------------------+-----------------------------------------------------------------------------------------------+
```

Now, call the stored procedure, but specify a table that doesn’t exist to cause an exception:

```sqlexample
CALL auto_event_logging_sp('no_table', 2, 82.44);
```

```output
+----------+-----------------------------------------------------+-----------+
| SQL_CODE | ERROR_MESSAGE                                       | SQL_STATE |
|----------+-----------------------------------------------------+-----------|
|     2003 | SQL compilation error:                              | 42S02     |
|          | Object 'NO_TABLE' does not exist or not authorized. |           |
+----------+-----------------------------------------------------+-----------+
```

Run the query on the event table again to see the information about the exception:

```sqlexample
SELECT
    TIMESTAMP as time,
    RECORD['name'] as event_name,
    RECORD_ATTRIBUTES as attributes,
  FROM
    my_db.public.my_events
  WHERE
    RESOURCE_ATTRIBUTES['snow.executable.name'] LIKE '%AUTO_EVENT_LOGGING_SP%'
    AND RECORD_TYPE LIKE 'SPAN%';
```

```output
+-------------------------+--------------------------+-----------------------------------------------------------------------------------------------------+
| TIME                    | EVENT_NAME               | ATTRIBUTES                                                                                          |
|-------------------------+--------------------------+-----------------------------------------------------------------------------------------------------|
| 2024-10-25 20:52:43.633 | "snow.auto_instrumented" | {                                                                                                   |
|                         |                          |   "childJobTime": 66,                                                                               |
|                         |                          |   "executionTime": 4,                                                                               |
|                         |                          |   "inputArgumentValues": "{ ID_VAL: 2, TABLE_NAME: no_table, NUM_VAL: 82.44 }"                      |
|                         |                          | }                                                                                                   |
| 2024-10-25 20:52:43.601 | "caught_exception"       | {                                                                                                   |
|                         |                          |   "exceptionCode": 2003,                                                                            |
|                         |                          |   "exceptionMessage": "SQL compilation error:\nObject 'NO_TABLE' does not exist or not authorized." |
|                         |                          | }                                                                                                   |
+-------------------------+--------------------------+-----------------------------------------------------------------------------------------------------+
```
