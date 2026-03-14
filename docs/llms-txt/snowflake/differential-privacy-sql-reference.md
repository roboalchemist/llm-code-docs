# Source: https://docs.snowflake.com/en/user-guide/diff-privacy/differential-privacy-sql-reference.md

# Differential privacy SQL reference

This topic provides the following information:

* A reference for the SQL functions that are unique to differential privacy.
* A list of the Snowflake data types, operators, query syntax, and functions that are supported by differential privacy.

## Differential privacy functions

The following functions are unique to differential privacy.

| Function | Description |
| --- | --- |
| [DP_INTERVAL_LOW](../../sql-reference/functions/dp_interval_low.md) | Returns the lower bound of the noise interval. |
| [DP_INTERVAL_HIGH](../../sql-reference/functions/dp_interval_high.md) | Returns the upper bound of the noise interval. |

## Data types

The following [data types](../../sql-reference-data-types.md) are supported.

| Data type | Notes |
| --- | --- |
| BOOLEAN |  |
| CHAR, CHARACTER |  |
| DATE |  |
| DATETIME |  |
| DECIMAL, NUMERIC |  |
| DOUBLE, DOUBLE PRECISION, REAL |  |
| FLOAT, FLOAT4, FLOAT8 |  |
| INT, INTEGER , BIGINT, SMALLINT, TINYINT, BYTEINT |  |
| NUMBER |  |
| STRING |  |
| TEXT |  |
| TIME |  |
| TIMESTAMP, TIMESTAMP_NTZ | Time data types with time zones are not supported. Use TIMESTAMP or TIMESTAMP_NTZ. |
| VARCHAR |  |

## Query syntax

The following elements of the Snowflake [query syntax](../../sql-reference/constructs.md) are supported.

| Syntax | Notes |
| --- | --- |
| SELECT |  |
| SELECT ALL |  |
| FROM |  |
| INNER JOIN ON | See [Supported joins](differential-privacy-analyst.md). |
| INNER JOIN USING | See [Supported joins](differential-privacy-analyst.md). |
| LEFT OUTER JOIN ON | See [Supported joins](differential-privacy-analyst.md). |
| LEFT OUTER JOIN USING | See [Supported joins](differential-privacy-analyst.md). |
| RIGHT OUTER JOIN ON | See [Supported joins](differential-privacy-analyst.md). |
| RIGHT OUTER JOIN USING | See [Supported joins](differential-privacy-analyst.md). |
| FULL OUTER JOIN ON | See [Supported joins](differential-privacy-analyst.md). |
| FULL OUTER JOIN USING | See [Supported joins](differential-privacy-analyst.md). |
| NATURAL JOIN | See [Supported joins](differential-privacy-analyst.md). |
| WHERE |  |
| GROUP BY | Aliases are not supported in the GROUP BY clause. For example, `GROUP BY col_a AS column_a` is not supported. |

Limitations on query syntax
:   Quoted identifiers (for example, column, table, schema and database names) are not supported.

## Operators

### Arithmetic operators

The following [arithmetic operators](../../sql-reference/operators-arithmetic.md) are supported.

| Operator | Notes |
| --- | --- |
| `-` (unary) |  |
| `-` |  |
| `+` (unary) | Does not work with strings. |
| `+` |  |
| `*` |  |
| `/` |  |
| `%` |  |

### Comparison operators

The following [comparison operators](../../sql-reference/operators-comparison.md) are supported.

| Operator | Notes |
| --- | --- |
| `=` |  |
| `!=` |  |
| `<` |  |
| `>` |  |
| `<=` |  |
| `>=` |  |

### Logical operators

The following [logical operators](../../sql-reference/operators-logical.md) are supported.

| Operator | Notes |
| --- | --- |
| AND |  |
| NOT |  |
| OR |  |

### Set operators

The following [set operators](../../sql-reference/operators-query.md) are supported.

| Operator | Notes |
| --- | --- |
| UNION [ ALL ] |  |

### Subquery operators

[Subquery operators](../../sql-reference/operators-subquery.md) are not supported.

