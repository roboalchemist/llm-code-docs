# Source: https://docs.snowflake.com/en/sql-reference/functions/to_object.md

Categories:
:   [Conversion functions](../functions-conversion.md) , [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# TO_OBJECT

Converts the input value to an [OBJECT](../data-types-semistructured.md):

* For a [VARIANT](../data-types-semistructured.md) value containing an OBJECT, returns the OBJECT.
* For NULL input, or for a VARIANT value containing only [JSON null](../../user-guide/semistructured-considerations.md), returns NULL.
* For an OBJECT, returns the OBJECT itself.
* For all other input values, reports an error.

## Syntax

```sqlsyntax
TO_OBJECT( <expr> )
```

## Arguments

`expr`
:   An expression that evaluates to a VARIANT that contains an OBJECT.

## Returns

The data type of the returned value is OBJECT.

## Examples

This demonstrates simple usage of the TO_OBJECT function:

> Create a table and insert a value of type VARIANT. (The function [PARSE_JSON](parse_json.md) returns a VARIANT.)
>
> > ```sqlexample
> > CREATE TABLE t1 (vo VARIANT);
> > INSERT INTO t1 (vo)
> >     SELECT PARSE_JSON('{"a":1}');
> > ```
>
> Call the TO_OBJECT function:
>
> > ```sqlexample
> > SELECT TO_OBJECT(vo) from t1;
> > +---------------+
> > | TO_OBJECT(VO) |
> > |---------------|
> > | {             |
> > |   "a": 1      |
> > | }             |
> > +---------------+
> > ```
