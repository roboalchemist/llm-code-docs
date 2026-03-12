# Source: https://docs.snowflake.com/en/sql-reference/functions-hash-scalar.md

# Hash functions

Snowflake provides hash functions, which take input value(s) and return a signed 64-bit numeric value. Hash functions are deterministic.
Snowflake provides both a scalar hash function and an aggregate hash function, both of which are listed here.

> **Note:**
>
> The hash functions are not cryptographic hash functions.
>
> For cryptographic functions, use the SHA families of functions (see [String & binary functions](functions-string.md)).

| Function Name | Notes |
| --- | --- |
| [HASH](functions/hash.md) |  |
| [HASH_AGG](functions/hash_agg.md) | [Aggregate function](functions-aggregation.md). |
