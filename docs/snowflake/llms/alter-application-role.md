# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-application-role.md

# ALTER APPLICATION ROLE

Modifies the properties for an existing application role.

See also:
:   [CREATE APPLICATION ROLE](create-application-role.md), [GRANT APPLICATION ROLE](grant-application-role.md),
    [REVOKE APPLICATION ROLE](revoke-application-role.md), [SHOW APPLICATION ROLES](show-application-roles.md)

## Syntax

```sqlsyntax
ALTER APPLICATION ROLE [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER APPLICATION ROLE [ IF EXISTS ] <name> SET COMMENT = '<string_literal>'

ALTER APPLICATION ROLE [ IF EXISTS ] <name> UNSET COMMENT
```

## Parameters

`name`
:   Specifies the identifier for the application role. If the identifier contains spaces or
    special characters, the entire string must be enclosed in double quotes. Identifiers enclosed
    in double quotes are also case-sensitive.

`RENAME TO new_name`
:   Specifies the new identifier for the application role. The identifier must be unique
    for within the application.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

    Note that when specifying the fully-qualified name of the application role, you cannot specify a
    different application. The name of the application, `application_name`, must remain the same.
    Only the `application_role_name` can change during a rename operation.

`SET ...`
:   Specifies the properties to set for the application role:

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites an existing comment for the application role.

`UNSET ...`
:   Specifies the properties to unset for the application role, which resets them to the defaults.

    * `COMMENT`

## Usage notes

* This command can only be run in the context of an application created using the Native
  Apps Framework.
* Only the application role owner (i.e. the role with the OWNERSHIP privilege on the application
  role), or a higher role, can run this command.
* Renaming an application role is only allowed within the same application.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

```sqlexample
ALTER APPLICATION ROLE app_role RENAME TO new_app_role;
```

```sqlexample
ALTER APPLICATION ROLE app_role SET
  COMMENT = 'Application role for the Hello Snowflake application.';
```

```sqlexample
ALTER APPLICATION ROLE app_role UNSET COMMENT;
```
