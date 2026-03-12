# Source: https://docs.snowflake.com/en/sql-reference/sql/show-network-policies.md

# SHOW NETWORK POLICIES

Lists all network policies defined in the system.

See also:
:   [ALTER NETWORK POLICY](alter-network-policy.md) , [CREATE NETWORK POLICY](create-network-policy.md) , [DESCRIBE NETWORK POLICY](desc-network-policy.md) , [DROP NETWORK POLICY](drop-network-policy.md)

## Syntax

```sqlsyntax
SHOW NETWORK POLICIES
```

## Usage notes

* Only the network policy owner (that is, role with the OWNERSHIP privilege on the network policy) or higher can execute this command.

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

List all network policies:

> ```sqlexample
> SHOW NETWORK POLICIES;
> ```
>
> ```output
> +-------------------------------+----------+---------+----------------------------+----------------------------+---------------------------------------------------------------------+
> | created_on                    | name     | comment | entries_in_allowed_ip_list | entries_in_blocked_ip_list | entries_in_allowed_network_rules | entries_in_blocked_network_rules |
> |-------------------------------+----------+---------+----------------------------+----------------------------+----------------------------------+----------------------------------|
> | 2016-04-29 13:22:34.034 -0700 | Policy1  |         |                          2 |                          1 |                                 0|                                0 |
> | 2016-04-28 17:31:59.269 -0700 | Policy2  |         |                          1 |                          0 |                                 0|                                0 |
> +-------------------------------+----------+---------+----------------------------+----------------------------+----------------------------------+----------------------------------+
> ```
