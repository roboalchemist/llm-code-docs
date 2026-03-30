# Source: https://docs.snowflake.com/en/sql-reference/functions/map_pick.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Map)

# MAP_PICK

Returns a new [MAP](../data-types-structured.md) containing the specified key-value pairs from an existing MAP.

To identify the key-value pairs to include in the new map, pass in the keys as arguments, or pass in an array containing the keys.

If a specified key isn’t present in the input map, the key is ignored.

## Syntax

```sqlsyntax
MAP_PICK( <map>, <key1> [, <key2>, ... ] )

MAP_PICK( <map>, <array> )
```

## Arguments

`map`
:   The input map.

`key1,key2`
:   One or more keys that identify the key-value pairs to be included in the returned map.

`array`
:   An array of keys that identify the key-value pairs to be included in the returned map. You can specify a semi-structured ARRAY
    or a structured ARRAY.

## Returns

Returns a new MAP containing some of the key-value pairs from an existing MAP.

## Examples

Create a new map that contains two of the three key-value pairs from an existing map:

```sqlexample
SELECT MAP_PICK({'a':1,'b':2,'c':3}::MAP(VARCHAR,NUMBER),'a', 'b')
  AS new_map;
```

```output
+-----------+
| NEW_MAP   |
|-----------|
| {         |
|   "a": 1, |
|   "b": 2  |
| }         |
+-----------+
```

In the previous example, the keys are passed as arguments to MAP_PICK. You can also use an array to specify the keys:

```sqlexample
SELECT MAP_PICK({'a':1,'b':2,'c':3}::MAP(VARCHAR,NUMBER), ['a', 'b'])
  AS new_map;
```

```output
+-----------+
| NEW_MAP   |
|-----------|
| {         |
|   "a": 1, |
|   "b": 2  |
| }         |
+-----------+
```

Create a temporary table that contains MAP values:

```sqlexample
CREATE OR REPLACE TEMP TABLE demo_maps(
  id INTEGER,
  attrs MAP(VARCHAR, VARCHAR),
  defaults MAP(VARCHAR, VARCHAR),
  keep_keys ARRAY(VARCHAR),
  ins_key VARCHAR,
  ins_val VARCHAR,
  update_existing BOOLEAN,
  del_key1 VARCHAR,
  del_key2 VARCHAR);

INSERT INTO demo_maps SELECT
  1,
  {'color':'red','size':'M','brand':'Acme'}::MAP(VARCHAR, VARCHAR),
  {'currency':'USD','size':'L'}::MAP(VARCHAR, VARCHAR),
  ['color','brand']::ARRAY(VARCHAR),
  'material',
  'cotton',
  TRUE,
  'size',
  'brand';

INSERT INTO demo_maps SELECT
  2,
  {'color':'blue','brand':'ZenCo'}::MAP(VARCHAR, VARCHAR),
  {'currency':'EUR','size':'M','brand':'ZenCo'}::MAP(VARCHAR, VARCHAR),
  ['brand','currency']::ARRAY(VARCHAR),
  'brand',
  'ZC',
  FALSE,
  'currency',
  'material';
```

Query the table to show the data:

```sqlexample
SELECT * FROM demo_maps;
```

```output
+----+---------------------+----------------------+--------------+----------+---------+-----------------+----------+----------+
| ID | ATTRS               | DEFAULTS             | KEEP_KEYS    | INS_KEY  | INS_VAL | UPDATE_EXISTING | DEL_KEY1 | DEL_KEY2 |
|----+---------------------+----------------------+--------------+----------+---------+-----------------+----------+----------|
|  1 | {                   | {                    | [            | material | cotton  | True            | size     | brand    |
|    |   "brand": "Acme",  |   "currency": "USD", |   "color",   |          |         |                 |          |          |
|    |   "color": "red",   |   "size": "L"        |   "brand"    |          |         |                 |          |          |
|    |   "size": "M"       | }                    | ]            |          |         |                 |          |          |
|    | }                   |                      |              |          |         |                 |          |          |
|  2 | {                   | {                    | [            | brand    | ZC      | False           | currency | material |
|    |   "brand": "ZenCo", |   "brand": "ZenCo",  |   "brand",   |          |         |                 |          |          |
|    |   "color": "blue"   |   "currency": "EUR", |   "currency" |          |         |                 |          |          |
|    | }                   |   "size": "M"        | ]            |          |         |                 |          |          |
|    |                     | }                    |              |          |         |                 |          |          |
+----+---------------------+----------------------+--------------+----------+---------+-----------------+----------+----------+
```

Using the keys in the `keep_keys` column, return new MAP values from the MAP values in
the `attrs` column:

```sqlexample
SELECT id, MAP_PICK(attrs, keep_keys) AS attrs_subset
  FROM demo_maps;
```

```output
+----+--------------------+
| ID | ATTRS_SUBSET       |
|----+--------------------|
|  1 | {                  |
|    |   "brand": "Acme", |
|    |   "color": "red"   |
|    | }                  |
|  2 | {                  |
|    |   "brand": "ZenCo" |
|    | }                  |
+----+--------------------+
```
