# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-pipe.md

# DROP PIPE

Removes the specified pipe from the current/specified schema.

See also:
:   [CREATE PIPE](create-pipe.md) , [ALTER PIPE](alter-pipe.md) , [SHOW PIPES](show-pipes.md) , [DESCRIBE PIPE](desc-pipe.md)

## Syntax

```sqlsyntax
DROP PIPE [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the pipe to drop. If the identifier contains spaces or special characters, the entire string must
    be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Usage notes

* Dropped pipes can’t be recovered; they must be recreated.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

> ```sqlexample
> DROP PIPE mypipe;
>
> +------------------------------+
> | status                       |
> |------------------------------|
> | MYPIPE successfully dropped. |
> +------------------------------+
> ```
