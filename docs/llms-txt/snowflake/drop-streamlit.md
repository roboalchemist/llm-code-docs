# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-streamlit.md

# DROP STREAMLIT

Removes the specified Streamlit object from the current/specified schema.

See also:
:   [CREATE STREAMLIT](create-streamlit.md), [SHOW STREAMLITS](show-streamlits.md), [DESCRIBE STREAMLIT](desc-streamlit.md), [UNDROP STREAMLIT](undrop-streamlit.md), [ALTER STREAMLIT](alter-streamlit.md)

## Syntax

```sqlsyntax
DROP STREAMLIT [IF EXISTS] <name>
```

## Required parameters

`name`
:   Specifies the identifier for the Streamlit object to drop. If the identifier contains spaces, special characters, or
    mixed-case characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are
    also case-sensitive (e.g. `"My Object"`).

    If the Streamlit object identifier is not fully-qualified (in the form of
    `db_name.schema_name.streamlit_name` or `schema_name.streamlit_name`), the command looks for
    the Streamlit object in the current schema for the session.

## Access control requirements

Your role must have the following [privileges](../../user-guide/security-access-control-overview.md) on objects:

| Privilege | Object |
| --- | --- |
| OWNERSHIP | Streamlit object that you remove |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* For Streamlit objects created using ROOT_LOCATION, this command does not drop the underlying stage because
  the owner of the Streamlit object may not be the owner of the stage. Additionally, multiple Streamlit objects
  may point to the same stage. If you need to drop the corresponding stage, use the [DROP STAGE](drop-stage.md) command.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.
