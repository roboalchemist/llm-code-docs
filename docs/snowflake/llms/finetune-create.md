# Source: https://docs.snowflake.com/en/sql-reference/functions/finetune-create.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# FINETUNE ('CREATE') (SNOWFLAKE.CORTEX)

Creates a fine-tuning job. The tuned model is saved to the model registry of the schema.

## Syntax

```sqlsyntax
SNOWFLAKE.CORTEX.FINETUNE(
  'CREATE',
  '<name>',
  '<base_model>',
  '<training_data_query>'
  [
    , '<validation_data_query>'
    [, '<options>' ]
  ]
)
```

## Required parameters

`'CREATE'`
:   Specifies that you want to create a fine-tuning job.

`'name'`
:   The identifier of the fine-tuned model that is saved to the model registry. This must be unique to the model registry it is saved to. If
    more than one model attempts to save using the same name, a suffix is appended to the name of the latter one to make it unique.

    Letters, underscores, decimal digits (0-9) are allowed in the identifier.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`'base_model'`
:   A string specifying the base model to fine-tune. This must be one of the following values:

    * `'llama3-8b'`
    * `'llama3-70b'`
    * `'llama3.1-8b'`
    * `'llama3.1-70b'`
    * `'mistral-7b'`
    * `'mixtral-8x7b'`

    For more information see [Models available to fine-tune](../../user-guide/snowflake-cortex/cortex-finetuning.md).

`'training_data_query'`
:   The SQL query to get the training data. The result must include `prompt` and `completion` columns.

## Optional parameters

`'validation_data_query'`
:   The SQL query to get the validation data. The result must include `prompt` and `completion` columns.
    If a query for validation data is not specified, your training data is automatically split into training and validation data.

`'options'`
:   A string representation of a JSON object containing zero or more of the following options that affect the training
    hyperparameters. For example: `'{"max_epochs": 3}'`

    * `max_epochs`: A value from 1 to 10 (inclusive) that controls the number of epochs to train the model for.

      Default: automatically determined by the system

## Returns

| Column | Type | Description |
| --- | --- | --- |
| FINETUNE | [STRING](../data-types-text.md) | When the tuning job is created, a generated unique job ID is returned. |

## Access control requirements

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE | DATABASE | The database that the training (and validation) data are queried from. |
| CREATE MODEL or OWNERSHIP | SCHEMA | The schema that the model is saved to. |

## Examples

Example with validation data:

```sqlexample
SELECT SNOWFLAKE.CORTEX.FINETUNE(
  'CREATE',
  'my_tuned_model',
  'mistral-7b',
  'SELECT prompt, completion FROM train',
  'SELECT prompt, completion FROM validation'
);
```

Example without validation data:

```sqlexample
SELECT SNOWFLAKE.CORTEX.FINETUNE(
  'CREATE',
  'my_tuned_model',
  'mistral-7b',
  'SELECT prompt, completion FROM train'
);
```

The output is the job ID of the fine-tuning job, such as:

```output
ft_6556e15c-8f12-4d94-8cb0-87e6f2fd2299
```

## Limitations

Snowflake Cortex functions do not support dynamic tables.
