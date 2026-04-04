# Source: https://docs.oxla.com/sql-reference/sql-functions/json-functions/json-extract-path.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON_EXTRACT_PATH

## Overview

`JSON_EXTRACT_PATH()` function extracts JSON nested value from a specified path.

## Syntax

The syntax of the `JSON_EXTRACT_PATH()` function can be seen below.

```sql  theme={null}
JSON_EXTRACT_PATH(from_json JSON, path TEXT[])
```

* `from_json`: the JSON value from which to extract.
* `path`: the path to extract.

### **Another Option**

Besides the syntax above, Oxla provides and supports the use of operators in queries.  See the syntax below:

```sql  theme={null}
SELECT 'from_json'::JSON -> 'path';
```

* `from_json`: the JSON value from which to extract.
* `::JSON`:  a symbol that casts the text literal to a JSON type.
* `path`: key of the field that we want to extract.

## Examples

These examples display how `JSON_EXTRACT_PATH()` extracts the "oxla" JSON sub-object from the specified path.&#x20;

1. Use the below query:

```sql  theme={null}
SELECT JSON_EXTRACT_PATH('{"f2":{"f3":1},"f4":{"f5":99,"f6":"oxla"}}', 'f4', 'f6');
```

**or**

```sql  theme={null}
SELECT '{"f2":{"f3":1},"f4":{"f5":99,"f6":"oxla"}}'::JSON -> 'f4' -> 'f6';
```

The query above will return the following result.

```sql  theme={null}
+---------+
| f       |
+---------+
| "oxla"  |
+---------+
```

2. Run the query below:

```sql  theme={null}
SELECT
    JSON_EXTRACT_PATH('{"a": 1, "b": {"x": "subtract", "y": "plus"}}', 'b', 'x') AS "bx",
    JSON_EXTRACT_PATH('{"a": 1, "b": {"x": "multiply", "y": "divide"}}', 'b', 'y') AS "by";
```

You will get the following output:

```sql  theme={null}
+---------------+-------------+
| bx            | by          |
+---------------+-------------+
| "subtract"    | "divide"    |
+---------------+-------------+
```
