# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-privacy-policy.md

# DROP PRIVACY POLICY

Removes the specified [privacy policy](../../user-guide/diff-privacy/differential-privacy-admin-privacy-policies.md) from the current/specified schema.

See also:
:   [CREATE PRIVACY POLICY](create-privacy-policy.md) , [ALTER PRIVACY POLICY](alter-privacy-policy.md) , [DESCRIBE PRIVACY POLICY](desc-privacy-policy.md) , [SHOW PRIVACY POLICIES](show-privacy-policies.md)

## Syntax

```sqlsyntax
DROP PRIVACY POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier for the privacy policy to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Privacy policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

A privacy policy cannot be dropped successfully if it is currently assigned to a table or view.

Before executing a DROP statement, execute the following statement to determine if the privacy policy is set on any tables or views.

```sqlexample
SELECT * FROM TABLE(mydb.INFORMATION_SCHEMA.POLICY_REFERENCES(POLICY_NAME=>'my_privacy_policy'));
```

For each table or view, use [ALTER TABLE … DROP PRIVACY POLICY …](alter-table.md) or
[ALTER VIEW … DROP PRIVACY POLICY …](alter-view.md) to [detach the privacy policy](../../user-guide/diff-privacy/differential-privacy-admin-privacy-policies.md) from the
table or view.

## Examples

The following example drops the privacy policy named `myprivpolicy`:

```sqlexample
DROP PRIVACY POLICY myprivpolicy;
```

```output
+------------------------------------+
| status                             |
|------------------------------------|
| MYPRIVPOLICY successfully dropped. |
+------------------------------------+
```
