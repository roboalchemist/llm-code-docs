# Source: https://docs.snowflake.com/en/sql-reference/functions/arrays_to_object.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# ARRAYS_TO_OBJECT

Returns an [OBJECT](../data-types-semistructured.md) that contains the keys specified by one input [ARRAY](../data-types-semistructured.md) and the values
specified by another input ARRAY.

## Syntax

```sqlsyntax
ARRAYS_TO_OBJECT( <key_array> , <value_array> )
```

## Arguments

`key_array`
:   ARRAY of VARCHAR values that specify the keys for the new OBJECT.

`value_array`
:   ARRAY of values for the new OBJECT. This ARRAY must be the same length as `key_array`. The values in this ARRAY should
    correspond to the keys in `key_array`.

## Returns

The function returns a value of the type OBJECT. The OBJECT contains the keys and values specified by the input ARRAYs.

## Usage notes

* If any element in `key_array` is not a string, the function reports the following error:

  ```output
  215002 (22000): Key supplied for ARRAYS_TO_OBJECT does not have string type
  ```

* `key_array` and `value_array` must be equal in length. Otherwise, the function reports the following error:

  ```output
  215001 (22000): Key array and value array had unequal lengths in ARRAYS_TO_OBJECT
  ```

* If an element in `key_array` is NULL, that key and the corresponding value are omitted from the returned OBJECT.

  If the key is not NULL but the corresponding element in `value_array` is NULL, the key and NULL value are included in
  the returned OBJECT.
* The returned OBJECT does not necessarily preserve the original order of the key-value pairs.

* This function doesn’t support a [structured type](../data-types-structured.md) as an input argument.

## Examples

The following example returns an OBJECT that contains key-value pairs specified by two input ARRAYs:

```sqlexample
SELECT ARRAYS_TO_OBJECT(['key1', 'key2', 'key3'], [1, 2, 3]);
```

```output
+-------------------------------------------------------+
| ARRAYS_TO_OBJECT(['KEY1', 'KEY2', 'KEY3'], [1, 2, 3]) |
|-------------------------------------------------------|
| {                                                     |
|   "key1": 1,                                          |
|   "key2": 2,                                          |
|   "key3": 3                                           |
| }                                                     |
+-------------------------------------------------------+
```

In the following example, the ARRAY of keys includes a NULL value. That key and the corresponding value are omitted from the
returned OBJECT.

```sqlexample
SELECT ARRAYS_TO_OBJECT(['key1', NULL, 'key3'], [1, 2, 3]);
```

```output
+-----------------------------------------------------+
| ARRAYS_TO_OBJECT(['KEY1', NULL, 'KEY3'], [1, 2, 3]) |
|-----------------------------------------------------|
| {                                                   |
|   "key1": 1,                                        |
|   "key3": 3                                         |
| }                                                   |
+-----------------------------------------------------+
```

In the following example, the ARRAY of values includes a NULL value. That value and the corresponding key are included in the
returned OBJECT.

```sqlexample
SELECT ARRAYS_TO_OBJECT(['key1', 'key2', 'key3'], [1, NULL, 3]);
```

```output
+----------------------------------------------------------+
| ARRAYS_TO_OBJECT(['KEY1', 'KEY2', 'KEY3'], [1, NULL, 3]) |
|----------------------------------------------------------|
| {                                                        |
|   "key1": 1,                                             |
|   "key2": null,                                          |
|   "key3": 3                                              |
| }                                                        |
+----------------------------------------------------------+
```
