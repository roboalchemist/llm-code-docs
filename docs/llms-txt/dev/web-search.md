# Source: https://dev.writer.com/home/web-search.md

# Source: https://dev.writer.com/api-reference/tool-api/web-search.md

# Source: https://dev.writer.com/api-reference/migration-guides/web-search.md

# Source: https://dev.writer.com/home/web-search.md

# Source: https://dev.writer.com/api-reference/tool-api/web-search.md

# Source: https://dev.writer.com/api-reference/migration-guides/web-search.md

# Source: https://dev.writer.com/home/web-search.md

# Source: https://dev.writer.com/api-reference/tool-api/web-search.md

# Source: https://dev.writer.com/api-reference/migration-guides/web-search.md

# Source: https://dev.writer.com/home/web-search.md

# Source: https://dev.writer.com/api-reference/tool-api/web-search.md

# Source: https://dev.writer.com/api-reference/migration-guides/web-search.md

# Migrate from web search API to web search tool

This guide shows you how to migrate from the deprecated [web search API endpoint](/api-reference/tool-api/web-search) to the [web search tool](/home/web-search-tool) in chat completions. After completing these steps, you can search the web using the web search tool, which provides the same capabilities within a chat completion workflow.

## Compare the APIs

The web search API and the web search tool provide similar search results, but the tool integrates web search into conversational workflows and requires specifying queries and configuration differently. The table below compares the two APIs.

| Aspect                | Web search API                                                                            | Web search tool                                                                                                                                                                                                                                                              |
| --------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Endpoint**          | `/v1/tools/web-search`                                                                    | `/v1/chat` with the prebuilt [web search tool](/home/web-search-tool) specification                                                                                                                                                                                          |
| **Request structure** | Pass search parameters such as `query`, `search_depth`, etc. directly in the request body | Provide the search query as part of the conversation `messages` and add the [web search tool](/home/web-search-tool) in the `tools` array. Additional parameters (like domains to include or exclude) are specified in the tool configuration, not as direct request fields. |
| **Response format**   | Results in `answer` and `sources` fields                                                  | Answer in `choices[0].message.content` and data in `web_search_data` field                                                                                                                                                                                                   |
| **Parameter control** | Explicit API parameters                                                                   | Most parameters specified in message prompt; only `include_domains` and `exclude_domains` as tool configuration                                                                                                                                                              |

## Migrate your code

The tabs below show a request using the web search API and the same request using the web search tool.

