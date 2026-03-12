# Source: https://docs.snowflake.com/en/sql-reference/functions/map_size.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Map)

# MAP_SIZE

Returns the size of a [MAP](../data-types-structured.md).

## Syntax

```sqlsyntax
MAP_SIZE( <map> )
```

## Arguments

`map`
:   The input map.

## Returns

Returns the number of entries in the map.

## Examples

Determine the number of entries in a map:

```sqlexample
SELECT MAP_SIZE({'a':1,'b':2,'c':3}::MAP(VARCHAR,NUMBER))
  AS map_size;
```

```output
+----------+
| MAP_SIZE |
|----------|
|        3 |
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

Return the number of entries in the MAP values in the `attrs` column:

```sqlexample
SELECT id, MAP_SIZE(attrs) AS attr_count
  FROM demo_maps;
```

```output
+----+------------+
| ID | ATTR_COUNT |
|----+------------|
|  1 |          3 |
|  2 |          2 |
+----+------------+
```
