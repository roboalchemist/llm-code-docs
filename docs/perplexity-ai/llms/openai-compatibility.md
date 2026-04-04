# Source: https://docs.perplexity.ai/docs/sonar/openai-compatibility.md

# Source: https://docs.perplexity.ai/docs/agent-api/openai-compatibility.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Compatibility

> Use your existing OpenAI SDKs with Perplexity's Agent API. Full compatibility with minimal code changes.

## Overview

Perplexity's Agent API is fully compatible with OpenAI's Responses API interface. You can use your existing OpenAI client libraries by simply changing the base URL and providing your Perplexity API key.

<Info>
  **Endpoint Note:** Perplexity's canonical Agent API endpoint is `POST /v1/agent`. For OpenAI SDK compatibility, `POST /v1/responses` is also accepted as an alias — the OpenAI SDK automatically routes `client.responses.create()` to `/v1/responses`, which Perplexity handles seamlessly. No SDK changes are needed beyond setting the base URL.
</Info>

<Tip>
  **We recommend using the [Perplexity SDK](/docs/sdk/overview)** for the best experience with full type safety, enhanced features, and preset support. Use OpenAI SDKs if you're already integrated and need drop-in compatibility.
</Tip>

## Quick Start

Use the OpenAI SDK with Perplexity's Agent API:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )

    response = client.responses.create(
        model="openai/gpt-5.4",
        input="Explain the key differences between REST and GraphQL APIs"
    )

    print(response.output_text)
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v1"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "Explain the key differences between REST and GraphQL APIs"
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

## Configuration

### Setting Up the OpenAI SDK

Configure OpenAI SDKs to work with Perplexity by setting the `base_url` to `https://api.perplexity.ai/v1`:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_PERPLEXITY_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_PERPLEXITY_API_KEY",
      baseURL: "https://api.perplexity.ai/v1"
    });
    ```
  </Tab>
</Tabs>

<Info>
  **Important**: Use `base_url="https://api.perplexity.ai/v1"` (with `/v1`) for the Agent API.
</Info>

## Agent API

Perplexity's Agent API follows OpenAI's Responses API request/response format. The OpenAI SDK's `client.responses.create()` method works out of the box — the SDK sends requests to `/v1/responses`, which Perplexity accepts alongside the canonical `/v1/agent` endpoint.

### Basic Usage

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )

    response = client.responses.create(
        model="openai/gpt-5.4",
        input="Explain the key differences between REST and GraphQL APIs"
    )

    print(response.output_text)
    print(f"Response ID: {response.id}")
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v1"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "Explain the key differences between REST and GraphQL APIs"
    });

    console.log(response.output_text);
    console.log(`Response ID: ${response.id}`);
    ```
  </Tab>
</Tabs>

### Using Presets

