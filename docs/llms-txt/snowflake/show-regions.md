# Source: https://docs.snowflake.com/en/sql-reference/sql/show-regions.md

# SHOW REGIONS

Lists all the [regions](../../user-guide/intro-regions.md) in which accounts can be created. This command returns the Snowflake Region name,
the cloud provider (AWS, Google Cloud Platform, or Microsoft Azure) that hosts the account, and the cloud provider’s name for the region.

See also:
:   [CURRENT_REGION](../functions/current_region.md)

## Syntax

```sqlsyntax
SHOW REGIONS [ LIKE '<pattern>' ]
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

The command output provides region properties and metadata in the following columns. The command output for organizations that span multiple [region groups](../../user-guide/admin-account-identifier.md) includes an additional
`region_group` column.

| Column | Description |
| --- | --- |
| `region_group` | [Region group](../../user-guide/admin-account-identifier.md) where the account is located. **Note**: This column is only displayed for organizations that span multiple region groups. |
| `snowflake_region` | Snowflake Region where the account is located. A Snowflake Region is a distinct location within a cloud platform region that is isolated from other Snowflake Regions. A Snowflake Region can be either multi-tenant or single-tenant (for a Virtual Private Snowflake account). |
| `cloud` | Name of the cloud provider that hosts the account. |
| `region` | Region where the account is located; i.e. the cloud provider’s name for the region. |
| `display_name` | Human-readable cloud region name, e.g. `US West (Oregon)` |

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
