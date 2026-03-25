# Source: https://docs.snowflake.com/en/sql-reference/functions/fl_get_file_type.md

Categories:
:   [File functions](../functions-file.md) (AI Functions)

# FL_GET_FILE_TYPE

Returns the file type (modality) of a [FILE](../data-types-unstructured.md). This is a more general classification than
the content type (see [FL_GET_CONTENT_TYPE](fl_get_content_type.md)).

## Syntax

Use one of the following:

```
FL_GET_FILE_TYPE( <file_expression> )

FL_GET_FILE_TYPE( <variant_expression> )
```

## Arguments

`file_expression`
:   The argument must be an expression of type FILE.

`variant_expression`
:   The argument must be an OBJECT representing a FILE.

## Returns

One of following values as a VARCHAR:

* `document`
* `video`
* `audio`
* `image`
* `compressed`
* `unknown`

> **Tip:**
>
> To test if a file is of a particular type, use one of the `FL_IS` functions:
>
> * [FL_IS_AUDIO](fl_is_audio.md)
> * [FL_IS_COMPRESSED](fl_is_compressed.md)
> * [FL_IS_DOCUMENT](fl_is_document.md)
> * [FL_IS_IMAGE](fl_is_image.md)
> * [FL_IS_VIDEO](fl_is_video.md)

## Examples

Example using an input FILE:

```sqlexample
CREATE TABLE FILE_TABLE(f FILE);
INSERT INTO file_table SELECT TO_FILE(BUILD_STAGE_FILE_URL('@mystage', 'image.png'));

SELECT FL_GET_FILE_TYPE(f) FROM file_table;
```

```output
+------------------------+
| FL_GET_FILE_TYPE(F)    |
|------------------------|
| image                  |
+------------------------+
```

Example using an input OBJECT:

```sqlexample
CREATE TABLE file_table(f OBJECT);
INSERT INTO file_table SELECT OBJECT_CONSTRUCT('STAGE', 'MYSTAGE', 'RELATIVE_PATH', 'document.pdf', 'ETAG', '<ETAG value>',
  'LAST_MODIFIED', 'Wed, 11 Dec 2024 20:24:00 GMT', 'SIZE', 105859, 'FILE_TYPE', 'application/pdf');

SELECT FL_GET_FILE_TYPE(f) FROM file_table;
```

```output
+------------------------+
| FL_GET_FILE_TYPE(F)    |
|------------------------|
| document               |
+------------------------+
```
