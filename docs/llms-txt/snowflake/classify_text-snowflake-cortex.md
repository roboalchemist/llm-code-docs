# Source: https://docs.snowflake.com/en/sql-reference/functions/classify_text-snowflake-cortex.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# CLASSIFY_TEXT (SNOWFLAKE.CORTEX)

> **Note:**
>
> [AI_CLASSIFY](ai_classify.md) is the latest version of this function.
> You can use AI_CLASSIFY for multi-label and image classification.
> You can continue to use CLASSIFY_TEXT (SNOWFLAKE.CORTEX).

Classifies free-form text into categories that you provide.

## Syntax

```sqlsyntax
SNOWFLAKE.CORTEX.CLASSIFY_TEXT( <input> , <list_of_categories>, [ <options> ] )
```

## Arguments

**Required:**

`input`
:   String to classify. The input string is case sensitive. You may get different results for the same string that uses different
    capitalization.

`list_of_categories`
:   Array that represents the categories. Must contain at least two and at most 100 unique categories. Categories are case
    sensitive.

    Categories may be simple strings or SQL objects; all categories must be the same type. Using objects, you can
    provide a description and examples of each category, providing context that can help improve classification accuracy.
    It is not required to provide descriptions or examples for each category; you are free to provide a description,
    examples, both, or neither for each category.

    * `label`: The name of the category. This key is required.
    * `description`: A description of the category. Descriptions should be no longer than about 25 words (1-2 sentences) long.
      This key is optional.
    * `examples`: An array of examples that are representative of the category. Typically no more than five examples are needed,
      but there is a limit of 20 examples per category. The number of examples does not need to be the same for every category.
      This key is optional.

    > **Note:**
    >
    > Descriptions and examples count as input tokens, which increases the cost of the classification operation. Read
    > more in [Cost considerations](../../user-guide/snowflake-cortex/aisql.md).

**Optional:**

`options`
:   An object that contains optional configuration (as key/value pairs) for the classification operation. Currently, the
    only available key is:

    * `task_description`: A string containing a short explanation of the text classification task. Task descriptions should
      be no more than about 50 words (3-4 sentences) long.

## Returns

An OBJECT value (VARIANT). The object’s `label` field is a string specifying the category to which the input prompt belongs.

## Access control requirements

Users must use a role that has been granted the [SNOWFLAKE.CORTEX_USER database role](../snowflake-db-roles.md).
See [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md) for more information on this privilege.

## Usage notes

For optimal performance, follow these guidelines:

* Use plain English text for input and categories.
* Limit the amount of text that is not plain English in the input text. For example, try to limit content such as code snippets or logs
  in the text input.
* Text shouldn’t contain code or formats that are not open source (company specific languages, proprietary formats, etc.). The function
  won’t return an error, but the results may not be what you expect.
* Don’t use abbreviations, special characters, or jargon in the category labels.
* Categories should be descriptive. For example using a category such as `Xa4s3` or `category 1` won’t produce good results.
* Categories should be mutually exclusive.
* Adding a clear task description can improve accuracy when the relationship between the input text and categories is
  ambiguous or nuanced.
* Adding label descriptions can improve accuracy in cases where the descriptions are ambiguous or when specific logic
  should be followed when selecting a particular label. When writing descriptions, focus on key aspects that distinguish
  a particular label from the others.
* Each label, description, and example counts as input tokens for each record processed by a CLASSIFY_TEXT function call.
  Costs are incurred accordingly.
* Examples can help to improve accuracy.

## Examples

### Using required arguments

These examples illustrate how to use the CLASSIFY_TEXT function with only the required arguments.

The following example classifies the prompt into one of two categories, `travel` or `cooking`:

```sqlexample
SELECT SNOWFLAKE.CORTEX.CLASSIFY_TEXT('One day I will see the world', ['travel', 'cooking']);
```

```output
{
  "label": "travel"
}
```

The following example creates a table, `text_classification_table`, that contains a column for text and a column for possible
categories for that text. The CLASSIFY_TEXT function is called on each row of the table to classify the string in the text column.

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
       SNOWFLAKE.CORTEX.CLASSIFY_TEXT(input, classes)['label'] as classification
FROM text_classification_table;
```

### Using optional arguments

These examples illustrate how to use the CLASSIFY_TEXT function with category descriptions and examples and/or a task description.

The following example classifies the prompt into one of three categories (travel, cooking, or fitness), providing only a task description:

```sqlexample
SELECT SNOWFLAKE.CORTEX.CLASSIFY_TEXT(
  'When I am not at work, I love creating recipes using every day ingredients',
  ['travel', 'cooking', 'fitness'],
  {
    'task_description': 'Return a classification of the Hobby identified in the text'
  }
);
```

```output
{
  "label": "cooking"
}
```

The following example classifies the prompt into one of the categories, travel, cooking, or fitness using all of the options.

```sqlexample
SELECT SNOWFLAKE.CORTEX.CLASSIFY_TEXT(
  'I love running every morning before the world wakes up',
  [{
    'label': 'travel',
    'description': 'Hobbies related to going from one place to another',
    'examples': ['I like flying to Europe', 'Every summer we go to Italy' , 'I love traveling to learn new cultures']
  },{
    'label': 'cooking',
    'description': 'Hobbies related to preparing food',
    'examples': ['I like learning about new ingredients', 'You must bring your soul to the recipe' , 'Baking is my therapy']
    },{
    'label': 'fitness',
    'description': 'Hobbies related to being active and healthy',
    'examples': ['I cannot live without my Strava app', 'Running is life' , 'I go to the Gym every day']
    }],
  {'task_description': 'Return a classification of the Hobby identified in the text'})
```

```output
{
  "label": "fitness"
}
```

The following example classifies the prompt into one of three categories (travel, cooking, or fitness) using all of the
options. However, the description or examples are omitted for some categories, and the number of examples varies.

```sqlexample
SELECT SNOWFLAKE.CORTEX.CLASSIFY_TEXT(
  'I love running every morning before the world wakes up',
  [{
    'label': 'travel',
    'description': 'Hobbies related to going from one place to another',
    'examples': ['I like flying to Europe']
  },{
    'label': 'cooking',
    'examples': ['I like learning about new ingredients', 'You must bring your soul to the recipe' , 'Baking is my therapy']
    },{
    'label': 'fitness',
    'description': 'Hobbies related to being active and healthy'
    }],
  {'task_description': 'Return a classification of the Hobby identified in the text'})
```

```output
{
  "label": "fitness"
}
```

## Limitations

Snowflake Cortex functions do not support dynamic tables.
