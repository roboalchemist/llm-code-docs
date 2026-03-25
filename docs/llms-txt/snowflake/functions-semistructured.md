# Source: https://docs.snowflake.com/en/sql-reference/functions-semistructured.md

# Semi-structured and structured data functions

These functions are used with:

* [Semi-structured data formats](../user-guide/semistructured-data-formats.md) (including JSON, Avro, and XML)
* [Semi-structured data types](data-types-semistructured.md) (including VARIANT, OBJECT, and ARRAY)
* [Structured data types](data-types-structured.md) (including structured OBJECT, structured ARRAY, and MAP)

## List of semi-structured and structured data functions

The functions are grouped by type of operation performed:

* Parsing JSON and XML data.
* Creating and manipulating [ARRAYs](data-types-semistructured.md) and [OBJECTs](data-types-semistructured.md).
* Extracting values from semi-structured and structured data (e.g. from an ARRAY, OBJECT, or MAP).
* Converting/casting semi-structured data types and structured data types to/from other data types.
* Determining the data type for values in semi-structured data (i.e. type predicates).

| Sub-category | Function | Notes |
| --- | --- | --- |
| **JSON and XML Parsing** | [CHECK_JSON](functions/check_json.md) |  |
|  | [CHECK_XML](functions/check_xml.md) |  |
|  | [JSON_EXTRACT_PATH_TEXT](functions/json_extract_path_text.md) |  |
|  | [PARSE_JSON](functions/parse_json.md) |  |
|  | [PARSE_XML](functions/parse_xml.md) |  |
|  | [STRIP_NULL_VALUE](functions/strip_null_value.md) |  |
| **Array/Object Creation and Manipulation** | [ARRAY_AGG](functions/array_agg.md) | See also [Aggregate functions](functions-aggregation.md). |
|  | [ARRAY_APPEND](functions/array_append.md) |  |
|  | [ARRAY_CAT](functions/array_cat.md) |  |
|  | [ARRAY_COMPACT](functions/array_compact.md) |  |
|  | [ARRAY_CONSTRUCT](functions/array_construct.md) |  |
|  | [ARRAY_CONSTRUCT_COMPACT](functions/array_construct_compact.md) |  |
|  | [ARRAY_CONTAINS](functions/array_contains.md) |  |
|  | [ARRAY_DISTINCT](functions/array_distinct.md) |  |
|  | [ARRAY_EXCEPT](functions/array_except.md) |  |
|  | [ARRAY_FLATTEN](functions/array_flatten.md) |  |
|  | [ARRAY_GENERATE_RANGE](functions/array_generate_range.md) |  |
|  | [ARRAY_INSERT](functions/array_insert.md) |  |
|  | [ARRAY_INTERSECTION](functions/array_intersection.md) |  |
|  | [ARRAY_MAX](functions/array_max.md) |  |
|  | [ARRAY_MIN](functions/array_min.md) |  |
|  | [ARRAY_POSITION](functions/array_position.md) |  |
|  | [ARRAY_PREPEND](functions/array_prepend.md) |  |
|  | [ARRAY_REMOVE](functions/array_remove.md) |  |
|  | [ARRAY_REMOVE_AT](functions/array_remove_at.md) |  |
|  | [ARRAY_REVERSE](functions/array_reverse.md) |  |
|  | [ARRAY_SIZE](functions/array_size.md) |  |
|  | [ARRAY_SLICE](functions/array_slice.md) |  |
|  | [ARRAY_SORT](functions/array_sort.md) |  |
|  | [ARRAY_TO_STRING](functions/array_to_string.md) |  |
|  | [ARRAY_UNION_AGG](functions/array_union_agg.md) | See also [Aggregate functions](functions-aggregation.md). |
|  | [ARRAY_UNIQUE_AGG](functions/array_unique_agg.md) | See also [Aggregate functions](functions-aggregation.md). |
|  | [ARRAYS_OVERLAP](functions/arrays_overlap.md) |  |
|  | [ARRAYS_TO_OBJECT](functions/arrays_to_object.md) |  |
|  | [ARRAYS_ZIP](functions/arrays_zip.md) |  |
|  | [OBJECT_AGG](functions/object_agg.md) | See also [Aggregate functions](functions-aggregation.md). |
|  | [OBJECT_CONSTRUCT](functions/object_construct.md) |  |
|  | [OBJECT_CONSTRUCT_KEEP_NULL](functions/object_construct_keep_null.md) |  |
|  | [OBJECT_DELETE](functions/object_delete.md) |  |
|  | [OBJECT_INSERT](functions/object_insert.md) |  |
|  | [OBJECT_PICK](functions/object_pick.md) |  |
|  | [PROMPT](functions/prompt.md) |  |
| **Higher-order** | [FILTER](functions/filter.md) | See also [Use lambda functions on data with Snowflake higher-order functions](../user-guide/querying-semistructured.md). |
|  | [REDUCE](functions/reduce.md) | See also [Use lambda functions on data with Snowflake higher-order functions](../user-guide/querying-semistructured.md). |
|  | [TRANSFORM](functions/transform.md) | See also [Use lambda functions on data with Snowflake higher-order functions](../user-guide/querying-semistructured.md). |
| **Map Creation and Manipulation** | [MAP_CAT](functions/map_cat.md) |  |
|  | [MAP_CONTAINS_KEY](functions/map_contains_key.md) |  |
|  | [MAP_DELETE](functions/map_delete.md) |  |
|  | [MAP_INSERT](functions/map_insert.md) |  |
|  | [MAP_KEYS](functions/map_keys.md) |  |
|  | [MAP_PICK](functions/map_pick.md) |  |
|  | [MAP_SIZE](functions/map_size.md) |  |
| **Extraction** | [FLATTEN](functions/flatten.md) | [Table function](functions-table.md). |
|  | [GET](functions/get.md) |  |
|  | [GET_IGNORE_CASE](functions/get_ignore_case.md) |  |
|  | [GET_PATH , :](functions/get_path.md) | Variation of GET. |
|  | [OBJECT_KEYS](functions/object_keys.md) | Extracts keys from key/value pairs in [OBJECT](data-types-semistructured.md). |
|  | [XMLGET](functions/xmlget.md) |  |
| **Conversion/Casting** | [AS_<object_type>](functions/as.md) |  |
|  | [AS_ARRAY](functions/as_array.md) |  |
|  | [AS_BINARY](functions/as_binary.md) |  |
|  | [AS_CHAR , AS_VARCHAR](functions/as_char-varchar.md) |  |
|  | [AS_DATE](functions/as_date.md) |  |
|  | [AS_DECIMAL , AS_NUMBER](functions/as_decimal-number.md) |  |
|  | [AS_DOUBLE , AS_REAL](functions/as_double-real.md) |  |
|  | [AS_INTEGER](functions/as_integer.md) |  |
|  | [AS_OBJECT](functions/as_object.md) |  |
|  | [AS_TIME](functions/as_time.md) |  |
|  | [AS_TIMESTAMP_\*](functions/as_timestamp.md) |  |
|  | [STRTOK_TO_ARRAY](functions/strtok_to_array.md) |  |
|  | [TO_ARRAY](functions/to_array.md) |  |
|  | [TO_JSON](functions/to_json.md) |  |
|  | [TO_OBJECT](functions/to_object.md) |  |
|  | [TO_VARIANT](functions/to_variant.md) |  |
|  | [TO_XML](functions/to_xml.md) |  |
| **Type Predicates** | [IS_<object_type>](functions/is.md) |  |
|  | [IS_ARRAY](functions/is_array.md) |  |
|  | [IS_BOOLEAN](functions/is_boolean.md) |  |
|  | [IS_BINARY](functions/is_binary.md) |  |
|  | [IS_CHAR , IS_VARCHAR](functions/is_char-varchar.md) |  |
|  | [IS_DATE , IS_DATE_VALUE](functions/is_date-value.md) |  |
|  | [IS_DECIMAL](functions/is_decimal.md) |  |
|  | [IS_DOUBLE , IS_REAL](functions/is_double-real.md) |  |
|  | [IS_INTEGER](functions/is_integer.md) |  |
|  | [IS_NULL_VALUE](functions/is_null_value.md) |  |
|  | [IS_OBJECT](functions/is_object.md) |  |
|  | [IS_TIME](functions/is_time.md) |  |
|  | [IS_TIMESTAMP_\*](functions/is_timestamp.md) |  |
|  | [TYPEOF](functions/typeof.md) |  |
