# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-managed-account.md

# DROP MANAGED ACCOUNT

Removes a managed account, including all objects created in the account, and immediately restricts access to the account. Currently
used by data providers to create reader accounts for their consumers. For more details, see [Manage reader accounts](../../user-guide/data-sharing-reader-create.md).

See also:
:   [CREATE MANAGED ACCOUNT](create-managed-account.md) , [SHOW MANAGED ACCOUNTS](show-managed-accounts.md)

## Syntax

```sqlsyntax
DROP MANAGED ACCOUNT <name>
```

## Usage notes

* This command can be executed by users with the ACCOUNTADMIN role (or a role that has been granted the CREATE ACCOUNT global privilege).
* This operation can not be undone.

## Examples

```sqlexample
DROP MANAGED ACCOUNT reader_acct1;

  +------------------------------------+
  | status                             |
  |------------------------------------|
  | READER_ACCT1 successfully dropped. |
  +------------------------------------+
```
