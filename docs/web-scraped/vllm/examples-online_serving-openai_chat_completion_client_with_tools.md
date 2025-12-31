# Source: https://docs.vllm.ai/en/stable/examples/online_serving/openai_chat_completion_client_with_tools/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/openai_chat_completion_client_with_tools.md "Edit this page")

# OpenAI Chat Completion Client With Tools[¶](#openai-chat-completion-client-with-tools "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client_with_tools.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    Set up this example by starting a vLLM OpenAI-compatible server with tool call
    options enabled. For example:

    IMPORTANT: for mistral, you must use one of the provided mistral tool call
    templates, or your own - the model default doesn't work for tool calls with vLLM
    See the vLLM docs on OpenAI server & tool calling for more details.

    vllm serve mistralai/Mistral-7B-Instruct-v0.3 \
                --chat-template examples/tool_chat_template_mistral.jinja \
                --enable-auto-tool-choice --tool-call-parser mistral

    OR
    vllm serve NousResearch/Hermes-2-Pro-Llama-3-8B \
                --chat-template examples/tool_chat_template_hermes.jinja \
                --enable-auto-tool-choice --tool-call-parser hermes
    """

    import json
    from typing import Any

    from openai import OpenAI

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

    def get_current_weather(city: str, state: str, unit: "str"):
        return (
            "The weather in Dallas, Texas is 85 degrees fahrenheit. It is "
            "partly cloudly, with highs in the 90's."
        )

    def handle_tool_calls_stream(
        client: OpenAI,
        messages: list[dict[str, str]],
        model: str,
        tools: list[dict[str, Any]],
    ) -> list[Any]:
        tool_calls_stream = client.chat.completions.create(
            messages=messages, model=model, tools=tools, stream=True
        )
        chunks = []
        print("chunks: ")
        for chunk in tool_calls_stream:
            chunks.append(chunk)
            if chunk.choices[0].delta.tool_calls:
                print(chunk.choices[0].delta.tool_calls[0])
            else:
                print(chunk.choices[0].delta)
        return chunks

    def handle_tool_calls_arguments(chunks: list[Any]) -> list[str]:
        arguments = []
        tool_call_idx = -1
        print("arguments: ")
        for chunk in chunks:
            if chunk.choices[0].delta.tool_calls:
                tool_call = chunk.choices[0].delta.tool_calls[0]
                if tool_call.index != tool_call_idx:
                    if tool_call_idx >= 0:
                        print(f"streamed tool call arguments: ")
                    tool_call_idx = chunk.choices[0].delta.tool_calls[0].index
                    arguments.append("")
                if tool_call.id:
                    print(f"streamed tool call id:  ")

                if tool_call.function:
                    if tool_call.function.name:
                        print(f"streamed tool call name: ")

                    if tool_call.function.arguments:
                        arguments[tool_call_idx] += tool_call.function.arguments

        return arguments

    def main():
        # Initialize OpenAI client
        client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key=openai_api_key,
            base_url=openai_api_base,
        )

        # Get available models and select one
        models = client.models.list()
        model = models.data[0].id

        chat_completion = client.chat.completions.create(
            messages=messages, model=model, tools=tools
        )

        print("-" * 70)
        print("Chat completion results:")
        print(chat_completion)
        print("-" * 70)

        # Stream tool calls
        chunks = handle_tool_calls_stream(client, messages, model, tools)
        print("-" * 70)

        # Handle arguments from streamed tool calls
        arguments = handle_tool_calls_arguments(chunks)

        if len(arguments):
            print(f"streamed tool call arguments: \n")

        print("-" * 70)

        # Add tool call results to the conversation
        messages.append(
            
        )

        # Now, simulate a tool call
        available_tools = 

        completion_tool_calls = chat_completion.choices[0].message.tool_calls
        for call in completion_tool_calls:
            tool_to_call = available_tools[call.function.name]
            args = json.loads(call.function.arguments)
            result = tool_to_call(**args)
            print("tool_to_call result: ", result)
            messages.append(
                
            )

        chat_completion_2 = client.chat.completions.create(
            messages=messages, model=model, tools=tools, stream=False
        )
        print("Chat completion2 results:")
        print(chat_completion_2)
        print("-" * 70)

    if __name__ == "__main__":
        main()