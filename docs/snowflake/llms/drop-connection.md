# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-connection.md

# DROP CONNECTION

Removes a connection from the account.

See also:
:   [CREATE CONNECTION](create-connection.md) , [ALTER CONNECTION](alter-connection.md) , [SHOW CONNECTIONS](show-connections.md)

## Syntax

```sqlsyntax
DROP CONNECTION [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the connection to drop.

## Usage notes

* Only account administrators (users with the ACCOUNTADMIN role) can execute this SQL command.
* A primary connection can’t be dropped if it has one or more secondary connections. To drop the primary connection, first promote a secondary
  connection to serve as the primary connection, and then drop the former primary connection. Alternatively, drop all of the secondary connections,
  and then drop the primary connection.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

Drop a connection:

> ```sqlexample
> SHOW CONNECTIONS LIKE 't2%';
>
>
> DROP CONNECTION t2;
>
>
> SHOW CONNECTIONS LIKE 't2%';
> ```

Drop the connection again, but don’t raise an error if the connection doesn’t exist:

> ```sqlexample
> DROP CONNECTION IF EXISTS t2;
> ```
