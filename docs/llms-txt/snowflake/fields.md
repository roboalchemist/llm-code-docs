# Source: https://docs.snowflake.com/en/sql-reference/info-schema/fields.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/fields.md

Schemas:
:   [ACCOUNT_USAGE](../account-usage.md)

# FIELDS view

This Account Usage view displays a row for each field in a [structured OBJECT type](../data-types-structured.md)
and a row for the key and value in a [MAP](../data-types-structured.md) in an object (a column in a table) in the
account.

For MAPs, the view contains separate rows for the key and value.

Each row describes the type of the element in the structured ARRAY.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ROW_IDENTIFIER | VARCHAR | Type identifier. Use this to join on:   *The DTD_IDENTIFIER column in the [COLUMNS view](../info-schema/columns.md).* The DTD_IDENTIFIER column in the [ELEMENT_TYPES view](../info-schema/element_types.md) (for nested types). * The DTD_IDENTIFIER column in this view (for nested types). |
| FIELD_NAME | VARCHAR | One of the following values:   *For structured OBJECTs, the name of the key.* For MAPs, KEY for the key or VALUE for the value. |
| OBJECT_ID | VARCHAR | Internal/system-generated identifier for the object that uses this OBJECT or MAP type (e.g. name of a table). |
| OBJECT_NAME | VARCHAR | Name of the object that uses this OBJECT or MAP type (e.g. name of a table). |
| OBJECT_TYPE | VARCHAR | Type of the object that uses this OBJECT or MAP type:   * TABLE (if used by a column) |
| OBJECT_SCHEMA_ID | VARCHAR | Internal/system-generated identifier for the schema for the object that uses this OBJECT or MAP type. |
| OBJECT_SCHEMA | VARCHAR | Schema that contains the object that uses this OBJECT or MAP type. |
| OBJECT_CATALOG_ID | VARCHAR | Internal/system-generated identifier for the database for the object that uses this OBJECT or MAP type. |
| OBJECT_CATALOG | VARCHAR | Database that contains the object that uses this OBJECT or MAP type. |
| ORDINAL_POSITION | NUMBER | The ordinal position of the key in the OBJECT or MAP. The position is 1-based.  For MAPs, the ordinal position of the key is 1, and the ordinal position of the value is 2. |
| DATA_TYPE | VARCHAR | Data type of the value (for OBJECTs) or the key or value (for MAPs). |
| CHARACTER_MAXIMUM_LENGTH | NUMBER | Maximum length in characters of string keys or values. |
| CHARACTER_OCTET_LENGTH | NUMBER | Maximum length in bytes of string keys or values. |
| NUMERIC_PRECISION | NUMBER | Numeric precision of numeric keys or values. |
| NUMERIC_PRECISION_RADIX | NUMBER | Radix of precision of numeric keys or values. |
| NUMERIC_SCALE | NUMBER | Scale of numeric keys or values. |
| DATETIME_PRECISION | NUMBER | Not applicable for Snowflake. |
| INTERVAL_TYPE | VARCHAR | Not applicable for Snowflake. |
| INTERVAL_PRECISION | NUMBER | Not applicable for Snowflake. |
| CHARACTER_SET_CATALOG | VARCHAR | Not applicable for Snowflake. |
| CHARACTER_SET_SCHEMA | VARCHAR | Not applicable for Snowflake. |
| CHARACTER_SET_NAME | VARCHAR | Not applicable for Snowflake. |
| COLLATION_CATALOG | VARCHAR | Not applicable for Snowflake. |
| COLLATION_SCHEMA | VARCHAR | Not applicable for Snowflake. |
| COLLATION_NAME | VARCHAR | The collation specification for this keys or values. |
| UDT_CATALOG | VARCHAR | Not applicable for Snowflake. |
| UDT_SCHEMA | VARCHAR | Not applicable for Snowflake. |
| UDT_NAME | VARCHAR | Not applicable for Snowflake. |
| SCOPE_CATALOG | VARCHAR | Not applicable for Snowflake. |
| SCOPE_SCHEMA | VARCHAR | Not applicable for Snowflake. |
| SCOPE_NAME | VARCHAR | Not applicable for Snowflake. |
| MAXIMUM_CARDINALITY | NUMBER | Maximum cardinality. Currently, this is always set to NULL. |
| DTD_IDENTIFIER | VARCHAR | Nested type identifier. Use this to join on:   *The COLLECTION_TYPE_IDENTIFIER column in the [ELEMENT_TYPES view](../info-schema/element_types.md).* The ROW_IDENTIFIER column in this view (for nested types). |
| IS_NULLABLE | VARCHAR | `Y` if the structured OBJECT or MAP allows NULL values; `N` otherwise. |
| DELETED | TIMESTAMP_LTZ | Date and time when the object was dropped. |

## Usage notes

* Latency for the view may be up to 90 minutes.

* The view only displays objects for which the current role for the session has been granted access privileges.
* The view does not honor the MANAGE GRANTS privilege and consequently may show less information compared to a SHOW command
  executed by a user who holds the MANAGE GRANTS privilege.
