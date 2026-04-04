# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/service-commands/unset.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/compute-pool-commands/unset.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/native-apps-commands/release-directive/unset.md

# Source: https://docs.snowflake.com/en/sql-reference/sql/unset.md

# UNSET

Drops a [session variable](../session-variables.md).

See also:
:   [SHOW VARIABLES](show-variables.md) , [SET](set.md)

## Syntax

```sqlsyntax
UNSET <var>

UNSET ( <var> [ , <var> ... ] )
```

## Parameters

`var`
:   Specifies the identifier for the variable to drop.

## Usage notes

* The command supports dropping multiple variables in the same statement.
* The command does not require a running warehouse to execute.

## Examples

```sqlexample
UNSET V1;

UNSET V2;

UNSET (V1, V2);
```
