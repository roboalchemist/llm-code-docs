# Source: https://docs.snowflake.com/en/sql-reference/functions/ai_complete-prompt-object.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# AI_COMPLETE (Prompt object)

> **Note:**
>
> AI_COMPLETE is the updated version of [COMPLETE (SNOWFLAKE.CORTEX)](complete-snowflake-cortex.md).
> For the latest functionality, use AI_COMPLETE.

Generates a response (completion) for a prompt object. The prompt can contain [FILE objects](to_file.md), which may contain images or documents.

[Preview Feature](../../release-notes/preview-features.md) — Open

The document processing capability of AI_COMPLETE is currently in preview. All other capabilities are generally available.

## Syntax

The function can be used with either positional or named argument syntax.

```sqlsyntax
AI_COMPLETE(
    <model>, <prompt> [ , <model_parameters> ] )
```

## Arguments

`model`
:   A string specifying the model to be used. For text only inputs, you can use one of the following models:

    * `claude-4-opus`
    * `claude-4-sonnet`
    * `claude-3-7-sonnet`
    * `claude-3-5-sonnet`
    * `deepseek-r1`
    * `llama3-8b`
    * `llama3-70b`
    * `llama3.1-8b`
    * `llama3.1-70b`
    * `llama3.1-405b`
    * `llama3.3-70b`
    * `llama4-maverick`
    * `llama4-scout`
    * `mistral-large`
    * `mistral-large2`
    * `mistral-7b`
    * `mixtral-8x7b`
    * `openai-gpt-4.1`
    * `openai-o4-mini`
    * `snowflake-arctic`
    * `snowflake-llama-3.1-405b`
    * `snowflake-llama-3.3-70b`

    For image inputs, you can use one of the following models:

    * `claude-4-opus`
    * `claude-4-sonnet`
    * `claude-3-7-sonnet`
    * `claude-haiku-4-5`
    * `claude-sonnet-4-5`
    * `claude-opus-4-5`
    * `claude-sonnet-4-6`
    * `claude-opus-4-6`
    * `llama4-maverick`
    * `llama4-scout`
    * `pixtral-large`
    * `openai-o4-mini`
    * `openai-gpt-4.1`
    * `openai-gpt-5`
    * `openai-gpt-5-chat`
    * `openai-gpt-5-mini`
    * `openai-gpt-5-nano`
    * `openai-gpt-5.1`
    * `openai-gpt-5.2`
    * `gemini-2.5-flash`
    * `gemini-2.5-flash-lite`
    * `gemini-3-pro`

    For document inputs, you can use one of the following models:

    * `gemini-3-pro`
    * `claude-4-opus`
    * `claude-4-sonnet`
    * `claude-3-7-sonnet`
    * `claude-haiku-4-5`
    * `claude-sonnet-4-5`
    * `claude-opus-4-5`

    Supported models might have different [costs](../../user-guide/snowflake-cortex/aisql.md).

`prompt`
:   A [prompt](prompt.md) object containing text and, optionally, images or documents.

