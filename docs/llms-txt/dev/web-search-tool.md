# Source: https://dev.writer.com/home/web-search-tool.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web search in a chat

> Search the web for real-time information during chat completions. Enable models to access current news, facts, and up-to-date data.

The web search tool for chat completions allows you to search the web for current information during a conversation.

This guide explains how to use the web search tool in a chat completion and provides an example of how to use it.

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

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
                  "content": "What are the latest developments in AI technology?"
              }
          ],
          "tool_choice": "auto",
          "tools": [
              {
                  "type": "web_search",
                  "function": {
                      "include_domains": ["wikipedia.org", "github.com", "techcrunch.com"],
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

  # Create the tools array containing a web search tool
  tools = [{
      "type": "web_search",
      "function": {
          "include_domains": ["wikipedia.org", "github.com", "techcrunch.com"],
          "exclude_domains": ["quora.com"]
      }
  }]

  # Create the messages array containing a user message that prompts the model to use the web search tool
  messages = [{"role": "user", "content": "What are the latest developments in AI technology?"}]

  response = client.chat.chat(
      model="palmyra-x5", 
      messages=messages, 
      tools=tools,  # The tools array defined earlier.
      tool_choice="auto"
  )

  print(response.choices[0].message.content)
  ```

  ```js JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  // Create the tools array containing a web search tool
  tools = [{
      type: "web_search",
      function: {
          include_domains: ["wikipedia.org", "github.com", "techcrunch.com"],
          exclude_domains: ["quora.com"]
      }
  }]

  // Create the messages array containing a user message that prompts the model to use the web search tool
  const messages = [{role: "user", content: "What are the latest developments in AI technology?"}];

  const response = await client.chat.chat({
      model: "palmyra-x5", 
      messages: messages, 
      tools: tools, // The tools array defined earlier.
      tool_choice: "auto"
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Tool structure

The web search tool allows you to search the web during a [chat completion](/home/chat-completion).

<Tip>
  To customize search parameters like including raw source text, limiting the number of sources, or specifying time ranges, include these requirements **in your prompt** to the model. The model uses these parameters when making the web search call. For example, your message to the model might include:

  * "Include raw source text"
  * "Limit the number of sources to 5"
  * "Search for news articles from the last 30 days"

  Example:

  ```json  theme={null}
  "messages": [{
    "role": "user",
    "content": "Find the latest news about AI technology. Include raw source text and limit the number of sources to 5."
  }]
  ```
</Tip>

To use the web search tool, add it to the `tools` array in your `chat-completion` endpoint request.

The web search tool object has the following structure:

| Parameter                  | Type     | Description                                                     |
| -------------------------- | -------- | --------------------------------------------------------------- |
| `type`                     | `string` | The type of tool, which is `web_search` for the web search tool |
| `function`                 | `object` | An object containing the tool's configuration                   |
| `function.include_domains` | `array`  | An array of domains to include in the search results            |
| `function.exclude_domains` | `array`  | An array of domains to exclude from the search results          |

Below shows the structure of the web search tool object.

<CodeGroup>
  ```bash cURL theme={null}
  "tools": [
      {
          "type": "web_search",
          "function": {
              "include_domains": ["wikipedia.org", "github.com"],
              "exclude_domains": ["quora.com"]
          }
      }  
  ]
  ```

  ```python Python theme={null}
  tools = [{
      "type": "web_search",
      "function": {
          "include_domains": ["wikipedia.org", "github.com"],
          "exclude_domains": ["quora.com"]
      }
  }]
  ```

  ```js JavaScript theme={null}
  const tools = [{
      type: "web_search",
      function: {
          include_domains: ["wikipedia.org", "github.com"],
          exclude_domains: ["quora.com"]
      }
  }]
  ```
</CodeGroup>

<Note>
  You can only pass one prebuilt tool in the `tools` array at a time. However, you can pass multiple [custom tools](/home/tool-calling) in the same request.

  Prebuilt tools are:

  * Web search tool
  * [Knowledge Graph tool](/home/kg-chat)
  * [LLM tool](/home/model-delegation)
  * [Translation tool](/home/translation-tool)
  * [Vision tool](/home/vision-tool)
</Note>

### Response format

For non-streaming responses, the search results and answer are in the `choices[0].message.content` field. For streaming responses, the search results and answer are in the `choices[0].delta.content` field.

The response also contains a `web_search_data` field that contains the following information:

| Parameter               | Type     | Description                                    |
| ----------------------- | -------- | ---------------------------------------------- |
| `query`                 | `string` | The search query that was submitted            |
| `answer`                | `string` | Generated answer based on the search results   |
| `sources`               | `array`  | The search results found                       |
| `sources[].url`         | `string` | URL of the search result                       |
| `sources[].raw_content` | `string` | Raw content from the source URL (if requested) |

<Warning>
  You can use the web search tool with streaming chat responses, but the web search tool call is not streamed. The sources comes back in the `choices[0].delta.content` field once the full search is complete. Then, the response from the model is streamed.

  If you are unfamiliar with the chat completions endpoint or streaming vs. non-streaming responses, learn more in the [chat completion guide](/home/chat-completion).
</Warning>

See the [chat completion endpoint](/api-reference/completion-api/chat-completion#response-id) for more information on the response fields.

<CodeGroup>
  ```json non-streaming response [expandable] theme={null}
  {
    "id": "2ac04514-35cd-49e7-8d11-df0ace4336db",
    "object": "chat.completion",
    "choices": [
      {
        "index": 0,
        "finish_reason": "tool_calls",
        "message": {
          "content": "The latest developments in AI technology are happening at a rapid pace...",
          "role": "assistant",
          "tool_calls": null,
          "graph_data": {
            "sources": null,
            "status": null,
            "subqueries": null
          },
          "llm_data": null,
          "image_data": null,
          "translation_data": null,
          "web_search_data": {
            "search_depth": "advanced",
            "sources": [
              {
                "url": "https://en.wikipedia.org/wiki/AI_boom",
                "raw_content": null
              },
              {
                "url": "https://techcrunch.com/2025/05/30/its-not-your-imagination-ai-is-speeding-up-the-pace-of-change/",
                "raw_content": null
              },
              {
                "url": "https://techcrunch.com/category/artificial-intelligence/",
                "raw_content": null
              },
              {
                "url": "https://techcrunch.com/2025/08/03/inside-openais-quest-to-make-ai-do-anything-for-you/",
                "raw_content": null
              },
              {
                "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
                "raw_content": null
              }
            ]
          },
          "refusal": null
        },
        "logprobs": null,
        "trace_details": null
      }
    ],
    "created": 1754521236,
    "model": "palmyra-x5",
    "usage": {
      "prompt_tokens": 3736,
      "total_tokens": 3764,
      "completion_tokens": 28,
      "completion_tokens_details": null,
      "prompt_token_details": null
    },
    "system_fingerprint": "v1",
    "service_tier": null
  }
  ```

  ```json streaming response [expandable] theme={null}
  {
    "id": "94131ba5-35f0-4319-b4a6-3929ebb1669a",
    "choices": [
      {
        "delta": {
          "content": "",
          "graph_data": {
            "sources": null,
            "status": null,
            "subqueries": null
          },
          "llm_data": null,
          "refusal": null,
          "role": "assistant",
          "tool_calls": null,
          "translation_data": null,
          "image_data": null,
          "web_search_data": {
            "search_depth": "advanced",
            "sources": [
              {
                "url": "https://en.wikipedia.org/wiki/AI_boom",
                "raw_content": null
              },
              {
                "url": "https://techcrunch.com/2025/05/12/improvements-in-reasoning-ai-models-may-slow-down-soon-analysis-finds/",
                "raw_content": null
              },
              {
                "url": "https://techcrunch.com/category/artificial-intelligence/",
                "raw_content": null
              },
              {
                "url": "https://en.wikipedia.org/wiki/Progress_in_artificial_intelligence",
                "raw_content": null
              }
            ]
          }
        },
        "finish_reason": null,
        "index": 0,
        "logprobs": null,
        "message": {
          "content": "",
          "refusal": null,
          "role": "assistant",
          "graph_data": {
            "sources": null,
            "status": null,
            "subqueries": null
          },
          "llm_data": null,
          "tool_calls": null,
          "translation_data": null,
          "image_data": null,
          "web_search_data": {
            "search_depth": "advanced",
            "sources": [
              {
                "url": "https://en.wikipedia.org/wiki/AI_boom",
                "raw_content": null
              },
              {
                "url": "https://techcrunch.com/2025/05/12/improvements-in-reasoning-ai-models-may-slow-down-soon-analysis-finds/",
                "raw_content": null
              },
              {
                "url": "https://techcrunch.com/category/artificial-intelligence/",
                "raw_content": null
              },
              {
                "url": "https://en.wikipedia.org/wiki/Progress_in_artificial_intelligence",
                "raw_content": null
              }
            ]
          }
        },
        "trace_details": null
      }
    ],
    "created": 1754521528,
    "model": "palmyra-x5",
    "object": "chat.completion.chunk",
    "service_tier": null,
    "system_fingerprint": "v1",
    "usage": null
  }
  ```
</CodeGroup>

## Usage example

This example uses the web search tool to find current information about AI developments during a chat completion.

To use the web search tool:

1. Create a `tools` array that specifies the web search tool.

* The tool array should include the `type` and `function` parameters. The `function` parameter should include the `include_domains` and `exclude_domains` parameters.

2. Create a `messages` array that contains the user message that prompts the model to use the web search tool.

* The message should contain the requirements for the search, such as including raw source text, limiting the number of sources, or specifying time ranges.

3. Call the `chat.chat` method with the `tools` parameter set to the `tools` array and `tool_choice` set to `auto`.

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
                  "content": "What are the latest developments in AI technology?"
              }
          ],
          "tool_choice": "auto",
          "tools": [
              {
                  "type": "web_search",
                  "function": {
                      "include_domains": ["wikipedia.org", "github.com", "techcrunch.com"],
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

  messages = [{"role": "user", "content": "What are the latest developments in AI technology?"}]

  response = client.chat.chat(
      model="palmyra-x5", 
      messages=messages, 
      tools=tools,  # The tools array defined earlier.
      tool_choice="auto"
  )

  print(response.choices[0].message.content)
  ```

  ```js JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const messages = [{role: "user", content: "What are the latest developments in AI technology?"}];

  const response = await client.chat.chat({
      model: "palmyra-x5", 
      messages: messages, 
      tools: tools, // The tools array defined earlier.
      tool_choice: "auto"
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

If you want to verify the web search data in the response, you can print the `web_search_data` field to see the search query, answer, and sources that the web search tool used.

<CodeGroup>
  ```python Python theme={null}
  print(response.choices[0].message.web_search_data)
  ```

  ```js JavaScript theme={null}
  console.log(response.choices[0].message.web_search_data);
  ```
</CodeGroup>

By following this guide, you can use the web search tool to have the model search the web for current information during a chat completion.

## Next steps

Learn more about the prebuilt tools available for chat completions:

* [Knowledge Graph tool](/home/kg-chat)
* [LLM tool](/home/model-delegation)
* [Translation tool](/home/translation-tool)
* [Vision tool](/home/vision-tool)
