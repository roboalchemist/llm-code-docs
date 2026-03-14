# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-file-format.md

# DESCRIBE FILE FORMAT

Describes the property type (for example, `String` or `Integer`), the defined value of the property, and the default value for each property in a file format object definition. For more information about available properties for each file type, see “[Format type options](create-file-format.md)” in [CREATE FILE FORMAT](create-file-format.md).

DESCRIBE can be abbreviated to DESC.

See also:
:   [DROP FILE FORMAT](drop-file-format.md) , [ALTER FILE FORMAT](alter-file-format.md) , [CREATE FILE FORMAT](create-file-format.md) , [SHOW FILE FORMATS](show-file-formats.md)

## Syntax

```sqlsyntax
DESC[RIBE] FILE FORMAT <name>
```

## Parameters

`name`
:   Specifies the identifier for the file format to describe. If the identifier contains spaces or special characters, the entire string
    must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Usage notes

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Examples

Describe the file format object named `my_csv_format`:

> ```sqlexample
> DESC FILE FORMAT my_csv_format;
> ```
>
> Output:
>
> > ```output
> > +--------------------------------+---------------+----------------+------------------+
> > | property                       | property_type | property_value | property_default |
> > +--------------------------------+---------------+----------------+------------------+
> > | TYPE                           | String        | csv            | CSV              |
> > | RECORD_DELIMITER               | String        | \n             | \n               |
> > | FIELD_DELIMITER                | String        | ,              | ,                |
> > | FILE_EXTENSION                 | String        |                |                  |
> > | SKIP_HEADER                    | Integer       | 0              | 0                |
> > | PARSE_HEADER                   | Boolean       | FALSE          | FALSE            |
> > | DATE_FORMAT                    | String        | AUTO           | AUTO             |
> > | TIME_FORMAT                    | String        | AUTO           | AUTO             |
> > | TIMESTAMP_FORMAT               | String        | AUTO           | AUTO             |
> > | BINARY_FORMAT                  | String        | HEX            | HEX              |
> > | ESCAPE                         | String        | NONE           | NONE             |
> > | ESCAPE_UNENCLOSED_FIELD        | String        | \\             | \\               |
> > | TRIM_SPACE                     | Boolean       | FALSE          | FALSE            |
> > | FIELD_OPTIONALLY_ENCLOSED_BY   | String        | NONE           | NONE             |
> > | NULL_IF                        | List          | [\\N]          | [\\N]            |
> > | COMPRESSION                    | String        | AUTO           | AUTO             |
> > | ERROR_ON_COLUMN_COUNT_MISMATCH | Boolean       | TRUE           | TRUE             |
> > | VALIDATE_UTF8                  | Boolean       | TRUE           | TRUE             |
> > | SKIP_BLANK_LINES               | Boolean       | FALSE          | FALSE            |
> > | REPLACE_INVALID_CHARACTERS     | Boolean       | FALSE          | FALSE            |
> > | EMPTY_FIELD_AS_NULL            | Boolean       | TRUE           | TRUE             |
> > | SKIP_BYTE_ORDER_MARK           | Boolean       | TRUE           | TRUE             |
> > | ENCODING                       | String        | UTF8           | UTF8             |
> > +--------------------------------+---------------+----------------+------------------+
> > ```

Describe the file format object named `my_json_format`:

> ```sqlexample
> DESC FILE FORMAT `my_json_format`;
> ```
>
> Output:
>
> > ```output
> > +----------------------------+---------------+----------------+------------------+
> > | property                   | property_type | property_value | property_default |
> > +----------------------------+---------------+----------------+------------------+
> > | TYPE                       | String        | JSON           | CSV              |
> > | FILE_EXTENSION             | String        |                |                  |
> > | DATE_FORMAT                | String        | AUTO           | AUTO             |
> > | TIME_FORMAT                | String        | AUTO           | AUTO             |
> > | TIMESTAMP_FORMAT           | String        | AUTO           | AUTO             |
> > | BINARY_FORMAT              | String        | HEX            | HEX              |
> > | TRIM_SPACE                 | Boolean       | FALSE          | FALSE            |
> > | NULL_IF                    | List          | []             | [\\N]            |
> > | COMPRESSION                | String        | AUTO           | AUTO             |
> > | ENABLE_OCTAL               | Boolean       | FALSE          | FALSE            |
> > | ALLOW_DUPLICATE            | Boolean       | FALSE          | FALSE            |
> > | STRIP_OUTER_ARRAY          | Boolean       | FALSE          | FALSE            |
> > | STRIP_NULL_VALUES          | Boolean       | FALSE          | FALSE            |
> > | IGNORE_UTF8_ERRORS         | Boolean       | FALSE          | FALSE            |
> > | REPLACE_INVALID_CHARACTERS | Boolean       | FALSE          | FALSE            |
> > | SKIP_BYTE_ORDER_MARK       | Boolean       | TRUE           | TRUE             |
> > +----------------------------+---------------+----------------+------------------+
> > ```

Describe the file format object named `my_parquet_format`:

> ```sqlexample
> DESC FILE FORMAT `my_parquet_format`;
> ```
>
> Output:
>
> > ```output
> > +----------------+---------------+----------------+------------------+
> > | property       | property_type | property_value | property_default |
> > +----------------+---------------+----------------+------------------+
> > | TYPE           | String        | PARQUET        | CSV              |
> > | TRIM_SPACE     | Boolean       | FALSE          | FALSE            |
> > | NULL_IF        | List          | []             | [\\N]            |
> > | COMPRESSION    | String        | SNAPPY         | AUTO             |
> > | BINARY_AS_TEXT | Boolean       | TRUE           | TRUE             |
> > +----------------+---------------+----------------+------------------+
> > ```
