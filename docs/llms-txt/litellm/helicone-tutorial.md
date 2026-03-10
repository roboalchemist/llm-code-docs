# Helicone Tutorial

[Helicone](https://helicone.ai/) is an open source observability platform that proxies your OpenAI traffic and provides you key insights into your spend, latency and usage.

## Use Helicone to log requests across all LLM Providers (OpenAI, Azure, Anthropic, Cohere, Replicate, PaLM) [​](https://docs.litellm.ai/observability/helicone_integration\#use-helicone-to-log-requests-across-all-llm-providers-openai-azure-anthropic-cohere-replicate-palm "Direct link to Use Helicone to log requests across all LLM Providers (OpenAI, Azure, Anthropic, Cohere, Replicate, PaLM)")

liteLLM provides `success_callbacks` and `failure_callbacks`, making it easy for you to send data to a particular provider depending on the status of your responses.

In this case, we want to log requests to Helicone when a request succeeds.

### Approach 1: Use Callbacks [​](https://docs.litellm.ai/observability/helicone_integration\#approach-1-use-callbacks "Direct link to Approach 1: Use Callbacks")

Use just 1 line of code, to instantly log your responses **across all providers** with helicone:

```codeBlockLines_e6Vv
litellm.success_callback=["helicone"]

```

Complete code

```codeBlockLines_e6Vv
from litellm import completion

## set env variables
os.environ["HELICONE_API_KEY"] = "your-helicone-key"
os.environ["OPENAI_API_KEY"], os.environ["COHERE_API_KEY"] = "", ""