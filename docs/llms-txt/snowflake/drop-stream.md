# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-stream.md

# DROP STREAM

Removes a stream from the current/specified schema.

See also:
:   [CREATE STREAM](create-stream.md) , [ALTER STREAM](alter-stream.md) , [SHOW STREAMS](show-streams.md) , [DESCRIBE STREAM](desc-stream.md)

## Syntax

```sqlsyntax
DROP STREAM [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the stream to drop. If the identifier contains spaces, special characters, or mixed-case characters, the
    entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive
    (e.g. `"My Object"`).

    If the stream identifier is not fully-qualified (in the form of `db_name.schema_name.stream_name` or
    `schema_name.stream_name`), the command looks for the stream in the current schema for the session.

## Usage notes

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

Drop a stream:

> ```sqlexample
> SHOW STREAMS LIKE 't2%';
>
>
> DROP STREAM t2;
>
>
> SHOW STREAMS LIKE 't2%';
> ```

Drop the stream again, but don’t raise an error if the stream does not exist:

> ```sqlexample
> DROP STREAM IF EXISTS t2;
> ```
