# Source: https://www.promptfoo.dev/docs/providers/openai/

# OpenAI

To use the OpenAI API, set the `OPENAI_API_KEY` environment variable to your OpenAI API key.

## Supported OpenAI Models

The OpenAI API supports a wide range of models, including:

- **gpt-5**: OpenAI's most capable vision model
- **o1**: Powerful reasoning model
- **o1-mini**: Smaller, more affordable reasoning model
- **o1-pro**: Enhanced reasoning model with more compute
- **o3-pro**: Highest-tier reasoning model
- **o3**: OpenAI's most powerful reasoning model
- **o3-mini**: Smaller, more affordable reasoning model
- **o4-mini**: Latest fast, cost-effective reasoning model
- **codex-mini-latest**: Fast reasoning model optimized for the Codex CLI
- **gpt-5-codex**: GPT-5 based coding model optimized for code generation
- **gpt-5-pro**: Premium GPT-5 model with highest reasoning capability ($15/$120 per 1M tokens)

## Using the OpenAI API

To use the OpenAI API, use the provider format `openai:responses:<model name>`:

```yaml
providers:
  - id: openai:responses:gpt-5
    config:
      modalities: [text, audio]
      voice: alloy
      instructions: You are a helpful, creative AI assistant.
      temperature: 0.7
      websocketTimeout: 60000
      max_response_output_tokens: inf
      tools: []
      tool_choice: auto
```

## Responses API

OpenAI's Responses API is the most advanced interface for generating model responses, supporting text and image inputs, function calling, and conversation state. It provides access to OpenAI's full suite of features including reasoning models like o1, o1-pro, o3, o3-pro, o3-mini, or o4-mini.

### Supported Responses Models

The Responses API supports a wide range of models, including:

- **gpt-5**: OpenAI's most capable vision model
- **o1**: Powerful reasoning model
- **o1-mini**: Smaller, more affordable reasoning model
- **o3-pro**: Highest-tier reasoning model
- **o3**: OpenAI's most powerful reasoning model
- **o3-mini**: Smaller, more affordable reasoning model
- **o4-mini**: Latest fast, cost-effective reasoning model

All deep research models:

- **Require** `web_search_preview` tool to be configured
- Support 200,000 token context window
- Support up to 100,000 output tokens
- May take 2-10 minutes to complete research tasks
- Use significant tokens for reasoning before generating output

Example configuration:

```yaml
providers:
  - id: openai:responses:o3-deep-research
    config:
      max_output_tokens: 100000
      max_tool_calls: 50
      background: true
      store: true
      tools:
        - type: web_search_preview
        - type: code_interpreter
          container:
            type: auto
        - type: mcp
          server_label: mycompany_data
          server_url: https://api.mycompany.com/mcp
          require_approval: never
```

### Advanced Configuration

Deep research models return specialized output items:

- **web_search_call**: Web search actions (search, open_page, find_in_page)
- **code_interpreter_call**: Code execution for analysis
- **message**: Final answer with inline citations and annotations

Example response structure:

```json
{
  "output": [
    {
      "type": "web_search_call",
      "action": {
        "type": "search",
        "query": "latest AI research papers 2025"
      }
    },
    {
      "type": "message",
      "content": [
        {
          "type": "output_text",
          "text": "Based on my research...",
          "annotations": [
            {
              "url": "https://arxiv.org/...",
              "title": "Paper Title",
              "start_index": 123,
              "end_index": 145
            }
          ]
        }
      ]
    }
  ]
}
```

### Best Practices

1. **Use Background Mode**: For production, always use `background: true` to handle long response times
2. **Set High Token Limits**: Use `max_output_tokens: 50000` or higher
3. **Configure Timeouts**: Set `PROMPTFOO_EVAL_TIMEOUT_MS=600000` for 10-minute timeouts
4. **Control Costs**: Use `max_tool_calls` to limit the number of searches
5. **Enhance Prompts**: Consider using a faster model to clarify/rewrite prompts before deep research

### Timeout Configuration

Deep research models automatically use appropriate timeouts:

- If `PROMPTFOO_EVAL_TIMEOUT_MS` is set, it will be used for the API call
- Otherwise, deep research models default to a 10-minute timeout (600,000ms)
- Regular models continue to use the standard 5-minute timeout

Example:

```bash
# Set a custom timeout for all evaluations
export PROMPTFOO_EVAL_TIMEOUT_MS=900000  # 15 minutes

# Or set the default API timeout (affects all providers)
export REQUEST_TIMEOUT_MS=600000  # 10 minutes
```

### Common GPT-5-pro Errors and Solutions

If you encounter errors with GPT-5-pro:

1. **Request timed out** - If GPT-5-pro needs more than the automatic 10 minutes, set `PROMPTFOO_EVAL_TIMEOUT_MS=1200000` (20 minutes)
2. **502 Bad Gateway** - Enable `PROMPTFOO_RETRY_5XX=true` to retry Cloudflare/OpenAI infrastructure timeouts
3. **getaddrinfo ENOTFOUND** - Transient DNS errors; reduce concurrency with `--max-concurrency 2`
4. **Upstream connection errors** - OpenAI load balancer issues; increase backoff with `PROMPTFOO_REQUEST_BACKOFF_MS=10000`

