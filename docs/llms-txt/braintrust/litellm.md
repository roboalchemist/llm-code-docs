# Source: https://braintrust.dev/docs/integrations/sdk-integrations/litellm.md

# LiteLLM

[LiteLLM](https://www.litellm.ai/) is a unified interface for calling 100+ LLM APIs using the OpenAI format. Braintrust automatically traces LiteLLM calls across all providers including OpenAI, Azure, Anthropic, Cohere, Replicate, and more.

## Setup

Install LiteLLM alongside the Braintrust SDK:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  // uv
  uv add braintrust litellm
  // pip
  pip install braintrust litellm
  ```
</CodeGroup>

## Trace with LiteLLM

Braintrust provides a patch function that automatically instruments LiteLLM to capture all model interactions.

Call `patch_litellm()` before importing LiteLLM to enable automatic tracing:

```python title="trace-litellm.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust.wrappers.litellm import patch_litellm

patch_litellm()

import litellm
from braintrust import init_logger

# Initialize Braintrust
logger = init_logger(project="litellm-example")

# Use LiteLLM as normal - all calls are automatically traced
response = litellm.completion(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is the capital of France?"}]
)
```

This will automatically send all LiteLLM interactions to Braintrust, including:

* Model calls across different providers
* Request and response data
* Token usage and costs
* Latency metrics
* Error tracking

## Resources

* [LiteLLM documentation](https://docs.litellm.ai/)
* [DSPy integration](/integrations/sdk-integrations/dspy) - Combines LiteLLM tracing with DSPy-specific callbacks
* [Supported providers](https://docs.litellm.ai/docs/providers)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt