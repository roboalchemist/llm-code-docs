# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/file_formats.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/file_formats.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/file_formats.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# FILE_FORMATS view

This Account Usage view displays a row for each file format defined in the account.

File formats are named objects that can be used for loading/unloading data. For more information, see [CREATE FILE FORMAT](../sql/create-file-format.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| FILE_FORMAT_ID | NUMBER | Internal/system-generated identifier for the file format. |
| FILE_FORMAT_NAME | VARCHAR | Name of the file format, |
| FILE_FORMAT_SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema of the file format. |
| FILE_FORMAT_SCHEMA | VARCHAR | Schema that the file format belongs to. |
| FILE_FORMAT_CATALOG_ID | NUMBER | Internal/system-generated identifier for the database of the file format. |
| FILE_FORMAT_CATALOG | VARCHAR | Database that the file format belongs to. |
| FILE_FORMAT_OWNER | VARCHAR | Name of the role that owns the file format. |
| FILE_FORMAT_TYPE | VARCHAR | File format type of the file format (`CSV`, `JSON`, etc.). |
| RECORD_DELIMITER | VARCHAR | Character that separates records. |
| FIELD_DELIMITER | VARCHAR | Character that separates fields. |
| SKIP_HEADER | NUMBER | Number of lines skipped at the start of the file. |
| DATE_FORMAT | VARCHAR | Date format. |
| TIME_FORMAT | VARCHAR | Time format. |
| TIMESTAMP_FORMAT | VARCHAR | Timestamp format. |
| BINARY_FORMAT | VARCHAR | Binary format. |
| ESCAPE | VARCHAR | String used as the escape character for any field values. |
| ESCAPE_UNENCLOSED_FIELD | VARCHAR | String used as the escape character for unenclosed field values. |
| TRIM_SPACE | BOOLEAN | Whether whitespace is removed from fields. |
| FIELD_OPTIONALLY_ENCLOSED_BY | VARCHAR | Character used to enclose strings. |
| NULL_IF | VARCHAR | A list of strings to be replaced by null. |
| COMPRESSION | VARCHAR | Compression method for the data file. |
| ERROR_ON_COLUMN_COUNT_MISMATCH | VARCHAR | Whether to generate a parsing error if the number of fields in an input file does not match the number of columns in the corresponding table. |
| CREATED | TIMESTAMP_LTZ | Date and time when the file format was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| DELETED | TIMESTAMP_LTZ | Date and time when the file format was dropped. |
| COMMENT | VARCHAR | Comment for the file format. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The view only displays objects for which the current role for the session has been granted access privileges.
* The view does not recognize the MANAGE GRANTS privilege and consequently may show less information compared to a SHOW command executed by a user who holds the MANAGE GRANTS privilege.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.
