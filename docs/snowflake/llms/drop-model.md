# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-model.md

# DROP MODEL

Removes a machine learning model from the current/specified schema.

See also:
:   [CREATE MODEL](create-model.md) , [ALTER MODEL](alter-model.md) , [SHOW MODELS](show-models.md)

## Syntax

```sqlsyntax
DROP MODEL <name>
```

## Parameters

`name`
:   Specifies the identifier for the model to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

    If the model identifier is not fully-qualified (in the form of `db_name.schema_name.model_name` or
    `schema_name.model_name`), the command looks for the model in the current schema for the session.

## Usage notes

* All versions in the model are dropped along with the model.
* There is no UNDROP MODEL command. To restore a dropped model, train and log it again.
