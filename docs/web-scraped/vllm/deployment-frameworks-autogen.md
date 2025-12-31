# Source: https://docs.vllm.ai/en/stable/deployment/frameworks/autogen/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/autogen.md "Edit this page")

# AutoGen[¶](#autogen "Permanent link")

[AutoGen](https://github.com/microsoft/autogen) is a framework for creating multi-agent AI applications that can act autonomously or work alongside humans.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM and [AutoGen](https://microsoft.github.io/autogen/0.2/docs/installation/) environment:

    pip install vllm

    # Install AgentChat and OpenAI client from Extensions
    # AutoGen requires Python 3.10 or later.
    pip install -U "autogen-agentchat" "autogen-ext[openai]"

## Deploy[¶](#deploy "Permanent link")

1.  Start the vLLM server with the supported chat completion model, e.g.

    ::: 
        vllm serve mistralai/Mistral-7B-Instruct-v0.2
    :::

2.  Call it with AutoGen:

Code

    import asyncio
    from autogen_core.models import UserMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient
    from autogen_core.models import ModelFamily

    async def main() -> None:
        # Create a model client
        model_client = OpenAIChatCompletionClient(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            base_url="http://:/v1",
            api_key="EMPTY",
            model_info=,
        )

        messages = [UserMessage(content="Write a very short story about a dragon.", source="user")]

        # Create a stream.
        stream = model_client.create_stream(messages=messages)

        # Iterate over the stream and print the responses.
        print("Streamed responses:")
        async for response in stream:
            if isinstance(response, str):
                # A partial response is a string.
                print(response, flush=True, end="")
            else:
                # The last response is a CreateResult object with the complete message.
                print("\n\n------------\n")
                print("The complete response:", flush=True)
                print(response.content, flush=True)

        # Close the client when done.
        await model_client.close()

    asyncio.run(main())

For details, see the tutorial:

-   [Using vLLM in AutoGen](https://microsoft.github.io/autogen/0.2/docs/topics/non-openai-models/local-vllm/)

-   [OpenAI-compatible API examples](https://microsoft.github.io/autogen/stable/reference/python/autogen_ext.models.openai.html#autogen_ext.models.openai.OpenAIChatCompletionClient)

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 2, 2025] ]