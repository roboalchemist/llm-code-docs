
# Agent API

Source: https://docs.perplexity.ai/docs/agent-api/quickstart

The Agent API is a multi-provider, interoperable API specification for building LLM applications. Access models from multiple providers with integrated real-time web search, tool configuration, reasoning control, and token budgets—all through one unified interface.

<Card title="Get your Perplexity API Key" icon="key" href="https://perplexity.ai/account/api">
  Navigate to the **API Keys** tab in the API Portal and generate a new key.
</Card>

## Why Use the Agent API?

<CardGroup>
  <Card title="Multi-Provider Access" icon="stack-3">
    Access OpenAI, Anthropic, Google, xAI, and more through one unified API, no need to manage multiple API keys.
  </Card>

  <Card title="Transparent Pricing" icon="receipt">
    See exact token counts and costs per request, no markup, just direct provider pricing.
  </Card>

  <Card title="Granular Control" icon="adjustments">
    Change models, reasoning, tokens, and tools with consistent syntax.
  </Card>
</CardGroup>

<Info>
  We recommend using our [official SDKs](/docs/sdk/overview) for a more convenient and type-safe way to interact with the Agent API.
</Info>

## Installation

Install the SDK for your preferred language:

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```bash

  ```bash Typescript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```bash
</CodeGroup>

## Authentication

Set your API key as an environment variable. The SDK will automatically read it:

<Tabs>
  <Tab title="macOS/Linux">
    ```bash theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```bash
  </Tab>

  <Tab title="Windows">
    ```powershell theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```bash
  </Tab>
</Tabs>

<Info>
  All SDK examples below automatically use the `PERPLEXITY_API_KEY` environment variable. You can also pass the key explicitly if needed.
</Info>

## Basic Usage

<Tip>
  **Convenience Property:** Both Python and Typescript SDKs provide an `output_text` property that aggregates all text content from response outputs. Instead of iterating through `response.output`, simply use `response.output_text` for cleaner code.
</Tip>

### Using a Third-Party Model

Use third-party models from OpenAI, Anthropic, Google, xAI, and other providers for specific capabilities:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Using a third-party model
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest developments in AI?",
      tools=[{"type": "web_search"}],
      instructions="You have access to a web_search tool. Use it for questions about current events, news, or recent developments. Use 1 query for simple questions. Keep queries brief: 2-5 words. NEVER ask permission to search - just search when appropriate",
  )

  print(f"Response ID: {response.id}")
  print(response.output_text)
  ```text

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest developments in AI?",
      tools: [{ type: "web_search" }],
      instructions: "You have access to a web_search tool. Use it for questions about current events.",
  });

  console.log(`Response ID: ${response.id}`);
  console.log(response.output_text);
  ```text

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest developments in AI?",
      "tools": [{"type": "web_search"}],
      "instructions": "You have access to a web_search tool. Use it for questions about current events.",
      "max_output_tokens": 1000
    }' | jq
  ```text
</CodeGroup>

### With Web Search Tool

Enable web search capabilities using the `web_search` tool:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What's the weather in San Francisco?",
      tools=[
          {
              "type": "web_search"
          }
      ],
      instructions="You have access to a web_search tool. Use it when you need current information.",
  )

  if response.status == "completed":
      print(response.output_text)
  ```text

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What's the weather in San Francisco?",
      tools: [
          {
              type: "web_search"
          }
      ],
      instructions: "You have access to a web_search tool. Use it when you need current information.",
  });

  if (response.status === "completed") {
      console.log(response.output_text);
  }
  ```text

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What'\''s the weather in San Francisco?",
      "tools": [{"type": "web_search"}],
      "instructions": "You have access to a web_search tool. Use it when you need current information."
    }' | jq
  ```text
</CodeGroup>

### Using a Preset

Presets provide optimized defaults for specific use cases. Start with a preset for quick setup:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Using a preset (e.g., pro-search)
  response = client.responses.create(
      preset="pro-search",
      input="What are the latest developments in AI?",
  )

  print(f"Response ID: {response.id}")
  print(response.output_text)
  ```text

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Using a preset
  const response = await client.responses.create({
      preset: "pro-search",
      input: "What are the latest developments in AI?",
  });

  console.log(`Response ID: ${response.id}`);
  console.log(response.output_text);
  ```text

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "preset": "pro-search",
      "input": "What are the latest developments in AI?"
    }' | jq
  ```text
</CodeGroup>

## Input Formats

The `input` parameter accepts either a string or an array of message objects.

