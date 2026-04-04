# Source: https://docs.perplexity.ai/docs/sonar/models.md

# Source: https://docs.perplexity.ai/docs/agent-api/models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Models

> Explore available presets and third-party models for the Agent API, including Perplexity presets and third-party model support.

## Available Models

The Agent API supports direct access to models from multiple providers. All models are accessed directly from first-party providers with transparent token-based pricing.

Pricing rates are updated monthly and **reflect direct first-party provider pricing with no markup**. All charges are based on actual token consumption, and every API response includes exact token counts so you know your costs per request.

<Warning>
  Not all third-party models support all features (e.g., reasoning, tools). Check model documentation for specific capabilities.
</Warning>

| Model                               | Input Price                                                                | Output Price                                                                 | Cache Read Price     | Provider Documentation                                                                  |
| ----------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------- |
| **Perplexity Models**               |                                                                            |                                                                              |                      |                                                                                         |
| `perplexity/sonar`                  | \$0.25 / 1M tokens                                                         | \$2.50 / 1M tokens                                                           | \$0.0625 / 1M tokens | [Sonar](https://docs.perplexity.ai/docs/sonar/models/sonar)                             |
| **Anthropic Models**                |                                                                            |                                                                              |                      |                                                                                         |
| `anthropic/claude-opus-4-6`         | \$5 / 1M tokens                                                            | \$25 / 1M tokens                                                             | \$0.50 / 1M tokens   | [Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)                       |
| `anthropic/claude-opus-4-5`         | \$5 / 1M tokens                                                            | \$25 / 1M tokens                                                             | \$0.50 / 1M tokens   | [Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5)                       |
| `anthropic/claude-sonnet-4-6`       | \$3 / 1M tokens                                                            | \$15 / 1M tokens                                                             | \$0.30 / 1M tokens   | [Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6)                   |
| `anthropic/claude-sonnet-4-5`       | \$3 / 1M tokens                                                            | \$15 / 1M tokens                                                             | \$0.30 / 1M tokens   | [Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5)                   |
| `anthropic/claude-haiku-4-5`        | \$1 / 1M tokens                                                            | \$5 / 1M tokens                                                              | \$0.10 / 1M tokens   | [Claude Haiku 4.5](https://www.anthropic.com/news/claude-haiku-4-5)                     |
| **OpenAI Models**                   |                                                                            |                                                                              |                      |                                                                                         |
| `openai/gpt-5.4`                    | \$2.50 / 1M tokens                                                         | \$15.00 / 1M tokens                                                          | \$0.25 / 1M tokens   | [GPT-5.4](https://platform.openai.com/docs/models/gpt-5.4)                              |
| `openai/gpt-5.2`                    | \$1.75 / 1M tokens                                                         | \$14 / 1M tokens                                                             | \$0.175 / 1M tokens  | [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2)                              |
| `openai/gpt-5.1`                    | \$1.25 / 1M tokens                                                         | \$10 / 1M tokens                                                             | \$0.125 / 1M tokens  | [GPT-5.1](https://platform.openai.com/docs/models/gpt-5.1)                              |
| `openai/gpt-5-mini`                 | \$0.25 / 1M tokens                                                         | \$2 / 1M tokens                                                              | \$0.025 / 1M tokens  | [GPT-5 Mini](https://platform.openai.com/docs/models/gpt-5-mini)                        |
| **Google Models**                   |                                                                            |                                                                              |                      |                                                                                         |
| `google/gemini-3.1-pro-preview`     | \$2.00 / 1M tokens (≤200k context)<br />\$4.00 / 1M tokens (>200k context) | \$12.00 / 1M tokens (≤200k context)<br />\$18.00 / 1M tokens (>200k context) | 90% discount         | [Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models#gemini-3.1-pro-preview)   |
| `google/gemini-3-flash-preview`     | \$0.50 / 1M tokens                                                         | \$3.00 / 1M tokens                                                           | 90% discount         | [Gemini 3.0 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-3-flash-preview) |
| `google/gemini-2.5-pro`             | \$1.25 / 1M tokens (≤200k context)<br />\$2.50 / 1M tokens (>200k context) | \$10.00 / 1M tokens (≤200k context)<br />\$15.00 / 1M tokens (>200k context) | 90% discount         | [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-pro_1)         |
| `google/gemini-2.5-flash`           | \$0.30 / 1M tokens                                                         | \$2.50 / 1M tokens                                                           | 90% discount         | [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash_1)     |
| **NVIDIA Models**                   |                                                                            |                                                                              |                      |                                                                                         |
| `nvidia/nemotron-3-super-120b-a12b` | \$0.25 / 1M tokens                                                         | \$2.50 / 1M tokens                                                           | —                    | [Nemotron 3 Super 120B](https://research.nvidia.com/labs/nemotron/Nemotron-3/)          |
| **xAI Models**                      |                                                                            |                                                                              |                      |                                                                                         |
| `xai/grok-4-1-fast-non-reasoning`   | \$0.20 / 1M tokens                                                         | \$0.50 / 1M tokens                                                           | \$0.05 / 1M tokens   | [Grok 4.1](https://docs.x.ai/docs/models/grok-4-1-fast-non-reasoning)                   |

<Tip>
  **See Your Costs in Real-Time:** Every response includes a `usage` field with exact input tokens, output tokens, and cache read tokens. Calculate your cost instantly using the pricing table above.

  ```json  theme={null}
  {
    "usage": {
      "input_tokens": 150,
      "output_tokens": 320,
      "total_tokens": 470
    }
  }
  ```
</Tip>

## Using a Model

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="nvidia/nemotron-3-super-120b-a12b",
      input="Explain the difference between supervised and unsupervised learning in machine learning.",
      max_output_tokens=300,
  )

  print(f"Response ID: {response.id}")
  print(response.output_text)
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "nvidia/nemotron-3-super-120b-a12b",
      input: "Explain the difference between supervised and unsupervised learning in machine learning.",
      max_output_tokens: 300,
  });

  console.log(`Response ID: ${response.id}`);
  console.log(response.output_text);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/agent \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "nvidia/nemotron-3-super-120b-a12b",
      "input": "Explain the difference between supervised and unsupervised learning in machine learning.",
      "max_output_tokens": 300
    }' | jq
  ```
</CodeGroup>

## Configuration Options

The Agent API supports two ways to configure models:

1. [**Presets**](/docs/agent-api/presets) — Pre-configured model setups optimized for specific use cases
2. [**Models**](/docs/agent-api/models) — Direct model selection, including third-party models

## Model Fallback

For high-availability applications, you can specify multiple models in a fallback chain. When one model fails or is unavailable, the API automatically tries the next model in the chain.

<Card title="Model Fallback Chain" icon="square-rounded-arrow-down" href="/docs/agent-api/model-fallback">
  Learn how to use model fallback chains to ensure high availability and reliability by automatically trying multiple models when one fails.
</Card>

<Info>
  **Example:**

  ```python  theme={null}
  response = client.responses.create(
      models=["nvidia/nemotron-3-super-120b-a12b", "openai/gpt-5.4", "google/gemini-3-flash-preview"],
      input="Your question here"
  )
  ```

  For detailed examples, pricing information, and best practices, see the [Model Fallback documentation](/docs/agent-api/model-fallback).
</Info>

## Next Steps

<CardGroup cols={2}>
  <Card title="Model Fallback" icon="square-rounded-arrow-down" href="/docs/agent-api/model-fallback">
    Learn how to use model fallback chains for higher availability.
  </Card>

  <Card title="Presets" icon="settings" href="/docs/agent-api/presets">
    Explore available presets and their configurations.
  </Card>

  <Card title="Agent API Quickstart" icon="rocket" href="/docs/agent-api/quickstart">
    Get started with your first Agent API call.
  </Card>

  <Card title="API Reference" icon="code-circle" href="/api-reference/agent-post">
    View complete endpoint documentation.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).