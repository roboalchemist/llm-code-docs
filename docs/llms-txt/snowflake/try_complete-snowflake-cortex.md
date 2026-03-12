# Source: https://docs.snowflake.com/en/sql-reference/functions/try_complete-snowflake-cortex.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# TRY_COMPLETE (SNOWFLAKE.CORTEX)

Performs the same operation as the [COMPLETE](complete-snowflake-cortex.md) function
but returns NULL instead of raising an error when the operation cannot be performed.

## Syntax

```sqlsyntax
SNOWFLAKE.CORTEX.TRY_COMPLETE( <model>, <prompt_or_history> [ , <options> ] )
```

## Arguments

**Required:**

`model`
:   A string specifying the model to be used. Specify one of the following values.

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

    Supported models might have different [costs](../../user-guide/snowflake-cortex/aisql.md).

`prompt_or_history`
:   The prompt or conversation history to be used to generate a completion.

    If `options` is not present, the prompt given must be a string.

    If `options` is present, the argument must be an [array](../data-types-semistructured.md) of objects representing a
    conversation in chronological order. Each [object](../data-types-semistructured.md) must contain a `role` key and a
    `content` key. The `content` value is a prompt or a response, depending on the role. The role must be one of the
    following.

> | `role` value | `content` value |
> | --- | --- |
> | `'system'` | An initial plain-English prompt to the language model to provide it with background information and instructions for a response style. For example, “Respond in the style of a pirate.” The model does not generate a response to a system prompt. Only one system prompt may be provided, and if it is present, it must be the first in the array. |
> | `'user'` | A prompt provided by the user. Must follow the system prompt (if there is one) or an assistant response. |
> | `'assistant'` | A response previously provided by the language model. Must follow a user prompt. Past responses can be used to provide a stateful conversational experience; see Usage Notes. |

**Optional:**

`options`
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
      Either TRUE or FALSE.

      Default: FALSE
    * `response_format`: A [JSON schema](https://json-schema.org/) that the response should follow. This is a SQL
      sub-object, not a string. If `response_format` is not specified, the response is a string containing either the
      response or a serialized JSON object containing the response and information about it.

      For more information, see [AI_COMPLETE structured outputs](../../user-guide/snowflake-cortex/complete-structured-outputs.md).

    Specifying the `options` argument, even if it is an empty object (`{}`), affects how the `prompt` argument is
    interpreted and how the response is formatted.

## Returns

When the `options` argument is not specified, returns a string containing the response.

When the `options` argument is given, and this object contains the `response_format` key, returns a string
representation of a JSON object adhering to the specified JSON schema.

When the `options` argument is given, and this object *does not* contain the `response_format` key, returns a
string representation of a JSON object containing the following keys.

* `"choices"`: An array of the model’s responses. (Currently, only one response is provided.) Each response is
  an object containing a `"messages"` key whose value is the model’s response to the latest prompt.
* `"created"`: UNIX timestamp (seconds since midnight, January 1, 1970) when the response was generated.
* `"model"`: The name of the model that created the response.
* `"usage"`: An object recording the number of tokens consumed and generated by this completion. Includes
  the following sub-keys:

  * `"completion_tokens"`: The number of tokens in the generated response.
  * `"prompt_tokens"`: The number of tokens in the prompt.
  * `"total_tokens"`: The total number of tokens consumed, which is the sum of the other two values.

## Access control requirements

Users must use a role that has been granted the [SNOWFLAKE.CORTEX_USER database role](../snowflake-db-roles.md).
See [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md) for more information on this privilege.

## Usage notes

TRY_COMPLETE does not retain any state from one call to the next. To use the TRY_COMPLETE function to provide a stateful,
conversational experience, pass all previous user prompts and model responses in the conversation as part of the `prompt_or_history`
array (see [Templates for Chat Models](https://huggingface.co/docs/transformers/en/chat_templating#templates-for-chat-models)).
Keep in mind that the number of tokens processed increases for each “round,” and costs increase proportionally.

## Examples

The following examples use the TRY_COMPLETE function in various use cases.

### Generating a single response

To generate a single response:

```sqlexample
SELECT SNOWFLAKE.CORTEX.TRY_COMPLETE('snowflake-arctic', 'What are large language models?');
```

### Controlling temperature and tokens

This example illustrates the use of the function’s `options` argument to control the inference hyperparameters in a
single response. Note that in this form of the function, the prompt must be provided as an array, since this form
supports multiple prompts and responses.

```sqlexample
SELECT SNOWFLAKE.CORTEX.TRY_COMPLETE(
    'deepseek-r1',
    [
        {
            'role': 'user',
            'content': 'how does a snowflake get its unique pattern?'
        }
    ],
    {
        'temperature': 0.7,
        'max_tokens': 10
    }
);
```

The response is a JSON object containing the message from the language model and other information. Note that the response
is truncated as instructed in the `options` argument.

```json
{
    "choices": [
        {
            "messages": " The unique pattern on a snowflake is"
        }
    ],
    "created": 1708536426,
    "model": "deepseek-r1",
    "usage": {
        "completion_tokens": 10,
        "prompt_tokens": 22,
        "total_tokens": 32
    }
}
```

For additional examples, see the [COMPLETE (SNOWFLAKE.CORTEX)](complete-snowflake-cortex.md) reference.

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).
