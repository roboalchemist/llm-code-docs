# LiteLLM - Getting Started

[https://github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)

## **Call 100+ LLMs using the OpenAI Input/Output Format** [​](https://docs.litellm.ai/\#call-100-llms-using-the-openai-inputoutput-format "Direct link to call-100-llms-using-the-openai-inputoutput-format")

- Translate inputs to provider's `completion`, `embedding`, and `image_generation` endpoints
- [Consistent output](https://docs.litellm.ai/docs/completion/output), text responses will always be available at `['choices'][0]['message']['content']`
- Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)
- Track spend & set budgets per project [LiteLLM Proxy Server](https://docs.litellm.ai/docs/simple_proxy)

## How to use LiteLLM [​](https://docs.litellm.ai/\#how-to-use-litellm "Direct link to How to use LiteLLM")

You can use litellm through either:

1. [LiteLLM Proxy Server](https://docs.litellm.ai/#litellm-proxy-server-llm-gateway) \- Server (LLM Gateway) to call 100+ LLMs, load balance, cost tracking across projects
2. [LiteLLM python SDK](https://docs.litellm.ai/#basic-usage) \- Python Client to call 100+ LLMs, load balance, cost tracking

### **When to use LiteLLM Proxy Server (LLM Gateway)** [​](https://docs.litellm.ai/\#when-to-use-litellm-proxy-server-llm-gateway "Direct link to when-to-use-litellm-proxy-server-llm-gateway")

tip

Use LiteLLM Proxy Server if you want a **central service (LLM Gateway) to access multiple LLMs**

Typically used by Gen AI Enablement / ML PLatform Teams

- LiteLLM Proxy gives you a unified interface to access multiple LLMs (100+ LLMs)
- Track LLM Usage and setup guardrails
- Customize Logging, Guardrails, Caching per project

### **When to use LiteLLM Python SDK** [​](https://docs.litellm.ai/\#when-to-use-litellm-python-sdk "Direct link to when-to-use-litellm-python-sdk")

tip

Use LiteLLM Python SDK if you want to use LiteLLM in your **python code**

Typically used by developers building llm projects

- LiteLLM SDK gives you a unified interface to access multiple LLMs (100+ LLMs)
- Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)

## **LiteLLM Python SDK** [​](https://docs.litellm.ai/\#litellm-python-sdk "Direct link to litellm-python-sdk")

### Basic usage [​](https://docs.litellm.ai/\#basic-usage "Direct link to Basic usage")

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/liteLLM_Getting_Started.ipynb)

```codeBlockLines_e6Vv
pip install litellm

```

- OpenAI
- Anthropic
- VertexAI
- NVIDIA
- HuggingFace
- Azure OpenAI
- Ollama
- Openrouter
- Novita AI

```codeBlockLines_e6Vv
from litellm import completion
import os

## set ENV variables
os.environ["OPENAI_API_KEY"] = "your-api-key"

response = completion(
  model="gpt-3.5-turbo",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)

```

```codeBlockLines_e6Vv
from litellm import completion
import os

## set ENV variables
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

response = completion(
  model="claude-2",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)

```

```codeBlockLines_e6Vv
from litellm import completion
import os