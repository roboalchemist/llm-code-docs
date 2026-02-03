# Source: https://docs.baseten.co/engines/performance-concepts/function-calling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Function calling

> Tool selection and structured function calls with LLMs

<Note>
  Function calling is supported by Baseten engines including [BIS-LLM](/engines/bis-llm/overview) and [Engine-Builder-LLM](/engines/engine-builder-llm/overview), as well as [Model APIs](/development/model-apis/overview) for instant access. It's also compatible with other inference frameworks like [vLLM](/examples/vllm) and [SGLang](/examples/sglang).
</Note>

## Overview

*Function calling* (also known as *tool calling*) lets a model **choose a tool and produce arguments** based on a user request.

**Important:** the model **does not execute** your Python function. Your application must:

1. run the tool, and
2. optionally send the tool’s output back to the model to produce a final, user-facing response.

This is a great fit for [chains](/development/chain/overview) and other orchestrators.

***

## How tool calling works

A typical tool-calling loop looks like:

1. **Send** the user message and a list of tools.
2. The model returns either normal text or one or more **tool calls** (name and JSON arguments).
3. **Execute** the tool calls in your application.
4. **Send tool output** back to the model.
5. Receive a **final response** or additional tool calls.

***

## 1. Define tools

Tools can be anything: API calls, database queries, internal scripts, etc.

Docstrings matter. Models use them to decide which tool to call and how to fill parameters:

```python  theme={"system"}
def multiply(a: float, b: float):
    """Multiply two numbers.

    Args:
        a: The first number.
        b: The second number.
    """
    return a * b


def divide(a: float, b: float):
    """Divide two numbers.

    Args:
        a: The dividend.
        b: The divisor (must be non-zero).
    """
    return a / b


def add(a: float, b: float):
    """Add two numbers.

    Args:
        a: The first number.
        b: The second number.
    """
    return a + b


def subtract(a: float, b: float):
    """Subtract two numbers.

    Args:
        a: The number to subtract from.
        b: The number to subtract.
    """
    return a - b
```

### Tool-writing tips

Design small, single-purpose tools and document constraints in docstrings (units, allowed values, required fields). Treat model-provided arguments as untrusted input and validate before execution.

***

## 2. Serialize functions

Convert functions into JSON-schema tool definitions (OpenAI-compatible format):

```python  theme={"system"}
from transformers.utils import get_json_schema

calculator_functions = {
    "multiply": multiply,
    "divide": divide,
    "add": add,
    "subtract": subtract,
}

tools = [get_json_schema(f) for f in calculator_functions.values()]
```

***

## 3. Call the model

Include the `tools` array in your request:

```python  theme={"system"}
import requests

payload = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is 3.14 + 3.14?"},
    ],
    "tools": tools,
    "tool_choice": "auto",  # default
}

MODEL_ID = ""
BASETEN_API_KEY = ""

resp = requests.post(
    f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
    json=payload,
)
```

***

## 4. Control tool selection

Set `tool_choice` to control how the model uses tools. With `auto` (default), the model may respond with text or tool calls. With `required`, the model must return at least one tool call. With `none`, the model returns plain text only. To force a specific tool:

```python  theme={"system"}
"tool_choice": {"type": "function", "function": {"name": "subtract"}}
```

***

## 5. Parse and execute tool calls

Depending on the engine and model, tool calls are typically returned in an assistant message under `tool_calls`:

```python  theme={"system"}
import json

data = resp.json()
message = data["choices"][0]["message"]

tool_calls = message.get("tool_calls") or []

for tool_call in tool_calls:
    name = tool_call["function"]["name"]
    args = json.loads(tool_call["function"]["arguments"])

    # Validate args in production.
    result = calculator_functions[name](**args)
    print(result)
```

### Full loop: send tool output back for a final answer

If you want the model to turn raw tool output into a user-facing response, append the assistant message and a tool response with the matching `tool_call_id`:

```python  theme={"system"}
# Continue the conversation
messages = payload["messages"]
messages.append(message)  # assistant tool call message

# Example: respond to the first tool call
tool_call = tool_calls[0]
name = tool_call["function"]["name"]
args = json.loads(tool_call["function"]["arguments"])
result = calculator_functions[name](**args)

messages.append({
    "role": "tool",
    "tool_call_id": tool_call["id"],
    "content": json.dumps({"result": result}),
})

final_payload = {
    **payload,
    "messages": messages,
}

final_resp = requests.post(
    f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
    json=final_payload,
)

print(final_resp.json()["choices"][0]["message"].get("content"))
```

***

## Practical tips

Use low temperature (0.0–0.3) for reliable tool selection and argument values. Add `enum` and `required` constraints in your JSON schema to guide model outputs. Consider parallel tool calls only if your model supports them. Always validate and sanitize inputs before calling real systems.

***

## Further reading

* [Chains](/development/chain/overview): Orchestrate multi-step workflows.
* [Custom engine builder](/engines/engine-builder-llm/custom-engine-builder): Advanced configuration options.
