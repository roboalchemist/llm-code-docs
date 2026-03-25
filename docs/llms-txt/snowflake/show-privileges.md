# Source: https://docs.snowflake.com/en/sql-reference/sql/show-privileges.md

# SHOW PRIVILEGES

Lists the privileges granted to an application.

## Syntax

```sqlsyntax
SHOW PRIVILEGES IN APPLICATION <name>
```

## Parameters

`name`
:   Specifies the name of the application.

## Output

Specifies the privileges granted to an application.

| Column | Description |
| --- | --- |
| privilege | The name of the privilege as specified in the manifest file. |
| description | A description of the privilege, which is specified in the manifest file. For details, refer to [Access control privileges](../../user-guide/security-access-control-privileges.md). |
| is_granted | Specifies if the consumer has granted the privilege. |
| is_grantable | Specifies if the user running the command has an [activated role](../../user-guide/security-access-control-overview.md) that can grant this privilege |

## Usage notes

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
