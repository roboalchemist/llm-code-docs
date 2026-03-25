# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-storage-lifecycle-policy.md

# DROP STORAGE LIFECYCLE POLICY

Removes the specified [storage lifecycle policy](../../user-guide/storage-management/storage-lifecycle-policies.md) from the current or specified schema.

See also:
:   [CREATE STORAGE LIFECYCLE POLICY](create-storage-lifecycle-policy.md) , [ALTER STORAGE LIFECYCLE POLICY](alter-storage-lifecycle-policy.md) , [DESCRIBE STORAGE LIFECYCLE POLICY](desc-storage-lifecycle-policy.md) , [SHOW STORAGE LIFECYCLE POLICIES](show-storage-lifecycle-policies.md)

## Syntax

```sqlsyntax
DROP STORAGE LIFECYCLE POLICY [ IF EXISTS ] <policy_name>
```

## Parameters

`policy_name`
:   Specifies the identifier for the storage lifecycle policy to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Schema or  Storage lifecycle policy | The schema that contains the policy.  OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

* Snowflake doesn’t support undropping storage lifecycle policy objects.
* If a table column has a storage lifecycle policy attached to it, you can’t drop the column from the table.
* You can’t drop a database or schema that contains a storage lifecycle policy attached to an object that belongs to a different database or schema.
* You can’t drop a storage lifecycle policy that is attached to a table. Remove the policy association before dropping the storage lifecycle policy.
* When you undrop a table or schema with an attached policy, the policy association is restored.

## Examples

The following example drops the storage lifecycle policy named `example_slp`:

```sqlexample
DROP STORAGE LIFECYCLE POLICY example_slp;
```

Output:

```output
+-----------------------------------+
| status                            |
|-----------------------------------|
| EXAMPLE_SLP successfully dropped. |
+-----------------------------------+
```
