# Source: https://docs.snowflake.com/en/sql-reference/functions/ai_complete.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions) ,
    [File functions](../functions-file.md) (AI Functions)

# AI_COMPLETE

> **Note:**
>
> AI_COMPLETE is the updated version of [COMPLETE (SNOWFLAKE.CORTEX)](complete-snowflake-cortex.md).
> For the latest functionality, use AI_COMPLETE.

Generates a response (completion) from text or an image using a supported language model. You can provide:

* A text prompt, to generate a response from the model. For more information, see [AI_COMPLETE (Single string)](ai_complete-single-string.md).
* A single image and a text prompt, to generate a response based on the image and prompt. For more information, see [AI_COMPLETE (Single image)](ai_complete-single-file.md).
* A prompt object that can support multiple images and text. For more information, see [AI_COMPLETE (Prompt object)](ai_complete-prompt-object.md).

## Syntax

The syntax for the function depends on the type of input that you provide. For information about the syntax, see the following sections:

* [Single string arguments](ai_complete-single-string.md)
* [Single image arguments](ai_complete-single-file.md)
* [Prompt object arguments](ai_complete-prompt-object.md)

## Access control requirements

Users must use a role that has been granted the [SNOWFLAKE.CORTEX_USER database role](../snowflake-db-roles.md).
See [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md) for more information on this privilege.

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md) for legal notices.

## Limitations

Snowflake Cortex functions do not support dynamic tables.
