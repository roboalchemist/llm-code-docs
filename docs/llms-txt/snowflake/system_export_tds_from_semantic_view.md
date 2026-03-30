# Source: https://docs.snowflake.com/en/sql-reference/functions/system_export_tds_from_semantic_view.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$EXPORT_TDS_FROM_SEMANTIC_VIEW

Returns a [semantic view](../../user-guide/views-semantic/overview.md) in Tableau Data Source (TDS) format.

## Syntax

```sqlsyntax
SYSTEM$EXPORT_TDS_FROM_SEMANTIC_VIEW( '<semantic_view_name>' )
```

## Arguments

`'semantic_view_name'`
:   Name of the semantic view to export.

    If the semantic view is not in the current schema and database, specify the
    [fully-qualified name of the view](../name-resolution.md) (for example, `my_db.my_schema.my_semantic_view`).

## Returns

Returns a VARCHAR value containing the semantic view in TDS format.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| Any | Semantic view |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

For details about the conversion process and limitations with the conversion, see [Exporting a semantic view to a Tableau Data Source (TDS) file](../../user-guide/views-semantic/sql.md).

## Examples

The following statement returns the semantic view `my_sv` in TDS format:

```sqlexample
SELECT SYSTEM$EXPORT_TDS_FROM_SEMANTIC_VIEW('my_sv');
```

```output
+------------------------------------------------------------------------+
| SYSTEM$EXPORT_TDS_FROM_SEMANTIC_VIEW('MY_SV')                          |
|------------------------------------------------------------------------|
| <?xml version="1.0" encoding="UTF-8"?>                                 |
| <!--Tableau compatibility notice:                                      |
| ... -->                                                                |
| <datasource xmlns:user="http://www.tableausoftware.com/xml/user" ... > |
| ...                                                                    |
+------------------------------------------------------------------------+
```
