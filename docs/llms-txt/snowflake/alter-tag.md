# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-tag.md

# ALTER TAG

Modifies the properties for an existing tag, including renaming the tag and setting a masking policy on a tag.

Any changes made to the tag go into effect when the next SQL query that uses the tag runs.

See also:
:   [CREATE TAG](create-tag.md) , [DROP TAG](drop-tag.md) , [SHOW TAGS](show-tags.md) , [UNDROP TAG](undrop-tag.md)

## Syntax

```sqlsyntax
ALTER TAG [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER TAG [ IF EXISTS ] <name> { ADD | DROP } ALLOWED_VALUES '<val_1>' [ , '<val_2>' [ , ... ] ]

ALTER TAG [ IF EXISTS ] <name> SET
  [ ALLOWED_VALUES '<val_1>' [ , '<val_2>' [ , ... ] ] ]
  [ PROPAGATE = { ON_DEPENDENCY_AND_DATA_MOVEMENT | ON_DEPENDENCY | ON_DATA_MOVEMENT }
    [ ON_CONFLICT = { '<string>' | ALLOWED_VALUES_SEQUENCE } ] ]
  [ COMMENT = '<string_literal>' ]

ALTER TAG [ IF EXISTS ] <name> UNSET { ALLOWED_VALUES | PROPAGATE | ON_CONFLICT | COMMENT }

ALTER TAG [ IF EXISTS ] <name> SET MASKING POLICY
  <masking_policy_name> [ , MASKING POLICY <masking_policy_2_name> , ... ] [ FORCE ]

ALTER TAG [ IF EXISTS ] <name> UNSET MASKING POLICY <masking_policy_name> [ , MASKING POLICY <masking_policy_2_name> , ... ]
```

## Parameters

`name`
:   Identifier for the tag. Assign the tag string value on an [object](../../user-guide/object-tagging/introduction.md) using either a
    [CREATE <object>](create.md) statement or an [ALTER <object>](alter.md) statement.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire
    identifier string is enclosed in double quotes (e.g. “My object”). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md)

`RENAME TO new_name`
:   Specifies the new identifier for the tag; must be unique for your schema. The new identifier cannot be used if the identifier is already
    in place for a different tag.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

    You can move the object to a different database and/or schema while optionally renaming the object. To do so, specify
    a qualified `new_name` value that includes the new database and/or schema name in the form
    `db_name.schema_name.object_name` or `schema_name.object_name`, respectively.

    > **Note:**
    >
    > * The destination database and/or schema must already exist. In addition, an object with the same name cannot already
    >   exist in the new location; otherwise, the statement returns an error.
    > * Moving an object to a managed access schema is prohibited unless the object owner (that is, the role that has
    >   the OWNERSHIP privilege on the object) also owns the target schema.

`ALLOWED_VALUES 'val_1' [ , 'val_2' [ , ... ] ]`
:   Specifies a comma-separated list of the possible string values that can be assigned to the tag when the tag is set on an
    [object](../../user-guide/object-tagging/introduction.md) using the corresponding [CREATE <object>](create.md) or
    [ALTER <object>](alter.md) command.

    The maximum number of tag values in this list is 5,000.

    If you use the SET ALLOWED_VALUES clause, the specified values *replace* previously specified values, which allows you to adjust the
    sequence of values atomically.

    Using the DROP ALLOWED_VALUES clause to remove all values prevents someone from setting the tag to a value. If your intention is to let
    users set the tag to any value, use UNSET ALLOWED_VALUES instead.

    If a tag is configured to automatically propagate to target objects, the order of values in the allowed list can affect how conflicts are
    resolved. For more information, see [Tag propagation conflicts](../../user-guide/object-tagging/propagation.md).

    Default: NULL (all string values are allowed, including an empty string value (that is, `' '`)).

