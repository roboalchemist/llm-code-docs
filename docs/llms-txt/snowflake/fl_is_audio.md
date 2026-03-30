# Source: https://docs.snowflake.com/en/sql-reference/functions/fl_is_audio.md

Categories:
:   [File functions](../functions-file.md) (AI Functions)

# FL_IS_AUDIO

Checks if the input is an audio [FILE](../data-types-unstructured.md).

## Syntax

Use one of the following:

```
FL_IS_AUDIO( <file_expression> )

FL_IS_AUDIO( <variant_expression> )
```

## Arguments

`file_expression`
:   The argument must be an expression of type FILE.

`variant_expression`
:   The argument must be an OBJECT representing a FILE.

## Returns

A BOOLEAN indicating whether the file is an audio file.

## Examples

Example using an input FILE:

```sqlexample
CREATE TABLE file_table(f FILE);
insert into file_table select to_file(BUILD_STAGE_FILE_URL('@mystage', 'image.png'));

SELECT FL_IS_AUDIO(f) FROM file_table;
```

```output
+-------------------+
| FL_IS_AUDIO(F)    |
|-------------------|
| False             |
+-------------------+
```

Example using an input OBJECT:

```sqlexample
CREATE TABLE file_table(f OBJECT);

INSERT INTO file_table SELECT OBJECT_CONSTRUCT('STAGE', 'MYSTAGE', 'RELATIVE_PATH', 'music.mpeg', 'ETAG', '<ETAG value>',
  'LAST_MODIFIED', 'Wed, 11 Dec 2024 20:24:00 GMT', 'SIZE', 105859, 'FILE_TYPE', 'audio/mpeg');

SELECT FL_IS_AUDIO(f) FROM file_table;
```

```output
+-------------------+
| FL_IS_AUDIO(F)    |
|-------------------|
| True              |
+-------------------+
```
