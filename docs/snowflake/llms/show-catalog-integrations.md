# Source: https://docs.snowflake.com/en/sql-reference/sql/show-catalog-integrations.md

# SHOW CATALOG INTEGRATIONS

Lists the [catalog integrations](../../user-guide/tables-iceberg.md) in your account.
The output returns integration metadata and properties.

See also:
:   [CREATE CATALOG INTEGRATION](create-catalog-integration.md) , [ALTER CATALOG INTEGRATION](alter-catalog-integration.md) , [DROP CATALOG INTEGRATION](drop-catalog-integration.md) , [DESCRIBE CATALOG INTEGRATION](desc-catalog-integration.md)

## Syntax

```sqlsyntax
SHOW CATALOG INTEGRATIONS [ LIKE '<pattern>' ]
```

## Parameters

`LIKE 'pattern'`
:   Optionally filters the command output by object name. The filter uses case-insensitive pattern matching, with support for SQL
    wildcard characters (`%` and `_`).

    For example, the following patterns return the same results:

    `... LIKE '%testing%' ...`

    `... LIKE '%TESTING%' ...`

    . Default: No value (no filtering is applied to the output).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE | Integration |  |
| OWNERSHIP | Integration | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Output

The command output provides table properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| `name` | Name of the catalog integration. |
| `enabled` | Specifies whether the catalog integration is available to use for Apache Iceberg™ tables. |
| `type` | Type of the integration. The value is always CATALOG. |
| `category` | Category of the integration. The value is always CATALOG. |
| `comment` | String (literal) that specifies a comment for the integration. |
| `created_on` | Date and time when the catalog integration was created. |

For more information about the properties that can be specified for a catalog integration, see [CREATE CATALOG INTEGRATION](create-catalog-integration.md).

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

## Examples

Show all catalog integrations:

```sqlexample
SHOW CATALOG INTEGRATIONS;
```

Show all the catalog integrations whose name starts with `demo` that you have privileges to view:

```sqlexample
SHOW CATALOG INTEGRATIONS LIKE 'demo%';
```
