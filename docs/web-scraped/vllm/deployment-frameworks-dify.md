# Source: https://docs.vllm.ai/en/stable/deployment/frameworks/dify/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/dify.md "Edit this page")

# Dify[¶](#dify "Permanent link")

[Dify](https://github.com/langgenius/dify) is an open-source LLM app development platform. Its intuitive interface combines agentic AI workflow, RAG pipeline, agent capabilities, model management, observability features, and more, allowing you to quickly move from prototype to production.

It supports vLLM as a model provider to efficiently serve large language models.

This guide walks you through deploying Dify using a vLLM backend.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM environment:

    pip install vllm

And install [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

## Deploy[¶](#deploy "Permanent link")

1.  Start the vLLM server with the supported chat completion model, e.g.

    ::: 
        vllm serve Qwen/Qwen1.5-7B-Chat
    :::

2.  Start the Dify server with docker compose ([details](https://github.com/langgenius/dify?tab=readme-ov-file#quick-start)):

    ::: 
        git clone https://github.com/langgenius/dify.git
        cd dify
        cd docker
        cp .env.example .env
        docker compose up -d
    :::

3.  Open the browser to access `http://localhost/install`, config the basic login information and login.

4.  In the top-right user menu (under the profile icon), go to Settings, then click `Model Provider`, and locate the `vLLM` provider to install it.

5.  Fill in the model provider details as follows:

    -   **Model Type**: `LLM`
    -   **Model Name**: `Qwen/Qwen1.5-7B-Chat`
    -   **API Endpoint URL**: `http://:/v1`
    -   **Model Name for API Endpoint**: `Qwen/Qwen1.5-7B-Chat`
    -   **Completion Mode**: `Completion`

    [![Dify settings screen](../../../assets/deployment/dify-settings.png)](../../../assets/deployment/dify-settings.png)

6.  To create a test chatbot, go to `Studio → Chatbot → Create from Blank`, then select Chatbot as the type:

    [![Dify create chatbot screen](../../../assets/deployment/dify-create-chatbot.png)](../../../assets/deployment/dify-create-chatbot.png)

7.  Click the chatbot you just created to open the chat interface and start interacting with the model:

    [![Dify chat screen](../../../assets/deployment/dify-chat.png)](../../../assets/deployment/dify-chat.png)

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 14, 2025] ]