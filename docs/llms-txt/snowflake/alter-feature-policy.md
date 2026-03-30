# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-feature-policy.md

# ALTER FEATURE POLICY

Alters or renames a [feature policy](../../developer-guide/native-apps/ui-consumer-feature-policies.md).

See also:
:   [CREATE FEATURE POLICY](create-feature-policy.md) , [DESCRIBE FEATURE POLICY](desc-feature-policy.md), [DROP FEATURE POLICY](drop-feature-policy.md), [SHOW FEATURE POLICIES](show-feature-policies.md)

## Syntax

```sqlsyntax
ALTER FEATURE POLICY [ IF EXISTS ] <name> SET
  [ BLOCKED_OBJECT_TYPES_FOR_CREATION = ( [ <type> [ , <type>  ... ] ] ) ]
  [ COMMENT = '<string_literal>' ]

ALTER FEATURE POLICY [ IF EXISTS ] <name> UNSET
  [ BLOCKED_OBJECT_TYPES_FOR_CREATION ]
  [ COMMENT ]

ALTER FEATURE POLICY [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER FEATURE POLICY [ IF EXISTS ] <name> SET  TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER FEATURE POLICY [ IF EXISTS ] <name> UNSET TAG <tag_name> [ , ... ]
```

## Parameters

`name`
:   Specifies the identifier for the feature policy to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`SET`
:   Specifies one (or more) properties to set for the feature policy.

    `BLOCKED_OBJECT_TYPES_FOR_CREATION = ( type [ , type ... ] )`
    :   Specifies the objects that an app is prohibit from creating.

        Possible values are:

        * COMPUTE_POOLS
        * DATABASES
        * TASKS
        * WAREHOUSES

    `COMMENT = 'string_literal'`
    :   String (literal) that specifies a comment for the feature policy.

`TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| APPLY FEATURE POLICY | Account | This privilege is required to set a feature policy for the current account. |
| APPLY or OWNERSHIP | Feature policy | One of these privileges is required to modify a feature policy. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* If a previous policy had been applied to the account or an app an error is return, unless the you
  specify the FORCE option to force the replacement of the existing policy.
* When a feature policy is unbound from an app, the account level policy takes effect, if it exists.

## Examples

The following example sets the BLOCKED_OBJECT_TYPES_FOR_CREATION property on the feature policy
to prohibit an app from creating databases or tasks:

```sqlexample
ALTER FEATURE POLICY block_create_db_policy SET
  BLOCKED_OBJECT_TYPES_FOR_CREATION = (DATABASES, TASKS);
```

The following example changes the name of a feature policy from `block_create_db_policy` to
`block_create_db_task_policy`:

```sqlexample
ALTER FEATURE POLICY block_create_db_policy RENAME TO block_create_db_task_policy;
```
