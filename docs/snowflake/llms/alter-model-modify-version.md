# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-model-modify-version.md

# ALTER MODEL … MODIFY VERSION

Modifies a version of a model, changing the version’s comment or metadata.

See also:
:   [ALTER MODEL … ADD VERSION](alter-model-add-version.md), [ALTER MODEL … DROP VERSION](alter-model-drop-version.md)

## Syntax

```sqlsyntax
ALTER MODEL [ IF EXISTS ] <name> MODIFY VERSION <version_or_alias_name> SET
  [ COMMENT = '<string_literal>' ]
  [ METADATA = '<json_metadata>']
```

## Parameters

`name`
:   Specifies the identifier of the model.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`version_or_alias_name`
:   Specifies the identifier of the version, either its version name or its alias. Version names that contain spaces or
    that are case sensitive must be enclosed in double quotes. For information on identifier syntax, see
    [Identifier requirements](../identifiers-syntax.md).

    Aliases must be valid identifiers without double quotes.

    See Usage Notes for more information on aliases.

`SET ...`
:   Specifies one or more model version properties to be set.

    `COMMENT = 'string_literal'`
    :   Sets the comment of the version.

    `METADATA = 'json_metadata'`
    :   Sets the metadata of the version. Metadata is a JSON object that stores key-value pairs of your choosing.

## Usage notes

Aliases are alternative names for model versions. In addition to aliases you create, the following three system aliases are available.

* `DEFAULT` refers to the default version of the model.
* `FIRST` refers to the oldest version of the model by creation time.
* `LAST` refers to the newest version of the model by creation time.
