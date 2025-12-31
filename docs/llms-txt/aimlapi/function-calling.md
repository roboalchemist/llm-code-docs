# Source: https://docs.aimlapi.com/capabilities/function-calling.md

# Function Calling

This article describes a specific capability of chat models: **function calling**, or simply **functions**.\
A list of models that support this feature is provided at the end of this page.

## Introduction

When using text (chat) models via the API, you can define functions that the model can choose to call, generating a JSON object with the necessary arguments. The text model API itself does not execute these functions; instead, it outputs the JSON, which you can then use to call the function within your code.

The latest models (gpt-4o, gpt-4-turbo, and gpt-3.5-turbo) are designed to detect when a function should be called based on the input and to produce JSON that closely matches the function signature. However, this functionality comes with potential risks. We strongly recommend implementing user confirmation steps before performing actions that could impact the real world (e.g., sending an email, posting online, making a purchase).

This guide focuses on function calling with our text models API.

## Common Use Cases

Function calling allows you to obtain structured data reliably from the model. For example, you can:

* **Create assistants that answer questions by calling external APIs**
  * Example functions: `send_email(to: string, body: string)`, `get_current_weather(location: string, unit: 'celsius' | 'fahrenheit')`
* **Convert natural language into API calls**
  * Example conversion: "Who are my top customers?" to `get_customers(min_revenue: int, created_before: string, limit: int)`, then call your internal API
* **Extract structured data from text**
  * Example functions: `extract_data(name: string, birthday: string)`, `sql_query(query: string)`

## Basic Sequence of Steps for Function Calling

1. **Call the model** with the user query and a set of functions defined in the `functions` parameter.
2. **Model response**: The model may choose to call one or more functions. If so, it will output a stringified JSON object adhering to your custom schema (note: the model may hallucinate parameters).
3. **Parse the JSON**: In your code, parse the string into JSON and call the function with the provided arguments if they exist.
4. **Call the model again**: Append the function response as a new message and let the model summarize the results back to the user.

## Examples

{% code title="python" overflow="wrap" %}

```python
import os
import json
import openai

client = openai.OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key='AI_ML_API',
)

tools = [
  {
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": [
              "celsius",
              "fahrenheit"
            ]
          }
        }
      }
    }
  }
]

messages = [
    {"role": "system", "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls."},
    {"role": "user", "content": "What is the current temperature of New York, San Francisco, and Chicago?"}
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)

print(json.dumps(response.choices[0].message.model_dump()['tool_calls'], indent=2))
```

{% endcode %}

## Models That Support Function Calling

* [claude-3-haiku-20240307](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-3-haiku)
* [claude-3-opus-20240229](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-3-opus)
* [claude-3-5-haiku-20241022](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-3.5-haiku)
* [claude-3-7-sonnet-20250219](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-3.7-sonnet)
* [claude-opus-4-20250514](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-4-opus)
* [claude-sonnet-4-20250514](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-4-sonnet)
* [anthropic/claude-opus-4.1](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-opus-4.1)
* [anthropic/claude-sonnet-4.5](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-4-5-sonnet)
* [anthropic/claude-opus-4-5](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-4.5-opus)

***

* [Qwen/Qwen2.5-7B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen2.5-7b-instruct-turbo)
* [Qwen/Qwen2.5-72B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen2.5-72b-instruct-turbo)
* [Qwen/Qwen2.5-Coder-32B-Instruct](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen2.5-coder-32b-instruct)
* [qwen-max](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen-max)
* [qwen-max-2025-01-25](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen-max)
* [qwen-plus](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen-plus)
* [qwen-turbo](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen-turbo)
* [Qwen/Qwen3-235B-A22B-fp8-tput](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen3-235b-a22b)
* [alibaba/qwen3-32b](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen3-32b)
* [alibaba/qwen3-coder-480b-a35b-instruct](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen3-coder-480b-a35b-instruct)
* [alibaba/qwen3-235b-a22b-thinking-2507](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen3-235b-a22b-thinking-2507)
* [alibaba/qwen3-max-preview](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen3-max-preview)
* [alibaba/qwen3-max-instruct](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen3-max-instruct)
* [alibaba/qwen3-vl-32b-instruct](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen3-vl-32b-instruct)
* [alibaba/qwen3-vl-32b-thinking](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen3-vl-32b-thinking)

***

* [google/gemini-2.0-flash](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.0-flash)
* [google/gemini-2.5-flash-lite-preview](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.5-flash-lite-preview)
* [google/gemini-2.5-flash](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.5-flash)
* [google/gemini-2.5-pro](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.5-pro)
* [google/gemini-3-pro-preview](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-3-pro-preview)

***

