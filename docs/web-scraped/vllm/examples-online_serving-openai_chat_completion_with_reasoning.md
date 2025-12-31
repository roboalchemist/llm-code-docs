# Source: https://docs.vllm.ai/en/stable/examples/online_serving/openai_chat_completion_with_reasoning/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/openai_chat_completion_with_reasoning.md "Edit this page")

# OpenAI Chat Completion With Reasoning[¶](#openai-chat-completion-with-reasoning "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_with_reasoning.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    An example shows how to generate chat completions from reasoning models
    like DeepSeekR1.

    To run this example, you need to start the vLLM server
    with the reasoning parser:

    ```bash
    vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B \
        --reasoning-parser deepseek_r1
    ```

    This example demonstrates how to generate chat completions from reasoning models
    using the OpenAI Python client library.
    """

    from openai import OpenAI

    # Modify OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"

    def main():
        client = OpenAI(
            api_key=openai_api_key,
            base_url=openai_api_base,
        )

        models = client.models.list()
        model = models.data[0].id

        # Round 1
        messages = []
        # ruff: noqa: E501
        # For granite, add: `extra_body=}`
        response = client.chat.completions.create(model=model, messages=messages)

        reasoning = response.choices[0].message.reasoning
        content = response.choices[0].message.content

        print("reasoning for Round 1:", reasoning)
        print("content for Round 1:", content)

        # Round 2
        messages.append()
        messages.append(
            
        )
        response = client.chat.completions.create(model=model, messages=messages)

        reasoning = response.choices[0].message.reasoning
        content = response.choices[0].message.content

        print("reasoning for Round 2:", reasoning)
        print("content for Round 2:", content)

    if __name__ == "__main__":
        main()