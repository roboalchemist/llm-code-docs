# Source: https://docs.snowflake.com/en/sql-reference/data-types-unsupported.md

# Unsupported data types

Snowflake doesn’t support the following data types:

| Category | Type | Notes |
| --- | --- | --- |
| LOB (Large Object) | BLOB | BINARY can be used instead; maximum of 67108864 bytes. For more information, see [String & binary data types](data-types-text.md). |
| CLOB | VARCHAR can be used instead; maximum of 134217728 bytes (for singlebyte). For more information, see [String & binary data types](data-types-text.md). |
| Other | ENUM |  |
| User-defined data types |  |
