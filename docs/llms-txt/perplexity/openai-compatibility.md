# OpenAI Compatibility
Source: https://docs.perplexity.ai/docs/agent-api/openai-compatibility

Use your existing OpenAI SDKs with Perplexity's Agent API. Full compatibility with minimal code changes.

## Overview

Perplexity's API is fully compatible with OpenAI's SDKs. You can use your existing OpenAI client libraries with the **Agent API** by simply changing the base URL and providing your Perplexity API key.

<Tip>
  **We recommend using the [Perplexity SDK](/docs/sdk/overview)** for the best experience with full type safety, enhanced features, and preset support. Use OpenAI SDKs if you're already integrated and need drop-in compatibility.
</Tip>

## Quick Start

Use the OpenAI SDK with Perplexity's Agent API:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="What are the latest developments in AI?"
    )

    print(response.output_text)
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v1"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "What are the latest developments in AI?"
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
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_PERPLEXITY_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript theme={null}
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

Perplexity's Agent API is fully compatible with OpenAI's Agent API interface.

### Basic Usage

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="What are the latest developments in AI?"
    )

    print(response.output_text)
    print(f"Response ID: {response.id}")
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v1"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "What are the latest developments in AI?"
    });

    console.log(response.output_text);
    console.log(`Response ID: ${response.id}`);
    ```
  </Tab>
</Tabs>

### Using Presets

Presets are pre-configured setups optimized for specific use cases. Use the `extra_body` parameter (Python) or cast the parameter (Typescript) to pass presets:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )

    # Use a preset instead of specifying model and parameters
    response = client.responses.create(
        input="What are the latest developments in AI?",
        extra_body={
            "preset": "pro-search"
        }
    )

    print(response.output_text)
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v1"
    });

    // Use a preset instead of specifying model and parameters
    const response = await client.responses.create({
      input: "What are the latest developments in AI?",
      preset: "pro-search"
    } as any);

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
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="What are the latest developments in AI?"
    )

    print(response.output_text)
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v1"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "What are the latest developments in AI?"
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

### Streaming Responses

Streaming works with the Agent API:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="Write a bedtime story about a unicorn.",
        stream=True
    )

    for event in response:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript theme={null}
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

The Agent API supports tools, including web search:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="What are the latest developments in AI?",
        tools=[
            {
                "type": "web_search",
                "filters": {
                    "search_domain_filter": ["techcrunch.com", "wired.com"]
                }
            }
        ],
        instructions="You have access to a web_search tool. Use it for current information."
    )

    print(response.output_text)
    ```
  </Tab>

  <Tab title="Typescript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v1"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "What are the latest developments in AI?",
      tools: [
        {
          type: "web_search",
          filters: {
            search_domain_filter: ["techcrunch.com", "wired.com"]
          }
        }
      ],
      instructions: "You have access to a web_search tool. Use it for current information."
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

## API Compatibility

### Standard OpenAI Parameters

These parameters work exactly the same as OpenAI's API:

**Agent API:**

* `model` - Model name (use 3rd party models like `openai/gpt-5.2`)
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
  See [Agent API Reference](/api-reference/responses-post) for complete parameter details.
</Info>

## Response Structure

### Agent API

Perplexity Agent API matches OpenAI's Agent API format:

* `output` - Structured output array containing messages with `content[].text`
* `model` - The model name used
* `usage` - Token consumption details
* `id`, `created_at`, `status` - Response metadata

## Best Practices

<Steps>
  <Step title="Use the correct base URL">
    Always use `https://api.perplexity.ai/v1` (with `/v1`) for the Agent API.

    ```python theme={null}
    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v1"  # Correct
    )
    ```
  </Step>

  <Step title="Handle errors gracefully">
    Use the OpenAI SDK's error handling:

    ```python theme={null}
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

    ```python theme={null}
    response = client.responses.create(
        model="openai/gpt-5-mini",
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

## Next Steps

<CardGroup>
  <Card title="Responses Quickstart" icon="arrow-back" href="/docs/agent-api/quickstart">
    Get started with Agent API using OpenAI SDKs.
  </Card>

  <Card title="Prompt Guide" icon="book" href="/docs/agent-api/prompt-guide">
    Learn best practices for prompting the Agent API.
  </Card>

  <Card title="API Reference" icon="code-circle" href="/docs/api-reference/responses-post">
    View complete API documentation for the Agent API endpoint.
  </Card>
</CardGroup>

## Migrating to the Perplexity SDK

Switch to the Perplexity SDK for enhanced features and cleaner syntax. With the Perplexity SDK, you can use presets directly without `extra_body` and get full type safety:

<Steps>
  <Step title="Install the Perplexity SDK">
    <Tabs>
      <Tab title="Python">
        ```bash theme={null}
        pip install perplexityai
        ```
      </Tab>

      <Tab title="Typescript">
        ```bash theme={null}
        npm install @perplexity-ai/perplexity_ai
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Update the import and client">
    <Tabs>
      <Tab title="Python">
        ```python theme={null}
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
        ```typescript theme={null}
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
        ```python theme={null}
        # Agent API - same interface
        response = client.responses.create(
            model="openai/gpt-5-mini",
            input="Hello!"
        )
        ```
      </Tab>

      <Tab title="Typescript">
        ```typescript theme={null}
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
        ```python theme={null}
        # Before (OpenAI SDK) - extra_body required
        response = client.responses.create(
            input="What are the latest developments in AI?",
            extra_body={"preset": "pro-search"}
        )

        # After (Perplexity SDK) - direct parameter
        response = client.responses.create(
            preset="pro-search",
            input="What are the latest developments in AI?"
        )
        ```
      </Tab>

      <Tab title="Typescript">
        ```typescript theme={null}
        // Before (OpenAI SDK) - type casting required
        const response = await client.responses.create({
          input: "What are the latest developments in AI?",
          preset: "pro-search"
        } as any);

        // After (Perplexity SDK) - fully typed
        const response = await client.responses.create({
          preset: "pro-search",
          input: "What are the latest developments in AI?"
        });
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>
