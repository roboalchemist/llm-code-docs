# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/connectors/sql-server/data-mapping.md

# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/connectors/postgres/data-mapping.md

# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/connectors/oracle/data-mapping.md

# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/connectors/mysql/data-mapping.md

# Openflow Connector for MySQL: Data mapping

> **Note:**
>
> This connector is subject to the [Snowflake Connector Terms](https://www.snowflake.com/legal/snowflake-connector-terms/).

This topic describes MySQL data types are mapped
to Snowflake data types.

## MySQL to Snowflake data type mapping

The following table shows how MySQL data types are mapped to Snowflake data types
when replicating data.

| MySQL type | Snowflake type | Notes |
| --- | --- | --- |
| DECIMAL / NUMERIC | NUMBER | The maximum number of digits in DECIMAL format for MySQL is 65. For Snowflake, the maximum is 38. Precision is lost when exceeded. |
| INT / INTEGER | INT |  |
| TINYINT / BOOL | INT |  |
| SMALLINT | INT |  |
| MEDIUMINT | INT |  |
| BIGINT | INT |  |
| YEAR | INT |  |
| FLOAT | FLOAT |  |
| DOUBLE | FLOAT |  |
| VARCHAR | TEXT |  |
| CHAR | TEXT | Trailing spaces are not preserved. |
| TINYTEXT | TEXT |  |
| TEXT | TEXT |  |
| MEDIUMTEXT | TEXT | Supported up to the maximum entry size in Snowflake (16 MB). |
| LONGTEXT | TEXT | Supported up to the maximum entry size in Snowflake (16 MB). |
| ENUM | TEXT | Stored as a string value. For example, for `ENUM('one', 'two')` the possible values are `'one'` and `'two'`. |
| SET | TEXT | Stored as a comma-separated string in column declaration order. For example, for `SET('one', 'two')` the possible values are `''`, `'one'`, `'two'`, and `'one,two'`. |
| BIT | TEXT | Represented as a hexadecimal string. For example: `'83060c183060c183'`. |
| DATE | DATE |  |
| DATETIME | TIMESTAMP_NTZ |  |
| TIMESTAMP | TIMESTAMP_TZ | Values are stored in UTC. |
| TIME | TIME |  |
| BINARY | BINARY |  |
| VARBINARY | BINARY |  |
| TINYBLOB | BINARY |  |
| BLOB | BINARY |  |
| MEDIUMBLOB | BINARY | Supported up to the maximum entry size in Snowflake (16 MB). |
| LONGBLOB | BINARY | Supported up to the maximum entry size in Snowflake (16 MB). |
| JSON | VARIANT | Supported up to the maximum entry size in Snowflake (16 MB). |

> **Note:**
>
> Any MySQL data types not listed in this table are mapped to TEXT by default.