### String Input

Simple string input for straightforward queries:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest AI developments?",
  )
  ```text

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest AI developments?",
  });
  ```text

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest AI developments?"
    }' | jq
  ```text
</CodeGroup>

### Message Array Input

Use message arrays for multi-turn conversations:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input=[
          {"type": "message", "role": "system", "content": "You are a helpful assistant."},
          {"type": "message", "role": "user", "content": "What are the latest AI developments?"},
      ],
      instructions="Provide detailed, well-researched answers.",
  )
  ```text

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: [
          { type: "message", role: "system", content: "You are a helpful assistant." },
          { type: "message", role: "user", content: "What are the latest AI developments?" },
      ],
      instructions: "Provide detailed, well-researched answers.",
  });
  ```text

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": [
        {"type": "message", "role": "system", "content": "You are a helpful assistant."},
        {"type": "message", "role": "user", "content": "What are the latest AI developments?"}
      ],
      "instructions": "Provide detailed, well-researched answers."
    }' | jq
  ```text
</CodeGroup>

## Instructions Parameter

The `instructions` parameter provides system instructions or guidelines for the model. This is particularly useful for:

* **Tool usage instructions**: Guide the model on when and how to use available tools
* **Response style guidelines**: Control the tone and format of responses
* **Behavior constraints**: Set boundaries and constraints for model behavior

**Example with tool instructions:**

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest developments in AI?",
      instructions="You have access to a web_search tool. Use it for questions about current events, news, or recent developments. Use 1 query for simple questions. Keep queries brief: 2-5 words. NEVER ask permission to search - just search when appropriate",
      tools=[{"type": "web_search"}],
  )
  ```text

  ```typescript Typescript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest developments in AI?",
      instructions: "You have access to a web_search tool. Use it for questions about current events, news, or recent developments. Use 1 query for simple questions. Keep queries brief: 2-5 words. NEVER ask permission to search - just search when appropriate",
      tools: [{ type: "web_search" }],
  });
  ```text

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest developments in AI?",
      "instructions": "You have access to a web_search tool. Use it for questions about current events, news, or recent developments. Use 1 query for simple questions. Keep queries brief: 2-5 words. NEVER ask permission to search - just search when appropriate",
      "tools": [{"type": "web_search"}]
    }' | jq
  ```text
</CodeGroup>

## Tools

The Agent API provides two powerful tools for accessing real-time web information:

* **`web_search`** - Performs web searches to retrieve current information and news
* **`fetch_url`** - Fetches and extracts content from specific URLs

The `web_search` tool can optionally include user location for localized results:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest news in San Francisco?",
      tools=[
          {
              "type": "web_search",
              "user_location": {
                  "latitude": 37.7749,
                  "longitude": -122.4194,
                  "country": "US",
                  "city": "San Francisco",
                  "region": "CA"
              }
          }
      ],
      instructions="Use web_search to find current information.",
  )
  ```text

  ```typescript Typescript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest news in San Francisco?",
      tools: [
          {
              type: "web_search",
              user_location: {
                  latitude: 37.7749,
                  longitude: -122.4194,
                  country: "US",
                  city: "San Francisco",
                  region: "CA"
              }
          }
      ],
      instructions: "Use web_search to find current information.",
  });
  ```text

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest news in San Francisco?",
      "tools": [
        {
          "type": "web_search",
          "user_location": {
            "latitude": 37.7749,
            "longitude": -122.4194,
            "country": "US",
            "city": "San Francisco",
            "region": "CA"
          }
        }
      ],
      "instructions": "Use web_search to find current information."
    }' | jq
  ```text
</CodeGroup>

## Generation Parameters

Control response generation with standard parameters:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Explain quantum computing",
      max_output_tokens=1000,  # Maximum tokens to generate
  )
  ```text

  ```typescript Typescript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Explain quantum computing",
      max_output_tokens: 1000,  // Maximum tokens to generate
  });
  ```text

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Explain quantum computing",
      "max_output_tokens": 1000,
    }' | jq
  ```text
</CodeGroup>

## Reasoning Effort

Control the reasoning effort level for reasoning models:

* **`low`**: Minimal reasoning effort
* **`medium`**: Moderate reasoning effort
* **`high`**: Maximum reasoning effort

<Info>
  The `reasoning` parameter is only supported by models with reasoning capabilities. Models without reasoning support will ignore this parameter.
