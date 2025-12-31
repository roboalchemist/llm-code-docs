# Source: https://docs.oxla.com/sql-reference/sql-functions/json-functions/json-array-extract.md

# JSON_ARRAY_EXTRACT

## **Overview**

The `JSON_ARRAY_EXTRACT()` function returns the JSON array as a set of JSON values. 

## **Syntax**

The `JSON_ARRAY_EXTRACT()` has the basic syntax as seen below.

```sql  theme={null}
JSON_ARRAY_EXTRACT('json_array'::JSON,id);
```

`JSON_ARRAY_EXTRACT()` requires the following parameters:

* `json_array`: the array to be extracted.
* `::JSON`: argument indicating that the query is of type JSON.
* `id`: ID of the element that we want to extract. It is read in an array format that starts with 0.

### Another Option

`JSON_ARRAY_EXTRACT` can also be achieved with the `->` operator, as shown in the syntax below:

```sql  theme={null}
SELECT 'from_json'::JSON -> path;
```

* `from_json`: the JSON value from which to extract.
* `::JSON`: a symbol that casts the string literal to a JSON type.
* `path`: key of the field that we want to extract.

## Examples

### Case #1: Basic JSON\_ARRAY\_EXTRACT() function

1. In the below example, we will extract a JSON array as a JSON set.

```sql  theme={null}
SELECT JSON_ARRAY_EXTRACT('["Bougenvile", 2, 12, "Lily"]'::JSON,3);
```

**or**

```sql  theme={null}
SELECT ('["Bougenvile", 2, 12, "Lily"]'::JSON -> 3);
```

2. The extracted array will look like the following.

```sql  theme={null}
+------------+
| f          |
+------------+
| "Lily"     |
+------------+
```

### Case #2: Extract element of JSON array as text

1. In this case, we will extract the element of the JSON array as text with the `->>` operator.

```sql  theme={null}
SELECT ('["Bougenvile", 2, 12, "Lily"]'::JSON ->> 1);
```

2. You will get the final output as follows:

```sql  theme={null}
+------------+
| f          |
+------------+
| 2.000000   |
+------------+
```
