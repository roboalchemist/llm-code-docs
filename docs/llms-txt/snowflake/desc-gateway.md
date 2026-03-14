# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-gateway.md

# DESCRIBE GATEWAY

Describes the properties of a [gateway](../../developer-guide/snowpark-container-services/gateway.md).

DESCRIBE can be abbreviated to DESC.

See also:
:   [CREATE GATEWAY](create-gateway.md) , [ALTER GATEWAY](alter-gateway.md), [DROP GATEWAY](drop-gateway.md) , [SHOW GATEWAYS](show-gateways.md)

## Syntax

```sqlsyntax
DESC[RIBE] GATEWAY <name>
```

## Parameters

`name`
:   Specifies the identifier for the gateway to describe.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Output

The command output provides gateway properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| `name` | Gateway name. |
| `ingress_url` | Gateway ingress URL. |
| `privatelink_ingress_url` | PrivateLink ingress URL. |
| `database_name` | Database in which the gateway is created. |
| `schema_name` | Schema in which the gateway is created. |
| `owner` | Role that owns the gateway. |
| `owner_role_type` | The type of role that owns the object, either ROLE or DATABASE_ROLE. |
| `spec` | Gateway specification (YAML format). This column is only shown if the role executing the command has USAGE, MODIFY, or OWNERSHIP privilege on the gateway. |
| `created_on` | Timestamp when the gateway was created. |
| `updated_on` | Timestamp when the gateway was last updated. |
| `comment` | Gateway related comment. |

> **Note:**
>
> If the role used has USAGE, MODIFY, or OWNERSHIP privilege on the gateway, the `spec` column will be shown.
> If not, the other columns will be shown, but not the `spec` column.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE, MODIFY, or OWNERSHIP | Gateway | Any of these privileges allows describing the gateway. Only roles with these privileges can view the spec. |
| USAGE | Database | Required on the database containing the gateway. |
| USAGE | Schema | Required on the schema containing the gateway. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

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

The following example describes the gateway named `split_gateway`:

```sqlexample
DESCRIBE GATEWAY split_gateway;
```
