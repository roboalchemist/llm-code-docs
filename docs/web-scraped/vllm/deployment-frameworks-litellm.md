# Source: https://docs.vllm.ai/en/stable/deployment/frameworks/litellm/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/litellm.md "Edit this page")

# LiteLLM[¶](#litellm "Permanent link")

[LiteLLM](https://github.com/BerriAI/litellm) call all LLM APIs using the OpenAI format \[Bedrock, Huggingface, VertexAI, TogetherAI, Azure, OpenAI, Groq etc.\]

LiteLLM manages:

-   Translate inputs to provider\'s `completion`, `embedding`, and `image_generation` endpoints
-   [Consistent output](https://docs.litellm.ai/docs/completion/output), text responses will always be available at `['choices'][0]['message']['content']`
-   Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)
-   Set Budgets & Rate limits per project, api key, model [LiteLLM Proxy Server (LLM Gateway)](https://docs.litellm.ai/docs/simple_proxy)

And LiteLLM supports all models on VLLM.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM and litellm environment:

    pip install vllm litellm

## Deploy[¶](#deploy "Permanent link")

### Chat completion[¶](#chat-completion "Permanent link")

1.  Start the vLLM server with the supported chat completion model, e.g.

    ::: 
        vllm serve qwen/Qwen1.5-0.5B-Chat
    :::

2.  Call it with litellm:

Code

    import litellm 

    messages = []

    # hosted_vllm is prefix key word and necessary
    response = litellm.completion(
        model="hosted_vllm/qwen/Qwen1.5-0.5B-Chat", # pass the vllm model name
        messages=messages,
        api_base="http://:/v1",
        temperature=0.2,
        max_tokens=80,
    )

    print(response)

### Embeddings[¶](#embeddings "Permanent link")

1.  Start the vLLM server with the supported embedding model, e.g.

    ::: 
        vllm serve BAAI/bge-base-en-v1.5
    :::

2.  Call it with litellm:

    from litellm import embedding   
    import os

    os.environ["HOSTED_VLLM_API_BASE"] = "http://:/v1"

    # hosted_vllm is prefix key word and necessary
    # pass the vllm model name
    embedding = embedding(model="hosted_vllm/BAAI/bge-base-en-v1.5", input=["Hello world"])

    print(embedding)

For details, see the tutorial [Using vLLM in LiteLLM](https://docs.litellm.ai/docs/providers/vllm).

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 14, 2025] ]