## Functions

### Aggregate functions

The following [aggregate functions](../../sql-reference/functions-aggregation.md) are supported.

| Function | Notes |
| --- | --- |
| ANY_VALUE | Supported only as an aggregate for a subquery with a GROUP BY clause. |
| COUNT |  |
| COUNT DISTINCT |  |

### Bitwise expression functions

[Bitwise expression functions](../../sql-reference/expressions-byte-bit.md) are not supported.

### Conditional expression functions

The following [conditional expression functions](../../sql-reference/expressions-conditional.md) are supported.

| Function | Notes |
| --- | --- |
| [ NOT ] IN |  |
| CASE |  |
| COALESCE |  |
| DECODE |  |
| EQUAL_NULL |  |
| GREATEST |  |
| IFF |  |
| IS [NOT] NULL |  |
| LEAST |  |

### Context functions

[Context functions](../../sql-reference/functions-context.md) are not supported.

### Conversion functions

The following [conversion functions](../../sql-reference/functions-conversion.md) are supported.

| Function | Notes |
| --- | --- |
| CAST, `::` | Columns must be explicitly non-null to be casted. To do this, filter out nulls before casting.  Casting other data types to STRING is not supported. |
| TO_BOOLEAN |  |
| TO_CHAR , TO_VARCHAR |  |
| TO_DECIMAL , TO_NUMBER , TO_NUMERIC |  |
| TO_DOUBLE |  |
| TRY_CAST |  |
| TRY_TO_BOOLEAN |  |
| TRY_TO_DECIMAL, TRY_TO_NUMBER, TRY_TO_NUMERIC |  |
| TRY_TO_DOUBLE |  |

### Data generation functions

[Data generation functions](../../sql-reference/functions-data-generation.md) are not supported.

### Data metric functions

[Data metric functions](../../sql-reference/functions-data-metric.md) are not supported. User-defined DMFs are also not supported.

### Date & time functions

The following [date & time functions](../../sql-reference/functions-date-time.md) are supported.

| Function | Notes |
| --- | --- |
| DATE_PART | The following date and time parts are not supported: `dayofweek`, `week`, `yearofweek`, `nanosecond`, `epoch_*`, and `timezone_*`. |
| DAYNAME |  |
| EXTRACT | The following date and time parts are not supported: `dayofweek`, `week`, `yearofweek`, `nanosecond`, `epoch_*`, and `timezone_*`. |
| HOUR |  |
| LAST_DAY |  |
| MINUTE |  |
| SECOND |  |
| TRUNC |  |
| YEAR\* / DAY\* / WEEK\* / MONTH / QUARTER |  |

### Encryption functions

[Encryption functions](../../sql-reference/functions-encryption.md) are not supported.

### File functions

[File functions](../../sql-reference/functions-file.md) are not supported.

### Geospatial functions

[Geospatial functions](../../sql-reference/functions-geospatial.md) are not supported.

### Hash functions

[Hash functions](../../sql-reference/functions-hash-scalar.md) are not supported.

### Metadata functions

[Metadata functions](../../sql-reference/functions-metadata.md) are not supported.

### Numeric functions

The following [numeric functions](../../sql-reference/functions-numeric.md) are supported.

| Function | Notes |
| --- | --- |
| ABS |  |
| CEIL |  |
| FLOOR |  |
| MOD |  |
| SIGN |  |

### Regular expression functions

[Regular expression functions](../../sql-reference/functions-regexp.md) are not supported.

### Semi-structured and structured data functions

[Semi-structured and structured data functions](../../sql-reference/functions-semistructured.md) are not supported.

### String and binary functions

The following [string & binary functions](../../sql-reference/functions-string.md) are supported.

| Function | Notes |
| --- | --- |
| CONTAINS |  |
| LENGTH , LEN |  |
| LOWER |  |
| POSITION |  |
| UPPER |  |

### System functions

[System functions](../../sql-reference/functions-system.md) are not supported.

### Table functions

[Table functions](../../sql-reference/functions-table.md) are not supported.
