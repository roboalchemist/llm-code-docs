# Source: https://docs.vllm.ai/en/stable/examples/online_serving/openai_chat_completion_tool_calls_with_reasoning/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/openai_chat_completion_tool_calls_with_reasoning.md "Edit this page")

# OpenAI Chat Completion Tool Calls With Reasoning[¶](#openai-chat-completion-tool-calls-with-reasoning "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_tool_calls_with_reasoning.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    An example demonstrates how to use tool calling with reasoning models 
    like QwQ-32B. The reasoning will not be parsed by the tool 
    calling process; only the final output will be parsed.

    To run this example, you need to start the vLLM server with both 
    the reasoning parser and tool calling enabled.

    ```bash
    vllm serve Qwen/QwQ-32B \
         --reasoning-parser deepseek_r1 \
         --enable-auto-tool-choice --tool-call-parser hermes

    ```

    """

    from openai import OpenAI

    # Now, simulate a tool call
    def get_current_weather(city: str, state: str, unit: "str"):
        return (
            "The weather in Dallas, Texas is 85 degrees fahrenheit. It is "
            "partly cloudly, with highs in the 90's."
        )

    available_tools = 

    # Modify OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"

    properties = ,
        "state": ,
        "unit": ,
    }

    tools = [
        ,
            },
        }
    ]
    messages = [
        ,
        ,
        ,
    ]

    def extract_reasoning_and_calls(chunks: list):
        reasoning = ""
        tool_call_idx = -1
        arguments = []
        function_names = []
        for chunk in chunks:
            if chunk.choices[0].delta.tool_calls:
                tool_call = chunk.choices[0].delta.tool_calls[0]
                if tool_call.index != tool_call_idx:
                    tool_call_idx = chunk.choices[0].delta.tool_calls[0].index
                    arguments.append("")
                    function_names.append("")

                if tool_call.function:
                    if tool_call.function.name:
                        function_names[tool_call_idx] = tool_call.function.name

                    if tool_call.function.arguments:
                        arguments[tool_call_idx] += tool_call.function.arguments
            else:
                if hasattr(chunk.choices[0].delta, "reasoning"):
                    reasoning += chunk.choices[0].delta.reasoning
        return reasoning, arguments, function_names

    def main():
        client = OpenAI(
            api_key=openai_api_key,
            base_url=openai_api_base,
        )

        models = client.models.list()
        model = models.data[0].id

        print("---------Full Generate With Automatic Function Calling-------------")
        tool_calls = client.chat.completions.create(
            messages=messages, model=model, tools=tools
        )
        print(f"reasoning: ")
        print(f"function name: ")
        print(
            f"function arguments: "
            f""
        )

        print("----------Stream Generate With Automatic Function Calling-----------")
        tool_calls_stream = client.chat.completions.create(
            messages=messages, model=model, tools=tools, stream=True
        )

        chunks = list(tool_calls_stream)

        reasoning, arguments, function_names = extract_reasoning_and_calls(chunks)

        print(f"reasoning: ")
        print(f"function name: ")
        print(f"function arguments: ")

        print("----------Full Generate With Named Function Calling-----------------")
        tool_calls = client.chat.completions.create(
            messages=messages,
            model=model,
            tools=tools,
            tool_choice=},
        )

        tool_call = tool_calls.choices[0].message.tool_calls[0].function
        print(f"reasoning: ")
        print(f"function name: ")
        print(f"function arguments: ")
        print("----------Stream Generate With Named Function Calling--------------")

        tool_calls_stream = client.chat.completions.create(
            messages=messages,
            model=model,
            tools=tools,
            tool_choice=},
            stream=True,
        )

        chunks = list(tool_calls_stream)

        reasoning, arguments, function_names = extract_reasoning_and_calls(chunks)
        print(f"reasoning: ")
        print(f"function name: ")
        print(f"function arguments: ")
        print("\n\n")

    if __name__ == "__main__":
        main()