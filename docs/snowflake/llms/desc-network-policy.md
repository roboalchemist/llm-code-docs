# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-network-policy.md

# DESCRIBE NETWORK POLICY

Describes the properties specified for a network policy.

DESCRIBE can be abbreviated to DESC.

See also:
:   [DROP NETWORK POLICY](drop-network-policy.md) , [ALTER NETWORK POLICY](alter-network-policy.md) , [CREATE NETWORK POLICY](create-network-policy.md) , [SHOW NETWORK POLICIES](show-network-policies.md)

## Syntax

```sqlsyntax
DESC[RIBE] NETWORK POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier for the network policy to describe. If the identifier contains spaces or special characters, the
    entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Usage notes

* Only the network policy owner (i.e. role with the OWNERSHIP privilege on the network policy) or higher can execute this command.

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Example

Describe a network policy named `mypolicy`:

> ```sqlexample
> DESC NETWORK POLICY mypolicy;
> ```
>
> ```output
> -----------------+---------------+
>       name       |     value     |
> -----------------+---------------+
>  ALLOWED_IP_LIST | 192.168.0.100 |
>  BLOCKED_IP_LIST | 192.168.0.101 |
> -----------------+---------------+
> ```
