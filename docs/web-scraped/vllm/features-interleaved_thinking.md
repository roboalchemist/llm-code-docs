# Source: https://docs.vllm.ai/en/stable/features/interleaved_thinking/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/interleaved_thinking.md "Edit this page")

# Interleaved Thinking[¶](#interleaved-thinking "Permanent link")

## Introduction[¶](#introduction "Permanent link")

Interleaved thinking allows models to reason between tool calls, enabling more sophisticated decision-making after receiving tool results. This feature helps models chain multiple tool calls with reasoning steps in between and make nuanced decisions based on intermediate results.

Important: Interleaved thinking increases token usage and response latency. Consider your budget and performance requirements when enabling this feature.

## How Interleaved Thinking Works[¶](#how-interleaved-thinking-works "Permanent link")

With interleaved thinking, the model can:

-   Reason about the results of a tool call before deciding what to do next
-   Chain multiple tool calls with reasoning steps in between
-   Make more nuanced decisions based on intermediate results
-   Provide transparent reasoning for its tool selection process

## Supported Models[¶](#supported-models "Permanent link")

vLLM currently supports the following interleaved thinking models:

  Model Series                  Reasoning Parser Name
  ----------------------------- -----------------------
  moonshotai/Kimi-K2-Thinking   kimi_k2
  MiniMaxAI/MiniMax-M2          minimax_m2

## Example Usage[¶](#example-usage "Permanent link")

To use interleaved thinking with tool calls, specify a model that supports this feature and enable tool calls in your chat completion request. Here\'s an example:

Code

    """
    vllm serve MiniMaxAI/MiniMax-M2 \
      --tensor-parallel-size 4 \
      --tool-call-parser minimax_m2 \
      --reasoning-parser minimax_m2 \
      --enable-auto-tool-choice
    """
    import json

    from openai import OpenAI

    client = OpenAI(base_url="http://localhost:8000/v1",     api_key="dummy")

    def get_current_weather(location: str, unit: "str"):
        """Get the current weather in a given location"""
        if unit == "celsius":
            return f"The current temperature in  is 22°C."
        else:
            return f"The current temperature in  is 72°F."

    tools = [
        ,
                        "unit": ,
                    },
                    "required": ["location", "unit"],
                },
            },
        }
    ]
    messages = []
    response = client.chat.completions.create(
        model=client.models.list().data[0].id,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    tool_call = response.choices[0].message.tool_calls[0].function

    messages.append(
        
    )

    # Simulate tool execution
    available_tools = 

    completion_tool_calls = response.choices[0].message.tool_calls
    for call in completion_tool_calls:
        tool_to_call = available_tools[call.function.name]
        args = json.loads(call.function.arguments)
        result = tool_to_call(**args)
        messages.append(
            
        )
    response_2 = client.chat.completions.create(
        model=client.models.list().data[0].id,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    print(response_2.choices[0].message.content)

This example demonstrates how to set up interleaved thinking with tool calls using a weather retrieval function. The model reasons about the tool results before generating the final response.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 13, 2025] ]