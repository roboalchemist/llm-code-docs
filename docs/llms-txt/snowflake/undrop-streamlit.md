# Source: https://docs.snowflake.com/en/sql-reference/sql/undrop-streamlit.md

# UNDROP STREAMLIT

Restores the most recent version of a dropped Streamlit object.

See also:
:   [CREATE STREAMLIT](create-streamlit.md) , [ALTER STREAMLIT](alter-streamlit.md) , [DROP STREAMLIT](drop-streamlit.md) , [SHOW STREAMLITS](show-streamlits.md) , [DESCRIBE STREAMLIT](desc-streamlit.md)

## Syntax

```sqlsyntax
UNDROP STREAMLIT <name>
```

## Parameters

`name`
:   Specifies the identifier for the Streamlit object to restore.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

If your role does not own the objects in the following table, then your role
must have the listed
[privileges](../../user-guide/security-access-control-overview.md) on those objects:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Streamlit object that you restore |  |
| CREATE STREAMLIT | Schema where you restore the Streamlit object |  |
| USAGE | Warehouse used by the Streamlit app |  |
| USAGE | Compute pool used by the Streamlit app | This privilege is only required if your app has a COMPUTE_POOL. |
| USAGE | External access integrations used by the Streamlit app | This privilege is only required if your app has EXTERNAL_ACCESS_INTEGRATIONS. |
| USAGE | Secrets used by the Streamlit app | This privilege is only required if your app has SECRETS. |
| CREATE STAGE | Schema where you restore the Streamlit object | This privilege is only required to undrop Streamlit objects that were created with the legacy ROOT_LOCATION parameter. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Streamlit object can only be restored to the database and schema that contained the Streamlit object at the time of deletion.
* If a Streamlit with the same name already exists, an error is returned.

* UNDROP relies on the Snowflake [Time Travel](../../user-guide/data-time-travel.md) feature. An object can be restored only if
  the object was deleted within the [Data retention period](../../user-guide/data-time-travel.md). The default value is 24 hours.

## Example

The following example restores the most recent version of a dropped Streamlit named `hello_streamlit`:

```sqlexample
UNDROP STREAMLIT hello_streamlit;
```