</Info>

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Solve this complex problem step by step",
      reasoning={
          "effort": "high"  # Use maximum reasoning
      },
  )
  ```text

  ```typescript Typescript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Solve this complex problem step by step",
      reasoning: {
          effort: "high"  // Use maximum reasoning
      },
  });
  ```text

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Solve this complex problem step by step",
      "reasoning": {
        "effort": "high"
      }
    }' | jq
  ```text
</CodeGroup>

## Streaming Responses

The Agent API supports streaming responses using Server-Sent Events (SSE). Enable streaming by setting `stream=True`:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Explain quantum computing in detail",
      stream=True,
  )

  # Process streaming response
  for chunk in response:
      if chunk.type == "response.output_text.delta":
          print(chunk.delta, end="", flush=True)
      elif chunk.type == "response.completed":
          print(f"\n\nResponse completed: {chunk.response.output_text}")
  ```text

  ```typescript Typescript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Explain quantum computing in detail",
      stream: true,
  });

  // Process streaming response
  for await (const chunk of response) {
      if (chunk.type === "response.output_text.delta") {
          process.stdout.write(chunk.delta);
      } else if (chunk.type === "response.completed") {
          console.log(`\n\nResponse completed: ${chunk.response.output_text}`);
      }
  }
  ```text

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Explain quantum computing in detail",
      "stream": true
    }'
  ```text
</CodeGroup>

<Info>
  For comprehensive streaming documentation, see the [Streaming Guide](/docs/agent-api/output-control/streaming-responses).
</Info>

## Error Handling

Handle errors gracefully:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity, APIError

  try:
      response = client.responses.create(
          model="openai/gpt-5.2",
          input="What is AI?",
      )

      if response.status == "completed":
          print(response.output_text)
      elif response.status == "failed":
          if response.error:
              print(f"Error: {response.error.message}")

  except APIError as e:
      print(f"API Error: {e.message}")
      print(f"Status Code: {e.status_code}")
  ```text

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  try {
      const response = await client.responses.create({
          model: "openai/gpt-5.2",
          input: "What is AI?",
      });

      if (response.status === "completed") {
          console.log(response.output_text);
      } else if (response.status === "failed") {
          if (response.error) {
              console.error(`Error: ${response.error.message}`);
          }
      }
  } catch (error) {
      if (error instanceof Perplexity.APIError) {
          console.error(`API Error: ${error.message}`);
          console.error(`Status Code: ${error.status}`);
      }
  }
  ```text

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What is AI?"
    }' | jq
  ```text
</CodeGroup>

## Response Structure

<Accordion title="Response Structure Example">
  Responses from the Agent API have a structured format:

  ```json theme={null}

  {
    "created_at": 1770431423,
    "id": "resp_7ac471db-4e3c-4059-a52d-c4bd6dc7c42b",
    "model": "openai/gpt-5.2",
    "object": "response",
    "output": [
      {
        "content": [
          {
            "text": "AI (artificial intelligence) is the field of creating...",
            "type": "output_text"
          }
        ],
        "id": "msg_3416c756-f840-4ffa-b4ae-07ad2c122a5d",
        "role": "assistant",
        "status": "completed",
        "type": "message"
      }
    ],
    "status": "completed",
    "usage": {
      "cost": {
        "currency": "USD",
        "input_cost": 0.0001,
        "output_cost": 0.00148,
        "total_cost": 0.00158
      },
      "input_tokens": 59,
      "output_tokens": 106,
      "total_tokens": 165
    }
  }

  ```text
</Accordion>

## Next Steps

<CardGroup>
  <Card title="Model Fallback" icon="layers" href="/docs/agent-api/model-fallback">
    Specify multiple models for automatic failover and higher availability.
  </Card>

  <Card title="Presets" icon="settings" href="/docs/agent-api/presets">
    Explore available presets and their configurations.
  </Card>

  <Card title="Models" icon="brain" href="/docs/agent-api/models">
    Explore available presets and third-party models for the Agent API.
  </Card>

  <Card title="API Reference" icon="code-circle" href="/api-reference/responses-post">
    View complete endpoint documentation and parameters.
  </Card>

  <Card title="Structured Outputs" icon="code-circle" href="/docs/agent-api/output-control/structured-outputs">
    Generate formatted responses with JSON schema or regex.
  </Card>

  <Card title="Search API" icon="search" href="/docs/search/quickstart">
    Get raw search results with the Search API.
  </Card>
</CardGroup>

<Info>
  Need help? Check out our [community](https://community.perplexity.ai) for support and discussions with other developers.
</Info>
