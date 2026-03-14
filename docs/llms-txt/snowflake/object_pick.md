# Source: https://docs.snowflake.com/en/sql-reference/functions/object_pick.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# OBJECT_PICK

Returns a new [OBJECT](../data-types-semistructured.md) containing some of the key-value pairs from an existing
object.

To identify the key-value pairs to include in the new object, pass in the keys as arguments, or pass in an array containing
the keys.

If a specified key is not present in the input object, the key is ignored.

## Syntax

```sqlsyntax
OBJECT_PICK( <object>, <key1> [, <key2>, ... ] )

OBJECT_PICK( <object>, <array> )
```

## Arguments

`object`
:   The input object.

`key1`, `key2`
:   One or more keys identifying the key-value pairs that should be included in the returned object.

`array`
:   Array of keys identifying the key-value pairs that should be included in the returned object.

## Returns

Returns a new OBJECT containing the specified key-value pairs.

## Usage notes

For structured OBJECTs:

* For the arguments that are keys, you must specify constants.
* You can’t pass in an ARRAY of keys as the second argument. You must specify each key as a separate argument.
* The function returns a structured OBJECT value. The type of the OBJECT value includes the keys in the order in which they are specified.

  For example, suppose that you select the `state` and `city` keys in that order:

  ```sqlexample
  SELECT
    OBJECT_PICK(
      {'city':'San Mateo','state':'CA','zip_code':94402}::OBJECT(city VARCHAR,state VARCHAR,zip_code DOUBLE),
      'state',
      'city') AS new_object,
    SYSTEM$TYPEOF(new_object);
  ```

  The function returns an OBJECT value of the type `OBJECT(state VARCHAR, city VARCHAR)`.

  ```output
  +-----------------------+------------------------------------------+
  | NEW_OBJECT            | SYSTEM$TYPEOF(NEW_OBJECT)                |
  |-----------------------+------------------------------------------|
  | {                     | OBJECT(state VARCHAR, city VARCHAR)[LOB] |
  |   "state": "CA",      |                                          |
  |   "city": "San Mateo" |                                          |
  | }                     |                                          |
  +-----------------------+------------------------------------------+
  ```

## Examples

The following example calls OBJECT_PICK to create a new object that contains two of the three key-value pairs from an existing
object:

> ```sqlexample
> SELECT OBJECT_PICK(
>     OBJECT_CONSTRUCT(
>         'a', 1,
>         'b', 2,
>         'c', 3
>     ),
>     'a', 'b'
> ) AS new_object;
> +------------+
> | NEW_OBJECT |
> |------------|
> | {          |
> |   "a": 1,  |
> |   "b": 2   |
> | }          |
> +------------+
> ```

In the example above, the keys are passed as arguments to OBJECT_PICK. You can also use an array to specify the keys,
as shown below:

> ```sqlexample
> SELECT OBJECT_PICK(
>     OBJECT_CONSTRUCT(
>         'a', 1,
>         'b', 2,
>         'c', 3
>     ),
>     ARRAY_CONSTRUCT('a', 'b')
> ) AS new_object;
> +------------+
> | NEW_OBJECT |
> |------------|
> | {          |
> |   "a": 1,  |
> |   "b": 2   |
> | }          |
> +------------+
> ```
