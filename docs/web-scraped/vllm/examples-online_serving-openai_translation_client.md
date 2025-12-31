# Source: https://docs.vllm.ai/en/stable/examples/online_serving/openai_translation_client/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/openai_translation_client.md "Edit this page")

# OpenAI Translation Client[¶](#openai-translation-client "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_translation_client.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    import asyncio
    import json

    import httpx
    from openai import OpenAI

    from vllm.assets.audio import AudioAsset

    def sync_openai(audio_path: str, client: OpenAI):
        with open(audio_path, "rb") as f:
            translation = client.audio.translations.create(
                file=f,
                model="openai/whisper-large-v3",
                response_format="json",
                temperature=0.0,
                # Additional params not provided by OpenAI API.
                extra_body=dict(
                    language="it",
                    seed=4419,
                    repetition_penalty=1.3,
                ),
            )
            print("translation result:", translation.text)

    async def stream_openai_response(audio_path: str, base_url: str, api_key: str):
        data = 
        url = base_url + "/audio/translations"
        headers = "}
        print("translation result:", end=" ")
        # OpenAI translation API client does not support streaming.
        async with httpx.AsyncClient() as client:
            with open(audio_path, "rb") as f:
                async with client.stream(
                    "POST", url, files=, data=data, headers=headers
                ) as response:
                    async for line in response.aiter_lines():
                        # Each line is a JSON object prefixed with 'data: '
                        if line:
                            if line.startswith("data: "):
                                line = line[len("data: ") :]
                            # Last chunk, stream ends
                            if line.strip() == "[DONE]":
                                break
                            # Parse the JSON response
                            chunk = json.loads(line)
                            # Extract and print the content
                            content = chunk["choices"][0].get("delta", ).get("content")
                            print(content, end="")

    def main():
        foscolo = str(AudioAsset("azacinto_foscolo").get_local_path())

        # Modify OpenAI's API key and API base to use vLLM's API server.
        openai_api_key = "EMPTY"
        openai_api_base = "http://localhost:8000/v1"
        client = OpenAI(
            api_key=openai_api_key,
            base_url=openai_api_base,
        )
        sync_openai(foscolo, client)
        # Run the asynchronous function
        asyncio.run(stream_openai_response(foscolo, openai_api_base, openai_api_key))

    if __name__ == "__main__":
        main()