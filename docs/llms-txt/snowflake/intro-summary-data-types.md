# Source: https://docs.snowflake.com/en/sql-reference/intro-summary-data-types.md

# Summary of data types

Snowflake supports most SQL data types. The following table provides a summary of the supported data types:

| Category | Type | Notes |
| --- | --- | --- |
| [Numeric data types](data-types-numeric.md) | NUMBER | Default precision and scale are (38,0). |
|  | DECIMAL, NUMERIC | Synonymous with NUMBER. |
|  | INT, INTEGER, BIGINT, SMALLINT, TINYINT, BYTEINT | Synonymous with NUMBER, except precision and scale can’t be specified. |
|  | FLOAT, FLOAT4, FLOAT8 | [1] |
|  | DOUBLE, DOUBLE PRECISION, REAL | Synonymous with FLOAT. [1] |
|  | DECFLOAT | Stores numbers exactly, with up to 38 significant digits of precision, and uses a dynamic base-10 exponent. |
| [String & binary data types](data-types-text.md) | VARCHAR | Default length is 16777216 bytes. Maximum length is 134217728 bytes. |
|  | CHAR, CHARACTER | Synonymous with VARCHAR, except the default length is VARCHAR(1). |
|  | STRING, TEXT | Synonymous with VARCHAR. |
|  | BINARY |  |
|  | VARBINARY | Synonymous with BINARY. |
| [Logical data types](data-types-logical.md) | BOOLEAN | Currently only supported for accounts provisioned after January 25, 2016. |
| [Date & time data types](data-types-datetime.md) | DATE |  |
|  | DATETIME | Synonymous with TIMESTAMP_NTZ. |
|  | TIME |  |
|  | TIMESTAMP | Alias for one of the TIMESTAMP variations (TIMESTAMP_NTZ by default). |
|  | TIMESTAMP_LTZ | TIMESTAMP with local time zone; time zone, if provided, isn’t stored. |
|  | TIMESTAMP_NTZ | TIMESTAMP with no time zone; time zone, if provided, isn’t stored. |
|  | TIMESTAMP_TZ | TIMESTAMP with time zone. |
| [Semi-structured data types](data-types-semistructured.md) | VARIANT |  |
|  | OBJECT |  |
|  | ARRAY |  |
| [Structured data types](data-types-structured.md) | ARRAY |  |
|  | OBJECT |  |
|  | MAP |  |
| [Unstructured data types](data-types-unstructured.md) | FILE | See [Introduction to unstructured data](../user-guide/unstructured-intro.md). |
| [Geospatial data types](data-types-geospatial.md) | GEOGRAPHY |  |
|  | GEOMETRY |  |
| [UUID data type](data-types-uuid.md) | UUID |  |
| [Vector data types](data-types-vector.md) | VECTOR |  |

[1] A known issue in Snowflake displays FLOAT, FLOAT4, FLOAT8, REAL, DOUBLE, and DOUBLE PRECISION as FLOAT, even though they are stored as DOUBLE.
