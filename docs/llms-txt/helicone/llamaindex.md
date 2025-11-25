# Source: https://docs.helicone.ai/integrations/openai/llamaindex.md

# Source: https://docs.helicone.ai/gateway/integrations/llamaindex.md

# Source: https://docs.helicone.ai/integrations/openai/llamaindex.md

# Source: https://docs.helicone.ai/gateway/integrations/llamaindex.md

# LlamaIndex Integration

> Use the Helicone LLM for LlamaIndex to route OpenAI-compatible requests through the Helicone AI Gateway with full observability.

## Introduction

The Helicone LLM for LlamaIndex lets you send OpenAI‑compatible requests through the Helicone AI Gateway — no provider keys needed. Gain centralized routing, observability, and control across many models and providers.

<Note>
  This integration uses a dedicated LlamaIndex package: <code>llama-index-llms-helicone</code>.
</Note>

## Install

```bash  theme={null}
pip install llama-index-llms-helicone
```

## Usage

```python  theme={null}
from llama_index.llms.helicone import Helicone
from llama_index.llms.openai_like.base import ChatMessage

llm = Helicone(
    api_key="<helicone-api-key>",
    model="gpt-4o-mini",  # works across providers
    is_chat_model=True,
)

message: ChatMessage = ChatMessage(role="user", content="Hello world!")

response = llm.chat(messages=[message])
print(str(response))
```

### Parameters

* model: OpenAI‑compatible model name routed via Helicone. See the
  <a href="https://www.helicone.ai/models" target="_blank">model registry</a>.
* api\_base (optional): Base URL for Helicone AI Gateway (defaults to the package’s `DEFAULT_API_BASE`). Can also be set via `HELICONE_API_BASE`.
* api\_key: Your Helicone API key. You can set via constructor or `HELICONE_API_KEY`.
* default\_headers (optional): Add additional headers; the `Authorization: Bearer <api_key>` header is set automatically.

## Environment Variables

```bash  theme={null}
export HELICONE_API_KEY=sk-helicone-...
# Optional override
export HELICONE_API_BASE=https://ai-gateway.helicone.ai/v1
```

## Advanced Configuration

```python  theme={null}
from llama_index.llms.helicone import Helicone

llm = Helicone(
    model="gpt-4.1-mini",
    api_key="<helicone-api-key>",
    api_base="https://ai-gateway.helicone.ai/v1",
    default_headers={
        "Helicone-Session-Id": "demo-session",
        "Helicone-User-Id": "user-123",
        "Helicone-Property-Environment": "production",
    },
    temperature=0.2,
    max_tokens=256,
)
```

<Tip>
  While you're here, why not <a href="https://github.com/helicone/helicone" target="_blank" rel="noreferrer">give us a star on GitHub</a>? It helps us a lot!
</Tip>

## Notes

* Authentication uses your Helicone API key; provider keys are not required when using the AI Gateway.
* All requests appear in the Helicone dashboard with full request/response visibility and cost tracking.
* Learn more about routing and model coverage:
  * <a href="/gateway/provider-routing">Provider routing</a>
  * <a href="https://www.helicone.ai/models" target="_blank">Model registry</a>
