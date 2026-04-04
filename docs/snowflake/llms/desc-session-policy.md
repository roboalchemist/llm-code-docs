# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-session-policy.md

# DESCRIBE SESSION POLICY

Describes the details about a session policy.

DESCRIBE can be abbreviated to DESC.

See also:
:   [Session Policy DDL Reference](../../user-guide/session-policies-managing.md)

## Syntax

```sqlsyntax
{ DESCRIBE | DESC } SESSION POLICY <name>
```

## Parameters

`name`
:   Identifier for the session policy; must be unique for your account.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire identifier
    string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| APPLY SESSION POLICY | Account |  |
| OWNERSHIP | Session policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For additional details on session policy DDL and privileges, see [Managing session policies](../../user-guide/session-policies-managing.md).

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

## Output

The output of the command includes the following columns, which describe the properties and metadata of the object:

| Column | Description |
| --- | --- |
| `created_on` | The timestamp when the session policy was created. |
| `name` | Identifier for the session policy. |
| `session_idle_timeout_mins` | For Snowflake Clients and programmatic clients, the number of minutes in which a session can be idle before users must authenticate to Snowflake again. |
| `session_ui_idle_timeout_mins` | For Snowsight, the number of minutes in which a session can be idle before users must authenticate to Snowflake again. |
| `allowed_secondary_roles` | The secondary roles for a session policy, if any. |
| `comment` | Comment for the session policy. |

## Example

```sqlexample
DESC SESSION POLICY session_policy_prod_1;
```

```output
+---------------------------------+-----------------------+---------------------------+------------------------------+-------------------------+--------------------------------------------------+
| created_on                       | name                 | session_idle_timeout_mins | session_ui_idle_timeout_mins | allowed_secondary_roles |  comment                                         |
+---------------------------------+-----------------------+---------------------------+------------------------------+-------------------------+--------------------------------------------------+
| Mon, 11 Jan 2021 00:00:00 -0700 | session_policy_prod_1 | 60                        | 30                           |           []            | session policy for use in the prod_1 environment |
+---------------------------------+-----------------------+---------------------------+------------------------------+-------------------------+--------------------------------------------------+
```