`model_parameters`
An [object](../data-types-semistructured.md) containing zero or more of the following options that affect the model’s
hyperparameters. See [LLM Settings](https://www.promptingguide.ai/introduction/settings).

> * `temperature`: A value from 0 to 1 (inclusive) that controls the randomness of the output of the language model. A
>   higher temperature (for example, 0.7) results in more diverse and random output, while a lower temperature (such as
>   0.2) makes the output more deterministic and focused.
>
>   Default: 0
> * `top_p`: A value from 0 to 1 (inclusive) that controls the randomness and diversity of the language model,
>   generally used as an alternative to `temperature`. The difference is that `top_p` restricts the set of possible tokens
>   that the model outputs, while `temperature` influences which tokens are chosen at each step.
>
>   Default: 0
> * `max_tokens`: Sets the maximum number of output tokens in the response. Small values can result in truncated responses.
>
>   Default: 4096
>   Maximum allowed value: 8192
> * `guardrails`: Filters potentially unsafe and harmful responses from a language model using [Cortex Guard](../../user-guide/snowflake-cortex/aisql.md).
>   Either `TRUE` or `FALSE`. The default value is `FALSE`.

> **Important:**
>
> If you’re using AI_COMPLETE with a prompt object, you can’t provide a JSON schema to get a structured output as a response.
>
> To get a structured output as the response, use the `response_format` parameter with [AI_COMPLETE (Single string)](ai_complete-single-string.md). For more information using structured outputs, see [AI_COMPLETE structured outputs](../../user-guide/snowflake-cortex/complete-structured-outputs.md).

## Example

### Passing multiple images as the input

The following example compares two images by passing both as input to the AI_COMPLETE function and asking whether both are pictures of cats:

```sqlexample
SELECT AI_COMPLETE('claude-3-5-sonnet',
  PROMPT('Are both image {0} and image {1} pictures of cats?',
    TO_FILE('@myimages', 'sleepingcat.png'), TO_FILE('@myimages', 'jumpingcat.png'))) AS image_classification;
```

### Batch processing images from a directory or table

For batch processing of multiple images, performing the same operation on each, store the image files in the same stage.
Apply the AI_COMPLETE function to each row of the table.

> **Note:**
>
> The stage must have a [directory table](../../user-guide/data-load-dirtables.md) to retrieve the paths to its files.

First, create the table by retrieving the image locations from the directory, convert these to FILE objects, and
storing the resulting FILE objects in a column in a table. Use SQL like the following:

```sqlexample
CREATE TABLE image_table AS
    (SELECT TO_FILE('@myimages', RELATIVE_PATH) AS img FROM DIRECTORY(@myimages));
```

Then, apply the AI_COMPLETE function to the column containing the FILE objects. The following example classifies each image in the table:

```sqlexample
SELECT AI_COMPLETE('claude-3-5-sonnet',
    PROMPT('Classify the input image {0} in no more than 2 words. Respond in JSON', img_file)) AS image_classification
FROM image_table;
```

Response:

```output
{ "classification": "Inflation Rates" }
{ "classification": "beverage refrigerator" }
{ "classification": "Space Needle" }
{ "classification": "Modern Kitchen" }
{ "classification": "Pie Chart" }
{ "classification": "Economic Graph" }
{ "classification": "Persian Cat" }
{ "classification": "Labrador Retriever" }
{ "classification": "Jedi Cat" }
{ "classification": "Sleeping cat" }
{ "classification": "Persian Cat" }
{ "classification": "Garden Costume" }
{ "classification": "Floral Fashion" }
```

If you already have a table with paths to the images, you can use the [TO_FILE function](to_file.md) to construct the FILE
objects within the query:

```sqlexample
SELECT AI_COMPLETE('claude-3-5-sonnet',
    PROMPT('Classify the input image {0} in no more than 2 words. Respond in JSON',
        TO_FILE('@myimages', img_path)) AS image_classification
FROM image_table;
```

You can also retrieve the images to be processed directly from a stage’s directory, as shown here:

```sqlexample
SELECT AI_COMPLETE('claude-3-5-sonnet',
    PROMPT('Classify the input image {0} in no more than 2 words. Respond in JSON',
        TO_FILE('@myimages', RELATIVE_PATH))) as image_classification
FROM DIRECTORY(@myimages);
```

### Providing images and prompts in a table

To perform a different operation on each image in a table, provide the images and their corresponding prompts in a
table. In the following example, the table contains the stage path of each image in the `img_path` column and the
prompt in the `prompt` column.

```sqlexample
AI_COMPLETE('claude-3-5-sonnet',
    PROMPT('Given the input image {0}, {1}. Respond in JSON',
        TO_FILE('@myimages', img_path), prompt) as image_result)
FROM image_table;
```

## Usage notes for processing images

* To process multiple images, specify a prompt object in the function call that defines a prompt template and the associated image files. You can use the [PROMPT](prompt.md) function to create this object. The prompt template can contain numbered placeholders (`{0}`, `{1}`, etc.) that correspond to the images in the prompt object. Use the [TO_FILE](to_file.md) function to specify the document files in the prompt object.
* Only text and images are supported. Video and audio files are not supported.
* Supported image formats:

  * `.jpg`
  * `.jpeg`
  * `.png`
  * `.gif`
  * `.webp`

  The `pixtral` and `llama4` models also support `.bmp`.
* The maximum image size is 10 MB for most models, and 3.75 MB for `claude` models. `claude` models do not support images with resolutions above 8000x8000.
* The stage containing the images must have server-side encryption enabled. Client-side encrypted stages are not supported.
* The function does not support custom network policies.
* Stage names are case-insensitive; paths are case-sensitive.

## Usage notes for processing documents

* To process multiple documents, specify a prompt object in the function call that defines a prompt template and the associated document files. You can use the [PROMPT](prompt.md) function to create this object. The prompt template can contain numbered placeholders (`{0}`, `{1}`, etc.) that correspond to the documents in the prompt object. Use the [TO_FILE](to_file.md) function to specify the document files in the prompt object.
* Only text and documents are supported. Video and audio files are not supported.
* All models support these formats: `.txt`, `.md`, and `.pdf`. Claude models also support `.txt`, `.md`, `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.csv`, and `.xhtml`.
* Claude models have a maximum document size of 4.5 MB. Gemini 3 Pro has a maximum document size of 10 MB.
* The function does not support custom network policies.
* Stage names are case-insensitive; paths are case-sensitive.
