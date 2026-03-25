# Source: https://docs.snowflake.com/en/sql-reference/functions/system_add_event.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$ADD_EVENT (for Snowflake Scripting)

Add an event for trace.

Use SYSTEM$ADD_EVENT to add an event when using trace events from a handler written in Snowflake Scripting.

For more information, refer to [Emitting trace events in Snowflake Scripting](../../developer-guide/logging-tracing/tracing-snowflake-scripting.md).

## Syntax

```sqlsyntax
SYSTEM$ADD_EVENT('<name>', '<object>');
```

## Arguments

`'name'`
:   The name of the event to add.

`'object'`
:   An object containing name-value pairs representing the attributes to add.

## Examples

Code in the following example uses the SYSTEM$ADD_EVENT function to add an event named `name_a` and an event named `name_b`.
With `name_b`, it associates two attributes, `score` and `pass`. The code also sets two attributes for the span,
`key1` and `key2`.

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
