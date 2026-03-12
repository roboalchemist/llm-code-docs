# Source: https://docs.snowflake.com/en/sql-reference/functions/fl_is_video.md

Categories:
:   [File functions](../functions-file.md) (AI Functions)

# FL_IS_VIDEO

Checks if the input is a video [FILE](../data-types-unstructured.md).

## Syntax

Use one of the following:

```
FL_IS_VIDEO( <file_expression> )

FL_IS_VIDEO( <variant_expression> )
```

## Arguments

`file_expression`
:   The argument must be an expression of type FILE.

`variant_expression`
:   The argument must be an OBJECT representing a FILE.

## Returns

A BOOLEAN indicating whether the file is a video.

## Examples

Example using an input FILE:

```sqlexample
CREATE TABLE file_table(f FILE);
INSERT INTO file_table SELECT TO_FILE(BUILD_STAGE_FILE_URL('@mystage', 'image.png'));

SELECT FL_IS_VIDEO(f) FROM file_table;
```

```output
+-------------------+
| FL_IS_VIDEO(F)    |
|-------------------|
| False             |
+-------------------+
```

Example using an input OBJECT:

```sqlexample
CREATE TABLE file_table(f OBJECT);
INSERT INTO file_table SELECT OBJECT_CONSTRUCT('STAGE', 'MYSTAGE', 'RELATIVE_PATH', 'movie.mp4', 'ETAG', '<ETAG value>',
  'LAST_MODIFIED', 'Wed, 11 Dec 2024 20:24:00 GMT', 'SIZE', 105859, 'FILE_TYPE', 'video/mp4');

SELECT FL_IS_VIDEO(f) FROM file_table;
```

```output
+-------------------+
| FL_IS_VIDEO(F)    |
|-------------------|
| True              |
+-------------------+
```
