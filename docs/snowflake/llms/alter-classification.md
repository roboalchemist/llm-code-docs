# Source: https://docs.snowflake.com/en/sql-reference/classes/classification/commands/alter-classification.md

# ALTER SNOWFLAKE.ML.CLASSIFICATION

You can change the name, description, and tags of a classification model object using forms of the ALTER command. Models
themselves are immutable and cannot be updated in place. To update a model, drop the existing model and train a new one.

See also:
:   [CREATE SNOWFLAKE.ML.CLASSIFICATION](create-classification.md)

## Syntax

Rename a model:

```sqlsyntax
ALTER SNOWFLAKE.ML.CLASSIFICATION [ IF EXISTS ] <name>
    RENAME TO '<new_model_name>';
```

Set or change a [tag](../../../../user-guide/object-tagging/introduction.md) value on a model:

```sqlsyntax
ALTER SNOWFLAKE.ML.CLASSIFICATION  [ IF EXISTS ] <name>
    SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ];
```

Set or change a model’s comment:

```sqlsyntax
ALTER SNOWFLAKE.ML.CLASSIFICATION [ IF EXISTS ] <name>
    SET COMMENT = '<string_literal>';
```

Remove a [tag](../../../../user-guide/object-tagging/introduction.md) from a model:

```sqlsyntax
ALTER SNOWFLAKE.ML.CLASSIFICATION [ IF EXISTS ] <name>
    UNSET TAG <tag_name> [ , <tag_name> ... ];
```

Remove a model’s comment:

```sqlsyntax
ALTER SNOWFLAKE.ML.CLASSIFICATION [ IF EXISTS ] <name>
    UNSET COMMENT;
```
