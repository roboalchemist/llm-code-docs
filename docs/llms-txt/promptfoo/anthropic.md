# Anthropic

This provider supports the [Anthropic Claude](https://www.anthropic.com/claude) series of models.

> **Note:** Anthropic models can also be accessed through [Azure AI Foundry](/docs/providers/azure/#using-claude-models), [AWS Bedrock](/docs/providers/aws-bedrock/), and [Google Vertex](/docs/providers/vertex/).

## Setup

To use Anthropic, you need to set the `ANTHROPIC_API_KEY` environment variable or specify the `apiKey` in the provider configuration.

Create Anthropic API keys [here](https://console.anthropic.com/settings/keys).

Example of setting the environment variable:

```sh
export ANTHROPIC_API_KEY=your_api_key_here
```

## Models

The `anthropic` provider supports the following models via the messages API:

| Model ID | Description |
| --- | --- |
| `anthropic:messages:claude-opus-4-5-20251101` (claude-opus-4-5-latest) | Latest Claude 4.5 Opus model |
| `anthropic:messages:claude-opus-4-1-20250805` (claude-opus-4-1-latest) | Latest Claude 4.1 Opus model |
| `anthropic:messages:claude-opus-4-20250514` (claude-opus-4-latest) | Latest Claude 4 Opus model |
| `anthropic:messages:claude-sonnet-4-5-20250929` (claude-sonnet-4-5-latest) | Latest Claude 4.5 Sonnet model |
| `anthropic:messages:claude-sonnet-4-20250514` (claude-sonnet-4-latest) | Latest Claude 4 Sonnet model |
| `anthropic:messages:claude-haiku-4-5-20251001` (claude-haiku-4-5-latest) | Latest Claude 4.5 Haiku model |
| `anthropic:messages:claude-3-7-sonnet-20250219` (claude-3-7-sonnet-latest) | Latest Claude 3.7 Sonnet model |
| `anthropic:messages:claude-3-5-sonnet-20241022` (claude-3-5-sonnet-latest) | Latest Claude 3.5 Sonnet model |
| `anthropic:messages:claude-3-5-sonnet-20240620` | Previous Claude 3.5 Sonnet model |
| `anthropic:messages:claude-3-5-haiku-20241022` (claude-3-5-haiku-latest) | Latest Claude 3.5 Haiku model |
| `anthropic:messages:claude-3-opus-20240229` (claude-3-opus-latest) | Claude 3 Opus model |
| `anthropic:messages:claude-3-haiku-20240307` | Claude 3 Haiku model |

### Cross-Platform Model Availability

Claude models are available across multiple platforms. Here's how the model names map across different providers:

| Model | Anthropic API | Azure AI Foundry ([docs](/docs/providers/azure/#using-claude-models)) | AWS Bedrock ([docs](/docs/providers/aws-bedrock/)) | GCP Vertex AI ([docs](/docs/providers/vertex/)) |
| --- | --- | --- | --- | --- |
| Claude 4.5 Opus | claude-opus-4-5-20251101 (claude-opus-4-5-latest) | claude-opus-4-5-20251101 | anthropic.claude-opus-4-5-20251101-v1:0 | claude-opus-4-5@20251101 |
| Claude 4.5 Sonnet | claude-sonnet-4-5-20250929 (claude-sonnet-4-5-latest) | claude-sonnet-4-5-20250929 | anthropic.claude-sonnet-4-5-20250929-v1:0 | claude-sonnet-4-5@20250929 |
| Claude 4.5 Haiku | claude-haiku-4-5-20251001 (claude-haiku-4-5-latest) | claude-haiku-4-5-20251001 | anthropic.claude-haiku-4-5-20251001-v1:0 | claude-haiku-4-5@20251001 |
| Claude 4.1 Opus | claude-opus-4-1-20250805 | claude-opus-4-1-20250805 | anthropic.claude-opus-4-1-20250805-v1:0 | claude-opus-4-1@20250805 |
| Claude 4 Opus | claude-opus-4-20250514 (claude-opus-4-latest) | claude-opus-4-20250514 | anthropic.claude-opus-4-20250514-v1:0 | claude-opus-4@20250514 |
| Claude 4 Sonnet | claude-sonnet-4-20250514 (claude-sonnet-4-latest) | claude-sonnet-4-20250514 | anthropic.claude-sonnet-4-20250514-v1:0 | claude-sonnet-4@20250514 |
| Claude 3.7 Sonnet | claude-3-7-sonnet-20250219 (claude-3-7-sonnet-latest) | claude-3-7-sonnet-20250219 | anthropic.claude-3-7-sonnet-20250219-v1:0 | claude-3-7-sonnet@20250219 |
| Claude 3.5 Sonnet | claude-3-5-sonnet-20241022 (claude-3-5-sonnet-latest) | claude-3-5-sonnet-20241022 | anthropic.claude-3-5-sonnet-20241022-v2:0 | claude-3-5-sonnet-v2@20241022 |
| Claude 3.5 Haiku | claude-3-5-haiku-20241022 (claude-3-5-haiku-latest) | claude-3-5-haiku-20241022 | anthropic.claude-3-5-haiku-20241022-v1:0 | claude-3-5-haiku@20241022 |
| Claude 3 Opus | claude-3-opus-20240229 (claude-3-opus-latest) | claude-3-opus-20240229 | anthropic.claude-3-opus-20240229-v1:0 | claude-3-opus@20240229 |
| Claude 3 Haiku | claude-3-haiku-20240307 | claude-3-haiku-20240307 | anthropic.claude-3-haiku-20240307-v1:0 | claude-3-haiku@20240307 |

### Supported Parameters

| Config Property | Environment Variable | Description |
| --- | --- | --- |
| apiKey | ANTHROPIC_API_KEY | Your API key from Anthropic |
| apiBaseUrl | ANTHROPIC_BASE_URL | The base URL for requests to the Anthropic API |
| temperature | ANTHROPIC_TEMPERATURE | Controls the randomness of the output (default: 0) |
| max_tokens | ANTHROPIC_MAX_TOKENS | The maximum length of the generated text (default: 1024) |
| top_p | - | Controls nucleus sampling, affecting the randomness of the output |
| top_k | - | Only sample from the top K options for each subsequent token |
| tools | - | An array of tool or function definitions for the model to call |
| tool_choice | - | An object specifying the tool to call |
| output_format | - | JSON schema configuration for structured outputs |
| thinking | - | Configuration for enabling Claude's extended thinking capability |
| showThinking | - | Whether to include thinking content in the output (default: true) |
| headers | - | Additional headers to be sent with the API request |
| extra_body | - | Additional parameters to be included in the API request body |

### Prompt Template

To allow for compatibility with the OpenAI prompt template, the following format is supported:

```json
[
  {
    "role": "system",
    "content": [
      {
        "type": "text",
        "text": "{{ system_message }}",
        "cache_control": {
          "type": "ephemeral"
        }
      },
      {
        "type": "text",
        "text": "{{ context }}",
        "cache_control": {
          "type": "ephemeral"
        }
      }
    ],
    "thoughts": {
      "type": "enabled",
      "budget_tokens": 16000  # Must be ≥1024 and less than max_tokens
    }
  },
  {
    "role": "user",
    "content": "{{ question }}"
  }
]
```

Common use cases for caching:

- System messages and instructions
- Tool/function definitions
- Large context documents
- Frequently used images

See [Anthropic's Prompt Caching Guide](https://docs.anthropic.com/en/docs/prompt-caching) for more details on requirements, pricing, and best practices.

### Citations

Claude can provide detailed citations when answering questions about documents. Basic example:

```yaml
providers:
  - id: anthropic:messages:claude-sonnet-4-5-20250929
    config:
      tools:
        - type: web_search_20250305
          name: web_search
          max_uses: 3
```

See [Anthropic's Citations Guide](https://docs.anthropic.com/en/docs/build-with-claude/citations) for more details.

### Extended Thinking

Claude supports an extended thinking capability that allows you to see the model's internal reasoning process before it provides the final answer. This can be configured using the `thinking` parameter:

```yaml
providers:
  - id: anthropic:messages:claude-sonnet-4-5-20250929
    config:
      max_tokens: 20000
      thinking:
        type: enabled
        budget_tokens: 16000  # Must be ≥1024 and less than max_tokens
```

The thinking configuration has two possible values:

1. **Enabled thinking:**

```yaml
thinking:
  type: enabled
  budget_tokens: number  # Must be ≥1024 and less than max_tokens
```

2. **Disabled thinking:**

```yaml
thinking:
  type: disabled
```

When thinking is enabled:

- Responses will include `thinking` content blocks showing Claude's reasoning process
- Requires a minimum budget of 1,024 tokens
- The budget_tokens value must be less than the max_tokens parameter
- The tokens used for thinking count towards your max_tokens limit
- A specialized 28 or 29 token system prompt is automatically included
- Previous turn thinking blocks are ignored and not counted as input tokens
- Thinking is not compatible with temperature, top_p, or top_k modifications

Example response with thinking enabled:

```json
{
  "content": [
    {
      "type": "thinking",
      "thinking": "Let me analyze this step by step...",
      "signature": "WaUjzkypQ2mUEVM36O2TxuC06KN8xyfbJwyem2dw3URve/op91XWHOEBLLqIOMfFG/UvLEczmEsUjavL...."
    },
    {
      "type": "text",
      "text": "Based on my analysis, here is the answer..."
    }
  ]
}
```

### Controlling Thinking Output

By default, thinking content is included in the response output. You can control this behavior using the `showThinking` parameter:

```yaml
providers:
  - id: anthropic:messages:claude-sonnet-4-5-20250929
    config:
      thinking:
        type: enabled
        budget_tokens: 16000
      showThinking: false  # Exclude thinking content from the output
```

When `showThinking` is set to `false`, the thinking content will be excluded from the output, and only the final response will be returned. This is useful when you want to use thinking for better reasoning but don't want to expose the thinking process to end users.

### Redacted Thinking

Sometimes Claude's internal reasoning may be flagged by safety systems. When this occurs, the thinking block will be encrypted and returned as a `redacted_thinking` block:

```json
{
  "content": [
    {
      "type": "redacted_thinking",
      "data": "EmwKAhgBEgy3va3pzix/LafPsn4aDFIT2Xlxh0L5L8rLVyIwxtE3rAFBa8cr3qpP..."
    },
    {
      "type": "text",
      "text": "Based on my analysis..."
    }
  ]
}
```

Redacted thinking blocks are automatically decrypted when passed back to the API, allowing Claude to maintain context without compromising safety guardrails.

### Extended Output with Thinking

Claude 4 models provide enhanced output capabilities and extended thinking support:

```yaml
providers:
  - id: anthropic:messages:claude-sonnet-4-5-20250929
    config:
      max_tokens: 64000  # Claude 4 Sonnet supports up to 64K output tokens
      thinking:
        type: enabled
        budget_tokens: 32000
```

Note: The `output-128k-2025-02-19` beta feature is specific to Claude 3.7 Sonnet and is not needed for Claude 4 models, which have improved output capabilities built-in.

When using extended output:

- Streaming is required when max_tokens is greater than 21,333
- For thinking budgets above 32K, batch processing is recommended
- The model may not use the entire allocated thinking budget

See [Anthropic's Extended Thinking Guide](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) for more details on requirements and best practices.

### Structured Outputs

Structured outputs constrain Claude's responses to a JSON schema. Available for Claude Sonnet 4.5 and Claude Opus 4.1.

#### JSON Outputs

Add `output_format` to get structured responses:

```yaml
providers:
  - id: anthropic:messages:claude-sonnet-4-5-20250929
    config:
      output_format:
        type: json_schema
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
          required:
            - name
            - email
          additionalProperties: false
```

Load schemas from files with `schema: file://path/to/schema.json`.

#### Strict Tool Use

Add `strict: true` to tool definitions for schema-validated parameters:

```yaml
providers:
  - id: anthropic:messages:claude-sonnet-4-5-20250929
    config:
      tools:
        - name: get_weather
          strict: true
          input_schema:
            type: object
            properties:
              location:
                type: string
            required:
              - location
            additionalProperties: false
```

#### Limitations

- **Supported:** object, array, string, integer, number, boolean, null, `enum`, `required`, `additionalProperties: false`
- **Not supported:** recursive schemas, `minimum`/`maximum`, `minLength`/`maxLength`
- **Incompatible with:** citations, message prefilling

See [Anthropic's guide](https://docs.anthropic.com/en/docs/build-with-claude/structured-outputs) and the [structured outputs example](https://github.com/promptfoo/promptfoo/tree/main/examples/anthropic/structured-outputs).

## Model-Graded Tests

[Model-graded assertions](/docs/configuration/expected-outputs/model-graded/) such as `factuality` or `llm-rubric` will automatically use Anthropic as the grading provider if `ANTHROPIC_API_KEY` is set and `OPENAI_API_KEY` is not set.

If both API keys are present, OpenAI will be used by default. You can explicitly override the grading provider in your configuration.

Because of how model-graded evals are implemented, **the model must support chat-formatted prompts** (except for embedding or classification models).

You can override the grading provider in several ways:

1. **For all test cases using `defaultTest`:**

```yaml
defaultTest:
  options:
    provider: anthropic:messages:claude-sonnet-4-5-20250929
```

2. **For individual assertions:**

```yaml
assert:
  - type: llm-rubric
    value: Do not mention that you are an AI or chat assistant
    provider:
      id: anthropic:messages:claude-sonnet-4-5-20250929
      config:
        temperature: 0.0
```

3. **For specific tests:**

```yaml
tests:
  - vars:
      question: What is the capital of France?
    options:
      provider:
        id: anthropic:messages:claude-sonnet-4-5-20250929
    assert:
      - type: llm-rubric
        value: Answer should mention Paris
```

### Additional Capabilities

- **Caching**: Promptfoo caches previous LLM requests by default.
- **Token Usage Tracking**: Provides detailed information on the number of tokens used in each request, aiding in usage monitoring and optimization.
- **Cost Calculation**: Calculates the cost of each request based on the number of tokens generated and the specific model used.

## See Also

### Examples

We provide several example implementations demonstrating Claude's capabilities:

#### Core Features

- [Tool Use Example](https://github.com/promptfoo/promptfoo/tree/main/examples/tool-use) - Shows how to use Claude's tool calling capabilities
- [Structured Outputs Example](https://github.com/promptfoo/promptfoo/tree/main/examples/anthropic/structured-outputs) - Demonstrates JSON outputs and strict tool use for guaranteed schema compliance
- [Vision Example](https://github.com/promptfoo/promptfoo/tree/main/examples/claude-vision) - Demonstrates using Claude's vision capabilities

#### Model Comparisons & Evaluations

- [Claude vs GPT](https://github.com/promptfoo/promptfoo/tree/main/examples/claude-vs-gpt) - Compares Claude with GPT-4 on various tasks
- [Claude vs GPT Image Analysis](https://github.com/promptfoo/promptfoo/tree/main/examples/claude-vs-gpt-image) - Compares Claude's and GPT's image analysis capabilities

#### Cloud Platform Integrations

- [Azure AI Foundry](https://github.com/promptfoo/promptfoo/tree/main/examples/azure/claude) - Using Claude through Azure AI Foundry
- [AWS Bedrock](https://github.com/promptfoo/promptfoo/tree/main/examples/amazon-bedrock) - Using Claude through AWS Bedrock
- [Google Vertex AI](https://github.com/promptfoo/promptfoo/tree/main/examples/google-vertex) - Using Claude through Google Vertex AI

#### Agentic Evaluations

- [Claude Agent SDK](/docs/providers/claude-agent-sdk/) - For agentic evals with file access, tool use, and MCP servers

For more examples and general usage patterns, visit our [examples directory](https://github.com/promptfoo/promptfoo/tree/main/examples) on GitHub.