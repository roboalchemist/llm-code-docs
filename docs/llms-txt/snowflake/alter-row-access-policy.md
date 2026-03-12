# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-row-access-policy.md

# ALTER ROW ACCESS POLICY

Modifies the properties for an existing row access policy, including renaming the policy or replacing the policy rules.

Any changes made to the policy rules go into effect when the next SQL query that uses the row access policy runs.

See also:
:   [Row access policy DDL](../../user-guide/security-row-intro.md)

## Syntax

```sqlsyntax
ALTER ROW ACCESS POLICY [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER ROW ACCESS POLICY [ IF EXISTS ] <name> SET BODY -> <expression_on_arg_name>

ALTER ROW ACCESS POLICY [ IF EXISTS ] <name> SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER ROW ACCESS POLICY [ IF EXISTS ] <name> UNSET TAG <tag_name> [ , <tag_name> ... ]

ALTER ROW ACCESS POLICY [ IF EXISTS ] <name> SET COMMENT = '<string_literal>'

ALTER ROW ACCESS POLICY [ IF EXISTS ] <name> UNSET COMMENT
```

## Parameters

`name`
:   Identifier for the row access policy; must be unique in the parent schema of the policy.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire
    identifier string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`RENAME TO new_name`
:   Specifies the new identifier for the row access policy; must be unique for your schema. The new identifier cannot be used if the
    identifier is already in place for a different row access policy.

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
:   Specifies one (or more) properties to set for the row access policy:

    `BODY -> expression_on_arg_name`
    :   SQL expression that filters the data.

        The expression can include [Conditional expression functions](../expressions-conditional.md) to represent conditional logic, built-in functions, or UDFs to
        transform the data.

        If a UDF or external function is used inside the row access policy body, the policy owner must have OWNERSHIP on the UDF or external
        function. Users querying a database object that has a row access policy applied to it do not need to have USAGE on the UDF or external
        function.

    `TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
    :   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

        The tag value is always a string, and the maximum number of characters for the tag value is 256.

        For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites the existing comment for the masking policy.

        Default: No value

    `UNSET ...`
    :   Specifies one or more properties and/or parameters to unset for the masking policy, which resets them to the defaults:

        * `TAG tag_name [ , tag_name ... ]`
        * `COMMENT`

        When resetting a property/parameter, specify only the name; specifying a value for the property will return an error.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Row access policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For additional details on row access policy DDL and privileges, see [Manage row access policies](../../user-guide/security-row-intro.md).

## Usage notes

* If you want to update an existing row access policy and need to see the current definition of the policy, call the
  [GET_DDL](../functions/get_ddl.md) function or run the [DESCRIBE ROW ACCESS POLICY](desc-row-access-policy.md) command.
* You cannot change the policy signature (i.e. argument name or input/output data type). Similarly, using
  `CREATE OR REPLACE ROW ACCESS POLICY` is not supported if the policy is attached to a table or view. If you need to change the
  signature, execute a [DROP ROW ACCESS POLICY](drop-row-access-policy.md) statement on the policy and create a new row access policy.
* Before executing an ALTER statement, you can execute a [DESCRIBE ROW ACCESS POLICY](desc-row-access-policy.md) statement to determine the
  argument name to use for updating the policy.
* Including one or more [subqueries](../../user-guide/querying-subqueries.md) in the policy body may cause errors. When possible, limit the
  number of subqueries, limit the number of JOIN operations, and simplify WHERE clause conditions.
* If the policy `body` contains a mapping table lookup, create a centralized mapping table and store the mapping table
  in the same database as the protected table. This is particularly important if the `body` calls the
  [IS_DATABASE_ROLE_IN_SESSION](../functions/is_database_role_in_session.md) function. For details, see the function usage notes.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

The following example updates the row access policy.

> ```sqlexample
> DESC ROW ACCESS POLICY rap_table_employee_info;
> ```

```output
+-------------------------+-------------+-------------+------+
| name                    | signature   | return_type | body |
+-------------------------+-------------+-------------+------+
| rap_table_employee_info | (V VARCHAR) | BOOLEAN     | true |
+-------------------------+-------------+-------------+------+
```

```sqlexample
ALTER ROW ACCESS POLICY rap_table_employee_info SET BODY -> false;
```
