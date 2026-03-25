# Source: https://docs.snowflake.com/en/sql-reference/sql/show-shares-in-replication-group.md

# SHOW SHARES IN REPLICATION GROUP

Lists shares in a [replication group](../../user-guide/account-replication-intro.md).

See also:
:   [SHOW DATABASES IN REPLICATION GROUP](show-databases-in-replication-group.md)

## Syntax

```sqlsyntax
SHOW SHARES IN REPLICATION GROUP <name>
```

## Parameters

`name`
:   Specifies the identifier for the replication group.

## Usage notes

* Executing this command requires a role with either the OWNERSHIP or MONITOR privilege on the replication group. The command
  returns results only for a role with the MONITOR privilege on a share.
* To retrieve the list of replication groups in your organization, use [SHOW REPLICATION GROUPS](show-replication-groups.md).

* The command doesn’t require a running warehouse to execute.
* The command only returns objects for which the current user’s current role has been granted at least one access privilege.
* The MANAGE GRANTS access privilege implicitly allows its holder to see every object in the account. By default, only the account
  administrator (users with the ACCOUNTADMIN role) and security administrator (users with the SECURITYADMIN role) have the
  MANAGE GRANTS privilege.

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

## Examples

List the shares in the replication group `myrg`:

```sqlexample
SHOW SHARES IN REPLICATION GROUP myrg;
```