* [meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/meta/meta-llama-3.1-8b-instruct-turbo)
* [meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/meta/meta-llama-3.1-70b-instruct-turbo)
* [meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/meta/meta-llama-3.1-405b-instruct-turbo)
* [meta-llama/Llama-3.2-3B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/meta/llama-3.2-3b-instruct-turbo)
* [meta-llama/Llama-3.3-70B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/meta/llama-3.3-70b-instruct-turbo)
* [meta-llama/LlamaGuard-2-8b](https://docs.aimlapi.com/api-references/moderation-safety-models/meta/meta-llama-guard-3-8b)
* [meta-llama/llama-4-scout](https://docs.aimlapi.com/api-references/text-models-llm/meta/llama-4-maverick)
* [meta-llama/llama-4-maverick](https://docs.aimlapi.com/api-references/text-models-llm/meta/llama-4-maverick)

***

* [gpt-3.5-turbo](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-3.5-turbo)
* [gpt-3.5-turbo-0125](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-3.5-turbo)
* [gpt-3.5-turbo-1106](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-3.5-turbo)
* [gpt-4](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4)
* [gpt-4-0125-preview](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4-preview)
* [gpt-4-1106-preview](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4-preview)
* [gpt-4-turbo](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4-turbo)
* [gpt-4-turbo-2024-04-09](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4-turbo)
* [gpt-4o](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4o-2024-05-13](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4o-2024-08-06](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [chatgpt-4o-latest](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4o-mini](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o-mini)
* [gpt-4o-mini-2024-07-18](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o-mini)
* [gpt-4o-audio-preview](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o-audio-preview)
* [gpt-4o-mini-audio-preview](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o-mini-audio-preview)
* [o1](https://docs.aimlapi.com/api-references/text-models-llm/openai/o1)
* [o3-mini](https://docs.aimlapi.com/api-references/text-models-llm/openai/o3-mini)
* [openai/o3-2025-04-16](https://docs.aimlapi.com/api-references/text-models-llm/openai/o3)
* [openai/gpt-4.1-2025-04-14](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4.1)
* [openai/gpt-4.1-mini-2025-04-14](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4.1-mini)
* [openai/gpt-4.1-nano-2025-04-14](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4.1-nano)
* [openai/o4-mini-2025-04-16](https://docs.aimlapi.com/api-references/text-models-llm/openai/o4-mini)
* [openai/gpt-oss-20b](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-oss-20b)
* [openai/gpt-oss-120b](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-oss-120b)
* [openai/gpt-5-2025-08-07](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5)
* [openai/gpt-5-mini-2025-08-07](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-mini)
* [openai/gpt-5-nano-2025-08-07](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-nano)
* [openai/gpt-5-1](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-1)
* [openai/gpt-5-1-chat-latest](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-1-chat-latest)
* [openai/gpt-5-1-codex](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-1-codex)
* [openai/gpt-5-1-codex-mini](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-1-codex-mini)
* [openai/gpt-5-2](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5.2)
* [openai/gpt-5-2-chat-latest](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5.2-chat-latest)

***

* [deepseek/deepseek-r1](https://docs.aimlapi.com/api-references/text-models-llm/deepseek/deepseek-r1)
* [deepseek/deepseek-thinking-v3.2-exp](https://docs.aimlapi.com/api-references/text-models-llm/deepseek/deepseek-reasoner-v3.2-exp-thinking)
* [deepseek/deepseek-non-thinking-v3.2-exp](https://docs.aimlapi.com/api-references/text-models-llm/deepseek/deepseek-reasoner-v3.2-exp-non-thinking)
* [MiniMax-Text-01](https://docs.aimlapi.com/api-references/text-models-llm/minimax/text-01)
* [minimax/m1](https://docs.aimlapi.com/api-references/text-models-llm/minimax/m1)
* [minimax/m2-1](https://docs.aimlapi.com/api-references/text-models-llm/minimax/m2-1)
* [mistralai/mistral-tiny](https://docs.aimlapi.com/api-references/text-models-llm/mistral-ai/mistral-tiny)
* [mistralai/mistral-nemo](https://docs.aimlapi.com/api-references/text-models-llm/mistral-ai/mistral-nemo)
* [moonshot/kimi-k2-preview](https://docs.aimlapi.com/api-references/text-models-llm/moonshot/kimi-k2-preview)
* [moonshot/kimi-k2-0905-preview](https://docs.aimlapi.com/api-references/text-models-llm/moonshot/kimi-k2-preview)
* [moonshot/kimi-k2-turbo-preview](https://docs.aimlapi.com/api-references/text-models-llm/moonshot/kimi-k2-turbo-preview)
* [vidia/nemotron-nano-9b-v2](https://docs.aimlapi.com/api-references/text-models-llm/nvidia/nemotron-nano-9b-v2)
* [nvidia/nemotron-nano-12b-v2-vl](https://docs.aimlapi.com/api-references/text-models-llm/nvidia/llama-3.1-nemotron-70b-1)
* [x-ai/grok-3-beta](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-3-beta)
* [x-ai/grok-3-mini-beta](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-3-mini-beta)
* [x-ai/grok-4-07-09](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-4)
* [x-ai/grok-code-fast-1](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-code-fast-1)
* [x-ai/grok-4-fast-non-reasoning](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-4-fast-non-reasoning)
* [x-ai/grok-4-fast-reasoning](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-4-fast-reasoning)
* [x-ai/grok-4-1-fast-non-reasoning](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-4-1-fast-non-reasoning)
* [x-ai/grok-4-1-fast-reasoning](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-4-1-fast-reasoning)
* [zhipu/glm-4.5-air](https://docs.aimlapi.com/api-references/text-models-llm/zhipu/glm-4.5-air)
* [zhipu/glm-4.5](https://docs.aimlapi.com/api-references/text-models-llm/zhipu/glm-4.5)
* [zhipu/glm-4.7](https://docs.aimlapi.com/api-references/text-models-llm/zhipu/glm-4.7)
