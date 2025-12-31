# Source: https://docs.vllm.ai/en/stable/examples/online_serving/openai_transcription_client/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/openai_transcription_client.md "Edit this page")

# OpenAI Transcription Client[¶](#openai-transcription-client "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_transcription_client.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    This script demonstrates how to use the vLLM API server to perform audio
    transcription with the `openai/whisper-large-v3` model.

    Before running this script, you must start the vLLM server with the following command:

        vllm serve openai/whisper-large-v3

    Requirements:
    - vLLM with audio support
    - openai Python SDK
    - httpx for streaming support

    The script performs:
    1. Synchronous transcription using OpenAI-compatible API.
    2. Streaming transcription using raw HTTP request to the vLLM server.
    """

    import asyncio

    from openai import AsyncOpenAI, OpenAI

    from vllm.assets.audio import AudioAsset

    def sync_openai(audio_path: str, client: OpenAI):
        """
        Perform synchronous transcription using OpenAI-compatible API.
        """
        with open(audio_path, "rb") as f:
            transcription = client.audio.transcriptions.create(
                file=f,
                model="openai/whisper-large-v3",
                language="en",
                response_format="json",
                temperature=0.0,
                # Additional sampling params not provided by OpenAI API.
                extra_body=dict(
                    seed=4419,
                    repetition_penalty=1.3,
                ),
            )
            print("transcription result:", transcription.text)

    async def stream_openai_response(audio_path: str, client: AsyncOpenAI):
        """
        Perform asynchronous transcription using OpenAI-compatible API.
        """
        print("\ntranscription result:", end=" ")
        with open(audio_path, "rb") as f:
            transcription = await client.audio.transcriptions.create(
                file=f,
                model="openai/whisper-large-v3",
                language="en",
                response_format="json",
                temperature=0.0,
                # Additional sampling params not provided by OpenAI API.
                extra_body=dict(
                    seed=420,
                    top_p=0.6,
                ),
                stream=True,
            )
            async for chunk in transcription:
                if chunk.choices:
                    content = chunk.choices[0].get("delta", ).get("content")
                    print(content, end="", flush=True)

        print()  # Final newline after stream ends

    def main():
        mary_had_lamb = str(AudioAsset("mary_had_lamb").get_local_path())
        winning_call = str(AudioAsset("winning_call").get_local_path())

        # Modify OpenAI's API key and API base to use vLLM's API server.
        openai_api_key = "EMPTY"
        openai_api_base = "http://localhost:8000/v1"
        client = OpenAI(
            api_key=openai_api_key,
            base_url=openai_api_base,
        )

        sync_openai(mary_had_lamb, client)
        # Run the asynchronous function
        client = AsyncOpenAI(
            api_key=openai_api_key,
            base_url=openai_api_base,
        )
        asyncio.run(stream_openai_response(winning_call, client))

    if __name__ == "__main__":
        main()