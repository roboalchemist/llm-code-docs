# Source: https://docs.snowflake.com/en/migrations/sma-docs/translation-reference/spark-sql/supported-functions.md

# Snowpark Migration Accelerator: Supported functions

## Strings

| Function | Status |
| --- | --- |
| CONCAT | SUPPORTED |
| LEFT | SUPPORTED |
| LOWER | SUPPORTED |
| SPLIT | SUPPORTED |
| SUBSTRING | SUPPORTED |
| SUBSTRING_INDEX | PENDING |
| TRIM | SUPPORTED |
| UPPER | SUPPORTED |

### Numerics

| Function | Status |
| --- | --- |
| COUNT | SUPPORTED |
| LAST | PENDING |
| MAX | SUPPORTED |
| MIN | SUPPORTED |
| ROUND | SUPPORTED |
| SUM | SUPPORTED |

### Date

| Function | Status |
| --- | --- |
| CURRENT_DATE | SUPPORTED |
| CURRENT_TIMESTAMP | SUPPORTED |
| DATEDIFF | PENDING |
| DATE_SUB | PENDING |
| DAY | SUPPORTED |
| FIRST_VALUE | PENDING |
| FROM_UNIXTIME | PENDING |
| TO_DATE | SUPPORTED |
| WEEKOFYEAR | SUPPORTED |

### Advanced functions

| Function | Status |
| --- | --- |
| COALESCE | SUPPORTED |
| EXPLODE | PENDING |
| IFNULL | SUPPORTERD |
| MERGE | PENDING |
| POSEXPLODE | PENDING |
| ROW_NUMBER | SUPPORTED |
