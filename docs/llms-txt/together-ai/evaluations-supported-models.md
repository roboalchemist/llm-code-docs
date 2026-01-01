# Source: https://docs.together.ai/docs/evaluations-supported-models.md

> Supported models for Evaluations

# Supported Models

### Serverless models (`model_source = "serverless"`)

Any Together serverless model that supports [structured outputs](/docs/json-mode), including LoRA serverless variants and LoRA fine-tuned models. See [LoRA serverless](docs/lora-inference#serverless-lora-inference) for supported models.

### Dedicated models (`model_source = "dedicated"`)

A user-launched [dedicated endpoint](/docs/dedicated-inference) (must be created before running evaluations). After launching an endpoint, you can just copy-paste the endpoint ID into the `model` field.

### External models shortcuts (`model_source = "external"`)

* `openai/gpt-5`
* `openai/gpt-5-mini`
* `openai/gpt-5-nano`
* `openai/gpt-5.2`
* `openai/gpt-5.2-pro`
* `openai/gpt-5.2-chat-latest`
* `openai/gpt-4.1`
* `openai/gpt-4o-mini`
* `openai/gpt-4o`
* `anthropic/claude-sonnet-4-5`
* `anthropic/claude-haiku-4-5`
* `anthropic/claude-sonnet-4-0`
* `anthropic/claude-opus-4-5`
* `anthropic/claude-opus-4-1`
* `anthropic/claude-opus-4-0`
* `google/gemini-2.0-flash`
* `google/gemini-2.0-flash-lite`
* `google/gemini-2.5-pro`
* `google/gemini-2.5-flash`
* `google/gemini-2.5-flash-lite`
* `google/gemini-3-pro-preview`

```yaml  theme={null}
allowed_models:
  - openai/gpt-5
  - openai/gpt-5-mini
  - openai/gpt-5-nano
  - openai/gpt-5.2
  - openai/gpt-5.2-pro
  - openai/gpt-5.2-chat-latest
  - openai/gpt-4
  - openai/gpt-4.1
  - openai/gpt-4o-mini
  - openai/gpt-4o
  - anthropic/claude-sonnet-4-5
  - anthropic/claude-haiku-4-5
  - anthropic/claude-sonnet-4-0
  - anthropic/claude-opus-4-5
  - anthropic/claude-opus-4-1
  - anthropic/claude-opus-4-0
  - google/gemini-2.0-flash
  - google/gemini-2.0-flash-lite
  - google/gemini-2.5-pro
  - google/gemini-2.5-flash
  - google/gemini-2.5-flash-lite
  - google/gemini-3-pro-preview
```

### External models with custom base URL (`model_source = "external"`)

You can specify a custom base URL for the external API (e.g., `https://api.openai.com`). This API must be [OpenAI `chat/completions`-compatible](https://docs.together.ai/docs/openai-api-compatibility).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt