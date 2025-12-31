# Source: https://docs.vllm.ai/en/stable/deployment/frameworks/anything-llm/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/anything-llm.md "Edit this page")

# AnythingLLM[¶](#anythingllm "Permanent link")

[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) is a full-stack application that enables you to turn any document, resource, or piece of content into context that any LLM can use as references during chatting.

It allows you to deploy a large language model (LLM) server with vLLM as the backend, which exposes OpenAI-compatible endpoints.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM environment:

    pip install vllm

## Deploy[¶](#deploy "Permanent link")

1.  Start the vLLM server with a supported chat-completion model, for example:

    ::: 
        vllm serve Qwen/Qwen1.5-32B-Chat-AWQ --max-model-len 4096
    :::

2.  Download and install [AnythingLLM Desktop](https://anythingllm.com/desktop).

3.  Configure the AI provider:

    -   At the bottom, click the 🔧 wrench icon -\> **Open settings** -\> **AI Providers** -\> **LLM**.
    -   Enter the following values:
        -   LLM Provider: Generic OpenAI
        -   Base URL: `http://:/v1`
        -   Chat Model Name: `Qwen/Qwen1.5-32B-Chat-AWQ`

    [![set AI providers](../../../assets/deployment/anything-llm-provider.png)](../../../assets/deployment/anything-llm-provider.png)

4.  Create a workspace:

    1.  At the bottom, click the ↺ back icon and back to workspaces.
    2.  Create a workspace (e.g., `vllm`) and start chatting.

    [![create a workspace](../../../assets/deployment/anything-llm-chat-without-doc.png)](../../../assets/deployment/anything-llm-chat-without-doc.png)

5.  Add a document.

    1.  Click the 📎 attachment icon.
    2.  Upload a document.
    3.  Select and move the document into your workspace.
    4.  Save and embed it.

    [![add a document](../../../assets/deployment/anything-llm-upload-doc.png)](../../../assets/deployment/anything-llm-upload-doc.png)

6.  Chat using your document as context.

    [![chat with your context](../../../assets/deployment/anything-llm-chat-with-doc.png)](../../../assets/deployment/anything-llm-chat-with-doc.png)

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [September 11, 2025] ]