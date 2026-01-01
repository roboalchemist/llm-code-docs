# Source: https://braintrust.dev/docs/integrations/sdk-integrations/llamaindex.md

# LlamaIndex

[LlamaIndex](https://docs.llamaindex.ai/) is a data framework for connecting LLMs with external data sources. Braintrust traces LlamaIndex applications using OpenTelemetry to capture queries, retrievals, and LLM interactions.

## Setup

This integration uses Braintrust's [Python SDK OpenTelemetry configuration](/integrations/sdk-integrations/opentelemetry#python-sdk-configuration).

Install LlamaIndex with OpenTelemetry support:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install "braintrust[otel]" llama-index openai python-dotenv
  ```
</CodeGroup>

Configure your environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY=your-api-key
BRAINTRUST_PARENT=project_name:llamaindex-demo
OPENAI_API_KEY=your-openai-key
```

## Trace with LlamaIndex

Configure LlamaIndex's global handler to send OpenTelemetry traces to Braintrust:

```python title="llamaindex_braintrust.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import os

import llama_index.core
from dotenv import load_dotenv
from llama_index.core.llms import ChatMessage
from llama_index.llms.openai import OpenAI

load_dotenv()

# Configure LlamaIndex to send OTel traces to Braintrust
# Note: "arize_phoenix" is LlamaIndex's OTel handler name.
# We redirect it to Braintrust by overriding the endpoint.
braintrust_api_url = os.environ.get("BRAINTRUST_API_URL", "https://api.braintrust.dev")
llama_index.core.set_global_handler("arize_phoenix", endpoint=f"{braintrust_api_url}/otel/v1/traces")

# Your LlamaIndex application code
messages = [
    ChatMessage(role="system", content="Speak like a pirate. ARRR!"),
    ChatMessage(role="user", content="What do llamas sound like?"),
]
result = OpenAI().chat(messages)
print(result)
```

<Note>
  LlamaIndex uses `"arize_phoenix"` as the OpenTelemetry handler name. By overriding the endpoint, traces are sent to Braintrust instead.
</Note>

## Resources

* [LlamaIndex documentation](https://docs.llamaindex.ai/)
* [LlamaIndex observability guide](https://docs.llamaindex.ai/en/stable/module_guides/observability/)
* [Braintrust OpenTelemetry guide](/integrations/sdk-integrations/opentelemetry)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt