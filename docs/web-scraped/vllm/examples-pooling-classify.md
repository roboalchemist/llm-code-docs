# Source: https://docs.vllm.ai/en/stable/examples/pooling/classify/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/pooling/classify.md "Edit this page")

# Classify[¶](#classify "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/pooling/classify>.

## OpenAI Classification Client[¶](#openai-classification-client "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """Example Python client for classification API using vLLM API server
    NOTE:
        start a supported classification model server with `vllm serve`, e.g.
        vllm serve jason9693/Qwen2.5-1.5B-apeach
    """

    import argparse
    import pprint

    import requests

    def post_http_request(payload: dict, api_url: str) -> requests.Response:
        headers = 
        response = requests.post(api_url, headers=headers, json=payload)
        return response

    def parse_args():
        parse = argparse.ArgumentParser()
        parse.add_argument("--host", type=str, default="localhost")
        parse.add_argument("--port", type=int, default=8000)
        parse.add_argument("--model", type=str, default="jason9693/Qwen2.5-1.5B-apeach")
        return parse.parse_args()

    def main(args):
        host = args.host
        port = args.port
        model_name = args.model

        api_url = f"http://:/classify"
        prompts = [
            "Hello, my name is",
            "The president of the United States is",
            "The capital of France is",
            "The future of AI is",
        ]

        payload = 

        classify_response = post_http_request(payload=payload, api_url=api_url)
        pprint.pprint(classify_response.json())

    if __name__ == "__main__":
        args = parse_args()
        main(args)