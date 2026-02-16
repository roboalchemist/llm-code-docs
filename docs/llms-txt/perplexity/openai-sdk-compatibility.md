# OpenAI SDK Compatibility

Source: https://docs.perplexity.ai/docs/sonar/openai-compatibility

Use OpenAI SDKs with the Sonar API by changing the base URL and API key

## Overview

Perplexity's Sonar API is fully compatible with OpenAI's Chat Completions format. You can use your existing OpenAI client libraries with the Sonar API by simply changing the base URL and providing your Perplexity API key.

<Tip>
  **We recommend using the [Perplexity SDK](/docs/sdk/overview)** for the best experience with full type safety, enhanced features, and preset support. Use OpenAI SDKs if you're already integrated and need drop-in compatibility.
</Tip>

## Quick Start

Use the OpenAI SDK with Perplexity's Sonar API:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai"
    )

    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "What are the latest developments in AI?"}
        ]
    )

    print(completion.choices[0].message.content)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai"
    });

    const completion = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
        { role: "user", content: "What are the latest developments in AI?" }
      ]
    });

    console.log(completion.choices[0].message.content);
    ```
  </Tab>
</Tabs>

## Configuration

### Setting Up the OpenAI SDK

Configure OpenAI SDKs to work with Perplexity by setting the `base_url` to `https://api.perplexity.ai`:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_PERPLEXITY_API_KEY",
        base_url="https://api.perplexity.ai"
    )
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_PERPLEXITY_API_KEY",
      baseURL: "https://api.perplexity.ai"
    });
    ```
  </Tab>
</Tabs>

<Info>
  **Important**: Use `base_url="https://api.perplexity.ai"` for the Sonar API.
</Info>

## Basic Usage

Perplexity's Sonar API is fully compatible with OpenAI's Chat Completions interface.

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai"
    )

    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "What are the latest developments in AI?"}
        ]
    )

    print(completion.choices[0].message.content)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai"
    });

    const completion = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
        { role: "user", content: "What are the latest developments in AI?" }
      ]
    });

    console.log(completion.choices[0].message.content);
    ```
  </Tab>
</Tabs>

## Streaming

Streaming works exactly like OpenAI's API:

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai"
    )

    stream = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "What are the latest developments in AI?"}
        ],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai"
    });

    const stream = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
        { role: "user", content: "What are the latest developments in AI?" }
      ],
      stream: true
    });

    for await (const chunk of stream) {
      if (chunk.choices[0]?.delta?.content) {
        process.stdout.write(chunk.choices[0].delta.content);
      }
    }
    ```
  </Tab>
</Tabs>

## Perplexity-Specific Parameters

Add Perplexity-specific search parameters using `extra_body` (Python) or direct parameters (TypeScript):

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai"
    )

    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "Latest climate research findings"}
        ],
        extra_body={
            "search_domain_filter": ["nature.com", "science.org"],
            "search_recency_filter": "month"
        }
    )

    print(completion.choices[0].message.content)
    print(f"Sources: {len(completion.search_results)} articles found")
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai"
    });

    const completion = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
        { role: "user", content: "Latest climate research findings" }
      ],
      search_domain_filter: ["nature.com", "science.org"],
      search_recency_filter: "month"
    } as any);

    console.log(completion.choices[0].message.content);
    console.log(`Sources: ${completion.search_results.length} articles found`);
    ```
  </Tab>
</Tabs>

## API Compatibility

### Standard OpenAI Parameters

These parameters work exactly the same as OpenAI's API:

* `model` - Model name (use Perplexity model names like `sonar-pro`)
* `messages` - Chat messages array
* `max_tokens` - Maximum tokens in response
* `stream` - Enable streaming responses
* `temperature` - Response randomness (0-2)
* `top_p` - Nucleus sampling parameter
* `response_format` - Response format specification

### Additional Perplexity Parameters

Sonar API supports additional search and response parameters:

* `search_domain_filter` - Limit or exclude specific domains
* `search_recency_filter` - Filter by content recency ("day", "week", "month", "year")
* `return_images` - Include image URLs in response
* `return_related_questions` - Include related questions
* `search_mode` - "web" (default) or "academic" mode selector
* `enable_search_classifier` - Let AI decide when to search
* `disable_search` - Turn off web search completely

<Info>
  See [Sonar API Reference](/api-reference/chat-completions-post) for complete parameter details.
</Info>

## Response Structure

Perplexity responses match OpenAI's format exactly, with additional fields:

### Standard OpenAI Fields

* `choices[0].message.content` - The AI-generated response
* `model` - The model name used
* `usage` - Token consumption details
* `id`, `created`, `object` - Standard response metadata

### Perplexity-Specific Fields

* `search_results` - Array of web sources with `title`, `url`, and `date`
* `citations` - Array of citation URLs referenced in the response

**Example Response:**

```json
{
  "id": "pplx-1234567890",
  "model": "sonar-pro",
  "created": 1234567890,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The latest developments in AI include..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 315,
    "total_tokens": 327
  },
  "search_results": [
    {
      "title": "Latest AI Developments",
      "url": "https://example.com/ai-news",
      "date": "2025-02-01"
    }
  ],
  "citations": [
    "https://example.com/ai-news"
  ]
}
```

## Best Practices

<Steps>
  <Step title="Use the correct base URL">
    Always use `https://api.perplexity.ai` for the Sonar API.

    ```python
    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai"  # Correct
    )
    ```
  </Step>

  <Step title="Handle errors gracefully">
    Use the OpenAI SDK's error handling:

    ```python theme={null}
    from openai import OpenAI, APIError, RateLimitError

    try:
        completion = client.chat.completions.create(...)
    except RateLimitError:
        print("Rate limit exceeded, please retry later")
    except APIError as e:
        print(f"API error: {e.message}")
    ```
  </Step>

  <Step title="Use streaming for better UX">
    Stream responses for real-time user experience:

    ```python theme={null}
    stream = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Long query..."}],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    ```
  </Step>

  <Step title="Access search results">
    Use the `search_results` field to get accurate source URLs:

    ```python theme={null}
    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Latest AI news"}]
    )

    # Access search results
    for result in completion.search_results:
        print(f"{result['title']}: {result['url']}")
    ```
  </Step>
</Steps>

## Recommended: Perplexity SDK

We recommend using Perplexity's native SDKs for the best developer experience:

* **Type safety** - Full TypeScript/Python type definitions for all parameters
* **Enhanced features** - Direct access to all Perplexity-specific features
* **Better error messages** - Perplexity-specific error handling
* **Simpler setup** - No need to configure base URLs

See the [Perplexity SDK Guide](/docs/sdk/overview) for details.

## Next Steps

<CardGroup>
  <Card title="Sonar Quickstart" icon="rocket" href="/docs/sonar/quickstart">
    Get started with Sonar API using OpenAI SDKs.
  </Card>

  <Card title="Sonar API Features" icon="book" href="/docs/sonar/features">
    Learn best practices for prompting and using the Sonar API.
  </Card>

  <Card title="API Reference" icon="code-circle" href="/api-reference/chat-completions-post">
    View complete API documentation for the Sonar endpoint.
  </Card>

  <Card title="Search Filters" icon="search" href="/docs/sonar/filters#search-control">
    Learn how to control search behavior with filters and parameters.
  </Card>
</CardGroup>
