# Source: https://docs.snowflake.com/en/sql-reference/functions/strip_null_value.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Parsing)

# STRIP_NULL_VALUE

Converts a [JSON null](../../user-guide/semistructured-considerations.md) value to a SQL NULL value. All other variant values are passed unchanged.

## Syntax

```sqlsyntax
STRIP_NULL_VALUE( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression of type VARIANT.

## Returns

* If the expression contains a JSON null value, the function returns a SQL NULL.
* If the expression does not contain a JSON null value, the function returns the input value.

## Examples

```sqlexample
CREATE OR REPLACE TABLE mytable
(
  SRC Variant
);

INSERT INTO mytable
  SELECT PARSE_JSON(column1)
  FROM VALUES
  ('{
  "a": "1",
  "b": "2",
  "c": null
  }')
  , ('{
  "a": "1",
  "b": "2",
  "c": "3"
  }');

SELECT STRIP_NULL_VALUE(src:c) FROM mytable;
```

```output
+-------------------------+
| STRIP_NULL_VALUE(SRC:C) |
|-------------------------|
| NULL                    |
| "3"                     |
+-------------------------+
```
