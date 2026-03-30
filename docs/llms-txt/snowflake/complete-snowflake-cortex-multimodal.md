# Source: https://docs.snowflake.com/en/sql-reference/functions/complete-snowflake-cortex-multimodal.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# COMPLETE (SNOWFLAKE.CORTEX) (multimodal)

> **Note:**
>
> [AI_COMPLETE](ai_complete.md) is the latest version of this function.
> Use AI_COMPLETE for the latest functionality.
> You can continue to use COMPLETE (SNOWFLAKE.CORTEX).

Given an image and a prompt, generates a response (completion) using a language model. This function variant supports
image models along with text models, and processes images stored in an internal Snowflake stage or an external stage.
COMPLETE can be used to process a single image, multiple images in a batch fashion, applying the same or a different
prompt to each image, or multiple images in a single operation (for example, comparison).

## Syntax

Use one of the following:

```sqlsyntax
SNOWFLAKE.CORTEX.COMPLETE(
    '<model>', '<prompt>', <file_object>)
FROM <table>
```

```sqlsyntax
SNOWFLAKE.CORTEX.COMPLETE(
    '<model>', <prompt_object> )
FROM <table>
```

## Arguments

`model`
:   A string specifying the model to be used. Specify one of the following models:

    * `claude-3-5-sonnet`
    * `pixtral-large`

    Supported models might have different costs and context windows. New models might be added from time to time.

`prompt`
:   A string containing a question about the image and optionally specifying an output format, such as JSON. Either
    this or the `prompt_object` argument is required.

`prompt_object`
:   A SQL OBJECT containing a string prompt with numbered placeholders (`{0}`, `{1}`, and so on) and one or more text or
    FILE valuse that are inserted into the prompt. The [PROMPT](prompt.md) function is a convenient way to create an object
    with the required layout. Either this argument or `prompt` is required.

`file_object`
:   A FILE object that contains an image file to be processed. Use the [TO_FILE](to_file.md) function to
    create FILE objects from a stage path. Required when using a string prompt.

`FROM table`
:   An optional table containing image paths and an optional prompt for each image, allowing images to be batch-processed
    in a single call to COMPLETE.

## Returns

A string containing the language model’s response.

## Usage notes

* Inputs exceeding the context window limit result in an error. Output which would exceed the context window limit is truncated.
* To process multiple images, the prompt must be an object (typically created using the PROMPT function) that specifies a prompt
  template and the files to be processed.
* Only text and images are supported. Video and audio files are not supported.
* Images with filename extensions `.jpg`, `.jpeg`, `.png`, `.gif`, and `.webp` are supported. `pixtral-large` also supports `.bmp`.
* Maximum image size is 10 MB for `pixtral-large` and 3.75 MB for `claude-3-5-sonnet`. Additionally, `claude-3-5-sonnet` does not support images with a resolution greater than 8000x8000.
* The stage containing the images must have server-side encryption enabled. Client-side encrypted stages are not supported.
* The function does not support custom network policies.
* Stage names are not case-sensitive, but paths are.

## Examples

The following examples demonstrate the basic capabilities of the COMPLETE function with images.

### Visual question answering

A chart of inflation rates is used to answer a question about the data.

```sqlexample
SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet',
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

### Image classification

This example classifies the landmark identified in a single image.

```sqlexample
SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet',
    'Classify the landmark identified in this image. Respond in JSON only with the landmark name.',
    TO_FILE('@myimages', 'Seattle.jpg'));
```

Response:

```output
{"landmark": "Space Needle"}
```

### Entity extraction from an image

This example extracts the entities (objects) from an image and returns the results in JSON format.

```sqlexample
SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet',
    'Extract the kitchen appliances identified in this image. Respond in JSON only with the identified appliances.',
    TO_FILE('@myimages', 'kitchen.png'));
```

Response:

```output
{
    "appliances": [ "microwave","electric stove","oven","refrigerator" ]
}
```

### Batch processing images from a directory or table

For batch processing of multiple images, performing the same operation on each, store the image files in the same stage.
Apply the COMPLETE function to each row of the table.

> **Note:**
>
> The stage must have a [directory table](../../user-guide/data-load-dirtables.md) to retrieve the paths to its files.

First, create the table by retrieving the image locations from the directory, convert these to FILE objects, and
storing the resulting FILE objects in a column in a table. Use SQL like the following:

```sqlexample
CREATE TABLE image_table AS
    (SELECT TO_FILE('@myimages', RELATIVE_PATH) AS img FROM DIRECTORY(@myimages));
```

Then, apply the COMPLETE function to the column containing the FILE objects. The following example classifies each image in the table:

```sqlexample
SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet',
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
SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet',
    PROMPT('Classify the input image {0} in no more than 2 words. Respond in JSON',
        TO_FILE('@myimages', img_path)) AS image_classification
FROM image_table;
```

You can also retrieve the images to be processed directly from a stage’s directory, as shown here:

```sqlexample
SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet',
    PROMPT('Classify the input image {0} in no more than 2 words. Respond in JSON',
        TO_FILE('@myimages', RELATIVE_PATH))) as image_classification
FROM DIRECTORY(@myimages);
```

### Providing images and prompts in a table

To perform a different operation on each image in a table, provide the images and their corresponding prompts in a
table. In the following example, the table contains the stage path of each image in the `img_path` column and the
prompt in the `prompt` column.

```sqlexample
SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet',
    PROMPT('Given the input image {0}, {1}. Respond in JSON',
        TO_FILE('@myimages', img_path), prompt) as image_result)
FROM image_table;
```

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).