<Tabs>
  <Tab title="Before: Web search API">
    The web search API accepts search parameters directly in the request body. The following example shows an example request using the web search API. View the same request using the web search tool in the [after migrating](#after-migrating) section.

    <CodeGroup>
      ```bash cURL theme={null}
      curl --location 'https://api.writer.com/v1/tools/web-search' \
        --header 'Content-Type: application/json' \
        --header "Authorization: Bearer $WRITER_API_KEY" \
        --data '{
          "query": "What are the most significant developments in artificial intelligence this year?",
          "include_domains": ["wikipedia.org", "github.com"],
          "exclude_domains": ["quora.com"],
          "search_depth": "advanced",
          "max_results": 10
        }'
      ```

      ```python Python theme={null}
      from writerai import Writer

      # Initialize the Writer client. If you don't pass the `api_key` parameter,
      # the client looks for the `WRITER_API_KEY` environment variable.
      client = Writer()

      response = client.tools.web_search(
        query="What are the most significant developments in artificial intelligence this year?",
        include_domains=["wikipedia.org", "github.com"],
        exclude_domains=["quora.com"],
        search_depth="advanced",
        max_results=10
      )

      print(response.answer)
      ```

      ```javascript JavaScript theme={null}
      import { Writer } from "writer-sdk";

      // Initialize the Writer client. If you don't pass the `apiKey` parameter,
      // the client looks for the `WRITER_API_KEY` environment variable.
      const client = new Writer();

      const response = await client.tools.webSearch({
        query: "What are the most significant developments in artificial intelligence this year?",
        include_domains: ["wikipedia.org", "github.com"],
        exclude_domains: ["quora.com"],
        search_depth: "advanced",
        max_results: 10
      });

      console.log(response.answer);
      ```
    </CodeGroup>

    **Response:**

    ```json  theme={null}
    {
      "query": "What are the most significant developments in artificial intelligence this year?",
      "answer": "This year has seen several significant developments...",
      "sources": [
        {
          "url": "https://www.ibm.com/think/insights/artificial-intelligence-trends",
          "raw_content": null
        }
      ]
    }
    ```
  </Tab>

  <Tab title="After: Web search tool">
    The web search tool uses the chat completions endpoint with a web search tool specification. The model handles the search based on your message and tool configuration. Parameters like `search_depth` and `max_results` are now specified in the message prompt:

    <CodeGroup>
      ```bash cURL theme={null}
      curl --location 'https://api.writer.com/v1/chat' \
        --header 'Content-Type: application/json' \
        --header "Authorization: Bearer $WRITER_API_KEY" \
        --data '{
          "model": "palmyra-x5",
          "messages": [
            {
              "role": "user",
              "content": "What are the most significant developments in artificial intelligence this year? Use advanced search depth and limit to 10 results."
            }
          ],
          "tool_choice": "auto",
          "tools": [
            {
              "type": "web_search",
              "function": {
                "include_domains": ["wikipedia.org", "github.com"],
                "exclude_domains": ["quora.com"]
              }
            }
          ]
        }'
      ```

      ```python Python theme={null}
      from writerai import Writer

      # Initialize the Writer client. If you don't pass the `api_key` parameter,
      # the client looks for the `WRITER_API_KEY` environment variable.
      client = Writer()

      messages = [{"role": "user", "content": "What are the most significant developments in artificial intelligence this year? Use advanced search depth and limit to 10 results."}]

      tools = [{
        "type": "web_search",
        "function": {
          "include_domains": ["wikipedia.org", "github.com"],
          "exclude_domains": ["quora.com"]
        }
      }]

      response = client.chat.chat(
        model="palmyra-x5", 
        messages=messages, 
        tools=tools,
        tool_choice="auto"
      )

      print(response.choices[0].message.content)
      ```

      ```javascript JavaScript theme={null}
      import { Writer } from "writer-sdk";

      // Initialize the Writer client. If you don't pass the `apiKey` parameter,
      // the client looks for the `WRITER_API_KEY` environment variable.
      const client = new Writer();

      const messages = [{role: "user", content: "What are the most significant developments in artificial intelligence this year? Use advanced search depth and limit to 10 results."}];

      const tools = [{
        type: "web_search",
        function: {
          include_domains: ["wikipedia.org", "github.com"],
          exclude_domains: ["quora.com"]
        }
      }];

      const response = await client.chat.chat({
        model: "palmyra-x5", 
        messages: messages, 
        tools: tools,
        tool_choice: "auto"
      });

      console.log(response.choices[0].message.content);
      ```
    </CodeGroup>

    **Response:**

    ```json  theme={null}
    {
      "id": "2ac04514",
      "object": "chat.completion",
      "choices": [
        {
          "index": 0,
          "finish_reason": "tool_calls",
          "message": {
            "content": "The latest developments in AI technology are happening at a rapid pace...",
            "role": "assistant",
            "web_search_data": {
              "search_depth": "advanced",
              "sources": [
                {
                  "url": "https://en.wikipedia.org/wiki/AI_boom",
                  "raw_content": null
                }
              ]
            }
          }
        }
      ]
    }
    ```
  </Tab>
</Tabs>

## Map your parameters

The following table shows how web search API parameters map to the web search tool. To customize search behavior in the web search tool, include your requirements in the message prompt.

| Web search API        | Web search tool                                                                      |
| --------------------- | ------------------------------------------------------------------------------------ |
| `query`               | Include in the message `content` field                                               |
| `include_domains`     | `tools[0].function.include_domains`                                                  |
| `exclude_domains`     | `tools[0].function.exclude_domains`                                                  |
| `search_depth`        | Include in the message prompt (for example, "perform an advanced search")            |
| `max_results`         | Include in the message prompt (for example, "limit to 10 sources")                   |
| `time_range`          | Include in the message prompt (for example, "from the last week")                    |
| `include_raw_content` | Include in the message prompt (for example, "include raw source text")               |
| `topic`               | Include in the message prompt (for example, "search news articles")                  |
| `country`             | Include in the message prompt (for example, "localize results to the United States") |
| `chunks_per_source`   | Include in the message prompt (for example, "extract 3 text segments per source")    |

<Note>
  With the web search tool, most search parameters are specified in your message prompt rather than as separate API parameters. The model interprets your requirements and configures the search accordingly.

  Only `include_domains` and `exclude_domains` are available as tool configuration parameters.
</Note>

## Access search metadata

The web search tool response includes search metadata, including sources and raw text if requested, in the `web_search_data` field:

<CodeGroup>
  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  messages = [{"role": "user", "content": "What are the most significant developments in artificial intelligence this year? Use advanced search depth and limit to 10 results."}]

  tools = [{
    "type": "web_search",
    "function": {
      "include_domains": ["wikipedia.org", "github.com"],
      "exclude_domains": ["quora.com"]
    }
  }]

  response = client.chat.chat(
    model="palmyra-x5", 
    messages=messages, 
    tools=tools,
    tool_choice="auto"
  )

  # Get the search answer
  answer = response.choices[0].message.content

  # Get search metadata
  search_metadata = response.choices[0].message.web_search_data
  search_depth = search_metadata.search_depth
  sources = search_metadata.sources

  print(f"Answer: {answer}")
  print(f"Search depth: {search_depth}")
  print(f"Found {len(sources)} sources")

  for source in sources:
      print(f"- {source.url}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const messages = [{role: "user", content: "What are the most significant developments in artificial intelligence this year? Use advanced search depth and limit to 10 results."}];

  const tools = [{
    type: "web_search",
    function: {
      include_domains: ["wikipedia.org", "github.com"],
      exclude_domains: ["quora.com"]
    }
  }];

  const response = await client.chat.chat({
    model: "palmyra-x5", 
    messages: messages, 
    tools: tools,
    tool_choice: "auto"
  });

  // Get the search answer
  const answer = response.choices[0].message.content;

  // Get search metadata
  const searchMetadata = response.choices[0].message.web_search_data;
  const searchDepth = searchMetadata.search_depth;
  const sources = searchMetadata.sources;

  console.log(`Answer: ${answer}`);
  console.log(`Search depth: ${searchDepth}`);
  console.log(`Found ${sources.length} sources`);

  sources.forEach(source => {
    console.log(`- ${source.url}`);
  });
  ```
</CodeGroup>

## Explore related features

Learn more about the web search tool and related features:

* [Web search tool guide](/home/web-search-tool)
* [Chat completion guide](/home/chat-completion)
* [Other prebuilt tools](/home/tool-calling)
* [Streaming responses](/home/streaming)
