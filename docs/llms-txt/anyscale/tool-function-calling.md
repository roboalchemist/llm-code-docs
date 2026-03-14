# Source: https://docs.anyscale.com/llm/serving/tool-function-calling.md

# Configure tool and function calling for LLMs

[View Markdown](/llm/serving/tool-function-calling.md)

# Configure tool and function calling for LLMs

Learn how to deploy models with tool and function calling patterns to enable your LLM to interact with external tools, databases, and APIs.

note

To use full tool and function calling support, install `ray>=2.49.0`.

## Understand tool and function calling[​](#understand-tool-and-function-calling "Direct link to Understand tool and function calling")

Tool calling allows your LLM to interact with external tools or functions, creating more modular applications.

Use tool and function calling when your application needs integrations with downstream tools, databases, APIs, or any other backend logic.

## Deploy a model with tool calling enabled[​](#deploy-a-model-with-tool-calling-enabled "Direct link to Deploy a model with tool calling enabled")

To use tool calling, update your Ray Serve LLM deployment configuration with a few extra settings.

note

Ray Serve LLM uses [vLLM](https://docs.vllm.ai/en/stable/) as its backend engine. You can forward tool-related settings through the `engine_kwargs` field in your Serve config.

To enable tool calling:

* Set `enable_auto_tool_choice: true`
* Specify the correct `tool_call_parser` for your model

See the full list, or how to register your custom parser, in the [vLLM documentation](https://docs.vllm.ai/en/stable/features/tool_calling.html#automatic-function-calling).

Create a file `serve_my_llama.yaml` with the following configuration:

```
applications:
- name: my-tool-calling-app
  ...
  args:
    llm_configs:
      - ...
        engine_kwargs:
          ...
          enable_auto_tool_choice: true
          tool_call_parser: <YOUR-TOOL-PARSER-ID>
```

## Make a tool call request[​](#make-a-tool-call-request "Direct link to Make a tool call request")

To make a tool call request, you must first define your tool schemas, specify the strategy the LLM should follow, and include the tools in the request payload.

### Define tools[​](#define-tools "Direct link to Define tools")

Define your tools using standard JSON schema format. Each tool includes a name, description, and a list of expected parameters with their types and constraints.

This example defines two tools with signatures:

* `get_current_temperature(location: string, unit: string = "celsius")`
* `get_temperature_date(location: string, date: string, unit: string = "celsius")`

```
# Tools schema definitions
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_temperature",
            "description": "Get current temperature at a location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The location to get the temperature for, in the format \"City, State, Country\"."
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The unit to return the temperature in. Defaults to \"celsius\"."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_temperature_date",
            "description": "Get temperature at a location and date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The location to get the temperature for, in the format \"City, State, Country\"."
                    },
                    "date": {
                        "type": "string",
                        "description": "The date to get the temperature for, in the format \"Year-Month-Day\"."
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The unit to return the temperature in. Defaults to \"celsius\"."
                    }
                },
                "required": ["location", "date"]
            }
        }
    }
]
```

### Configure tool calling strategy[​](#configure-tool-calling-strategy "Direct link to Configure tool calling strategy")

The tool calling strategy controls how the model decides to use tools. Set the `tool_choice` parameter in your client call to the model.

You can let the model decide automatically, force it to call one or multiple tools, disable tool usage entirely, or specify a single tool to use.

| `tool_choice` value                                       | Description                                                                                                                                                                                                |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"auto"` (default)                                        | The model decides whether to use a tool based on the prompt and available tools. Returns an empty tool call list if no tool is used.                                                                       |
| `"none"`                                                  | Tool calling is disabled. The model responds with plain text, even if tools are defined. However, tool descriptions already present in the system or user prompt may still influence the model's behavior. |
| `"required"`                                              | Forces the model to call at least one tool, even if it may not be appropriate. Use only when the tool definitions cover all relevant use cases; otherwise, prefer `"auto"`.                                |
| `{"type": "function", "function": {"name": "your_tool"}}` | Forces the model to call a specific tool by name. Useful for single-tool workflows or when chaining calls deterministically.                                                                               |

### Query the model[​](#query-the-model "Direct link to Query the model")

Once you decide on your tools and tool calling strategy, send a request to the model by including both the `tools` and `tool_choice` parameters.

```
client = OpenAI(...)

messages = [
    {
        "role": "system",
        "content": "You are a weather assistant. Use the given functions to get weather data and provide the results."
    },
    {
        "role": "user",
        "content": "What's the temperature in San Francisco now? How about tomorrow? Current Date: 2025-07-29."
    }
]
response = client.chat.completions.create(
    ...
    messages=messages,
    tools=tools,
    tool_choice= "auto" # tool calling strategy: Let the model decide
)

print(response.choices[0].message)
```

You should get a response similar to:

```
ChatCompletionMessage(
    content=None, 
    refusal=None, 
    role='assistant',
    annotations=None, 
    audio=None, 
    function_call=None, 
    tool_calls=[
        ChatCompletionMessageToolCall(
            id='chatcmpl-tool-3c89da30948f4760b54d457691f92208', 
            function=Function(
                arguments='{"location": "San Francisco, California, USA", "unit": "celsius"}', 
                name='get_current_temperature'
            ), 
            type='function'
        ), 
        ChatCompletionMessageToolCall(
            id='chatcmpl-tool-6ee9721ff2a04426881493c31a36d9f1', 
            function=Function(
                arguments='{"location": "San Francisco, California, USA", "date": "2025-07-30", "unit": "celsius"}', 
                name='get_temperature_date'
            ), 
            type='function'
        )
    ], 
    reasoning_content=None
)
```

You can access the tool calls in the `tool_calls` field of your model's response.

## Handle tool responses[​](#handle-tool-responses "Direct link to Handle tool responses")

When the model wants to use a tool, it returns a `tool_calls` field containing the tool name and its arguments.

Route the call to your own function or APIs. For example:

```
import json

for tool_call in response.choices[0].message.tool_calls:
    if tool_call.function.name == "get_current_temperature":
        curr_temperature = get_current_temperature(**json.loads(tool_call.function.arguments))
        # Handle the result
        ...
    elif tool_call.function.name == "get_temperature_date":
        temperature = get_temperature_date(**json.loads(tool_call.function.arguments))
        # Handle the result
        ...
```

## Send tool results back to the model[​](#send-tool-results-back "Direct link to Send tool results back to the model")

If you choose to return tool results to the model for further generation, you must include both the assistant message that triggered the tool calls and the corresponding `tool` messages containing the results. The model uses the `tool_call_id` field in each `tool` message to match the output to its corresponding tool call.

Add your tool responses as new messages with the role `"tool"`:

```
def call_tool(tool_call):
    # Handle your tool_call here
    ...

# `response` is your model's last response containing the tool calls it requests.
# Add the previous response containing the tool calls
messages.append(response.choices[0].message.model_dump())

# Loop through the tool calls and create `tool` messages
for tool_call in response.choices[0].message.tool_calls:
    # 1. Call your tool
    output = call_tool(tool_call) 

    # 2. Create a new message of role `"tool"` containing the output of your tool
    messages.append({
        "role": "tool",
        "content": output,
        "tool_call_id": tool_call.id # Refer to the `tool_call_id` in the model's response containing the tool calls
    })

print(messages)
```

Your messages history should look like:

```
[
  # Your initial request to the model
  {
    'role': 'system', 'content': 'You are a weather assistant. Use the given functions to get weather data and provide the results.'
  },
  {
    'role': 'user', 'content': "What's the temperature in San Francisco now? How about tomorrow? Current Date: 2025-07-29."
  },
  # Your model response with the requested tool calls
  {'content': None, 'role': 'assistant', 'tool_calls': [
            {'id': 'chatcmpl-tool-be5e993a5bb64701992f13c51f9e7e9a', 'function': {'arguments': '{"location": "San Francisco, California, USA", "unit": "celsius"}', 'name': 'get_current_temperature'}, 'type': 'function'}, 
            {'id': 'chatcmpl-tool-d20a696b01e14994b036e0292cee56de', 'function': {'arguments': '{"location": "San Francisco, California, USA", "date": "2025-07-30", "unit": "celsius"}', 'name': 'get_temperature_date'}, 'type': 'function'}
  ]},
  # You send back the outputs of your tools to the model.
  {
    'role': 'tool', 'content': '{"temperature": 16, "location": "San Francisco, California, USA", "unit": "celsius"}'
  },
  {
    'role': 'tool', 'content': '{"temperature": 26, "location": "San Francisco, California, USA", "date": "2025-07-30", "unit": "celsius"}'
  }
]
```

Now you can request a new response from the model:

```
response = client.chat.completions.create(
    ...,
    messages=messages
)

print(response.choices[0].message.content)
```

Your model should respond with something similar to:

```
The current temperature in San Francisco is 16 degrees Celsius. 
Tomorrow, on 2025-07-30, the temperature in San Francisco will be 26 degrees Celsius.
```

## Use parallel tool calling[​](#use-parallel-tool-calling "Direct link to Use parallel tool calling")

Parallel tool calls allow the model to request and execute multiple tools in a single response. Iterate over each tool call returned by the model and append a corresponding tool message with its output.

Make sure to include the correct `tool_call_id` for each tool message to ensure the model can match responses to the original tool calls.

For implementation details, see [Send tool results back to the model](#send-tool-results-back).

note

Not all models support parallel tool calls. See the documentation for your model. For example, Llama-3 models don't support parallel tool calls, while Llama-4 models do.

## Configure tool calling with reasoning models[​](#tool-calling-with-reasoning-models "Direct link to Configure tool calling with reasoning models")

When a model decides to call a tool in its response, the `content` field is usually empty, and tool details appear in the `tool_calls` field. However, reasoning models still include their thought process in the response.

Reasoning content is usually returned in the `reasoning_content` field. To ensure the model parses this correctly, set the appropriate `reasoning_parser` in your Serve config during deployment. See the vLLM docs for a [list of supported reasoning parsers](https://docs.vllm.ai/en/stable/features/reasoning_outputs.html#supported-models).

```
applications:
- ...
  args:
    llm_configs:
        ...
        engine_kwargs:
          ...
          reasoning_parser: <REASONING-PARSER> # See vLLM supported reasoning parsers
```

The response includes an empty `content`, the model's reasoning in `reasoning_content`, and the tool calls in `tool_calls`:

```
# Response from the model "What is the weather in ..."
ChatCompletionMessage(
    # Empty content
    content='\n\n', 
    ...
    tool_calls=[
        # List of tool calls here
    ], 
    # Reasoning contained here
    reasoning_content='\nOkay, the user is asking for ...'
)
```

If a reasoning parser isn't configured, the reasoning may fall back into the regular `content` field.

## Configure tool calling with hybrid models[​](#configure-tool-calling-with-hybrid-models "Direct link to Configure tool calling with hybrid models")

Models such as *Qwen-3* are hybrid and can toggle reasoning. To control reasoning in hybrid models, see their documentation.

For example, to [control reasoning in Qwen-3](https://huggingface.co/Qwen/Qwen3-32B#switching-between-thinking-and-non-thinking-mode), you can:

* Add `"/think"` or `"/no_think"` in the prompt
* Or set `enable_thinking` in the request: `extra_body={"chat_template_kwargs": {"enable_thinking": ...}}`

Call a hybrid model such as Qwen-3 with tools and thinking mode enabled:

```
response = client.chat.completions.create(
    model="my-qwen3",
    messages=messages,
    tools=tools,
    tool_choice= tool_choice,
    extra_body={"chat_template_kwargs": {"enable_thinking": True}} # <-- specific to Qwen-3
)
```

In thinking mode, follow the same recommendations outlined in [Configure tool calling with reasoning models](#tool-calling-with-reasoning-models).

## Apply best practices[​](#apply-best-practices "Direct link to Apply best practices")

Follow these suggestions for more reliable and predictable behavior when using tool calling:

### Validate tool inputs[​](#validate-tool-inputs "Direct link to Validate tool inputs")

Validate and sanitize tool arguments before execution. Models can occasionally produce missing or invalid fields. Use frameworks such as [Pydantic](https://docs.pydantic.dev/latest/) for reliable validation.

### Control tool choice[​](#control-tool-choice "Direct link to Control tool choice")

Use `"tool_choice": "auto"` to let the model decide when to call a tool, or specify a particular tool by name if you want to force a specific tool.

### Use descriptive tool names[​](#use-descriptive-tool-names "Direct link to Use descriptive tool names")

Use clear and specific names, descriptions, and arguments to help the model understand their purpose and improve tool selection accuracy.

### Set a low temperature[​](#set-a-low-temperature "Direct link to Set a low temperature")

Set a lower `temperature` to reduce randomness and ensure the model consistently outputs valid tool calls when appropriate.

### Choose a model optimized for tool calling[​](#choose-a-model-optimized-for-tool-calling "Direct link to Choose a model optimized for tool calling")

Some models, especially reasoning models, are better at deciding when and how to call tools. Check the documentation of your model family to see if a specialized or fine-tuned version exists.

## Summary[​](#summary "Direct link to Summary")

In this guide, you learned how to enable tool calling with Ray Serve LLM, define tools, handle model responses, and work with reasoning and hybrid models. You also learned best practices to improve your tool calling workflow.
