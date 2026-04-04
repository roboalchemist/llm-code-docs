# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-share.md

# DROP SHARE

Removes the specified [share](../../user-guide/data-sharing-intro.md) from the system and immediately revokes access for all consumers
(i.e. accounts who have created a database from the share).

See also:
:   [CREATE SHARE](create-share.md) , [ALTER SHARE](alter-share.md) , [SHOW SHARES](show-shares.md) , [DESCRIBE SHARE](desc-share.md)

## Syntax

```sqlsyntax
DROP SHARE <name>
```

## Parameters

`name`
:   Specifies the identifier for the share to drop. If the identifier contains spaces, special characters, or mixed-case characters, the
    entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Usage notes

* Only the share owner, the role with the OWNERSHIP privilege on the share, has the privileges to drop a share.
  Executing this command with any other role returns an error.
* Dropped shares cannot be recovered; they must be recreated.
* Dropping a share does not affect the database in the share (or any of the objects in the database).

> **Important:**
>
> Before dropping a share, consider the downstream impact of performing this operation:
>
> * Consumer accounts that have created databases from the share will no longer be able to query these databases.
> * Recreating a share with the same name as a previous share does not restore the databases created (by any consumers) from the share.
>   Each consumer must create a new database from the new share.
> * A dropped share can not be restored. The share must be created again using the [CREATE SHARE](create-share.md) command and then
>   configured using [GRANT <privilege> … TO SHARE](grant-privilege-share.md) and [ALTER SHARE](alter-share.md).

## Examples

> ```sqlexample
> DROP SHARE sales_s;
>
> +-------------------------------+
> | status                        |
> |-------------------------------|
> | SALES_S successfully dropped. |
> +-------------------------------+
> ```
