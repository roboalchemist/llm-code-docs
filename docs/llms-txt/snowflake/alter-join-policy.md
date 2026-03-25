# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-join-policy.md

# ALTER JOIN POLICY

Replaces the existing rules or comment for a [join policy](../../user-guide/join-policies.md). Also allows you to rename a join policy.

See also:
:   [Join policy DDL reference](../../user-guide/join-policies.md)

## Syntax

```sqlsyntax
ALTER JOIN POLICY [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER JOIN POLICY [ IF EXISTS ] <name> SET BODY -> <expression>

ALTER JOIN POLICY <name> SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER JOIN POLICY <name> UNSET TAG <tag_name> [ , <tag_name> ... ]

ALTER JOIN POLICY [ IF EXISTS ] <name> SET COMMENT = '<string_literal>'

ALTER JOIN POLICY [ IF EXISTS ] <name> UNSET COMMENT
```

## Parameters

`name`
:   Specifies the identifier for the join policy to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`RENAME TO new_name`
:   Specifies the new identifier for the join policy; must be unique for your schema. The new identifier cannot be used if the
    identifier is already in place for a different join policy.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

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
:   Specifies one (or more) properties to set for the join policy:

    `BODY -> expression`
    :   SQL expression that determines the restrictions of a join policy.

        To define the body of the join policy, call the JOIN_CONSTRAINT function, which returns TRUE or FALSE.
        When the function returns TRUE, queries are required to use a join to return results.

        The syntax of the JOIN_CONSTRAINT function is:

        ```sqlsyntax
        JOIN_CONSTRAINT (
          { JOIN_REQUIRED => <boolean_expression> }
          )
        ```

        Where:

        `JOIN_REQUIRED => boolean_expression`
        :   Specifies whether a join is required in queries when data is selected from tables or views that have
            the join policy assigned to them.

        The body of a policy cannot reference user-defined functions, tables, or views.

        Allowed join columns are specified in the CREATE or ALTER statement for the table or view to which the
        policy is applied, not in the CREATE JOIN POLICY statement.

    `TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
    :   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

        The tag value is always a string, and the maximum number of characters for the tag value is 256.

        For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites the existing comment for the join policy.

        Default: No value

`UNSET ...`
:   Specifies one or more properties and/or parameters to unset, by resetting them to their defaults, for the join policy:

    * `TAG tag_name [ , tag_name ... ]`
    * `COMMENT`

    When resetting a property/parameter, specify only the name; specifying a value for the property will return an error.

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

For more information about join policy DDL and privileges, see [Privileges and commands](../../user-guide/aggregation-policies.md).

## Usage notes

* If you want to update an existing join policy and need to see the current body of the policy, run the
  [DESCRIBE JOIN POLICY](desc-join-policy.md) command. You can also use the [GET_DDL](../functions/get_ddl.md) function to obtain the full definition of the join policy, including its body.
* Moving a join policy to a [managed access schema](../../user-guide/security-access-control-configure.md)
  (using the ALTER JOIN POLICY … RENAME TO syntax) is prohibited unless the join policy owner
  (that is, the role that has the OWNERSHIP privilege on the join policy) also owns the target schema.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Modify the SQL expression for a join policy:

```sqlexample
ALTER JOIN POLICY jp3 SET BODY -> JOIN_CONSTRAINT(JOIN_REQUIRED => FALSE);
```

Rename a join policy:

```sqlexample
ALTER JOIN POLICY my_join_policy RENAME TO my_join_policy_2;
```
