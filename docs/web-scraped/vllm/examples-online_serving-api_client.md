# Source: https://docs.vllm.ai/en/stable/examples/online_serving/api_client/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/api_client.md "Edit this page")

# API Client[¶](#api-client "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/api_client.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """Example Python client for `vllm.entrypoints.api_server`
    Start the demo server:
        python -m vllm.entrypoints.api_server --model <model_name>

    NOTE: The API server is used only for demonstration and simple performance
    benchmarks. It is not intended for production use.
    For production use, we recommend `vllm serve` and the OpenAI client API.
    """

    import argparse
    import json
    from argparse import Namespace
    from collections.abc import Iterable

    import requests

    def clear_line(n: int = 1) -> None:
        LINE_UP = "\033[1A"
        LINE_CLEAR = "\x1b[2K"
        for _ in range(n):
            print(LINE_UP, end=LINE_CLEAR, flush=True)

    def post_http_request(
        prompt: str, api_url: str, n: int = 1, stream: bool = False
    ) -> requests.Response:
        headers = 
        pload = 
        response = requests.post(api_url, headers=headers, json=pload, stream=stream)
        return response

    def get_streaming_response(response: requests.Response) -> Iterable[list[str]]:
        for chunk in response.iter_lines(
            chunk_size=8192, decode_unicode=False, delimiter=b"\n"
        ):
            if chunk:
                data = json.loads(chunk.decode("utf-8"))
                output = data["text"]
                yield output

    def get_response(response: requests.Response) -> list[str]:
        data = json.loads(response.content)
        output = data["text"]
        return output

    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("--host", type=str, default="localhost")
        parser.add_argument("--port", type=int, default=8000)
        parser.add_argument("--n", type=int, default=1)
        parser.add_argument("--prompt", type=str, default="San Francisco is a")
        parser.add_argument("--stream", action="store_true")
        return parser.parse_args()

    def main(args: Namespace):
        prompt = args.prompt
        api_url = f"http://:/generate"
        n = args.n
        stream = args.stream

        print(f"Prompt: \n", flush=True)
        response = post_http_request(prompt, api_url, n, stream)

        if stream:
            num_printed_lines = 0
            for h in get_streaming_response(response):
                clear_line(num_printed_lines)
                num_printed_lines = 0
                for i, line in enumerate(h):
                    num_printed_lines += 1
                    print(f"Beam candidate : ", flush=True)
        else:
            output = get_response(response)
            for i, line in enumerate(output):
                print(f"Beam candidate : ", flush=True)

    if __name__ == "__main__":
        args = parse_args()
        main(args)