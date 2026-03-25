# Source: https://docs.snowflake.com/en/sql-reference/functions/system_disable_database_replication.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$DISABLE_DATABASE_REPLICATION

Disable replication for a primary database and any secondary databases linked to it.

If a database was previously enabled for replication using ALTER DATABASE … ENABLE REPLICATION TO ACCOUNTS, database replication
must be disabled before the database can be added to a [replication or failover group](../../user-guide/account-replication-intro.md).

## Syntax

```sqlsyntax
SYSTEM$DISABLE_DATABASE_REPLICATION('<db_name>');
```

## Arguments

`db_name`
:   Specifies the identifier for the database.

## Usage notes

* Only account administrators (users with the ACCOUNTADMIN role) can execute this SQL function.
* This function must be executed from the source account with the primary database.

## Examples

Disable replication for primary database `mydb` and any linked secondary databases.

Executed from the source account:

```sqlexample
SELECT SYSTEM$DISABLE_DATABASE_REPLICATION('mydb');
```
