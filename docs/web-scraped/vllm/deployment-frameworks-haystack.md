# Source: https://docs.vllm.ai/en/stable/deployment/frameworks/haystack/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/haystack.md "Edit this page")

# Haystack[¶](#haystack "Permanent link")

[Haystack](https://github.com/deepset-ai/haystack) is an end-to-end LLM framework that allows you to build applications powered by LLMs, Transformer models, vector search and more. Whether you want to perform retrieval-augmented generation (RAG), document search, question answering or answer generation, Haystack can orchestrate state-of-the-art embedding models and LLMs into pipelines to build end-to-end NLP applications and solve your use case.

It allows you to deploy a large language model (LLM) server with vLLM as the backend, which exposes OpenAI-compatible endpoints.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM and Haystack environment:

    pip install vllm haystack-ai

## Deploy[¶](#deploy "Permanent link")

1.  Start the vLLM server with the supported chat completion model, e.g.

    ::: 
        vllm serve mistralai/Mistral-7B-Instruct-v0.1
    :::

2.  Use the `OpenAIGenerator` and `OpenAIChatGenerator` components in Haystack to query the vLLM server.

Code

    from haystack.components.generators.chat import OpenAIChatGenerator
    from haystack.dataclasses import ChatMessage
    from haystack.utils import Secret

    generator = OpenAIChatGenerator(
        # for compatibility with the OpenAI API, a placeholder api_key is needed
        api_key=Secret.from_token("VLLM-PLACEHOLDER-API-KEY"),
        model="mistralai/Mistral-7B-Instruct-v0.1",
        api_base_url="http://:/v1",
        generation_kwargs=,
    )

    response = generator.run(
      messages=[ChatMessage.from_user("Hi. Can you help me plan my next trip to Italy?")]
    )

    print("-"*30)
    print(response)
    print("-"*30)

    ------------------------------
    })]}
    ------------------------------

For details, see the tutorial [Using vLLM in Haystack](https://github.com/deepset-ai/haystack-integrations/blob/main/integrations/vllm.md).

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 14, 2025] ]