### GPT-5-pro Timeout Configuration

GPT-5-pro is a long-running model that often requires extended timeouts due to its advanced reasoning capabilities. Like deep research models, GPT-5-pro **automatically** receives a 10-minute timeout (600,000ms) instead of the standard 5-minute timeout.

**Automatic timeout behavior:**

- GPT-5-pro automatically gets a 10-minute timeout (600,000ms) - **no configuration needed**
- If you need longer, set `PROMPTFOO_EVAL_TIMEOUT_MS` (e.g., 900000 for 15 minutes)
- `REQUEST_TIMEOUT_MS` is **ignored** for GPT-5-pro (the automatic timeout takes precedence)

**Most users won't need any timeout configuration** - the automatic 10-minute timeout is sufficient for most GPT-5-pro requests.

**If you experience timeouts, configure this:**

```bash
# Only if you need more than the automatic 10 minutes
export PROMPTFOO_EVAL_TIMEOUT_MS=1200000   # 20 minutes

# For infrastructure reliability (recommended)
export PROMPTFOO_RETRY_5XX=true            # Retry 502 Bad Gateway errors
export PROMPTFOO_REQUEST_BACKOFF_MS=10000  # Longer retry backoff
```

### Sending Images in Prompts

The Responses API supports structured prompts with text and image inputs. Example:

```json
{
  "type": "message",
  "role": "user",
  "content": [
    {
      "type": "input_text",
      "text": "Describe what you see in this image about {{topic}}."
    },
    {
      "type": "image_url",
      "image_url": {
        "url": "{{image_url}}"
      }
    }
  ]
}
```

### Function Calling

The Responses API supports tool and function calling, similar to the Chat API:

```yaml
providers:
  - id: openai:responses:gpt-5
    config:
      tools: []
      tool_choice: auto
```

### Using with Azure

The Responses API can also be used with Azure OpenAI endpoints by configuring the `apiHost`:

```yaml
providers:
  - id: openai:responses:gpt-4.1
    config:
      apiHost: your-resource.openai.azure.com
      apiKey: {{ env.AZURE_API_KEY }}  # or set OPENAI_API_KEY env var
      temperature: 0.7
      instructions: You are a helpful assistant.
      response_format: file://./response-schema.json
```

For comprehensive Azure Responses API documentation, see the [Azure provider documentation](https://www.promptfoo.dev/docs/providers/azure/#azure-responses-api).

### Troubleshooting

#### OpenAI rate limits

There are a few things you can do if you encounter OpenAI rate limits (most commonly with GPT-4):

1. **Reduce concurrency to 1** by setting `--max-concurrency 1` in the CLI, or by setting `evaluateOptions.maxConcurrency` in the config.
2. **Set a delay between requests** by setting `--delay 3000` (3000 ms) in the CLI, or by setting `evaluateOptions.delay` in the config, or with the environment variable `PROMPTFOO_DELAY_MS` (all values are in milliseconds).
3. **Adjust the exponential backoff for failed requests** by setting the environment variable `PROMPTFOO_REQUEST_BACKOFF_MS`. This defaults to 5000 milliseconds and retries exponential up to 4 times. You can increase this value if requests are still failing, but note that this can significantly increase end-to-end test time.

#### OpenAI flakiness

To retry HTTP requests that are Internal Server errors, set the `PROMPTFOO_RETRY_5XX` environment variable to `1`.

### Agentic Providers

OpenAI offers several agentic providers for different use cases:

#### Agents SDK

Test multi-turn agentic workflows with the [OpenAI Agents provider](https://www.promptfoo.dev/docs/providers/openai-agents/). This provider supports the [@openai/agents](https://github.com/openai/openai-agents-js) SDK with tools, handoffs, and tracing.

```yaml
providers:
  - id: openai:agents:my-agent
    config:
      agent: file://./agents/support-agent.ts
      tools: file://./tools/support-tools.ts
      maxTurns: 10
```

See the [OpenAI Agents documentation](https://www.promptfoo.dev/docs/providers/openai-agents/) for full configuration options and examples.

#### Codex SDK

For agentic coding tasks with working directory access and structured JSON output, use the [OpenAI Codex SDK provider](https://www.promptfoo.dev/docs/providers/openai-codex-sdk/). This provider supports `gpt-5.1-codex` models optimized for code generation:

```yaml
providers:
  - id: openai:codex-sdk
    config:
      model: gpt-5.1-codex
      working_dir: ./src
      output_schema:
        type: object
        properties:
          code: { type: string }
          explanation: { type: string }
```

See the [OpenAI Codex SDK documentation](https://www.promptfoo.dev/docs/providers/openai-codex-sdk/) for thread management, structured output, and Git-aware operations.