Presets are pre-configured setups optimized for specific use cases. Use `extra_body` to pass presets via the OpenAI SDK:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )

    # Pass preset via extra_body
    response = client.responses.create(
        input="What are the key differences between the latest iPhone and Samsung Galaxy flagship phones?",
        extra_body={
            "preset": "pro-search"
        }
    )

    print(response.output_text)
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v1"
    });

    // Use type casting (as any) to pass preset via extra_body
    const response = await (client.responses.create as any)({
      input: "What are the key differences between the latest iPhone and Samsung Galaxy flagship phones?",
      extra_body: {
        "preset": "pro-search"
      }
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

<Info>
  See [Agent API Presets](/docs/agent-api/presets) for available presets and their configurations.
</Info>

### Using Third-Party Models

You can also specify third-party models directly instead of using presets:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )

    response = client.responses.create(
        model="openai/gpt-5.4",
        input="Explain the key differences between REST and GraphQL APIs"
    )

    print(response.output_text)
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v1"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "Explain the key differences between REST and GraphQL APIs"
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

### Streaming Responses

Streaming works with the Agent API:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )

    response = client.responses.create(
        model="openai/gpt-5.4",
        input="Write a bedtime story about a unicorn.",
        stream=True
    )

    for event in response:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v1"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "Write a bedtime story about a unicorn.",
      stream: true
    });

    for await (const event of response) {
      if (event.type === "response.output_text.delta") {
        process.stdout.write(event.delta);
      }
    }
    ```
  </Tab>
</Tabs>

### Using Tools

The Agent API supports built-in tools, including web search. Use `extra_body` to pass tools via the OpenAI SDK:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )

    # Pass tools via extra_body
    response = client.responses.create(
        model="openai/gpt-5.4",
        input="Which companies announced the largest AI acquisitions this quarter?",
        extra_body={
            "tools": [
                {
                    "type": "web_search",
                    "filters": {
                        "search_domain_filter": ["techcrunch.com", "crunchbase.com"]
                    }
                }
            ]
        }
    )

    print(response.output_text)
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v1"
    });

    // Use type casting (as any) to pass tools via extra_body
    const response = await (client.responses.create as any)({
      model: "openai/gpt-5-mini",
      input: "Which companies announced the largest AI acquisitions this quarter?",
      extra_body: {
        "tools": [
          {
            "type": "web_search",
            "filters": {
              "search_domain_filter": ["techcrunch.com", "crunchbase.com"]
            }
          }
        ]
      }
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

## API Compatibility

### Standard OpenAI Parameters

These parameters work exactly the same as OpenAI's API:

**Agent API:**

* `model` - Model name (use 3rd party models like `openai/gpt-5.4`)
* `input` - Input text or message array
* `instructions` - System instructions
* `max_output_tokens` - Maximum tokens in response
* `stream` - Enable streaming responses
* `tools` - Array of tools including `web_search`

### Perplexity-Specific Parameters

**Agent API:**

* `preset` - Preset name (use Perplexity presets like `pro-search`)
* `tools[].filters` - Search filters within web\_search tool
* `tools[].user_location` - User location for localized results

<Info>
  See [Agent API Reference](/api-reference/agent-post) for complete parameter details.
</Info>

## Endpoint Mapping

| Method                      | Perplexity Endpoint | OpenAI Equivalent    | Notes                                               |
| --------------------------- | ------------------- | -------------------- | --------------------------------------------------- |
| `client.responses.create()` | `POST /v1/agent`    | `POST /v1/responses` | Both paths accepted by Perplexity for compatibility |

<Info>
  When using the OpenAI SDK, `client.responses.create()` sends requests to `/v1/responses`. Perplexity accepts this path as an alias for `/v1/agent`, so no SDK configuration changes are needed beyond `base_url`.
</Info>

## Response Structure

### Agent API

Perplexity's Agent API matches OpenAI's Responses API response format:

* `output` - Structured output array containing messages with `content[].text`
* `model` - The model name used
* `usage` - Token consumption details
* `id`, `created_at`, `status` - Response metadata

## Best Practices

<Steps>
  <Step title="Use the correct base URL">
    Always use `https://api.perplexity.ai/v1` (with `/v1`) for the Agent API.

    ```python  theme={null}
    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"  # Correct
    )
    ```
  </Step>

  <Step title="Handle errors gracefully">
    Use the OpenAI SDK's error handling:

    ```python  theme={null}
    from openai import OpenAI, APIError, RateLimitError

    try:
        response = client.responses.create(...)
    except RateLimitError:
        print("Rate limit exceeded, please retry later")
    except APIError as e:
        print(f"API error: {e.message}")
    ```
  </Step>

  <Step title="Use streaming for better UX">
    Stream responses for real-time user experience:

    ```python  theme={null}
    response = client.responses.create(
        model="openai/gpt-5.4",
        input="Long query...",
        stream=True
    )

    for event in response:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
    ```
  </Step>
</Steps>

## Recommended: Perplexity SDK

We recommend using Perplexity's native SDKs for the best developer experience:

* **Cleaner preset syntax** - Use `preset="pro-search"` directly instead of `extra_body={"preset": "pro-search"}`
* **Type safety** - Full Typescript/Python type definitions for all parameters
* **Enhanced features** - Direct access to all Perplexity-specific features
* **Better error messages** - Perplexity-specific error handling
* **Simpler setup** - No need to configure base URLs

See the [Perplexity SDK Guide](/docs/sdk/overview) for details.

## Migrating to the Perplexity SDK

