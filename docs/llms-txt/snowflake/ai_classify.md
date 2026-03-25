# Source: https://docs.snowflake.com/en/sql-reference/functions/ai_classify.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# AI_CLASSIFY

> **Note:**
>
> AI_CLASSIFY is the updated version of [CLASSIFY_TEXT (SNOWFLAKE.CORTEX)](classify_text-snowflake-cortex.md).
> For the latest functionality, use AI_CLASSIFY.

Classifies text or images into categories that you specify.

## Region availability

The following table shows the regions where you can use the AI_CLASSIFY function for both text and images:

| Data type | AWS US West 2  (Oregon) | AWS US East 1  (N. Virginia) | AWS Europe Central 1  (Frankfurt) | AWS Europe West 1  (Ireland) | AWS AP Southeast 2  (Sydney) | AWS AP Northeast 1  (Tokyo) | Azure East US 2  (Virginia) | Azure West Europe  (Netherlands) | AWS  (Cross-Region) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TEXT | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| IMAGE | ✔ | ✔ | ✔ |  |  |  |  |  | ✔ |

## Syntax

```sqlsyntax
AI_CLASSIFY( <input> , <list_of_categories> [, <config_object>] )
```

## Arguments

**Required:**

`input`
:   The string, image, or [prompt](prompt.md) object that you’re classifying.

    For text classification, the input string is case sensitive. Results may vary based on capitalization.

`list_of_categories`
:   An array of categories with at least two unique values. The number of categories is restricted only by the
    token window, but in practice, exceeding twenty categories might reduce classification accuracy.
    Categories are case sensitive.

    Categories can be simple strings or SQL objects of the same type.
    If you’re using objects, you can provide a description for one or more categories to improve classification accuracy.

    For each category, specify the following:

    * `label` (Required): The name of the category.
    * `description` (Optional): Describes the category in no more than 25 words.

    > **Note:**
    >
    > Descriptions count as input tokens, which affects the cost of the classification operation.
    > For more information, see [Cost considerations](../../user-guide/snowflake-cortex/aisql.md).

**Optional:**

`config_object`
:   Configuration settings specified as key/value pairs. Supported keys:

    * `task_description`: A explanation of the classification task that is 50 words or fewer. This can help the model understand the context of the classification task and improve accuracy.
    * `output_mode`: Set to `'multi'` for multi-label classification. Defaults to `'single'` for single-label classification.
    * `examples`: A list of example objects for few-shot learning. Each example must include:

      + `input`: Example text to classify.
      + `labels`: List of correct categories for the input.
      + `explanation`: Explanation of why the input maps to those categories.

## Returns

A serialized object. The object’s `labels` field is an array that specifies the list of categories to which the input belongs.

For single label classification, the `labels` array has exactly one element. For multi-label classification, the `labels` field can have multiple elements.

## Access control requirements

Users must use a role that has the [SNOWFLAKE.CORTEX_USER database role](../snowflake-db-roles.md).
For more information about this privilege, see [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md).

## Usage notes

For best results, follow these guidelines:

* Use plain text in English for the `input` and `list_of_categories`.
* Avoid trying to classify non-prose such as code snippets, logs, or non-English text.
* Avoid using code or formatting that is not open source (such as proprietary languages or formats) in the text. The
  underlying language model is not trained on proprietary formats.
* Don’t use abbreviations, special characters, or jargon in the category labels.
* Use descriptive categories. Avoid using category names such as “Xa4s3” or “category 1”.
* Use mutually exclusive categories.
* Providing a clear task description can improve accuracy when the relationship between the input and categories is unclear or complex.
* Adding label descriptions can improve accuracy, especially when labels are ambiguous or require specific selection
  criteria. Write descriptions that clearly highlight what distinguishes each label from the others.
* Each label, description, and example increases the number of input tokens for every AI_CLASSIFY call, which affects cost.
* Examples can help to improve accuracy.

> **Note:**
>
> AI_CLASSIFY adds a prompt to your input to generate its response. This increases the token count beyond the text that you’ve provided.

## Examples

The following examples use the AI_CLASSIFY function with only the required arguments.

### AI_CLASSIFY: Text

The following example classifies the prompt into one of two categories, travel or cooking:

```sqlexample
SELECT AI_CLASSIFY('One day I will see the world', ['travel', 'cooking']);
```

The following is the output of the preceding command.

```output
'{
  "labels": ["travel"]
 }';
```

The following example uses multi-label classification:

```sqlexample
SELECT AI_CLASSIFY(
  'One day I will see the world and learn to cook my favorite dishes',
  ['travel', 'cooking', 'reading', 'driving'],
  {'output_mode': 'multi'}
);
```

The following is the output of the preceding command.

```output
'{
  "labels": ["travel", "cooking"]
 }';
```

The following example passes in a task description, label descriptions, and few-shot examples:

```sqlexample
SELECT AI_CLASSIFY(
  'One day I will see the world and learn to cook my favorite dishes',
  [
    {'label': 'travel', 'description': 'content related to traveling'},
    {'label': 'cooking'},
    {'label': 'reading'},
    {'label': 'driving'}
  ],
  {
    'task_description': 'Determine topics related to the given text',
    'output_mode': 'multi',
    'examples': [
      {
        'input': 'i love traveling with a good book',
        'labels': ['travel', 'reading'],
        'explanation': 'the text mentions traveling and a good book which relates to reading'
      }
    ]
  });
```

The following is the output of the preceding command.

```output
'{
  "labels": ["travel", "cooking"]
}';
```

The following example creates a `text_classification_table` that contains a column for text and a column for possible
categories for that text. The AI_CLASSIFY function is called on each row of the table to classify the string in the text
column.

```sqlexample
CREATE OR REPLACE TEMPORARY TABLE text_classification_table AS
SELECT 'France' AS input, ['North America', 'Europe', 'Asia'] AS classes
UNION ALL
SELECT 'Singapore', ['North America', 'Europe', 'Asia']
UNION ALL
SELECT 'one day I will see the world', ['travel', 'cooking', 'dancing']
UNION ALL
SELECT 'my lobster bisque is second to none', ['travel', 'cooking', 'dancing'];

SELECT input,
    classes,
    AI_CLASSIFY(input, classes):labels AS classification
FROM text_classification_table;
```

### AI_CLASSIFY: Images

Using single file input:

```sqlexample
WITH food_pictures AS (
  SELECT
      TO_FILE(file_url) AS img
  FROM DIRECTORY(@file_stage)
)
SELECT
*,
AI_CLASSIFY(img, ['dessert', 'drink', 'main dish', 'side dish']):labels AS classification
FROM food_pictures;
```

Using a prompt object constructed by PROMPT():

```sqlexample
  WITH food_pictures AS (
  SELECT
      TO_FILE(file_url) AS img
  FROM DIRECTORY(@file_stage)
)
SELECT
*,
AI_CLASSIFY(PROMPT('Please help me classify the food within this image {0}', img),
  ['dessert', 'drink', 'main dish', 'side dish']):labels AS classification
FROM food_pictures;
```

## Limitations

* Snowflake AI functions don’t work on FILE objects created from files in the following kinds of stages:

  * Internal stages with encryption mode `TYPE = 'SNOWFLAKE_FULL'`
  * External stages with any customer-side encrypted mode:

    * `TYPE = 'AWS_CSE'`
    * `TYPE = 'AZURE_CSE'`
  * User stage
  * Table stage
  * Stage with double-quoted names
