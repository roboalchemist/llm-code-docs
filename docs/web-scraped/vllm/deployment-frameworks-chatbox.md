# Source: https://docs.vllm.ai/en/stable/deployment/frameworks/chatbox/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/chatbox.md "Edit this page")

# Chatbox[¶](#chatbox "Permanent link")

[Chatbox](https://github.com/chatboxai/chatbox) is a desktop client for LLMs, available on Windows, Mac, Linux.

It allows you to deploy a large language model (LLM) server with vLLM as the backend, which exposes OpenAI-compatible endpoints.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM environment:

    pip install vllm

## Deploy[¶](#deploy "Permanent link")

1.  Start the vLLM server with the supported chat completion model, e.g.

    ::: 
        vllm serve qwen/Qwen1.5-0.5B-Chat
    :::

2.  Download and install [Chatbox desktop](https://chatboxai.app/en#download).

3.  On the bottom left of settings, Add Custom Provider

    -   API Mode: `OpenAI API Compatible`
    -   Name: vllm
    -   API Host: `http://:/v1`
    -   API Path: `/chat/completions`
    -   Model: `qwen/Qwen1.5-0.5B-Chat`

    [![Chatbox settings screen](../../../assets/deployment/chatbox-settings.png)](../../../assets/deployment/chatbox-settings.png)

4.  Go to `Just chat`, and start to chat:

    [![Chatbot chat screen](../../../assets/deployment/chatbox-chat.png)](../../../assets/deployment/chatbox-chat.png)

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 14, 2025] ]