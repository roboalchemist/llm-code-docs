# Source: https://docs.snowflake.com/en/sql-reference/sql/create-tag.md

# CREATE TAG

Creates a new tag or replaces an existing tag in the system.

This command supports the following variants:

* CREATE OR ALTER TAG: Creates a tag if it doesn’t exist or alters an existing tag.

See also:
:   [ALTER TAG](alter-tag.md) , [SHOW TAGS](show-tags.md) , [DROP TAG](drop-tag.md) , [UNDROP TAG](undrop-tag.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] TAG [ IF NOT EXISTS ] <name>
    [ ALLOWED_VALUES '<val_1>' [ , '<val_2>' [ , ... ] ] ]
    [ PROPAGATE = { ON_DEPENDENCY_AND_DATA_MOVEMENT | ON_DEPENDENCY | ON_DATA_MOVEMENT }
      [ ON_CONFLICT = { '<string>' | ALLOWED_VALUES_SEQUENCE } ] ]
    [ COMMENT = '<string_literal>' ]
```

## Variant syntax

### CREATE OR ALTER TAG

Creates a new tag if it doesn’t already exist, or transforms an existing tag into the tag defined in the statement.
A CREATE OR ALTER TAG statement follows the syntax rules of a CREATE TAG statement and has the same limitations as an
[ALTER TAG](alter-tag.md) statement.

Supported alterations include changes to the ALLOWED_VALUES and COMMENT properties.

For more information, see CREATE OR ALTER TAG usage notes.

```sqlsyntax
CREATE OR ALTER TAG <name>
  [ ALLOWED_VALUES '<val_1>' [ , '<val_2>' [ , ... ] ] ]
  [ COMMENT = '<string_literal>' ]
```

## Required parameters

`name`
:   Identifier for the tag. Assign the tag string value on an [object](../../user-guide/object-tagging/introduction.md) using either a
    [CREATE <object>](create.md) statement or an [ALTER <object>](alter.md) statement.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire
    identifier string is enclosed in double quotes (e.g. “My object”). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`ALLOWED_VALUES 'val_1' [ , 'val_2' [ , ... ] ]`
:   Specifies a comma-separated list of the possible string values that can be assigned to the tag when the tag is set on an
    [object](../../user-guide/object-tagging/introduction.md) using the corresponding [CREATE <object>](create.md) or
    [ALTER <object>](alter.md) command.

    Must come before all other parameters to work.

    The maximum number of tag values in this list is 5,000.

    If a tag is configured to automatically propagate to target objects, the order of values in the allowed list can affect how conflicts are
    resolved. For more information, see [Tag propagation conflicts](../../user-guide/object-tagging/propagation.md).

    Default: NULL (all string values are allowed, including an empty string value (that is, `' '`)).

`PROPAGATE = { ON_DEPENDENCY_AND_DATA_MOVEMENT | ON_DEPENDENCY | ON_DATA_MOVEMENT }`
:   [Enterprise Edition Feature](../../user-guide/intro-editions.md)

    This parameter requires Enterprise Edition or higher. To inquire about upgrading, please contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

    Specifies that the tag will be [automatically propagated](../../user-guide/object-tagging/propagation.md) from source objects to target
    objects. You can configure the tag to propagate when there is an [object dependency](../../user-guide/object-tagging/propagation.md),
    [data movement](../../user-guide/object-tagging/propagation.md), or both.

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

    Possible values are:

    `'string'`
    :   When there is a conflict, the value of the tag is set to the specified string.

    `ALLOWED_VALUES_SEQUENCE`
    :   The order of the values in the ALLOWED_VALUES property of the tag determines which value is used when there is a conflict. For example,
        suppose you created a tag with the following statement:

        ```sqlexample
        CREATE TAG my_tag ALLOWED_VALUES 'blue', 'red'
          PROPAGATE = ON_DEPENDENCY
          ON_CONFLICT = ALLOWED_VALUES_SEQUENCE;
        ```

        If there is a conflict, then the value of `my_tag` will be `blue` because it comes before `red` in the allowed values list.

    Default: Set the value of the tag to `CONFLICT`.

`COMMENT = 'string_literal'`
:   Specifies a comment for the tag.

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE TAG | Schema |  |
| OWNERSHIP | Tag | *A role must be granted or inherit the OWNERSHIP privilege on the object to create a temporary object that has the same name as the object   that already exists in the schema.* Required to execute a CREATE OR ALTER TAG statement for an *existing* tag. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For additional details on tag DDL and privileges, see [Access control privileges](../../user-guide/object-tagging/work.md).

## General usage notes

* You must set the ALLOWED_VALUES parameter before all other parameters, such as COMMENT.
* For more information about how tags can be associated with Snowflake objects, see [Introduction to object tagging](../../user-guide/object-tagging/introduction.md).
* For more information about tag DDL authorization, see [required privileges](../../user-guide/object-tagging/work.md).
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## CREATE OR ALTER TAG usage notes

* When you use this command, all unspecified parameters are reset. For example, if you specify a new comment only, then the PROPAGATE
  parameter no longer enables tag propagation.
* All limitations of the [ALTER TAG](alter-tag.md) command apply.
* Setting or unsetting a masking policy is not supported.

## Examples

Create a tag with the key `cost_center`.

```sqlexample
CREATE TAG cost_center COMMENT = 'cost_center tag';
```

Update `cost_center` to include new allowed values and unset the comment:

```sqlexample
CREATE OR ALTER TAG cost_center ALLOWED_VALUES 'finance', 'engineering', 'sales';
```
