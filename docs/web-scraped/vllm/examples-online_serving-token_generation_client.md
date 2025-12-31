# Source: https://docs.vllm.ai/en/stable/examples/online_serving/token_generation_client/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/token_generation_client.md "Edit this page")

# Token Generation Client[¶](#token-generation-client "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/token_generation_client.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    import httpx
    from transformers import AutoTokenizer

    GEN_ENDPOINT = "http://localhost:8000/inference/v1/generate"
    DUMMY_API_KEY = "empty"
    MODEL_NAME = "Qwen/Qwen3-0.6B"

    transport = httpx.HTTPTransport()
    headers = "}
    client = httpx.Client(
        transport=transport,
        base_url=GEN_ENDPOINT,
        timeout=600,
        headers=headers,
    )
    messages = [
        ,
        ,
    ]

    def main(client):
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        token_ids = tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            enable_thinking=False,
        )
        payload = ,
            "stream": False,
        }
        resp = client.post(GEN_ENDPOINT, json=payload)
        resp.raise_for_status()
        data = resp.json()
        print(data)
        print("-" * 50)
        print("Token generation results:")
        res = tokenizer.decode(data["choices"][0]["token_ids"])
        print(res)
        print("-" * 50)

    if __name__ == "__main__":
        main(client)