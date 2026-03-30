# Source: https://docs.snowflake.com/en/sql-reference/sql/show-global-accounts.md

# SHOW GLOBAL ACCOUNTS

Lists all the accounts in your organization that are enabled for replication and indicates the Snowflake Region in which each account
is located.

Currently, linking accounts in your organization for replication requires assistance from Snowflake Support.

See also:
:   [SHOW REPLICATION DATABASES](show-replication-databases.md)

## Syntax

```sqlsyntax
SHOW GLOBAL ACCOUNTS [ LIKE '<pattern>' ]
```

## Parameters

`LIKE 'pattern'`
:   Optionally filters the command output by object name. The filter uses case-insensitive pattern matching, with support for SQL
    wildcard characters (`%` and `_`).

    For example, the following patterns return the same results:

    `... LIKE '%testing%' ...`

    `... LIKE '%TESTING%' ...`

    . Default: No value (no filtering is applied to the output).

## Output

The command output provides global account properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| `region_group` | Region group where the account is located. |
| `snowflake_region` | Snowflake Region where the account is located. A Snowflake Region is a distinct location within a cloud platform region that is isolated from other Snowflake Regions. A Snowflake Region can be either multi-tenant or single-tenant (for a Virtual Private Snowflake account). |
| `created_on` | Date and time when the account was created. |
| `name` | Name of the account. |
| `comment` | Comment for the account. |
| `is_org_admin` | Indicates whether the ORGADMIN role is enabled in an account. If TRUE, the role is enabled. |

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

* The command returns a maximum of ten thousand records for the specified object type, as dictated by the access privileges for the role
  used to execute the command. Any records above the ten thousand records limit aren’t returned, even with a filter applied.

  To view results for which more than ten thousand records exist, query the corresponding view (if one exists) in the [Snowflake Information Schema](../info-schema.md).

## Examples

Show all the global accounts whose name starts with `myaccount`:

```sqlexample
SHOW GLOBAL ACCOUNTS LIKE 'myaccount%';
```
