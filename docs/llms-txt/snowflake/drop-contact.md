# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-contact.md

# DROP CONTACT

Removes the specified [contact](../../user-guide/contacts-using.md) from the current schema.

See also:
:   [CREATE CONTACT](create-contact.md) , [ALTER CONTACT](alter-contact.md), [SHOW CONTACTS](show-contacts.md)

## Syntax

```sqlsyntax
DROP CONTACT <name>
```

## Parameters

`name`
:   Specifies the identifier of the contact to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

You must have the OWNERSHIP privilege on a contact to drop it.

## Examples

The following example drops the contact named `mycontact`:

```sqlexample
DROP CONTACT mycontact;
```

```output
+---------------------------------+
| status                          |
|---------------------------------|
| MYCONTACT successfully dropped. |
+---------------------------------+
```
