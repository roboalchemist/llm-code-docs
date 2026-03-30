# Source: https://docs.snowflake.com/en/sql-reference/sql/create-contact.md

# CREATE CONTACT

Creates a new [contact](../../user-guide/contacts-using.md) or replaces an existing contact.

See also:
:   [ALTER CONTACT](alter-contact.md) , [DROP CONTACT](drop-contact.md) , [SHOW CONTACTS](show-contacts.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] CONTACT [ IF NOT EXISTS ] <name>
  [ {
    USERS = ( '<user-name>' [ , '<user_name>' ... ] )
    | EMAIL_DISTRIBUTION_LIST = '<email>'
    | URL = '<url>'
    } ]
  [ COMMENT = '<string_literal>' ]
```

## Required parameters

`name`
:   Specifies the name of the new contact.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`USERS = ( 'user_name' [ , 'user_name' ... ] )`
:   Comma-delimited list of Snowflake users who can be contacted, specified by the name of their user objects.

    If the user name is case-sensitive or includes any special characters or spaces, double quotes are required. The double quotes must be
    enclosed within the single quotes. For example, if the user is `joe@example.com`, you must specify `'"joe@example.com"'`.

`EMAIL_DISTRIBUTION_LIST = 'email'`
:   A valid email address, which can be a distribution list if you want users to be able to contact more than one individual.

`URL = 'url'`
:   A URL that can be used to contact people about an object.

`COMMENT`
:   A user-defined string. Specifies a comment for the contact.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE CONTACT | Schema |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Examples

```sqlexample
CREATE CONTACT my_contact
  EMAIL_DISTRIBUTION_LIST = 'company_support@example.com';
```
