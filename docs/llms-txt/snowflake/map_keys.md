# Source: https://docs.snowflake.com/en/sql-reference/functions/map_keys.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Map)

# MAP_KEYS

Returns the keys in a [MAP](../data-types-structured.md).

## Syntax

```sqlsyntax
MAP_KEYS( <map> )
```

## Arguments

`map`
:   The input map.

## Returns

Returns a structured ARRAY containing the keys in the MAP. The order of the keys is undefined.

## Examples

List the keys in a map:

```sqlexample
SELECT MAP_KEYS({'a':1,'b':2,'c':3}::MAP(VARCHAR,NUMBER))
  AS map_keys;
```

```output
+----------+
| MAP_KEYS |
|----------|
| [        |
|   "a",   |
|   "b",   |
|   "c"    |
| ]        |
+----------+
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

Return the keys in the MAP values in the `attrs` column:

```sqlexample
SELECT id, MAP_KEYS(attrs) AS attr_keys
  FROM demo_maps;
```

```output
+----+------------+
| ID | ATTR_KEYS  |
|----+------------|
|  1 | [          |
|    |   "brand", |
|    |   "color", |
|    |   "size"   |
|    | ]          |
|  2 | [          |
|    |   "brand", |
|    |   "color"  |
|    | ]          |
+----+------------+
```
