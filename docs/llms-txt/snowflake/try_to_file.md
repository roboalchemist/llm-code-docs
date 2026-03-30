# Source: https://docs.snowflake.com/en/sql-reference/functions/try_to_file.md

Categories:
:   [File functions](../functions-file.md) (AI Functions)

# TRY_TO_FILE

A version of [TO_FILE](to_file.md) that returns NULL instead of raising an error.

## Syntax

Use one of the following:

```
TRY_TO_FILE( <stage_name>, <relative_path> )

TRY_TO_FILE( <file_url> )

TRY_TO_FILE( <metadata> )
```

## Arguments

Specify the file by providing:

* Both `stage_name` and `relative_path`
* `file_url`
* `metadata`

Only one of these methods can be used at a time.

`stage_name`
:   The name of the stage where the file is located, as a string, in the form `'@stage_name'`.

`relative_path`
:   The path to the file on the stage specified by `stage_name` as a string.

`file_url`
:   A valid stage or scoped file URL as a string.

`metadata`
:   An OBJECT containing the required FILE attributes. A FILE must have CONTENT_TYPE, SIZE, ETAG, and LAST_MODIFIED fields.
    It must also specify the file’s location in one of the following ways:

    * Both STAGE and RELATIVE_PATH
    * STAGE_FILE_URL
    * SCOPED_FILE_URL

## Returns

A [FILE](../data-types-unstructured.md), or NULL.

## Usage notes

Returns NULL when:

* The supplied URL is not validL.
* The file is on a stage that the user lacks privileges to access.
* The supplied metadata doesn’t contain the required FILE fields.

## Examples

Unlike TO_FILE, which raises an error on invalid arguments, TRY_TO_FILE returns NULL in this situation.
It otherwise works exactly like [TO_FILE](to_file.md).

The example below illustrates the behavior of TRY_TO_FILE when given an invalid file path, assuming that
the file `image.png` exists on the stage but the other two files do not.

```sqlexample
SELECT
    TRY_TO_FILE('@mystage/image.png'),
    TRY_TO_FILE('@mystage/incorrect_file1.jpg'),
    TRY_TO_FILE('@mystage', 'incorrect_file2.png');
```

Result:

```output
+-----------------------------------------------------+---------------------------------------------+------------------------------------------------+
| TRY_TO_FILE('@MYSTAGE/IMAGE.PNG')                   | TRY_TO_FILE('@MYSTAGE/INCORRECT_FILE1.JPG') | TRY_TO_FILE('@MYSTAGE', 'INCORRECT_FILE2.PNG') |
|-----------------------------------------------------|---------------------------------------------|------------------------------------------------|
| {                                                   | NULL                                        | NULL                                           |
|   "CONTENT_TYPE": "image/png",                      |                                             |                                                |
|   "ETAG": "2859efde6e26491810f619668280a2ce",       |                                             |                                                |
|   "LAST_MODIFIED": "Thu, 18 Sep 2025 09:02:00 GMT", |                                             |                                                |
|   "RELATIVE_PATH": "image.png",                     |                                             |                                                |
|   "SIZE": 23698,                                    |                                             |                                                |
|   "STAGE": "@MYDB.MYSCHEMA.MYSTAGE"                 |                                             |                                                |
| }                                                   |                                             |                                                |
+-----------------------------------------------------+---------------------------------------------+------------------------------------------------+
```

For more examples of creating FILE objects from valid inputs, see [TO_FILE examples](to_file.md).
