# Source: https://docs.vllm.ai/en/stable/examples/online_serving/openai_chat_completion_client/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/openai_chat_completion_client.md "Edit this page")

# OpenAI Chat Completion Client[¶](#openai-chat-completion-client "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """Example Python client for OpenAI Chat Completion using vLLM API server
    NOTE: start a supported chat completion model server with `vllm serve`, e.g.
        vllm serve meta-llama/Llama-2-7b-chat-hf
    """

    import argparse

    from openai import OpenAI

    # Modify OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"

    messages = [
        ,
        ,
        ,
        ,
    ]

    def parse_args():
        parser = argparse.ArgumentParser(description="Client for vLLM API server")
        parser.add_argument(
            "--stream", action="store_true", help="Enable streaming response"
        )
        return parser.parse_args()

    def main(args):
        client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key=openai_api_key,
            base_url=openai_api_base,
        )

        models = client.models.list()
        model = models.data[0].id

        # Chat Completion API
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model,
            stream=args.stream,
        )

        print("-" * 50)
        print("Chat completion results:")
        if args.stream:
            for c in chat_completion:
                print(c)
        else:
            print(chat_completion)
        print("-" * 50)

    if __name__ == "__main__":
        args = parse_args()
        main(args)