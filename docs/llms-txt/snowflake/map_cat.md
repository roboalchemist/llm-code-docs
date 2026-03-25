# Source: https://docs.snowflake.com/en/sql-reference/functions/map_cat.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Map)

# MAP_CAT

Returns the concatenatation of two [MAP](../data-types-structured.md) values.

## Syntax

```sqlsyntax
MAP_CAT( <map1> , <map2> )
```

## Arguments

`map1`
:   The source MAP.

`map2`
:   The MAP to be appended to `map1`.

## Returns

The return type of this function is the type of `map1`. `map2` is coerced into the `map1` type following the coercion rules. For information about coercion rules, see [Implicit casting a value (coercion)](../data-types-structured.md).

## Usage notes

* If both `map1` and `map2` have a value with the same key, then the output map contains the value from `map2`.
* If either argument is NULL, the function returns NULL without reporting any error.

## Examples

Create two MAPs and concatenate them:

```sqlexample
SELECT MAP_CAT(
  {'map1key1':'map1value1','map1key2':'map1value2'}::MAP(VARCHAR,VARCHAR),
  {'map2key1':'map2value1','map2key2':'map2value2'}::MAP(VARCHAR,VARCHAR))
  AS concatenated_maps;
```

```output
+-----------------------------+
| CONCATENATED_MAPS           |
|-----------------------------|
| {                           |
|   "map1key1": "map1value1", |
|   "map1key2": "map1value2", |
|   "map2key1": "map2value1", |
|   "map2key2": "map2value2"  |
| }                           |
+-----------------------------+
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

Concatenate the two MAP columns `attrs` and `defaults`:

```sqlexample
SELECT id, MAP_CAT(attrs, defaults) AS merged
  FROM demo_maps;
```

```output
+----+----------------------+
| ID | MERGED               |
|----+----------------------|
|  1 | {                    |
|    |   "brand": "Acme",   |
|    |   "color": "red",    |
|    |   "currency": "USD", |
|    |   "size": "L"        |
|    | }                    |
|  2 | {                    |
|    |   "brand": "ZenCo",  |
|    |   "color": "blue",   |
|    |   "currency": "EUR", |
|    |   "size": "M"        |
|    | }                    |
+----+----------------------+
```

The output contains the keys and values from both maps. The output also shows that when both
`map1` in the `attr` column and `map2` in the `defaults` column have a value
with the same key, then the output map contains the value from `map2`. That is,
size `L` is in the output for row `1` instead of size `M`.