`PROPAGATE = { ON_DEPENDENCY_AND_DATA_MOVEMENT | ON_DEPENDENCY | ON_DATA_MOVEMENT }`
:   [Enterprise Edition Feature](../../user-guide/intro-editions.md)

    This parameter requires Enterprise Edition or higher. To inquire about upgrading, please contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

    Specifies that the tag will be [automatically propagated](../../user-guide/object-tagging/propagation.md) from source objects to target
    objects. You can configure the tag to propagate when there is an [object dependency](../../user-guide/object-tagging/propagation.md),
    [data movement](../../user-guide/object-tagging/propagation.md), or both.

    Changes to this parameter do not automatically propagate to target objects. These changes have no effect on tags that were previously
    applied to target objects as part of tag propagation.

    Possible values are:

    `ON_DEPENDENCY_AND_DATA_MOVEMENT`
    :   Propagates the tag when there is an object dependency or data movement.

    `ON_DEPENDENCY`
    :   Propagates the tag for object dependencies, but not for data movement.

    `ON_DATA_MOVEMENT`
    :   Propagates the tag when there is data movement, but not for object dependencies.

`ON_CONFLICT = { 'string' | ALLOWED_VALUES_SEQUENCE }`
:   [Enterprise Edition Feature](../../user-guide/intro-editions.md)

    This parameter requires Enterprise Edition or higher. To inquire about upgrading, please contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

    Specifies what happens when there is a conflict between the values of [propagated tags](../../user-guide/object-tagging/propagation.md).

    If you don’t set this parameter and there is a conflict, the value of the tag is set to the string `CONFLICT`.

    Changes to this parameter do not automatically propagate to target objects. These changes have no effect on tags that were previously
    applied to target objects as part of tag propagation.

    Possible values are:

    `'string'`
    :   When there is a conflict, the value of the tag is set to the specified string.

    `ALLOWED_VALUES_SEQUENCE`
    :   The order of the values in the ALLOWED_VALUES property of the tag determines which value is used when there is a conflict.
        For example, suppose you created a tag with the following statement:

        ```sqlexample
        CREATE TAG my_tag ALLOWED_VALUES 'blue', 'red' PROPAGATE = ON_DEPENDENCY;
        ```

        If there is a conflict, then the value of `my_tag` will be `blue` because it comes before `red` in the allowed values list.

    Default: Set the value of the tag to `CONFLICT`.

`MASKING POLICY masking_policy_name [ , MASKING POLICY masking_policy_2_name , ... ]`
:   Specifies a comma-separated list of [masking policies](../../user-guide/security-column-intro.md) that can be assigned to the tag.

`FORCE`
:   Replaces a masking policy that is currently set on a tag with a different masking policy in a single statement.

    Note that using the FORCE keyword replaces the masking policy when a policy of the same [data type](../../sql-reference-data-types.md) is
    already set on the tag.

    If a masking policy is not currently set on the tag, specifying this keyword has no effect.

    For details, see [Replace a masking policy on a tag](../../user-guide/tag-based-masking-policies.md).

`COMMENT = 'string_literal'`
:   Specifies a comment for the tag.

    Default: No value

`UNSET`
:   Specifies one (or more) properties and/or parameters to unset for the tag, which resets them to the defaults:

    * `ALLOWED_VALUES`
    * `PROPAGATE`
    * `ON_CONFLICT`
    * `COMMENT`

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Tag | This privilege is required to modify tag properties (e.g. comment, allowed values).  OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |
| APPLY MASKING POLICY | Account | Assigning and replacing a masking policy on a tag requires the global APPLY MASKING POLICY privilege. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For additional details on tag DDL and privileges, see [Access control privileges](../../user-guide/object-tagging/work.md).

## Usage notes

* For more information on tag DDL authorization, see [required privileges](../../user-guide/object-tagging/work.md).
* Regarding assigning one or more masking policies to a tag:

  * A tag can have only one masking policy per data type.

    For example, a tag can have one policy for the STRING data type, one policy for the NUMBER data type, and so on.
  * If a masking policy already protects a column and the tag with a masking policy is set on the same column, the masking policy
    directly assigned to the column takes precedence over the masking policy assigned to the tag.
  * A tag cannot be [dropped](drop-tag.md) if a masking policy is assigned to the tag, nor can the masking policy be
    dropped if the masking policy is assigned to a tag.
* Regarding replication, particularly with tag-based masking policies, see
  [policy replication considerations](../../user-guide/database-replication-considerations.md).
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Rename the `cost_center` tag to `cost_center_na`, where `na` specifies North America.

> ```sqlexample
> ALTER TAG cost_center RENAME TO cost_center_na;
> ```
