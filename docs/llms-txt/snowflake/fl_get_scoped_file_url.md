# Source: https://docs.snowflake.com/en/sql-reference/functions/fl_get_scoped_file_url.md

Categories:
:   [File functions](../functions-file.md) (AI Functions)

# FL_GET_SCOPED_FILE_URL

Returns the scoped URL of a [FILE](../data-types-unstructured.md).

## Syntax

Use one of the following:

```
FL_GET_SCOPED_FILE_URL( <file_expression> )

FL_GET_SCOPED_FILE_URL( <variant_expression> )
```

## Arguments

`file_expression`
:   The argument must be an expression of type FILE.

`variant_expression`
:   The argument must be an OBJECT representing a FILE.

## Returns

The scoped URL of the file as a VARCHAR.

## Examples

Example using an input FILE:

```sqlexample
CREATE TABLE file_table(f FILE);
INSERT INTO file_table SELECT TO_FILE(BUILD_SCOPED_FILE_URL('@mystage', 'image.png'));

SELECT FL_GET_SCOPED_FILE_URL(f) FROM file_table;
```

```output
+--------------------------------------------------------------------------------------------------------------------+
| FL_GET_SCOPED_FILE_URL(F)                                                                                          |
|--------------------------------------------------------------------------------------------------------------------|
| https://snowflake.account.snowflakecomputing.com/api/files/01ba4df2-0100-0001-0000-00040002e2b6/299017/Y6JShH6KjV  |
+--------------------------------------------------------------------------------------------------------------------+
```

Example using an input OBJECT:

```sqlexample
CREATE TABLE file_table(f OBJECT);
INSERT INTO file_table SELECT OBJECT_CONSTRUCT('SCOPED_FILE_URL', 'https://snowflake.account.snowflakecomputing.com/api/files/01ba4df2-0100-0001-0000-00040002e2b6/299017/Y6JShH6KjV',
  'ETAG', '<ETAG value>', 'LAST_MODIFIED', 'Wed, 11 Dec 2024 20:24:00 GMT', 'SIZE', 105859, 'CONTENT_TYPE', 'image/jpg');

SELECT FL_GET_SCOPED_FILE_URL(f) FROM file_table;
```

```output
+--------------------------------------------------------------------------------------------------------------------+
| FL_GET_SCOPED_FILE_URL(F)                                                                                          |
|--------------------------------------------------------------------------------------------------------------------|
| https://snowflake.account.snowflakecomputing.com/api/files/01ba4df2-0100-0001-0000-00040002e2b6/299017/Y6JShH6KjV  |
+--------------------------------------------------------------------------------------------------------------------+
```
