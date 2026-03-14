# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-contact.md

# ALTER CONTACT

Modifies the properties of an existing [contact](../../user-guide/contacts-using.md).

See also:
:   [CREATE CONTACT](create-contact.md) , [DROP CONTACT](drop-contact.md) , [SHOW CONTACTS](show-contacts.md)

## Syntax

```sqlsyntax
ALTER CONTACT [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER CONTACT [ IF EXISTS ] <name> SET
  [ {
    USERS = ( '<user_name>' [ , '<user_name>' ... ] )
    | EMAIL_DISTRIBUTION_LIST = '<email>'
    | URL = '<url>'
    } ]
  [ COMMENT = '<string_literal>' ]
```

## Parameters

`name`
:   Specifies the identifier for the contact to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`RENAME TO new_name`
:   Changes the name of the contact to `new_name`. The new identifier must be unique for the schema.

    For more information about identifiers, see [Identifier requirements](../identifiers-syntax.md).

    You can move the object to a different database and/or schema while optionally renaming the object. To do so, specify
    a qualified `new_name` value that includes the new database and/or schema name in the form
    `db_name.schema_name.object_name` or `schema_name.object_name`, respectively.

    > **Note:**
    >
    > * The destination database and/or schema must already exist. In addition, an object with the same name cannot already
    >   exist in the new location; otherwise, the statement returns an error.
    > * Moving an object to a managed access schema is prohibited unless the object owner (that is, the role that has
    >   the OWNERSHIP privilege on the object) also owns the target schema.

    When a contact is renamed, other objects that reference it must be updated with the new name.

`SET ...`
:   Sets one of the following parameters for the contact:

    `USERS = ( 'user_name' [ , 'user_name' ... ] )`
    :   Comma-delimited list of Snowflake users who can be contacted, specified by the name of their user objects.

        If the user name is case-sensitive or includes any special characters or spaces, double quotes are required. The double quotes must be
        enclosed within the single quotes. For example, if the user is `joe@example.com`, you must specify `'"joe@example.com"'`.

    `EMAIL_DISTRIBUTION_LIST = 'email'`
    :   A valid email address, which can be a distribution list if you want users to be able to contact more than one individual.

    `URL = 'url'`
    :   A URL that can be used to contact people about an object.

    `COMMENT = '<string_literal>'`
    :   A user-defined string. Specifies a comment for the contact.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| MODIFY | Contact |  |
| OWNERSHIP | Contact | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

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

```sqlexample
ALTER CONTACT my_contact SET EMAIL_DISTRIBUTION_LIST = 'support@example.com';
```
