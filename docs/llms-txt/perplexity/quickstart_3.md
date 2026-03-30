# Source: https://docs.perplexity.ai/docs/getting-started/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Generate an API key and make your first call in < 3 minutes.

## Generating an API Key

<Card title="Get your Perplexity API Key" icon="key" arrow="True" horizontal="True" iconType="solid" cta="Click here" href="https://console.perplexity.ai">
  Navigate to the **API Keys** tab in the API Portal and generate a new key.
</Card>

<Info>
  See the [API Groups](/docs/getting-started/api-groups) page to learn more about API groups.
</Info>

## Overview

The Perplexity API provides four core APIs for different use cases: **Agent API** for accessing OpenAI, Anthropic, Google, and xAI models with unified search tools and transparent pricing, **Search** for ranked web search results, **Sonar** for web-grounded AI responses with Sonar models, and **Embeddings** for generating text embeddings.

All APIs support both REST and SDK access with streaming, filtering, and advanced controls.

## Available APIs

<CardGroup cols={2}>
  <Card title="Agent API" icon="code-circle" href="/docs/agent-api/quickstart">
    Third-party models from OpenAI, Anthropic, Google, and more with presets and web search tools.
  </Card>

  <Card title="Search" icon="search" href="/docs/search/quickstart">
    Ranked web search results with filtering, multi-query support, and domain controls.
  </Card>

  <Card title="Sonar" icon="message" href="/docs/sonar/quickstart">
    Web-grounded AI responses with citations, conversation context, and streaming support.
  </Card>

  <Card title="Embeddings" icon="cube" href="/docs/embeddings/quickstart">
    Generate high-quality text embeddings for semantic search and RAG.
  </Card>
</CardGroup>

## Choosing the Right API

<AccordionGroup>
  <Accordion title="Use the Agent API when..." icon="code-circle">
    * You need **multi-provider access** to OpenAI, Anthropic, Google, and more models through one API
    * You want **granular control** over model selection, reasoning, token budgets, and tools
    * You want **presets** for common use configurations or full customization for advanced workflows

    **Best for:** Agentic workflows, custom AI applications, multi-model experimentation
  </Accordion>

  <Accordion title="Use the Search API when..." icon="search">
    * You need **raw search results** without LLM processing
    * You want to **build custom AI workflows** with your own models
    * You need **search data** for indexing, analysis, or training

    **Best for:** Custom AI pipelines, data collection, search integration
  </Accordion>

  <Accordion title="Use the Sonar API when..." icon="message">
    * You want **Perplexity's Sonar models** optimized for research and Q\&A
    * You need **built-in citations** and conversation context
    * You prefer **simplicity**—just send a message and get a researched answer

    **Best for:** AI assistants, research tools, Q\&A applications
  </Accordion>
</AccordionGroup>

## Installation

