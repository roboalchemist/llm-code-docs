# Source: https://docs.vllm.ai/en/stable/deployment/frameworks/open-webui/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/open-webui.md "Edit this page")

# Open WebUI[¶](#open-webui "Permanent link")

[Open WebUI](https://github.com/open-webui/open-webui) is an extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline. It supports various LLM runners like Ollama and OpenAI-compatible APIs, with built-in RAG capabilities, making it a powerful AI deployment solution.

To get started with Open WebUI using vLLM, follow these steps:

1.  Install the [Docker](https://docs.docker.com/engine/install/).

2.  Start the vLLM server with a supported chat completion model:

    ::: 
        vllm serve Qwen/Qwen3-0.6B-Chat
    :::

    ::: 
    Note

    When starting the vLLM server, be sure to specify the host and port using the `--host` and `--port` flags. For example:

    ::: 
        vllm serve <model> --host 0.0.0.0 --port 8000
    :::
    :::

3.  Start the Open WebUI Docker container:

    ::: 
        docker run -d \
            --name open-webui \
            -p 3000:8080 \
            -v open-webui:/app/backend/data \
            -e OPENAI_API_BASE_URL=http://0.0.0.0:8000/v1 \
            --restart always \
            ghcr.io/open-webui/open-webui:main
    :::

4.  Open it in the browser: <http://open-webui-host:3000/>

    At the top of the page, you should see the model `Qwen/Qwen3-0.6B-Chat`.

    [![Web portal of model Qwen/Qwen3-0.6B-Chat](../../../assets/deployment/open_webui.png)](../../../assets/deployment/open_webui.png)

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 2, 2025] ]