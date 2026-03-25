# Source: https://docs.snowflake.com/en/sql-reference/functions/ai_complete-single-file.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# AI_COMPLETE (Single image)

> **Note:**
>
> AI_COMPLETE is the updated version of [COMPLETE (SNOWFLAKE.CORTEX)](complete-snowflake-cortex.md).
> For the latest functionality, use AI_COMPLETE.

Generates a response (completion) for a text prompt using a supported language model. This variant of the function enhances AI_COMPLETE with document understanding capabilities. The prompt can reference information or images found in a file containing a document. The function supports a single document input.

## Syntax

The function has two required arguments and four optional arguments.
The function can be used with either positional or named argument syntax.

Using AI_COMPLETE with a single image input:

```sqlsyntax
AI_COMPLETE(
    <model>, <predicate>, <file> [, <model_parameters> ] )
```

## Arguments

`model`
:   A string specifying the model to be used. Specify one of the following models:

    > * `claude-4-opus`
    > * `claude-4-sonnet`
    > * `claude-3-7-sonnet`
    > * `claude-3-5-sonnet`
    > * `llama4-maverick`
    > * `llama4-scout`
    > * `openai-o4-mini`
    > * `openai-gpt-4.1`
    > * `pixtral-large`

    Supported models might have different [costs](../../user-guide/snowflake-cortex/aisql.md).

`predicate`
:   A string prompt.

`file`
:   A FILE type object representing an image.

`model_parameters`
:   An [object](../data-types-semistructured.md) containing zero or more of the following options that affect the model’s
    hyperparameters. See [LLM Settings](https://www.promptingguide.ai/introduction/settings).

    * `temperature`: A value from 0 to 1 (inclusive) that controls the randomness of the output of the language model. A
      higher temperature (for example, 0.7) results in more diverse and random output, while a lower temperature (such as
      0.2) makes the output more deterministic and focused.

      Default: 0
    * `top_p`: A value from 0 to 1 (inclusive) that controls the randomness and diversity of the language model,
      generally used as an alternative to `temperature`. The difference is that `top_p` restricts the set of possible tokens
      that the model outputs, while `temperature` influences which tokens are chosen at each step.

      Default: 0
    * `max_tokens`: Sets the maximum number of output tokens in the response. Small values can result in truncated responses.

      Default: 4096
      Maximum allowed value: 8192
    * `guardrails`: Filters potentially unsafe and harmful responses from a language model using [Cortex Guard](../../user-guide/snowflake-cortex/aisql.md).
      Either `TRUE` or `FALSE`. The default value is `FALSE`.

## Returns

Returns the string response from the language model.

## Examples

The following examples demonstrate the basic capabilities of the COMPLETE function with images.

### Visual question answering

A chart of inflation rates is used to answer a question about the data.

```sqlexample
SELECT AI_COMPLETE('claude-3-5-sonnet',
    'Which country will observe the largest inflation change in 2024 compared to 2023?',
    TO_FILE('@myimages', 'highest-inflation.png'));
```

Response:

```output
Looking at the data, Venezuela will experience the largest change in inflation rates between 2023 and 2024.
The inflation rate in Venezuela is projected to decrease significantly from 337.46% in 2023 to 99.98% in 2024,
representing a reduction of approximately 237.48 percentage points. This is the most dramatic change among
all countries shown in the chart, even though Zimbabwe has higher absolute inflation rates.
```

### Entity extraction from an image

This example extracts the entities (objects) from an image and returns the results in JSON format.

```sqlexample
SELECT AI_COMPLETE('claude-3-5-sonnet',
    'Extract the kitchen appliances identified in this image. Respond in JSON only with the identified appliances.',
    TO_FILE('@myimages', 'kitchen.png'));
```

Response:

```output
{
    "appliances": [ "microwave","electric stove","oven","refrigerator" ]
}
```

## Usage notes for processing images

* Only text and images are supported. Video and audio files are not supported.
* Supported image formats:

  * `.jpg`
  * `.jpeg`
  * `.png`
  * `.gif`
  * `.webp`
  * `pixtral` and `llama4` models also support `.bmp`.
* The maximum image size is 10 MB for most models, and 3.75 MB for `claude` models. `claude` models do not support images with resolutions above 8000x8000.
* The stage containing the images must have server-side encryption enabled. Client-side encrypted stages are not supported.
* The function does not support custom network policies.
* Stage names are case-insensitive; paths are case-sensitive.
