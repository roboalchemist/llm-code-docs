# Source: https://docs.snowflake.com/en/sql-reference/functions/finetune-snowflake-cortex.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# FINETUNE (SNOWFLAKE.CORTEX)

This function lets you create and manage large language models customized for your specific task.

## Syntax

```sqlsyntax
FINETUNE (
  { 'CREATE' | 'SHOW' | 'DESCRIBE' | 'CANCEL' }
  ...
  )
```

The syntax varies considerably between the different commands. For specific syntax, usage notes, and examples, see:

* [FINETUNE ('CREATE') (SNOWFLAKE.CORTEX)](finetune-create.md)
* [FINETUNE ('DESCRIBE') (SNOWFLAKE.CORTEX)](finetune-describe.md)
* [FINETUNE ('SHOW') (SNOWFLAKE.CORTEX)](finetune-show.md)
* [FINETUNE ('CANCEL') (SNOWFLAKE.CORTEX)](finetune-cancel.md)

## Access control requirements

For access requirements, see [Access control requirements](../../user-guide/snowflake-cortex/cortex-finetuning.md).

## Limitations

Snowflake Cortex functions do not support dynamic tables.
