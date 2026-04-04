# Source: https://docs.snowflake.com/en/sql-reference/info-schema/element_types.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/element_types.md

Schemas:
:   [ACCOUNT_USAGE](../account-usage.md)

# ELEMENT_TYPES view

This Account Usage view displays a row for each [structured ARRAY type](../data-types-structured.md) in an
object (a column in a table) in the account.

Each row describes the type of the element in the structured ARRAY.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| COLLECTION_TYPE_IDENTIFIER | VARCHAR | Type identifier. Use this to join on:   *The DTD_IDENTIFIER column in the [COLUMNS view](../info-schema/columns.md).* The DTD_IDENTIFIER column in this view (for nested types). * The DTD_IDENTIFIER column in the [FIELDS view](../info-schema/fields.md) (for nested types). |
| OBJECT_ID | VARCHAR | Internal/system-generated identifier for the object that uses this ARRAY type (e.g. name of a table). |
| OBJECT_NAME | VARCHAR | Name of the object that uses this ARRAY type (e.g. name of a table). |
| OBJECT_TYPE | VARCHAR | Type of the object that uses this ARRAY type:   * TABLE (if used by a column) |
| OBJECT_SCHEMA_ID | VARCHAR | Internal/system-generated identifier for the schema of the object that uses this ARRAY type. |
| OBJECT_SCHEMA | VARCHAR | Schema that contains the object that uses this ARRAY type. |
| OBJECT_CATALOG_ID | VARCHAR | Internal/system-generated identifier for the database of the object that uses this ARRAY type. |
| OBJECT_CATALOG | VARCHAR | Database that contains the object that uses this ARRAY type. |
| DATA_TYPE | VARCHAR | Data type of the element. |
| CHARACTER_MAXIMUM_LENGTH | NUMBER | Maximum length in characters of string elements. |
| CHARACTER_OCTET_LENGTH | NUMBER | Maximum length in bytes of string elements. |
| NUMERIC_PRECISION | NUMBER | Numeric precision of numeric elements. |
| NUMERIC_PRECISION_RADIX | NUMBER | Radix of precision of numeric elements. |
| NUMERIC_SCALE | NUMBER | Scale of numeric elements. |
| DATETIME_PRECISION | NUMBER | Not applicable for Snowflake. |
| INTERVAL_TYPE | VARCHAR | Not applicable for Snowflake. |
| INTERVAL_PRECISION | NUMBER | Not applicable for Snowflake. |
| CHARACTER_SET_CATALOG | VARCHAR | Not applicable for Snowflake. |
| CHARACTER_SET_SCHEMA | VARCHAR | Not applicable for Snowflake. |
| CHARACTER_SET_NAME | VARCHAR | Not applicable for Snowflake. |
| COLLATION_CATALOG | VARCHAR | Not applicable for Snowflake. |
| COLLATION_SCHEMA | VARCHAR | Not applicable for Snowflake. |
| COLLATION_NAME | VARCHAR | The collation specification for this element |
| UDT_CATALOG | VARCHAR | Not applicable for Snowflake. |
| UDT_SCHEMA | VARCHAR | Not applicable for Snowflake. |
| UDT_NAME | VARCHAR | Not applicable for Snowflake. |
| SCOPE_CATALOG | VARCHAR | Not applicable for Snowflake. |
| SCOPE_SCHEMA | VARCHAR | Not applicable for Snowflake. |
| SCOPE_NAME | VARCHAR | Not applicable for Snowflake. |
| MAXIMUM_CARDINALITY | NUMBER | Maximum cardinality. Currently, this is always set to NULL. |
| DTD_IDENTIFIER | VARCHAR | Nested type identifier. Use this to join on:   *The COLLECTION_TYPE_IDENTIFIER column in this view.* The ROW_IDENTIFIER column in the [FIELDS view](../info-schema/fields.md) (for nested types). |
| IS_NULLABLE | VARCHAR | `Y` if the structured ARRAY allows NULL values; `N` otherwise. |
| DELETED | TIMESTAMP_LTZ | Date and time when the object was dropped. |

## Usage notes

* Latency for the view may be up to 90 minutes.

* The view only displays objects for which the current role for the session has been granted access privileges.
* The view does not honor the MANAGE GRANTS privilege and consequently may show less information compared to a SHOW command
  executed by a user who holds the MANAGE GRANTS privilege.