Install the SDK for your preferred language:

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```

  ```bash Typescript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```
</CodeGroup>

## Authentication

Set your API key as an environment variable:

<Tabs>
  <Tab title="macOS/Linux">
    ```bash  theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell  theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```
  </Tab>
</Tabs>

<Note>
  **OpenAI SDK Compatible:** Perplexity's API supports the OpenAI Chat Completions format. You can use OpenAI client libraries by pointing to our endpoint. See the [OpenAI Compatibility Guide](/docs/agent-api/openai-compatibility) for examples.
</Note>

## Making Your First API Call

Choose your API based on your use case:

<Tabs>
  <Tab title="Agent API">
    Use for third-party models with web search tools and presets:

    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      # Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      client = Perplexity()

      # Make the API call with a preset
      response = client.responses.create(
          preset="pro-search",
          input="What are the key differences between the latest iPhone and Samsung Galaxy flagship phones released this year?",
      )

      # Print the AI's response
      print(response.output_text)
      ```

      ```typescript Typescript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      // Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      const client = new Perplexity();

      // Make the API call with a preset
      const response = await client.responses.create({
          preset: "pro-search",
          input: "What are the key differences between the latest iPhone and Samsung Galaxy flagship phones released this year?",
      });

      // Print the AI's response
      console.log(response.output_text);
      ```

      ```bash cURL theme={null}
      curl https://api.perplexity.ai/v1/agent \
        -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "preset": "pro-search",
          "input": "What are the key differences between the latest iPhone and Samsung Galaxy flagship phones released this year?"
        }' | jq
      ```
    </CodeGroup>

    <Accordion title="Example Response">
      The response includes structured output with tool usage and citations:

      ```json  theme={null}
      {
        "background": false,
        "completed_at": 1756485272,
        "created_at": 1756485272,
        "error": null,
        "frequency_penalty": 0,
        "id": "resp_1234567890",
        "incomplete_details": null,
        "instructions": "## Abstract\n<role>\nYou are an AI assistant developed by Perplexity AI. Given a user's query, your goal is to...",
        "max_output_tokens": null,
        "max_tool_calls": null,
        "metadata": {},
        "model": "openai/gpt-5.1",
        "object": "response",
        "output": [
          {
            "type": "message",
            "id": "msg_abc123",
            "role": "assistant",
            "status": "completed",
            "content": [
              {
                "type": "output_text",
                "text": "Recent developments in AI include...",
                "annotations": [
                  {
                    "type": "citation",
                    "url": "https://example.com/article1"
                  }
                ],
                "logprobs": []
              }
            ]
          }
        ],
        "parallel_tool_calls": true,
        "presence_penalty": 0,
        "previous_response_id": null,
        "prompt_cache_key": null,
        "reasoning": null,
        "safety_identifier": null,
        "service_tier": "default",
        "status": "completed",
        "store": true,
        "temperature": 1,
        "text": {
          "format": {
            "type": "text"
          }
        },
        "tool_choice": "auto",
        "tools": [
          {
            "type": "web_search"
          },
          {
            "type": "fetch_url"
          }
        ],
        "top_logprobs": 0,
        "top_p": 1,
        "truncation": "disabled",
        "usage": {
          "cost": {
            "currency": "USD",
            "input_cost": 0.0046,
            "output_cost": 0.0078,
            "tool_calls_cost": 0.005,
            "total_cost": 0.0174
          },
          "input_tokens": 3681,
          "input_tokens_details": {
            "cached_tokens": 0
          },
          "output_tokens": 780,
          "output_tokens_details": {
            "reasoning_tokens": 0
          },
          "tool_calls_details": {
            "search_web": {
              "invocation": 1
            }
          },
          "total_tokens": 4461
        },
        "user": null
      }
      ```
    </Accordion>
  </Tab>

  <Tab title="Search API">
    Use for ranked web search results without LLM processing:

    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      # Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      client = Perplexity()

      # Make the API call
      search = client.search.create(
          query="SpaceX Starship launch updates 2026",
          max_results=5
      )

      # Print the search results
      for result in search.results:
          print(f"{result.title}: {result.url}")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      // Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      const client = new Perplexity();

      // Make the API call
      const search = await client.search.create({
          query: "SpaceX Starship launch updates 2026",
          max_results: 5
      });

      // Print the search results
      for (const result of search.results) {
          console.log(`${result.title}: ${result.url}`);
      }
      ```

      ```bash cURL theme={null}
      curl -X POST 'https://api.perplexity.ai/search' \
        -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "query": "SpaceX Starship launch updates 2026",
          "max_results": 5
        }' | jq
      ```
    </CodeGroup>

    <Accordion title="Example Response">
      The response includes ranked search results with titles, URLs, and snippets:

      ```json  theme={null}
      {
        "results": [
          {
            "title": "SpaceX Starship Flight 10: Full Mission Recap",
            "url": "https://example.com/starship-flight-10",
            "snippet": "SpaceX successfully completed its tenth Starship test flight, achieving full booster recovery and orbital insertion...",
            "date": "2026-02-20",
            "last_updated": "2026-02-21"
          },
          {
            "title": "Starship Launch Manifest: 2026 Schedule and Updates",
            "url": "https://example.com/starship-2026-schedule",
            "snippet": "SpaceX has announced an ambitious 2026 launch manifest for Starship, targeting monthly flights and the first cargo mission...",
            "date": "2026-01-15",
            "last_updated": "2026-03-01"
          }
        ],
        "query_info": {
          "query": "SpaceX Starship launch updates 2026",
          "normalized_query": "spacex starship launch updates 2026"
        }
      }
      ```
    </Accordion>
  </Tab>

  <Tab title="Sonar API">
    Use for web-grounded AI responses with Perplexity's Sonar models:

    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      # Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      client = Perplexity()

      # Make the API call
      completion = client.chat.completions.create(
          model="sonar-pro",
          messages=[
              {"role": "user", "content": "What breakthroughs in fusion energy have been announced this year?"}
          ]
      )

      # Print the AI's response
      print(completion.choices[0].message.content)
      ```

      ```typescript Typescript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      // Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      const client = new Perplexity();

      // Make the API call
      const completion = await client.chat.completions.create({
          model: "sonar-pro",
          messages: [
              { role: "user", content: "What breakthroughs in fusion energy have been announced this year?" }
          ]
      });

      // Print the AI's response
      console.log(completion.choices[0].message.content);
      ```

      ```bash cURL theme={null}
      curl https://api.perplexity.ai/v1/sonar \
        -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "sonar-pro",
          "messages": [
            {
              "role": "user",
              "content": "What breakthroughs in fusion energy have been announced this year?"
            }
          ]
        }' | jq
      ```
    </CodeGroup>

    <Accordion title="Example Response">
      The response includes the AI's answer with citations and search results:

      ```json  theme={null}
      {
        "id": "66f3900f-e32e-4d59-b677-1a55de188262",
        "model": "sonar-pro",
        "created": 1756485272,
        "object": "chat.completion",
        "choices": [
          {
            "index": 0,
            "finish_reason": "stop",
            "message": {
              "role": "assistant",
              "content": "Several notable breakthroughs in fusion energy have been announced this year...[1][2]"
            }
          }
        ],
        "usage": {
          "prompt_tokens": 12,
          "completion_tokens": 315,
          "total_tokens": 327
        },
        "citations": [
          "https://example.com/article1",
          "https://example.com/article2"
        ]
      }
      ```
    </Accordion>
  </Tab>
