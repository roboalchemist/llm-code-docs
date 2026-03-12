# Source: https://docs.snowflake.com/en/sql-reference/functions/object_keys.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# OBJECT_KEYS

Returns an array containing the list of keys in the top-most level of the input object.

## Syntax

```sqlsyntax
OBJECT_KEYS( <object> )
```

## Arguments

`object`
:   The value for which you want the keys. The input value must be one of the following:

    * An [OBJECT](../data-types-semistructured.md).
    * A [VARIANT](../data-types-semistructured.md) that contains a value of type OBJECT.

## Returns

The function returns an [ARRAY](../data-types-semistructured.md) containing the keys.

If `object` is a [structured OBJECT](../data-types-structured.md), the function returns an ARRAY(VARCHAR).

## Usage notes

* If the object contains nested objects (e.g. objects within objects), this returns only the keys from the top-most level.

## Examples

### Basic example

The next example shows OBJECT_KEYS working with both an [OBJECT](../data-types-semistructured.md) and a
[VARIANT](../data-types-semistructured.md) that contains a value of type OBJECT.

> Create a table that contains columns of types [OBJECT](../data-types-semistructured.md) and
> [VARIANT](../data-types-semistructured.md).
>
> ```sqlexample
> CREATE TABLE objects_1 (id INTEGER, object1 OBJECT, variant1 VARIANT);
> ```
>
> INSERT values:
>
> ```sqlexample
> INSERT INTO objects_1 (id, object1, variant1)
>   SELECT
>     1,
>     OBJECT_CONSTRUCT('a', 1, 'b', 2, 'c', 3),
>     TO_VARIANT(OBJECT_CONSTRUCT('a', 1, 'b', 2, 'c', 3))
>     ;
> ```
>
> Retrieve the keys from both the OBJECT and the VARIANT:
>
> ```sqlexample
> SELECT OBJECT_KEYS(object1), OBJECT_KEYS(variant1)
>     FROM objects_1
>     ORDER BY id;
> +----------------------+-----------------------+
> | OBJECT_KEYS(OBJECT1) | OBJECT_KEYS(VARIANT1) |
> |----------------------+-----------------------|
> | [                    | [                     |
> |   "a",               |   "a",                |
> |   "b",               |   "b",                |
> |   "c"                |   "c"                 |
> | ]                    | ]                     |
> +----------------------+-----------------------+
> ```

### Example of nested objects

This example shows that if the object contains nested objects, only the keys from the top-most level are returned.

> ```sqlexample
> SELECT OBJECT_KEYS (
>            PARSE_JSON (
>                '{
>                     "level_1_A": {
>                                  "level_2": "two"
>                                  },
>                     "level_1_B": "one"
>                     }'
>                )
>            ) AS keys
>     ORDER BY 1;
> +----------------+
> | KEYS           |
> |----------------|
> | [              |
> |   "level_1_A", |
> |   "level_1_B"  |
> | ]              |
> +----------------+
> ```
