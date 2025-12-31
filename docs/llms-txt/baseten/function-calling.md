# Source: https://docs.baseten.co/inference/function-calling.md

# Function calling (tool use)

> Use an LLM to select amongst provided tools

<Note>
  Function calling requires an LLM deployed using the [TensorRT-LLM Engine
  Builder](/development/model/performance/engine-builder-overview).
</Note>

To use function calling:

1. Define a set of functions/tools in Python.
2. Pass the function set to the LLM with the `tools` argument.
3. Receive selected function(s) as output.

With function calling, it's essential to understand that **the LLM itself is not capable of executing the code in the function**. Instead, the LLM is used to suggest appropriate function(s), if they exist, based on the prompt. Any code execution must be handled outside of the LLM call – a great use for [chains](/development/chain/overview).

## Define functions in Python

Functions can be anything: API calls, ORM access, SQL queries, or just a script. It's essential that functions are well-documented; the LLM relies on the docstrings to select the correct function.

As a simple example, consider the four basic functions of a calculator:

```python  theme={"system"}
def multiply(a: float, b: float):
    """
    A function that multiplies two numbers

    Args:
        a: The first number to multiply
        b: The second number to multiply
    """
    return a * b

def divide(a: float, b: float):
    """
    A function that divides two numbers

    Args:
        a: The dividend
        b: The divisor
    """
    return a / b

def add(a: float, b: float):
    """
    A function that adds two numbers

    Args:
        a: The first number
        b: The second number
    """
    return a + b

def subtract(a: float, b: float):
    """
    A function that subtracts two numbers

    Args:
        a: The number to subtract from
        b: The number to subtract
    """
    return a - b
```

These functions must be serialized into LLM-accessible tools:

```python  theme={"system"}
from transformers.utils import get_json_schema

calculator_functions = {
    'multiply': multiply,
    'divide': divide,
    'add': add,
    'subtract': subtract
}

tools = [get_json_schema(f) for f in calculator_functions.values()]
```

## Pass functions to the LLM

The input spec for models like Llama 3.1 includes a `tools` key that we use to pass the functions:

```python  theme={"system"}
import json
import requests

payload = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "What is 3.14+3.14?"},
    ],
    "tools": tools,  # tools are provided in the same format as OpenAI's API
    "tool_choice": "auto",  # auto is default - the model will choose whether or not to make a function call
}

MODEL_ID = ""
BASETEN_API_KEY = ""

resp = requests.post(
    f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
    json=payload,
)
```

### tool\_choice: auto (default) – may return a function

The default `tool_choice` option, `auto`, leaves it up to the LLM whether to return one function, multiple functions, or no functions at all, depending on what the model feels is most appropriate based on the prompt.

### tool\_choice: required – will always return a function

The `required` option for `tool_choice` means that the LLM is guaranteed to chose at least one function, no matter what.

### tool\_choice: none – will always return a function

The `none` option for `tool_choice` means that the LLM will **not** return a function, and will instead produce ordinary text output. This is useful when you want to provide the full context of a conversation without adding and dropping the `tools` parameter call-by-call.

### tool\_choice: direct – will return a specified function

You can also pass a specific function directly into the call, which is guaranteed to be returned. This is useful if you want to hardcode specific behavior into your model call for testing or conditional execution.

```python  theme={"system"}
"tool_choice": {"type": "function", "function": {"name": "subtract"}}
```

## Receive function(s) as output

When the model returns functions, they'll be a list that can be parsed as follows:

```python  theme={"system"}
func_calls = json.loads(resp.text)

# In this example, we execute the first function (one of +-/*) on the provided parameters
func_call = func_calls[0]
calculator_functions[func_call["name"]](**func_call["parameters"])
```

After reading the LLM's selection, your execution environment can run the necessary functions. For more on combining LLMs with other logic, see the [chains documentation](/development/chain/overview).
