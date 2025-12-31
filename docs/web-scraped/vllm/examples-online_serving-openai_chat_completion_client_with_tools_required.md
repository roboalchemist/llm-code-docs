# Source: https://docs.vllm.ai/en/stable/examples/online_serving/openai_chat_completion_client_with_tools_required/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/openai_chat_completion_client_with_tools_required.md "Edit this page")

# OpenAI Chat Completion Client With Tools Required[¶](#openai-chat-completion-client-with-tools-required "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client_with_tools_required.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    To run this example, you can start the vLLM server
    without any specific flags:

    ```bash
    vllm serve unsloth/Llama-3.2-1B-Instruct \
        --structured-outputs-config.backend outlines
    ```

    This example demonstrates how to generate chat completions
    using the OpenAI Python client library.
    """

    from openai import OpenAI

    # Modify OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"

    tools = [
        ,
                        "state": ,
                        "unit": ,
                    },
                    "required": ["city", "state", "unit"],
                },
            },
        },
        ,
                        "state": ,
                        "days": ,
                        "unit": ,
                    },
                    "required": ["city", "state", "days", "unit"],
                },
            },
        },
    ]

    messages = [
        ,
        ,
        ,
    ]

    def main():
        client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key=openai_api_key,
            base_url=openai_api_base,
        )

        models = client.models.list()
        model = models.data[0].id

        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model,
            tools=tools,
            tool_choice="required",
            stream=True,  # Enable streaming response
        )

        for chunk in chat_completion:
            if chunk.choices and chunk.choices[0].delta.tool_calls:
                print(chunk.choices[0].delta.tool_calls)

        chat_completion = client.chat.completions.create(
            messages=messages, model=model, tools=tools, tool_choice="required"
        )

        print(chat_completion.choices[0].message.tool_calls)

    if __name__ == "__main__":
        main()