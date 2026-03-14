# Source: https://docs.snowflake.com/en/sql-reference/functions/fl_get_etag.md

Categories:
:   [File functions](../functions-file.md) (AI Functions)

# FL_GET_ETAG

Returns the content hash (ETAG) of a [FILE](../data-types-unstructured.md).

## Syntax

Use one of the following:

```
FL_GET_ETAG( <file_expression> )

FL_GET_ETAG( <variant_expression> )
```

## Arguments

`file_expression`
:   The argument must be an expression of type FILE.

`variant_expression`
:   The argument must be an OBJECT representing a FILE.

## Returns

A VARCHAR value with the ETAG of the file.

## Examples

Example using an input FILE:

```sqlexample
CREATE TABLE file_table(f FILE);
INSERT INTO file_table SELECT TO_FILE(BUILD_STAGE_FILE_URL('@mystage', 'image.png'));

SELECT FL_GET_ETAG(f) FROM file_table;
```

```output
+-----------------------------------+
| FL_GET_ETAG(F)                    |
|-----------------------------------|
| <ETAG value>                      |
+-----------------------------------+
```

Example using an input OBJECT:

```sqlexample
CREATE TABLE file_table(f OBJECT);
INSERT INTO file_table SELECT OBJECT_CONSTRUCT('STAGE', 'MYSTAGE', 'RELATIVE_PATH', 'image.jpg', 'ETAG', '<ETAG value>',
  'LAST_MODIFIED', 'Wed, 11 Dec 2024 20:24:00 GMT', 'SIZE', 105859, 'CONTENT_TYPE', 'image/jpg');

SELECT FL_GET_ETAG(f) FROM file_table;
```

```output
+-----------------------------------+
| FL_GET_ETAG(F)                    |
|-----------------------------------|
| <ETAG value>                      |
+-----------------------------------+
```
