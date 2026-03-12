# Source: https://docs.snowflake.com/en/sql-reference/functions/ai_count_tokens.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# AI_COUNT_TOKENS

> **Note:**
>
> AI_COUNT_TOKENS is the updated version of [COUNT_TOKENS (SNOWFLAKE.CORTEX)](count_tokens-snowflake-cortex.md).
> For the latest functionality, use AI_COUNT_TOKENS.

Returns an estimate of the number of tokens in a prompt for the specified large language model or task-specific
function. For functions that can take additional inputs that affect token count, such as model name or
categories/labels, those inputs can also be specified.

## Syntax

The syntax can vary based on the function used. In general, you pass the function name, model name if applicable,
input text, and any additional options that affect token count.

```sqlsyntax
AI_COUNT_TOKENS(<function_name>, <input_text> )
AI_COUNT_TOKENS( <function_name>, <model_name> , <input_text> )
AI_COUNT_TOKENS( <function_name>, <input_text>, <options> )
AI_COUNT_TOKENS( <function_name>, <model_name>, <input_text>, <options> )
```

AI_COUNT_TOKENS uses specific syntax variations for some functions. For example:

```sqlsyntax
AI_COUNT_TOKENS( 'ai_similarity', <input_text_1>, <input_text_2>, <options> )
AI_COUNT_TOKENS( 'ai_classify', <input_text>, <categories> )
AI_COUNT_TOKENS( 'ai_translate', <input_text>, <source_language>, <target_language> )
```

See Examples for function specific usage patterns.

## Arguments

**Required:**

`function_name`
:   String containing the name of the function you want to base the token count on, such as `'ai_complete'` or `'ai_sentiment'`.
    The function’s name must begin with “ai_” and use only lowercase letters.

    A complete list of supported functions is available in the [Regional availability](../../user-guide/snowflake-cortex/aisql.md) table.

`input_text` or `input_text_1`, `input_text_2`
:   Input text to count the tokens in.

**Optional:**

`model_name`
:   String containing the name of the model you want to base the token content on. Required if the function specified by
    `function_name` requires you to choose the model to use, such as AI_COMPLETE or AI_EMBED.

    A list of available LLM models is available in the [Regional availability](../../user-guide/snowflake-cortex/aisql.md) table. However, not all models are
    currently supported. Snowflake intends to add support for additional models over time.

    For AI_COMPLETE, the following models are not supported:

    * claude-4-opus
    * claude-4-sonnet
    * claude-3-7-sonnet
    * claude-3-5-sonnet
    * openai-gpt-4.1
    * openai-o4-mini

`categories`
:   An array of VARIANT values that specify one or more categories or labels to use, for functions that require this data. Categories are included in the input token count.

`options`
:   A VARIANT that specifies additional options that affect how the function processes the input. For functions that take
    two text inputs, such as AI_SIMILARITY, options are used to specify the model.

## Returns

An [INTEGER](../data-types-numeric.md) value that is the number of tokens of input text calculated using the given parameter values.

## Usage notes

* Although function names are usually written in all uppercase, use only lowercase letters in function and model
  names.
* COUNT_TOKENS does not work with LLM functions in the SNOWFLAKE.CORTEX namespace or with fine-tuned models.
  You must specify a function name that begins with “ai_”.
* COUNT_TOKENS accepts only text, not image, audio, or video inputs.
* COUNT_TOKENS only incurs compute costs and does not bill based on token count.
* COUNT_TOKENS is available in all regions, even for models not available in a given region.

## Examples

### AI_COMPLETE example

The following SQL statement counts the number of tokens in a prompt for AI_COMPLETE and the `llama3.3-70b` model:

```sqlexample
SELECT AI_COUNT_TOKENS('ai_complete', 'llama3.3-70b', 'Summarize the insights from this
call transcript in 20 words: "I finally splurged on these after months of hesitation about
the price, and I\'m mostly impressed. The Nulu fabric really is as buttery-soft as everyone says,
and they\'re incredibly comfortable for yoga and lounging. The high-rise waistband stays put
and doesn\'t dig in, which is rare for me. However, I\'m already seeing some pilling after
just a few wears, and they definitely require gentle care. They\'re also quite delicate -
I snagged them slightly on my gym bag zipper. Great for low-impact activities, but I wouldn\'t
recommend for high-intensity workouts. Worth it for the comfort factor"');
```

Response:

```output
158
```

### AI_EMBED example

The following SQL statement counts the number of tokens in text being embedded using the AI_EMBED function and the `nv-embed-qa-4'` model:

