# Source: https://docs.together.ai/docs/evaluations-supported-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Supported models for Evaluations

# Supported Models

This page lists all supported model sources for the Evaluations API. You can use serverless models, dedicated endpoints, or external models from providers like OpenAI, Anthropic, and Google.

## Serverless models

Set `model_source = "serverless"` to use Together's serverless inference.

<Info>
  Any Together serverless model that supports [structured outputs](/docs/json-mode) can be used, including LoRA serverless variants and LoRA fine-tuned models. See [LoRA serverless](/docs/lora-inference#serverless-lora-inference) for supported models.
</Info>

**Example configuration:**

```python Python theme={null}
from together import Together

client = Together()

model_config = {
    "model": "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    "model_source": "serverless",
    "system_template": "You are a helpful assistant.",
    "input_template": "{{prompt}}",
    "max_tokens": 512,
    "temperature": 0.7,
}
```

## Dedicated models

Set `model_source = "dedicated"` to use your own dedicated endpoint.

<Info>
  A user-launched [dedicated endpoint](/docs/dedicated-inference) must be created before running evaluations. After launching an endpoint, copy-paste the endpoint ID into the `model` field.
</Info>

**Example configuration:**

```python Python theme={null}
from together import Together

client = Together()

model_config = {
    "model": "your-endpoint-id",
    "model_source": "dedicated",
    "system_template": "You are a helpful assistant.",
    "input_template": "{{prompt}}",
    "max_tokens": 512,
    "temperature": 0.7,
}
```

## External models

Set `model_source = "external"` to use models from external providers.

<Warning>
  External models require an API token from the respective provider. Set the `external_api_token` parameter with your provider's API key.
</Warning>

### Supported shortcuts

Use these shortcuts in the `model` field - the API base URL will be determined automatically:

| Provider  | Model Name            | Model String for API           |
| :-------- | :-------------------- | :----------------------------- |
| OpenAI    | GPT-5                 | `openai/gpt-5`                 |
| OpenAI    | GPT-5 Mini            | `openai/gpt-5-mini`            |
| OpenAI    | GPT-5 Nano            | `openai/gpt-5-nano`            |
| OpenAI    | GPT-5.2               | `openai/gpt-5.2`               |
| OpenAI    | GPT-5.2 Pro           | `openai/gpt-5.2-pro`           |
| OpenAI    | GPT-5.2 Chat Latest   | `openai/gpt-5.2-chat-latest`   |
| OpenAI    | GPT-4.1               | `openai/gpt-4.1`               |
| OpenAI    | GPT-4o Mini           | `openai/gpt-4o-mini`           |
| OpenAI    | GPT-4o                | `openai/gpt-4o`                |
| Anthropic | Claude Sonnet 4.5     | `anthropic/claude-sonnet-4-5`  |
| Anthropic | Claude Haiku 4.5      | `anthropic/claude-haiku-4-5`   |
| Anthropic | Claude Sonnet 4.0     | `anthropic/claude-sonnet-4-0`  |
| Anthropic | Claude Opus 4.5       | `anthropic/claude-opus-4-5`    |
| Anthropic | Claude Opus 4.1       | `anthropic/claude-opus-4-1`    |
| Anthropic | Claude Opus 4.0       | `anthropic/claude-opus-4-0`    |
| Google    | Gemini 2.0 Flash      | `google/gemini-2.0-flash`      |
| Google    | Gemini 2.0 Flash Lite | `google/gemini-2.0-flash-lite` |
| Google    | Gemini 2.5 Pro        | `google/gemini-2.5-pro`        |
| Google    | Gemini 2.5 Flash      | `google/gemini-2.5-flash`      |
| Google    | Gemini 2.5 Flash Lite | `google/gemini-2.5-flash-lite` |
| Google    | Gemini 3 Pro Preview  | `google/gemini-3-pro-preview`  |

**Example configuration with shortcut:**

```python Python theme={null}
from together import Together

client = Together()

model_config = {
    "model": "openai/gpt-5",
    "model_source": "external",
    "external_api_token": "your-openai-api-key",
    "system_template": "You are a helpful assistant.",
    "input_template": "{{prompt}}",
    "max_tokens": 512,
    "temperature": 0.7,
}
```

### Custom base URL

You can also use any OpenAI `chat/completions`-compatible API by specifying a custom `external_base_url`:

```python Python theme={null}
from together import Together

client = Together()

model_config = {
    "model": "mistral-small-latest",
    "model_source": "external",
    "external_api_token": "your-mistral-api-key",
    "external_base_url": "https://api.mistral.ai/",
    "system_template": "You are a helpful assistant.",
    "input_template": "{{prompt}}",
    "max_tokens": 512,
    "temperature": 0.7,
}
```

<Info>
  The external API must be [OpenAI `chat/completions`-compatible](https://docs.together.ai/docs/openai-api-compatibility).
</Info>


Built with [Mintlify](https://mintlify.com).