# Source: https://docs.snowflake.com/en/sql-reference/functions/finetune-cancel.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# FINETUNE ('CANCEL') (SNOWFLAKE.CORTEX)

Cancels the specified fine-tuning job from the current schema.

## Syntax

```sqlsyntax
SNOWFLAKE.CORTEX.FINETUNE(
  'CANCEL',
  '<finetune_job_id>'
)
```

## Parameters

`'CANCEL'`
:   Specifies that you want to cancel a fine-tuning job.

`finetune_job_id`
:   The ID of the fine-tuning job that was generated when you created the job.

## Output

| Column | Type | Description |
| --- | --- | --- |
| SNOWFLAKE.CORTEX.FINETUNE | [STRING](../data-types-text.md) | Message that the job was canceled. |

## Access control requirements

For access requirements, see [Access control requirements](../../user-guide/snowflake-cortex/cortex-finetuning.md).

## Examples

```sqlexample
SELECT SNOWFLAKE.CORTEX.FINETUNE(
  'CANCEL',
  'ft_194bbea4-1208-42f3-88c6-cfb202086125'
);
```

```output
Canceled Cortex Fine-tuning job: ft_194bbea4-1208-42f3-88c6-cfb202086125
```

## Limitations

Snowflake Cortex functions do not support dynamic tables.
