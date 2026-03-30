# request sent to model set on litellm proxy, `litellm --model`
response = client.chat.completions.create(model="gpt-3.5-turbo", messages = [\
    {\
        "role": "user",\
        "content": "this is a test request, write a short poem"\
    }\
])

print(response)

```

## More details [​](https://docs.litellm.ai/\#more-details "Direct link to More details")

- [exception mapping](https://docs.litellm.ai/docs/exception_mapping)
- [E2E Tutorial for LiteLLM Proxy Server](https://docs.litellm.ai/docs/proxy/docker_quick_start)
- [proxy virtual keys & spend management](https://docs.litellm.ai/docs/proxy/virtual_keys)

- [**Call 100+ LLMs using the OpenAI Input/Output Format**](https://docs.litellm.ai/#call-100-llms-using-the-openai-inputoutput-format)
- [How to use LiteLLM](https://docs.litellm.ai/#how-to-use-litellm)
  - [**When to use LiteLLM Proxy Server (LLM Gateway)**](https://docs.litellm.ai/#when-to-use-litellm-proxy-server-llm-gateway)
  - [**When to use LiteLLM Python SDK**](https://docs.litellm.ai/#when-to-use-litellm-python-sdk)
- [**LiteLLM Python SDK**](https://docs.litellm.ai/#litellm-python-sdk)
  - [Basic usage](https://docs.litellm.ai/#basic-usage)
  - [Streaming](https://docs.litellm.ai/#streaming)
  - [Exception handling](https://docs.litellm.ai/#exception-handling)
  - [Logging Observability - Log LLM Input/Output (Docs)](https://docs.litellm.ai/#logging-observability---log-llm-inputoutput-docs)
  - [Track Costs, Usage, Latency for streaming](https://docs.litellm.ai/#track-costs-usage-latency-for-streaming)
- [**LiteLLM Proxy Server (LLM Gateway)**](https://docs.litellm.ai/#litellm-proxy-server-llm-gateway)
  - [📖 Proxy Endpoints - Swagger Docs](https://docs.litellm.ai/#-proxy-endpoints---swagger-docs)
  - [Quick Start Proxy - CLI](https://docs.litellm.ai/#quick-start-proxy---cli)
  - [Step 1. CREATE config.yaml](https://docs.litellm.ai/#step-1-create-configyaml)
  - [Step 2. RUN Docker Image](https://docs.litellm.ai/#step-2-run-docker-image)
- [More details](https://docs.litellm.ai/#more-details)

## Completion Function Guide
[Skip to main content](https://docs.litellm.ai/completion/input#__docusaurus_skipToContent_fallback)