```sqlexample
SELECT AI_COUNT_TOKENS('ai_embed', 'nv-embed-qa-4', '"I finally splurged on these after months
of hesitation about the price, and I\'m mostly impressed. The Nulu fabric really is as buttery-soft
as everyone says, and they\'re incredibly comfortable for yoga and lounging. The high-rise waistband
stays put and doesn\'t dig in, which is rare for me. However, I\'m already seeing some pilling after
just a few wears, and they definitely require gentle care. They\'re also quite delicate - I snagged
them slightly on my gym bag zipper. Great for low-impact activities, but I wouldn\'t recommend for
high-intensity workouts. Worth it for the comfort factor"');
```

Response:

```output
142
```

### AI_CLASSIFY examples

This example calculates the total number of input tokens required for text classification with given input and labels:

```sqlexample
SELECT AI_COUNT_TOKENS('ai_classify',
  'One day I will see the world and learn to cook my favorite dishes',
  [
      {'label': 'travel'},
      {'label': 'cooking'},
      {'label': 'reading'},
      {'label': 'driving'}
  ]
);
```

Response:

```output
187
```

The following example adds per-label descriptions and an overall task description to the previous example:

```sqlexample
SELECT AI_COUNT_TOKENS('ai_classify',
  'One day I will see the world and learn to cook my favorite dishes',
  [
    {'label': 'travel', 'description': 'content related to traveling'},
    {'label': 'cooking','description': 'content related to food preparation'},
    {'label': 'reading','description': 'content related to reading'},
    {'label': 'driving','description': 'content related to driving a car'}
  ],
  {
    'task_description': 'Determine topics related to the given text'
  };
```

Response:

```output
254
```

The following example builds upon the previous two examples by adding label examples:

```sqlexample
SELECT AI_COUNT_TOKENS('ai_classify',
  'One day I will see the world and learn to cook my favorite dishes',
  [
    {'label': 'travel', 'description': 'content related to traveling'},
    {'label': 'cooking','description': 'content related to food preparation'},
    {'label': 'reading','description': 'content related to reading'},
    {'label': 'driving','description': 'content related to driving a car'}
  ],
  {
    'task_description': 'Determine topics related to the given text',
    'examples': [
      {
        'input': 'i love traveling with a good book',
        'labels': ['travel', 'reading'],
        'explanation': 'the text mentions traveling and a good book which relates to reading'
      }
    ]
  }
);
```

Response:

```output
298
```

### AI_SENTIMENT examples

The following SQL statement counts the number of tokens in text being analyzed for sentiment using the AI_SENTIMENT function:

```sqlexample
SELECT AI_COUNT_TOKENS('ai_sentiment',
  'This place makes the best truffle pizza in the world! Too bad I cannot afford it');
```

Response:

```output
139
```

The following example adds labels to the previous example:

```sqlexample
SELECT AI_COUNT_TOKENS('ai_sentiment',
  'This place makes the best truffle pizza in the world! Too bad I cannot afford it',
  [
    {'label': 'positive'},
    {'label': 'negative'},
    {'label': 'neutral'}
  ]
);
```

Response:

```output
148
```

### AI_SIMILARITY examples

The following SQL statement counts the number of tokens in an AI_SIMILARITY call that uses the default model.

```sqlexample
SELECT AI_COUNT_TOKENS('ai_similarity',
  'The plot is fast and the characters feel real. This book kept me awake all night
  because the mystery is so deep. I love how the author  handles the ending. It is a
  great read for anyone who likes suspense.',
  'The story is quick and the people feel true. This novel kept me awake all night
  because the puzzle is so big. I love how the writer handles the finale. It is a
  solid choice for anyone who enjoys suspense.');
```

Response:

```output
101
```

The following SQL statement counts the number of tokens in an AI_SIMILARITY that uses the `e5-base-v2` model:

```sqlexample
SELECT AI_COUNT_TOKENS('ai_similarity',
  'The plot is fast and the characters feel real. This book kept me awake all night
  because the mystery is so deep. I love how the author handles the ending. It is a
  great read for anyone who likes suspense.',
  'The story is quick and the people feel true. This novel kept me awake all night
  because the puzzle is so big. I love how the writer handles the finale. It is a
  solid choice for anyone who enjoys suspense.', {'model': 'e5-base-v2'})
```

Response:

```output
92
```

### AI_TRANSLATE example

The following SQL statement counts the number of tokens used by AI_TRANSLATE when translating text from English to
German.

```sqlexample
SELECT AI_COUNT_TOKENS('ai_translate',
  'The plot is fast and the characters feel real. This book kept me awake all night
  because the mystery is so deep. I love how the author handles the ending. It is a
  great read for anyone who likes suspense.', 'en', 'de');
```

Response:

```output
51
```

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).
