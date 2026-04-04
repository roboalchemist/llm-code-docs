# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-session-policy.md

# ALTER SESSION POLICY

Modifies the properties for an existing session policy.

Any changes made to the session policy properties go into effect when the next SQL query that uses the session policy runs.

See also:
:   [Session Policy DDL Reference](../../user-guide/session-policies-managing.md)

## Syntax

```sqlsyntax
ALTER SESSION POLICY [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER SESSION POLICY [ IF EXISTS ] <name> SET
  [ SESSION_IDLE_TIMEOUT_MINS = <integer> ]
  [ SESSION_UI_IDLE_TIMEOUT_MINS = <integer> ]
  [ ALLOWED_SECONDARY_ROLES = ( [ { 'ALL' | <role_name> [ , <role_name> ... ] } ] ) ]
  [ BLOCKED_SECONDARY_ROLES = ( [ { 'ALL' | <role_name> [ , <role_name> ... ] } ] ) ]
  [ COMMENT = '<string_literal>' ]

ALTER SESSION POLICY [ IF EXISTS ] <name> SET
  TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER SESSION POLICY [ IF EXISTS ] <name> UNSET TAG <tag_name> [ , <tag_name> ... ]

ALTER SESSION POLICY [ IF EXISTS ] <name> UNSET
  [ SESSION_IDLE_TIMEOUT_MINS ]
  [ SESSION_UI_IDLE_TIMEOUT_MINS ]
  [ ALLOWED_SECONDARY_ROLES ]
  [ BLOCKED_SECONDARY_ROLES ]
  [ COMMENT ]
```

## Parameters

`name`
:   Identifier for the session policy; must be unique for your account.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire identifier
    string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`RENAME TO new_name`
:   Specifies the new identifier for the session policy; must be unique for your account.

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
:   Specifies one or more parameters to set for the session policy separated by blank spaces, commas, or new lines.

    `SESSION_IDLE_TIMEOUT_MINS = integer`
    :   For Snowflake clients and programmatic clients, the number of minutes in which a session can be idle before users must authenticate to
        Snowflake again. If a value is not specified, Snowflake uses the default value.

        The number of minutes can be any integer between `5` and `1440`, inclusive.

        Default: `240` (4 hours)

    `SESSION_UI_IDLE_TIMEOUT_MINS = integer`
    :   For Snowsight, the number of minutes in which a session can be idle before a user must authenticate to Snowflake again. If a
        value is not specified, Snowflake uses the default value.

        The number of minutes can be any integer between `5` and `1440`, inclusive.

        Default: `240` (4 hours)

    `ALLOWED_SECONDARY_ROLES = ( [ { 'ALL' | role_name [ , role_name ... ] } ] )`
    :   Specifies the secondary roles for a session policy, if any.

        The possible values for the property are:

        `()`
        :   Disallows secondary roles.

        `('ALL')`
        :   Allows all secondary roles.

        `( role_name [ , role_name ... ] )`
        :   Allows the specified roles as secondary roles. The secondary roles can be user-defined account roles or system roles. Specify the
            role name as it is stored in Snowflake. For details, see [Identifier requirements](../identifiers-syntax.md).

        Default: `('ALL')`. If you unset this property, its value in the output of a [DESCRIBE SESSION POLICY](desc-session-policy.md) command is `'ALL'`.

    `BLOCKED_SECONDARY_ROLES = ( [ { 'ALL' | role_name [ , role_name ... ] } ] )`
    :   Specifies the blocked secondary roles for a session policy, if any. Blocked secondary roles take precedence over
        allowed secondary roles.

        The possible values for the property are:

        `()`
        :   Allows all secondary roles.

        `('ALL')`
        :   Disallows secondary roles.

        `( role_name [ , role_name ... ] )`
        :   Blocks the specified roles as secondary roles. The specified roles, and the roles granted to those roles, cannot be
            activated as secondary roles. These blocked roles can be user-defined account roles or system roles. Specify the
            role name as it is stored in Snowflake. For details, see [Identifier requirements](../identifiers-syntax.md).

        Default: `()`. If you unset this property, its value in the output of a [DESCRIBE SESSION POLICY](desc-session-policy.md) command is
        `'()'`.

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites an existing comment for the session policy.

    `TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
    :   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

        The tag value is always a string, and the maximum number of characters for the tag value is 256.

        For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`UNSET ...`
:   Specifies one or more parameters to unset for the session policy, which resets them to the system defaults.

    You can reset multiple properties with a single ALTER statement. Each property must be separated by a comma. When
    resetting a property, specify only the name. Specifying a value for the property will return an error.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Session policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For additional details on session policy DDL and privileges, see [Managing session policies](../../user-guide/session-policies-managing.md).

## Usage notes

* If you want to update an existing session policy and need to see the current definition of the policy, call the
  [GET_DDL](../functions/get_ddl.md) function or run the [DESCRIBE SESSION POLICY](desc-session-policy.md) command.
* Before executing an ALTER statement, you can execute a DESCRIBE SESSION POLICY statement to determine the attribute values of the policy.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

The following example updates the session policy to have a Snowsight session timeout value of `15` minutes.

```sqlexample
DESC SESSION POLICY session_policy_prod_1;
```

```output
+---------------------------------+-----------------------+------------------------+--------------------------+--------------------------------------------------+
| createdOn                       | name                  | sessionIdleTimeoutMins | sessionUIIdleTimeoutMins | comment                                          |
+---------------------------------+-----------------------+------------------------+--------------------------+--------------------------------------------------+
| Mon, 11 Jan 2021 00:00:00 -0700 | session_policy_prod_1 | 30                     | 30                       | session policy for use in the prod_1 environment |
+---------------------------------+-----------------------+------------------------+--------------------------+--------------------------------------------------+
```

```sqlexample
ALTER SESSION POLICY session_policy_prod_1 SET SESSION_UI_IDLE_TIMEOUT_MINS = 15;
```
