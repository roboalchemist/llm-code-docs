# Source: https://docs.snowflake.com/en/sql-reference/sql/create-feature-policy.md

# CREATE FEATURE POLICY

Creates a new [feature policy](../../developer-guide/native-apps/ui-consumer-feature-policies.md).

See also:
:   [ALTER FEATURE POLICY](alter-feature-policy.md) , [DESCRIBE FEATURE POLICY](desc-feature-policy.md), [DROP FEATURE POLICY](drop-feature-policy.md), [SHOW FEATURE POLICIES](show-feature-policies.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] FEATURE POLICY [ IF NOT EXISTS ] <name>
  BLOCKED_OBJECT_TYPES_FOR_CREATION = ( <type> [ , ... ] )
  [ COMMENT = '<string-literal>' ]
```

## Parameters

`name`
:   Specifies the identifier for the feature policy.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`BLOCKED_OBJECT_TYPES_FOR_CREATION = ( type [ , ... ] )`
:   Specifies a list of objects that an app can’t create in the consumer account. The
    following objects can be blocked:

    * COMPUTE POOLS
    * WAREHOUSES
    * TASKS
    * DATABASES

`COMMENT = 'string_literal'`
:   String (literal) that specifies a comment for the feature policy.

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE FEATURE POLICY | SCHEMA | Grants the ability to create feature policies. You must have this privilege set on the schema containing the policy to be created. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* If a policy is bound to an object, for example an account or an app, the policy cannot be replaced.
  Use the [ALTER FEATURE POLICY](alter-feature-policy.md) to update or rename the feature policy.
* This command does not support using the CLONE clause to create a copy of a feature policy.

## Examples

The following example creates a new feature policy that prohibits an app from creating a database:

```sqlexample
CREATE FEATURE POLICY block_create_db_policy
  BLOCKED_OBJECT_TYPES_FOR_CREATION = (DATABASES);
```

The following example creates a new feature policy, but doesn’t specify any objects to prohibit.

```sqlexample
CREATE FEATURE POLICY block_nothing_policy
  BLOCKED_OBJECT_TYPES_FOR_CREATION = ();
```

> **Note:**
>
> This syntax would typically be applied to an app to lift any restrictions that were applied at
> the account level.
