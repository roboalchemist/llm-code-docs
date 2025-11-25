# Source: https://docs.oxla.com/sql-reference/sql-functions/json-functions/json-extract-path-text.md

# JSON_EXTRACT_PATH_TEXT

## Overview

The `JSON_EXTRACT_PATH_TEXT()` function extracts JSON nested value from a specified JSON value according to the defined path.

<Info>This function may be similar to the `JSON_EXTRACT_PATH()`. This function returns a value of type text instead of type JSON.</Info>

## Syntax

The `JSON_EXTRACT_PATH_TEXT()` syntax is shown below:

```sql  theme={null}
JSON_EXTRACT_PATH_TEXT(from_json JSON, path TEXT[])
```

The required arguments are explained below.

* `from_json`: the JSON value to extract.
* `path`: the path to extract.

### Another Option

Besides the syntax above, Oxla provides and supports the use of operators in queries. See the syntax below:

```sql  theme={null}
SELECT 'from_json'::JSON ->> 'path';
```

* `from_json`: the JSON value from which to extract.
* `::JSON`: a symbol that casts the text literal to a JSON type.
* `path`: key of the field that we want to extract.

## Example

1. This example shows how to use the `JSON_EXTRACT_PATH_TEXT()` function to extract values ​​from a JSON object at a specified index.

Run the following query:

```sql  theme={null}
SELECT JSON_EXTRACT_PATH_TEXT('{"a": "Oxla", "b": {"x": 1.234, "y": 4.321}}', 'a') AS "result a";
```

**or**

```sql  theme={null}
SELECT '{"a": "Oxla", "b": {"x": 1.234, "y": 4.321}}'::JSON ->> 'a' AS "result a";
```

2. The `JSON\_EXTRACT\_PATH\_TEXT()` function extracts the values and returns the output below:

```sql  theme={null}
+------------+
| result a   |
+------------+
| "Oxla"     |
+------------+
```