Switch to the Perplexity SDK for enhanced features and cleaner syntax. With the Perplexity SDK, you can use presets directly without `extra_body` and get full type safety:

<Steps>
  <Step title="Install the Perplexity SDK">
    <Tabs>
      <Tab title="Python">
        ```bash  theme={null}
        pip install perplexityai
        ```
      </Tab>

      <Tab title="Typescript">
        ```bash  theme={null}
        npm install @perplexity-ai/perplexity_ai
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Update the import and client">
    <Tabs>
      <Tab title="Python">
        ```python  theme={null}
        # Before (OpenAI SDK)
        from openai import OpenAI
        client = OpenAI(
            api_key="pplx-...",
            base_url="https://api.perplexity.ai/v1"
        )

        # After (Perplexity SDK)
        from perplexity import Perplexity
        client = Perplexity(api_key="pplx-...")
        # Or just: client = Perplexity() if PERPLEXITY_API_KEY env var is set
        ```
      </Tab>

      <Tab title="Typescript">
        ```typescript  theme={null}
        // Before (OpenAI SDK)
        import OpenAI from 'openai';
        const client = new OpenAI({
          apiKey: "pplx-...",
          baseURL: "https://api.perplexity.ai/v1"
        });

        // After (Perplexity SDK)
        import Perplexity from '@perplexity-ai/perplexity_ai';
        const client = new Perplexity({ apiKey: "pplx-..." });
        // Or just: const client = new Perplexity() if PERPLEXITY_API_KEY env var is set
        ```
      </Tab>
    </Tabs>

    <Info>
      **No base URL needed** - The Perplexity SDK automatically uses the correct endpoint.
    </Info>
  </Step>

  <Step title="Update the API calls">
    The API calls are very similar:

    <Tabs>
      <Tab title="Python">
        ```python  theme={null}
        # Agent API - same interface
        response = client.responses.create(
            model="openai/gpt-5.4",
            input="Hello!"
        )
        ```
      </Tab>

      <Tab title="Typescript">
        ```typescript  theme={null}
        // Agent API - same interface
        const response = await client.responses.create({
          model: "openai/gpt-5-mini",
          input: "Hello!"
        });
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Use presets with cleaner syntax">
    The Perplexity SDK supports presets with cleaner syntax compared to OpenAI SDK:

    <Tabs>
      <Tab title="Python">
        ```python  theme={null}
        # Before (OpenAI SDK) - extra_body required
        response = client.responses.create(
            input="What were the biggest tech IPOs this year and how did they perform on day one?",
            extra_body={"preset": "pro-search"}
        )

        # After (Perplexity SDK) - direct parameter
        response = client.responses.create(
            preset="pro-search",
            input="What were the biggest tech IPOs this year and how did they perform on day one?"
        )
        ```
      </Tab>

      <Tab title="Typescript">
        ```typescript  theme={null}
        // Before (OpenAI SDK) - type casting required
        const response = await client.responses.create({
          input: "What were the biggest tech IPOs this year and how did they perform on day one?",
          preset: "pro-search"
        } as any);

        // After (Perplexity SDK) - fully typed
        const response = await client.responses.create({
          preset: "pro-search",
          input: "What were the biggest tech IPOs this year and how did they perform on day one?"
        });
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

## Next Steps

<CardGroup cols={2}>
  <Card title="Agent API Quickstart" icon="rocket" href="/docs/agent-api/quickstart">
    Get started with Agent API using OpenAI SDKs.
  </Card>

  <Card title="Models" icon="brain" href="/docs/agent-api/models">
    Explore direct model selection and third-party models.
  </Card>

  <Card title="API Reference" icon="code-circle" href="/api-reference/agent-post">
    View complete endpoint documentation.
  </Card>

  <Card title="Output Control" icon="indent-decrease" href="/docs/agent-api/output-control">
    Configure streaming responses and structured outputs with JSON schema.
  </Card>

  <Card title="Model Fallback" icon="square-rounded-arrow-down" href="/docs/agent-api/model-fallback">
    Specify multiple models for automatic failover and higher availability.
  </Card>

  <Card title="Filters" icon="filter" href="/docs/agent-api/filters">
    Apply filters to web search results.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).