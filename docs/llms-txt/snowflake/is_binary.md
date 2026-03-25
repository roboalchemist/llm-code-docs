# Source: https://docs.snowflake.com/en/sql-reference/functions/is_binary.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Type Predicates)

# IS_BINARY

Returns TRUE if its [VARIANT](../data-types-semistructured.md) argument contains a [binary string](../data-types-text.md) value.

See also:
:   [IS_<object_type>](is.md)

## Syntax

```sqlsyntax
IS_BINARY( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

Returns a BOOLEAN value or NULL.

* Returns TRUE if the VARIANT value contains a BINARY value. Otherwise, returns FALSE.
* If the input is NULL, returns NULL without reporting an error.

## Examples

Return all of the BINARY values in a VARIANT column.

> **Note:**
>
> The output format for BINARY values is set using the [BINARY_OUTPUT_FORMAT](../parameters.md) parameter.
> The default setting is `HEX`.

Create and load a table with a BINARY value in a VARIANT column:

```sqlexample
CREATE OR REPLACE TABLE varbin (v VARIANT);

INSERT INTO varbin SELECT TO_VARIANT(TO_BINARY('snow', 'utf-8'));
```

Show the BINARY values in the data by using the IS_BINARY function in a WHERE clause:

```sqlexample
SELECT v AS hex_encoded_binary_value
  FROM varbin
  WHERE IS_BINARY(v);
```

```output
+--------------------------+
| HEX_ENCODED_BINARY_VALUE |
|--------------------------|
| "736E6F77"               |
+--------------------------+
```