</Tabs>

## Streaming Responses

Enable streaming for real-time output with either API:

<Tabs>
  <Tab title="Agent API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      # Make the streaming API call
      stream = client.responses.create(
          preset="pro-search",
          input="What are the most promising quantum computing startups and their recent funding rounds?",
          stream=True
      )

      # Process the streaming response
      for chunk in stream:
          if chunk.type == "response.output_text.delta":
              print(chunk.delta, end="", flush=True)
      ```

      ```typescript Typescript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      // Make the streaming API call
      const stream = await client.responses.create({
          preset: "pro-search",
          input: "What are the most promising quantum computing startups and their recent funding rounds?",
          stream: true
      });

      // Process the streaming response
      for await (const chunk of stream) {
          if (chunk.type === "response.output_text.delta") {
              process.stdout.write((chunk as any).delta);
          }
      }
      ```

      ```bash cURL theme={null}
      curl https://api.perplexity.ai/v1/agent \
        -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "preset": "pro-search",
          "input": "What are the most promising quantum computing startups and their recent funding rounds?",
          "stream": true
        }'
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Sonar API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity

      client = Perplexity()

      # Make the streaming API call
      stream = client.chat.completions.create(
          model="sonar-pro",
          messages=[
              {"role": "user", "content": "What are the most promising quantum computing startups and their recent funding rounds?"}
          ],
          stream=True
      )

      # Process the streaming response
      for chunk in stream:
          if chunk.choices[0].delta.content:
              print(chunk.choices[0].delta.content, end="")
      ```

      ```typescript Typescript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      // Make the streaming API call
      const stream = await client.chat.completions.create({
          model: "sonar-pro",
          messages: [
              { role: "user", content: "What are the most promising quantum computing startups and their recent funding rounds?" }
          ],
          stream: true
      });

      // Process the streaming response
      for await (const chunk of stream) {
          if (chunk.choices[0]?.delta?.content) {
              process.stdout.write((chunk.choices[0]?.delta?.content ?? '') as string);
          }
      }
      ```

      ```bash cURL theme={null}
      curl https://api.perplexity.ai/v1/sonar \
        -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "sonar-pro",
          "messages": [
            {
              "role": "user",
              "content": "What are the most promising quantum computing startups and their recent funding rounds?"
            }
          ],
          "stream": true
        }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<Info title="Complete Streaming Guide" href="/docs/agent-api/output-control/streaming-responses">
  For a full guide on streaming, including parsing, error handling, citation management, and best practices, see our [streaming guide](/docs/agent-api/output-control/streaming-responses).
</Info>

## Next Steps

Now that you've made your first API call, explore each API in depth:

<CardGroup cols={3}>
  <Card title="Agent API" icon="code-circle" href="/docs/agent-api/quickstart">
    Get started with third-party models and presets
  </Card>

  <Card title="Search API" icon="search" href="/docs/search/quickstart">
    Get started with web search results
  </Card>

  <Card title="Sonar API" icon="message" href="/docs/sonar/quickstart">
    Get started with web-grounded AI responses
  </Card>

  <Card title="Embeddings API" icon="cube" href="/docs/embeddings/quickstart">
    Get started with text embeddings
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Perplexity SDK" icon="book" href="/docs/sdk/overview">
    Learn about the official Perplexity SDK with type safety and async support
  </Card>

  <Card title="Models" icon="brain" href="/docs/sonar/models">
    Explore available models and their capabilities
  </Card>

  <Card title="API Reference" icon="file-code" href="/api-reference/sonar-post">
    View complete API documentation with detailed endpoint specifications
  </Card>

  <Card title="Examples" icon="player-play" href="/docs/cookbook/index">
    Explore code examples, tutorials, and integration patterns
  </Card>
</CardGroup>

<Info>
  Need help? Check out our [community](https://community.perplexity.ai) for support and discussions with other developers.
</Info>


Built with [Mintlify](https://mintlify.com).