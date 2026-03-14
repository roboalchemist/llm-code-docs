# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-projection-policy.md

# ALTER PROJECTION POLICY

Replaces the existing [projection policy](../../user-guide/projection-policies.md) rules with new rules or a new comment and allows the
renaming of a projection policy.

Any changes made to the policy rules go into effect when the next SQL query that uses the projection policy runs.

See also:
:   [Projection policy DDL reference](../../user-guide/projection-policies.md)

## Syntax

```sqlsyntax
ALTER PROJECTION POLICY [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER PROJECTION POLICY [ IF EXISTS ] <name> SET BODY -> <expression>

ALTER PROJECTION POLICY <name> SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER PROJECTION POLICY <name> UNSET TAG <tag_name> [ , <tag_name> ... ]

ALTER PROJECTION POLICY [ IF EXISTS ] <name> SET COMMENT = '<string_literal>'

ALTER PROJECTION POLICY [ IF EXISTS ] <name> UNSET COMMENT
```

## Parameters

`name`
:   Specifies the identifier for the projection policy to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`RENAME TO new_name`
:   Specifies the new identifier for the projection policy; must be unique for your schema. The new identifier cannot be used if the
    identifier is already in place for a different projection policy.

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

`SET ...`
:   Specifies one (or more) properties to set for the projection policy:

    `BODY -> expression`
    :   SQL expression that determines whether to project the column.

        The expression can contain CASE and other logic statements, but must call the PROJECTION_CONSTRAINT function:

        ```sqlsyntax
        PROJECTION_CONSTRAINT(ALLOW=>{TRUE|FALSE}, ENFORCEMENT=><enforcement_style>)
        ```

        * `ALLOW => { TRUE | FALSE }` - TRUE allows the column to be projected. FALSE prevents the column from being projected, with the behavior
          specified by ENFORCEMENT. FALSE affects only columns that appear in the final results table.
        * `ENFORCEMENT => 'enforcement_style'` - If ALLOW=FALSE, specifies what should happen if a query includes a protected column.
          Supported values:

          + FAIL - The query will fail if a protected column is included in the outermost query.
          + NULLIFY - All rows in the protected column return the value NULL.

          Default: FAIL

    `TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
    :   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

        The tag value is always a string, and the maximum number of characters for the tag value is 256.

        For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites the existing comment for the projection policy.

        Default: No value

`UNSET ...`
:   Specifies one or more properties and/or parameters to unset, by resetting them to their defaults, for the projection policy:

    * `TAG tag_name [ , tag_name ... ]`
    * `COMMENT`

    When resetting a property/parameter, specify only the name; specifying a value for the property will return an error.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Projection policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For additional details on projection policy DDL and privileges, see [Privileges and commands](../../user-guide/projection-policies.md).

## Usage notes

* If you want to update an existing projection policy and need to see the current definition of the policy, run the
  [DESCRIBE PROJECTION POLICY](desc-projection-policy.md) command or [GET_DDL](../functions/get_ddl.md) function.
* Moving a projection policy to a [managed access schema](../../user-guide/security-access-control-configure.md)
  (using the ALTER PROJECTION POLICY … RENAME TO syntax) is prohibited unless the projection policy owner
  (i.e. the role that has the OWNERSHIP privilege on the projection policy) also owns the target schema.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Rename a projection policy:

> ```sqlexample
> ALTER PROJECTION POLICY mypolicy RENAME TO proj_policy_acctnumber;
> ```
