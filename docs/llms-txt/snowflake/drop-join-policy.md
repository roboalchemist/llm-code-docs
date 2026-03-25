# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-join-policy.md

# DROP JOIN POLICY

Removes a [join policy](../../user-guide/join-policies.md) from the current/specified schema.

See also:
:   [Join policy DDL reference](../../user-guide/join-policies.md)

## Syntax

```sqlsyntax
DROP JOIN POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier for the join policy to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Join policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For more information about join policy DDL and privileges, see [Managing join policies](../../user-guide/join-policies.md).

## Usage notes

* Prior to dropping the join policy, execute the following statement to determine if the policy is set on any tables or
  views.

  ```sqlexample
  SELECT * FROM TABLE(mydb.INFORMATION_SCHEMA.POLICY_REFERENCES(POLICY_NAME=>'my_join_policy'));
  ```

  For more information, see [Getting information about tables and views attached to join policies](../../user-guide/join-policies.md).
* A join policy cannot be dropped successfully if it is currently assigned to a table or view.

  Before executing a DROP statement, [detach the join policy](../../user-guide/join-policies.md) from the table or view with an ALTER TABLE or ALTER VIEW statement.

## Example

Drop a join policy:

```sqlexample
DROP JOIN POLICY my_join_policy;
```
