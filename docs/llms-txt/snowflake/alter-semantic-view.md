# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-semantic-view.md

# ALTER SEMANTIC VIEW

Modifies the comment for an existing [semantic view](../../user-guide/views-semantic/overview.md) or renames a semantic view.

> **Note:**
>
> You can’t use the ALTER SEMANTIC VIEW command to change properties other than the comment. To change other properties of the
> semantic view, replace the semantic view. See [Replacing an existing semantic view](../../user-guide/views-semantic/sql.md).

See also:
:   [CREATE SEMANTIC VIEW](create-semantic-view.md) , [DESCRIBE SEMANTIC VIEW](desc-semantic-view.md) , [DROP SEMANTIC VIEW](drop-semantic-view.md) , [SHOW SEMANTIC VIEWS](show-semantic-views.md) , [SHOW SEMANTIC DIMENSIONS](show-semantic-dimensions.md) , [SHOW SEMANTIC DIMENSIONS FOR METRIC](show-semantic-dimensions-for-metric.md) , [SHOW SEMANTIC FACTS](show-semantic-facts.md) , [SHOW SEMANTIC METRICS](show-semantic-metrics.md)

## Syntax

```sqlsyntax
ALTER SEMANTIC VIEW [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER SEMANTIC VIEW [ IF EXISTS ] <name> SET
  COMMENT = '<string_literal>'

ALTER SEMANTIC VIEW [ IF EXISTS ] <name> UNSET
  COMMENT
```

## Parameters

`name`
:   Specifies the identifier for the semantic view to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`RENAME TO new_name`
:   Changes the name of the semantic view to `new_name`. The new identifier must be unique within the schema.

    For more details about identifiers, see [Identifier requirements](../identifiers-syntax.md).

    You can move the object to a different database and/or schema while optionally renaming the object. To do so, specify
    a qualified `new_name` value that includes the new database and/or schema name in the form
    `db_name.schema_name.object_name` or `schema_name.object_name`, respectively.

    > **Note:**
    >
    > * The destination database and/or schema must already exist. In addition, an object with the same name cannot already
    >   exist in the new location; otherwise, the statement returns an error.
    > * Moving an object to a managed access schema is prohibited unless the object owner (that is, the role that has
    >   the OWNERSHIP privilege on the object) also owns the target schema.

    When an object is renamed, other objects that reference it must be updated with the new name.

`SET ...`
:   Sets one or more specified properties or parameters for the semantic view:

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites an existing comment for the semantic view.

`UNSET ...`
:   Unsets one or more specified properties or parameters for the semantic view, which resets the properties to their defaults:

    * `COMMENT`

    To unset multiple properties or parameters with a single ALTER statement, separate each property or parameter with a comma.

    When unsetting a property or parameter, specify only the property or parameter name (unless the syntax above indicates that you
    should specify the value). Specifying the value returns an error.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Semantic view | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

The following example renames a semantic view:

```sqlexample
ALTER SEMANTIC VIEW sv RENAME TO sv_new_name;
```

The following example sets the comment for a semantic view:

```sqlexample
ALTER SEMANTIC VIEW my_semantic_view SET COMMENT = 'my comment';
```

The following example unsets the existing comment for a semantic view:

```sqlexample
ALTER SEMANTIC VIEW my_semantic_view UNSET COMMENT;
```
