# Source: https://docs.snowflake.com/en/sql-reference/functions/to_decfloat.md

Categories:
:   [Conversion functions](../functions-conversion.md)

# TO_DECFLOAT

Converts an expression to a decimal floating-point number ([DECFLOAT](../data-types-numeric.md)).

See also:
:   [TRY_TO_DECFLOAT](try_to_decfloat.md)

## Syntax

```sqlsyntax
TO_DECFLOAT( <expr> [ , '<format>' ] )
```

## Arguments

**Required:**

`expr`
:   An expression of a numeric, character, or Boolean type.

**Optional:**

`'format'`
:   If the expression evaluates to a string, the function accepts
    an optional format model. For more information, see
    [SQL format models](../sql-format-models.md). The format model
    specifies the format of the input string, not the format of the
    output value.

## Returns

This function returns a value of DECFLOAT data type.

If `expr` is NULL, the function returns NULL.

## Usage notes

The special values `'NaN'` (not a number), `'inf'` (infinity),
and `'-inf'` (negative infinity) aren’t supported.

## Examples

After you create a table with columns of different data types, call the TO_DECFLOAT
function to convert the values in each of those columns:

```sqlexample
CREATE OR REPLACE TABLE to_decfloat_demo (d DECIMAL(7, 2), v VARCHAR);
INSERT INTO to_decfloat_demo (d, v) SELECT 1.1, '2.2';
SELECT TO_DECFLOAT(d), TO_DECFLOAT(v) FROM to_decfloat_demo;
```

```output
+----------------+----------------+
| TO_DECFLOAT(D) | TO_DECFLOAT(V) |
|----------------+----------------|
| 1.1            | 2.2            |
+----------------+----------------+
```
