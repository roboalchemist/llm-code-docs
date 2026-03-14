# Source: https://docs.snowflake.com/en/sql-reference/sql/show-roles-in-service.md

# SHOW ROLES IN SERVICE

Lists all the service roles associated with a service. These are the roles defined in the service specification. For more information, see [Managing service-related privileges](../../developer-guide/snowpark-container-services/working-with-services.md).

See also:
:   [REVOKE SERVICE ROLE](revoke-service-role.md), [GRANT SERVICE ROLE](grant-service-role.md),
    [SHOW GRANTS](show-grants.md)

## Syntax

```sqlsyntax
SHOW ROLES IN SERVICE <name>
```

## Parameters

`name`
:   Name of the service.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE | Service |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Output

The command output provides the following columns:

| Column | Description |
| --- | --- |
| `created_on` | Date and time when the service role was created |
| `name` | Service role name |
| `comment` | Comment, if any, for the service role |

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

List the service roles in the `echo_service` service.

```sqlexample
SHOW ROLES IN SERVICE echo_service;
```

```output
+-------------------------------+-------------------------+------------+
| created_on                    |   name                      |  comment   |
+-------------------------------+-------------------------+------------+
| 2024-04-29 14:58:50.063 -0700 |   ALL_ENDPOINTS_USAGE   |            |
+-------------------------------+-------------------------+------------+
```
